import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import string

# Download necessary NLTK data files (only once)
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

def preprocess_text(text):
    """
    Preprocesses input text by performing the following steps:
    1. Tokenization
    2. Lowercasing
    3. Removal of stopwords and punctuation
    4. Lemmatization

    Args:
    text (str): The input raw text to be preprocessed.

    Returns:
    str: The preprocessed text.
    """
    # 1. Tokenize the text
    tokens = word_tokenize(text.lower())  # Convert text to lowercase and tokenize
    
    # 2. Remove stopwords and punctuation
    stop_words = set(stopwords.words('english'))
    punctuation = set(string.punctuation)  # Set of all punctuation symbols
    tokens = [word for word in tokens if word.isalpha() and word not in stop_words and word not in punctuation]
    
    # 3. Lemmatization
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    
    # 4. Join the tokens back into a single string
    return ' '.join(tokens)
