from django.urls import path, re_path
from .views import CreateUser, LoginUser, RedirectLogin, detail_user

app_name = 'users'

urlpatterns = [
    path('registro',CreateUser.as_view(), name='signup'),
    path('login/', LoginUser.as_view(), name='login'),
    path('minha_conta', detail_user, name="my_account"),
    path('<int:pk>', detail_user, name="other_user_account"),
    path('login/redirect',RedirectLogin.as_view(), name="login_redirect"),
]
