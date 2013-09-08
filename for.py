######################################################################################
######################################################################################
######################################################################################
# file for.py
# version 1.0.0
# For loop example
######################################################################################
######################################################################################
######################################################################################

######################################################################################
################################### Main #############################################
######################################################################################

if __name__ == '__main__':
    print "Example 1"

    array = ["a","b","c","d"]

    for element in array:
        print element
    else:
        print "End of the loop. No interrupt."

    print "\nExample 2 - Enumerate"

    for index,element in enumerate(array):
        print str(index) + " : " + element

    print "\nExample 3 - Dictionary"
    dictionary = { "a": "aa","b": "bb", "c": "cc"}

    for key,element in dictionary.items():
        print key + " => " + element

    print "\nExample 4 - Dictionary"
    for key in dictionary:
        if key == "a":
            print "Key " + key
            print "Continue"
            continue

        if key == "b":
            print "Key " + key
            print "Break"
            break
    else:
        print "You won't see this because of break."

    print "\nExample 4 - Indexing"
    for index in range(10):
        print index