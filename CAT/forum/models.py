from django.db import models
import datetime


# class Users(models.Model):
# 	user_name = models.CharField(primary_key = True, max_length=50)
# 	first_name = models.CharField(max_length=100)
# 	last_name = models.CharField(max_length=100)
# 	cell_num = models.CharField(max_length=10)
# 	email_id = models.CharField(max_length=100)

class Question(models.Model):
	question = models.TextField()
	question_id = models.AutoField(primary_key = True)