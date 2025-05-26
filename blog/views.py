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

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_counter += 1
        self.object.save()
        return self.object


class MessageCreateView(CreateView):
    model = BlogMessage
    fields = ['title', 'description', 'preview']
    template_name = 'blog/message_form.html'
    success_url = reverse_lazy('blog:message_list')


class MessageUpdateView(UpdateView):
    model = BlogMessage
    fields = ['title', 'description', 'preview']
    template_name = 'blog/message_form.html'
    success_url = reverse_lazy('blog:message_list')


class MessageDeleteView(DeleteView):
    model = BlogMessage
    template_name = 'blog/message_confirm_delete.html'
    success_url = reverse_lazy('blog:message_list')