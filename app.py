import streamlit as st
import pandas as pd
from keybert import KeyBERT
from sentence_transformers import SentenceTransformer
import matplotlib.pyplot as plt
from collections import Counter

# Set up Streamlit page configuration
st.set_page_config(page_title="Chat Keyword Extractor", layout="wide")

# Load model function with caching to optimize performance
@st.cache_resource
def load_model():
    """
    Loads the SentenceTransformer model and initializes KeyBERT for keyword extraction.

    Returns:
    - KeyBERT model for keyword extraction.
    """
    model = SentenceTransformer("all-MiniLM-L6-v2")
    return KeyBERT(model)

# Initialize KeyBERT model
kw_model = load_model()

# Keyword extraction function using KeyBERT
def extract_keywords(text):
    """
    Extracts the top 5 keywords from a given text using the KeyBERT model.

    Args:
    - text (str): The input text from which to extract keywords.

    Returns:
    - List of keywords.
    """
    keywords = kw_model.extract_keywords(
        text,  # The input text to extract keywords from
        keyphrase_ngram_range=(1, 2),  # Extract unigrams and bigrams
        stop_words='english',  # Remove common English stop words
        use_maxsum=True,  # Reduce redundancy in keywords using MaxSum optimization
        nr_candidates=10,  # Number of candidates to consider during extraction
        top_n=5  # Extract the top 5 keywords
    )
    return [kw[0] for kw in keywords]  # Return the keywords as a list

# Streamlit UI setup
st.title("🧠 Customer Chat Keyword Extractor")

# Upload chat log CSV file
uploaded_file = st.file_uploader("📂 Upload your chat_logs.csv", type=["csv"])

# Process the uploaded file
if uploaded_file:
    df = pd.read_csv(uploaded_file)

    # Check if required columns exist in the uploaded CSV
    if not {"chat_id", "role", "message"}.issubset(df.columns):
        st.error("CSV must have 'chat_id', 'role', and 'message' columns.")
    else:
        # Filter customer messages and remove duplicates
        df_customer = df[df["role"].str.lower() == "customer"].copy()
        df_customer.drop_duplicates(subset='message', inplace=True)
        df_customer.reset_index(drop=True, inplace=True)

        # Extract keywords if the button is clicked
        if st.button("🚀 Extract Keywords"):
            with st.spinner("Extracting keywords..."):
                # Apply keyword extraction to each customer message
                df_customer["keywords"] = df_customer["message"].apply(lambda x: extract_keywords(x))
            st.success("Done! ✅")

            # Convert list of keywords to comma-separated string for display
            df_customer["keywords_str"] = df_customer["keywords"].apply(lambda x: ", ".join(x))
            st.dataframe(df_customer[["chat_id", "message", "keywords_str"]])

            # Save the processed data with keywords to a CSV file
            df_customer[["chat_id", "message", "keywords_str"]].to_csv("outputs/cleaned_keywords.csv", index=False)

            # Plot the top keywords based on frequency
            st.subheader("📊 Top Keywords")
            all_keywords = [kw for row in df_customer["keywords"] for kw in row]
            top_keywords = Counter(all_keywords).most_common(15)
            if top_keywords:
                words, counts = zip(*top_keywords)
                fig, ax = plt.subplots(figsize=(10, 5))
                ax.bar(words, counts)
                plt.xticks(rotation=45)
                st.pyplot(fig)

            # Search functionality to filter messages based on a keyword
            st.subheader("🔍 Search by Keyword")
            search_kw = st.text_input("Enter keyword to filter:")
            if search_kw:
                # Filter customer messages that contain the search keyword
                filtered = df_customer[df_customer["keywords"].apply(lambda x: search_kw.lower() in [kw.lower() for kw in x])]
                st.write(f"{len(filtered)} results:")
                st.dataframe(filtered[["chat_id", "message", "keywords_str"]])