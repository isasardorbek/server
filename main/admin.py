from django.contrib import admin

from .models import Note

# admin.site.register(Note)

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    search_fields = ['title', 'body', ]
    list_filter = ['created', 'updated']
    list_display = [ 'title', 'body','is_done']
    list_display_links = ['title']
    list_editable = ['body','is_done']
    list_per_page = 10
    ordering = ['-created']
    save_on_top = True  
