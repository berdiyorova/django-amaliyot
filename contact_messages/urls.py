from django.urls import path

from .views import ContactView, ContactListView


urlpatterns = [
    path('', ContactView.as_view(), name='contact'),
    path('messages/', ContactListView.as_view(), name='messages')
]
