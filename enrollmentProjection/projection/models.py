from django.db import models

class EnrollmentProjection(models.Model):
  id = models.CharField(max_length=10, primary_key=True)
  course_code = models.CharField(max_length=50)
  course_name = models.CharField(max_length=400)
  academic_period = models.CharField(max_length=50)
  area = models.CharField(max_length=400)
  estimated_amount = models.IntegerField(null=True)
  class Meta:
    db_table = 'enrollment_projection'

  def __str__(self):
    return self.name
