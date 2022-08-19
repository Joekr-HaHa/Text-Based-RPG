import cmd
import textwrap
import sys
import os
import time
from random import randint
import turtle
battlewon=False
screen_width=100

##### Player Setup ####

class player():
    def __init__(self):
        self.name=''
        self.hp=0
        self.water=0
        self.balance=0
        self.fear=0
        self.skeleton=''
        self.location='a1'
        self.connected=False
        self.camera=False
        self.picture=False
        self.sbclue=False
        self.followed=False
        self.dead=0
        self.socialclue=False
myPlayer=player()
#### Battle #######
def battle(enemytype):
  global battlewon
  class Person(object):
    tired=0
    def __init__(self):
      self.health=100
      self.multi=False
    def battle2(self):
      hit=randint(0,20)
      if self.tired==3:
        self.tired=0
        return "You missed because you ran out of stamina!!"
      elif hit in ([x for x in range(0,20) if x%2==0]):
        enemy.health-=10
        self.tired=self.tired+1
        if role.lower()=="tank":
          self.tired=self.tired+1
        if self.multi==True:
          hit=randint(0,20)
          multich=randint(0,99)
          if hit==multich:
            enemy.health-=10
            print("Multi-Hit!!")
            return "Enemy Health: {}, Your Health: {}".format(enemy.health,player.health)
        elif enemy.type=='soldier':
            print("Extra dmg to soldier")
            player.health-=5
            return "Enemy Health: {}, Your Health: {}".format(enemy.health,player.health)
        return "Enemy Health: {}, Your Health: {}".format(enemy.health,player.health)
      else:
        return "You missed!!"
      
  class Enemy(Person):
    def __init__(self):
      Person.__init__(self)
      self.flame=False
      self.type='soldier'
    def battle2(self):
      hit=randint(0,20)
      if self.tired==3:
        self.tired=0
        return "Enemy missed because he ran out of stamina!!"
      elif hit in([x for x in range(0,20) if x%2==0]) and self.flame==True:
        player.health-=20
        return "Boss health: {}, Your Health: {}".format(enemy.health,player.health)
        i=randint(0,20)
        if i in ([x for x in range(0,30) if x%2!=0]):
          player.health-=10
          return "Boss used flame attack, your health is now {}".format(player.health)
        
      elif hit in ([x for x in range(0,20) if x%2==0]):
        player.health-=10
        self.tired=self.tired+1
        if enemy.type=='tank':
          player.health-=10
          self.tired=self.tired+1
        elif enemy.type=='speed':
          self.tired=self.tired-1
          hit=randint(0,20)
          multich=randint(0,99)
          if hit==multich:
            enemy.health-=10
            print("Multi-Hit!!")
            return "Enemy Health: {}, Your Health: {}".format(enemy.health,player.health)
          elif role=='soldier':
            print("Extra dmg to soldier")
            player.health-=5
            return "Enemy Health: {}, Your Health: {}".format(enemy.health,player.health)
        return "Enemy Health: {}, Your Health: {}".format(enemy.health,player.health)
      else:
        return "Enemy missed!!"
  x=0
  enemy=Enemy()
  player=Person()
  erole=['soldier','tank','speed']
  erole1=erole[randint(0,len(erole)-1)]
  enemy.type=erole1
  if enemytype=='tank':
    enemy.health=150
    enemy.multi=False
  elif enemytype=='speed':
    enemy.health=150
    enemy.multi=True
  else:
    enemy.health=100
    enemy.multi=False
  print ("Enemy type is {}".format(enemy.type))
  while x==False:
    role=input("Pick a fight style. (speed, soldier or tank)  ")
    if role.lower()=="speed":
      player.health=80
      player.multi=True
      x=True
    elif role.lower()=="tank":
      player.health=150
      player.multi=False
      x=True
    elif role.lower()=="soldier":
      player.health=100
      player.multi=False
      x=True
    else:
      x=False
  bosschance=101#[x for x in range(0,10)]
  if bosschance==randint(0,100):
    enemy.health=250
    enemy.multi=True
    enemy.flame=True
  
  # Main Game Loop  
  for counter in range(20):
    while player.health>0 and enemy.health>0:
      print(player.battle2())
      print(enemy.battle2())
  if enemy.health==player.health:
    print("Draw")
  elif player.health<=0:
    print("Enemy Wins!!")
    battlewon=False
    return battlewon
  else:
    print("You win!!")
    battlewon=True
    return battlewon



