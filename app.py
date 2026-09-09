import os

from flask import Flask, render_template, request, redirect, url_for
from trip_data import trips

app = Flask(__name__)
app.secret_key = os.environ['SECRET_KEY']


@app.route("/")
def home():

    upcoming_trips = []
    planning_trips = []
    completed_trips = []

    total_budget = 0
    total_spent = 0
    total_activities = 0
    total_memories = 0

    for trip in trips:

        if trip["status"] == "Upcoming":
            upcoming_trips.append(trip)

        if trip["status"] == "Planning":
            planning_trips.append(trip)

        if trip["status"] == "Completed":
            completed_trips.append(trip)

        # Add each trip's budget
        total_budget += trip["budget"]

        # Add each trip's expenses
        for expense in trip["expenses"]:
            total_spent += expense["amount"]

        # Count activities
        total_activities += len(trip["activities"])

        # Count memories
        total_memories += len(trip["memories"])

    # Calculate remaining budget
    remaining_budget = total_budget - total_spent

    # Calculate percentage of budget spent
    if total_budget > 0:
        budget_percentage = round(
            total_spent / total_budget * 100
        )
    else:
        budget_percentage = 0

    # Find the next upcoming trip
    next_trip = None

    if upcoming_trips:
        next_trip = upcoming_trips[0]

    return render_template(
        "index.html",
        user_name="Yoni",
        trips=trips,
        upcoming_trips=upcoming_trips,
        planning_trips=planning_trips,
        completed_trips=completed_trips,
        next_trip=next_trip,
        total_budget=total_budget,
        total_spent=total_spent,
        remaining_budget=remaining_budget,
        budget_percentage=budget_percentage,
        total_activities=total_activities,
        total_memories=total_memories
    )


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

    return render_template(
        "all_trips.html",
        trips=trips,
        upcoming_trips=upcoming_trips,
        planning_trips=planning_trips,
        completed_trips=completed_trips
    )


@app.route("/trip/<int:trip_id>")
def trip_details(trip_id):

    selected_trip = None

    for trip in trips:

        if trip["id"] == trip_id:
            selected_trip = trip
            break

    if selected_trip:

        total_spent = sum(
            expense["amount"]
            for expense in selected_trip["expenses"]
        )

        remaining = selected_trip["budget"] - total_spent

        budget_percentage = (
            round(
                total_spent
                / selected_trip["budget"]
                * 100
            )
            if selected_trip["budget"] > 0
            else 0
        )

    else:

        total_spent = 0
        remaining = 0
        budget_percentage = 0

    return render_template(
        "trip.html",
        trip=selected_trip,
        total_spent=total_spent,
        remaining=remaining,
        budget_percentage=budget_percentage
    )


@app.route("/all_trips/new", methods=["GET", "POST"])
def create_trip():

    if request.method == "POST":

        destination = request.form["destination"]
        start_date = request.form["start_date"]
        end_date = request.form["end_date"]
        budget = request.form["budget"]
        description = request.form["description"]
        trip_type = request.form["trip_type"]

        # Get activity fields
        activity_days = request.form.getlist("activity_day")
        activity_times = request.form.getlist("activity_time")
        activity_names = request.form.getlist("activity_name")

        activities = []

        for position in range(len(activity_names)):

            if (
                activity_names[position]
                and activity_days[position]
                and activity_times[position]
            ):

                activities.append({
                    "day": int(activity_days[position]),
                    "time": activity_times[position],
                    "activity": activity_names[position],
                    "completed": False
                })

        # Get expense fields
        expense_categories = request.form.getlist("expense_category")
        expense_descriptions = request.form.getlist(
            "expense_description"
        )
        expense_amounts = request.form.getlist("expense_amount")

        expenses = []

        for position in range(len(expense_descriptions)):

            if (
                expense_descriptions[position]
                and expense_amounts[position]
            ):

                expenses.append({
                    "category": expense_categories[position],
                    "description": expense_descriptions[position],
                    "amount": float(expense_amounts[position])
                })

        # Create the new trip
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
            "memories": []
        }

        trips.append(new_trip)

        return redirect(url_for("all_trips"))

    return render_template("create_trip.html")


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True, port=8000)
