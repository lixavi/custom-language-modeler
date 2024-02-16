import re
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

def clean_text(text):
    """
    Clean the input text by removing special characters, digits, and extra whitespaces.
    """
    text = re.sub(r'\d+', '', text)  # Remove digits
    text = re.sub(r'[^\w\s]', '', text)  # Remove special characters
    text = text.strip()  # Remove leading/trailing whitespaces
    return text

def tokenize_text(text):
    """
    Tokenize the input text into words.
    """
    tokens = word_tokenize(text)
    return tokens

def remove_stopwords(tokens):
    """
    Remove stopwords from the tokenized text.
    """
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [token for token in tokens if token.lower() not in stop_words]
    return filtered_tokens

def lemmatize_tokens(tokens):
    """
    Lemmatize the tokens to their base form.
    """
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
    return lemmatized_tokens
