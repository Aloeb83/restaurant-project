from django.db import models

# Create your models here.

class Menu(models.Model):
    name = models.CharField(max_length=200)

    def publish(self):
        self.save()
    
    def __str__(self):
        return self.name

class Item(models.Model):
    menu = models.ForeignKey('menu.Menu', on_delete=models.CASCADE, related_name='item')
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=3, decimal_places=1)
    image = models.ImageField(upload_to='food_pictures', blank=True)

    def __str__(self):
        return self.name

