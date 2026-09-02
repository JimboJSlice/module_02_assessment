import os

from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = os.environ['SECRET_KEY']


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/trips")
def trips():
    return render_template("trips.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True, port=8000)

# Functions

# 
# Display trips()
# create a trip()
# itinerary ()
# budget()
# calculate_total()
# budget_percentage()
# add_memory()
# get_next_trip()

# get and post for create trips, add memories(images), budget, itinerary