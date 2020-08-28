from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template("welcome.html")

 @app.route('/date')
 def date():
     return "This page was served at " + str(datetime.now())

 counter = 0

 @app.route("/count_views")
 def count_demo():
     global counter
     counter += 1
     return "This page was served " + str(counter) + " times"
