from django.db import models



class CustomManager(models.Manager):
    def get_salary_500(self,esal):
        return super().get_queryset().filter(esal__eq=500)






class Employee(models.Model):
    eid= models.IntegerField()
    ename = models.CharField(max_length=50)
    esal = models.FloatField()
    objects = CustomManager

    def __str__(self):
        return f"{self.eid}--{self.ename}--{self.esal}"
