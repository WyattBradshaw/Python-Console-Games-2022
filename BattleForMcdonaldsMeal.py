import time
import random
import replit
###Get out of my code >:( its not meant to be pretty! -SS
def clear():
 time.sleep(1)
 replit.clear()

def intro():
  print("It's a nice day")
  time.sleep(2)
  print("You walk into a McDonalds")
  time.sleep (2)
  print("You go to order a Burger")
  clear()

def fChoice():
  print("What do you order?")
  time.sleep(1)
  print(" ")
  print("1: BigMac")
  print(" ")
  print("2: McDouble")
  print(" ")
  print("3: Fish Fellet")
  print(" ")
  time.sleep(1)
  fc = input("What Number Do You Order? ")
  if fc=="1":
    order ="BigMac"
    print(" ")
    print("You ordered a BigMac")
  elif fc=="2":
    order ="McDouble"
    print(" ")
    print("You ordered a McDouble")
  elif fc=="3":
    order ="Fish Fellet"
    print(" ")
    print("You ordered a Fish Fellet")
  else:
    print(" ")
    print("You ordered nothing!")
    clear()
    fChoice()

def orderTime():
  clear()
  print("You Wait 3 Minutes")
  time.sleep(1.5)
  print("You Check Your Order")
  time.sleep(1.5)
  print("You: Wow They Got Your Order Right")
  print(" ")
  time.sleep(1)
  print("SLAM!")
  time.sleep(1)
  print("You look behind you thinking someone fell!")
  time.sleep(1)
  print("You hear a deeper voice than your own start speaking")
  print(" ")
  print("Worker: Sir I'm very sorry but we got your order right. We will need to be taking this back now")
  time.sleep(3)
  print(" ")
  print("You: Im not Giving you it back")
  print(" ")
  print("Worker: Then I Guess I'LL TAKE THE ORDER FROM YOU!")
  time.sleep(10)

def roastPicker():
  rIndex = random.randint(1,11)
  if rIndex==1:
    return("You look like the moon emoji")
  if rIndex==2:
    return("You smell like you farted, Harded, AB honor roll. All F's you are stupid")
  if rIndex==3:
    return("I’m not shy. I just don’t like you.")
  if rIndex==4:
    return("I’m jealous of people who don’t know you.")
  if rIndex==5:
    return("That's why you girlfriend look like my mom")
  if rIndex==6:
    return("My phone battery lasts longer than your relationships.")
  if rIndex==7:
    return("It’s scary to think people like you are allowed to vote.")
  if rIndex==8:
    return("Where’s your off button?")
  if rIndex==9:
    return("You sound reasonable… Time to up my medication.")
  if rIndex==10:
    return("I’m sorry that my brutal honesty inconvenienced your ego.")
  if rIndex==11:
    return("If I throw a stick, will you leave?")
