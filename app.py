from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import scripts.comparison as c
import scripts.getuserstats as g


app = Flask(__name__)

@app.route("/")
def index():
    id1 = "16368163461376577876"
    id2 = "10363298386750518290"
    firstUser = g.getUserStats(id1)
    secondUser = g.getUserStats(id2)
    firstUserTitle = firstUser[16]
    secondUserTitle = secondUser[16]
    win_percentage = c.wPercentageCompare(firstUser, secondUser, firstUserTitle, secondUserTitle)
    wins = c.winsCompare(firstUser, secondUser, firstUserTitle, secondUserTitle)
    kd_ratio = c.kdRatioCompare(firstUser, secondUser, firstUserTitle, secondUserTitle)
    damage_per_min = c.damageperminCompare(firstUser, secondUser, firstUserTitle, secondUserTitle)
    kills = c.killsCompare(firstUser, secondUser, firstUserTitle, secondUserTitle)
    deaths = c.deathsCompare(firstUser, secondUser, firstUserTitle, secondUserTitle)
    assists = c.assistsCompare(firstUser, secondUser, firstUserTitle, secondUserTitle)
    losses = c.lossesCompare(firstUser, secondUser, firstUserTitle, secondUserTitle)
    allies_revived = c.alliesRevivedCompare(firstUser, secondUser, firstUserTitle, secondUserTitle)
    diableries = c.diableriesCompare(firstUser, secondUser, firstUserTitle, secondUserTitle)
    damage_done = c.damageDoneCompare(firstUser, secondUser, firstUserTitle, secondUserTitle)
    distance_traveled = c.distanceTraveledCompare(firstUser, secondUser, firstUserTitle, secondUserTitle)
    average_time_alive = c.averageTimeAliveCompare(firstUser, secondUser, firstUserTitle, secondUserTitle)
    kill_per_match = c.killPerMatchCompare(firstUser, secondUser, firstUserTitle, secondUserTitle)
    damage_per_match = c.damagePerMatchCompare(firstUser, secondUser, firstUserTitle, secondUserTitle)
    bullet_accuracy = c.bulletAccuracyCompare(firstUser, secondUser, firstUserTitle, secondUserTitle)
    return render_template("index.html", win_percentage=win_percentage, wins=wins, kd_ratio=kd_ratio, damage_per_min=damage_per_min, kills=kills, deaths=deaths, assists=assists, losses=losses, allies_revived=allies_revived, diableries=diableries, damage_done=damage_done, distance_traveled=distance_traveled, average_time_alive=average_time_alive, kill_per_match=kill_per_match, damage_per_match=damage_per_match, bullet_accuracy=bullet_accuracy)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(debug=True)
    app.static_folder = 'static'