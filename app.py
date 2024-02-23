from flask import Flask, render_template, request
from datetime import timedelta

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_plan', methods=['GET', 'POST'])  # Allow both GET and POST requests for this route
def generate_plan():
    if request.method == 'POST':  # Ensure method is POST
        age = int(request.form['age'])
        workout_time = request.form['workout-time']
        activities = request.form.getlist('activities')
        activity_days = request.form.getlist('activity-days')
        weight = float(request.form['weight'])
        goals = request.form['goals']

        # Logic to generate fitness plan
        # You can use the provided code for generating the plan here

        # For demonstration purposes, let's assume we generate a sample plan
        plan = {
            'age': age,
            'workout_time': workout_time,
            'activities': activities,
            'activity_days': activity_days,
            'weight': weight,
            'goals': goals
        }

        return render_template('plan.html', plan=plan)
    else:
        return render_template('index.html')  # Render the index.html template for GET requests

if __name__ == '__main__':
    app.run(debug=True)
