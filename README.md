# 🔍 Vector Search RAG System

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-4.4%2B-green?logo=mongodb&logoColor=white)
![HuggingFace](https://img.shields.io/badge/HuggingFace-Transformers-yellow?logo=huggingface&logoColor=white)

A sophisticated movie recommendation system using Vector Search and RAG (Retrieval Augmented Generation) capabilities, powered by HuggingFace's sentence transformers and MongoDB Atlas.

## 🌟 Features

- **Semantic Search**: Utilizes sentence embeddings for meaningful movie searches
- **Vector Database**: Leverages MongoDB Atlas's vector search capabilities
- **Real-time Processing**: Generate embeddings on-the-fly using HuggingFace's API
- **Efficient Retrieval**: Fast and accurate movie recommendations based on plot descriptions

## 🏗️ Project Structure

```
Vector-Search-RaG/
├── apps/
│   └── semantic_search/
│       ├── __init__.py
│       ├── hf_connection.py    # HuggingFace API connection
│       ├── mongo_connection.py # MongoDB connection handler
│       └── movie_recs.py      # Movie recommendation logic
├── ragenv/                    # Virtual environment
├── LICENSE
└── README.md
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- MongoDB Atlas account
- HuggingFace API token
- pip (Python package manager)

### Environment Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Vector-Search-RaG.git
cd Vector-Search-RaG
```

2. Create and activate virtual environment:
```bash
python -m venv ragenv
source ragenv/bin/activate  # On Windows: ragenv\Scripts\activate
```

3. Install dependencies:
```bash
pip install pymongo requests python-decouple
```

4. Create a `.env` file in the root directory with your credentials:
```env
MONGODB_URI=your_mongodb_connection_string
HUGGING_FACE_TOKEN=your_huggingface_token
```

## 💻 Configuration Components

### HuggingFace Connection (`hf_connection.py`)
- Manages connections to HuggingFace's API
- Uses the `sentence-transformers/all-MiniLM-L6-v2` model for generating embeddings
- Handles API authentication and error handling

### MongoDB Connection (`mongo_connection.py`)
- Establishes secure connection to MongoDB Atlas
- Implements TLS security
- Includes connection validation and error handling

### Movie Recommendations (`movie_recs.py`)
- Implements vector search functionality
- Processes movie queries and generates recommendations
- Includes utilities for fetching and updating movie data

## 🔧 Usage

### Basic Search Example
```python
from apps.semantic_search.movie_recs import search_movies

# Search for movies with a specific plot description
query = "A group of bandits stage a brazen train hold-up"
search_movies(query)
```

### Update Movie Data
```python
from apps.semantic_search.movie_recs import fetch_and_update_movies

# Fetch and update movie information
fetch_and_update_movies()
```

## 🎯 Vector Search Details

The system uses MongoDB's `$vectorSearch` aggregation for semantic search:
- Generates embeddings using HuggingFace's sentence transformer
- Searches against pre-computed plot embeddings stored in MongoDB
- Returns the most semantically similar movies based on plot descriptions

## 🔒 Security Features

- TLS encryption for MongoDB connections
- Secure API token handling via environment variables
- Certificate validation for secure connections

## ⚠️ Important Notes

1. Ensure your MongoDB Atlas cluster has vector search capability enabled
2. The HuggingFace API has rate limits - consider implementing caching for production use
3. Keep your `.env` file secure and never commit it to version control

## 📈 Performance Considerations

- The system uses `numCandidates: 100` for broad search coverage
- Results are limited to 4 movies per query for optimal response time
- Vector search index "PlotSemanticSearch" should be properly configured in MongoDB

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the terms of the LICENSE file included in the repository.
