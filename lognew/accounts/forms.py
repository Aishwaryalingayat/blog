from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from accounts.models import User

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','password1','password2','email', 'profile_pic']