from django.db import models

class Registration(models.Model):
    username = models.CharField('Username',max_length=50)
    password = models.CharField('Password',max_length=255)

    def __str__(self):
        return self.username
    
    
class Login(models.Model):
    username = models.CharField('Username',max_length=50)
    password = models.CharField('Password',max_length=255)
