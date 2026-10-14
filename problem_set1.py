
def main():
    blue()
    blastoff()
    print(candy_shop())
    fruit_pricing()
def blue():
    red = 3
    purple = red*12
    print(purple)
def blastoff():
    count = input("Give me a number: ")
    while(count>=0):
        print(count)
        count = count-1
    print("blastoff!")
def candy_shop():
    candies = ["reeces peanutbutter cups", "snickers", "milkyway"]
    candies.append("kitkat")
    candies.insert(1, "m&m")
    candies.sort()
    candies.pop(candies.index("kitkat"))
    print(candies)
    user_candies = []
    print("List your 3 favorite candies")
    firstCandy = input("1: ")
    secondCandy = input("2: ")
    thirdCandy = input("3: ")
    user_candies.append(firstCandy)
    user_candies.append(secondCandy)
    user_candies.append(thirdCandy)
    all_candies = []
    all_candies.append(candies)
    all_candies.append(user_candies)
    print(len(all_candies))
    candyLength = len(all_candies)
    while(candyLength>0):
        print(all_candies[candyLength-1])
        candyLength = candyLength-1
    totalCost = candyLength*1.25
    return(totalCost)
def fruit_pricing():
    fruits = {
        "apple": .75,
        "banana": 1.25,
        "orange": .80,
        "peach": 2.25,
        "coconut": 2.80
    }
    fruits["pear"] = 1.15
    print(fruits.get("pear"))
    length = len(fruits)
    while(length>0):
        if(fruits.get(length-1)>=1.25):
            print(fruits[length-1])
    totalCost = (3*.75)+(2*1.25)+(1*2.80)
    print(totalCost)

if __name__ == "__main__":
    main()