import random


def rollDice():
    minValue = 1
    maxValue = 6
    roll = random.randint(minValue, maxValue)

    return roll

def startGame():

    while True:
        playersNumber = input("Enter the number of players (2 - 4): ")
        if playersNumber.isdigit():
            playersNumber = int(playersNumber)
            if playersNumber >=2 and playersNumber <= 4:
                break
            else:
                print("Maximum players allowed is 4 and you must at least have 2 players to begin.")
        else:
            print("Invalid characters, try again....")

    maxScore = 20
    playersScores = [0 for _ in range(playersNumber)]

    while max(playersScores) < maxScore:
        for i in range(playersNumber):
            
            print("\n************************************")
            print("Player's Turn :", i + 1)
            print("************************************")
            totalScore = 0

            while True:
                isRolling = input("\nDo you like to roll (y)? ")
                if isRolling.lower() != "y":
                    break

                diceValue = rollDice()
                if diceValue == 1:
                    print("You rolled 1. Stoped rolling.....")
                    totalScore = 0
                    break
                else:
                    totalScore += diceValue
                    print("Rolled:", diceValue)
                    
                
                print("\nYour score is:", totalScore)
                

            playersScores[i] += totalScore

    maxScore = max(playersScores)
    winnerIs = playersScores.index(maxScore)
    print("************************************")
    print("************************************")
    print("Congrats, the Winner is:",winnerIs+1)
    print("Winning score is:",maxScore)
    
startGame()