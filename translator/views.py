from django.shortcuts import render
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from translator.models import Translation
# from translator.serializers import TranslationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Translation
from .serializers import TranslationSerializer
from sandbox.gemini import translate
from django.http import HttpResponse
def documentation_view(request):
    doc = """
    <h1>API Documentation - Redhoc</h1>
    <p><strong>Endpoint:</strong> /api/translations/</p>
    <h3>GET</h3>
    <p>Affiche toutes les traductions.</p>
    <h3>POST</h3>
    <p>Paramètres requis :</p>
    <ul>
        <li>source_text: Texte à traduire</li>
        <li>source_language: Langue source (ex: en)</li>
        <li>target_language: Langue cible (ex: fr)</li>
    </ul>
    <p>Retourne la traduction créée.</p>
    """
    return HttpResponse(doc)


class TranslationAPIView(APIView):
    def get(self, request):
        translation = Translation.objects.all()
        serializer = TranslationSerializer(translation, many=True)
        return Response(serializer.data, status= status.HTTP_200_OK)
    
    def post(self, request):
        source_text = request.data.get('source_text')
        source_language = request.data.get('source_language')
        target_language = request.data.get('target_language')

        if not source_text or not source_language or not target_language:
            return Response(
                {"error": "Missing required parameters"},
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            prompt = f"Translate the following text from {source_language} to {target_language}: {source_text}"
            tranlated_text = translate(prompt)
        except Exception as e:
            return Response(
                {"error": f"Translation failed : {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        translation = Translation.objects.create(
            source_text=source_text,
            source_language=source_language,
            target_language=target_language,
            tranlated_text=tranlated_text,
        )
        serializer = TranslationSerializer(translation)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# Create your views here.



class FrenchSpanishTranslationViewSet(APIView):

    def get(self, request):
        return Response(data={}, status=None)
    
    def post(self, request):
        return Response(data={}, status=None)
    
    def put(self, request, pk):
        return Response(data={}, status=None)
    
    def delete(self, request, pk):
        return Response(data={}, status=None)
    
class FrenchEnglishTranslationViewSet(APIView):

    def get(self, request):
        return Response(data={}, status=None)
    
    def post(self, request):
        return Response(data={}, status=None)
    
    def put(self, request, pk):
        return Response(data={}, status=None)
    
    def delete(self, request, pk):
        return Response(data={}, status=None)

class DeutshtoFrench(APIView):
    def get(self, request):
        return Response(data={}, status=None)
    
    def post(self, request):
        return Response(data={}, status=None)
    def put(self, request, pk):
        return Response(data={}, status=None)
    
    def delete(self, request, pk):
        return Response(data={}, status=None)

class ArameentoFrench(APIView):
    def get(self, request):
        return Response(data={}, status=None)
    
    def post(self, request):
        return Response(data={}, status=None)
    def put(self, request, pk):
        return Response(data={}, status=None)
    
    def delete(self, request, pk):
        return Response(data={}, status=None)



class Alltranslaition(APIView):
    def get(self, request):
        data = Translation.objects.all()
        serialized_data = TranslationSerializer(data, many=True)
        return Response(data=serialized_data.data, status=None)

def index(request):
    return render(request, 'index.html', context={})

    return render(request, 'contact.html', context={})