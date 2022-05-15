from datetime import datetime

def wPercentageCompare(firstUser, secondUser, firstUserTitle, secondUserTitle):
    if float(firstUser[0][:-1]) > float(secondUser[0][:-1]):
        wPercentageDiff = float(firstUser[0][:-1]) - float(secondUser[0][:-1])
        result = (firstUserTitle + " Has the highest Win %: " + firstUser[0] + ", " + secondUserTitle + " Win % is: " + secondUser[0] + ". Win % Difference is: " + str(round(wPercentageDiff,2))+ "%")
    elif float(firstUser[0][:-1]) < float(secondUser[0][:-1]):
        wPercentageDiff = float(secondUser[0][:-1]) - float(firstUser[0][:-1])
        result = (secondUserTitle + " Has the highest Win %: " + secondUser[0] + ", " + firstUserTitle + " Win % is: " + firstUser[0] + ". Win % Difference is: " + str(round(wPercentageDiff,2))+ "%")
    elif float(firstUser[0][:-1]) == float(secondUser[0][:-1]):
        result = (firstUserTitle + " and " + secondUserTitle + " Have the same Win %: " + firstUser[0])
    else:
        result = ("Error")
    return result

def winsCompare(firstUser, secondUser, firstUserTitle, secondUserTitle):
    if int(firstUser[1]) > int(secondUser[1]):
        winsDiff = int(firstUser[1]) - int(secondUser[1])
        result = (firstUserTitle + " Has the most Wins: " + firstUser[1] + ", " + secondUserTitle + " Wins is: " + secondUser[1] + ". Wins Difference is: " + str(winsDiff))
    elif int(firstUser[1]) < int(secondUser[1]):
        winsDiff = int(secondUser[1]) - int(firstUser[1])
        result = (secondUserTitle + " Has the most Wins: " + secondUser[1] + ", " + firstUserTitle + " Wins is: " + firstUser[1] + ". Wins Difference is: " + str(winsDiff))
    elif int(firstUser[1]) == int(secondUser[1]):
        result = (firstUserTitle + " and " + secondUserTitle + " Have the same Wins: " + firstUser[1])
    else:
        result = ("Error")
    return result

def kdRatioCompare(firstUser, secondUser, firstUserTitle, secondUserTitle):
    if float(firstUser[2]) > float(secondUser[2]):
        kdRatioDiff = float(firstUser[2]) - float(secondUser[2])
        result = (firstUserTitle + " Has the highest K/D Ratio: " + firstUser[2] + ", " + secondUserTitle + " K/D Ratio is: " + secondUser[2] +  ". K/D Ratio Difference is: " + str(round(kdRatioDiff,2)))
    elif float(firstUser[2]) < float(secondUser[2]):
        kdRatioDiff = float(secondUser[2]) - float(firstUser[2])
        result = (secondUserTitle + " Has the highest K/D Ratio: " + secondUser[2] + ", " + firstUserTitle + " K/D Ratio is: " + firstUser[2] +  ". K/D Ratio Difference is: " + str(round(kdRatioDiff,2)))
    elif float(firstUser[2]) == float(secondUser[2]):
        result = (firstUserTitle + " and " + secondUserTitle + " Have the same K/D Ratio: " + firstUser[2])
    else:
        result = ("Error")
    return result

def damageperminCompare(firstUser, secondUser, firstUserTitle, secondUserTitle):
    if float(firstUser[3]) > float(secondUser[3]):
        damageperminDiff = float(firstUser[3]) - float(secondUser[3])
        result = (firstUserTitle + " Damage per Minute is: " + firstUser[3] + ", " + secondUserTitle + " Damage per Minute is: " + secondUser[3] + ". Damage per Minute Difference is: " + str(round(damageperminDiff,3)))
    elif float(firstUser[3]) < float(secondUser[3]):
        damageperminDiff = float(secondUser[3]) - float(firstUser[3])
        result = (secondUserTitle + " Damage per Minute is: " + secondUser[3] + ", " + firstUserTitle + " Damage per Minute is: " + firstUser[3] + ". Damage per Minute Difference is: " + str(round(damageperminDiff,3)))
    elif float(firstUser[3]) == float(secondUser[3]):
        result = (firstUserTitle + " and " + secondUserTitle + " Have the same Damage per Minute: " + firstUser[3])
    else:
        result = ("Error")
    return result

