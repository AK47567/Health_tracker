import random
import os
from decimal import Decimal
import django
from faker import Faker


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'health_tracker.settings')  # Replace 'your_project' with your actual project name
django.setup()
from api.models import BMI

fake = Faker()

def generate_fake_bmi_data():
    MIN_BMI = 0.0
    MAX_BMI = 45.0
    STEP = Decimal('0.1')

    bmi_values = []

    current_bmi = Decimal(MIN_BMI)
    while current_bmi <= Decimal(MAX_BMI):
        bmi_values.append(round(float(current_bmi), 1))
        current_bmi += STEP

    bmi_data = [{'bmi_value': bmi, 'classification': get_classification(bmi)} for bmi in bmi_values]

    return bmi_data

def get_classification(bmi):
    # Define your classification logic based on the BMI ranges
    # Modify this according to your specific classification criteria
    if bmi < 18.5:
        return 'Underweight'
    elif 18.5 <= bmi <= 24.9:
        return 'Normal weight (Healthy)'
    elif 25 <= bmi <= 29.9:
        return 'Overweight'
    elif 30 <= bmi <= 34.9:
        return 'Obesity (Class 1)'
    elif 35 <= bmi <= 39.9:
        return 'Obesity (Class 2)'
    else:
        return 'Obesity (Class 3) or Severe Obesity'

def save_fake_bmi_data():
    bmi_data = generate_fake_bmi_data()

    for data in bmi_data:
        # Check if BMI entry with the same value already exists
        existing_bmi = BMI.objects.filter(bmi_value=data['bmi_value']).first()
        if not existing_bmi:
            BMI.objects.create(**data)

# Run the script to save fake BMI data
save_fake_bmi_data()