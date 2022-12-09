import matplotlib.pyplot as plt
import cartopy
import cartopy.crs as ccrs


def plot_world(data):

    print("plotting")

    data_to_plot = data.T

    ax = plt.axes(projection=ccrs.EqualEarth())  # map projection
    data_to_plot.plot(ax=ax, transform=ccrs.PlateCarree())
    ax.coastlines()
    ax.gridlines()  # Add gridlines and coastlines to the plot
    plt.show()
