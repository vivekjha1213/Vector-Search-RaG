from apps.semantic_search.hf_connection import generate_embedding
from .mongo_connection import get_mongo_client

def search_movies(query):
    """
    Searches for movies based on the provided query using vector search.
    """
    client = get_mongo_client()
    
    if client:
        try:
            db = client['sample_mflix']
            collection = db.movies
            
            # Generate the embedding for the query
            query_vector = generate_embedding(query)

            # Execute the vector search
            results = collection.aggregate([
                {
                    "$vectorSearch": {
                        "queryVector": query_vector,
                        "path": "plot_embedding_hf",
                        "numCandidates": 100,
                        "limit": 4,
                        "index": "PlotSemanticSearch",
                    }
                }
            ])

            # Print the search results
            for document in results:
                print(f'Movie Name: {document["title"]},\nMovie Plot: {document["plot"]}\n')

        except Exception as e:
            print(f"An error occurred while searching: {e}")

def fetch_and_update_movies():
    """
    Fetches and prints documents from the 'movies' collection,
    and updates a specific document.
    """
    client = get_mongo_client()
    
    if client:
        try:
            db = client['sample_mflix']
            collection = db.movies
            
            doc_count = collection.count_documents({})
            print(f"Total documents in 'movies' collection: {doc_count}")

            if doc_count > 0:
                print("Fetching the first 5 documents:")
                for item in collection.find().limit(5):
                    print(item)

                filter_criteria = {"title": "Some Movie Title"}  
                update_data = {"$set": {"title": "Updated Movie Title"}} 

                result = collection.update_one(filter_criteria, update_data)

                if result.modified_count > 0:
                    print("Document updated successfully.")
                else:
                    print("No documents matched the criteria or document already updated.")

                print("Updated documents:")
                for item in collection.find(filter_criteria):
                    print(item)

            else:
                print("No documents found in the 'movies' collection.")

        except Exception as e:
            print(f"An error occurred while fetching or updating data: {e}")

if __name__ == "__main__":
    query = "A group of bandits stage a brazen train hold-up"
    search_movies(query)  # Perform vector search
    fetch_and_update_movies()  # Fetch and update documents
