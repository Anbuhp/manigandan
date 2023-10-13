program:

fname = input("Enter the name of the file:") 
infile = open(fname, 'r') 
lines = 0 
words = 0 
characters = 0 
for line in infile: 
    wordslist = line.split() 
    lines = lines + 1 
    words = words + len(wordslist) 
    characters = characters + len(line) 
print("No of Lines:",lines) 
print("No of Words:",words) 
print("No of Characters:",characters)

output:
Enter the name of the file:practical 14.py
No of Lines: 13
No of Words: 52
No of Characters: 358
