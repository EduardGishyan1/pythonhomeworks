# Task1

# # secret_password = "python"

# # user_password = input("Enter password: ")

# # print("success" if user_password == secret_password else "enter right password")

# # Task2

# # for num in range(2, 101):
# #     for j in range(2, num):
# #         if num % j == 0:
# #             break
# #     else:
# #         print(num)

# # Task3

# print("""You enter a dark room with two doors.
# Do you go through door #1 or door #2 or door #3?""")

# door = input("> ")

# if door == "1":
#     print("There's a giant bear here eating a cheese cake and there is box.")
#     print("What do you do?")
#     print("1. Take the cake.")
#     print("2. Scream at the bear.")
    
#     bear = input("> ")

#     if bear == "1":
#      print("The bear eats your face off. Good job!")
#     elif bear == "2":
#      print("The bear eats your legs off. Good job!")
#     else:
#      print(f"Well, doing {bear} is probably better.")
#      print("Bear runs away.")

# if door == "2":
#  print("You stare into the endless abyss at Cthulhu's retina.")
#  print("1. Blueberries.")
#  print("2. Yellow jacket clothespins.")
#  print("3. Understanding revolvers yelling melodies.")


#  insanity = input("> ")
#  if insanity == "1" or insanity == "2":
#   print("Your body survives powered by a mind of jello.")
#   print("Good job!")
#  else:
#   print("The insanity rots your eyes into a pool of muck.")
#   print("Good job!")
  
# elif door == "3":
#   print("You open the door and see a box.")
#   print("1. open the box")
#   print("2. continue your way")
#   print("3. do nothing")

#   choose = input("> ")

#   if choose == "1":
#     print("You open the box and there are keys and food")
#     print("1. eat food and take keys")
#     print("2. take only keys and continue your way")
#     print("3. only eat food")
#     choose2 = input("> ")
#     if choose2 == "1" or choose2 == "3":
#       print("The food was old, and you were poisoned.")
#     elif choose2 == "3":
#       print("you take the keys continue see a door you open the door and leave the room you are saved")
#     else:
#         print(f"Well, doing {choose2} maybe is better.")
#   elif choose == "2":
#       print("you continue and see a door but you have not keys to open the door then you are starving")
#   elif choose == "3":
#     print("you do nothing and you are starving")
#   else:
#     print(f"Well, doing {choose} maybe is better.")
# else:
#  print("You stumble around and fall on a knife and die. Good job!")

# Task 4

# bit_length() function

# n = 101
# bits = 0

# while n:
#     bits += 1
#     n >>= 1

# print(bits)

# bit_count() function

# n = 101
# count = 0
# while n:
#     count += n & 1
#     n >>= 1
# print(count)
