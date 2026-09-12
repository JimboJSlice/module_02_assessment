# Roamly Python Assignment

# Roamly

**Plan. Explore. Remember.**

## Description

Roamly is a travel planning and recording web application built with Python and Flask. It allows users to create trips, organise activities, track expenses, and view memories from their travels.

The project was developed to demonstrate Python programming, Flask, Jinja templates, HTML/CSS, responsive design, and clean code organisation.

## Features

- Personal travel dashboard
- View upcoming, planning, and completed trips
- Create new trips
- Add activities, itinerary details, and image URLs
- Track trip expenses and budgets
- View remaining budget and spending progress
- Store and display travel memories
- Responsive mobile-first design
- Individual pages for each trip

## Tech Stack

- **Python**
- **Flask**
- **Jinja2**
- **HTML5**
- **CSS3**
- **Bootstrap 5**

Trip data is currently stored using Python lists and dictionaries.

## How It Works

Flask routes control the different pages of the application:

```text
/                       → Home dashboard
/all_trips              → View all trips
/all_trips/new          → Create a new trip
/trip/<trip_id>         → View an individual trip
/about                  → About Roamly
```

Users can create a trip through the HTML form. Flask uses `request.form` and `request.form.getlist()` to collect the submitted trip, activity, and expense information.

The data is then added to the trips list and displayed dynamically using Jinja templates.

Budget calculations, including total spending, remaining budget, and budget percentage, are handled in Python before being passed to the templates.

## Future Improvements

- Add a database for persistent data storage
- Add user authentication and profiles
- Allow users to edit and delete trips
- Allow users to upload travel photos
- Add dynamic activity and expense fields
- Add trip search and filtering
- Add interactive maps and travel information

## Deployment

The application is deployed using Render.

1. Upload/push the project to Github
2. Create a new Web Service on Render
3. Connect Github repository
4. Install dependencies: 
    pip isntall -r requirements.txt
5. Use the following start command:
    gunicorn app:app
6. Add the SECRET_KEY environment variable
7. Deploy the application

## Live Site

https://module-02-assessment.onrender.com

## Author

JimboJSlice
