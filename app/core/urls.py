from django.urls import path, include
from . import views

urlpatterns = [
    path('contacts/', views.ContactList.as_view(), name='contacts'),
    path('contacts/<int:pk>', views.ContactDetail.as_view(), name='details')
]