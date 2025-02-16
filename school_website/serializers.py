

from rest_framework import serializers
from .models import FAQ, AcademicEvent, CurriculumOffer, FooterData, GalleryImage, AboutPage, NewsletterSubscriber, PrincipalWelcomeMessage, Event, Subject
from django.conf import settings

class AboutPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutPage
        fields = ['id', 'content']


 

class PrincipalWelcomeMessageSerializer(serializers.ModelSerializer):
    picture_url = serializers.SerializerMethodField()

    class Meta:
        model = PrincipalWelcomeMessage
        fields = ['message', 'principal_name', 'picture_url']  # Replace 'picture' with 'picture_url'

    def get_picture_url(self, obj):
        if obj.picture:
            return f'{self.context["request"].scheme}://{self.context["request"].get_host()}{obj.picture.url}'
        return None



class FooterDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = FooterData
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'title', 'type', 'date', 'description', 'display_picture', 'optional_image_1', 'optional_image_2', 'optional_image_3']




class AcademicEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicEvent
        fields = ['id', 'title', 'category', 'start_datetime', 'end_datetime', 'description']

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'name']

class CurriculumOfferSerializer(serializers.ModelSerializer):
    subjects = SubjectSerializer(many=True, read_only=True)
    
    class Meta:
        model = CurriculumOffer
        fields = ['id', 'name', 'description', 'subjects', 'created_at', 'updated_at']


class GalleryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryImage
        fields = '__all__'




class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ['id', 'question', 'answer', 'created_at', 'updated_at']




class ContactFormSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    message = serializers.CharField(max_length=1000)



class NewsletterSubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsletterSubscriber
        fields = ['email']


