Name:Cristian


Period:P3


Virtual / Hybrid / In-Person Class: Hybrid




Programming Experience:
 I have some experience but it's nothing major, I still have trouble remembering how to code.

9th Grade Year: In the space below, write 2-5 sentences describing your programming experience in the previous year, even if you went to another school.

  It was fine for the first 2/3 of the year since I could get help when I needed it, but then the pandemic hit and it was pretty rough after that. School didn't go into virtual till a month after, I forgot a lot about coding during that so the transition was difficult. 



10th Grade Year: In 2-5 sentences, describe each of the programming projects you’ve completed this year.  Think back to Block 1, Block 2/3, and your Passion Project (if that applies).
 When i got back into coding classes I wasnt all that sure about it. I hadn't really remembered it so i had to jog my memory in order to get the definitions to some of the words. I had trouble really getting the grove for the first bolck i had it again, especially with the passion project and such.


What is one part or element of programming that you would like to improve or grow in this year?

 Just remembering definitions and being able to use them correctly.



What is one part of programming or this class that you feel like challenges you more than others?

 Coding really gets my head jumbled up, it's complex for me.


What is your “goal” with computer programming or Computational Thinking?  This answer can be focused on your time at school, or it could describe how you want to experience college or your future career.

 Being abe to spend more time on it would really help a lot.
 
import random

myList = []

unique_List = []

def mainProgram():
#build our while loop
    while True:
    print("Hello, there! Let's work with lists")
    print("Please choose from the following options. Type the number of the choice")
    choice = input("""1. Add to a list,
2. Return a value in a list,
3. Random Search
4. to quit   """)
    if choice == "1":
        AddToList()
    elif choice == "2":
        indexValues()
    elif choice == "3":
        addABunch()
    elif choice == "4":
        randomSearch()
    elif choice == "5":
        LinearsSearch()
    elif choice == "6":
        sortlist(myList)
        else:
            break
        
def AddToList():
    print("adding to a list! Great choice!")
    newitem = input("Type an integer here!")
    myList.append(int(newitem))
    #we need to think about errors!

def sortList(myList):
    #"myList" is the ARGUMENT this function takes.
    for x in myList:
        if x not in unique_list:
            unique_list.append(x)
    unique_List.sort()
    showMe = input("Wanna see your new, sorted list? Y/N")
    if showMe.lower() == "y":
        print(unique_List)

def randomSearch():
    print("Oh I'm so random")
    print(myList[random.randit(0, len(myList)-1)])

def printlist():
    if len(unique_myList) == 0:
        print(myList)
    else:
        whichOne = input("Which list do you want to see? sorted or un-sorted? ")
        if whichOne.lower() =="sorted":
            print(unique_list)

def indexvalues():
    print("At what index positoin do you want to search?")
    indexPos = input("Type an index position here:   ")
    print(myList[int(indexPos)])

if __name__ == "__main__":
    mainProgram()

def factorial(x):
    if x == 1:
        return 1
    else:
        return(x*factorial(x-1))

 if__name__ == "__main__":
    num = input("what number would you like the fatorial of?
    print("The fatorial of ", num,"is", factorial(int(num))


