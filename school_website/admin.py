from django.contrib import admin
from .models import FAQ, AcademicEvent, FooterData, GalleryImage, NewsletterSubscriber, PrincipalWelcomeMessage, CurriculumOffer, Subject, Event, AboutPage

# Register your models here.

admin.site.register(CurriculumOffer)
admin.site.register(Subject)
admin.site.register(Event)
admin.site.register(AboutPage)
admin.site.register(PrincipalWelcomeMessage)
admin.site.register(FooterData)
admin.site.register(AcademicEvent)
admin.site.register(GalleryImage)
admin.site.register(FAQ)
admin.site.register(NewsletterSubscriber)