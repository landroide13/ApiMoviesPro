from django.contrib import admin
from .models import Movie, CustomerProfile

# Register your models here.

admin.site.site_header = "Movie Rater App Corporate"
admin.site.site_title = "Movie Go"
admin.site.index_title = "Welcome to the Movie Go Admin Area"

#admin.site.register(Movie)
admin.site.register(CustomerProfile)

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    fields = ['title', 'description']
    list_display = ['title', 'description']
    list_filter= ['title']
    search_fields = ['title']






