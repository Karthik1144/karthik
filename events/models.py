from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    location = models.CharField(max_length=100)
    venue = models.CharField(max_length=100)
    available_seats = models.IntegerField()
    description = models.TextField()
    slug = models.SlugField(unique=True)  # This will help in the URL

    def __str__(self):
        return self.title
