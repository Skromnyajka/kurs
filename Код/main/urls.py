from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.document_list, name='home'),
    path('create/', views.document_create, name='create_doc'),
    path('document/<int:pk>/', views.document_detail, name='detail_doc'),

    # Вход и выход (используем стандартные views Django)
    path('login/', LoginView.as_view(template_name='main/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]