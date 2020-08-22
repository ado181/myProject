print("Welcome to myProgram")
password = input('Enter password: ')
password = "imNoob"
gues = ""
if gues == password:
    print("You have access to myProgram")
elif gues != password:
    gues = input("enter the password again: ")
    while gues != password:
        gues = input("password wrong, try again: ")

print("")
print("")
print("You have access to myProgram")
print("")
print("Options:")
print("1. make blin")
print("2. squat")
print("3. drink kvass")
print("")
print("choose the number")
choose = "1"
choo = "2"
ch = "3"
activity = ""
activity = input("What do you want to do? ")
while activity != choose and activity != choo and activity != ch:
    print("")
    print("Thats not in this program :(")
    activity = input("please choose again: ")
if activity == choose:
    print("")
    print("You know how to make blin?")
    answer = input("yes/no: ")
    while answer != "yes" and answer != "no":
        print("")
        print("I don't know what do you mean, please answer again")
        answer = input("yes/no: ")
    if answer == "yes": print("okay")
    elif answer == "no" :
        print("")
        print("i will guide you")
        print("")
        print("you will learn from this program or from youtube?")
        blinmaker = input("program/youtube: ")
        while blinmaker != "program" and blinmaker != "youtube":
            blinmaker = input("what do you mean by " +blinmaker+ "? ")
        if blinmaker == "youtube":
            print("here is your youtube link: ")
            print("https://www.youtube.com/watch?v=5UOowIxfX88&t=55s")

        elif blinmaker == "program" :
            print("follow my instruction")
            print("")
            milk = input("how much milk do you have in milli liter? ")
            print("you have " +milk+ " ml milk")
            print("")
            flour = input("how much flour do you have in gram? ")
            print("you haye " +flour+ " g flour")
            print("")
            egg = input("how many egg do you have? ")
            print("you have "+egg+ " egg(s)")
            print("")
            sugar = input("you have sugar? yes/no: ")
            while sugar != "yes" and sugar != "no":
                sugar = input("please write correctly: ")
            if sugar == "yes":
                print("you have sugar")
                print("")
            elif sugar == "no":
                print("you dont have sugar")
                print("")
            salt = input("you have salt? yes/no: ")
            while salt != "yes" and salt != "no":
                salt = input("please write correctly: ")
            if salt == "yes":
                print("you have salt")
                print("")
            elif salt == "no":
                print("you dont have salt")
                print("")
            cooking_oil = input("you have cooking oil? yes/no: ")
            while cooking_oil != "yes" and cooking_oil != "no":
                cooking_oil = input("please write correctly: ")
            if cooking_oil == "yes":
                print("you have salt")
                print("")
            elif cooking_oil == "no":
                print("you dont have cooking oil")
                print("")
            if milk == "100" and flour == "100" and egg == "1" and sugar == "yes" and salt == "yes" and cooking_oil == "yes":
                print("")
                print("")
                print("")
                print("here the step:")
                print("Step 1: Beat together the milk and the eggs. Stir in the salt and the sugar and mix well. Add the baking soda and citric acid.")
                print("Step 2: Blend in the flour. Add the vegetable oil and pour in the boiling water, stirring constantly. The batter should be very thin, almost watery. Set the bowl aside and let it rest for 20 minutes.")
                print("Step 3: Melt a tablespoon of butter in a small frying pan over medium-high heat. Pick the pan up off the heat. Pour in a ladleful of batter while you rotate your wrist, tilting the pan so the batter makes a circle and coats the bottom. The blini should be very thin.")
                print("Step 4: Return the pan to the heat. Cook the blini for 90 seconds. Carefully lift up an edge of the blini to see if it's fully cooked: the edges will be golden and it should have brown spots on the surface. Flip the blini over and cook the other side for 1 minute.")
                print("Step 5: Transfer the blini to a plate lined with a clean kitchen towel. Continue cooking the blini, adding an additional tablespoon of butter to the pan after each 4 blini. Stack them on top of each other and cover with the kitchen towel to keep warm.")
                print("Step 6: Spread your favorite filling in the center of the blini, and fold three times to make a triangle shape. You can also fold up all 4 sides, like a small burrito.")
                print("")
                print("")
                print("good luck:)")
            else:
                print("no blin today")

elif activity == choo:
    print("Can you squad? ")
    capability = input("yes/no: ")
    while capability != "yes" and capability != "no":
        capability = input("please write again: ")
    if capability == "yes":
        print("")
        print("have fun :v")
    elif capability == "no":
        print("how will you learn squat?")
        squat = input()
        print("you will learn squat by " +squat)

elif activity == ch:
    print("")
    print("enjoy :)")