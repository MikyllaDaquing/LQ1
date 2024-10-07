# Name: Daquing, Princess Mikylla P.
# Section: CS3B
# GroupName: Svelte

#variables that will store the names of your groupmates
mem1 = "Jerimie Dela Cruz"
mem2 = "Vinico Sumbad"
mem3 = "Princess Mikylla Daquing"

#variables that contains the age in whole number (strings)
age1 = "21"
age2 = "20"
age3 = "20"

#variables that contains the weekly allowance in decimal form.
weekly_allowance1 = 500.00
weekly_allowance2 = 2000.00
weekly_allowance3 = 1000.00

#print all results formatted as follows: (use concat)
#   member 1: "student name", his age is "age", allowance per week is "allowance"; .... up to memebr 3
print(mem1, "his age is", age1, "allowance per week is", weekly_allowance1)     #prints out "Jerimie Dela Cruz his age is 21 allowance per week is 500.0"
print(mem2, "his age is", age2, "allowance per week is", weekly_allowance2)     #prints out "Vinico Sumbad his age is 20 allowance per week is 2000.0"
print(mem3, "her age is", age3, "allowance per week is", weekly_allowance3)     #prints out "Princess Mikylla Daquing her age is 20 allowance per week is 1000.0"

#variables to store the length of the names of the members 4, print them formatted as follows:
#   print member 1 consists of "length" characters! .... up to member 3
a = len(mem1)
b = len(mem2)
c = len(mem3)

print("Member 1 consists of ", a, "characters!")
print("Member 2 consists of ", b, "characters!")        
print("Member 3 consists of ", c, "characters!")