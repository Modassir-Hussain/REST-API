from django.db import models

class emp(models.Model):
    enum = models.IntegerField()
    ename = models.CharField(max_length=64)
    esla = models.FloatField()
    eaddr = models.CharField(max_length=256)

    def __str__(self):
        return self.ename
