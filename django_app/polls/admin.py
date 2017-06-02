from django.contrib import admin

from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        'question_text',
        'pub_date',
        'was_published_recently',
    )
    list_filter = (
        'pub_date',
    )
    fieldsets = [
        ('Basic Information', {
            'fields': [
                'question_text'
            ]
        }),
        ('Date Information', {
            'fields': [
                'pub_date',
            ]
        })
    ]
    inlines = (ChoiceInline,)
    # fields = ('pub_date', 'question_text')


# admin.site.register(Question)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
