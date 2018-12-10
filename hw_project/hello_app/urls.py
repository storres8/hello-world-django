from django.urls import path, include
from . import views

urlpatterns = [
    path('hello_app/', include([
        path('', views.general, name="hello_app_general"),
        path('<int:id>/', views.detail, name="hello_app_detail"),
        path('/help/', views.help, name="hello_app_help"),
    ]))
]
