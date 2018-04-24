from django.db import models

# Create your models here.
class Contents(models.Model):
    name = models.CharField(max_length=32)
    content = models.TextField()
    def __str__(self):
        return (self.name + ": " + self.content)
