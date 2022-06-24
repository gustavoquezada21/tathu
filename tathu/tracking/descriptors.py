#
# This file is part of TATHU - Tracking and Analysis of Thunderstorms.
# Copyright (C) 2022 INPE.
#
# TATHU - Tracking and Analysis of Thunderstorms is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

import itertools
import multiprocessing

from affine import Affine
from osgeo import gdal
from pathos.multiprocessing import ProcessingPool
from rasterstats import zonal_stats

from tathu.tracking.detectors import ThresholdDetector, ThresholdOp
from tathu.tracking.system import ConvectiveSystemManager

class StatisticalDescriptor(object):
    '''
    This class implements a convective system descriptor that
    defines a set of statistical attributes for each system.
    '''
    def __init__(self, stats=['min', 'mean', 'std', 'count'], prefix='', rasterOut=False):
        self.stats = stats
        self.prefix = prefix
        self.rasterOut = rasterOut

    def describe(self, image, systems):
        # Get Affine object in order to run zonal_stats
        aff = Affine.from_gdal(*image.GetGeoTransform())

        # Extract values
        values = image.ReadAsArray()

        # Get no-data value
        nodata = image.GetRasterBand(1).GetNoDataValue()

        #  Create WKT representation for each polygon
        wkts = []
        for sys in systems:
            wkts.append(sys.geom.ExportToWkt())

        # Compute stats for each polygon
        stats = zonal_stats(wkts, values, stats=self.stats,
                            affine=aff, nodata=nodata,
                            raster_out=self.rasterOut, prefix=self.prefix)


        # Each stat for each system
        for sys, stat in zip(systems, stats):
            sys.attrs.update(stat)

        if self.rasterOut:
            for sys in systems:
                # Extract raster data from attrs dic
                sys.raster = sys.attrs.pop(self.prefix + 'mini_raster_array')
                sys.nodata = sys.attrs.pop(self.prefix + 'mini_raster_nodata')
                sys.geotransform = sys.attrs.pop(self.prefix + 'mini_raster_affine').to_gdal()

        return systems

def chunks(data, n):
    """Yield successive n-sized chunks from a slice-able iterable."""
    for i in range(0, len(data), n):
        yield data[i:i+n]

class StatisticalDescriptorMT(object):
    '''
    *** Note: Experimental multithread version. ***
    This class implements a convective system descriptor that
    defines a set of statistical attributes for each system.
    '''
    def __init__(self, stats=['min', 'mean', 'std', 'count'], prefix='', rasterOut=False):
        self.stats = stats
        self.prefix = prefix
        self.rasterOut = rasterOut
        self.values = None
        self.nodata = None
        self.affine = None

    def describe(self, image, systems):
        # Get Affine object in order to run zonal_stats
        self.aff = Affine.from_gdal(*image.GetGeoTransform())

        # Extract values
        self.values = image.ReadAsArray()

        # Get no-data value
        self.nodata = image.GetRasterBand(1).GetNoDataValue()

        #  Create WKB representation for each polygon
        wkbs = []
        for sys in systems:
            wkbs.append(sys.geom.ExportToWkb())

        # Create a process pool using all cores
        cores = multiprocessing.cpu_count()
        p = ProcessingPool(cores)

        # Compute chunksize
        #chunksize = max(1, int(len(systems)/cores))

        # Parallel map
        stats_list = p.map(self.__getstats, chunks(wkbs, cores))

        # Flatten to a single list
        stats = list(itertools.chain(*stats_list))

        # Each stat for each system
        for sys, stat in zip(systems, stats):
            sys.attrs.update(stat)

        if self.rasterOut:
            for sys in systems:
                # Extract raster data from attrs dic
                sys.raster = sys.attrs.pop(self.prefix + 'mini_raster_array')
                sys.nodata = sys.attrs.pop(self.prefix + 'mini_raster_nodata')
                sys.geotransform = sys.attrs.pop(self.prefix + 'mini_raster_affine').to_gdal()

        return systems

    def __getstats(self, wkbs):
        # Compute stats for each polygon
        stats = zonal_stats(wkbs, self.values, stats=self.stats,
                            affine=self.aff, nodata=self.nodata,
                            raster_out=self.rasterOut, prefix=self.prefix)
        return stats

class ConvectiveCellsDescriptor():
    '''
    This class implements a convective system descriptor
    that computes the number of convectives cells.
    '''
    def __init__(self, cellTemp, minarea=None):
        self.cellTemp = cellTemp # The temperature (kelvin) used to define a convective cell.
        self.minarea = minarea   # The minimum area used to define a convective cell.

    def describe(self, image, systems):
        # Create detector for cells
        detector = ThresholdDetector(self.cellTemp, ThresholdOp.LESS_THAN, self.minarea)

        # Searching for cells
        cells = detector.detect(image)

        # Indexing convective cells
        manager = ConvectiveSystemManager(cells)

        # For each system, count the number of convective cells
        for sys in systems:
            # Get overlap cells
            overlapCells = manager.getSystemsFromSystem(sys)
            # Count it!
            ncells = {'ncells' : len(overlapCells)}
            # Add atribute to system
            sys.attrs.update(ncells)