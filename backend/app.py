from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import joblib
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
import pdfplumber

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

app = FastAPI()

# Load pre-trained models
vectorizer = joblib.load('/home/aditya/Programs/Git_HUB/Topic-Modeling/backend/models/vectorizer.pkl')
lda_model = joblib.load('/home/aditya/Programs/Git_HUB/Topic-Modeling/backend/models/lda_model.pkl')

# Preprocessing function
def preprocess_text(text):
    

    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('wordnet')

    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(text.lower())
    tokens = [word for word in tokens if word.isalpha() and word not in stop_words]
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    return ' '.join(tokens)

# Extract text from PDF
def extract_text_from_pdf(file):
    with pdfplumber.open(file) as pdf:
        return " ".join(page.extract_text() for page in pdf.pages)

@app.post("/process-text/")
async def process_text_endpoint(text: str):
    preprocessed = preprocess_text(text)
    dt_matrix = vectorizer.transform([preprocessed])
    topic_distribution = lda_model.transform(dt_matrix)
    dominant_topic = topic_distribution.argmax()
    return JSONResponse(content={"dominant_topic": int(dominant_topic)})

@app.post("/process-pdf/")
async def process_pdf_endpoint(file: UploadFile = File(...)):
    text = extract_text_from_pdf(file.file)
    preprocessed = preprocess_text(text)
    dt_matrix = vectorizer.transform([preprocessed])
    topic_distribution = lda_model.transform(dt_matrix)
    dominant_topic = topic_distribution.argmax()
    return JSONResponse(content={"dominant_topic": int(dominant_topic)})
