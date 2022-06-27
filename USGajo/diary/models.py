from django.db import models

# Create your models here.
class Diary(models.Model):
    date = models.DateField(verbose_name ='날짜')
    weather = models.CharField(max_length=200, verbose_name ='날씨')
    contents = models.TextField(blank=True, null=True, verbose_name ='내용') #can't be blank
    mainphoto = models.FileField(upload_to='diaryPics', blank = True, null = True)
    #created = models.DateTimeField(auto_now_add=True, verbose_name ='작성일') #글 쓴 날짜

    def __str__(self):
        return self.weather  #should return string md later
