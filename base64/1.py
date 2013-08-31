######################################################################################
######################################################################################
######################################################################################
# file 1.py
# version 1.0.0
# Base64 example 1
######################################################################################
######################################################################################
######################################################################################

######################################################################################
################################### Main #############################################
######################################################################################

if __name__ == "__main__":
    import base64

    print "### base64 module example"

    data = "The miracle of the appropriateness of the language of mathematics for the formulation of the laws of physics is a wonderful gift which we neither understand nor deserve. by Eugene Wigner" * 10

    print "### String used for encoding and decoding"
    print data
    print ""

    encoded_data = base64.b64encode(data)

    print "### Encoded string - base64.b64encode()"
    print encoded_data
    print ""

    decoded_data = base64.b64decode(encoded_data)

    print "### Decoded string - base64.b64decode()"
    print decoded_data
    print ""

    encoded_data = base64.urlsafe_b64encode(data)

    print "### Encoded string - base64.urlsafe_b64encode()"
    print encoded_data
    print ""

    decoded_data = base64.urlsafe_b64decode(encoded_data)

    print "### Encoded string - base64.urlsafe_b64decode()"
    print decoded_data
    print ""