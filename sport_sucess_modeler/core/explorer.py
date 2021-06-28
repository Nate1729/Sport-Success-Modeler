import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def covariance(arr, rowvar=True, sample=True):
	if rowvar:
		dim = arr.shape[1]

		arr_out = np.zeros((dim, dim))
		for i in range(dim):
			j = 0
			while j <= i:
				vec_mean = arr_out.mean(axis=0)
				arr_out[i, j] = ((arr[:, i] - vec_mean[i])*(arr[:, j] - vec_mean[j])).sum()
				arr_out[j, i] = arr_out[i, j]
				j += 1

	if sample:	
		arr_out /= dim - 1
	else:
		arr_out /= dim

	return arr_out

def cov_heatmap(df, title=None):
	cov = df.cov()	

	fig, ax = plt.subplots()
	im = ax.imshow(cov)

	# Configure axes
	ax.set_xticks(np.arange(len(labels)))
	ax.set_yticks(np.arange(len(labels)))
	# Label Axes
	ax.set_xticklabels(labels)
	ax.set_yticklabels(labels)
	# Create color bar
	cbar = ax.figure.colorbar(im, ax=ax)
	# Set title
	plt.title(title)
	# Full size figure
	fig.tight_layout()

	plt.show()

X = np.random.rand(5,5)
labels = ['one', 'two', 'three', 'four', 'five']
labels = pd.Index(labels)
df = pd.DataFrame(X, columns=labels)
cov_heatmap(df, 'Example Covariance Heatmap')