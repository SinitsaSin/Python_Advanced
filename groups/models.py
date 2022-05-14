from django.db import models

class Groups(models.Model):
    name = models.CharField(max_length=100)
    count_students = models.PositiveIntegerField()


    def __str__(self):
        return f'{self.name} {self.count_students}'
