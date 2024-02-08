from django.db import models
from django.contrib.auth.models import User

class BMI(models.Model):
    bmi_value = models.FloatField(verbose_name='BMI Value', unique=True, null=False)
    classification = models.CharField(max_length=50, blank=True)
    users = models.ManyToManyField('UserList', related_name='bmi_values')

    def save(self, *args, **kwargs):
        if self.bmi_value < 18.4:
            self.classification = 'Underweight'
        elif 18.5 <= self.bmi_value <= 24.9:
            self.classification = 'Normal weight (Healthy)'
        elif 25 <= self.bmi_value <= 29.9:
            self.classification = 'Overweight'
        elif 30 <= self.bmi_value <= 34.9:
            self.classification = 'Obesity (Class 1)'
        elif 35 <= self.bmi_value <= 39.9:
            self.classification = 'Obesity (Class 2)'
        else:
            self.classification = 'Obesity (Class 3) or Severe Obesity'

        super(BMI, self).save(*args, **kwargs)

    def __str__(self):
        return f'BMI: {self.bmi_value} - {self.classification}'

class UserList(models.Model):
    MALE = 'male'
    FEMALE = 'female'
    OTHER = 'other'

    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    Name = models.CharField(max_length=255, null=False, unique=True, default="Full Name")
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    height = models.FloatField(verbose_name='Height (meters)', default=0.0)
    weight = models.FloatField(verbose_name='Weight (kgs)', default=0.0)
    blood_type = models
    bmi = models.ManyToManyField(BMI, related_name='userlists', blank=True)

    def calculate_bmi(self):
        
        if self.height > 0 and self.weight > 0:
            bmi_value = round(self.weight / (self.height ** 2), 1)
            return bmi_value
        return None

    def save(self, *args, **kwargs):
        super(UserList, self).save(*args, **kwargs)  
        bmi_value = self.calculate_bmi()

       
        if bmi_value is not None:
            bmi, created = BMI.objects.get_or_create(bmi_value=bmi_value)
            self.bmi.add(bmi)

    def __str__(self):
        return f'{self.Name} - {self.age} years old'
