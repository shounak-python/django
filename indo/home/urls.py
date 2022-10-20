from django.urls import path
from . import views

app_name = "home"
urlpatterns = [
    path("", views.HomeView.as_view(), name="homepage"),
    path("about", views.AboutView.as_view(), name="about"),
    path("tutorial", views.TutorialView.as_view(), name="tutorial"),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name="logout"),
]
