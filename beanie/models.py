from django.db import models

# Create your models here.
class Demographic(models.Model):
    sex_choices=[('M','Male'),('F','Female')]
    respondent_code=models.IntegerField(null=True)
    name=models.TextField()
    contact_number=models.IntegerField(null=True)
    address=models.TextField()
    sex=models.CharField(choices=sex_choices, max_length=1, blank=True)
    household_size=models.IntegerField(null=True)
    household_income=models.IntegerField(null=True)
    submission_date=models.DateTimeField()
