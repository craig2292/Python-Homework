import arcpy
from arcpy import env
out_path = "P:/Fall2015/Python/Python Scipting for ArcGIS/Data/Exercise09"
env.workspace = out_path
rasterlist = arcpy.ListRaster()
arcpy.CreatePersonalGDB_management(out_path + "/Results", "myrasters.gdb")
for raster in rasterlist:
    desc = arcpy.Describe(raster)
    rname = desc.baseName
    outraster = out_path + "/Results/myrasters.gdb/" + rname
    arcpy.CopyRaster_management(raster, outraster)
