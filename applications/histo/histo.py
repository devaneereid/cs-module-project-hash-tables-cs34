# Your code here
import string 
# open the file in "read" mode 
text = open("robin.txt", "r") 
  
# creating an empty dictionary 
d = dict() 
  
# for loop through each line of the file 
for line in text: 
    # remove the leading spaces and newline character 
    line = line.strip() 
  
    # convert the characters in line to  
    # lowercase to avoid case mismatch 
    line = line.lower() 
  
    # remove punctuation marks from the line 
    line = line.translate(line.maketrans("", "", string.punctuation)) 
  
    # split- the line into words 
    words = line.split(" ") 
    words.sort()
    count = 0
  
    # for loop to iterate over each word in line 
    for word in words: 
        # see if the word is already in dictionary 
        if word in d: 
            # increment count by 1 
            d[word] = d[word] + 1
        else: 
            # add the word to dictionary with count 1 
            d[word] = 1
  
# Print the contents of dictionary 
for key in list(d.keys()): 
    print(d[key], ":", key, words) 

