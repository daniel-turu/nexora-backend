from django.utils.html import strip_tags
from django.conf import settings
from django.core.mail import send_mail
from django.dispatch import receiver
from django.db.models.signals import post_save
from tinymce.models import HTMLField
from django.db import models

# Create your models here.

class CurriculumOffer(models.Model):
    EDUCATION_LEVELS = [
        ('kindergarten', 'Kindergarten'),
        ('nursery', 'Nursery'),
        ('primary', 'Primary'),
        ('secondary', 'Secondary'),
        ('islamiyya', 'Islamiyya'),
        ('nexora_digital', 'Nexora Digital Academy'),
    ]
    
    name = models.CharField(max_length=255, choices=EDUCATION_LEVELS, unique=True)
    description = models.TextField(blank=True, null=True)
    subjects = models.ManyToManyField('Subject', related_name='curriculums')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return dict(self.EDUCATION_LEVELS).get(self.name, self.name)

class Subject(models.Model):
    name = models.CharField(max_length=255, unique=True)
    def __str__(self):
        return self.name



# Academic Calendar Model

class Event(models.Model):
    CHOICES = [
        ('Event', 'Event'),
        ('News', 'News'),
    ]
    title = models.CharField(max_length=200)
    type = models.CharField(max_length=10, choices=CHOICES, default='Event')
    date = models.DateField()
    description = HTMLField()
    display_picture = models.ImageField(upload_to='events/', help_text="Main image (720x400)")
    optional_image_1 = models.ImageField(upload_to='events/', blank=True, null=True)
    optional_image_2 = models.ImageField(upload_to='events/', blank=True, null=True)
    optional_image_3 = models.ImageField(upload_to='events/', blank=True, null=True)


    def __str__(self):
        return f"{self.title} - {self.date}"


class AboutPage(models.Model):

    content = HTMLField()
    
    def save(self, *args, **kwargs):
        if not self.pk:  # Only set pk to 1 for new object
            self.pk = 1
        super().save(*args, **kwargs)


    def delete(self, *args, **kwargs):
        pass  # Prevent deletion

    @classmethod
    def get_instance(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj
    def __str__(self):
        return "About-Page"
    class Meta:
        verbose_name = "About Page"
        verbose_name_plural = "About Page"  # Singular in Admin







class PrincipalWelcomeMessage(models.Model):
    message = HTMLField()
    principal_name = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='principal_pictures/')

    def save(self, *args, **kwargs):
        self.pk = 1  # Ensure only one instance exists
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass  # Prevent deletion

    @classmethod
    def get_instance(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

    def __str__(self):
        return self.principal_name

    class Meta:
        verbose_name = "Principal Welcome Message"
        verbose_name_plural = "Principal Welcome Message"  # Singular in Admin




class FooterData(models.Model):
    address = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    facebook_link = models.URLField(blank=True, null=True)
    twitter_link = models.URLField(blank=True, null=True)
    linkedin_link = models.URLField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.pk = 1  # Ensure only one instance exists
        super(FooterData, self).save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        pass  # Prevent deletion of the instance
    
    @classmethod
    def get_instance(cls):
        instance, _ = cls.objects.get_or_create(pk=1)
        return instance

    def __str__(self):
        return "Footer Data"

    class Meta:
        verbose_name = "Footer Data"
        verbose_name_plural = "Footer Data"



        
class AcademicEvent(models.Model):
    CATEGORY_CHOICES = [
        ('Exam', 'Exam'),
        ('Lecture', 'Lecture'),
        ('Holiday', 'Holiday'),
        ('Workshop', 'Workshop'),
        ('Meeting', 'Meeting'),
        ('Other', 'Other'),
    ]

    title = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='Other')
    start_datetime = models.DateTimeField()  # 🔹 Changed to DateTimeField
    end_datetime = models.DateTimeField()  # 🔹 Added DateTimeField for time-based events
    description = models.TextField(max_length=170)

    def __str__(self):
        return f"{self.title} ({self.start_datetime} - {self.end_datetime})"



# Model for Gallery Images
class GalleryImage(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='gallery/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title


class FAQ(models.Model):
    question = models.CharField(max_length=255, unique=True)
    answer = models.TextField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.question



class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email





@receiver(post_save, sender=Event)
def send_newsletter_update(sender, instance, created, **kwargs):
    """
    Sends an email update to all newsletter subscribers when a new Event is created.
    """
    if created:  # Ensures email is sent only when a new event is created
        subscribers = NewsletterSubscriber.objects.all()
        recipient_list = [subscriber.email for subscriber in subscribers]

        if recipient_list:
            # Get the full domain URL from settings
            domain = settings.DOMAIN_URL.rstrip("/")  # Ensure no trailing slash

            # Build the full image URL
            image_url = f"{domain}{instance.display_picture.url}" if instance.display_picture else "No image"

            # Convert HTML description to plain text
            description_text = strip_tags(instance.description)[:300] + "..."  # Limit to 300 chars

            # Generate event link
            event_url = f"{domain}/#EventDetail?id={instance.id}"  # Adjust based on your actual event URL pattern

            # Email Content
            subject = f"📢 Update From Nexora Academy Title: {instance.title}"
            message = f"""
            Hello,

            A new event has been added:

            📌 **Title**: {instance.title}
            📅 **Date**: {instance.date.strftime('%Y-%m-%d')}
            🏷 **Type**: {instance.type}

            📖 **Description**: {description_text}

            📷 **Image**: {image_url}

            👉 **View Full Event & Register Here**: {event_url}

            Stay tuned for more updates!

            Best,
            Your Event Team
            """

            # Send Email
            send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list)
