from django.db import models

# Create your models here.
# Create your models here.
hearingStatus = (('not_selected', 'not selected'),
                 ('accepted', 'accepted'),
                 ('rejected', 'rejected'),
                 )


class Hearing(models.Model):
    email = models.EmailField(max_length=100)
    email_hearing_by = models.EmailField(max_length=254)
    message = models.TextField()
    jobHearingStatus = models.CharField(
        choices=hearingStatus, default='not_selected', max_length=20)
    is_accepting_The_offer = models.BooleanField("Is Need Job", default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.message
