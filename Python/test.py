

mySentence = 'loves the color'

color_list = ['red', 'blue', 'green', 'yellow', 'teal', 'black']

#Define a function and set parameters
def color_function(name):
    lst = []
    for x in color_list:
        msg = "{0} {1} {2}".format(name,mySentence,x)
        lst.append(msg)
    return lst

#Call the function and pass arguments
lst = color_function('Amanda')
for x in lst:
    print(x)
