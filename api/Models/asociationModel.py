from django.db import models

class Asociation(models.Model):
    name = models.CharField(max_length=32, blank=False)

    def __str__(self):
        return self.name