#### Title Screen ####

def title_screen_selections():
    option=input("> ")
    if option.lower()==("play"):
        setup_game()
    elif option.lower()==("help"):
        help_menu()
    elif option.lower()==("quit"):
        sys.exit()
    while option.lower() not in ['play','help','quit']:
        print("Please enter a valid command")
        option=input("> ")
        if option.lower()==("play"):
            setup_game()
        elif option.lower()==("help"):
            help_menu()
        elif option.lower()==("quit"):
            sys.exit()
def title_screen():
    os.system('cls')
    print('#####################')
    print('# Welcome to my RPG!#')
    print('#####################')
    print('--------Play---------')
    print('--------Help---------')
    print('--------Quit---------')
    print('Copyright 2019 joe.me')
    title_screen_selections()

def help_menu():
    print('#####################')
    print('# Welcome to my RPG!#')
    print('#####################')
    print('Type move then press enter then type direction to move')
    print('You start on the top left of the map')
    print('Use "look" to inspect something')
    print('If you need help, type hint')
    print('Good luck and have fun!')
    title_screen_selections()
##### Game Interactivity #####
def clueoption():
        loc=zonemap[myPlayer.location][ZONENAME]
        if myPlayer.followed==True:
            clue2=input("You wander into the forest....")
            puzzle2(clue2)
        elif loc=='An Outpost':
            clue=input(print("The campsite has SLEEPING BAGS, a CAMPFIRE and BACKPACKS or you can LEAVE"))
            puzzle(clue)
        elif loc=="Joe's Goods":
            clue1=input(print("The store is nicely furnished with stocked SHELVES, a barren COUNTER and a massive FRIDGE or you can LEAVE"))
            puzzle1(clue1)
def puzzle(clue):
    if clue.lower()=='hint':
        clue=input(print("The ground is interactible"))
    elif clue.lower()=='sleeping bags':
        print("These sleeping bags are still warm")
        print("They look new")
        sb=input(print("Investigate the inside or outside of the bag?"))
        if sb.lower()=='inside':
            print("You check each bag one-by-one")
            print("You check the first, nothing is in it apart from blackened dirt, it's warm to the touch")
            print("You crawl across to the left inside the dirty tent")
            print("You check the second bag, you feel something cool against your touch, you pull it out")
            print("You have acquired the CAMERA")
            myPlayer.camera=True
            sb1=input(print("Check the outside?"))
            if sb1 in ['yep','yes','ok','okay','outside','k']:
                print("You check the outside of the first bag")
                print("It says:")
                print("J-e-- ---ds")
                print("You check the second, slightly older-looking bag, it has a note on it")
                print("Emma Sharkerton")
                print("That must be her name")
                myPlayer.sbclues=True
                clueoption()
            else:
                clueoption()
        elif sb.lower()=='outside':
            print("You check the outside of the first bag")
            print("It says:")
            print("J-e-- ---ds")
            print("You check the second, slightly older-looking bag, it has a note on it")
            print("Emma Sharkerton")
            print("That must be her name")
            myPlayer.sbclues=True
            sb1=input(print("Check the inside?"))
            if sb1 in ['yep','yes','ok','okay','outside','k']:
                print("You check each bag one-by-one")
                print("You check the first, nothing is in it apart from blackened dirt, it's warm to the touch")
                print("You crawl across to the left inside the dirty tent")
                print("You check the second bag, you feel something cool against your touch, you pull it out")
                print("You have acquired the CAMERA")
                myPlayer.camera=True
            else:
                clueoption()
    elif clue.lower()=='campfire':
        print('You look at the campfire, there is food cooking on it')
        print('There is a muddy picture on the ground next to it')
        print('Where are these people?')
        print('What happened to them?')
        #output picture here
        clueoption()
    elif clue.lower()=='backpack':
        print("You look at the backpack, it's new")
        print("It still has tags in and it's empty")
        clueoption()
    elif clue.lower()in['ground','floor','dirt','mud']:
        print("You look at the floor, there are footprints")
        #maybe picture
        print("They're red, how peculiar")
        clueoption()
    elif clue.lower()in['follow trail','follow footprints','follow']:
        #skip ahead in game
        myPlayer.followed=True
        clueoption()
    elif clue.lower()=='leave':
        prompt()
    else:
        print("Invalid Object, Try Again")
        clueoption()
