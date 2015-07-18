from django.contrib import admin

from cms.models import Article, Tag, Category, \
    Gallery, Image


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category',
                    'creation_date', 'edit_date',
                    'publish_status',)
    list_editable = ('publish_status',)
    list_filter = ('category',
                   'creation_date',
                   'publish_status',)
    search_fields = ['author__first_name',
                     'author__last_name',
                     'author__email',
                     'author__username',
                     'title', 'content', ]

    filter_horizontal = ['tags']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Gallery)
admin.site.register(Image)
