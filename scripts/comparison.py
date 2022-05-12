def wPercentageCompare(firstUser, secondUser, firstUserTitle, secondUserTitle):
    if float(firstUser[0][:-1]) > float(secondUser[0][:-1]):
        wPercentageDiff = float(firstUser[0][:-1]) - float(secondUser[0][:-1])
        print(firstUserTitle + " Win % is: " + firstUser[0] + ", " + secondUserTitle + " Win % is: " + secondUser[0] + ". Win % Difference is: " + str(round(wPercentageDiff,2))+ "%")
        print(firstUserTitle + " Has the highest Win %")
    elif float(firstUser[0][:-1]) < float(secondUser[0][:-1]):
        wPercentageDiff = float(secondUser[0][:-1]) - float(firstUser[0][:-1])
        print(secondUserTitle + " Win % is: " + secondUser[0] + ", " + firstUserTitle + " Win % is: " + firstUser[0] + ". Win % Difference is: " + str(round(wPercentageDiff,2))+ "%")
        print(secondUserTitle + " Has the highest Win %")
    elif float(firstUser[0][:-1]) == float(secondUser[0][:-1]):
        wPercentageDiff = float(firstUser[0][:-1]) - float(secondUser[0][:-1])
        print(firstUserTitle + " Win % is: " + firstUser[0] + ", " + secondUserTitle + " Win % is: " + secondUser[0] + ". Win % Difference is: " + str(round(wPercentageDiff,2)) + "%")
        print(firstUserTitle + " and " + secondUserTitle + " Have the same Win %")
    else:
        print("Error")

def winsCompare(firstUser, secondUser, firstUserTitle, secondUserTitle):
    if int(firstUser[1]) > int(secondUser[1]):
        winsDiff = int(firstUser[1]) - int(secondUser[1])
        print(firstUserTitle + " Wins is: " + firstUser[1] + ", " + secondUserTitle + " Wins is: " + secondUser[1] + ". Wins Difference is: " + str(winsDiff))
        print(firstUserTitle + " Has the most Wins")
    elif int(firstUser[1]) < int(secondUser[1]):
        winsDiff = int(secondUser[1]) - int(firstUser[1])
        print(secondUserTitle + " Wins is: " + secondUser[1] + ", " + firstUserTitle + " Wins is: " + firstUser[1] + ". Wins Difference is: " + str(winsDiff))
        print(secondUserTitle + " Has the most Wins")
    elif int(firstUser[1]) == int(secondUser[1]):
        winsDiff = int(firstUser[1]) - int(secondUser[1])
        print(firstUserTitle + " Wins is: " + firstUser[1] + ", " + secondUserTitle + " Wins is: " + secondUser[1] + ". Wins Difference is: " + str(winsDiff))
        print(firstUserTitle + " and " + secondUserTitle + " Have the same Wins")
    else:
        print("Error")

def kdRatioCompare(firstUser, secondUser, firstUserTitle, secondUserTitle):
    if float(firstUser[2]) > float(secondUser[2]):
        kdRatioDiff = float(firstUser[2]) - float(secondUser[2])
        print(firstUserTitle + " K/D Ratio is: " + firstUser[2] + ", " + secondUserTitle + " K/D Ratio is: " + secondUser[2] + ". K/D Ratio Difference is: " + str(round(kdRatioDiff,2)))
        print(firstUserTitle + " Has the highest K/D Ratio")
    elif float(firstUser[2]) < float(secondUser[2]):
        kdRatioDiff = float(secondUser[2]) - float(firstUser[2])
        print(secondUserTitle + " K/D Ratio is: " + secondUser[2] + ", " + firstUserTitle + " K/D Ratio is: " + firstUser[2] + ". K/D Ratio Difference is: " + str(round(kdRatioDiff,2)))
        print(secondUserTitle + " Has the highest K/D Ratio")
    elif float(firstUser[2]) == float(secondUser[2]):
        kdRatioDiff = float(firstUser[2]) - float(secondUser[2])
        print(firstUserTitle + " K/D Ratio is: " + firstUser[2] + ", " + secondUserTitle + " K/D Ratio is: " + secondUser[2] + ". K/D Ratio Difference is: " + str(round(kdRatioDiff,2)))
        print(firstUserTitle + " and " + secondUserTitle + " Have the same K/D Ratio")
    else:
        print("Error")

def damageperminCompare(firstUser, secondUser, firstUserTitle, secondUserTitle):
    if float(firstUser[3]) > float(secondUser[3]):
        damageperminDiff = float(firstUser[3]) - float(secondUser[3])
        print(firstUserTitle + " Damage per Minute is: " + firstUser[3] + ", " + secondUserTitle + " Damage per Minute is: " + secondUser[3] + ". Damage per Minute Difference is: " + str(round(damageperminDiff,3)))
        print(firstUserTitle + " Has the highest Damage per Minute")
    elif float(firstUser[3]) < float(secondUser[3]):
        damageperminDiff = float(secondUser[3]) - float(firstUser[3])
        print(secondUserTitle + " Damage per Minute is: " + secondUser[3] + ", " + firstUserTitle + " Damage per Minute is: " + firstUser[3] + ". Damage per Minute Difference is: " + str(round(damageperminDiff,3)))
        print(secondUserTitle + " Has the highest Damage per Minute")
    elif float(firstUser[3]) == float(secondUser[3]):
        damageperminDiff = float(firstUser[3]) - float(secondUser[3])
        print(firstUserTitle + " Damage per Minute is: " + firstUser[3] + ", " + secondUserTitle + " Damage per Minute is: " + secondUser[3] + ". Damage per Minute Difference is: " + str(round(damageperminDiff,3)))
        print(firstUserTitle + " and " + secondUserTitle + " Have the same Damage per Minute")
    else:
        print("Error")