def puzzle1(clue1):
    if clue1.lower()=='shelves':
        print("The shelves look mostly newly stocked")
        shcl=input(print("Check what section of shelves?\nSURVIVAL, GROCERIES, FRESH FOODS or ENTERTAINMENT"))
        if shcl.lower() in ['groceries','fresh foods','entertainment']:
            print("The shelves are full and untouched")
            clueoption()
        elif shcl.lower()=='survival':
            print("It looks as though something ravenous has been down this aisle")
            print("The shelves are toppled, goods on the floor and all food and equipment seems to be gone")
            print("There are muddy footprints on the floor")
            #maybe picture
            print("Whoever stole these was in a hurry")#italics, different colour
            clueoption()
    elif clue1.lower()=='counter':
            print("It's mostly empty, but there is some money and a pin")
            steal=input(print("Steal from the register?"))
            if steal in['yes','yup','yep','ok','k']:
                print("You took MONEY and a COMMEMORATIVE PIN")
                myPlayer.pin=True
                clueoption()
            else:
                clueoption()
    elif clue1.lower()=='fridge':
            print("You open the fridge with a steamy hiss")
            print("Horrified, you see nothing...")
            print("Apart from..\n a handprint was smeared in the dirt encrusting the side of the fridge")
            print("The inside of the fridge itself seemed pinkish in colour")
            clueoption()
    elif clue1=='leave':
            prompt()
def puzzle2(clue2):
  print("You hear a faint shriek in the distance, it could be an owl")
  if myPlayer.camera!=True:
    print("You can't see, go back")
    cantsee=input("Do you want to go back?")
    if cantsee.lower() in ['yes','yep','okay','go',' go back']:
      print("You go back to the campsite")
      myPlayer.followed=False
      clueoptions()
    elif cantsee.lower() in ['go forward','stay','no','nope']:
      print("You fumble through the darkness")
      time.sleep(0.08)
      print("The darkness starts to envelop you")
      time.sleep(0.1)
      print("You feel something at your feet")
      time.sleep(0.1)
      print("It's cold and smooth")
      time.sleep(0.05)
      print("You feel it wrapping around your leg")
      battle1=input("What do you do? (attack or run?)")
      if battle1 in['fight','hit','kick','attack']:
        enemytype='speed'
        battle(enemytype)
        if battlewon==False:
          print("Ouch, you died")
          dead()
        else:
          print("Oops, you weren't meant to win")
          dead()
      elif battle1 in['run','go','hide']:
        print("You start to run")
        print("It's still on your leg")
        print("You feel it's fangs bite into your skin")
        print("You fall")
        time.sleep(0.2)
        print("Everything becomes dark")
        dead()
  elif myPlayer.camera==True:
    print("You venture further into the forest")
    print("You see a snake dart toward you")
    print("You kick the snake")
    print("The snake soars through the air and disappears into the fog")
    print('"Fog...I didn\'t notice any fog..."')
    print("The fog starts to surround you as you venture on")
    print("If you venture beyond this point, you cannot go back")
    fog=input("Continue into the fog?")
    if fog.lower()in['y','yes']:
        fog_venture()
    else:
        myPlayer.followed=False
        clueoption()
