from datetime import date
today = date.today()

birthYear = int(input("Your birthyear? "))

age = today.year - birthYear

if (age >=201):
    print("hi old man")
else:
    print("you're kid go home")

