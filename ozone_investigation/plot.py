import matplotlib.pyplot as plt
import cartopy.crs as ccrs


def plot_world(data):
    """Plots given xarray data over earth projection"""
    data_to_plot = data.T
    ax = plt.axes(projection=ccrs.EqualEarth())  # map projection
    data_to_plot.plot(ax=ax, transform=ccrs.PlateCarree())
    ax.coastlines()
    ax.gridlines()  # Add gridlines and coastlines to the plot


def singleplot(data, title):
    """Plots a single given plot"""
    plot_world(data)
    plt.title(title)
    plt.show()


def multiplot(data_list, attribute):
    """Plots a several given plots.
    The original plan was to plot several plots in one figure.
    This does not work at the moment, but may be a challenge
    for the future."""
    for d in range(len(data_list)):
        obj = {}
        # obj["p"+str(d)]=plt.subplot(411+d)#plt.figure(d)
        obj["p" + str(d)] = plt.figure(d)
        plot_world(data_list[d].altitude_of_interest)
        obj["p" + str(d)].suptitle(data_list[d].attrs[attribute])
    plt.show()

def plot_vertical_multiplot(data_list, title_list):
    """Creates a multiplot with vertical profiles from
    a list of xarrays"""
    nr_of_plots = len(data_list)
    fig, axis = plt.subplots(nr_of_plots, 1, sharex=True, figsize=(10, 2*nr_of_plots))
    for nr in range(nr_of_plots):
        data_list[nr]["ozone"].T.plot(ax=axis[nr])
        axis[nr].set_title(title_list[nr], loc="left")
    fig.suptitle("Vertical profiles of ozone concentration")
    #fig.tight_layout()
    plt.show()


def plot_timeseries(data, title):
    """plots timeseries data"""
    data.plot()
    plt.grid()
    plt.title(title)
    plt.show()
