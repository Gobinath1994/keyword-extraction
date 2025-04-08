# **Customer Support Chat Log Keyword Extraction**

This project aims to **automatically extract keywords** from **customer support chat logs**. It helps businesses identify common issues or trends in customer interactions by analyzing the content of chat messages.

## **Table of Contents**

- [Overview](#overview)
- [Key Features](#key-features)
- [Technologies Used](#technologies-used)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Streamlit Interface](#streamlit-interface)
- [Output](#output)
- [Future Improvements](#future-improvements)

---

## **Overview**

Customer support chat logs contain valuable information about customer issues, product feedback, and more. However, manually reviewing these logs can be time-consuming and error-prone. This tool automates the process of **extracting relevant keywords** from customer messages, allowing companies to quickly identify patterns and improve their services.

### **Key Objectives:**
- Extract meaningful **keywords** from customer messages.
- Build an **interactive UI** with Streamlit for easy exploration.
- Visualize the **most frequent keywords** across multiple chat logs.

---

## **Key Features**

- **Keyword Extraction**: Extracts unigrams and bigrams (e.g., "slow performance", "freezing", "system issues") from customer messages.
- **Streamlit Interface**: A user-friendly web interface to upload chat logs, view keywords, and search/filter messages.
- **Top Keyword Visualization**: A bar chart displaying the most common keywords extracted from all customer messages.
- **Data Export**: Ability to export the extracted keywords along with the customer messages into a CSV file.

---

## **Technologies Used**

- **Python 3.10+**
- **Pandas**: For data manipulation and cleaning.
- **KeyBERT** & **Sentence-Transformers**: For extracting keywords using pre-trained models.
- **Streamlit**: For creating an interactive web interface.
- **Matplotlib**: For visualizing the frequency of extracted keywords.
- **TQDM**: For showing progress bars during long-running operations.

---

## **Setup and Installation**

### **2. Set up a Python environment

It’s recommended to use Conda or virtualenv to manage your dependencies.

Using conda:

conda create -n keyword-extraction python=3.10
conda activate keyword-extraction

Using virtualenv:

python -m venv keyword-extraction
source keyword-extraction/bin/activate  # On Windows: keyword-extraction\Scripts\activate

3. Install required dependencies

pip install -r requirements.txt

4. Verify installation

Check the installation by running the following:

python -c "import pandas, streamlit, keybert, torch"

If no errors appear, you’re all set.

⸻

Usage

1. Batch Processing (without UI)

For batch processing of customer chat logs, run the main.py script:

python main.py

This will:
	•	Load the customer support chat logs.
	•	Extract keywords from the customer messages.
	•	Save the results to outputs/cleaned_keywords.csv.

2. Streamlit UI

To use the interactive Streamlit UI, run the app.py script:

streamlit run app.py

This will launch a web interface where you can:
	•	Upload your chat logs in CSV format.
	•	View and explore the extracted keywords.
	•	Visualize keyword frequencies in a bar chart.
	•	Filter messages by specific keywords.

⸻

Streamlit Interface

1. Upload your chat log CSV:

The app allows you to upload a CSV file that contains the chat logs with columns: chat_id, role, and message.

2. Keyword Extraction:

After uploading the file, the app will automatically extract keywords from customer messages.

3. Keyword Search and Filtering:

You can search for a specific keyword and filter the customer messages containing that keyword.

4. Visualize the Top Keywords:

The app provides a bar chart of the most frequent keywords extracted across all chat logs.

⸻

Output

After processing, the extracted keywords are saved in a CSV file with the following columns:
	•	chat_id: Unique identifier for each chat.
	•	message: The original customer message.
	•	keywords: The extracted keywords (comma-separated).

Example output:

chat_id, message, keywords
1, My system is freezing after a recent update, freezing, system, recent update
2, My system is slowing down, slowing down, system, recent update



⸻

Future Improvements
	•	Sentiment Analysis: Analyze the sentiment of customer messages (e.g., positive, neutral, or negative).
	•	Issue Categorization: Group customer messages into categories like “technical issue”, “account query”, or “feedback”.
	•	Real-Time Chat Integration: Extend the tool to process live customer chat messages and provide real-time analysis.
	•	Enhanced Visualization: Implement more advanced visualizations such as time-based trends or word clouds.

⸻

License

This project is licensed under the MIT License - see the LICENSE file for details.

---

### Explanation of the Sections:

1. **Overview**: Gives an introduction to the problem your project solves — keyword extraction from customer chat logs.
2. **Key Features**: Lists the main functionalities, such as keyword extraction, UI interaction, and data export.
3. **Technologies Used**: Describes the tools and libraries that make the project work.
4. **Setup and Installation**: Step-by-step instructions on setting up the project in a virtual environment.
5. **Usage**: Explains how to use both the **batch processing** script (`main.py`) and the **Streamlit UI** (`app.py`).
6. **Streamlit Interface**: Describes the user interface features for uploading files, searching keywords, and visualizing results.
7. **Output**: Explains the structure of the output CSV file.
8. **Future Improvements**: Mentions possible enhancements you might want to make in the future.
9. **License**: A placeholder for licensing information.

---

