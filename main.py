import pandas as pd
from tqdm import tqdm
from keybert import KeyBERT
from sentence_transformers import SentenceTransformer

# Load input CSV file containing the chat logs
df = pd.read_csv("data/chat_logs.csv")

# Filter only customer messages (where role is 'customer')
df_customer = df[df['role'].str.lower() == 'customer'].copy()

# Remove duplicate messages from the customer data to avoid repetitive keyword extraction
df_customer.drop_duplicates(subset='message', inplace=True)

# Reset the index after removing duplicates to keep the DataFrame in proper order
df_customer.reset_index(drop=True, inplace=True)

# Load the pre-trained SentenceTransformer model for embedding text
model = SentenceTransformer("all-MiniLM-L6-v2")

# Initialize KeyBERT with the SentenceTransformer model for keyword extraction
kw_model = KeyBERT(model)

# Function to extract keywords from a given text
def extract_keywords(text):
    """
    Extracts the top 5 keywords from a given text using KeyBERT and Sentence-Transformers.

    Args:
    - text (str): The input text from which to extract keywords.

    Returns:
    - str: Comma-separated string of the top 5 extracted keywords.
    """
    keywords = kw_model.extract_keywords(
        text,  # The input text to extract keywords from
        keyphrase_ngram_range=(1, 2),  # Extract unigrams and bigrams
        stop_words='english',  # Remove common English stop words (e.g., 'the', 'is', 'and')
        use_maxsum=True,  # Reduce redundancy in keywords using MaxSum optimization
        nr_candidates=10,  # Number of candidates to consider during keyword extraction
        top_n=5  # Extract the top 5 keywords
    )
    # Join the extracted keywords into a comma-separated string and return
    return ", ".join([kw[0] for kw in keywords])

# Apply the extract_keywords function to each customer message and track progress using tqdm
tqdm.pandas()  # Enables progress_apply to show a progress bar
df_customer["keywords"] = df_customer["message"].progress_apply(extract_keywords)

# Save the results (customer message and extracted keywords) to a new CSV file
df_customer.to_csv("outputs/cleaned_keywords.csv", index=False)

# Print a confirmation message that the output has been saved
print("✅ Saved to outputs/cleaned_keywords.csv")