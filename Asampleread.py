"""
Write a program (doesn't have to be a function, but can be) that reads what's in sample.txt and prints it to the console.
"""
textfile = open("sample.txt", "r")
content = textfile.read()
print(content)
 