
""" Simple as it looks, performs basic object inspection """
def esto(ob):
    print('~~~~') 
    print('TYPE')
    print('~~~~') 
    print(type(ob))
    print(' ')

    print('~~~~~~~~~')
    print('DOCSTRING')
    print('~~~~~~~~~')
    print(ob.__doc__)
    print(' ')

    print('~~~')
    print('DIR')
    print('~~~')
    print(dir(ob))
    print(' ')

    print('~~~~')
    print('VARS')
    print('~~~~')
    
    try: 
        print(vars(ob))
    except TypeError:
        print('Object has no __dict__ attributes')
    print(' ')

