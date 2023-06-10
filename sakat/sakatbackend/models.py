from django.db import models

class User(models.Model):
    name=models.TextField()

    def __str__(self):
        return self.name
       

class Doctor(models.Model):
    doctor=models.ForeignKey(User,on_delete=models.CASCADE)
    tag=models.TextField(max_length=30,null=True)
    address=models.TextField(max_length=30,null=True)
    
    def __str__(self):
        return f"{self.doctor.name} ({self.tag})"
    # daily_date_times=models.DateTimeField()
class Programs(models.Model):
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    
    title=models.TextField(max_length=50)
    

    #doktor ve user foreign key olarak gelecek baba
class Program_image(models.Model):
    program=models.ForeignKey(Programs,on_delete=models.CASCADE,)
    image=models.ImageField()