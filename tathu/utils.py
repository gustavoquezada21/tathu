#
# This file is part of TATHU - Tracking and Analysis of Thunderstorms.
# Copyright (C) 2022 INPE.
#
# TATHU - Tracking and Analysis of Thunderstorms is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

import os
import re
import time
from datetime import datetime

import numpy as np
from osgeo import gdal, gdal_array

from tathu.constants import LAT_LON_WGS84

def getGeoT(extent, nlines, ncols):
    '''
    This function computes the resolution based on data dimensions.
    '''
    resx = (extent[2] - extent[0]) / ncols
    resy = (extent[3] - extent[1]) / nlines
    return [extent[0], resx, 0, extent[3] , 0, -resy]

def geo2grid(x, y, geoT):
    '''
    This function returns the grid point associated to a spatial location.
    \param x The spatial x-coordiante.
    \param y The spatial y-coordiante.
    \param geoTransform A list of 6 coefficients describing an affine transformation to georeference a grid.
    \return The grid point line and column.
    '''
    lin = (y - geoT[3]) / geoT[5]
    col = (x - geoT[0]) / geoT[1]
    return int(lin), int(col)

def grid2geo(lin, col, geoT):
    '''
    This function returns the spatial location of a grid point.
    \param geoTransform A list of 6 coefficients describing an affine transformation to georeference a grid.
    \param col The grid point column.
    \param row The grid point row.
    \return The spatial location.
    '''
    x = col * geoT[1] + geoT[0]
    y = lin * geoT[5] + geoT[3]
    return x, y

def getExtent(gt, shape):
    '''
    This function returns the extent based on the given GDAL
    geo-transform parameters and dimensions.
    '''
    llx = gt[0]
    lly = gt[3] + ((shape[0]) * gt[5])
    urx = gt[0] + ((shape[1])  * gt[1])
    ury = gt[3]
    return (llx, lly, urx, ury)

def array2raster(array, extent, srs=LAT_LON_WGS84, nodata=None, output='', driver='MEM'):
    # Get array dimension and data type
    nlines = array.shape[0]
    ncols = array.shape[1]
    type = gdal_array.NumericTypeCodeToGDALTypeCode(array.dtype)
    
    # Adjust nodata values
    if nodata is not None and isinstance(array, np.ma.MaskedArray):
        array = np.ma.filled(array, nodata)

    # Create GDAL raster
    driver = gdal.GetDriverByName(driver)
    raster = driver.Create(output, ncols, nlines, 1, type)
    raster.SetGeoTransform(getGeoT(extent, nlines, ncols))

    # Adjust band and write
    band = raster.GetRasterBand(1)
    if nodata is not None:
        band.SetNoDataValue(float(nodata))
    band.WriteArray(array)

    # Adjust SRS
    if srs is not None:
        raster.SetProjection(srs.ExportToWkt())

    band.FlushCache()

    return raster

def file2timestamp(path, regex='\d{12}', format='%Y%m%d%H%M'):
    '''
    This function extracts timestamp based on the given full-path file.
    '''
    # Extract filename
    filename = os.path.basename(path)

    # Extract date strings
    dates_strings = re.findall(regex, filename)

    for s in dates_strings:
        # Build date object
        date = datetime.strptime(s, format)
        # Return now. Detail: considering first found date
        return date

class Timer(object):
    def __enter__(self):
        self.start = time.time()

    def __exit__(self, *args):
        print('> Time:', time.time() - self.start, 'seconds')