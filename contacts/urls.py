from django.urls import path
from contacts.views import ContactListView, ContactDetailView

urlpatterns = [
    path('', ContactListView.as_view()),
    path('<int:id>', ContactDetailView.as_view()),
]
