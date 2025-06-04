from blogs.models import BlogMessage
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .forms import BlogMessageForm
from django.contrib.auth.mixins import LoginRequiredMixin


class BlogListView(ListView):
    model = BlogMessage
    template_name = 'blogs/blogs_list.html'
    context_object_name = 'blogs'

    def get_queryset(self):
        return BlogMessage.objects.filter(is_published=True)


class BlogDetailView(DetailView):
    model = BlogMessage
    template_name = 'blogs/blog_detail.html'
    context_object_name = 'blog'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_counter += 1
        self.object.save()
        return self.object


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = BlogMessage
    form_class = BlogMessageForm
    template_name = 'blogs/blog_form.html'
    success_url = reverse_lazy('blogs:blogs_list')


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = BlogMessage
    form_class = BlogMessageForm
    template_name = 'blogs/blog_form.html'
    success_url = reverse_lazy('blogs:blogs_list')

    def get_success_url(self):
        return reverse('blogs:blog_detail', args=[self.kwargs.get('pk')])


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = BlogMessage
    template_name = 'blogs/blog_confirm_delete.html'
    success_url = reverse_lazy('blogs:blogs_list')
