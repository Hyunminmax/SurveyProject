from django.shortcuts import render, redirect
from django.urls.base import reverse

from a_users.forms import CustomUserForm


def user_view(request):
    form = CustomUserForm()
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            request.session['user_id'] = user.id
            return redirect(reverse('survey_view', args=(1,)))
        else:
            print(form.errors)
    return render(request, 'userInfo.html', {'form': form})
