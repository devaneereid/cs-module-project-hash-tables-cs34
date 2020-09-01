array = ['Waltz','Waltz','Tango', 'Tango', 'Tango', 'Viennese Waltz', 'Foxtrot', 'Cha Cha', 'Samba', 'Rumba', 'Paso Doble', 'Jive']
# so the idea is to take this array and return a python dictionary where each string in the array is a key, and the values are the frequency that those strings appear in the array.
# for example:
#  {'Waltz': 2, 'Tango': 3,  etc...} 

def danceCount(array):
    # set up an empty dictionary
    dict = {}

    # set up the for loop, passing item into array
    for item in array:
        if (item in dict):
            dict[item] += 1
        else:
            dict[item] = 1

    # created for loop passing the key/value pairs into the dictionary
    for key, value in dict.items():
        # printing the key/value
        print ("'% s':% d"% (key, value))

# returning the entire function to show the key/value pairs
danceCount(array)
