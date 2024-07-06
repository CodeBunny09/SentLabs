from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import TextData
from .serializers import TextDataSerializer
from .summarizer import generate_summary, generate_wordcloud, analyze_sentiment

class TextDataListCreateView(APIView):
    def get(self, request, *args, **kwargs):
        texts = TextData.objects.all()
        serializer = TextDataSerializer(texts, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        data = request.data.get('text')
        if not data:
            return Response({'error': 'Text data is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        summary, summary_length = generate_summary(data)
        wordcloud_url = generate_wordcloud(data)
        sentiment_analysis = analyze_sentiment(data)

        text_data = TextData.objects.create(
            original_text=data,
            summary_text=summary,
            wordcloud=wordcloud_url
        )

        response_data = {
            'original_text_count': len(data.split()),
            'summary_text_count': summary_length,
            'wordcloud': wordcloud_url,
            'summary': summary,
            'sentiments': sentiment_analysis
        }

        return Response(response_data, status=status.HTTP_201_CREATED)
 