import pandas as pd
import random
import faker

# Initialize Faker for generating realistic text
fake = faker.Faker()

# Define 3,000 unique categories covering diverse fields
categories = [
    f"General_Knowledge_{i}" for i in range(1, 251)
] + [
    f"Science_{i}" for i in range(1, 251)
] + [
    f"Math_{i}" for i in range(1, 251)
] + [
    f"AI_{i}" for i in range(1, 251)
] + [
    f"Data_Security_{i}" for i in range(1, 251)
] + [
    f"Finance_{i}" for i in range(1, 251)
] + [
    f"IoT_{i}" for i in range(1, 251)
] + [
    f"Defence_{i}" for i in range(1, 251)
] + [
    f"Sports_{i}" for i in range(1, 251)
] + [
    f"Politics_{i}" for i in range(1, 251)
] + [
    f"Nature_{i}" for i in range(1, 251)
] + [
    f"Computer_Science_{i}" for i in range(1, 249)
]  # Total 3,000 categories

# Generate random content for each category
def generate_content(category):
    if "General_Knowledge" in category:
        return fake.sentence() + " Did you know that Mount Everest is the highest peak in the world?"
    elif "Science" in category:
        return fake.sentence() + " Scientists have recently discovered a new species of deep-sea fish."
    elif "Math" in category:
        return fake.sentence() + " The Pythagorean theorem is fundamental in trigonometry."
    elif "AI" in category:
        return fake.sentence() + " AI and deep learning are transforming industries like healthcare and finance."
    elif "Data_Security" in category:
        return fake.sentence() + " Cybersecurity threats are increasing, with companies investing more in data protection."
    elif "Finance" in category:
        return fake.sentence() + " The stock market fluctuates daily based on economic conditions."
    elif "IoT" in category:
        return fake.sentence() + " The Internet of Things is connecting billions of smart devices worldwide."
    elif "Defence" in category:
        return fake.sentence() + " Military advancements in drone technology are revolutionizing warfare."
    elif "Sports" in category:
        return fake.sentence() + " The FIFA World Cup attracts millions of fans every four years."
    elif "Politics" in category:
        return fake.sentence() + " Elections and political campaigns influence global policy-making."
    elif "Nature" in category:
        return fake.sentence() + " The Amazon Rainforest is home to a diverse range of plant and animal species."
    elif "Computer_Science" in category:
        return fake.sentence() + " Computer algorithms are the backbone of modern software applications."
    else:
        return fake.sentence() + " Knowledge is expanding in various fields of study."

# Number of rows to generate
num_rows = 50000000

# Generate dataset
data = []
for _ in range(num_rows):
    category = random.choice(categories)  # Randomly select one of 3,000 categories
    content = generate_content(category)  # Generate unique content
    data.append({'content': content, 'category': category})

# Create DataFrame
df = pd.DataFrame(data)

# Save dataset to CSV file
df.to_csv('dataset.csv', index=False)

print(f"Generated dataset with {num_rows} rows and saved it as 'dataset.csv'.")
