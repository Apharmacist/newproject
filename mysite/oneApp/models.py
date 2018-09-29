from django.db import models

# Create your models here.



class Grades(models.Model):

    g_name = models.CharField(max_length=20)
    g_date = models.DateTimeField()
    g_girl_num = models.IntegerField()
    g_boy_num = models.IntegerField()
    isDelete = models.BooleanField(default=False)


    def __str__(self):
        return self.g_name



class Students(models.Model):



    s_name = models.CharField(max_length=200)
    s_gender = models.BooleanField(default=True)
    s_age = models.IntegerField()
    s_contend = models.CharField(max_length=200)
    isDelete = models.BooleanField(default=False)
    grades = models.ForeignKey(Grades, on_delete=models.CASCADE)
    # 这里有不同 on_delete 与其他版本不同


    def __str__(self):

        return self.s_name








