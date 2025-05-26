from django.urls import path
from blog.apps import BlogConfig

# from blog.views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView, ContactsView

app_name = BlogConfig.name

urlpatterns = [
    # path('products/', ProductListView.as_view(), name='products_list'),
    # path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    # path('products/create/', ProductCreateView.as_view(), name='product_create'),
    # path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    # path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    #
    # path('contacts/', ContactsView.as_view(), name='contacts'),
]
