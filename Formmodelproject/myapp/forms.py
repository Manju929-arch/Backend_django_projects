from django import forms
from myapp.models import Student
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields= '__all__'
    def clean_name(self):
        n = self.cleaned_data['name']
        if len(n) <= 3:
            raise forms.ValidationError("Min no fthe char must greater than or equal to 4")
        return n
    def clean_age(self):
        a = self.cleaned_data['age']
        if a<=0:
            raise forms.ValidationError("age always positive")
        return a
    