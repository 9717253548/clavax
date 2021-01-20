from django import forms
from django.forms import ModelForm
from student.models import StudentRecord

class StudentForm(ModelForm):
    """
    save student record.
    """
    class Meta:
        model = StudentRecord
        fields = '__all__'

    def clean_date_of_birth(self, date_of_birth):
        pass
