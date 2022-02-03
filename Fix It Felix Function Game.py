"""
Brayden Sherrod
(Fix It Felix Function Game)
Period: 6
"""
import time

#Winning and lose function
def play_again():
    answer = input("> ").lower().split()
    if len(answer) == 0:
        play_again()
    else:
        if answer[0] in ['yes', 'ya', 'sure', 'yea']:
            reset()
        else:
            print("Ok bye \nThanks for playing")
            exit()
        
def lose():
    print("You lose \nWould you like to try again?")
    play_again()

def win():
    print("You Win!!!! \nWould you like to play again?")
    play_again()

#Functions for the different actions the user can do
    
#Enter Function
def enter(place):
    global point, mansion_window
    if point == 44 and mansion_window == True:
        go('south')
    else:
        print("You can't")

#Show inventory function
def show_inventory():
    global inventory
    if len(inventory) > 0:
        print(inventory)
    else:
        print("You have no items in your inventory")

#Show commands function
def show_commands():
    print("Go 'direction' (North, South, etc.) \nEnter \nGet 'item' \nDrop 'item' \nOpen 'object' \nClose 'object' \nFix 'object' \nInventory \nKill or lose (makes you lose)")
    
#Fix Function
def fix(item):
    if point in [25]:
        if item == '':
            print("I don't know what to fix")
        elif item in ['light', 'lightbulb']:
            if 'ladder' in inventory and 'lightbulb' in inventory and 'screwdriver' in inventory:
                print(item, "fixed")
                win()
            else:
                print("You don't have the correct tools")
        else:
            print(item, "doesn't need fixing")
    else:
        print("There is nothing to fix in this room")
        
#Open and close Functions
def openobject():
    global mansion_window
    if point == 44:
        if mansion_window == False:
            mansion_window = True
            print("The window is open")
        else:
            print("The window is already open")
    else:
        print("You can't")

def closeobject():
    global mansion_window
    if point == 44:
        if mansion_window == True:
            mansion_window = False
            print("The window is closed")
        else:
            print("The window is already closed")
    else:
        print("You can't")
        
#Get and drop functions
def get(item):
    global point
    grabble_rooms = [15, 16, 25, 26]
    grabble_stuff = [['screwdriver', 'ladder', 'hammer', 'rope'], ['knife', 'spoon', 'fork',], ['tv'],
                     ['lightbulb', 'duct-tape', 'bottle-of-invisible-ink', 'chess-set', 'wrench', 'scissors']]
    if len(inventory) < 3:
        if point in grabble_rooms:
            grabble_stuff = [['screwdriver', 'ladder', 'hammer', 'rope'], ['knife', 'spoon', 'fork',], ['tv'],
                             ['lightbulb', 'duct-tape', 'bottle-of-invisible-ink', 'chess-set', 'wrench', 'scissors']]
            if item in grabble_stuff[grabble_rooms.index(point)]:
                inventory.append(item)
                print(f"'{item}' taken")
            else:
                print(f"'{item}' is not an item in this room")
        else:
            print("There is nothing to grab in this room")
    else:
        print("You can't storage is full")

def drop(item):
    if item in inventory:
        inventory.remove(item)
        print(item, "dropped")
    else:
        print("You can't drop something you don't have")
        
#Go Function
def go(subtext):
    global point, room_column, room_row, mansion_window, show
    change = True
    if subtext == 'north' and not point in [42, 26, 34, 44, 54]:
        if point == 16:
            room_column = 4
            room_row = 4
        else:
            room_row += 1
    elif subtext == 'east' and not point in [33, 15, 25, 26, 52, 53, 54]:
        room_column += 1
    elif subtext == 'south' and not point in [15, 25, 32, 42, 52]:
        if point == 44 and mansion_window == True:
            room_column = 1
            room_row = 6
        elif point == 44:
            print("The window is closed \nYou can't")
            change = False
        else:
            room_row -= 1
    elif subtext == 'west' and not point in [53, 25, 15, 16, 32, 33, 34]:
        room_column -= 1
    elif subtext == 'northwest' and not point in [52, 15, 16, 26, 32, 33, 34, 44, 54]:
        room_row += 1
        room_column -= 1
    elif subtext == 'southwest' and not point in [54, 15, 25, 16, 32, 33, 34, 42, 52]:
        room_row -= 1
        room_column -= 1
    elif subtext == 'northeast' and not point in [32, 25, 26, 16, 52, 53, 54, 44, 34]:
        room_row += 1
        room_column += 1
    elif subtext == 'southeast' and not point in [34, 15, 25, 26, 32, 42, 52, 53, 54]:
        room_row -= 1
        room_column += 1
    else:
        print("You Can't")
        change = False
    point = int((f"{room_column}{room_row}"))
    if change == True:
        print(places[point])
        print(info[point])
        if point == 25 and not show == True:
            time.sleep(5)
            print("Now the light is flickering")
            time.sleep(2)
            print("That can't be good")
            time.sleep(2)
            print("Now the light is out")
            show = True
        elif point == 25 and show == True:
            print("And the light is still broke")
        
