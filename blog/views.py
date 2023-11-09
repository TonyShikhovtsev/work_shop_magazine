from django.urls import reverse_lazy, reverse
from django.utils.text import slugify
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blog.models import BlogPost


class BlogListView(ListView):
    model = BlogPost


class BlogCreateView(CreateView):
    model = BlogPost
    fields = ('name', 'description', 'is_published')
    success_url = reverse_lazy('blog:blog_list')

    def form_valid(self, form):
        new_post = form.save(commit=False)
        new_post.slug = slugify(new_post.name)
        new_post.save()
        return super().form_valid(form)


class BlogDetailView(DetailView):
    model = BlogPost

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1  # Увеличение счетчика просмотров
        self.object.save()
        return self.object


class BlogUpdateView(UpdateView):
    model = BlogPost
    fields = ('name', 'description', 'is_published')
    success_url = reverse_lazy('blog:blog_list')

    def form_valid(self, form):
        new_post = form.save(commit=False)
        new_post.slug = slugify(new_post.name)
        new_post.save()
        return super().form_valid(form)

class BlogListView(ListView):
    model = BlogPost

    def get_queryset(self):
        return BlogPost.objects.filter(is_published=True)


class BlogDeleteView(DeleteView):
    model = BlogPost
    success_url = reverse_lazy('blog:blog_list')
