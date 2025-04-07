from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import RegisterView, TodoListCreateView, TodoRetrieveUpdateDestroyView, VerifyTokenView

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('todo/', TodoListCreateView.as_view(), name='todo_list_create'),
    path('todo/<int:pk>/', TodoRetrieveUpdateDestroyView.as_view(), name='todo_retrieve_update_destroy'),
    path('user/', VerifyTokenView.as_view(), name='token_verify'),

]
