from transformers import pipeline
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import io
import base64
from PIL import Image

# Load summarization pipeline
summarizer = pipeline("summarization")

def generate_summary(text):
    # Ensure text length is manageable for the model
    max_length = 1024
    input_length = len(text.split())
    
    if input_length > max_length:
        text = ' '.join(text.split()[:max_length])
    
    summary = summarizer(text, max_length=150, min_length=30, do_sample=False)[0]['summary_text']
    return summary, len(summary.split())

def generate_wordcloud(text):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    plt.figure(figsize=(8, 4), facecolor='w', edgecolor='k')
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    image = Image.open(buf)
    buffered = io.BytesIO()
    image.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    return f"data:image/png;base64,{img_str}"

def analyze_sentiment(text):
    # Dummy function for sentiment analysis
    return {
        "happy": "35%",
        "dark": "76%"
    }
