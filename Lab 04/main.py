import random

def main():
    miles_traveled = 0
    thirst = 0
    unicorn_tiredness = 0
    natives_miles_traveled = -20
    water_in_canteen = 5

    print("Welcome to The Desert Escape!\n")
    print("You have stolen a unicorn to make your way across the desert.")
    print("The natives want their unicorn back and are chasing you down! Survive your ")
    print("desert trek and out run the natives.\n")

    done = False
    while not done:
        print("\nWhat will you do?")
        print("A. Drink from your canteen.")
        print("B. Travel ahead at full speed.")
        print("C. Travel ahead at moderate speed.")
        print("D. Stop for the night.")
        print("E. Check status.")
        print("Q. Quit")

        user_choice = input("What is your choice? ")

        elif user_choice.upper() == "A":
            if water_in_canteen == 0:
                print("\nThere is no water left in your canteen!")
            else:
                thirst = 0
                water_in_canteen -= 1
                print("\nYou drink from your canteen, and are no longer thirsty.")
        elif user_choice.upper() == "B":
            full_speed_ahead = random.randrange(10, 21)
            miles_traveled += full_speed_ahead
            thirst += 1
            tired_speed = random.randrange(1, 4)
            unicorn_tiredness += tired_speed
            native_speed = random.randrange(1, 15)
            natives_miles_traveled += native_speed
            print("\nYou have traveled " + str(full_speed_ahead) + " miles.")
        elif user_choice.upper() == "C":
            mod_speed_ahead = random.randrange(5, 13)
            miles_traveled += mod_speed_ahead
            thirst += 1
            unicorn_tiredness += 1
            native_speed = random.randrange(1, 15)
            natives_miles_traveled += native_speed
            print("\nYou traveled " + str(mod_speed_ahead) + " miles.")
        elif user_choice.upper() == "D":
            unicorn_tiredness = 0
            print("\nYour unicorn enjoys your company a little more.")
            native_speed = random.randrange(1, 15)
            natives_miles_traveled += native_speed
        elif user_choice.upper() == "E":
            print("\nYou have traveled " + str(miles_traveled) + " miles.")
            print("You have " + str(water_in_canteen) + " drinks left in your canteen.")
            print("The natives are " + str(miles_traveled - natives_miles_traveled) + " miles behind you.")
        if user_choice.upper() == "Q":
            done = True

main()

