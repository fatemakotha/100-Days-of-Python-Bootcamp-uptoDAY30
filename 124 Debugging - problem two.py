# Reproduce the Bug
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6) #produces a bug a number of time but not always, because it chooses a number from 1 to 6, not 0th to 5th index as we need. So when it randomly picks 6, there is an error
dice_num = randint(0, 5) #changed the range and fixed the bug
print(dice_imgs[dice_num])