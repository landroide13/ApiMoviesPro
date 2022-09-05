from django.contrib import admin
from .models import Movie, CustomerProfile, Rating, CommentMovie

# Register your models here.

admin.site.site_header = "Movie Rater App Corporate"
admin.site.site_title = "Movie Go"
admin.site.index_title = "Welcome to the Movie Go Admin Area"

#admin.site.register(Movie)
admin.site.register(CustomerProfile)
admin.site.register(Rating)
admin.site.register(CommentMovie)



@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    fields = ['title', 'description']
    list_display = ['title', 'description']
    list_filter= ['title']
    search_fields = ['title']






