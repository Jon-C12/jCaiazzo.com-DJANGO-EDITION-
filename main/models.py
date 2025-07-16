from django.db import models
from django.utils import timezone

class ContactSubmission(models.Model):
    REASON_CHOICES = [
        ('general', 'General Inquiry'),
        ('collaboration', 'Collaboration'),
        ('job_opportunity', 'Job Opportunity'),
        ('freelance', 'Freelance Project'),
        ('technical', 'Technical Question'),
        ('other', 'Other'),
    ]
    
    name = models.CharField(max_length=100)
    email = models.EmailField()
    reason = models.CharField(max_length=20, choices=REASON_CHOICES)
    message = models.TextField()
    submitted_at = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-submitted_at']
    
    def __str__(self):
        return f"{self.name} - {self.get_reason_display()}"
