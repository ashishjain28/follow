from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from .models import Post, Profile


class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(label="First Name",
                                 max_length=50,
                                 required=True)
    last_name = forms.CharField(label="Last Name",
                                max_length=50,
                                required=True)
    email = forms.EmailField(label="Email ID",
                             max_length=50,
                             required=True)

    # def __init__(self, *args, **kwargs):
    #     super(ProfileForm, self).__init__(*args, **kwargs)
        # self.fields['first_name'] = self.user.first_name
        # self.fields['last_name'] = self.user.last_name
        # self.fields['email'] = self.user.email

    class Meta:
        model = Profile
        fields = [
            "mobile_number",
            "is_mobile_visible",
            "is_email_visible",
            "image"
        ]


class SignUpForm(forms.ModelForm):

    mobile_number = forms.CharField(label="Mobile Number",
                                    max_length=10,
                                    required=True)

    def clean_mobile_number(self):
        mobile = self.cleaned_data['mobile_number']

        error_message = []
        if not mobile.isdigit():
            error_message.append("Contact Number should contain only digits")
        if not len(mobile) == 10:
            error_message.append("Contact number should be of 10 digits")
        if error_message:
            raise ValidationError(error_message)
        return mobile

    class Meta:
        model = get_user_model()
        fields = [
            "username",
            "password",
            "email"
        ]


class CreatePostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = [
            "content",
            "post_image"
        ]