def killsCompare(firstUser, secondUser, firstUserTitle, secondUserTitle):
    if int(firstUser[4]) > int(secondUser[4]):
        killsDiff = int(firstUser[4]) - int(secondUser[4])
        result = (firstUserTitle + " Has the most Kills: " + firstUser[4] + ", " + secondUserTitle + " Kills is: " + secondUser[4] + ". Kills Difference is: " + str(killsDiff))
    elif int(firstUser[4]) < int(secondUser[4]):
        killsDiff = int(secondUser[4]) - int(firstUser[4])
        result = (secondUserTitle + " Has the most Kills: " + secondUser[4] + ", " + firstUserTitle + " Kills is: " + firstUser[4] + ". Kills Difference is: " + str(killsDiff))
    elif int(firstUser[4]) == int(secondUser[4]):
        result = (firstUserTitle + " and " + secondUserTitle + " Have the same Kills: " + firstUser[4])
    else:
        result = ("Error")
    return result

def deathsCompare(firstUser, secondUser, firstUserTitle, secondUserTitle):
    if int(firstUser[5]) > int(secondUser[5]):
        deathsDiff = int(firstUser[5]) - int(secondUser[5])
        result = (firstUserTitle + " Has the most Deaths: " + firstUser[5] + ", " + secondUserTitle + " Deaths is: " + secondUser[5] + ". Deaths Difference is: " + str(deathsDiff))
    elif int(firstUser[5]) < int(secondUser[5]):
        deathsDiff = int(secondUser[5]) - int(firstUser[5])
        result = (secondUserTitle + " Has the most Deaths: " + secondUser[5] + ", " + firstUserTitle + " Deaths is: " + firstUser[5] + ". Deaths Difference is: " + str(deathsDiff))
    elif int(firstUser[5]) == int(secondUser[5]):
        result = (firstUserTitle + " and " + secondUserTitle + " Have the same Deaths: " + firstUser[5])
    else:
        result = ("Error")
    return result

def assistsCompare(firstUser, secondUser, firstUserTitle, secondUserTitle):
    if int(firstUser[6]) > int(secondUser[6]):
        assistsDiff = int(firstUser[6]) - int(secondUser[6])
        result = (firstUserTitle + " Has the most Assists: " + firstUser[6] + ", " + secondUserTitle + " Assists is: " + secondUser[6] + ". Assists Difference is: " + str(assistsDiff))
    elif int(firstUser[6]) < int(secondUser[6]):
        assistsDiff = int(secondUser[6]) - int(firstUser[6])
        result = (secondUserTitle + " Has the most Assists: " + secondUser[6] + ", " + firstUserTitle + " Assists is: " + firstUser[6] + ". Assists Difference is: " + str(assistsDiff))
    elif int(firstUser[6]) == int(secondUser[6]):
        result = (firstUserTitle + " and " + secondUserTitle + " Have the same Assists: " + firstUser[6])
    else:
        result = ("Error")
    return result

def lossesCompare(firstUser, secondUser, firstUserTitle, secondUserTitle):
    if int(firstUser[7]) > int(secondUser[7]):
        lossesDiff = int(firstUser[7]) - int(secondUser[7])
        result = (firstUserTitle + " Has the most Losses: " + firstUser[7] + ", " + secondUserTitle + " Losses is: " + secondUser[7] + ". Losses Difference is: " + str(lossesDiff))
    elif int(firstUser[7]) < int(secondUser[7]):
        lossesDiff = int(secondUser[7]) - int(firstUser[7])
        result = (secondUserTitle + " Has the most Losses: " + secondUser[7] + ", " + firstUserTitle + " Losses is: " + firstUser[7] + ". Losses Difference is: " + str(lossesDiff))
    elif int(firstUser[7]) == int(secondUser[7]):
        result = (firstUserTitle + " and " + secondUserTitle + " Have the same Losses: " + firstUser[7])
    else:
        result = ("Error")
    return result

def alliesRevivedCompare(firstUser, secondUser, firstUserTitle, secondUserTitle):
    if int(firstUser[8]) > int(secondUser[8]):
        alliesRevivedDiff = int(firstUser[8]) - int(secondUser[8])
        result = (firstUserTitle + " Has the most Allies Revived: " + firstUser[8] + ", " + secondUserTitle + " Allies Revived is: " + secondUser[8] + ". Allies Revived Difference is: " + str(alliesRevivedDiff))
    elif int(firstUser[8]) < int(secondUser[8]):
        alliesRevivedDiff = int(secondUser[8]) - int(firstUser[8])
        result = (secondUserTitle + " Has the most Allies Revived: " + secondUser[8] + ", " + firstUserTitle + " Allies Revived is: " + firstUser[8] + ". Allies Revived Difference is: " + str(alliesRevivedDiff))
    elif int(firstUser[8]) == int(secondUser[8]):
        result = (firstUserTitle + " and " + secondUserTitle + " Have the same Allies Revived: " + firstUser[8])
    else:
        result = ("Error")
    return result

