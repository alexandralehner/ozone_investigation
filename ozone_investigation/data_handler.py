from . import plot
# import xarray as xr


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

    plot.plot_world(data.ozone.mean(["longitude", "latitude"]), "2000-01-01")
