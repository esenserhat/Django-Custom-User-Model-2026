from django.urls import path
from django.contrib.auth.views import LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetCompleteView, PasswordResetConfirmView
from django.views.generic import TemplateView

from app_auth.forms import LoginForm, UserPasswordResetForm, UserSetPasswordForm
from app_auth.views import PasswordChangeView, UserProfileView,LoginView

urlpatterns = [
    path('login/', LoginView.as_view(), name="pageLogin"),
    path('logout/',LogoutView.as_view(next_page="pageLogin"), name="pageLogout"),
    
    # #! Reset email formu
    path('forgot-password/', PasswordResetView.as_view(form_class=UserPasswordResetForm,template_name = 'app_auth/app_auth02_forgot_password.html',
                                                       html_email_template_name='app_auth/app_auth03_reset_pass_email_template.html'),name='password_reset'),
    # #! Mail gönderildi mesajı
    path('forgot-password/mail-sent/',PasswordResetDoneView.as_view(template_name = "app_auth/app_auth04_success_to_mail.html"),name='password_reset_done'), 
    # #! Yeni şifre formu
    path('forgot-password/<uidb64>/<token>/',PasswordResetConfirmView.as_view(form_class=UserSetPasswordForm,template_name = "app_auth/app_auth05_new_password.html"),name='password_reset_confirm'),
    # #! Şifre değiştirildi mesajı
    path('forgot-password/complete/',PasswordResetCompleteView.as_view(template_name = "app_auth/app_auth06_new_password_done.html"),name='password_reset_complete'),

    path('account/profile/', UserProfileView.as_view(), name="profilim"),
    path('change-password/', PasswordChangeView.as_view(), name="sifre_degistir"),

]
