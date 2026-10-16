def main():
    blue()
    blastoff()
    print(candy_shop())
    fruit_pricing()
def blue():
    red = 3
    purple = red*12
    #should print 36, since that is the value of purple
    print(purple)
def blastoff():
    #stores user's input as the number to countdown from
    count = int(input("Give me a number: "))
    #prints out countdown and blastoff
    while(count>0):
        print(count)
        count = count-1
    print("blastoff!")
def candy_shop():
    candies = ["reeces peanutbutter cups", "snickers", "milkyway"]
    #add kitkat, insert m&m at index 1 and sort
    candies.append("kitkat")
    candies.insert(1, "m&m")
    candies.sort()
    candies.pop(candies.index("kitkat"))
    #print the candies list after changing it
    print(candies)
    #create user candy list, and add user input to the list
    user_candies = []
    print("List your 3 favorite candies")
    firstCandy = input("1: ")
    secondCandy = input("2: ")
    thirdCandy = input("3: ")
    user_candies.append(firstCandy)
    user_candies.append(secondCandy)
    user_candies.append(thirdCandy)
    #merge both lists in new list called all candies
    all_candies = candies + user_candies
    #create variable for length of all candies and print
    candyLength = len(all_candies)
    print("len: ", candyLength)
    #print all candies list
    while(candyLength>0):
        print(all_candies[candyLength-1])
        candyLength = candyLength-1
    #create total cost variable and return it
    totalCost = len(all_candies)*1.25
    return(totalCost)
def fruit_pricing():
    fruits = {
        "apple": .75,
        "banana": 1.25,
        "orange": .80,
        "peach": 2.25,
        "coconut": 2.80
    }
    #add pear key and value
    fruits["pear"] = 1.15
    #print peach's value
    print("peach cost: $",fruits.get("peach"))
    #print fruits with prices above $1.25
    for fruit in fruits:
        if fruits[fruit] >= 1.25:
            print(fruit)
    #make total cost variable and print 
    totalCost = (3*fruits.get("apple"))+(2*fruits.get("banana"))+(1*fruits.get("coconut"))
    print("total cost: $",totalCost)

if __name__ == "__main__":
    main()