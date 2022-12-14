from django.urls import path
from .views import ListAllProfile
from .views import CreateProfile
from django.contrib.auth.views import (
    LoginView, LogoutView,
    PasswordChangeView, PasswordChangeDoneView,
    PasswordResetView, PasswordResetDoneView,
    PasswordResetConfirmView, PasswordResetCompleteView,
)
from django.contrib.auth import (
    REDIRECT_FIELD_NAME, get_user_model, login as auth_login,
    logout as auth_logout, update_session_auth_hash,
)
from datetime import datetime, date

from django.urls import reverse_lazy
from django.contrib import admin
from django.contrib.auth import views as auth_views
from .modules import form_auth
from .modules import views_auth
app_name = 'user'

urlpatterns = [
    # APIs: Django REST framework
    path("all-accounts", ListAllProfile.as_view(), name="all-accounts"),
    path("create-account", CreateProfile.as_view(), name="create-account"),

    # =============| Admin site |============
    # path('', admin.site.urls),
    path('', views_auth.index, name='index'),
    path('home/', views_auth.Homepage.as_view(), name='home'),
    path('accounts/', views_auth.AuthView.as_view(), name="accounts"),
    # Login form
    # path('accounts/login/', views_auth.loginUser.as_view(), name="login"),
    path('accounts/login/', views_auth.LoginView.as_view(), name="login"),
    path('accounts/login-social/', views_auth.LoginSocialView.as_view(), name="login_social"),

    path('accounts/logout/', auth_views.LogoutView.as_view(
            #template_name="registration/logged_out.html",
            next_page=reverse_lazy('user:login'), #next_page='/',
        ), name='logout'),
    path('accounts/sign-up/', views_auth.RegistrationUser.as_view(), name='sign_up'), #path('sign_up/', MySignUpView.as_view(), name='sign_up'),

    # =============| Profile |============
    path('profile/', views_auth.ProfileView.as_view(), name='profile'),
    path('profile/edit/', views_auth.EditUserProfileView.as_view(), name='profile_edit'),
    path('profile/<int:gu_id>/edit/', views_auth.edit_profile_pk, name='profile_edit_pk'),

    # =============| Inside: password-reset for user |============
    path('accounts/password-change/', PasswordChangeView.as_view(
                title = 'Thay ?????i m???t kh???u',
                form_class = form_auth.PassChangeForm, template_name = 'registration/password_change_form_accounts.html',
                extra_context = {'next': reverse_lazy('user:password_change_done'), 'crumbs': [('Trang ch???', reverse_lazy('user:home')), ('Th??ng tin c?? nh??n', reverse_lazy('user:profile')), ('Thay ?????i m???t kh???u', reverse_lazy('user:password_change'))],'year':datetime.now().year},
                success_url='done/',
        ), name="password_change"),
    path('accounts/password-change/done/', PasswordChangeDoneView.as_view(
                title = 'Thay ?????i m???t kh???u th??nh c??ng',
                extra_context = {'next': reverse_lazy('user:profile'), 'crumbs': [('Trang ch???', reverse_lazy('home')), ('Th??ng tin c?? nh??n', reverse_lazy('user:profile')), ('Thay ?????i m???t kh???u', reverse_lazy('user:password_change')), ('Thay ?????i m???t kh???u th??nh c??ng', reverse_lazy('user:password_change_done'))],'year':datetime.now().year},
        ), name="password_change_done"),

    # =============| Outside: password-reset for user |============
    # path('accounts/password-reset/', PasswordResetView.as_view(
    #             title = 'L???y l???i m???t kh???u',
    #             form_class = form_auth.ResetPassToEmailForm,
    #             template_name = 'registration/password_reset_form_new.html',
    #             # extra_context={'next': '/accounts/login/',
    #             #        'crumbs': [('Trang ch???', reverse_lazy('user:index')), ('????ng nh???p', reverse_lazy('user:login')),
    #             #                   ('L???y l???i m???t kh???u', reverse_lazy('user:password_reset'))],
    #             #        'year': datetime.now().year},
    #             success_url = reverse_lazy("user:password_reset_done")
    #             # success_url='done/',
    #     ), name="password_reset"),
    # path('accounts/password-reset/done/', PasswordResetDoneView.as_view(
    #             title = 'G???i y??u c???u th??nh c??ng. V??o email ????? l???y l???i m???t kh???u',
    #             template_name = 'registration/password_reset_done_new.html',
    #             # extra_context = {'next':'/accounts/login/', 'crumbs': [('Trang ch???', reverse_lazy('user:index')), ('????ng nh???p', reverse_lazy('user:login')), ('G???i y??u c???u th??nh c??ng. V??o email ????? l???y l???i m???t kh???u', reverse_lazy('user:password_reset_done'))],'year':datetime.now().year},
    #     ), name="password_reset_done"),
    # # path('accounts/reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    # #Link ???????c send v??o mail
    # path('accounts/reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
    #             title = '?????t l???i m???t kh???u m???i',
    #             form_class = form_auth.ResetPassForm, template_name = 'registration/password_reset_form_new.html',
    #             extra_context = {'next':'/accounts/login/', 'crumbs': [('Trang ch???', reverse_lazy('user:index')), ('????ng nh???p', reverse_lazy('user:login')), ('?????t l???i m???t kh???u m???i', reverse_lazy('user:password_reset_confirm'))],'year':datetime.now().year},
    #             success_url = reverse_lazy("user:password_reset_complete")
    #             # success_url='/accounts/reset/done/',
    #     ), name="password_reset_confirm"),
    # path('accounts/reset/done/', PasswordResetCompleteView.as_view(
    #             title = '?????i m???t kh???u th??nh c??ng',
    #             extra_context = {'next':'/accounts/login/', 'crumbs': [('Trang ch???', reverse_lazy('user:index')), ('????ng nh???p', reverse_lazy('user:login')), ('?????i m???t kh???u th??nh c??ng', reverse_lazy('user:password_reset_complete'))],'year':datetime.now().year},
    #     ), name="password_reset_complete"),

]

