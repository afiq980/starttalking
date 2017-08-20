from django.db import models


class Season(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    from_date = models.DateField()
    to_date = models.DateField()

    class Meta:
        app_label = 'playundercover'


class Pair(models.Model):
    id = models.AutoField(primary_key=True)
    word1 = models.CharField(max_length=20)
    word2 = models.CharField(max_length=20)
    level = models.IntegerField(default=0)
    season = models.ForeignKey(Season, on_delete=models.CASCADE, null=True, default=None)

    class Meta:
        app_label = 'playundercover'


class User(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=50, primary_key=True)

    class Meta:
        app_label = 'playundercover'


class UserPair(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User)
    pair = models.ForeignKey(Pair)

    class Meta:
        app_label = 'playundercover'


class Namelist(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, unique=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=14)

    class Meta:
        app_label = 'playundercover'