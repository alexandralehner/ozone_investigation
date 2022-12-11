import matplotlib.pyplot as plt
import cartopy
import cartopy.crs as ccrs

def plot_world(data):
    data_to_plot = data.T
    ax = plt.axes(projection=ccrs.EqualEarth())  # map projection
    data_to_plot.plot(ax=ax, transform=ccrs.PlateCarree())
    ax.coastlines()
    ax.gridlines()  # Add gridlines and coastlines to the plot

def singleplot(data, title):
        plot_world(data)
        plt.title(title)
        plt.show()
def multiplot(data_list, attribute):

    for d in range(len(data_list)):
        obj={}
        #obj["p"+str(d)]=plt.subplot(411+d)#plt.figure(d)
        obj["p" + str(d)] = plt.figure(d)
        plot_world(data_list[d].altitude_of_interest)
        obj["p"+str(d)].suptitle(data_list[d].attrs[attribute])
    plt.show()

def plot_vertical(data_list):

    for d in data_list:
        d["ozone"].T.plot()
    #plt.plot(data_list[0].altitude)
        plt.show()
def plot_timeseries(data, title):
    data.plot()
    plt.grid()
    plt.title(title)
    plt.show()