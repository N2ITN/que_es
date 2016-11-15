
""" Simple as it looks, performs basic object inspection """
def esto(ob):

    print('____')
    print('VARS')
    print('___')
    try: 
        print(vars(ob))
    except TypeError:
        print('Object has no __dict__ attributes')
    print(' ')

    print('___')
    print('DIR')
    print('___')
    print(dir(ob))
    print(' ')

    print('_________')
    print('DOCSTRING')
    print('_________')
    print(ob.__doc__)
    print(' ')

    print('____') 
    print('TYPE')
    print('____') 
    print(type(ob))
    print(' ')




    

