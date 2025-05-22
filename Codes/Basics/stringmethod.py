# stings are immutanle
name = "!! !! Urval ! ! !"
print(name)
#in both folllowing case it will make new strings
print(name.upper())
print(name.lower())
print(name.rstrip("!")) # remove the next !!!
print(name.replace("Urval","Heet")) # replce Heet with Urval
print(name.split(" "))
blogHeading = "introduction tO jS"
print(blogHeading.capitalize()) # first charecter uppercase and another all lowercase
str = "Welcome to the Console!!!"
print(len(str))
print(len(str.center(50)))
print(str.center(50)) #add 25 sapce to left side
print(str)
name2 = "Urval Urval Urval Urval Urval Urval Urval"
print(name2.count("Urval"))
str1 = "Welcome to the console !!!"

print(str.endswith("!!!"))
print(str1.endswith("to",4,10))

str2 = "His name is Don. He is an honest Man."
print(str2.find("is"))
print(str2.index("is"))
str1 = "WelcomeToTheConsole"
print(str1.isalnum())
str1 = "Welcome1234"
print(str1.isalpha())
str1="hello world"
print(str1.islower())
str1="We wish you a Merry Christmas\n"
print(str1.isprintable())
str1 = "jello"
str2 = "                    "
print(str2.isspace())
print(str1.isspace())