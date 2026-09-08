import os

from flask import Flask, render_template, request, redirect, url_for
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

@app.route("/all_trips/new", methods=["GET", "POST"])
def create_trip():

    if request.method == "POST":

        destination = request.form["destination"]
        start_date = request.form["start_date"]
        end_date = request.form["end_date"]
        budget = request.form["budget"]
        description = request.form["description"]
        trip_type = request.form["trip_type"]

        new_trip = {
            "id": len(trips) + 1,
            "destination": destination,
            "start_date": start_date,
            "end_date": end_date,
            "budget": float(budget),
            "description": description,
            "trip_type": trip_type,
            "status": "Planning",
            "image": "default-trip.jpg",
            "ativities": [],
            "expenses": [],
            "memories": [],
        }

        trips.append(new_trip)

        return redirect(url_for("all_trips"))

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