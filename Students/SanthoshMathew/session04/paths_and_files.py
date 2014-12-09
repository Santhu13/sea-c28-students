import os

def get_filepaths(directory):

    file_paths = []  # Creating a Py LIST which will store all of the full filepaths.
    #print os.walk(directory)  
    # Then: we 'walk' the tree: 
    # os.walk yields a 3-tuple (dirpath, dirnames, filenames)
    for root, directories, files in os.walk(directory):
        #print files + "j"
        for filename in files:
            # Then: we join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)  # Add it to the LIST here 

    return file_paths  #


full_file_paths = get_filepaths(".")
print full_file_paths

#f = open('/home/santhosh/cfpy/sea-c28-students/Students/SanthoshMathew/session03
#', 'w') # opening w/ a "w" to write 
#for file in full_file_paths:
 #   fname=str(file)
    # use following line to check file name length ... 
    # le=len(fname)
  #      #if len(fname)>120 
     #   print 'shorten this file name', fname # print le, fname
#f.close()  