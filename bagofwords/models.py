from django.db import models

class Dictionary(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Sentiment(models.Model):
    unit = models.CharField(max_length=255)
    positivity = models.DecimalField(max_digits=5, decimal_places=4, blank=True, null=True)
    negativity = models.DecimalField(max_digits=5, decimal_places=4, blank=True, null=True)
    objectivity = models.DecimalField(max_digits=5, decimal_places=4, blank=True, null=True)
    polarity = models.IntegerField(default=0)
    dictionary = models.ForeignKey(Dictionary, on_delete=models.CASCADE, default=0)
    def __str__(self):
        return self.unit
