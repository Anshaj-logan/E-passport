from django.db import models

# Create your models here.

# class user_model(models.Model):
#     username = models.CharField(max_length=256)
#     address = models.CharField(max_length=256)
#     gender = models.CharField(choices=GENDER_CHOICES,max_length=50)
#     phone_number = models.CharField(max_length=256)
#     passport_ofice = models.CharField(choices=CITY_CHOICES, max_length=50)
#     password= models.CharField(max_length=256)
#     image= models.ImageField(upload_to='images')
#     date=models.DateField()


GENDER_CHOICES = [
    ('male', 'MALE'),
    ('female', 'FEMALE'),
    ('other', 'OTHER'),
]



class user_model(models.Model):
    upload_image= models.ImageField(upload_to='images')
    upload_sign= models.ImageField(upload_to='images')
    passport_number = models.CharField(max_length=256)
    given_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    gender = models.CharField(choices=GENDER_CHOICES,max_length=50)
    date_of_birth=models.DateField()
    date_of_issue=models.DateField()
    date_of_expiry=models.DateField()
    
    def __str__(self):
            return self.given_name
    
class user_siup(models.Model):
    psprt_no = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


    

    def __str__(self):
        return self.username

