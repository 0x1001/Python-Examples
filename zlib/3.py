######################################################################################
######################################################################################
######################################################################################
# file 3.py
# version 1.0.0
# zlib example 3
######################################################################################
######################################################################################
######################################################################################

######################################################################################
################################### Main #############################################
######################################################################################
if __name__ == "__main__":
    import zlib

    print "### zlib module example for streaming data"

    data = "The miracle of the appropriateness of the language of mathematics for the formulation of the laws of physics is a wonderful gift which we neither understand nor deserve. by Eugene Wigner" * 10

    # Compression
    zipped_obj = zlib.compressobj()
    zipped_data = ""
    for element in data:
        zipped_data += zipped_obj.compress(element)
    zipped_data += zipped_obj.flush()

    # Decompression
    unzipped_obj = zlib.decompressobj()
    unzipped_data = ""
    for element in zipped_data:
        unzipped_data += unzipped_obj.decompress(element)
    unzipped_data += unzipped_obj.flush()

    print "### Data size: " + str(len(data))
    print "### Zipped data size: " + str(len(zipped_data))

    if data == unzipped_data: print "Data are the same!"
