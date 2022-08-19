



# Adventure Story Program

print("Youre in a dark alley. Where do you go?")
print("(1) left (2) straight (3) right")
choice = input("choose: ")

if choice == "1":
   print("u go left and die")
elif choice == "2":
   print("u go straight and there is another crossing")
   #continue tree here
   print("(1) left (2) straight (3) right")
   choice = input("choose: ")
   if choice == "1":
         print("u go left")
   elif choice == "2":
         print("u go straight")
   elif choice == "3":
      print("u go right")
elif choice == "3": 
   print("u go right and theres a wall")
else:
   print("u just die for inaction")



#    print("u go straight and there is another crossing")
#    #continue tree here
#    print("(1) left (2) straight (3) right")
#    elif choice == "1":
#         print("u go left")
#     elif choice == "2":
#         print("u go straight")
#     elif choice == "3":
#         print("u go right")