from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    password = models.CharField(max_length=120)
    is_private = models.BooleanField(default=False)

    def _str_(self):
        return self.name
