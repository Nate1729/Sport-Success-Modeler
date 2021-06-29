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
