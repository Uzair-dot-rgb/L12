string = input("Enter a word please : ")
char = input("Enter a character please : ")
i = 0
count = 0
while(i<len(string)):
    if (string[i] == char):
        count = count + 1
    i = i + 1
print("The characters are ", char, "And the occrence is ", count)
