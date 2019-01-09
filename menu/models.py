from django.db import models

# Create your models here.

class Menu(models.Model):
    name = models.CharField(max_length=200)

    def publish(self):
        self.save()
    
    def __str__(self):
        return self.name