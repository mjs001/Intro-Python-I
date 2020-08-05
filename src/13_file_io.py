"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"
f = open('foo.txt', 'r')
# YOUR CODE HERE
with open('foo.txt', 'r') as f:
          print(f.read())
# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain
block = '''
Sir stuffington the third likes stuff. 
He was very passionate about stuff.
Enjoyed playing video games especially ones about stuff.
'''
with open('bar.txt', 'w') as f2:
    f2.write(block)
with open('bar.txt', 'r') as check:
    for line in check:
        print(line, end='')
# YOUR CODE HERE