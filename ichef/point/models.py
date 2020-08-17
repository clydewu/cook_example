# -*- coding:utf-8 -*-
from django.db import models


class Member(models.Model):
    mobile = models.CharField(max_length=128, null=False, primary_key=True)
    name = models.CharField(max_length=128, null=False, unique=True, db_index=True)


class Point(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    point = models.IntegerField(null=False)
