print("Welcome to The Pony Picker 3000")
print("Answer questions to find which My Little Pony character you are!")

ans = input("dawn or dusk?")
if ans == "dawn":
    ans = input("spring (spr) or summer (sum)?")
    if ans == "spr":
        ans = input("Red (r) or orange (o)?")
        if ans == "r":
            print("You are Rainbow Dash!")
        else:
            print("You are Apple Jack!")
ans = input("dawn or dusk?")
if ans == "dawn":
    ans = input("spring (spr) or summer (sum)?")
    if ans == "sum":
        ans = input("Yellow (y) or green (g)?")
        if ans == "y":
            print("You are Princess Celestia!")
        else:
            print("You are Fluttershy!")
ans = input("dawn or dusk?")
if ans == "dusk":
    ans = input("winter (win) or autumn (aut)?")
    if ans == "win":
        ans = input("Blue (b) or Purple (p)?")
        if ans == "b":
            print("You are Rarity!")
        else:
            print("You are Twilight Sparkle!")
ans = input("dawn or dusk?")
if ans == "dusk":
    ans = input("winter (win) or autumn (aut)?")
    if ans == "aut":
        ans = input("Pink (pi) or Black (bl)?")
        if ans == "pi":
            print("You are Pinkie Pie!")
        else:
            print("You are Princess Luna!")
