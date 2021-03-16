from django.urls import path, re_path
from .views import CreateUser, LoginUser, RedirectLogin, DetailUser,UserEditView,PasswordsChangeView
from django.contrib.auth import views as auth_views
app_name = 'users'

urlpatterns = [
    path('registro',CreateUser.as_view(), name='signup'),
    path('login/', LoginUser.as_view(), name='login'),
    re_path(r'^minha_conta/(?P<pk>\w+)/$', DetailUser.as_view(), name="minha_conta"),
    path('login/redirect',RedirectLogin.as_view(), name="login_redirect"),
    path('edit_profile',UserEditView.as_view(), name='edit_profile'),
     path('password/', PasswordsChangeView.as_view(),name="change_pass"),

]
