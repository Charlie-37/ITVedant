from django import forms
from .models import Emp,EmpQuali,EmpQuali2,EmpQuali3

class EmpForm(forms.ModelForm):
    class Meta:
        model=Emp
        fields="__all__"

class EmpQualiForm(forms.ModelForm):
    class Meta:
        model=EmpQuali
        fields="__all__"

class EmpQualiForm2(forms.ModelForm):
    class Meta:
        model=EmpQuali2
        fields="__all__"


class EmpQualiForm3(forms.ModelForm):
    class Meta:
        model=EmpQuali3
        fields="__all__"

from .models import Singer,Songs
class SingerForm(forms.ModelForm):
    class Meta:
        model=Singer
        fields="__all__"

class SongsForm(forms.ModelForm):
    class Meta:
        model=Songs
        fields="__all__"
