#usage python .\play-song-demo.py artistname
import json
import requests
import sys
import random
import webbrowser

# Ensure there's exactly one argument
if len(sys.argv) != 2:
    sys.exit("Please provide exactly one search term (the artist's name).")

# Join the arguments into a single search term (if more than one argument is provided)
search_term = " ".join(sys.argv[1:])

# Make the API request using the search term
response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + search_term)

# Check if the request was successful
if response.status_code != 200:
    sys.exit(f"Request failed with status code {response.status_code}")

# Parse the JSON response
data = response.json()

# Check if there are results
if "results" not in data or len(data["results"]) == 0:
    sys.exit("No results found.")

# Randomly choose one song from the results
random_song = random.choice(data["results"])

# Get the track name and the preview URL
track_name = random_song["trackName"]
preview_url = random_song["previewUrl"]

# Print out the chosen track name
print(f"Now playing: {track_name}")

# Open the preview URL in the web browser
webbrowser.open(preview_url)