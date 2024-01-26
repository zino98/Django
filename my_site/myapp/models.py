from django.db import models

# Create your models here.

# Item(models.Model) -> models 
class Item(models.Model):  # 클래스 하나 당 데이터베이스의 테이블 하나
    itemId = models.CharField(max_length = 40, primary_key = True)  # 자료형
    itemName = models.CharField(max_length = 50)
    price = models.IntegerField()
    description = models.CharField(max_length = 50)
    pictureURL = models.CharField(max_length = 50)

# myapp_book 테이블 생성
class Book(models.Model):
    bookId = models.IntegerField(primary_key= True)
    title = models.CharField(max_length = 50)
    author = models.CharField(max_length = 50)
    publish_Date = models.DateField()
    price = models.IntegerField()