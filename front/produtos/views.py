from django.shortcuts import render
from .forms import LoginForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']
            # Aqui você pode autenticar o usuário se quiser
            return render(request, 'produtos/login.html', {'email': email})
    else:
        form = LoginForm()
    return render(request, 'produtos/login.html', {'form': form})

