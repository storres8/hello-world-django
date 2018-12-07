from django.urls import path, include
from . import views

urlpatterns = [
    path('common/', include([
        path('', views.general, name="hello_app_general"),
        path('<int:id>/', views.detail, name="hello_app_detail"),
    ]))
]
