from django.db import models

# Create your models here.

class Knowledge(models.Model):
    title = models.CharField(max_length=256)
    text = models.TextField()
    autor = models.CharField(max_length=256)

    def __str__(self):
        return '{0}'.format(self.title)