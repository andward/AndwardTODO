from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.views import logout_then_login


class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


def getRegister(request):
    form = UserCreateForm()
    return render_to_response("register.html", {
        'form': form
    })


def postRegister(request):
    form = UserCreateForm(request.POST)
    if form.is_valid():
        new_user = form.save()
        return HttpResponseRedirect("/feedback/tag/ALL")
    else:
        return HttpResponseRedirect("/accounts/signup/")


def logout(request):
    return logout_then_login(request, login_url='/accounts/login')
