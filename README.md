# 🎵 Lyrics Sentiment Analysis

## Overview
This project explores the **sentiment analysis of song lyrics**, leveraging data from **Genius API** and **Spotify's sentiment data**. The goal is to analyze how song lyrics correlate with their emotional tone as inferred from Spotify's metadata. 

## 🚀 Features
- **Lyrics Extraction**: Fetches song lyrics using the Genius API.
- **Spotify Sentiment Data**: Incorporates Spotify's sentiment-related features.
- **Data Parsing & Processing**: Cleans and structures lyrics for sentiment analysis.
- **Sentiment Analysis Techniques**: Applies different methodologies to analyze the emotions conveyed in lyrics.
- **Deep Learning Models**: Implements machine learning models such as **DAN with GloVe embeddings** and **BERT**.

## 📂 Project Structure
```
├── data/                      # Processed data files
├── scripts/                   # Python scripts for data collection & processing
│   ├── Install Lyric Genius.py     # Installs required API dependencies
│   ├── Genius_path_for_lyrics_pandas.py  # Fetches song lyrics using Genius API
│   ├── parsing_lyrics_pandas.py     # Extracts and cleans lyrics
│   ├── (More to be added...)        
├── notebooks/                 # Jupyter notebooks for sentiment analysis
│   ├── DAN_glove_Cristobal_no_stop_words_nopunctuation.ipynb  # DAN model without stopwords & punctuation
│   ├── DAN_glove_Cristobal_no_stop_words_punct_4layers.ipynb  # DAN model with 4-layer architecture
│   ├── DAN_glove_Cristobal_w_stopWords.ipynb  # DAN model with stopwords
│   ├── BERT.ipynb  # BERT-based sentiment analysis
├── README.md                  # Project documentation
```

## 📜 How It Works
1. **Lyrics Collection**
   - Uses the **Genius API** to search for songs and extract lyrics.
   - Handles missing data by retrying and logging failed attempts.

2. **Spotify Sentiment Data Integration**
   - Pulls **song-level metadata** (e.g., valence, energy) from Spotify.
   - Maps these attributes to corresponding lyrics for sentiment analysis.

3. **Lyrics Processing & Sentiment Analysis**
   - Cleans and structures the lyrics data.
   - Applies **text-based sentiment analysis** using techniques such as:
     - Natural Language Processing (NLP) sentiment scoring
     - Lexicon-based sentiment comparison
     - Machine learning models (DAN with GloVe, BERT)

## 🔧 Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/repository-name.git
   cd repository-name
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   *(If `requirements.txt` is missing, install manually: `pip install lyricsgenius rauth pandas requests beautifulsoup4 torch transformers`)*

## 🛠 Usage
- Run **`Install Lyric Genius.py`** to set up API dependencies.
- Use **`Genius_path_for_lyrics_pandas.py`** to fetch song lyrics from the Genius API.
- Execute **`parsing_lyrics_pandas.py`** to clean and structure lyrics.
- Experiment with different sentiment models in the `notebooks/` directory:
  - **DAN with GloVe embeddings** for sentiment prediction.
  - **BERT-based models** for deep learning sentiment analysis.

## 📌 Contributions
This project was a **team effort**. If you'd like to contribute, feel free to fork the repository, make changes, and submit a pull request.
