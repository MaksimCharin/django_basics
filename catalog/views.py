from catalog.models import Product
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied

from .forms import ProductForm, ProductModeratorForm

from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from .services import ProductService, CategoryService

from .models import Category

class CategoryListView(ListView):
    model = Category
    template_name = 'catalog/category.html'
    context_object_name = 'categories'

    def get_queryset(self):
        return CategoryService.get_category_from_cache()


class ProductByCategoryListView(ListView):
    model = Product
    template_name = 'catalog/category_products.html'
    context_object_name = 'products'

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return ProductService.get_products_in_category(category_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = self.kwargs['category_id']
        context['category'] = Category.objects.get(pk=category_id)
        context['categories'] = Category.objects.all()
        return context


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/products_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        return ProductService.get_products_from_cache()

    # отображение списка товаров со значением is_published=True, отключил для целостного отображения
    # def get_queryset(self):
    #     return Product.objects.filter(is_published=True)


@method_decorator(cache_page(60 * 15), name='dispatch')
class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product_detail'


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:products_list')

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.creator = user
        product.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:products_list')

    def get_form_class(self):
        user = self.request.user
        if user == self.get_object().creator:
            return ProductForm
        if user.has_perm('catalog.can_unpublish_product') and user.has_perm('catalog.can_delete_product'):
            return ProductModeratorForm
        raise PermissionDenied


class ProductDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:products_list')
    permission_required = 'catalog.can_delete_product'


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'