def fog_venture():
    os.system('cls')
    os.system('color f1')
    time.sleep(4)
    print("Something feels...")
    time.sleep(4)
    print("O\nd\nd")
    time.sleep(3)
    print("Light flickers before your eyes as your torch struggles to stay on")
    time.sleep(3)
    print("You check your phone")
    time.sleep(3)
    print("No signal")
    time.sleep(3)
    print("You look up at your surroundings")
    time.sleep(3)
    print("There is only darkness")
    time.sleep(3)
    os.system('cls')
    os.system('color f2')
    print("All of a sudden there is a sudden flash of light")
    time.sleep(3)
    os.system('cls')
    print("A faint outline of something materialises in the distance")
    time.sleep(2)
    print("It seems to resemble a man")
    time.sleep(2)
    print("THE BEING starts to approach you!!!!")
    time.sleep(2)
    talk=input("Wait for THE BEING or run?")
    if talk.lower() in ['wait','w','stay','yes']:
        talk_being()
    else:
        run_being()
def talk_being():
    os.system('cls')
    time.sleep(2)
    print("THE BEING stands before you")
    time.sleep(2)
    print("You notice that it's still silhouetted")
    time.sleep(2)
    os.system('cls')
    os.system('color 52')
    for letter in '"HELLO"':
        time.sleep(0.3)
        sys.stdout.flush()
        sys.stdout.write(letter)
    os.system('color 00')
    time.sleep(2)
    print("\nYou notice the creature is holding an odd glowing device")
    time.sleep(2)
    print("Look at the phone?")
    look=input("> ")
    if look in ['yes','y']:
        os.system('color f2')
        time.sleep(2)
        print("The phone has pictures on it")
        time.sleep(2)
        print("The pictures resemble family photos")
        time.sleep(2)
        print("THE BEING isn't in half of the photos")
        time.sleep(2)
        myPlayer.socialclue=True
        print("SOCIAL clue unlocked")
    talk_creature()
def run_being():
    time.sleep(2)
    print("You start to run, but you feel..")
    time.sleep(1.5)
    print("You feel as though you are wading through water")
    time.sleep(1.7)
    l1="You try to run, but you get"
    for letter in l1:
        time.sleep(0.7)
        sys.stdout.write(letter)
    l1="Slower, and \n slower and \n slower..."
    for letter in l1:
        time.sleep(1)
        sys.stdout.write(letter)
    print("You freeze as you feel a cold touch on your shoulder")
    talk_creature()
def dead():
  print("You died a horrible death")
  retry=input("Start again?")
  if retry in['yes','start again','retry']:
    myPlayer.dead+=1
    title_screen()
  else:
    quit()
def talk_creature():
    pass
        
    ##murder mystery##
    ##give them clues and evidence##
    ##let them figure it out##
    ##one location leads to another##
    ##eventually get killed, but can escape by fighting back##
    ##last quote in game hints at going away or escaping##
    ##lead onto move_away or escaping through the way out##
def print_location():
    print ('\n'+('#'*(4+len(zonemap[myPlayer.location][ZONENAME]))))
    print('# '+(zonemap[myPlayer.location][ZONENAME]).upper()+' #')
    print('#' + zonemap[myPlayer.location][DESCRIPTION]+ ' #')
    print ('\n'+('#'*(4+len(zonemap[myPlayer.location][ZONENAME]))))
### jzcb£%$jwsmam)&* ###
def move_away():
    return
def wrong_name():
    ###dsjabsdbuysabyu21392199 controls###
    '''Example
screen = turtle.Screen()

# this assures that the size of the screen will always be 400x400 ...
screen.setup(400, 400)

# ... which is the same size as our image
# now set the background to our space image
screen.bgpic("space.jpg")

# Or, set the shape of a turtle
screen.addshape("rocketship.png")
turtle.shape("rocketship.png")

move_speed = 10
turn_speed = 10

# these defs control the movement of our "turtle"
def forward():
  turtle.forward(move_speed)

def backward():
  turtle.backward(move_speed)

def left():
  turtle.left(turn_speed)

def right():
  turtle.right(turn_speed)

turtle.penup()
turtle.speed(0)
turtle.home()

# now associate the defs from above with certain keyboard events
screen.onkey(forward, "Up")
screen.onkey(backward, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.listen()'''
    
    sc.listen() #listens for keyboard input
    sc.onkeypress(jamesup,"w"or"Up")
    sc.onkeypress(jamesdown,"s"or"Down")
    sc.onkeypress(jamesleft,"a"or"Left")
    sc.onkeypress(jamesright,"d"or"Right")


    def jamesup():
        y=james.ycor()
        y+=20
        james.sety(y)
    def jamesdown():
        y=james.ycor()
        y-=20
        james.sety(y)
    def jamesleft():
        x=james.xcor()
        x-=20
        james.setx(x)
    def jamesright():
        x=james.xcor()
        x+=20
        james.setx(x)
