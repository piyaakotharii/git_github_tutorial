shades = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
for (i,val) in enumerate(shades):
    if i not in (0,4,5):
        print("value at position",i,"is",val)