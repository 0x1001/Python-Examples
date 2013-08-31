######################################################################################
######################################################################################
######################################################################################
# file 2.py
# version 1.0.0
# zlib example 2
######################################################################################
######################################################################################
######################################################################################

######################################################################################
################################### Main #############################################
######################################################################################
if __name__ == "__main__":
    print "### zlib module example"

    data = "The miracle of the appropriateness of the language of mathematics for the formulation of the laws of physics is a wonderful gift which we neither understand nor deserve. by Eugene Wigner" * 10

    zipped_data = data.encode('zip')
    unzipped_data = zipped_data.decode('zip')

    print "### Data size: " + str(len(data))
    print "### Zipped data size: " + str(len(zipped_data))

    if data == unzipped_data: print "Data are the same!"
