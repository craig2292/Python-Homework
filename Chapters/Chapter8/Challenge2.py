import arcpy
from arcpy import env
env.workspace = "P:/Fall2015/Python/Python Scipting for ArcGIS/Data/Exercise08"
fc = "Hawaii.shp"
cursor = arcpy.da.SearchCursor(fc, ["SHAPE@"])
length = 0

for row in cursor:
    partnum = 0
    length = 0
    for part in row[0]:
        poly = arcpy.Polygon(part)
        print("Part {0} area: {1}".format(partnum, poly.area))
        print("Part {0} perimeter: {1}".format(partnum, poly.length))
        
        partnum += 1