#Stats
pHealth=100
pDamage=3
pDefense=2
eHealth=100
eNum=1
br=10 
def pTurn():
  global pHealth, pDamage, pDefense, eHealth, eDamage, eNum, br, bh, adr,nd,eKill
  #Ronald Fight
  if eNum==10:
    clear()
    print("Ronald McDonald Aproaches")
    eHealth= 10000
    eDamage= 10000
    eDamage=(random.randint(3,eDamage))//pDefense
    pHealth=pHealth-eDamage
    print("He Did " + str(eDamage) + " Damage")
    if pHealth<=0:
      print("Ronald Killed Your Punk Ass")
  #BK Fight!

  elif eNum==20:
    clear()
    print("BURGER KING! Aproaches")
    print(eHealth)
    eHealth= 200000
    eDamage= 200000
    eDamage=(random.randint(3,eDamage)*eNum*5)//pDefense
    pHealth=pHealth-eDamage
    print("He Did " + str(eDamage) + " Damage")
    time.sleep(10)
  elif eNum==30:
    clear()
    print("WENDY!!! Aproaches")
    eHealth= 300000
    eDamage= 300000
    eDamage=(random.randint(3,eDamage)*eNum*5)//pDefense
    pHealth=pHealth-eDamage
    print("She Did " + str(eDamage) + " Damage")
    time.sleep(10)
  elif eNum==40:
    clear()
    print("Arby's!!!! Aproaches")
    eHealth= 400000
    eDamage= 400000
    eDamage=(random.randint(3,eDamage)*eNum*5)//pDefense
    pHealth=pHealth-eDamage
    print("IT Did " + str(eDamage) + " Damage")
    time.sleep(10)
  elif eNum==50:
    clear()
    print("FIVEGUYS!!!!! Aproaches")
    eHealth= 500000
    eDamage= 500000
    eDamage=(random.randint(3,eDamage)*eNum*5)//pDefense
    pHealth=pHealth-eDamage
    print("They Did " + str(eDamage) + " Damage")
    time.sleep(10)
  elif eNum==100:
    clear()
    print("JARED FROM SUBWAY Aproaches And Shows you his footlong :)))")
    eHealth= 1000000
    eDamage= 1000000
    eDamage=(random.randint(3,eDamage)*eNum*5)//pDefense
    pHealth=pHealth-eDamage
    print("They Did " + str(eDamage) + " Damage")
    time.sleep(10)
  #Kill Ronald
  elif eNum==11:
    clear()
    print("CONGRATS! YOU WIPED OUT LIKE A DOZEN OF MINIMUM WAGE EMPLOYEES!")
    print(" ")
    print("How Far Can You Go?")
    time.sleep(10)
    clear()
    print("The McDonalds Employee Slaps You Across The Face!")
    eKill=eNum-1
    eDamage=(random.randint(3,13)*eNum*5)//pDefense
    pHealth=pHealth-eDamage
    print("He Did " + str(eDamage) + " Damage")
    time.sleep(1)
  #Default Enemy ""AI""
  else:
    clear()
    crit=random.randint(1,50)
    if crit==26:
      print("The McDonalds Employee Slaps You Across The Face!")
      eKill=eNum-1
      print("HOLY SHIT A CRIT!")
      eDamage=(random.randint(3,13)*eNum*5)
      pHealth=pHealth-eDamage
      print("He Did " + str(eDamage) + " Damage")
      time.sleep(1)
    else:
      print("The McDonalds Employee Slaps You Across The Face!")
      eKill=eNum-1
      eDamage=(random.randint(3,13)*eNum*5)//pDefense
      pHealth=pHealth-eDamage
      print("He Did " + str(eDamage) + " Damage")
      time.sleep(1)
  #Menu And Player
  if pHealth>0:
    clear()
    print("Your Health: " + str(pHealth))
    print("Employee's Health: " + str(eHealth))
    print("Employee's Taken Out: "+ str(eKill))
    print("Burgers Remaning: " + str(br))
    print("Damage: " + str(pDamage))
    print("Defense: " + str(pDefense))
    print("-------------------------------------- ")
    print("What do you want to do? ")
    print(" ")
    print("1: Attack")
    print(" ")
    print("2: Defend")
    print(" ")
    print("3: Roast")
    print(" ")
    print("4: Eat Burger")
    print("-------------------------------------- ")
    adr= input("What Do You Want To Do? ")
  if adr == "1":
    clear()
    print("You Chose To Attack")
    print(" ")
    rd=pDamage + random.randint(1,pDamage)
    eDef=3*eNum
    eHealth =eHealth - rd/eDef
    print("You Did "+str(rd)+ " Damage" + " But his Defense is "+ str(eDef))
    print(" ")
    if eHealth>0:
      print(str(eHealth)+ " Health Remaning")
      time.sleep(1)
      pTurn()
    else:
      clear()
      eNum=eNum+1
      bn= random.randint(1,3)
      br= br+ bn
      eHealth=100*eNum
      print("Oh God You Killed The Employee With Only Slaps!")
      print("A New Challenger Aproaches!")
      print("The Employee Dropped " + str(bn) + " Burgers")
      pTurn()
  elif adr=="2":
    clear()
    nd=pDefense + random.randint(1, pDefense)
    pDefense=nd
    print("You Chose To Defend")
    print(" ")
    print("Your Defense Increased By " + str(nd))
    time.sleep(1)
    pTurn()
  elif adr=="3":
    #Attack Up
    clear()
    print("You Chose To Roast")
    pDamage=pDamage+ random.randint(1,pDamage*2)
    roast= roastPicker()
    print(roast)
    print(" ")
    print("You Hurt His Ego So Much That You Now Do " + str(pDamage)+ " Damage")
    time.sleep(3)
    pTurn()
  elif adr =="4":
    if br>0:
      clear()
      bt= random.randint(1,3)
      if bt==1:
        global bh
        br=br-1
        bh=(100+br//2*eNum)//2 + random.randint(1,20)
        pHealth=pHealth+bh
        print("You Eat The Burger And Gain "+ str(bh) + " Health")
        time.sleep(3)
      if bt==2:
        br=br-1
        pDamage = pDamage*3
        print("You Eat The Burger And Doubled Your "+ str(br) + " Attack!")
        time.sleep(3)
      if bt==3:
        br=br-1
        pDefense=pDefense*3
        print("You Eat The Burger And Doubled Your "+ str(br) + " Defense!")
        time.sleep(3)
      pTurn()
    else:
      clear()
      print("No Burgers Remaning!")
      time.sleep(2)
      pTurn()
  else:
    print("You stood there like an idiot and did nothing")
    time.sleep(2)
    pTurn()
  if pHealth <= 0:
    clear()
    print("You Got Knocked Out Cold By The McDonald's Minimum Wage Employee!")
    time.sleep("2")
intro()
fChoice()
orderTime()
pTurn()
