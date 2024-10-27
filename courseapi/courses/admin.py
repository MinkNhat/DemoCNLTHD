from django.contrib import admin
from django.utils.html import mark_safe
from courses.models import Category, Course, Lesson


class LessonAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject', 'activate', 'course', 'created_date']
    list_filter = ['id', 'subject', 'created_date']
    search_fields = ['subject']
    readonly_fields = ['avatar']

    def avatar(self, lesson):
        return mark_safe(f"<img src='/static/{lesson.image.name}' width='120'/>")

    class Media:
        css = {
            'all': ('/static/css/style.css', )
        }
        js = ('static/js/script.js', )

admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Lesson, LessonAdmin)