## prompt ##
def prompt():
    loc=zonemap[myPlayer.location][ZONENAME]
    print("""
    ----------------------------------------------------
    |   An Outpost  | Gas Station | Grandparent's Home |
    ----------------------------------------------------
    |  Joe's Goods  |   Stables   |     Crop Field     |
    ----------------------------------------------------
    | Train Station | Wishing Well|     The Way Out    |
    ----------------------------------------------------
    """)
    print("You are at",loc)
    print("\n"+"================================")
    print("What would you like to do?")
    action=input("> ")
    acceptable_actions=['move', 'go', 'travel', 'walk', 'quit', 'examine', 'inspect', 'interact', 'look']
    while action.lower() not in acceptable_actions:
        print("Unknown action, try again. \n")
        action= input("> ")
    if action.lower()=='quit':
        sys.exit()
    elif action.lower() in ['move','go','travel','walk']:
        player_move(action.lower())
    elif action.lower() in ['examine', 'inspect']:
        clueoption()
    elif action.lower() in ['look','see','peer','hint']:
        player_examine(action.lower())
def player_move(action):
    ask=("Where would you like to move to?\n")
    dest=input(ask)
    if dest in ['up','north']:
        destination=zonemap[myPlayer.location][UP]
        movement_handler(destination)
    elif dest in ['left','west']:
        destination=zonemap[myPlayer.location][LEFT]
        movement_handler(destination)
    elif dest in ['right','east']:
        destination=zonemap[myPlayer.location][RIGHT]
        movement_handler(destination)
    elif dest in ['down','south']:
        destination=zonemap[myPlayer.location][DOWN]
        movement_handler(destination)
    elif dest is 'away':
        move_away()

def movement_handler(destination):
    loc=zonemap[myPlayer.location][ZONENAME]
    myPlayer.location=destination
    print_location()

def player_examine(action):
    if zonemap[myPlayer.location][SOLVED]:
        print("You've already connected this area")
        print(zonemap[myPlayer.location][EXAMINATION])
    else:
        print("You can help connect this area")
        print(zonemap[myPlayer.location][EXAMINATION])
###### The Game Functions ######


def main_game_loop():
    while myPlayer.connected is False:
        prompt()
    #here handle if puzzles have been solved
def setup_game():
    os.system('cls')
    #name collecting
    q1="Hello, what's your name?\n"
    for character in q1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    player_name=input("> ")
    myPlayer.name=player_name

    #Skeleton Selection
    q2=("What buff do you want?\n Power or Speed?\n")
    for character in q2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    player_skeleton=input("> ")
    valid_skeletons=["power","speed"]
    if player_skeleton.lower() in valid_skeletons:
        myPlayer.skeleton=player_skeleton
        print("You now have a "+player_skeleton+" buff; it does what it says on the tin\n")
    else:
        while player_skeleton.lower not in valid_skeletons:
            player_skeleton=input("> ")
            if player_skeleton.lower() in valid_skeletons:
                myPlayer.skeleton=player_skeleton
                print("You now have a "+player_skeleton+" buff; it does what it says on the tin\n")
                
    if myPlayer.skeleton is 'power':
        self.hp=120
        self.water=80
    elif myPlayer.skeleton is 'speed':
        self.hp=100
        self.water=100

        #INTRODUCTION
    q3=("Welcome "+player_name+" nice "+player_skeleton+" buff you have there\n")
    os.system('cls')
    speech1=("Welcome to Orely\n")
    for character in speech1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    speech2=("This is a small town, connected by roads\n")
    for character in speech2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    speech3=("You are a PI\n")
    for character in speech3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    speech4=("Don't stray off the path "+player_name+"\n")
    for character in speech4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    speech6=("Find out what happened here\n")
    for character in speech6:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    if player_name.lower() in ['no','none of your business','james']:
        speech5=("\033[3;31;40m Never question your objective\n]")
        for character in speech5:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.2)
        wrong_name()
    os.system('cls')
    print('########################')
    print('#   Help Us Reconnect  #')
    print('########################')
    print("""
    ----------------------------------------------------
    |   An Outpost  | Gas Station | Grandparent's Home |
    ----------------------------------------------------
    |  Joe's Goods  |   Stables   |     Crop Field     |
    ----------------------------------------------------
    | Train Station | Wishing Well|     The Way Out    |
    ----------------------------------------------------
    """)
    main_game_loop()



    
