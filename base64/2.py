######################################################################################
######################################################################################
######################################################################################
# file 2.py
# version 1.0.0
# Base64 example 2
######################################################################################
######################################################################################
######################################################################################

######################################################################################
################################### Main #############################################
######################################################################################

if __name__ == "__main__":
    print "### base64 module example"

    data = "The miracle of the appropriateness of the language of mathematics for the formulation of the laws of physics is a wonderful gift which we neither understand nor deserve. by Eugene Wigner" * 10

    print "### String used for encoding and decoding"
    print data
    print ""

    encoded_data = data.encode('base64')

    print "### Encoded string - string.encode('base64')"
    print encoded_data
    print ""

    decoded_data = encoded_data.decode('base64')

    print "### Decoded string - string.decode('base64')"
    print decoded_data
    print ""
