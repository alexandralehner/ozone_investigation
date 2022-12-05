import matplotlib.pyplot as plt
# import cartopy
import cartopy.crs as ccrs


def plot_world(data, time_point):
    data_to_plot = data.sel(time=time_point)
    ax = plt.axes(projection=ccrs.EqualEarth())  # map projection
    data_to_plot.plot(ax=ax, transform=ccrs.PlateCarree())
    ax.coastlines()
    ax.gridlines()  # Add gridlines and coastlines to the plot
    plt.show()
