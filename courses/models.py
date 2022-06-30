from django.db import models


class Courses(models.Model):
    name = models.CharField(max_length=100)
    count_students = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'course'
        verbose_name_plural = 'courses'
        db_table = 'courses'

    def __str__(self):
        return f'{self.name} {self.count_students}'
