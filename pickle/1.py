######################################################################################
######################################################################################
######################################################################################
# file 1.py
# version 1.0.0
# pickle example 1
######################################################################################
######################################################################################
######################################################################################

######################################################################################
################################### Main #############################################
######################################################################################

if __name__ == "__main__":
    import pickle
    import os

    # Data used for pickle
    data1 = ["absc","dddd","dsfss"]
    data2 ="fsfsfdsfsf"
    data3 = True
    data4 = 59

    pickle_file = open("temp.txt","wb")

    pickle.dump(data1,pickle_file)
    pickle.dump(data2,pickle_file)
    pickle.dump(data3,pickle_file)
    pickle.dump(data4,pickle_file)

    pickle_file.close()

    pickle_file = open("temp.txt","rb")

    _data1 = pickle.load(pickle_file)
    _data2 = pickle.load(pickle_file)
    _data3 = pickle.load(pickle_file)
    _data4 = pickle.load(pickle_file)

    pickle_file.close()

    os.unlink("temp.txt")
