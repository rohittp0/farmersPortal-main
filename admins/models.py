from django.db import models


# Create your models here.


class Announcements(models.Model):
    title = models.CharField("Title of Announcement", max_length=100)
    description = models.TextField("Announcement description")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    link = models.CharField(max_length=1000, default='')

    def __str__(self):
        return self.title


class Weather(models.Model):
    title = models.CharField("Title of Weather Report", max_length=100)
    url_of_weather = models.CharField("Drive Link", max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.url_of_weather


class Crop(models.Model):
    crop_name = models.CharField("Name Of crop", max_length=100)
    crop_price = models.IntegerField("Price of crop")
    crop_description = models.TextField("Description of crop", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    yield_per_hector = models.FloatField(default=0)

    def __str__(self):
        return self.crop_name
