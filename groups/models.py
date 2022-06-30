from django.db import models


class Groups(models.Model):
    name = models.CharField(max_length=100)
    count_students = models.PositiveIntegerField()
    main_course = models.OneToOneField(
        'courses.Courses',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='main_courses'
    )

    class Meta:
        verbose_name = 'groups'
        verbose_name_plural = 'groups'
        db_table = 'groups'

    def __str__(self):
        return f'{self.name} {self.count_students}'
