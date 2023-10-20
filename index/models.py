from django.db import models

# Create your models here.
class Feedback(models.Model):
        username = models.CharField(max_length=30)
        feedback = models.TextField()
        created_on = models.DateTimeField(auto_now_add=True)
        
        def __str__(self):
                return self.username
        
        class Meta:
                verbose_name = "Feedback"
                verbose_name_plural = "Feedback"
        
class Contact_us(models.Model):
        name = models.CharField(max_length=30, null=False, blank=False)
        email = models.EmailField(max_length=50, null=False, blank=False)
        topic = models.CharField(max_length=100, null=False, blank=False)
        number = models.CharField(max_length=11, null=True, blank=True)
        message = models.TextField(null=False, blank=False)

        def __str__(self):
                return self.name
        
        class Meta:
                verbose_name = "Contact us"
                verbose_name_plural = "Contact us"

class Batch(models.Model):
        TYPE_CHOICES = (
                ("weekends","weekends"),
                ("weekdays", "weekdays")
        )
        MODE_CHOICES = (
                ("Hybrid", "Hybrid"),
                ("Online Only","Online Only"),
                ("Classroom Only", "Classroom Only")
        )
        technology = models.CharField(max_length=30)
        start_date = models.DateField(auto_now_add=False)
        type = models.CharField(max_length=20, choices=TYPE_CHOICES)
        days = models.CharField(max_length=30)
        batch_time = models.CharField(max_length=30)
        batch_mode = models.CharField(max_length=30, choices=MODE_CHOICES)

        def __str__(self):
                return self.technology
        
        class Meta:
                verbose_name = "Batch Timing"
                verbose_name_plural = "Batch Timings"

