from django import forms
from .models import message

class MessageForm(forms.ModelForm): 
     class Meta:
          model=message
          fields=['recipient_name','msg_text']
          widgets={
               'recipient_name':forms.TextInput(attrs={'class':'form-control shadow-sm border-0','placeholder':"Recipient's name"}),
               'msg_text':forms.Textarea(attrs={'class':'message-area form-control shadow-sm','placeholder':'Your thoughts, unfiltered...','rows':5,'maxlength':240}),
}

