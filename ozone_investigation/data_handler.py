from . import plot
import xarray as xr


def maxozone(data):
    # mask = data.where(data != data.attrs['missing_value'])
    # data[112, :, :].plot()
    # ds.temperature_2_meter.mean("longitude").sel(latitude=5).plot()
    # ds.temperature.sel(
    #   latitude=slice(70, 90), altitude=20000).mean(
    #   ["longitude", "latitude"]).plot()
    # groupby
    # ds.sel(time=slice("1991-01-01", "2019-12-31"))
    # ds.sel(time=slice("1991-01-01", "2019-12-31")).groupby("time.month")
    # clim = ds.sel(time=slice("1991-01-01", "2019-12-31")).groupby(
    #   "time.month").mean()
    # clim
    # anom = ds.groupby("time.month") - clim
    # anom
    # anom.temperature_2_meter.mean(["longitude", "latitude"]).plot();

    #print("coords")
    #print(data.coords)
    #print("values")
    #print(data.values)
    print("Mean")
    #plot height of maximum level of ozone: xr.where(cond,a,b)
    data_time_mean=data.mean(dim=["time"])
    #max_altitude=data_time_mean.where(data_time_mean.max(dim=["altitude"]))
    #max_altitude=data_time_mean.where(data_time_mean==data_time_mean.max(dim=["altitude"]), drop=True).squeeze()
    max_altitude=data_time_mean.where(data_time_mean["ozone"]==data_time_mean["ozone"].max(dim=["altitude"]), data_time_mean["altitude"])


    print(max_altitude.values)

#    plot.plot_world(max_altitude.ozone(["longitude_bins", "latitude_bins"]))
    plot.plot_world(max_altitude, variable="ozone")