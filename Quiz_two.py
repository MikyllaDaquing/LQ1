# Name: Daquing, Princess Mikylla P.
# Section: CS3B
# GroupName: Svelte

#variables that will store the names of your groupmates
mem1 = "Jerimie Dela Cruz"
mem2 = "Vinico Sumbad"
mem3 = "Princess Mikylla Daquing"

#variables that contains the age in whole number 
age1 = 21
age2 = 20
age3 = 20

#variables that contains the weekly allowance in decimal form.
weekly_allowance1 = 500.00
weekly_allowance2 = 2000.00
weekly_allowance3 = 1000.00

#perform and print the following math options for all the age and allowances:
#   "+": age member1 - member 3
#   "-": age member1 - member 3
#   "*": age member 1 and allowance .... member 3
sum = age1 + age2 + age3
diff = age1 - age2 - age3
mul = age1 * weekly_allowance1
mul1 = age2 * weekly_allowance2
mul2 = age3 * weekly_allowance3

print(sum)      #prints out "61"
print(diff)     #prints out "-19"
print(mul)      #prints out "10500.0"
print(mul1)      #prints out "40000.0"
print(mul2)      #prints out "20000.0"

#perform and print (compare)
#   age member 1 - member 2; member 2 - member 3
print(age1 > age2)       #prints out "True"
print(age2 < age3)       #prints out "False"
print(age2 == age3)       #prints out "True"

#   length member 1 - member 2; member 2 - member 3
print(len(mem1) > len(mem2))    #prints out "True"
print(len(mem2) < len(mem3))    #prints out "True"