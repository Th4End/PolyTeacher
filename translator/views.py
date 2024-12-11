from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Translation
from .serializers import TranslationSerializer
import requests
from django.http import HttpResponse
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
import os

class TranslationAPIView(APIView):
    @swagger_auto_schema(
        operation_description="Récupérer toutes les traductions disponibles.",
        responses={200: TranslationSerializer(many=True)}
    )
    def get(self, request):
        translations = Translation.objects.all()
        serializer = TranslationSerializer(translations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Effectuer la traduction d'un texte.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'source_text': openapi.Schema(type=openapi.TYPE_STRING, description="Texte à traduire"),
                'source_language': openapi.Schema(type=openapi.TYPE_STRING, description="Langue source (ex: en)"),
                'target_language': openapi.Schema(type=openapi.TYPE_STRING, description="Langue cible (ex: fr)"),
            },
            required=['source_text', 'source_language', 'target_language']
        ),
        responses={
            201: TranslationSerializer,
            400: openapi.Response(description="Paramètres manquants"),
            500: openapi.Response(description="Erreur interne du serveur")
        }
    )
    def post(self, request):
        # Récupération des données depuis le JSON dans le corps de la requête
        source_text = request.data.get('source_text')
        source_language = request.data.get('source_language')
        target_language = request.data.get('target_language')

        if not source_text or not source_language or not target_language:
            return Response(
                {"error": "Missing required parameters"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Vérification si la traduction existe déjà
        existing_translation = Translation.objects.filter(
            source_text=source_text,
            source_language=source_language,
            target_language=target_language
        ).first()

        if existing_translation:
            serializer = TranslationSerializer(existing_translation)
            return Response(serializer.data, status=status.HTTP_200_OK)

        try:
            # Génération du prompt directement à partir des données du JSON
            prompt = f"Translate this text {source_language} to {target_language} without formatting : {source_text}"
            translated_text = self.get_translation_from_gemini(prompt)
        except Exception as e:
            return Response(
                {"error": f"Translation failed: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        # Sauvegarde de la traduction
        translation = Translation.objects.create(
            source_text=source_text,
            source_language=source_language,
            target_language=target_language,
            target_text=translated_text
        )

        serializer = TranslationSerializer(translation)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get_translation_from_gemini(self, prompt):
        
        token = os.environ.get('GOOGLE_API_KEY')
        url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key="+ token 
        data = {
            "contents": [{
                "parts":[{
                    "text": prompt
                }]
            }]
        }

        response = requests.post(url, json=data)
        # print(response.json())
        # raise Exception(f"Gemini API translation failed: {response.status_code} - {response.text}")
        if response.status_code == 200:
            parts = response.json()["candidates"][0]["content"]["parts"]
            text = ""
            for partie in parts:
                text =  text + partie["text"] 
        
            return text.strip()
        else:
            raise Exception(f"Gemini API translation failed: {response.status_code} - {response.text}")
