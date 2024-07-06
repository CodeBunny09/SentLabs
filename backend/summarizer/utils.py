# summarizer/utils.py
import torch
import textwrap
from transformers import pipeline



# Wrap functin for text
def wrap(x):
  return textwrap.fill(x, replace_whitespace=False, fix_sentence_endings=True)

# Check if GPU is available and set the device
device = 0 if torch.cuda.is_available() else -1

# Create the summarizer pipeline with the specified device
summarizer = pipeline("summarization")

def generate_summary(text):
    summary = summarizer(text)
    return summary[0]['summary_text']
