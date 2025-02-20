import pandas as pd
from bertopic import BERTopic
import joblib
from backend.utils.text_preprocessing import preprocess_text

# Step 1: Load Dataset
data = pd.read_csv("backend/data/dataset.csv")  # Ensure dataset.csv exists
documents = data["content"].dropna().tolist()   # Ensure 'content' column exists

# Step 2: Preprocess Text
preprocessed_docs = [preprocess_text(doc) for doc in documents]

# Step 3: Train BERTopic Model with a heavier transformer model
# Example: using "paraphrase-mpnet-base-v2" for richer embeddings
topic_model = BERTopic(embedding_model="paraphrase-mpnet-base-v2", verbose=True)
topics, probs = topic_model.fit_transform(preprocessed_docs)

# Step 4: Save the trained BERTopic model
topic_model.save("backend/models/bertopic_model")

print("BERTopic model trained and saved successfully with a heavier model!")

# Step 5 (Optional): Save Topics to CSV for Analysis
topic_info = topic_model.get_topic_info()
topic_info.to_csv("backend/data/topics.csv", index=False)
print("Topics saved for analysis!")