#Function to check the user iput to run the correct operation
def testverb(verb, subtext):
    if verb in ['go', 'move'] and subtext in ['north', 'south', 'east', 'west', 'northwest', 'southwest', 'northeast', 'southeast']:
        go(subtext)
    elif verb in ['get', 'grab', 'steal', 'take']:
        get(subtext)
    elif verb in ['drop', 'throw']:
        drop(subtext)
    elif verb in ['open']:
        openobject()
    elif verb in ['i', 'inventory']:
        show_inventory()
    elif verb in ['c', 'commands', '?']:
        show_commands()
    elif verb in ['close']:
        closeobject()
    elif verb in ['fix']:
        fix(subtext)
    elif verb in ['enter'] and subtext in ['house', 'window', 'inside'] or verb in ['enter'] or verb in ['go', 'move'] and subtext in ['inside', 'in', 'through']:
        enter(subtext)
    elif verb in ['lose', 'kill', 'die']:
        lose()
    elif subtext == '':
        print("I need more information")
    else:
        if verb in ['go', 'move']:
            print("I don't know the word", f"'{subtext}'")
        else:
            print("I don't know the word", f"'{verb}'" )

#Reset Variables before being used inside functions
def reset():
    global room_column, room_row, point, inventory, mansion_window, light_bulb_fixed, show
    inventory =[]
    show = False
    light_bulb_fixed = False
    mansion_window = False
    room_column = 4
    room_row = 2
    point = int((f"{room_column}{room_row}"))
    level_one()

#Each 'place' is a room based on its point on the coordinate plane
places = {61 : 'Room 61', 62 : 'Room 62', 63 : 'Room 63', 64 : 'Room 64', 65 : 'Room 65', 66 : 'Room 66',
          51 : 'Room 51', 52 : 'South East Corner of the Yard', 53 : 'East of Mansion', 54 : 'North East Corner of the Yard', 55 : 'Room 55', 56 : 'Room 56',
          41 : 'Room 41', 42 : 'South of Mansion', 43 : 'Mansion', 44 : 'North of Mansion', 45 : 'Room 45', 46 : 'Room 46',
          31 : 'Room 31', 32 : 'South West Corner of the Yard', 33 : 'West of Mansion', 34 : 'North West Corner of the Yard', 35 : 'Room 35', 36 : 'Room 36',
          21 : 'Room 21', 22 : 'Room 22', 23 : 'Room 23', 24 : 'Room 24', 25 : 'Living Room', 26 : 'Dining Room',
          11 : 'Room 11', 12 : 'Room 12', 13 : 'Room 13', 14 : 'Room 14', 15 : 'Garage', 16 : 'Kitchen'
          }    
#Info for each room which is displayed when ever the user changes rooms
info = {61 : '61 info', 62 : '62 info', 63 : '63 info', 64 : '64 info', 65 : '65 info', 66 : '66 info', 51 : '51 info',
        52 : 'There is only some trees here',
        53 : 'The Mansion is to the west but there is no way in',
        54 : "There's nothing here for you", 55 : '62 info', 56 : '62 info', 41 : '41 info',
        42 : 'The Mansion is to the north and there is no entrance', 43 : '62 info',
        44 : 'All of the windows on this side are closed but one is not locked', 45 : '62 info', 46 : '62 info', 31 : '31 info',
        32 : 'Well this might have been a garden at some point, but there is nothing to do here',
        33 : 'The Mansion is to the east, all the doors and windows are locked shut',
        34 : 'There is only dirt and dead grass here', 35 : '62 info', 36 : '62 info', 21 : '21 info', 22 : '22 info', 23 : '62 info', 24 : '62 info',
        25 : 'You see a couch facing towards the flat screen TV on the wall \nIn the center of the room there is a coffee table with a light high above it',
        26 : 'There is a few random items on the dining table including \nA chess-set, a wrench, a lightbulb, a roll of duct-tape, \nA bottle-of-invisible-ink, and a pair of scissors.',
        11 : '11 info', 12 : '12 info', 13 : '62 info', 14 : '62 info',
        15 : 'You see a hammer, a screwdriver, and a rope on the shelf to the right \nNext to the shelf there is a ladder leaning against the wall.',
        16 : 'There is a steak knife, a fork, and a spoon set out on the counter, \nBut no food.'
        }

#Initialize the game
inventory = []
show = False
mansion_window = False
room_column = 4
room_row = 2
point = int((f"{room_column}{room_row}"))

def main():
    while True:
        command = input("> ").lower().split()
        if len(command) == 0:
            continue
        verb = command[0]
        if len(command) == 2 or len(command) > 2:
            subtext = command[1]
        else:
            subtext = ''
        testverb(verb, subtext)
        
#Levels
def level_one():
    print("Welcome to 'Fix It Felix' \n"
          "You are Felix \nYour goal is to fix all the things that need fixing! \n"
          "There is an old Mansion to the North \nThe Mansion needs some interior repairs \nBut, all the doors and windows on this side are locked shut \nType '?' to see the command options \n")
    main()

level_one()  
