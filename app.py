import os

from flask import Flask, render_template
from trip_data import trips

app = Flask(__name__)
app.secret_key = os.environ['SECRET_KEY']


@app.route("/")
def home():
    return render_template("index.html", user_name="Yoni")

@app.route("/all_trips")
def all_trips():
    upcoming_trips = []
    planning_trips = []
    completed_trips = []

    for trip in trips:
        if trip["status"] == "Upcoming":
            upcoming_trips.append(trip)
        if trip["status"] == "Planning":
            planning_trips.append(trip)
        if trip["status"] == "Completed":
            completed_trips.append(trip)

    return render_template("all_trips.html", trips=trips, upcoming_trips=upcoming_trips, planning_trips=planning_trips,completed_trips=completed_trips)

@app.route("/trip/<int:trip_id>")
def trip_details(trip_id):

    selected_trip = None
    for trip in trips:
        if trip["id"] == trip_id:
            selected_trip = trip
    #create a 404 page

    return render_template("trip.html", trip=selected_trip)

@app.route("/create_trip")
def create_trip():
    return render_template("create_trip.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True, port=8000)

# Functions

# create a trip()
# itinerary ()
# budget()
# calculate_total()
# budget_percentage()
# add_memory()
# get_next_trip()

# get and post for create trips, add memories(images), budget, itinerary