from django.db import models

# Part 2: Create Mode
class EventRegistration(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    age = models.PositiveBigIntegerField()
    # I used PositiveIntegerField() for age so that it only accepts positive numbers :))
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name

# Create your models here.
