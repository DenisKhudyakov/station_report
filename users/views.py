from django.contrib.auth.views import LoginView


class UserLogin(LoginView):
    template_name = 'users/start_page.html'
