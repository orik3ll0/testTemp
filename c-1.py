d1 = {i: [] for i in range(5)}    #with curly brackets we decleared that it is a dictionary. In inside of dict
                                  # by for loop we are settign "i" value wich is key here. Value is givven []
d2 = dict.fromkeys(range(5), [])  # fromkeys function which creates dictionary with empty values [] and keys in range(5)

print(d1)
print(d2)
