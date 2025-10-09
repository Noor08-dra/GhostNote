from django.urls import path
from . import views


urlpatterns=[
    path('',views.home,name="home-page"),
    path("messages/add/",views.MessageCreateView.as_view(),name="message_create_form"),
    path("messages/",views.MessageListView.as_view(),name="message_list"),
    path("messages/<int:pk>/delete/",views.MessageDeleteView.as_view(),name="delete_msg"),
    path("messages/<int:pk>/edit/",views.MessageEditView.as_view(),name="message_edit")
]