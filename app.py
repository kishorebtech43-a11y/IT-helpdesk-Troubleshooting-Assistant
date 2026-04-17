from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

def log_issue(issue):
    with open("issues_log.txt", "a") as file:
        time = datetime.datetime.now()
        file.write(f"{time} - {issue}\n")

@app.route("/", methods=["GET", "POST"])
def home():
    solution = ""

    if request.method == "POST":
        issue = request.form["issue"]

        if issue == "internet":
            solution = "Check WiFi, restart router, run troubleshooter"
            log_issue("Internet Issue")

        elif issue == "slow":
            solution = "Close apps, restart system, check disk space"
            log_issue("Slow System")

        elif issue == "software":
            solution = "Restart software, reinstall, check updates"
            log_issue("Software Issue")

        elif issue == "printer":
            solution = "Check cable/WiFi, restart printer, reinstall driver"
            log_issue("Printer Issue")

    return render_template("index.html", solution=solution)