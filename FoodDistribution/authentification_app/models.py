from django.db import models

# Create your models here.


class DistributionSite(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    commune = models.CharField(max_length=255)

    def __str__(self):
        return self.name  