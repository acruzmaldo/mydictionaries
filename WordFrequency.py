infile = open('sometext.txt', 'r')

count = 0

#initiate the dictionary
dict = {}
for text in infile:
    words = text.split()

    #clean values
    for value in range(len(words)):
        words[value] = words[value].strip(',.')

    #iterate through words to make the dictionary
    for word in words:
        dict[words[count].strip(',.')] = words.count(word)
        count += 1
        
#print the dictionary
print(dict)
