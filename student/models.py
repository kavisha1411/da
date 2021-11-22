from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=30)
    department = models.CharField(max_length=30)

    class Meta:
        db_table = 'teacher'
        verbose_name = 'Teacher Detail'
        verbose_name_plural = 'Teacher Details'

    def __str__(self) -> str:
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=20)
    standard = models.IntegerField()
    teacher = models.ManyToManyField(Teacher, db_table='reference_table')

    class Meta:
        db_table = 'student'
        verbose_name = 'Student Detail'
        verbose_name_plural = 'Student Details'

    def __str__(self) -> str:
        return self.name

