"""
Python exposes a terse and intuitive syntax for performing 
slicing on lists and strings. This makes it easy to reference
only a portion of a list or string. 

This Stack Overflow answer provides a brief but thorough
overview: https://stackoverflow.com/a/509295

Use Python's slice syntax to achieve the following:
"""

a = [2, 4, 1, 7, 9, 6]

# Output the second element: 4:
b = a.copy()
print(b[1:2])

# Output the second-to-last element: 9
c = a.copy()
print(c[4:5])

# Output the last three elements in the array: [7, 9, 6]
d = a.copy()

print(d[3:5])

# Output the two middle elements in the array: [1, 7]
e = a.copy()
print(e[2:3])

# Output every element except the first one: [4, 1, 7, 9, 6]
f = a.copy()
print(f[1:5])

# Output every element except the last one: [2, 4, 1, 7, 9]
g = a.copy()
print(g[0:4])

# For string s...

s = "Hello, world!"

# Output just the 8th-12th characters: "world"
h = s
print(h[7:13])