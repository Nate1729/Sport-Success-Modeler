import numpy as np
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

def cov_heatmap(arr, labels, rowvar=True, sample=True):
	if rowvar:
		arr_cov = covariance(arr)
	else:
		pass

	fig, ax = plt.subplots()
	im = ax.imshow(arr)

	# Configure axes
	ax.set_xticks(np.arange(len(labels)))
	ax.set_yticks(np.arange(len(labels)))
	# Label Axes
	ax.set_xticklabels(labels)
	ax.set_yticklabels(labels)
	# Create color bar
	cbar = ax.figure.colorbar(im, ax=ax)

	fig.tight_layout()

	plt.show()

X = np.random.rand(5,5)
cov_heatmap(X, ['one', 'two', 'three', 'four', 'five'])