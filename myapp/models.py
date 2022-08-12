from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Application_settings(models.Model):
    id = models.IntegerField(primary_key=True)
    module = models.CharField(max_length=50)
    setting_name = models.CharField(max_length=50)
    setting_value = models.CharField(max_length=250)
    is_enabled = models.IntegerField(null=True)

    def __str__(self):
        return self.module


