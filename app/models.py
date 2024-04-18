from django.db import models

# Create your models here.
class apps(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False)
    icon = models.CharField(max_length=500, null=False)
    link = models.CharField(max_length=500, null=False)
    discription = models.TextField(null=True)

    def __str__(self):
        return self.name