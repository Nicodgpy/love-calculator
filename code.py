# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

nombres=name1 + name2
nombre_cadenas_mn=nombres.lower()
t=nombre_cadenas_mn.count("t")
r=nombre_cadenas_mn.count("r")
u=nombre_cadenas_mn.count("u")
e=nombre_cadenas_mn.count("e")

true=t + r + u + e

l=nombre_cadenas_mn.count("l")
o=nombre_cadenas_mn.count("o")
v=nombre_cadenas_mn.count("v")
e=nombre_cadenas_mn.count("e")

love=l + o + v + e

true_love=int(str(true) + str(love))


if (true_love <10)  or (true_love >90):
  print(f"Your score is {true_love}, you go together like coke and mentos.")
elif (true_love >=40) and (true_love <=50):
  print(f"Your score is {true_love}, you are alright together.")
else:
  print(f"Your score is {true_love}.ss")
  
