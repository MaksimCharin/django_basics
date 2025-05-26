from django.urls import path
from blog.apps import BlogConfig

from blog.views import MessageListView, MessageDetailView, MessageCreateView, MessageUpdateView, MessageDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('messages/', MessageListView.as_view(), name='message_list'),
    path('messages/<int:pk>/', MessageDetailView.as_view(), name='message_detail'),
    path('messages/create/', MessageCreateView.as_view(), name='message_create'),
    path('messages/<int:pk>/update/', MessageUpdateView.as_view(), name='message_update'),
    path('messages/<int:pk>/delete/', MessageDeleteView.as_view(), name='message_delete'),
]
