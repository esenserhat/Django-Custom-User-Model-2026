from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

from django.contrib.auth import update_session_auth_hash, logout
from django.contrib import messages

from django.shortcuts import redirect, render
from django.core.cache import cache
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth import authenticate, login
from app_auth.forms import ChangePasswordForm
from app_auth.models import Account


class IndexView(LoginRequiredMixin,View):
    template_name = 'index.html'
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):   
        
        context = {
            'page_title': 'Home Page',
        }
        return render(request, self.template_name, context)
    
def normalize_email(email):
    turkish_map = str.maketrans("çğıöşüÇĞİÖŞÜ", "cgiosuCGIOSU")
    return email.translate(turkish_map).lower()

class LoginView(View):
    http_method_names = ['get', 'post']
    template_name = "app_auth/app_auth01_signin.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        email = normalize_email(request.POST.get("email", ""))
        password = request.POST.get("password", "")

        session_key = f'login_attempts_{request.session.session_key}_{email}'
        block_key = f'login_block_{request.session.session_key}_{email}'

        if cache.get(block_key):
            now = timezone.localtime()
            block_duration = 5  # minutes
            block_end = now + timedelta(minutes=block_duration)
            block_end_str = block_end.strftime('%H:%M')
            now_str = now.strftime('%H:%M')
            messages.error(request, f'Too many failed attempts. Please try again in {block_duration} minutes ({block_end_str}).')
            return render(request, self.template_name)

        attempts = cache.get(session_key, 0)

        try:
            user = Account.objects.get(email=email)
        except Account.DoesNotExist:
            messages.error(request, 'No user found with this email address.')
            return render(request, self.template_name)

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            cache.delete(session_key)
            print(f"\nLogin successful: {user.email}\n")
            return redirect('home')
        else:
            attempts += 1
            cache.set(session_key, attempts, timeout=5*60)
            if attempts >= 5:
                cache.set(block_key, True, timeout=5*60)
                now = timezone.localtime()
                block_duration = 5  # minutes
                block_end = now + timedelta(minutes=block_duration)
                block_end_str = block_end.strftime('%H:%M')
                now_str = now.strftime('%H:%M')
                messages.error(request, f'Too many failed attempts. Please try again in {block_duration} minutes ({block_end_str}).')
            else:
                messages.error(request, f'Login failed. Remaining attempts: {5 - attempts}')
            return render(request, self.template_name)

class UserProfileView(LoginRequiredMixin, View):
    login_url = 'pageLogin'

    def get(self, request):
        context = {
            "user": request.user
        }
        return render(request, 'app_auth/profile.html', context)
            

class PasswordChangeView(LoginRequiredMixin, View):
    login_url = 'pageLogin'

    def get(self, request):
        form = ChangePasswordForm(request.user)
        return render(request, 'app_auth/profile_password.html', context={'form': form})

    def post(self, request):
        form = ChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password has been changed successfully. Please log in again.')
            logout(request)
            return redirect('pageLogin')
        else:
            messages.error(request, 'Password change failed. Please check your information.')
        return render(request, 'app_auth/profile_password.html', context={'form': form})