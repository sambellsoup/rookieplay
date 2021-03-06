from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def login(request):
    return render(reques, 'users/login.html')

@login_required
def account(request):
    context = {
        'account_page': "active",
    }
    return render(request, 'users/account.html', context)

def register(request):
    """Register a new user."""
    if request.method != 'POST':
        #Display blank registration form.
        form = UserCreationForm()
    else:
        # Process completed form.
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Log the user in and then redirect to home page.
            authenticated_user = authenticate(username=new_user.username,
                password = request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('recs:index'))

    context = {'form': form}
    return render(request, 'users/register.html', context)
