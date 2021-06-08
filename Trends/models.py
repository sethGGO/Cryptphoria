from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.utils import timezone

#Create database by using makemigrations command in terminal

#CREATE TABLE "Trends_trend" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "coin_name" varchar(100) NOT NULL,
# "datetime" datetime NOT NULL, "post_count" integer NOT NULL, "sentiment" integer NOT NULL);

class Trend(models.Model):
    coin_name= models.CharField(max_length=100)
    datetime= models.DateTimeField(auto_now_add=True)
    post_count= models.IntegerField()
    sentiment= models.IntegerField()








# count for each tweet per hour
# date time
# name
# sentiment score
