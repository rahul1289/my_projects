from django.db import models

# Create your models here.
from django.urls import reverse

class Product(models.Model):
    pname = models.CharField(max_length=200)
    price = models.IntegerField()

    def __str__(self):
        return self.pname

    def get_absolute_url(self):
        return reverse('P_edit', kwargs={'pk': self.pk})