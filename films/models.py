from django.db import models

class Film(models.Model):
    name = models.CharField("Name", max_length=250)
    short_name = models.CharField("Short name", max_length=250)
    icon_uri = models.CharField("Icon uri", max_length=250)
    data = models.JSONField("Data")

    def load_data(self):
        if 'name' in self.data:
            self.name = self.data['name']
        if 'shortName' in self.data:
            self.short_name = self.data['shortName']
        if 'iconUri' in self.data:
            self.icon_uri = self.data['iconUri']


    def __str__(self):
        return self.name