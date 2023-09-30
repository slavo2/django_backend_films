from django.db import models

class Film(models.Model):
    name = models.CharField("Name", max_length=250)
    short_name = models.CharField("Short name", max_length=250)
    icon_uri = models.CharField("Icon uri", max_length=250)
    data = models.JSONField("Data")
    def __str__(self):
        return self.name