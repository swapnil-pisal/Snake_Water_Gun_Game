# snake water gun game (solution)

# import random library for generate the random number 
import random

# show to the user
print("Welcome to snake,water,gun game")

# for selection to the user
print("1 for Snake \n2 for Water \n3 for Gun")

# take the input from the user 
user=int(input("you choose between 1 to 3 : "))

# computer can generate the ranmdom number between 1 to 2
com=random.randint(1,3)

# print the  computer choose which one
print("computer choose : ",com)

# logic - 

# snake x snake    =  draw
# snake x water    =  snake
# snake x gun      =  gun
# water x water    =  draw
# water x gun      =  water
# gun x  gun       =  draw

#            com
#          1  2  3
# user  1  d  u  c
# user  2  c  d  u
# user  3  u  c  d


# usxe the conditional statement

if (user==com):
    print("its draw")
elif(user==1 and com==2):
    print("you  won")
elif(user==2 and com==3):
    print("you  won")
elif(user==3 and com==1):
    print("you  won")
else:
    print("you lose")

