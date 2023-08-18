from django.contrib import admin
from .models import Note, Tag

class NoteAdmin(admin.ModelAdmin):
    pass

class TagAdmin(admin.ModelAdmin):
    pass

admin.site.register(Note, NoteAdmin)
admin.site.register(Tag, TagAdmin)