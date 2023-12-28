from django.db import models


class SpecialHeadline(models.Model):
    content = models.TextField()
    imgage = models.ImageField(upload_to="home/static/images")


class attractionsHeadline(models.Model):
    content = models.TextField()
    imgage = models.ImageField(upload_to="home/static/images")


class mostVisitedHeadline(models.Model):
    content = models.TextField()
    imgage = models.ImageField(upload_to="home/static/images")


class politicalNews(models.Model):
    content = models.TextField()


class economicNews(models.Model):
    content = models.TextField()


class sportNews(models.Model):
    content = models.TextField()


class culturalNews(models.Model):
    content = models.TextField()
