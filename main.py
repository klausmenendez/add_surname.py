# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def add_surname(names):
    for i in range(0,len(names)):
        if names[i][0]=="k":
            #find names that start with k
           fullname = names[i] + "Kardashian"
           print(fullname.split(" , "))


#print(add_surname(["ken","kim","kang"]))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
