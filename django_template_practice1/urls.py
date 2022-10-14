"""Django_template_practice1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, reverse_lazy #, include
from django.conf.urls import include

# from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import (LoginView, LogoutView,
    PasswordChangeView, PasswordChangeDoneView,PasswordResetView,
    PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView,
)
from django.contrib.auth import (
    REDIRECT_FIELD_NAME, get_user_model, login as auth_login,
    logout as auth_logout, update_session_auth_hash,
)
from django.views.generic.base import TemplateView
# # from book.views import homepage #1
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve
from datetime import datetime, date
from user_app.modules import views_auth
from user_app.modules import form_auth

urlpatterns = [
    path('', views_auth.index, name='index_admin'),
    # djoser endpoints: Django REST framework
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    # =============| Admin site |============
    path('admin/', admin.site.urls),
    # path('auth/', include('authentication.urls')),
    # =============| app endpoints |============
    path("user/", include("user_app.urls")),
    path("catalog/", include("catalog_app.urls")),
    path('upload/', include('upload_app.urls')),
    # path('employee/', include('employee_app.urls')),

    # =============| Transmit Admin |============
    # .........................................
    # =============| password-reset for user |============
    path('user/accounts/password-reset/', PasswordResetView.as_view(
                title = 'Lấy lại mật khẩu',
                form_class = form_auth.ResetPassToEmailForm,
                template_name = 'registration/password_reset_form_new.html',
                extra_context = {'next':'/accounts/login/', 'crumbs': [('Trang chủ', reverse_lazy('index')), ('Đăng nhập', reverse_lazy('login')), ('Lấy lại mật khẩu', reverse_lazy('password_reset'))],'year':datetime.now().year},
                success_url='done/',
        ), name="password_reset"),
    path('user/accounts/password-reset/done/', PasswordResetDoneView.as_view(
                title = 'Gửi yêu cầu thành công. Vào email để lấy lại mật khẩu',
                template_name = "registration/password_reset_done_new.html",
                extra_context = {'next':'/accounts/login/', 'crumbs': [('Trang chủ', reverse_lazy('index')), ('Đăng nhập', reverse_lazy('login')), ('Gửi yêu cầu thành công. Vào email để lấy lại mật khẩu', reverse_lazy('password_reset_done'))],'year':datetime.now().year},
        ), name="password_reset_done"),
    #path('user/accounts/reset/<uidb64>/<token>/', ctrl_auth.PassResetView.as_view(), name="password_reset_confirm"),
    #Link được send vào mail
    path('user/accounts/reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
                title = 'Đặt lại mật khẩu mới',
                form_class = form_auth.ResetPassForm,
                template_name = 'registration/password_reset_confirm_new.html',
                extra_context = {'next':'/accounts/login/', 'crumbs': [('Trang chủ', reverse_lazy('index')), ('Đăng nhập', reverse_lazy('login')), ('Đặt lại mật khẩu mới', reverse_lazy('password_reset_confirm'))],'year':datetime.now().year},
                success_url='/user/accounts/reset/done/',
        ), name="password_reset_confirm"),
    path('user/accounts/reset/done/', PasswordResetCompleteView.as_view(
                title = 'Đổi mật khẩu thành công',
                template_name = "registration/password_reset_complete_new.html",
                extra_context = {'next':'/accounts/login/', 'crumbs': [('Trang chủ', reverse_lazy('index')), ('Đăng nhập', reverse_lazy('login')), ('Đổi mật khẩu thành công', reverse_lazy('password_reset_complete'))],'year':datetime.now().year},
        ), name="password_reset_complete"),
]

# from django.conf import settings
# from django.conf.urls.static import static
# if settings.DEBUG:
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)