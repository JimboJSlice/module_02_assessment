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
        activity_days = request.form.getlist("activity_day")
        activity_times = request.form.getlist("activity_time")
        activity_names = request.form.getlist("activity_name")
        expense_categories = request.form.getlist("expense_category") 
        expense_descriptions = request.form.getlist("expense_description") 
        expense_amounts = request.form.getlist("expense_amount") 

        activities =[]

        for position in range(len(activity_names)):
            if activity_names[position]:
                activities.append({"day": int(activity_days[position]),
                                   "time": activity_times[position],
                                    "activity": activity_names[position],
                                    "completed": False
                                   })


        expenses = [] 

        for position in range(len(expense_descriptions)): 
            if expense_descriptions[position] and expense_amounts[position]: 
                expenses.append({ "category": expense_categories[position], 
                                 "description": expense_descriptions[position], 
                                 "amount": float(expense_amounts[position]) 
                                 })

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
            "activities": activities,
            "expenses": expenses,
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
