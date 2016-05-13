from datetime import datetime
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    now = datetime.now()
    timeString = strftime("%Y-%m-%d %H:%M")
    
    date = int(timeString[8:10])
    
    dl = 20 - date
    DL = str(dl)
    
    templateData = {
        'title' : "Hello",
        'time' : timeString,
        'DL' : DL
    }
    return render_template("main.html", **templateData)

if __name__ == "__main__":
    app.run()
