from django.conf import settings
from django.core.mail import send_mail
from django.db.models import Q
from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView
from django.utils.dateparse import parse_date
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import AboutPageSerializer, AcademicEventSerializer, ContactFormSerializer, CurriculumOfferSerializer, EventSerializer, FAQSerializer, FooterDataSerializer, GalleryImageSerializer, NewsletterSubscriberSerializer, PrincipalWelcomeMessageSerializer
from .models import FAQ, AcademicEvent, CurriculumOffer, FooterData, GalleryImage, AboutPage, PrincipalWelcomeMessage, Event



# Create your views here.


def home(request):
    return render(request, 'home.html')

class AboutView(APIView):
    def get(self, request):
        about = AboutPage.get_instance()
        serializer = AboutPageSerializer(about)
        return Response(serializer.data)


class PrincipalWelcomeMessageView(APIView):
    def get(self, request):
        instance = PrincipalWelcomeMessage.get_instance()
        serializer = PrincipalWelcomeMessageSerializer(instance, context={'request': request})
        return Response(serializer.data)



class FooterDataAPIView(APIView):
    def get(self, request):
        footer_data = FooterData.get_instance()
        serializer = FooterDataSerializer(footer_data)
        return Response(serializer.data)
    

class EventListView(ListAPIView):
    queryset = Event.objects.all().order_by('-id')
    serializer_class = EventSerializer

# Get a single event by ID
class EventDetailView(RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer



class AcademicCalendarView(ListAPIView):
    serializer_class = AcademicEventSerializer

    def get_queryset(self):
        month = self.request.query_params.get('month', None)  # Expected format: "YYYY-MM"

        if month:
            try:
                month_date = parse_date(f"{month}-01")  # Convert "YYYY-MM" to date object
                return AcademicEvent.objects.filter(
                    Q(start_datetime__year=month_date.year, start_datetime__month=month_date.month) |  # Starts in this month
                    Q(end_datetime__year=month_date.year, end_datetime__month=month_date.month)       # Ends in this month
                )
            except ValueError:
                return AcademicEvent.objects.none()

        return AcademicEvent.objects.all()



class CurriculumOfferViewSet(ListAPIView):
    queryset = CurriculumOffer.objects.all()
    serializer_class = CurriculumOfferSerializer


class GalleryImageView(ListAPIView):
    queryset = GalleryImage.objects.all().order_by('-uploaded_at')
    serializer_class = GalleryImageSerializer



class FAQListView(ListAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer



class ContactFormView(APIView):
    def post(self, request):
        serializer = ContactFormSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data["name"]
            email = serializer.validated_data["email"]
            message = serializer.validated_data["message"]

            subject = f"New Contact Form Submission from {name}"
            body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

            send_mail(
                subject, 
                body, 
                settings.EMAIL_HOST_USER,  # Fetch sender email from settings
                [settings.EMAIL_HOST_USER]  # Send email to the admin
            )

            return Response({"success": "Message sent successfully!"}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





class SubscribeNewsletter(APIView):
    def post(self, request):
        serializer = NewsletterSubscriberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Subscription successful!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)