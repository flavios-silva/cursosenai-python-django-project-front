from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'placeholder': 'Digite seu e-mail'}))
    senha = forms.CharField(label='Senha', widget=forms.PasswordInput(attrs={'placeholder': 'Digite sua senha'}))

class RetornoForm(forms.Form):
    mensagem = forms.CharField(
        label='',
        initial='E-mail válido',
        widget=forms.HiddenInput()
    )
    bem_vindo = forms.CharField(
        label='',
        initial='Seja bem-vindo',
        widget=forms.HiddenInput()
    )