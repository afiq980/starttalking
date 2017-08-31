from django.db import models

class Question(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=500)
    type = models.CharField(max_length=20)
    nsfw = models.BooleanField(default=False)