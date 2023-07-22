# comparing expertise of mentor and project idea and description
from nltk.corpus import stopwords
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('stopwords')
nltk.download('punkt')
stop_words = set(stopwords.words('english'))

# Initialize the NLTK stemmer
stemmer = nltk.stem.PorterStemmer()


def preprocess(text):
    # Tokenize the text
    tokens = nltk.word_tokenize(text.lower())

    # Remove punctuation and stopwords
    tokens = [token for token in tokens if token.isalpha()
              and token not in stop_words]

    # Apply stemming to the tokens
    stemmed_tokens = [stemmer.stem(token) for token in tokens]

    # Join the stemmed tokens back to a string
    preprocessed_text = " ".join(stemmed_tokens)

    return preprocessed_text


def compare_similarity(paragraph1, paragraph2):
    # Preprocess the paragraphs
    preprocessed_paragraph1 = preprocess(paragraph1)
    preprocessed_paragraph2 = preprocess(paragraph2)

    # Create a TfidfVectorizer
    vectorizer = TfidfVectorizer()

    # Fit and transform the paragraphs to TF-IDF vectors
    tfidf_matrix = vectorizer.fit_transform(
        [preprocessed_paragraph1, preprocessed_paragraph2])

    # Calculate the cosine similarity between the two paragraphs
    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])

    return similarity[0][0]


# paragraph1 = "This is the first paragraph in the comparison."
# paragraph2 = "This is the second paragraph for comparison."

# similarity_score = compare_similarity(paragraph1, paragraph2)
# print(f"Similarity Score: {similarity_score:.2f}")
