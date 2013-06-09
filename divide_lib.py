###############################################################
# FUNCTION
#
#
#   dissolve:   Per reference to an article on how the ESRI
#               dissolve functionality can be made better using
#               the ESRI dissolve functionality.
#
#   read up:    http://www.mindland.com/wp/solving-the-arcpy-dissolve/
#
#
#


import arcpy, os



###############################################################
# Divide and conquer dissolve
#
# Specialized sub-dissolve based on group size. Bacause ESRI
# didn't get it right.
#
# Read more about the needs for this function on this page:
#
#    http://www.mindland.com/wp/solving-the-arcpy-dissolve/
#
def group_dissolve(file_in, file_out,group_by,path_maps_temp):

    count           =  0
    current_min     =  0
    current_max     =  group_by
    joinstring      =  []
    timer_dissolve  =  0


    features_total    =  int(arcpy.GetCount_management(file_in).getOutput(0))



    while (current_max < (features_total+group_by)):

        resulting_file  = "%sbuffer_result_%s.shp" % (path_maps_temp,count)

        where_clause    = '"FID"> %s AND "FID" <= %s' %(current_min,current_max)

        arcpy.Select_analysis(file_in, resulting_file, where_clause)


        resulting_file_d = "%sbuffer_result_d_%s.shp" % (path_maps_temp,count)



        arcpy.Dissolve_management(resulting_file, resulting_file_d,"","","SINGLE_PART","")


        # delete temporary files
        arcpy.Delete_management(resulting_file)


        joinstring.append(resulting_file_d)

        current_min = group_by*count
        current_max = current_min + group_by

        count +=1




    resultbuffer = "%sresultbuffer_%s.shp" % (path_maps_temp, group_by)



    arcpy.Merge_management(joinstring, resultbuffer,"")


    # delete temporary files
    for shapefile in joinstring:

        arcpy.Delete_management(shapefile)


    arcpy.Dissolve_management(resultbuffer, file_out,"","","SINGLE_PART","")


    # delete temporary files
    arcpy.Delete_management(resultbuffer)