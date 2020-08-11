from django.db import models


# Create your models here.
class Submit(models.Model):
    clsCode = models.CharField(max_length=20)
    stu_id = models.CharField(max_length=20)


class Classes(models.Model):
    clsCode = models.CharField(max_length=20)
    cls_name = models.CharField(max_length=50)
    ownedby = models.CharField(max_length=15)


