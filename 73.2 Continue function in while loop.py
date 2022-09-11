# In Python, we can use the continue statement to stop the current iteration of the while loop and continue with the next one. 

n = 1

while n < 5: #n = 1 2 3 4 5 -----------1
    if n == 2: #only when n = 2:
        n = n+1 #n becomes n+1 which is 3
        continue #goes back to ----------1 if n = 2, BUT IF n = 3, prints Hello Pythonista and then adds 1 to n
    print("Hello Pythonista")
    n = n+1 #when n = 4, and in this step n = 4 + 1 which means n = 5 it goes to ---------1, and there it becomes while 5 < 5, ehich is not true thus it stops the while loop