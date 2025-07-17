import requests

# Correct API key
api_key = "YOUR-API-KEY"
base_url = "https://www.omdbapi.com/"

def get_movie(name):
    # Fix API query format
    url = f"{base_url}?t={name}&apikey={api_key}"
    response = requests.get(url)
    print(f"API Response Status: {response.status_code}")

    if response.status_code == 200:
        data = response.json()

        # Check if movie exists in API response
        if data.get("Response") == "True":
            return data
        else:
            print(f"Error: Movie '{name}' not found.")
            return None
    else:
        print(f"API Error: {response.text}")
        return None

def main():
    movie_name = input("Enter the movie name: ")
    movie_data = get_movie(movie_name)

    if movie_data:
        # Extract movie details safely using `.get()`
        year = movie_data.get('Year', 'N/A')
        rating = movie_data.get('imdbRating', 'N/A')
        rated = movie_data.get('Rated', 'N/A')
        runtime = movie_data.get('Runtime', 'N/A')
        plot = movie_data.get('Plot', 'N/A')

        # Display movie details
        print("\n🎬 Movie Details 🎬")
        print(f"Title: {movie_data.get('Title', movie_name)}")
        print(f"Year: {year}")
        print(f"IMDB Rating: {rating}")
        print(f"Rated: {rated}")
        print(f"Runtime: {runtime}")
        print(f"Plot: {plot}\n")

if __name__ == "__main__":
    main()
