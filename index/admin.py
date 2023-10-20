from django.contrib import admin
from .models import Feedback, Contact_us, Batch

# Register your models here.
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('username', 'feedback', 'created_on')

class Contact_usAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'number', 'topic', 'message')

class BatchAdmin(admin.ModelAdmin):
    list_display = ('technology', 'start_date', 'type', 'days', 'batch_time', 'batch_mode')

admin.site.register(Batch, BatchAdmin)
admin.site.register(Contact_us, Contact_usAdmin)
admin.site.register(Feedback, FeedbackAdmin)