from django.contrib import admin
from .models import ContactSubmission

@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'reason', 'submitted_at', 'is_read']
    list_filter = ['reason', 'is_read', 'submitted_at']
    search_fields = ['name', 'email', 'message']
    readonly_fields = ['submitted_at']
    list_editable = ['is_read']
    ordering = ['-submitted_at']
    
    fieldsets = (
        ('Contact Information', {
            'fields': ('name', 'email', 'reason')
        }),
        ('Message', {
            'fields': ('message',)
        }),
        ('Admin', {
            'fields': ('submitted_at', 'is_read')
        })
    )
    
    def get_queryset(self, request):
        return super().get_queryset(request)
    
    def has_add_permission(self, request):
        return False  # Prevent adding submissions through admin
