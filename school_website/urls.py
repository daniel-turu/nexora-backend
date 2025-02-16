from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('api/about/', views.AboutView.as_view(), name='about'),
    path('api/principal-message/', views.PrincipalWelcomeMessageView.as_view(), name='principal-message'),
    path('api/footer/', views.FooterDataAPIView.as_view(), name='footer-data'),
    path('api/events/', views.EventListView.as_view(), name='event-list'),
    path('api/events/<int:pk>/', views.EventDetailView.as_view(), name='event-detail'),
    path('api/academic-calendar/', views.AcademicCalendarView.as_view(), name='academic-calendar'),
    path('api/curriculum-offers/', views.CurriculumOfferViewSet.as_view(), name='curriculum-offer-list'),
    path('api/gallery/', views.GalleryImageView.as_view(), name='gallery-list'),
    path('api/faqs/', views.FAQListView.as_view(), name='faq-list'),
    path('api/contact/', views.ContactFormView.as_view(), name='contact-form'),
    path('api/subscribe/', views.SubscribeNewsletter.as_view(), name='subscribe-newsletter'),

    ]

