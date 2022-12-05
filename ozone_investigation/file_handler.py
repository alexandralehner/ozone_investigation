import xarray as xr


def read_in_file(filename):
    """reads in netCDF file"""
    # data = nc.open_dataset(filename)
    xr.set_options(keep_attrs=True)
    with xr.open_dataset(filename) as ds:
        ds.load()
    return ds
