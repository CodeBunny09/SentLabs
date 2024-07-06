# summarizer/utils.py
import torch
import textwrap
from transformers import pipeline


# Check if GPU is available and set the device
device = 0 if torch.cuda.is_available() else -1

# Create the summarizer pipeline with the specified device
summarizer = pipeline("summarization")
print("\n\nPipeline Initialized")

def generate_summary(text):
    summary = summarizer(text)
    print(summary[0]['summary_text'])
    return summary[0]['summary_text']
