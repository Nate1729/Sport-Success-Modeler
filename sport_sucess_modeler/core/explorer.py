import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class Explore:

	def __init__(self, df_inputs, title):
		self.inputs = df_inputs
		self.title = title

	def heatmap(self):
		cov = self.inputs.cov()
		labels = self.inputs.columns

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
		plt.title(self.title)
		# Full size figure
		fig.tight_layout()

		plt.show()

	def svd_energy(self):
		array = self.df.to_numpy()

		# Column wise centering
		array = array - array.mean(axis=1)

		_, S, _ = np.linalg.svd(array, full_matrices=False)

		plt.subplots(121)
		plt.semilogy(S)
		plt.ylabel('Signular Values')
		plt.xlabel('k')
		plt.grid()

		plt.subplots(122)
		plt.plot(S.cumsum()/S.sum())
		plt.ylabel('Cumulative Sum')
		plt.xlabel('k')
		plt.grid()

		plt.tight_layout()
		plt.savefig(f'svd_Energy_{self.title}', dpi=800)


