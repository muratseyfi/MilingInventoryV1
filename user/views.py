from django.shortcuts import render, redirect
from .forms import CreateUserForm

def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-index')
    else:
        form = CreateUserForm()
    context = {
        'form': form,

    }
    return render(request, 'user/register.html', context)
