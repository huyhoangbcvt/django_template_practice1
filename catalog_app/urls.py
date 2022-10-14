from django.urls import path
from .views import ListAllProfile
from .views import CreateProfile
from django.contrib.auth.views import (
    LoginView, LogoutView,
    PasswordChangeView, PasswordChangeDoneView,
    PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView,
)
from django.contrib.auth import (
    REDIRECT_FIELD_NAME, get_user_model, login as auth_login,
    logout as auth_logout, update_session_auth_hash,
)
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from .modules import views_category
from .modules import views_product
from .modules import views_catalog
# from django.views.generic import RedirectView
app_name = 'catalog'

urlpatterns = [
    path("all-catalog", ListAllProfile.as_view(), name="all-catalog"),
    path("create-catalog", CreateProfile.as_view(), name="create-catalog"),

    path('', views_catalog.CatalogView.as_view(

    ), name="catalog"),
    path('category/', views_category.list, name="view-category"),

    path('category/create/', views_category.UploadImage.as_view(), name='upload_template'),
    path('category/view/<int:pk>/', views_category.UploadImageDisplay.as_view(), name='view_upload_template_page'),

    path('product/', views_product.list, name="view-product"),
    # path('', RedirectView.as_view(url='catalog-detail/', permanent=True)),
    path('product/create/', views_product.UploadImage.as_view(), name='upload_p_template'),
    path('product/view/<int:pk>/', views_product.UploadImageDisplay.as_view(), name='view_upload_p_template_page'),

]

