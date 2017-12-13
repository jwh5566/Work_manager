from django import forms
from .models import Supervisor, Developer, Task
from django.contrib.auth import authenticate, login

error_name = {
    'required': 'you must type a name!',
    'invalid': 'Wrong format.'
}


class Form_task_time(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['time_elapsed']


class Form_task_delete(forms.Form):
    task = forms.IntegerField()


class Form_project_create(forms.Form):
    title = forms.CharField(label="Title", max_length=30)
    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'cols': 100}))
    client_name = forms.CharField(label="Client", max_length=50)


class Form_inscription(forms.Form):
    name = forms.CharField(label="Name", max_length=30, error_messages=error_name)
    login = forms.CharField(label="Login", max_length=30, help_text="Letters, digits and @/./+/-/_ only.")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password_bis = forms.CharField(label="password", widget=forms.PasswordInput, help_text="Enter the same password as before, for verification.")
    supervisor = forms.ModelChoiceField(label="Supervisor",
                                        queryset=Supervisor.objects.all())
    
    def clean(self):
        cleaned_data = super(Form_inscription, self).clean()
        password = self.cleaned_data.get('password')
        password_bis = self.cleaned_data.get('password_bis')

        if password and password_bis and password != password_bis:
            raise forms.ValidationError("Passwords are not identical.")
        return self.cleaned_data


class Form_connection(forms.Form):
    username = forms.CharField(label='Login')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super(Form_connection, self).clean()
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if not authenticate(username=username, password=password):
            raise forms.ValidationError("Wrong username or password!")
        return self.cleaned_data


# class Form_supervisor(forms.ModelForm):
#     class Meta:
#         model = Supervisor
#         exclude = ('date_created', 'last_connection')


class Form_supervisor(forms.Form):
    name = forms.CharField(label='Name', max_length=30)
    login = forms.CharField(label='Login')
    email = forms.EmailField(label='Email')
    specialisation = forms.CharField(label='Specialisation')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password_bis = forms.CharField(label='Password', widget=forms.PasswordInput)
    
    
    def clean(self):
        cleaned_data = super(Form_supervisor, self).clean()
        password = self.cleaned_data.get('password')
        password_bis = self.cleaned_data.get('password_bis')
        if password and password_bis and password != password_bis:
            raise forms.ValidationError("Passwords are not identical.")
        return self.cleaned_data
