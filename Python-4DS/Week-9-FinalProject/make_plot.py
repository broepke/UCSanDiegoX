# This script was produced by glue and can be used to further customize a
# particular plot.

### Package imports

from glue.core.state import load
import matplotlib.pyplot as plt

### Set up data

data_collection = load('make_plot.py.data')

### Set up viewer

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, aspect='auto')

### Set up layers

## Layer 1: winemag-data_first150k

layer_data = data_collection[0]

# Get main data values
x = layer_data['price']
y = layer_data['points']

ax.plot(x, y, 'o', color='#595959', markersize=6, alpha=0.8, zorder=1, mec='none')

### Finalize viewer

# Set limits
ax.set_xlim(-26.12, 787.12)
ax.set_ylim(79.2, 100.8)

# Set scale (log or linear)
ax.set_xscale('linear')
ax.set_yscale('linear')

# Set axis label properties
ax.set_xlabel('Price', weight='normal', size=11)
ax.set_ylabel('Points', weight='normal', size=11)

# Set tick label properties
ax.tick_params('x', labelsize=9)
ax.tick_params('y', labelsize=9)

# Save figure
fig.savefig('glue_plot.png')
plt.close(fig)