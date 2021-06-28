import numpy as np
import pandas as pd


def model_regression_linear(df, metric='wins', train_pt=90):
	"""
	Generate a linear regression model from a pandas DataFrame.
	This uses SVD to compute the model

	Inputs
	------
	df : DataFrame
		columns are different parameters
	metric : string
		the column in df that you want the model to predict
	train_pt : int (0, 100]
		What percent of the dat to use for training
	"""
	cols = df.columns
	cols = cols.remove('metric')
	# Transform data into numpy arrays
	b = df[metric].to_numpy()
	A = df.drop(metric).to_numpy()

	# Seperating data into Training and Test sets
	data_size = A.shape[0]
	train_index = int(data_size*train_pt/100)
	b_train = b[0:train_index]
	b_test = b[train_index + 1:data_size]
	A_train = A[0:train_index, :]
	A_test = A[train_index + 1:, :]
	del A, b
	
	# Calcuate SVD
	U, S, VT = np.linalg.svd(A_train, full_matricies=0)

	# Solve the equation
	x = VT.T @ np.linalg.inv(np.linalg.diag(S)) @ U.T @ b_train
	
	# Put the weights in a DataFrame
	df_weights = pd.DataFrame(x, cols)
	return df_weights

	