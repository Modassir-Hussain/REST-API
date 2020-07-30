from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()




class Employee(models.Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length=256,blank=True)
    esal = models.FloatField(blank=True)
    eaddr = models.CharField(max_length=256,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    

    def __str__(self):
        return self.ename

    class Meta:
        ordering = ['created']

