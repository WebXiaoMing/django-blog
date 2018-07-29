import xadmin
from .models import Tags, Categories, Years, Detail, Blogs
from users.models import UserProfile


class TagsAdmin(object):
    list_display = ['tag_name', 'count', 'add_time']
    search_fields = ['tag_name', 'count']
    list_filter = ['tag_name', 'count', 'add_time']

    def save_models(self):
        obj = self.new_obj
        obj.save()
        user = UserProfile.objects.get(username='ming_admin')
        user.tags_counts = user.tags_counts + 1
        user.save()


class CategoriesAdmin(object):
    list_display = ['name', 'count', 'add_time']
    search_fields = ['name', 'count']
    list_filter = ['name', 'count', 'add_time']

    def save_models(self):
        obj = self.new_obj
        obj.save()
        user = UserProfile.objects.get(username='ming_admin')
        user.categories_counts = user.categories_counts + 1
        user.save()


class YearsAdmin(object):
    list_display = ['name', 'count', 'add_time']
    search_fields = ['name', 'count']
    list_filter = ['name', 'count', 'add_time']


class DetailAdmin(object):
    list_display = ['blog', 'add_time']
    search_fields = ['blog']
    list_filter = ['blog', 'add_time']


class BlogInline(object):
    model = Detail
    extra = 0


class BlogsAdmin(object):
    list_display = ['title', 'categories', 'year', 'tags', 'add_time']
    search_fields = ['title', 'categories', 'year', 'tags']
    list_filter = ['title', 'categories', 'year', 'tags', 'add_time']
    inlines = [BlogInline]

    def save_models(self):
        obj = self.new_obj
        obj.save()
        user = UserProfile.objects.get(username='ming_admin')
        user.archives_counts = user.archives_counts + 1
        user.save()

        if obj.categories is not None and obj.year is not None:
            categories = obj.categories
            year = obj.year
            categories.count = Categories.objects.filter(name=categories).count()
            year.count = Years.objects.filter(name=year).count()
            categories.save()
            year.save()


xadmin.site.register(Tags, TagsAdmin)
xadmin.site.register(Categories, CategoriesAdmin)
xadmin.site.register(Years, YearsAdmin)
xadmin.site.register(Detail, DetailAdmin)
xadmin.site.register(Blogs, BlogsAdmin)
