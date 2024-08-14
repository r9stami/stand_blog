from django.shortcuts import render
from django.views.generic import TemplateView
from blog.models import Post


class HomePageView(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView ,self).get_context_data(**kwargs)
        context['object_list'] = Post.objects.filter(is_public=True).order_by('-updated_at','-created_at')[:2]

        return context