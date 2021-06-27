import numpy as np

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

