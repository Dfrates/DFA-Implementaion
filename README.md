# DFA-Implementaion
A DFA implementation created with python. It reads the DFA from a file with a certain format. Allows user input to test strings on DFA
The file format for the program to read the DFA is as follows with an example.
Note: program ignores comments that come after ";", however, it works without the comments as well

example:

ab      ; the alphabet
3       ; 3 states to read, 0, 1, and 2
1 0     ; 0 on a = 1; 0 on b = 0
2 0     ; 1 on a = 2; 1 on b = 0
2 2     ; 2 on a = 2; 2 on b = 2
2       ; accept state is 2

