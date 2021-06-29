import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



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