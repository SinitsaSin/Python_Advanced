from django.db import models
from faker import Faker

class Teachers(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    phone_number = models.CharField(max_length=25, null=True)

    class Meta():
        verbose_name = 'teacher'
        verbose_name_plural = 'teachers'
        db_table = 'teachers'

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.age} {self.phone_number}'

    @staticmethod
    def gen_teachers(cnt=10):
        fk = Faker()
        for _ in range(cnt):
            tc = Teachers(
                first_name = fk.first_name(),
                last_name = fk.last_name(),
                age = fk.random_int(min=18, max=45)

            )
            tc.save()
