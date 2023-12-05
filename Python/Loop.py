
mySentence = 'loves the color'

color_list = ['red', 'blue', 'green', 'yellow', 'teal', 'black']

#Define a function and set parameters
def color_function(name):
    lst = []
    for x in color_list:
        msg = "{0} {1} {2}".format(name,mySentence,x)
        lst.append(msg)
    return lst

def get_name():
    go = True
    while go:
        name = input('What is your name? ')
        if name == '':
            print('You need to provide your name!')
        elif name == 'Sally':
            print('Sally, you may not use this software.')
        else:
            go = False
    lst = color_function(name)
    for x in lst:
        print(x)

get_name()
