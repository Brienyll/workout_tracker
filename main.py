import requests
from datetime import datetime
import os

GENDER = "male"
WEIGHT = "97.5224"
HEIGHT = "177.8"
AGE = "40"

NUTRITIONIX_API_ID = os.environ["7ee804e6"]
NUTRITIONIX_API = os.environ["37741896747764f6949f267f6e831fee"]

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = os.environ["https://api.sheety.co/edfd8afcaa4132cfdeee65e57cdda9d6/myWorkouts/workouts"]

exercise_text = input("What Exercises did you do: ")

headers = {
    "x-app-id": NUTRITIONIX_API_ID,
    "x-app-key": NUTRITIONIX_API,
}

exercises_params = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

response = requests.post(nutritionix_endpoint, json=exercises_params, headers=headers)
result = response.json()
print(result)

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")
bearer_headers = {
        "Authorization": f"Bearer {os.environ['devndevndev29']}"
    }

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheety_endpoint, json=sheet_inputs, headers=bearer_headers)

    print(sheet_response.text)

