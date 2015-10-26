import arcpy
from arcpy import env
env.workspace = "P:/Fall2015/Python/Python Scipting for ArcGIS/Data/Exercise09"
raster = "landcover.tif"
desc = arcpy.Describe(raster)
x = desc.meanCellHeight
y = desc.meanCellWidth
spatialref = desc.SpatialReference
units = spatialref.linearUnitName
print "Cells are" + str(x) + " by " + str(y) + " " + units + "."


"""
    on line 3, the original workspace "C:/EsriPress/Python/Data\Exercise09" had a backslash
    on line 4, "landcover.tiff" needed to be changed to "landcover.tif"
    on line 5, "arcpy.describe(raster)" needed to be changed to "arcpy.Describe(raster)"
    on line 6, "desc.MeanCellHeight" needed to be "desc.meanCellHeight"
    on line 7, "desc.MeanCellWidth" needed to be "desc.meanCellWidth"
    on line 8, "desc.spatialReference" needed to be "desc.SpatialReference"
"""    
