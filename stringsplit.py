
# This program will split a string and can extract a portion you want
# If your string is 'Python programming is fun', then if you want
# to extract only programming from the string, using the 'split()' function
# you can specity split(string,' ',2)
# The first parameter contains the string
# The second parameter specifies how the string to be extracted, like when
# we see a blank space
# The thrid parameter specifies, from which split_mode index, we have to
# extract the string
# Example :-
# string = 'Pythong programming is fun'
# newstring = split(string,' ',2)
# 'newstring' will have the word 'programming'
# If third parameter is 3, then the 'newstring' variable will have the
# value 'is'


# Start of funtion split
def split(string,split_mode,count):
    check_count=0
    counter=0
    # if the last character is not space, then insert a space
    if string[len(string)-1] != ' ': 
        new_string=string+' '
    else:
        new_string=string # string without any space
    for letter in new_string:
        # if letter matches the mode, then increment the count
        if letter in split_mode: 
            check_count=check_count+1
        else:
            continue
    if count <= check_count: # the count is within range 
        word=' '
        for letter in string:
            if letter not in split_mode:
                word=word+letter
            else:
                counter=counter+1
                if counter == count: # mathching count
                    break
                else: # set the word to ' '
                    word=' '
    else: # the mode position out of range
        return 'Count out of range'
    return word

#End of function split

# Main process goes here
while True:
    string=input("Write a sentence : ")
    range=input("Input the range : ")
    if string in ' ' or range in ' ':
        print("You should type in some string ... ")
    else:
        split_string=split(string,' ',int(range))
        print(split_string)
    cont=input("Type quit for (exit) or anything to continue : ")
    if cont in 'quit':
        break
    
        

    
                
