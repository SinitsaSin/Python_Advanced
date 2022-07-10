from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from accounts.forms import UserRegistrationForm


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

