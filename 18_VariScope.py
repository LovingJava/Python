# x = 'global x'

# def test(z):
#     global x
#     x = 'local x'
#     print(z)

# test('local z')
# print(x)

x = 'global x'

def outer():
    #x = 'outer x'

    def inner():
        #nonlocal x
        #x = 'inner x'
        print(x)
    
    inner()
    print(x)

outer()
print(x)     
    


