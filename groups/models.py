from django.db import models

class Groups(models.Model):
    name = models.CharField(max_length=100)
    count_students = models.PositiveIntegerField()

    class Meta():
        verbose_name = 'teacher'
        verbose_name_plural = 'teachers'


    def __str__(self):
        return f'{self.name} {self.count_students}'
