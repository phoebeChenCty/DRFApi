from django.db import models


class Cake(models.Model):
    title = models.CharField(max_length=120)
