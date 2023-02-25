#assign numbers of variables in single line
x,y,z = 1,2,3
print(x,y,z)

#assigning one value to many variables
x=y=z="Hi There"
print(x)
print(y)
print(z)

#assigning string to variable
a = "Hello Dear"
#multiline string using """  """
b = """Hi There
how uh doing?"""
print(a)
print(b)

#string slicing
mystr = "How uh doing?"
print(len(mystr))                #print the length of the string (including spaces)
print(mystr[4:])                 #print just the 0th index element in string
print("will uh just","shut up")  #comma is used for adding multiple strings in one print statement or space
