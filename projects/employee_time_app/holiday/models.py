from django.db import models
from employee.models import UserProfile
# Create your models here.

class Holiday(models.Model):
    HOLIDAY_TYPES = (('1', 'General Holiday'),('2', 'Weekly Holiday'))
    holiday_type = models.CharField(max_length=1, choices = HOLIDAY_TYPES)
    holiday_name = models.CharField(max_length=100)
    holiday_date = models.DateField()
    def __str__(self):
        return str(self.holiday_date) + ' ' + self.holiday_name
    

class PersonalLeave(models.Model):
    emp_id = models.ForeignKey(UserProfile)
    leave_name = models.CharField(max_length=100)
    leave_date = models.DateField()
    def __str__(self):
        return str(self.leave_date) + ' ' + self.leave_name + ' ' + self.emp_id.emp_id


class SpecialNotes(models.Model):
    emp_id = models.ForeignKey(UserProfile)
    note = models.CharField(max_length=100)
    note_date = models.DateField()
    def __str__(self):
        return str(self.note_date) + ' ' + self.emp_id.emp_id
