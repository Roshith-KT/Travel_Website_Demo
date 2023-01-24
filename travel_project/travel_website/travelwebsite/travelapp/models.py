from django.db import models


# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to='pics')
    description = models.TextField()

    def __str__(self):
        return self.name


class TeamMembers(models.Model):
    member_name = models.CharField(max_length=255)
    member_img = models.ImageField(upload_to='pics')
    member_description = models.TextField()

    def __str__(self):
        return self.member_name
