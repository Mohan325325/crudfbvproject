from .models import EmployeeModel
from django.forms import ModelForm

class EmployeeForm(ModelForm):
    class Meta:
        model = EmployeeModel
        fields = '__all__'
