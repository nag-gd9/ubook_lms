from django import forms
from django.contrib.auth import authenticate, get_user_model


User = get_user_model()

# Login form with validation
 
class UserLoginForm(forms.Form):
    username = forms.CharField(label='User name', widget=forms.TextInput(attrs={'class':'form-control','id':"user", 'placeholder':"Enter User name",}),)
    password = forms.CharField(label='Password', widget=forms.TextInput(attrs={'class':'form-control','type':'password', 'placeholder':"Enter Password",}),)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('This user does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect password')
            if not user.is_active:
                raise forms.ValidationError('This user is not active')
        return super(UserLoginForm, self).clean(*args, **kwargs)



# Registration form with validation

class UserRegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=30, label='Username', widget=forms.TextInput(attrs={"type":"text", "name":"username", "class":"form-control", "id":"username", "placeholder":"Enter User name",}),)
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={"name":"email", "class":"form-control", "id":"email", "placeholder":"Enter Email",}),)
    password = forms.CharField(label='Password', widget=forms.TextInput(attrs={'class':'form-control','type':'password', 'placeholder':"Enter Password",}),)
    password2 = forms.CharField(label='Conform Password', widget=forms.TextInput(attrs={'class':'form-control','type':'password', 'placeholder':"Enter Password",}),)
    
# meta data on database
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password'
        ]

    def clean(self, *args, **kwargs):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError("Password must match")
        email_qs = User.objects.filter(email='email')
        if email_qs.exists():
            raise forms.ValidationError("This email has already been registered")
        return super(UserRegisterForm, self).clean(*args, **kwargs)

