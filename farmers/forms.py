from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User
from admins.models import Crop
from employees.models import Hearing
from farmers.models import FarmerCropDetails


class FarmerSignUpForm(UserCreationForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    age = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    address = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    aadhar = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    state = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    hector = forms.FloatField()
    is_farmer = forms.BooleanField(
        disabled=True,
        initial=True,
        widget=forms.CheckboxInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2',
                  'is_farmer', 'age', 'phone', 'address', 'aadhar', "corps", "hector")


class HiringEmployeeForm(forms.ModelForm):
    class Meta:
        model = Hearing
        fields = ('email', 'email_hearing_by', 'message')
        labels = {
            'email': 'Employee Name',
            "email_hearing_by": 'My Email',
            'message': "Message For Employee"
        }

        def __init__(self, *args, **kwargs):
            super(HiringEmployeeForm, self).__init__(*args, **kwargs)
            for visible in self.visible_fields():
                visible.field.widget.attrs['class'] = 'form-control'


class FarmerDetailsForm(forms.ModelForm):
    class Meta:
        model = FarmerCropDetails
        fields = ('crop_category', 'land_per_hectare')

    land_per_hectare = forms.IntegerField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    crop_category = forms.ModelChoiceField(
        label="Crop Category",
        queryset=Crop.objects.all(),
        widget=forms.Select(
            attrs={
                "class": "form-control",
            }
        )
    )

    # def __init__(self, *args, **kwargs):
    #     super(FarmerDetailsForm, self).__init__(*args, **kwargs)
