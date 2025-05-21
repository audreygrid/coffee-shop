import os

os.chdir("/Users/SmoeLas/Desktop/Labs/coffee-shop-challenge")
os.system("touch trial2.txt")

with open("trial2.txt", "a") as file:
    lines = file.write("\nyou stupid nigger!")
    

with open("trial2.txt", "r") as file:
    lines = file.read()
    print(lines)
    
    # for line in lines:
    #     pass