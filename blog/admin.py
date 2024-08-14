from django.contrib import admin
from .models import Post ,Comment,Category,Like


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_public', )
    list_filter = ('is_public', )


admin.site.register(Category)
admin.site.register(Like)
admin.site.register(Comment)