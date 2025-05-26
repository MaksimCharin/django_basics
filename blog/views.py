from blog.models import BlogMessage
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class MessageListView(ListView):
    model = BlogMessage
    template_name = 'blog/message_list.html'
    context_object_name = 'messages'


class MessageDetailView(DetailView):
    model = BlogMessage
    template_name = 'blog/message_detail.html'
    context_object_name = 'message'


class MessageCreateView(CreateView):
    model = BlogMessage
    fields = ['title', 'description', 'preview']
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:products_list')


# class ProductUpdateView(UpdateView):
#     model = BlogMessage
#     fields = ['name', 'description', 'image', 'category', 'price']
#     template_name = 'catalog/product_form.html'
#     success_url = reverse_lazy('catalog:products_list')
#
#
# class ProductDeleteView(DeleteView):
#     model = BlogMessage
#     template_name = 'catalog/product_confirm_delete.html'
#     success_url = reverse_lazy('catalog:products_list')