def diableriesCompare(firstUser, secondUser, firstUserTitle, secondUserTitle):
    if int(firstUser[9]) > int(secondUser[9]):
        diableriesDiff = int(firstUser[9]) - int(secondUser[9])
        result = (firstUserTitle + " Has the most Diableries: " + firstUser[9] + ", " + secondUserTitle + " Diableries is: " + secondUser[9] + ". Diableries Difference is: " + str(diableriesDiff))
    elif int(firstUser[9]) < int(secondUser[9]):
        diableriesDiff = int(secondUser[9]) - int(firstUser[9])
        result = (secondUserTitle + " Has the most Diableries: " + secondUser[9] + ", " + firstUserTitle + " Diableries is: " + firstUser[9] + ". Diableries Difference is: " + str(diableriesDiff))
    elif int(firstUser[9]) == int(secondUser[9]):
        result = (firstUserTitle + " and " + secondUserTitle + " Have the same Diableries: " + firstUser[9])
    else:
        result = ("Error")
    return result

def damageDoneCompare(firstUser, secondUser, firstUserTitle, secondUserTitle):
    if int(firstUser[10].replace(",", "")) > int(secondUser[10].replace(",", "")):
        damageDoneDiff = int(firstUser[10].replace(",", "")) - int(secondUser[10].replace(",", ""))
        result = (firstUserTitle + " Has the most Damage Done: " + firstUser[10] + ". " + secondUserTitle + " Damage Done is: " + secondUser[10] + ". Damage Done Difference is: " + str(damageDoneDiff))
    elif int(firstUser[10].replace(",", "")) < int(secondUser[10].replace(",", "")):
        damageDoneDiff = int(secondUser[10].replace(",", "")) - int(firstUser[10].replace(",", ""))
        result = (secondUserTitle + " Has the most Damage Done: " + secondUser[10] + ". " + firstUserTitle + " Damage Done is: " + firstUser[10] + ". Damage Done Difference is: " + str(damageDoneDiff))
    elif int(firstUser[10].replace(",", "")) == int(secondUser[10].replace(",", "")):
        result = (firstUserTitle + " and " + secondUserTitle + " Have the same Damage Done: " + firstUser[10])
    else:
        result = ("Error")
    return result

def distanceTraveledCompare(firstUser, secondUser, firstUserTitle, secondUserTitle):
    if int(firstUser[11][:-2]) > int(secondUser[11][:-2]):
        distanceTraveledDiff = int(firstUser[11][:-2]) - int(secondUser[11][:-2])
        result = (firstUserTitle + " Has the most Distance Traveled: " + firstUser[11] + ". " + secondUserTitle + " Distance Traveled is: " + secondUser[11] + ". Distance Traveled Difference is: " + str(distanceTraveledDiff))
    elif int(firstUser[11][:-2]) < int(secondUser[11][:-2]):
        distanceTraveledDiff = int(secondUser[11][:-2]) - int(firstUser[11][:-2])
        result = (secondUserTitle + " Has the most Distance Traveled: " + secondUser[11] + ". " + firstUserTitle + " Distance Traveled is: " + firstUser[11] + ". Distance Traveled Difference is: " + str(distanceTraveledDiff))
    elif int(firstUser[11][:-2]) == int(secondUser[11][:-2]):
        result = (firstUserTitle + " and " + secondUserTitle + " Have the same Distance Traveled: " + firstUser[11])
    else:
        result = ("Error")
    return result

