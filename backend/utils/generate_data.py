import pandas as pd
import random
import faker

# Initialize the Faker object for generating fake sentences
fake = faker.Faker()

# Define 300 unique categories for the news articles
categories = [
    'business', 'sports', 'politics', 'health', 'technology', 'science', 'education', 'economy', 'entertainment', 'travel',
    'art', 'music', 'finance', 'startup', 'education', 'government', 'climate change', 'space', 'environment', 'history',
    'religion', 'law', 'medicine', 'AI', 'robotics', 'self-driving cars', 'blockchain', 'cryptocurrency', 'data science', 'big data',
    'quantum computing', 'cybersecurity', 'social media', 'marketing', 'advertising', 'psychology', 'nutrition', 'lifestyle', 'fashion', 
    'celebrity', 'social issues', 'global warming', 'urbanization', 'future tech', 'food industry', 'literature', 'poetry', 'movie reviews',
    'gaming', 'virtual reality', 'augmented reality', 'machine learning', 'neuroscience', 'healthcare', 'fitness', 'personal finance', 
    'cryptography', 'cloud computing', 'smart cities', 'public health', 'disaster management', 'vaccine', 'public speaking', 'law enforcement',
    'pandemic', 'architecture', 'advertisement industry', 'digital transformation', 'philanthropy', 'non-profit', 'space exploration',
    'online education', 'E-commerce', 'sports science', 'political theory', 'food security', 'space technology', 'bioengineering', 'climate action',
    'medical technology', 'sustainable development', 'labor markets', 'robotic surgery', 'mental health', 'self-improvement', 'wellness', 
    'leadership', 'productivity', 'startup culture', 'cloud storage', 'cloud security', 'app development', 'web development', 'urban farming',
    'public transport', 'smart home', 'green energy', 'environmentalism', 'gender equality', 'poverty alleviation', 'immigration', 'freedom of speech',
    'geopolitics', 'neoliberalism', 'socioeconomic issues', 'workplace culture', 'telemedicine', 'economic growth', 'resource management', 
    'machine vision', 'internet of things', 'data privacy', 'public transport', 'emotional intelligence', 'remote work', 'gig economy', 'corporate world',
    'supply chain', 'food waste', 'mental illness', 'political correctness', 'higher education', 'scientific discovery', 'tech startups', 'pharmaceuticals',
    'artificial intelligence', 'renewable energy', 'public relations', 'marketing strategy', 'social entrepreneurship', 'corporate social responsibility',
    'voting', 'leadership development', 'corporate culture', 'sustainability', 'biotech', 'economic development', 'machine learning models', 
    'biotechnology', 'space tourism', 'global issues', 'alternative medicine', 'corporate ethics', 'remote education', 'human rights', 'technology startups',
    'space stations', 'intellectual property', 'social change', 'climate justice', 'women’s rights', 'cyberbullying', 'digital currency', 'mental health awareness',
    'emergency response', 'global trade', 'corporate strategy', 'international relations', 'renewable resources', 'self-driving technology', 'trade agreements',
    'natural resources', 'financial management', 'privacy laws', 'international organizations', 'public health crises', 'gender studies', 'robotic process automation',
    'political parties', 'subsidies', 'capitalism', 'pollution', 'sustainable agriculture', 'energy efficiency', 'telecommunication', 'electric vehicles', 'finance industry',
    'international development', 'crisis management', 'privacy policy', 'cloud services', 'autonomous vehicles', 'social media marketing', 'human trafficking', 
    'cyber attacks', 'green business', 'consumer behavior', 'food safety', 'addiction', 'cybersecurity attacks', 'political activism', 'mental health care',
    'sports broadcasting', 'industrial automation', 'financial institutions', 'scientific community', 'global conflicts', 'international business', 'economic policies',
    'digital marketing', 'travel technology', 'bioinformatics', 'weather patterns', 'international trade', 'data security', 'health insurance', 'food security', 
    'public health policy', 'environmental protection', 'sustainable energy', 'agriculture', 'chemical engineering', 'online privacy', 'health policy', 'drug development'
]

# Generate random content for the dataset
def generate_content(category):
    # Generate random sentences depending on the category
    return fake.sentence() + f" This article discusses issues related to {category}."

# Number of rows to generate
num_rows = 6000000

# Create a list of dictionaries with content and category
data = []

for _ in range(num_rows):
    category = random.choice(categories)
    content = generate_content(category)
    data.append({'content': content, 'category': category})

# Create a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv('/home/aditya/Programs/Git_HUB/Topic-Modeling/backend/data/dataset.csv', index=False)

print(f"Generated a dataset with {num_rows} rows and saved it as 'dataset.csv'.")
