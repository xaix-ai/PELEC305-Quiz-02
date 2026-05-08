from django.shortcuts import render, redirect
from .forms import EventRegistrationForm

def register_event(request):
    if request.method == 'POST':
        form = EventRegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = EventRegistrationForm()

    return render(request, 'register.html', {'form': form})

def success(request):
    return render(request, 'success.html')