
import pyfiglet
banner = pyfiglet.figlet_format("Game Start")
print(banner)
import random
while True:
    idea = int(input("Value : "))
    rand = random.randint(1,6)
    if idea == rand:
        reusult = "Ok"
        print(reusult)
        print("The has Finish")
        break
    else:
        print("Wrong")
        print("random Was :",rand)
    