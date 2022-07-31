from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':"Write your name"}
    ), min_length=3, max_length=100)
    
    email = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={'class':'form-control', 'placeholder':"Write your mail"}
    ),min_length=3, max_length=100)
    
    content = forms.CharField(required=True, widget=forms.Textarea(
        attrs={'class':'form-control', 'rows':3, 'placeholder':"Write your message"}
    ),min_length=10, max_length=1000)

    phone_number = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':"Write your phone number"}
    ), min_length=3, max_length=100)
