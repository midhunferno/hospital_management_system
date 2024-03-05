from django.db import models

# Create your models here.
class doctor(models.Model):
    name = models.CharField(max_length=20)
    mobile = models.IntegerField()
    special = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
 
class patient(models.Model):
    name = models.CharField(max_length=30)
    gender = models.CharField(max_length=10)
    mobile = models.IntegerField(null=True)
    address = models.TextField()
    def __str__(self):
        return self.name


class appoiment(models.Model):
    doctor=models.ForeignKey(doctor,on_delete=models.CASCADE)
    patient=models.ForeignKey(patient,on_delete=models.CASCADE)
    date=models.DateField()
    time=models.TimeField()      