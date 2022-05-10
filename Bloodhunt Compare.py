import requests
from bs4 import BeautifulSoup

def getUserStats(user):
    url = "https://tracker.gg/bloodhunt/profile/" + str(user) + "/overview?playlist=BattleRoyale_Casual&season=1&mode=Trios"
    page = requests.get(url)
    doc = BeautifulSoup(page.content, 'html.parser')

    title = doc.title.text
    print(title)

    sNames = ["Win %","Wins","K/D Ratio","Damage/min","Kills","Deaths","Assists","Losses","Allies Revived","Diableries","Damage Done","Distance Traveled","Avg Time Alive","Kills/match","Damage/match","Bullet Accuracy"]
    container = doc.find(class_="segment-stats area-main-stats lifetime card bordered header-bordered responsive")
    values = container.find_all(class_="value")
    
    i = 0
    for value in values:
        print(sNames[i] + ": " + value.text)
        i += 1

    wPercentage = values[0].text
    wins = values[1].text
    kdRatio = values[2].text
    damagePerMinute = values[3].text
    kills = values[4].text
    deaths = values[5].text
    assists = values[6].text
    losses = values[7].text
    alliesRevived = values[8].text
    diableries = values[9].text
    damageDone = values[10].text
    distanceTraveled = values[11].text
    avgTimeAlive = values[12].text
    killPerMatch = values[13].text
    damagePerMatch = values[14].text
    bAccuracy = values[15].text

    return wPercentage, wins, kdRatio, damagePerMinute, kills, deaths, assists, losses, alliesRevived, diableries, damageDone, distanceTraveled, avgTimeAlive, killPerMatch, damagePerMatch, bAccuracy


def userInput():
    while True:
        try:
            firstUser = int(input("First User Input: "))
            if firstUser == "":
                print("Please Enter an Input")
            else:
                while True:
                    try:
                        secondUser = int(input("Second User Input: "))
                        if secondUser == "":
                            print("Please Enter an Input")
                        else:
                            return firstUser, secondUser
                    except ValueError:
                        print("Invalid Value Input")
        except ValueError:
            print("Invalid Value Input")

def compareUsers(firstUser, secondUser):
    print("Comparing Users...")

if __name__ == "__main__":
         users = userInput()
         firstUser = getUserStats(users[0])
         secondUser = getUserStats(users[1])
         compareUsers (firstUser, secondUser)