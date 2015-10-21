import arcpy
from arcpy import env
env.workspace = "P:/Fall2015/Python/Python Scipting for ArcGIS/Data/Exercise10"
mxd = arcpy.mapping.MapDocument("P:/Fall2015/Python/Python Scipting for ArcGIS/Data/Exercise10/Austin_TX.mxd")
df = arcpy.mapping.ListDataFrames(mxd, "parks")[0]
lyr = arcpy.mapping.ListLayers(mxd, "parks", df)[0]
dflist = arcpy.mapping.ListDataFrames(mxd)
for dframe in dflist:
    if dframe.name == "Parks":
        arcpy.mapping.AddLayer(dframe, lyr)
mxd.save()
del mxd
