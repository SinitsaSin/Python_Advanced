from django.db import models


class Groups(models.Model):
    name = models.CharField(max_length=100)
    count_students = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'group'
        verbose_name_plural = 'groups'
        db_table = 'groups'

    def __str__(self):
        return f'{self.name} {self.count_students}'
