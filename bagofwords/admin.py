from django.contrib import admin
from .models import Sentiment, Dictionary
# Register your models here.

admin.site.register(Sentiment)
admin.site.register(Dictionary)
