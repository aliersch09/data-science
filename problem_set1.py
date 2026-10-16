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
    count = int(input("Give me a number: "))
    while(count>0):
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
    all_candies = candies + user_candies
    candyLength = len(all_candies)
    print("len: ", candyLength)
    while(candyLength>0):
        print(all_candies[candyLength-1])
        candyLength = candyLength-1
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
    fruits["pear"] = 1.15
    print(fruits.get("peach"))
    totalCost = 0
    for fruit in fruits:
        if fruits[fruit] >= 1.25:
            print(fruit) 
    totalCost = (3*fruits.get("apple"))+(2*fruits.get("banana"))+(1*fruits.get("coconut"))
    print(totalCost)

if __name__ == "__main__":
    main()