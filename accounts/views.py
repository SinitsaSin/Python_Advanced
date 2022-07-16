from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from django.views.generic.edit import ProcessFormView

from accounts.forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm


class AccountRegistrationView(CreateView):
    model = User
    template_name = 'accounts/registration.html'
    success_url = reverse_lazy('index')
    form_class = UserRegistrationForm


class AccountLoginView(LoginView):
    template_name = 'accounts/login.html'

    def get_redirect_url(self):
        next_value = self.request.GET.get('next')
        if next_value:
            return next_value

        return reverse('index')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f'User <{self.request.user}> has successfully logged in.')
        return response


class AccountLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'accounts/logout.html'


class AccountUpdateView(LoginRequiredMixin, ProcessFormView):
    def get(self, request, *args, **kwargs):
        user = request.user
        profile = request.user.profile
        user_form = UserUpdateForm(instance=user)
        profile_form = ProfileUpdateForm(instance=profile)

        return render(request, 'accounts/update.html', {'user_form': user_form, 'profile_form': profile_form})

    def post(self, request, *args, **kwargs):
        user = self.request.user
        profile = user.profile
        user_form = UserUpdateForm(instance=user, data=request.POST)
        profile_form = ProfileUpdateForm(instance=profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return HttpResponseRedirect(reverse('accounts:profile_view'))

        return render(request, 'accounts/update.html', {'user_form': user_form, 'profile_form': profile_form})


@login_required
def account_view(request):
    return render(request, 'accounts/profile.html')
