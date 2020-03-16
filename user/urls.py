from django.urls import path

from .views import(
    SignUpView,
    SignUpEmailCheckView,
    SignInView,
    GoogleSignInView
)

urlpatterns = [
    path('/sign-up', SignUpView.as_view()),
    path('/email-check', SignUpEmailCheckView.as_view()),
    path('/sign-in', SignInView.as_view()),
    path('/google', GoogleSignInView.as_view()),
]
