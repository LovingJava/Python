'''
LEGB
Local. Enclosing, Global, Built-in
'''
x = 'global x'

def test():
    # global x
    x = 'local x'
    print(x)

test()
print(x)
