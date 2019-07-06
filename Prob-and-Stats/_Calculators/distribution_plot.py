import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

samples = np.random.normal(size=40000)

bins = np.linspace(-4, 4, 40)
histogram, bins = np.histogram(samples, bins=bins, normed=True)

bin_centers = 0.5 * (bins[1:] + bins[:-1])

pdf = stats.norm.pdf(bin_centers)
cdf = stats.norm.cdf(bin_centers)

plt.figure(figsize=(7, 7))
plt.plot(bin_centers, histogram, label="Histogram of Random Variables")
plt.plot(bin_centers, pdf, label="PDF")
plt.plot(bin_centers, cdf, label="CDF")
plt.legend()
plt.show()
