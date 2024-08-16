from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=50)
    des=models.TextField()
    email = models.EmailField(unique=True)
    def __str__(self):
        return self.name