score = 0 #integer
height = 5.7 #float
isWinning = True #Boolean

# print("My score is: " + score + "height is " + height + "w/l: " + isWinning) #wont work!!
print("My score is: " + str(score) + "height is " + str(height) + "w/l: " + str(isWinning)) 
#prints: My score is: 0height is 5.7 w/l: True

# OR 
#You can use an f-string

print(f"your score is {score}, height is {height}), you are winning {isWinning}")
#prints: your score is 0, height is 5.7), you are winning True