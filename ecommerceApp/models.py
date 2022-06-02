from django.db import models
import django
from django.utils import timezone
# Create your models here.

class product(models.Model):
    title=models.CharField(max_length=50)
    image=models.ImageField()
    image_1=models.ImageField(null=True)
    image_2=models.ImageField(null=True)
    ptype=models.CharField(max_length=50)
    pname=models.CharField(max_length=50)
    price=models.CharField(max_length=20)
    pdetails=models.TextField()
    date_added=models.DateTimeField(default=django.utils.timezone.now)

    def __str__(self):
        return self.pname

    class Meta:
        ordering = ['-date_added']

class comment(models.Model):
    uname=models.CharField(max_length=20)
    email=models.EmailField()
    review=models.TextField()

    def __str__(self):
        return self.uname

