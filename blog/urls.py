from django.urls import path
from blog.apps import BlogConfig

from blog.views import MessageListView, MessageDetailView

app_name = BlogConfig.name

urlpatterns = [
    path('messages/', MessageListView.as_view(), name='message_list'),
    path('messages/<int:pk>/', MessageDetailView.as_view(), name='message_detail'),
    # path('products/create/', ProductCreateView.as_view(), name='product_create'),
    # path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    # path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    #
    # path('contacts/', ContactsView.as_view(), name='contacts'),
]
