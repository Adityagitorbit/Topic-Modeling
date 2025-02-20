import pandas as pd
import joblib
from bertopic import BERTopic
from utils.text_preprocessing import preprocess_text  # Assuming this function is in utils

# Load dataset (using an absolute path)
data = pd.read_csv('/home/aditya/Programs/Git_HUB/Topic-Modeling/backend/data/dataset.csv')

# Ensure the correct column is used (here, 'content')
if 'content' not in data.columns:
    raise KeyError("The dataset must contain a 'content' column.")

# Preprocess documents
preprocessed_docs = [preprocess_text(doc) for doc in data['content'].dropna()]

# Train BERTopic model using the same transformer model
topic_model = BERTopic(embedding_model="all-MiniLM-L6-v2")
topics, probs = topic_model.fit_transform(preprocessed_docs)

# Save the trained model
topic_model.save('/home/aditya/Programs/Git_HUB/Topic-Modeling/backend/models/bertopic_model')

print("BERTopic model trained and saved successfully!")

# Optionally, export topic details to CSV
topic_info = topic_model.get_topic_info()
topic_info.to_csv('/home/aditya/Programs/Git_HUB/Topic-Modeling/backend/data/topics.csv', index=False)
print("Topics saved for analysis!")
