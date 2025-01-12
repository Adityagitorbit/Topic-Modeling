import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
import joblib
from backend.utils.text_preprocessing import preprocess_text  # Assuming this function is in utils

# Step 1: Load your dataset (you can replace this with your actual CSV or other data source)
# Make sure to adjust the file path and column name based on your data
data = pd.read_csv('/home/aditya/Programs/Git_HUB/Topic-Modeling/backend/data/dataset.csv')  # Replace with your actual dataset
documents = data['content']  # Replace 'text' with the column that contains your documents

# Step 2: Preprocess the text data
preprocessed_docs = [preprocess_text(doc) for doc in documents]

# Step 3: Convert text data to a numerical representation (Bag-of-Words)
vectorizer = CountVectorizer(max_df=0.95, min_df=2, stop_words='english')  # Optional stopwords removal
dt_matrix = vectorizer.fit_transform(preprocessed_docs)

# Step 4: Train the LDA model (Topic Modeling)
lda_model = LatentDirichletAllocation(n_components=5, random_state=42)  # Set number of topics (n_components)
lda_model.fit(dt_matrix)

# Step 5: Save the trained models
joblib.dump(vectorizer, '/home/aditya/Programs/Git_HUB/Topic-Modeling/backend/models/vectorizer.pkl')
joblib.dump(lda_model, '/home/aditya/Programs/Git_HUB/Topic-Modeling/backend/models/lda_model.pkl')


print("Models saved successfully!")
