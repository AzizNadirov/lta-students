from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import ProfileUpdateForm
from .models import Profile


@login_required
def edit_profile_view(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES,  instance = request.user)

        if form.is_valid():
            form.save()
            messages.success(request, f'Dəyişiklik uğurla tamamlandı.')
            return redirect('profile')

    else:
        form = ProfileUpdateForm(instance = request.user)

    context = {'form':form}
    return render(request, 'students/edit_profile.html', context)
