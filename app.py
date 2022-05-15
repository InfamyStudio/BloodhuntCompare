from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import scripts.comparison as c
import scripts.getuserstats as g


app = Flask(__name__)
app.static_folder = 'static'
app.secret_key = b"&k;5fdRJSj%V4E8W:ysBYXF39A)a&RS[?hQ48R"
app.run(debug=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/results", methods=["POST"])
def results():
    id1 = str(request.form.get("playerid1"))
    id2 = str(request.form.get("playerid2"))
    firstUser = g.getUserStats(id1)
    if firstUser == None:
        flash("Invalid Player ID 1 entered!")
        return render_template("index.html")
    secondUser = g.getUserStats(id2)
    if secondUser == None:
        flash("Invalid Player ID 2 entered!")
        return render_template("index.html")
        
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
    return render_template("results.html", fut=firstUserTitle[:-2], sut=secondUserTitle[:-2], win_percentage=win_percentage, wins=wins, kd_ratio=kd_ratio, damage_per_min=damage_per_min, kills=kills, deaths=deaths, assists=assists, losses=losses, allies_revived=allies_revived, diableries=diableries, damage_done=damage_done, distance_traveled=distance_traveled, average_time_alive=average_time_alive, kill_per_match=kill_per_match, damage_per_match=damage_per_match, bullet_accuracy=bullet_accuracy)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
