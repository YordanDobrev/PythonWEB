from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView
from Artonia_v2.accounts.forms import CustomUserCreationForm, UserUpdateForm

UserModel = get_user_model()


class UserRegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('home')


class UserDetailsView(DetailView):
    model = UserModel
    template_name = 'registration/details-account.html'
    context_object_name = 'user'

    def get_object(self, queryset=None):
        return self.request.user


class UserUpdateView(UpdateView):
    model = UserModel
    form_class = UserUpdateForm
    template_name = 'registration/edit-account.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return self.request.user
