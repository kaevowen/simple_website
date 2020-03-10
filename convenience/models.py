from django.db import models


class CU_Products(models.Model):
    prodName = models.CharField(max_length=64, unique=True)
    prodPrice = models.CharField(max_length=20)
    prodBonus = models.CharField(max_length=10)

    def __str__(self):
        return self.prodName


class GS25_Products(models.Model):
    prodName = models.CharField(max_length=64, unique=True)
    prodPrice = models.CharField(max_length=20)
    prodBonus = models.CharField(max_length=10)

    def __str__(self):
        return self.prodName