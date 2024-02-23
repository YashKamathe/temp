<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fitness Plan Generator</title>
</head>
<body>
    <h1>Generate Your Fitness Plan</h1>
    <form action="/generate_plan" method="post">
        <label for="age">Age:</label>
        <input type="number" id="age" name="age" required><br><br>

        <label for="workout-time">Preferred Workout Time:</label>
        <select id="workout-time" name="workout-time">
            <option value="Morning">Morning</option>
            <option value="Afternoon">Afternoon</option>
            <option value="Evening">Evening</option>
        </select><br><br>

        <label>Additional Activities:</label><br>
        <input type="checkbox" id="yoga" name="activities" value="Yoga">
        <label for="yoga">Yoga</label><br>
        <input type="checkbox" id="swimming" name="activities" value="Swimming">
        <label for="swimming">Swimming</label><br>
        <input type="checkbox" id="sports" name="activities" value="Playing Sports">
        <label for="sports">Playing Sports</label><br><br>

        <label for="activity-days">Additional Activity Days:</label><br>
        <input type="checkbox" id="monday" name="activity-days" value="Monday">
        <label for="monday">Monday</label><br>
        <input type="checkbox" id="tuesday" name="activity-days" value="Tuesday">
        <label for="tuesday">Tuesday</label><br>
        <input type="checkbox" id="wednesday" name="activity-days" value="Wednesday">
        <label for="wednesday">Wednesday</label><br>
        <input type="checkbox" id="thursday" name="activity-days" value="Thursday">
        <label for="thursday">Thursday</label><br>
        <input type="checkbox" id="friday" name="activity-days" value="Friday">
        <label for="friday">Friday</label><br><br>

        <label for="weight">Weight (kg):</label>
        <input type="number" id="weight" name="weight" required><br><br>

        <label for="goals">Fitness Goals:</label><br>
        <textarea id="goals" name="goals" rows="4" required></textarea><br><br>

        <button type="submit">Generate Plan</button>
    </form>
</body>
</html>
