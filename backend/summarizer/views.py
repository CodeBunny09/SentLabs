from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .summarizer import generate_summary, generate_wordcloud, analyze_sentiment

class TextDataListCreateView(APIView):

    def post(self, request, *args, **kwargs):
        data = request.data.get('text')
        print(data)
        if not data:
            return Response({'error': 'Text data is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        summary, summary_length = generate_summary(data)
        wordcloud_url = generate_wordcloud(data)
        sentiment_analysis = analyze_sentiment(data)


        response_data = {
            'original_text_count': len(data.split()),
            'summary_text_count': summary_length,
            'wordcloud': wordcloud_url,
            'summary': summary,
            'sentiments': sentiment_analysis
        }

        return Response(response_data, status=status.HTTP_201_CREATED)
 