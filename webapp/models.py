from django.db import models

# Create your models here.
class address(models.Model):
    street = models.CharField( max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.IntegerField()
    def __str__(self):
        return self.firstname

class employee(models.Model):
    firstname = models.CharField(primary_key=True,max_length=100)
    lastname = models.CharField(max_length=100)
    emp_id = models.IntegerField()
    # Adress = models.Foreignkey(address,on_delete=models.CASCADE)

    def __str__(self):
        return self.firstname


