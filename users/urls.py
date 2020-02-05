# users/urls.py
from django.urls import path, include
from .views import SignUpView # new

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', SignUpView.as_view(), name='signup'), # new
]
