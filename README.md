# Customer Support Chat Log Keyword Extraction

This project aims to **automatically extract keywords** from **customer support chat logs**. It helps businesses identify common issues or trends in customer interactions by analyzing the content of chat messages.

---

## Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Technologies Used](#technologies-used)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
  - [Batch Processing](#1-batch-processing-without-ui)
  - [Streamlit UI](#2-streamlit-ui)
- [Streamlit Interface](#streamlit-interface)
- [Output](#output)
- [Future Improvements](#future-improvements)
- [License](#license)

---

## Overview

Customer support chat logs contain valuable information about customer issues, product feedback, and more. However, manually reviewing these logs can be time-consuming and error-prone. This tool automates the process of **extracting relevant keywords** from customer messages, allowing companies to quickly identify patterns and improve their services.

### Key Objectives

- Extract meaningful **keywords** from customer messages.
- Build an **interactive UI** with Streamlit for easy exploration.
- Visualize the **most frequent keywords** across multiple chat logs.

---

## Key Features

- 🔍 **Keyword Extraction**: Extracts unigrams and bigrams (e.g., "slow performance", "freezing", "system issues") from customer messages.
- 🧭 **Streamlit Interface**: A user-friendly web interface to upload chat logs, view keywords, and search/filter messages.
- 📊 **Top Keyword Visualization**: Bar chart displaying the most common keywords extracted from all messages.
- 💾 **Data Export**: Export the extracted keywords and original messages to a CSV file.

---

## Technologies Used

- **Python 3.10+**
- **Pandas** – Data manipulation and cleaning
- **KeyBERT** & **Sentence-Transformers** – Keyword extraction using pre-trained models
- **Streamlit** – Interactive web application
- **Matplotlib** – Visualization
- **TQDM** – Progress bars for long operations

---

## Setup and Installation

### 1. Set Up a Python Environment

Using `conda`:

```bash
conda create -n keyword-extraction python=3.10
conda activate keyword-extraction
```

Or using `virtualenv`:

```bash
python -m venv keyword-extraction
# On macOS/Linux:
source keyword-extraction/bin/activate
# On Windows:
keyword-extraction\Scripts\activate
```

### 2. Install Required Dependencies

```bash
pip install -r requirements.txt
```

### 3. Verify Installation

```bash
python -c "import pandas, streamlit, keybert, torch"
```

If no errors appear, you're good to go!

---

## Usage

### 1. Batch Processing (without UI)

Run the script to process chat logs:

```bash
python main.py
```

This will:
- Load the customer support chat logs
- Extract keywords from the messages
- Save the results to `outputs/cleaned_keywords.csv`

---

### 2. Streamlit UI

Launch the Streamlit app:

```bash
streamlit run app.py
```

This will open a browser-based UI where you can:
- Upload your chat logs in CSV format
- View and explore the extracted keywords
- Visualize keyword frequencies in a bar chart
- Filter messages by specific keywords

---

## Streamlit Interface

1. **Upload Chat Log CSV**  
   Upload a CSV file with columns: `chat_id`, `role`, and `message`.

2. **Keyword Extraction**  
   The app automatically extracts keywords from customer messages after upload.

3. **Search and Filter**  
   Use the search box to filter messages by keyword.

4. **Visualize Top Keywords**  
   A bar chart shows the most frequently occurring keywords.

---

## Output

The output CSV file `cleaned_keywords.csv` includes:

| chat_id | message                                 | keywords                          |
|---------|-----------------------------------------|-----------------------------------|
| 1       | My system is freezing after an update   | freezing, system, recent update   |
| 2       | My system is slowing down               | slowing down, system              |

---

## Future Improvements

- 🧠 **Sentiment Analysis**: Analyze sentiment of messages (positive/neutral/negative)
- 🗂️ **Issue Categorization**: Group messages into categories (e.g., “technical issue”, “feedback”)
- 🔁 **Real-Time Chat Integration**: Process live chat streams
- 📈 **Enhanced Visualizations**: Add word clouds, time-series trends, etc.

---

## License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.
