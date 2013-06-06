
Split String
=============

This program will split a string and can extract a portion you want
If your string is 'Python programming is fun', then if you want to extract only programming from the string, using the 'split()' function you can specity split(string,' ',2). The first parameter contains the string. The second parameter specifies how the string to be extracted, like when we see a blank space or if we find '\' etc. The thrid parameter specifies, from which split_mode index, we have to extract the string

Example :-
string = 'Pythong programming is fun'
newstring = split(string,' ',2)
'newstring' will have the word 'programming'
If third parameter is 3, then the 'newstring' variable will have the value 'is'
