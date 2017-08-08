from django.contrib import admin

# Register your models here.

from posts.models import Post

class PostModelAdmin(admin.ModelAdmin):
	list_display = ["title", "timestamp", "updated"]
	list_filter = ["title", "timestamp"]
	search_fields = ["title","content"]
	class Meta:
		model = Post

admin.site.register(Post, PostModelAdmin)
