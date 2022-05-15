import requests
from bs4 import BeautifulSoup

def getUserStats(user):
    url = "https://tracker.gg/bloodhunt/profile/" + str(user) + "/overview?playlist=BattleRoyale_Casual&season=1&mode=Trios"
    page = requests.get(url)
    doc = BeautifulSoup(page.content, 'html.parser')

    title = doc.title.text.split()[0]
    try:
        container = doc.find(class_="segment-stats area-main-stats lifetime card bordered header-bordered responsive")
        values = container.find_all(class_="value")
        
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
    except AttributeError:
        return None

    return wPercentage, wins, kdRatio, damagePerMinute, kills, deaths, assists, losses, alliesRevived, diableries, damageDone, distanceTraveled, avgTimeAlive, killPerMatch, damagePerMatch, bAccuracy, title

