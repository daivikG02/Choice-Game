# input for the age 
age = int(input("Enter your age to play : ")) 
choices = ["forest", "murder", "dragons"]

# age if statement
if age >= 8:

  # choices of the game
  print(choices)
  first_input = input("Choose one of the following : ")
  
    # forest input
  if first_input == "forest" or first_input == "1":

    # tree story
    print("you find yourself in a forest")
    print("no civilization in miles")
    print("you start walking..")
    print("two trees then fall, both of them had holes with light coming out")
    forest = input("Which tree do you choose? tree1 or tree2 : ")
    # tree1 story riddle
    if forest == "tree1" or forest == "1":
      print("you take a glance as you enter tree1")
      print("inside is a riddle")
      print("the riddle says - choose the correct password")
      print("it must also have to be in a minimum words")
      print("HINT: It can be squishy or hard, and come in all sizes")
      rid = input("What do you choose : ")
      # correct statement
      if len(rid) <= 5 and rid == "ball":
        print("You win this game! good work")
      # incorrect statement
      elif rid != "ball":
        print("nope you're answer is incorrect")

      # input for play again 1st attempt
        y_n = input("do you want to play again [Y/N] : ")

        # first no
        if y_n == "N":
          print("go eat dust fool")

        # first yes
        elif y_n == "Y":
          # 1st attempt
          print("1 of 3 attempts")

          print("you take a glance as you enter tree1")
          print("inside is a riddle")
          print("the riddle says - choose the correct password")
          print("it must also have to be in a minimum words")
          print("HINT: It can be squishy or hard, and come in all sizes")
          rid = input("What do you choose : ")
          # correct statement
          if len(rid) <= 5 and rid == "ball":
            print("You win this game! good work")
          # incorrect statement
          elif rid != "ball":
            print("nope you're answer is incorrect")

            y_n = input("do you want to play again [Y/N] : ")

            # second no
            if y_n == "N":
              print("go eat dust fool")

            elif y_n == "Y":
              # 2nd attempt
              print("2 of 3 attempts")

              print("you take a glance as you enter tree1")
              print("inside is a riddle")
              print("the riddle says - choose the correct password")
              print("it must also have to be in a minimum words")
              print("HINT: It can be squishy or hard, and come in all sizes")
              rid = input("What do you choose : ")
              # correct statement
              if len(rid) <= 5 and rid == "ball":
                print("You win this game! good work")
              # incorrect statement
              elif rid != "ball":
                print("nope you're answer is incorrect")

                # 3rd input
                y_n = input("do you want to play again [Y/N] : ")
                # third no
                if y_n == "N":
                  print("go eat dust fool")

                elif y_n == "Y":
                  # 3rd attempt
                  print("3 of 3 attempts")

                  print("you take a glance as you enter tree1")
                  print("inside is a riddle")
                  print("the riddle says - choose the correct password")
                  print("it must also have to be in a minimum words")
                  print("HINT: It can be squishy or hard, and come in all sizes")
                  rid = input("What do you choose : ")
                  # correct statement
                  if len(rid) <= 5 and rid == "ball":
                    print("You win this game! good work")
                  # incorrect statement
                  elif rid != "ball":
                    print("nope you're answer is incorrect")
                    print("sorry, you have used up all three tries... better luck next time")

    # tree2 story
    if forest == "tree2" or forest == "2":
      print("you enter tree2")
      print("as you enter, poison gets in and kills you")
      print("THE END, better luck next time.")

  # murder
  if first_input == "2" or first_input == "murder":
    print("you enter a forest...")
    print("you find two paths, one with trees, another with more trees, but taller")
    murd = input("Which path do you choose? trees, or tall trees : ")
    if murd == "trees" or murd == "1":
      print("you chose trees, so you look around, and there's nothing but trees")
      print("you find two knives come past you")
      murd1 = input("Will you duck or stay up : ")
      if murd1 == "duck" or murd1 == "1":
        print("two knives come at you from beneath and kill you The end... better luck next time")
      elif murd1 == "stay up" or murd1 == "2":
        print("the two knives pierce you. The end, better luck next time")
    if murd == "tall trees" or murd == "2":
      print("tall trees are everywhere, you're soon lost")
      print("animals creep towards you")
      print("you then die... better luck next time")

  # dragons
  if first_input == "3" or first_input == "dragons":

    print("You enter a land filled with dragons")
    print("then you see two dragons")
    drag = input("Which dragon do you choose - the t-rex dragon, or the rhinodragon : ")
    if drag == "t-rexdragon" or drag == "1":
      print("As soon as you touch the t-rex, it blows fire")
      print("and you die")
      print("better luck next time.")
    elif drag == "rhinodragon" or drag == "2":
      print("you get on it")
      print("and it starts flying")
      print("but then it tilts")
      print("you fall")
      print("better luck next time")

# for young age
else:
  print("you are too young to play")
  
