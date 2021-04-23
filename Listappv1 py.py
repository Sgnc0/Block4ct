"""
Program goals:
3. Pull the values stored at specific indexes
4. Convert input to INTs
5. Put all action into a while loop
6. Write a exit option
#these are our program goals, the quotes at the start and end our so the goals don't interfere with the code.

"""
#these are our program goals, the quotes at the start and end are so the goals don't interfere with the code.
import random
#this is more like an application, it is used to randomize and we are simply just adding to our code.
myList = []
#this will be our list, we can name it anything we want it to were just going to name it "myList" for now.
unique_list = []
#We are going to talk about how indentations work and how they are kind of the hardest part and easiest part of coding. Computers don't really use steps like we
#normally do they mainly use indentation where if we want to continue a piece code you are going to have to but it a space after the first piece of code, python makes
#this easier with letting us enter space and will automatically indent for us, if you want to start a new piece of code then you can start back to the start and continue
#to make more code, python also makes this harder with not every code works that way, for example when your not making steps and really only using quotes it dosen't
#really matter at that point. 
def mainProgram():
    #this will be where most of our code will be, you can think of mainProgram as running a part of our code. the def in front of mainProgram is short for define it will let us run the piece of code that we made.
    while True:
        #the while true will let this piece of code run forever 
        print("Hello , there! Let's work with lists!")
        #The print option will allows to show something when we are running a piece of code, for example if you put print("something, something") it will run it in our shell.
        print("PLease choose from the following options. Type the number of your choice")
        #this will print the quotes at the start of the shell.
        choice = input("""1. Add to a list,
2. Return a value at a list
3. Add a bunch of numbers!
4. Random Search
5. Linear search
6. sort list
7. print list
8. Recursive Binary Search
9. Iterative Binary Search
10. Big brain 
11. to quit   """)

        if choice == "1":
            addToList()
        elif choice == "2":
            indexValues()
        elif choice == "3":
            addABunch()
        elif choice == "4":
            randomSearch()
        elif choice == "5":
            linearSearch()
        elif choice == "6":
            sortList(myList)
        elif choice == "7":
            printLists()
        elif choice == "8":
            searchItem = input("What are you looking for?   ")
            recursiveBinarySearch(unique_list, 0, len(unique_list)-1, int(searchItem))
        elif choice == "9":
            searchItem = input("What are you looking for   ")
            iterativeBinarySearch(unique_list, 0, len(unique_list)-1, int(searchItem))
        elif choice == "10":
            searchItem = input("Return to monke?   ")
            iterativeBinarySearch(unique_list, 0, len(unique_list)-1, int(searchItem))
  
            
  
            
            #this will print the list we made, it's actually pretty simple, if you type 6 in the shell you will get the data in your list.
        else:
            #else is like the last piece of elif in our data, it will be the last piece of code before it stops the loop.
            break
        #this will break the loop from repeating every time.
        
def addToList():
    #this is the name of the code we will make, we typed this above we're our numbers are!, we are using def instead of elif, def is short for define, it will define
    #the addToList we just made.
    print("Adding to a list! Great Choice!")
    #this will print the quotes when addTOlist is chosen
    newItem = input("Type an integer here!  ")
    #this is similar to what we did above, it will name a data set, for example newItem will be('Type and integer here!")
    myList.append(int(newItem))
    #Append here is used to create, some of this code might seem complicated but it's more like steps we the code will do for us, for example mylist.append will
    #create a data set into(newItem) the int at the start will convert the integer into data set that will fit MyList. 
    #we need to think about errors!


def addabunch():#the name of our function
    print("we're going to add a bunch of numbers to your list")
    #this will print the quotes when addabunch is chosen
    numToAdd = input("How many new integers do you want to add   ")
    numRange = input("And how high would you like these numbers to go?  ")#the space at the end will help us incase we wanna add new code or just for more space when
    #it's being show in the shell
    for x in range (0, int(numToAdd)):
        #for x in range, it simply means python will try to find a value between the numbers you added, for example it shows us 0, then converts that data set
        #into a int inside numRange.
        myList.append(random.randint(0, int(numRange)))
        #instead of finding, this time it wil create something using append and also will also use random.randint to 
    print("Your list is complete")
    #this will print when the code is done running

def sortList(myList):
    #"myList"is the ARGUMENT this function take.
    for x in myList:
        if x not in unique_list:
            unique_list.append(x)
    unique_list.sort()
    showMe = input("Wanna se your new, sorted list? Y/N")
    if showMe.lower() =="y":
        print(unique_list)

def randomSearch():
    print("bruh, how you doing bruv, im a random search engine")
     #this will print the quotes when randomSearch is chosen
    print(myList[random.randint(0, len(myList)-1)])
    #the line of code is again similar to like steps, print myList will then do a random search, len is similar to int in where it will convert the data into another
    #thing, this time the len will turn it into a string then add the data set you want to add or change and the -1 is really only used because computers like using
    #01234 instead of the normal 1234 we use.

def linearSearch():#the name of our function
    print("Where going to go through this list one item at a time")
    #this will print the quotes when linearSearch is chosen
    SearchValue = input("What are you looking for?  ")
    #This will let us to be able to search for a certain value(it's in the name) 
    for x in range(len(myList)):
        #this will search for string in myList
        if myList (x) == int(SearchValue):
            #this will search a certain value in our MyList
            print("Your item is at index position {}".format (8))
            #this will tell us where the position is, we don't want it to search and not tell us anything so this is here.

def recursiveBinarySearch(unique_list, low, high, x):
    if high >= low:
        mid = (high + low) //2
        if unique_list[mid] == x:
            print("Your number is at index position()".format(mid))
            return mid
        elif unique_list[mid] > x:
            return recursiveBinarySearch(unique_list, low, mid-1, x)
        else:
            return recursiveBinarySearch(unique_list, mid+1, high, x)
    else:
        print("your number isn't here")


def iterativeBinarySearch(unique_list, x):
    low = 0
    high = len(unique_list)-1
    mid = 0

    while low<- high:
        mid = (high + low) // 2
        if unique_list[mid] < x:
            low = mid + 1
        elif unique_list[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1
    
    
    
def indexValues():#the name of our function
    print("At what index position do you want to search?")
    #this will print when indexValues is turned on.
    indexPos = input("Type an index position here!   ")
    #this will give us a input when indexPos is entered.
    print(myList[int(indexPos)])
    #this is pretty simple, it's kind of like steps, for example it will give a i am going to print myList and convert that piece of dat into a int inside the index
    #position of your choosing. 
    myList[random.randint(0, len(myList))]
    #we do a similar thing here but we just add a random.randint and try to search for a value inside the mylist we created.

def printLists():
    if len(unique_list) == 0:
        print(myList)
    else:
        whichOne = input("which list do you want to see? sorted or unsorted?  ")
        if whichOne.lower() == "sorted":
            print(unique_list)
    
            
          
      
  



if __name__ == "__main__":
    #this is how a program will read a python file and to be able to run it.
    mainProgram()
    #this marks the end of our "mainProgram" program

