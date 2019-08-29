def hello_func(greeting, name= 'You'):
    return '{}, {}'.format(greeting, name)
#hello_func()
#print(hello_func())

#print(hello_func('Hi', name ='Corey'))

#print(len('Test'))

#10.38
def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

#tuples
#dictionary

courses = ['Math', 'Art']  #List
info = {'name':'John', 'age':22} #Dictionary

#student_info('Math', 'Art', name='John', age=22)
student_info(*courses, **info)
