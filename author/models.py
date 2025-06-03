from django.db import models

class employee(models.Model):
    name=models.CharField(max_length=100)
    email = models.EmailField(default='test@example.com')
    password = models.CharField(max_length=255, default='defaultpassword123')
    

