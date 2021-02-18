from django.urls import path, re_path
from .views import CreateUser, LoginUser, RedirectLogin, DetailUser

app_name = 'users'

urlpatterns = [
    path('registro',CreateUser.as_view(), name='signup'),
    path('login/', LoginUser.as_view(), name='login'),
    re_path(r'^minha_conta/(?P<pk>\w+)/$', DetailUser.as_view(), name="minha_conta"),
    path('login/redirect',RedirectLogin.as_view(), name="login_redirect"),
]
