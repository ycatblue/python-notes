"""
The translate() method returns a string where some specified characters are replaced with the character described
in a dictionary, or in a mapping table.

Use the maketrans() method to create a mapping table.

If a character is not specified in the dictionary/table, the character will not be replaced.

If you use a dictionary, you must use ascii codes instead of characters.
"""
mydict = {83: 80}
txt = "hello Sam!"
print(txt.translate(mydict))

mytable = txt.maketrans("S", "P")
print(txt.translate(mytable))

x = "mSa"
y = "eJo"
mytable2 = txt.maketrans(x, y)
print(txt.translate(mytable2))
