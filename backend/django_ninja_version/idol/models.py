from django.db import models

# Create your models here.

class Group(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.name}"

class Idol(models.Model):
    name = models.CharField(max_length=50)
    birthday = models.DateField()
    birthplace = models.CharField(max_length=10, db_comment="出身地")
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)
    profile_image = models.ImageField(null=True , blank=True)
    def __str__(self):
        return f"idol: {self.name}"

class CD(models.Model):
    title = models.CharField(max_length=50)
    release_date = models.DateField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
