from django.db import models


class Employee(models.Model):
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    department = models.CharField(max_length=50,null=False)
    salary = models.IntegerField(null=False)

    def __str__(self):
        return self.first_name