def averageTimeAliveCompare(firstUser, secondUser, firstUserTitle, secondUserTitle):
    firstUserDateTime = datetime.strptime(firstUser[12][:-1].replace("m ",":"), "%M:%S")
    secondUserDateTime = datetime.strptime(secondUser[12][:-1].replace("m ",":"), "%M:%S")
    timeAliveFU = firstUserDateTime.minute * 60 + firstUserDateTime.second
    timeAliveSU = secondUserDateTime.minute * 60 + secondUserDateTime.second
    if int(timeAliveFU) > int(timeAliveSU):
        timeAliveDiff = int(timeAliveFU) - int(timeAliveSU)
        result = (firstUserTitle + " Has the most Time Alive: " + firstUser[12] + ". " + secondUserTitle + " Time Alive is: " + secondUser[12] + ". Time Alive Difference is: " + str(timeAliveDiff) + " seconds")
    elif int(timeAliveFU) < int(timeAliveSU):
        timeAliveDiff = int(timeAliveSU) - int(timeAliveFU)
        result = (secondUserTitle + " Has the most Time Alive: " + secondUser[12] + ". " + firstUserTitle + " Time Alive is: " + firstUser[12] + ". Time Alive Difference is: " + str(timeAliveDiff) + " seconds")
    elif int(timeAliveFU) == int(timeAliveSU):
        result = (firstUserTitle + " and " + secondUserTitle + " Have the same Time Alive: " + firstUser[12])
    else:
        result = ("Error")
    return result

def killPerMatchCompare(firstUser, secondUser, firstUserTitle, secondUserTitle):
    if float(firstUser[13]) > float(secondUser[13]):
        killPerMatchDiff = float(firstUser[13]) - float(secondUser[13])
        result = (firstUserTitle + " Has the most Kills per Match: " + firstUser[13] + ", " + secondUserTitle + " Kills per Match is: " + secondUser[13] + ". Kills per Match Difference is: " + str(round(killPerMatchDiff,2)))
    elif float(firstUser[13]) < float(secondUser[13]):
        killPerMatchDiff = float(secondUser[13]) - float(firstUser[13])
        result = (secondUserTitle + " Has the most Kills per Match: " + secondUser[13] + ", " + firstUserTitle + " Kills per Match is: " + firstUser[13] + ". Kills per Match Difference is: " + str(round(killPerMatchDiff,2)))
    elif float(firstUser[13]) == float(secondUser[13]):
        result = (firstUserTitle + " and " + secondUserTitle + " Have the same Kills per Match: " + firstUser[13])
    else:
        result = ("Error")
    return result

def damagePerMatchCompare(firstUser, secondUser, firstUserTitle, secondUserTitle):
    if int(firstUser[14].replace(",", "")) > int(secondUser[14].replace(",", "")):
        damagePerMatchDiff = int(firstUser[14].replace(",", "")) - int(secondUser[14].replace(",", ""))
        result = (firstUserTitle + " Has the most Damage per Match: " + firstUser[14] + ". " + secondUserTitle + " Damage per Match is: " + secondUser[14] + ". Damage per Match Difference is: " + str(damagePerMatchDiff))
    elif int(firstUser[14].replace(",", "")) < int(secondUser[14].replace(",", "")):
        damagePerMatchDiff = int(secondUser[14].replace(",", "")) - int(firstUser[14].replace(",", ""))
        result = (secondUserTitle + " Has the most Damage per Match: " + secondUser[14] + ". " + firstUserTitle + " Damage per Match is: " + firstUser[14] + ". Damage per Match Difference is: " + str(damagePerMatchDiff))
    elif int(firstUser[14].replace(",", "")) == int(secondUser[14].replace(",", "")):
        result = (firstUserTitle + " and " + secondUserTitle + " Have the same Damage per Match: " + firstUser[14])
    else:
        result = ("Error")
    return result

def bulletAccuracyCompare(firstUser, secondUser, firstUserTitle, secondUserTitle):
    if float(firstUser[15][:-1]) > float(secondUser[15][:-1]):
        bulletAccuracyDiff = float(firstUser[15][:-1]) - float(secondUser[15][:-1])
        result = (firstUserTitle + " Has the most Bullet Accuracy: " + firstUser[15] + ". " + secondUserTitle + " Bullet Accuracy is: " + secondUser[15] + ". Bullet Accuracy Difference is: " + str(round(bulletAccuracyDiff,2)) + "%")
    elif float(firstUser[15][:-1]) < float(secondUser[15][:-1]):
        bulletAccuracyDiff = float(secondUser[15][:-1]) - float(firstUser[15][:-1])
        result = (secondUserTitle + " Has the most Bullet Accuracy: " + secondUser[15] + ". " + firstUserTitle + " Bullet Accuracy is: " + firstUser[15] + ". Bullet Accuracy Difference is: " + str(round(bulletAccuracyDiff,2)) + "%")
    elif float(firstUser[15][:-1]) == float(secondUser[15][:-1]):
        result = (firstUserTitle + " and " + secondUserTitle + " Have the same Bullet Accuracy: " + firstUser[15])
    else:
        result = ("Error")
    return result
