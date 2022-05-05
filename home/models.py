from django.db import models

class Contact(models.Model):
    names = models.CharField(max_length=30)
    email = models.EmailField()
    phone=models.CharField(max_length=10)
    desc=models.TextField()
    def __str__(self):
        return self.names