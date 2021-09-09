from os import lchown
import random
import turtle
from array import *
import csv


#121
listOfNames = []
mainMenu = True
#Main Menu
def mainMenu():
   while mainMenu == True:
      return_to_main = input("Would you like to return to the main menu?(y/n) ").lower()
      if return_to_main == "y":
         mainMenu = True
      elif return_to_main == "n":
         mainMenu = False

#ADD name to list
def addName():
   add_a_name = input("Enter name to add: ").capitalize()
   listOfNames.append(add_a_name)
   print(f"{add_a_name} has been added to the list of names.")
   return add_a_name

#CHANGE name in list
def changeName():
   print(sorted(listOfNames))
   name_change_selection = input("What name would you like to change? ")
   new_name = input("Enter new name: ").capitalize()
   print(f"You changed {name_change_selection} to {new_name}.")
   changed_name = (name_change_selection, new_name)
   return changed_name

#DELETE name in list
def deleteName():
   delete_name_selection = input("Which name would you like to delete? ").capitalize()
   listOfNames.remove(delete_name_selection)
   print(f"{delete_name_selection} has been deleted from the list.")
   return delete_name_selection

#VIEW ALL names in the list
def viewAllNames():
   sorted_names = print(sorted(listOfNames)).capitalize()
   return sorted_names

#END program
   

def main():
   userMenu = int(input("1) ADD name to the list\n2) CHANGE name in the list\n3) DELETE name in the list\n4) VIEW ALL names in the list\n5) QUIT program\nSelect Number: "))
   if userMenu == 1:
      add_a_name = addName()
      mainMenu() 


   elif userMenu == 2:
      name_change_selection, new_name = changeName()


   elif userMenu == 3:
      delete_name_selection = deleteName()
      

   elif userMenu == 4:
      sorted_names = viewAllNames()
     

   else:
      print("Invalid selection")


main()