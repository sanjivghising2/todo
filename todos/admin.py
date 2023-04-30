
from django.contrib import admin

from .models import Todos, Notes

admin.site.site_header = "Todos Admin"
admin.site.site_title = "Todos Admin Area"
admin.site.index_title = "Welcome to the Todos admin area"


class ChoiceInline(admin.TabularInline):
    model = Notes
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['todo_text']}),
                 ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}), ]
    inlines = [ChoiceInline]


# admin.site.register(Question)
# admin.site.register(Choice)
admin.site.register(Todos, QuestionAdmin)