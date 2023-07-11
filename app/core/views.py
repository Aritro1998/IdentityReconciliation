from django.shortcuts import render
from .models import Contact
from .serializers import ContactSerializer
from rest_framework import generics

# Create your views here.
class ContactList(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class ContactDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    lookup_url_kwarg = 'pk'
