import arcpy
from arcpy import env
env.workspace = "P:/Fall2015/Python/Python Scipting for ArcGIS/Data/Exercise07"

fc = "roads.shp"
newfield = "FERRY"
fieldtype = "TEXT"
fieldname = arcpy.ValidateFieldName(newfield)
fieldlist = arcpy.ListFields(fc)
 
 
if fieldname not in fieldlist:
    arcpy.AddField_management(fc, fieldname, fieldtype, "", "", 12)
    print "New field has been added."
else:
    print "Field name already exists."
 
 
cursor = arcpy.da.UpdateCursor(fc, ["FEATURE","FERRY"])
 
 
for row in cursor:
    if row[0] == "Ferry Crossing":
        #print row[0]
        #cursor.insertRow("YES")
        row[1] = "YES"
    else:
        #print row[0]
        #row.insertRow("NO")
        row[1] = "NO"
    cursor.updateRow(row)
del row
del cursor

