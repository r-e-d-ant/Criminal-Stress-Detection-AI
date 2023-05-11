import os
from django.shortcuts import render
from django.template  import loader
from joblib import load

def index(request):
	return render(request, "criminal_stress_detection_app/index.html")

def required_data(request):
    return render(request, "criminal_stress_detection_app/required-data.html")

model_path = os.path.join(os.path.dirname(__file__), 'savedModels/stress-predictor.joblib')
model = load(model_path)

def service(request):
    if request.method == 'POST':
        # Retrieve form data
        snoring_rate = request.POST.get('snoring_rate')
        respiration_rate = request.POST.get('respiration_rate')
        body_temperature = request.POST.get('body_temperature')
        limb_movement = request.POST.get('limb_movement')
        blood_oxygen = request.POST.get('blood_oxygen')
        eye_movement = request.POST.get('eye_movement')
        sleeping_hours = request.POST.get('sleeping_hours')
        heart_rate = request.POST.get('heart_rate')

        if snoring_rate != "" and respiration_rate != "" and body_temperature != "" and \
            limb_movement != "" and blood_oxygen != "" and eye_movement != "" and sleeping_hours != "" and heart_rate != "":
             # predict with trained model
            prediction = model.predict([[snoring_rate, respiration_rate, body_temperature, limb_movement, blood_oxygen, eye_movement, sleeping_hours, heart_rate]])
            stress_level = prediction

            submitted_data = {
                'snoring_rate': snoring_rate,
                'respiration_rate': respiration_rate,
                'body_temperature': body_temperature,
                'limb_movement': limb_movement,
                'blood_oxygen': blood_oxygen,
                'eye_movement': eye_movement,
                'sleeping_hours': sleeping_hours,
                'heart_rate': heart_rate,
                'stress_level': stress_level
            }
        else:
             submitted_data = {
                'snoring_rate': 0,
                'respiration_rate': 0,
                'body_temperature': 0,
                'limb_movement': 0,
                'blood_oxygen': 0,
                'eye_movement': 0,
                'sleeping_hours': 0,
                'heart_rate': 0,
                'stress_level': 0
            }

        # Render the template with the submitted_data
        return render(request, 'criminal_stress_detection_app/service.html', {'submitted_data': submitted_data})

    # Render the template for GET requests
    return render(request, "criminal_stress_detection_app/service.html")
