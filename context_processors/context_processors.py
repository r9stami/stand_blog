from blog.models import Category, Post


def categories(request):
    categories = Category.objects.all()
    return {'categories': categories}


def recent_post(request):
    posts = Post.objects.all()
    return {'recent_post': posts}