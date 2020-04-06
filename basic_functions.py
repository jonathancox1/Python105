#python function that accepts two arguments, a number and a string
#the function should return the string printed num amount of times
#function should be able to accpet itself as an argument
#ex repeat(3, repeat(5, 'woof'))

def repeat(times, string):
    i = 0
    finished_string = ''
    while i < int(times):
        finished_string += string
        i += 1
    return finished_string
    

#alternate and much simpler to read
def repeat1(times, string):
    return string * times
