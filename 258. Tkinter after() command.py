my_window = Window()

def say_sth(thing):
    print(thing)


#after() takes in a TIME in ms after which it starts, a FUNCTION and *args for the FUNCTION:
my_window.after(1000, say_sth, "Hello")
#waits for 1000ms and PRINTS: Hello

def say_sth(a, b, c):
    print(a)
    print(b)
    print(c)


#after() takes in a TIME in ms after which it starts, a FUNCTION and *args for the FUNCTION:
my_window.after(1000, say_sth, 3, 5, 8)
##waits for 1000ms and PRINTS:
# 3
# 5
# 8
