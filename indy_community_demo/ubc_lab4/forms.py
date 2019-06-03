from django import forms


class IssueCredentialForm(forms.Form):
    connection_id = forms.CharField(widget=forms.HiddenInput())
    first_name = forms.CharField(label='First Name', max_length=120)
    last_name = forms.CharField(label='Last Name', max_length=120)
    status = forms.CharField(label='Status', max_length=120)
    year = forms.CharField(label='Year', max_length=120)

