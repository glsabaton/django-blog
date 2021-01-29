from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.urls import reverse_lazy
from .forms import SignUpForm, UserEditForm, PasswordsChangeForm, CreateProfileViewForm
from django.contrib.auth.views import PasswordChangeView
from theblog.models import Profile
# Create your views here.


def password_success(request):
    return render(request, 'registration/password-success.html', {})


class CreateProfilePageView(generic.CreateView):
    model = Profile
    form_class = CreateProfileViewForm
    template_name = 'registration/create_profile_page.html'
    success_url = reverse_lazy("home")
    # to hijack the user use the function below

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_absolute_url(self):
        return reverse("home")


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordsChangeForm
    template_name = "registration/password-change.html"
    success_url = reverse_lazy("password_succes")


class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("login")


class UserEditView(generic.UpdateView):
    model = Profile
    form_class = UserEditForm
    template_name = "registration/edit_profile.html"
    success_url = reverse_lazy("home")

    def get_object(self):
        return self.request.user


class ShowProfilePageView(generic.DetailView):
    model = Profile
    template_name = "registration/user_profile.html"

    def get_context_data(self, *args, **kwargs):
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context = super(ShowProfilePageView,
                        self).get_context_data(*args, **kwargs)
        context["page_user"] = page_user
        return context


class EditProfilePageView(generic.UpdateView):
    model = Profile
    template_name = "registration/edit_profile_page.html"
    fields = ['bio', 'profile_pic', 'facebook_url', 'instagram_url', 'twitter_url'
              ]
    success_url = reverse_lazy("home")
