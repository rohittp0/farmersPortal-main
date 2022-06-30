from django.conf import settings
from django.db import models
from accounts.models import User

from admins.models import Crop


class FarmerCropDetails(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    land_per_hectare = models.IntegerField('Land per hectare', default=0)
    crop_category = models.ForeignKey(Crop, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.crop_category}-{self.user.username}"


class HiringRequest(models.Model):
    from_user = models.ForeignKey(User, related_name="from_user", on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name="to_user", on_delete=models.CASCADE)
    accepted = models.BooleanField(blank=True, null=True)
    rejected = models.BooleanField(blank=True, null=True)
