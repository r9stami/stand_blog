from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render ,redirect
from django.views import View
from django.views.generic import DetailView , ListView
from .models import Post, Category, Comment, Like
from django.contrib.auth.mixins import LoginRequiredMixin


class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetailView,self).get_context_data(**kwargs)
        if self.request.user.likes.filter(user_id=self.request.user.id,post__slug=self.object.slug):
            context['is_like'] = True
        else:
            context['is_like'] = False

        return context


class CommentCreateView(LoginRequiredMixin,View):
    def post(self,request,slug):
        post = Post.objects.get(slug=slug)
        full_name, email, comment,parent_id = self.request.POST.get('full_name'),  self.request.POST.get('email'),  self.request.POST.get('comment'),self.request.POST.get('parent_id')
        print(full_name, email, comment , parent_id)
        if full_name and email and comment:
            Comment.objects.create(full_name=full_name, email=email, comment=comment, user=self.request.user, post=post,parent_id=parent_id)
            return redirect('blog:post_detail',slug=slug)


class LikePostView(View):
    def get(self,request,slug,pk):
        try:
            like = Like.objects.get(user_id=request.user.id,post__slug=slug)
            like.delete()
            return JsonResponse({'response':'unlike'})

        except:
            Like.objects.create(user_id=request.user.id,post_id=pk)
            return JsonResponse({'response':'like'})


class PostListView(View):
    def get(self,request):
        queryset = Post.objects.filter(is_public=True)
        page = request.GET.get('page')
        paginator = Paginator(queryset, 2)
        object_list = paginator.get_page(page)
        return render(request,'blog/post_list.html',{'object_list':object_list})


class SearchPostView(View):
    def get(self,request):
        q = request.GET.get('q')
        queryset = Post.objects.filter(Q(title__icontains=q) | Q(description__icontains=q))
        page = request.GET.get('page')
        paginator = Paginator(queryset, 2)
        object_list = paginator.get_page(page)
        return render(request,'blog/post_list.html',{'object_list':object_list})


class CategoryDetailView(View):
    def get(self,request,id):
        instance = Category.objects.get(id=id)
        object_list = instance.posts.filter(is_public=True)
        return render(request,'blog/post_list.html',{'object_list':object_list})