###The Map####
"""
-------
| | | |
-------
| | | |
-------
| | | |
-------
| | | |
-------
"""
ZONENAME=''
DESCRIPTION='description'
EXAMINATION='examine'
SOLVED=False
UP='up','north'
DOWN='down','south'
LEFT='left','west'
RIGHT='right','east'

solved_places={'a1': False, 'a2': False, 'a3': False,
               'b1': False, 'b2': False, 'b3': False,
               'c1': False, 'c2': False, 'c3': False,
               'c1': False, 'c2': False, 'c3': False}
zonemap={
    'a1':{
        ZONENAME:"An Outpost",
        DESCRIPTION:"Sleeping bags here, looks like it's been recently deserted",
        EXAMINATION:'The food is still warm, so are the sleeping bags',
        SOLVED:False,
        UP:'c1',
        DOWN:'b1',
        LEFT:'a3',
        RIGHT:'a2'},
    'a2':{
        ZONENAME:"Gas Station",
        DESCRIPTION:'Run by Jack, he is not currently here...',
        EXAMINATION:"Looks like it hasn't been used in a while",
        SOLVED:False,
        UP:'c2',
        DOWN:'b2',
        LEFT:'a1',
        RIGHT:'a3'},
    'a3':{
        ZONENAME:"Your temporary home",
        DESCRIPTION:'Your grandparents let you stay here',
        EXAMINATION:"It's a neat old house, furnished with plush antiques",
        SOLVED:False,
        UP:'c3',
        DOWN:'b3',
        LEFT:'a2',
        RIGHT:'b1'},
    'b1':{
        ZONENAME:"Joe's Goods",
        DESCRIPTION:"The Only Store You'll ever need",
        EXAMINATION:"This looks like a fairly new construction",
        SOLVED:False,
        UP:'a1',
        DOWN:'c1',
        LEFT:'a3',
        RIGHT:'b2'},
    'b2':{
        ZONENAME:"Stables",
        DESCRIPTION:'A fairly old looking stables',
        EXAMINATION:'Smells like poop, you can hear faint whinny',
        SOLVED:False,
        UP:'a2',
        DOWN:'c2',
        LEFT:'b1',
        RIGHT:'b3'},
    'b3':{
        ZONENAME:"Crop Field",
        DESCRIPTION:'Do not enter',
        EXAMINATION:'Trespassers will be shot on sight',
        SOLVED:False,
        UP:'a3',
        DOWN:'c3',
        LEFT:'b2',
        RIGHT:'b1'},
    'c1':{
        ZONENAME:"Train Station",
        DESCRIPTION:'An old train station, looks like trains come through every 6 hours',
        EXAMINATION:"You hear a faint whistle, you're unsure wether it's the wind or a distant train",
        SOLVED:False,
        UP:'b1',
        DOWN:'a1',
        LEFT:'b3',
        RIGHT:'c2'},
    'c2':{
        ZONENAME:"Wishing Well",
        DESCRIPTION:'Do not enter',
        EXAMINATION:'Trespassers will be shot on sight',
        SOLVED:False,
        UP:'b2',
        DOWN:'a2',
        LEFT:'c1',
        RIGHT:'c3'},
    'c3':{
        ZONENAME:"The Way Out",
        DESCRIPTION:'A gate blocks your path',
        EXAMINATION:'This is the only way out of the village',
        SOLVED:False,
        UP:'b3',
        DOWN:'a3',
        LEFT:'c2',
        RIGHT:'c1'}}

title_screen()
