from django.db import models

# Create your models here.
    
class KaizenUser(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField('User Email')
    department = models.CharField(max_length=50)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name + '' + self.last_name