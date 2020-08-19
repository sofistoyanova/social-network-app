from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout, update_session_auth_hash
from .forms import SigninForm, SignupForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect
# import django_rq
# from .messaging import email_message


def signin(request):
    form = SigninForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('posts_app:post-list')

    context = {
        'title': 'Signin',
        'form': form
    }
    return render(request, 'user_form.html', context)

def signup(request):
    form = SignupForm(request.POST or None)
    context = {
        'title': 'Sign up today',
        'form': form
    }

    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        # django_rq.enqueue(email_message, {
        #     'email': user.email
        # })
        return redirect('users_app:signin')

    return render(request, 'user_form.html', context)

def signout(request):
    logout(request)
    return HttpResponseRedirect(reverse('users_app:signin'))

@login_required(login_url='/auth/signin/')
def change_password(request):
    context = {}
    print(request.user)

    if request.method == "POST":
        old_password = request.POST['old_password']
        new_password1 = request.POST['new_password1']
        new_password2 = request.POST['new_password2']
        user = get_object_or_404(User, username=request.user.username)
        if user.check_password(old_password):
            if new_password1 == new_password2:
                user.set_password(new_password1)
                user.save()
                context = {'message': 'Password updated successfully '}
                update_session_auth_hash(request, user)
            else:
                context = {'message': 'Passwords did not match'}
        else:
            context = {'message': 'old password is incorrect'}

    return render(request, 'profile_settings.html', context)
