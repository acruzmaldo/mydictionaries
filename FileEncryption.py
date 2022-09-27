import random
import string

# open the info_security file
infile = open('info_security.txt', 'r')


# create an output file
outfile = open('encrypted.txt', 'w')

# create an empty dictionary
characters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
codes = []
encryption = {}
count = 0

#create encryption for each letter
while len(codes) <= 52:
    rand_digit = random.choice(string.digits)
    rand_punc = random.choice(string.punctuation)
    rand_mix = (random.choice(string.digits) + random.choice(string.punctuation))

    if str(rand_punc) not in codes:
        codes.append(rand_punc) 
    if str(rand_digit) not in codes:
        codes.append(rand_digit) 
    if rand_mix not in codes:
        codes.append(rand_mix) 

#assign codes to letter
for letters in characters:
    encryption[letters.upper()] = codes[count]
    count += 1
    for letter in letters:
        encryption[letter] = codes[count]
        count += 1

#print encryption
count = 0
char = []
letter_list = []

for message in infile:
    text = message.split()
    for character in text:
        char += character.strip(',.:')
    for clean_letter in char:
        letter_list += clean_letter
        outfile.write(encryption[letter_list[count]])
        count += 1
        
outfile.close()


