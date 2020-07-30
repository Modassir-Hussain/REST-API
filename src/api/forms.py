from django import forms
from .models import emp

class EmployeeForm(forms.ModelForm):
    def clean_esal(self):
        input_esal = self.cleaned_data['esal']
        # print(input_esal)
        if input_esal<5000:
            raise forms.ValidationError('Sal should be greater than 5000')
        return input_sal
    class Meta:
        model = emp
        fields = '__all__'
