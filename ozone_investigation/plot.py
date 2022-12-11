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

    #fig, axs = plt.subplots(nrows=len(data_list), ncols=1)
    #plt.figure(1)

    #fig, [(p1, p2), (p3, p4)] = plt.subplots(nrows=2, ncols=2)

    for d in range(len(data_list)):
        obj={}
        #obj["p"+str(d)]=plt.subplot(411+d)#plt.figure(d)
        obj["p" + str(d)] = plt.figure(d)
        plot_world(data_list[d].altitude_of_interest)
        obj["p"+str(d)].suptitle(data_list[d].attrs[attribute])


        #obj={}
        #obj["p"+str(d)] = plt.axes(projection=ccrs.EqualEarth())
        #data_list[d].altitude_of_interest.T.plot(ax=p1, transform=ccrs.PlateCarree())
        #p1.coastlines()
        #p1.gridlines()
        #p1.set_title(data_list[d].attrs[attribute])
    #plt.subplots_adjust(hspace=0.0)
    plt.show()
