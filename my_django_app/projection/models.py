from django.db import models

class EnrollmentProjection(models.Model):
  id = models.CharField(max_length=10, primary_key=True)
  course_code = models.CharField(max_length=50)
  course_name = models.CharField(max_length=400)
  r2_value = models.FloatField(null = True)
  area = models.CharField(max_length=400)
  estimated_amount = models.IntegerField(null=True)
  class Meta:
    db_table = 'enrollment_projection'

  def __str__(self):
    return self.course_name