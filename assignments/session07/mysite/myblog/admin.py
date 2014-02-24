from django.contrib import admin
from myblog.models import Post, Category


class CategoryInline(admin.TabularInline):
    model = Category.posts.through


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created_date', 'modified_date', )
    list_display = ('title', 'created_date', 'modified_date', 'published_date', 'author', )
    list_display_links = ('title', )
    fields = ('title', 'created_date', 'modified_date', 'published_date', 'author')
    inlines = [CategoryInline, ]
    list_filter = ('published_date', 'author')
    search_fields = ['title', ]


class CategoryAdmin(admin.ModelAdmin):
    exclude = ('posts', )
    list_display = ('name','description', )


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)