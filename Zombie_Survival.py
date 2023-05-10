import time
import random
import replit
days=1
def clear():
 replit.clear()
def intro():
  print("The end of the world has come")
  time.sleep(2)
  print("You are one of the last survivors on Earth")
  time.sleep(2)
  print("Scavange, Build, and fight off the Zombies")
  time.sleep(2)
def day(health,defense,energy,strength,hunger,thirst,weak,medium,strong,days,z, zombiehealth, zombieattack):
  if energy==0:
    zombiehealth=random.randint(3,5)
    zombieattack=random.randint(1,3)+days
    z=random.randint(2,3)*days
    night(days,strength,defense,health, z, zombiehealth, zombieattack,hunger,thirst)
    
  elif health <= 0:
    clear()
    print("YOUR DEAD LOL")
    time.sleep(99999999999)
  else:
    clear()
    if hunger<= 0:
      strength=strength//2
      print("Strength Impacted By Hunger")
    if thirst<=0:
      health=health - random.randint(1,15)
      print("Health impacted by thirst")
    print("A New Day Begins")
    if days == 1:
      print(str(days)+ " Day Gone")
    else:
      print(str(days)+ " Days Gone")
    print("----------------------")
    print("1: Scavange ")
    print("2: Forage")
    print("3: Build")
    print("4: Craft")
    print("5: Sleep")
    print("----------------------")
    print("Health: "+ str(health))
    print("Defense: "+ str(defense))
    print("Strength: "+ str(strength))
    print("Hunger: "+ str(hunger))
    print("Thirst: "+ str(thirst))
    print("Energy "+ str(energy))
    print("----------------------")
    print("Weak Materials: " + str(weak) + "; Medium Materials: " + str(medium) + "; Strong Materials: " +str(strong) )
    print("----------------------")
    print(''' 
              (                 ,&&&.
               )                .,.&&
              (  (              \=__/
                  )             ,'-'.
            (    (  ,,      _.__|/ /|
             ) /\ -((------((_|___/ |
           (  // | (`'      ((  `'--|
         _ -.;_/ \\--._      \\ \-._/.
        (_;-// | \ \-'.\    <_,\_\`--'|
        ( `.__ _  ___,')      <_,-'__,'
         `'(_ )_)(_)_)' ''')
    print("----------------------")
    choice=input("What Will You Choose? : ")  
    if choice == '1':
      clear()
      print("You Chose To Scavenge")
      skip=input("Enter to Continue")
      w=random.randint(3,27)
      m=random.randint(1,15)
      s=random.randint(0,5)
      weak = weak + w
      medium = medium + m
      strong = strong + s
      print("Your scavenging has left you tired but with more materials")
      print("You found "+ str(w) + " weak materials")
      print("You found "+ str(m) + " medium materials")
      print("You found "+ str(s) + " strong materials")
      print("You now have "+ str(weak) + " Weak Materials " + str(medium) + " medium materials and "+ str(strong) + " strong materials")
      skip=input("Enter to Continue")
      energy=energy-1
      day(health,defense,energy,strength,hunger,thirst,weak,medium,strong,days,z, zombiehealth, zombieattack)
    if choice == '2':
      clear()
      print("You Chose To Forage")
      skip=input("Enter to Continue")
      hunger=hunger + random.randint(10,50)    
      thirst= thirst + random.randint(50,75)
      energy=energy-1 
      print("You found some food, you now have "+ str(hunger) +" hunger" )
      print("You found some water, you now have "+ 
      str(thirst) + " thirst")
      day(health,defense,energy,strength,hunger,thirst,weak,medium,strong,days,z,zombiehealth, zombieattack)
  
    if choice == '3':
      clear()
      print("You chose to build")
      print("You have "+ str(weak) +" Weak materials")
      print("You have "+ str(medium)+ " Medium materials")
      print("You have "+ str(strong) +" Strong materials")
      print("----------------------")    
      print("1: Build with Weak materials (costs 15)")
      print("2: Build with Medium materials (costs 10)")
      print("3: Build with Strong materials (costs 7)")
      buildchoice=input("What will you choose? : ")
      if buildchoice == '1' and weak >= 15:
        print("You built defenses with weak materials")
        print("| +5 Defense")      
        print("| -15 Weak Materials")
        defense = defense + random.randint(5,15)
        weak=weak-15
      elif buildchoice == '2' and medium >= 10:
        print("You built defenses with medium materials")
        print("| +10 Defense")
        print("| -10 Medium Materials")
        defense=defense+10+random.randint(15,30)
        medium=medium-10
      elif buildchoice == '3' and strong >= 7:
        print("You built defences with strong materials")
        print("| -7 Strong Materials")
        print("| + 15 Defense")
        defense=defense+15+random.randint(20,50)
        strong=strong-7
      else:
        print("Your broke as hell kid") 
      skip=input("Enter to Continue")
      energy=energy-1
      day(health,defense,energy,strength,hunger,thirst,weak,medium,strong, days,z, zombiehealth, zombieattack) 
    if choice == '4':
      clear()
      print("You chose to Craft")
      print("You have "+ str(weak) +" Weak materials")
      print("You have "+ str(medium)+ " Medium materials")
      print("You have "+str(strong) +" Strong materials") 
      print("1: Weak (Costs 15)")
      print("2: Medium (Costs 10)")
      print("3: Strong (Costs 7)")
      craftchoice=input("Craft with which materials? ")
      if craftchoice=='1' and weak >= 15:
        print("You crafted new weapons with weak materials")
        print(" +5 Strength")
        print("-15 Weak Materials")
        strength=strength + 5
        weak=weak-15
      elif craftchoice=='2' and medium >= 10:
        print("You crafted new weapons with medium materials")
        print (" +10 Strength")
        print ("-10 Medium Materials")
        strength=strength + 10
        medium=medium-10
      elif craftchoice=='3' and strong >= 7:
        print("You crafted new weapons with strong materials")
        print(" +15 stength")
        print(" -10 Strong Materials")
        strength=strength + 15
        strong=strong-7
      else:
        print("poor lol")
      skip=input("Enter to Continue")
      energy=energy-1
    if choice == '5':
      zombiehealth=random.randint(3,5)*days
      zombieattack=random.randint(1,4)+days
      z=random.randint(2,3)*days
      print("For some unknown reason, you decide to sleep")
      print("You wake up at night, although you feel rested, +2 energy tomorrow")
      energy=2
      night(days,strength, defense, health,z, zombiehealth, zombieattack,hunger,thirst)
    day(health, defense, energy, strength, hunger, thirst, weak, medium, strong, days,z, zombiehealth, zombieattack)
