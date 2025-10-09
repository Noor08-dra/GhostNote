from django import forms
from .models import message
from allauth.account.forms import (LoginForm, SignupForm, ResetPasswordForm,
                                   ResetPasswordKeyForm)
from crispy_forms.layout import Layout, Div, Field ,Row, Submit,HTML
from crispy_forms.helper import FormHelper

class MessageForm(forms.ModelForm): 
     class Meta:
          model=message
          fields=['recipient_name','msg_text']
          widgets={
               'recipient_name':forms.TextInput(attrs={'class':'form-control shadow-sm border-0','placeholder':"Recipient's name"}),
               'msg_text':forms.Textarea(attrs={'class':'message-area form-control shadow-sm','placeholder':'Your thoughts, unfiltered...','rows':5,'maxlength':240}),
}


class MyCustomLogin(LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields["password"].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter password'
        })
        
        self.fields["login"].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter email'
        })
        
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Div(
                Field("login", wrapper_class="mb-3 w-50 mx-auto"),
                Field("password", wrapper_class="mb-3 w-50 mx-auto"),
                Row(Submit('submit','Login',css_class="btn btn-lg btn-success w-50"),css_class="justify-content-center"),
                css_class="mx-auto"
            )
        )


class MyCustomSignup(SignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        if 'username' in self.fields:
            self.fields.pop('username')
        
        self.fields["email"].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter email'
        })
        
        self.fields["password1"].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter password'
        })
        
        self.fields["password2"].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Confirm password'
        })
        
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Div(
                Field('email', wrapper_class="mb-3 w-50 mx-auto"),
                Field('password1', wrapper_class="mb-3 w-50 mx-auto"),
                Field('password2', wrapper_class="w-50 mx-auto mb-3"),
                Row( Submit("submit","Create Account",css_class="btn btn-success btn-lg w-50"),css_class="justify-content-center"),
                css_class="mx-auto"
            )
        )



class MyCustomReset(ResetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields["email"].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter email'
        })
        
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Div(
                Field("email", wrapper_class="w-50 mx-auto"),
                Row(Submit('submit','Reset',css_class="btn btn-success btn-lg w-50 mt-3"),css_class="justify-content-center"),
                css_class="mx-auto my-4"
            )
        )

class MyCustomResetPasswordKey(ResetPasswordKeyForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Div(
                Field("password1", wrapper_class="w-50 mx-auto"),
                Field("password2", wrapper_class="w-50 mx-auto"),
                Row(
                    Submit('submit', 'Change password', css_class="btn btn-success btn-lg w-50 mt-3"),
                    css_class="justify-content-center"
                ),
                Row(
                     HTML('<a href="{% url \'account_login\' %}" class="btn btn-lg w-50 mt-3 text-decoration-none btn-outline-primary">Back to Login</a>'),
                     css_class="justify-content-center",
                ),
                css_class="mx-auto my-4"
            )
        )
