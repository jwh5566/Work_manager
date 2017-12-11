from django import forms
from .models import Supervisor, Developer

error_name = {
    'required': 'you must type a name!',
    'invalid': 'Wrong format.'
}


class Form_project_create(forms.Form):
    title = forms.CharField(label="Title", max_length=30)
    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'cols': 100}))
    client_name = forms.CharField(label="Client", max_length=50)


class Form_inscription(forms.Form):
    name = forms.CharField(label="Name", max_length=30, error_messages=error_name)
    login = forms.CharField(label="Login", max_length=30)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password_bis = forms.CharField(label="password", widget=forms.PasswordInput)
    supervisor = forms.ModelChoiceField(label="Supervisor",
                                        queryset=Supervisor.objects.all())
    
    def clean(self):
        cleaned_data = super(Form_inscription, self).clean()
        password = self.cleaned_data.get('password')
        password_bis = self.cleaned_data.get('password_bis')

        if password and password_bis and password != password_bis:
            raise forms.ValidationError("Passwords are not identical.")
        return self.cleaned_data


class Form_supervisor(forms.ModelForm):
    class Meta:
        model = Supervisor
        exclude = ('date_created', 'last_connection')