z=random.randint(2,3)*days
def night(days,strength, defense, health,z, zombiehealth, zombieattack,hunger,thirst):
  global energy
  zombies=random.randint(2,3)*days
  zombieattack=random.randint(1,4)+days
  zKill=0
  clear()
  print("The Sun Sets, And You Hear Something In The Distance")
  print("You Look Out Of Your Base And See "+ str(z+1) + " ZOMBIES!") 
  print("THE ZOMBIES ARE ATTACKING YOUR SHELTER!")  
  print("""                                
                                .....            
                               O O  /            
                              /<   /             
               ___ __________/_^__/           
              /(- /(\_\________   \              
              \ ) \ )_      \o     \             
              /|\ /|\       |'     |             
                            |     _|             
                            /o   __\             
                           / '     |             
                          / /      |             
                         /_/\______|             
                        (   _(    <              
                         \    \    \             
                          \    \    |            
                           \____\____\           
                           ____\_\__\_\          
                         /`   /`     o\          
                         |___ |_______|""")
  if z<=0 :
    clear()
    print("You fended off the horde for one more night")
    print("A New Day Begins")
    time.sleep(2)
    skip=input("Enter to Continue")
    energy=2+energy
    days=days+1
    hunger=hunger-random.randint(20,50)
    thirst=thirst-random.randint(30,60)
    day(health, defense, energy, strength, hunger, thirst, weak, medium, strong, days,z, zombiehealth, zombieattack)
  else:
    if zombiehealth>0:
      skip=input("Enter to Continue")
      clear()
      print("----------------------")
      defense=defense-zombieattack
      print("Zombie Did " + str(zombieattack) + " Damage To Your Structure")
      print("----------------------")
      print("""                                
                                .....            
                               O O  /            
                              /<   /             
               ___ __________/_^__/           
              /(- /(\_\________   \              
              \ ) \ )_      \o     \             
              /|\ /|\       |'     |             
                            |     _|             
                            /o   __\             
                           / '     |             
                          / /      |             
                         /_/\______|             
                        (   _(    <              
                         \    \    \             
                          \    \    |            
                           \____\____\           
                           ____\_\__\_\          
                         /`   /`     o\          
                         |___ |_______|""")
      skip=input("Enter to Continue")
    else:
      skip=input("Enter to Continue")
      clear()
      z = z-1 
      zKill=zKill+1
      zombiehealth=random.randint(3,5)*days
      print("You Killed One Zombie")
      print("The Next Zombie Approaches")
      print("""                                
                                .....            
                               O O  /            
                              /<   /             
               ___ __________/_^__/           
              /(- /(\_\________   \              
              \ ) \ )_      \o     \             
              /|\ /|\       |'     |             
                            |     _|             
                            /o   __\             
                           / '     |             
                          / /      |             
                         /_/\______|             
                        (   _(    <              
                         \    \    \             
                          \    \    |            
                           \____\____\           
                           ____\_\__\_\          
                         /`   /`     o\          
                         |___ |_______|""")

    if defense>0:
      skip=input("Enter to Continue")
      clear()      
      print("-------------------------------------- ")
      print("Your Health: " + str(health))
      print("Zombies's Health: " + str(zombiehealth))
      print("Zombies's Remaning: "+ str(z+1))
      print("Damage: " + str(strength))
      print("Defense: " + str(defense))
      print("-------------------------------------- ")
      print("""                                
                                .....            
                               O O  /            
                              /<   /             
               ___ __________/_^__/           
              /(- /(\_\________   \              
              \ ) \ )_      \o     \             
              /|\ /|\       |'     |             
                            |     _|             
                            /o   __\             
                           / '     |             
                          / /      |             
                         /_/\______|             
                        (   _(    <              
                         \    \    \             
                          \    \    |            
                           \____\____\           
                           ____\_\__\_\          
                         /`   /`     o\          
                         |___ |_______|""")
      skip=input("Enter to Continue")
      clear()
      print("You Attacked")
      print(" ")
      rd=strength + random.randint(1,strength)
      zombiehealth =zombiehealth - rd
      print("You Did "+str(rd)+ " Damage")
      print(" ")
      skip=input("Enter to Continue")
      night(days,strength, defense, health,z, zombiehealth, zombieattack,hunger, thirst)  
      
    else:
      print("THE ZOMBIES BROKE INTO YOUR BASE")
      rd=random.randint(25,50)
      skip=input("Enter to Continue")
      print("The Zombies hit you but you've escaped for another day")
      print("They did "+ str(rd)+ " damage to your health")
      health=health-rd
      skip=input("Enter to Continue")
      days=days+1
      hunger=hunger-random.randint(20,50)
      thirst=thirst-random.randint(30,60)
      day(health, defense, energy, strength, hunger, thirst, weak, medium, strong, days,z, zombiehealth, zombieattack)

      if zombiehealth>0:
        print(str(zombiehealth)+ " Total Zombie Health Remaning")
        print("""                                
                                .....            
                               O O  /            
                              /<   /             
               ___ __________/_^__/           
              /(- /(\_\________   \              
              \ ) \ )_      \o     \             
              /|\ /|\       |'     |             
                            |     _|             
                            /o   __\             
                           / '     |             
                          / /      |             
                         /_/\______|             
                        (   _(    <              
                         \    \    \             
                          \    \    |            
                           \____\____\           
                           ____\_\__\_\          
                         /`   /`     o\          
                         |___ |_______|""")
        skip=input("Enter to Continue")
        night(days,strength, defense, health,z, zombiehealth, zombieattack,hunger, thirst)
      else: 
        night(days,strength, defense, health,z, zombiehealth, zombieattack, hunger, thirst)  
#Varablies
health=(100)
defense=(25)
energy=(3)
strength=(2)
hunger=(100)
thirst=(100)
days=(1)
weak=(10)
medium=(5)
strong=(0)
zombiehealth=random.randint(3,5)
zombieattack=random.randint(1,3)+days
intro()
day(health,defense,energy,strength,hunger,thirst,weak,medium,strong,days,z, zombiehealth, zombieattack)
#Night and Fight cycle and more stuff lol
