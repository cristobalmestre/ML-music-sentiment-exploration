import requests
import pandas as pd
import os

def search_song_lyrics_url(artist, title, access_token):
    search_url = "https://api.genius.com/search"
    headers = {'Authorization': f'Bearer {access_token}'}
    params = {'q': f'{artist} {title}'}

    response = requests.get(search_url, headers=headers, params=params)
    if response.status_code != 200:
        return None

    data = response.json()
    hits = data['response']['hits']
    if hits:
        song_url = hits[0]['result']['url']
        return song_url
    return None

access_token = # get a key from genius
input_csv_path = 'Song_names - from luis villegas.csv'
output_csv_path = 'Song_names_with_urls_complete.csv'

checkpoint_path = 'checkpoint.csv'

# Check if checkpoint exists, load from it; otherwise, load the input CSV
if os.path.exists(checkpoint_path):
    df = pd.read_csv(checkpoint_path, delimiter=';')
    print("Resuming from checkpoint.")
else:
    try:
        df = pd.read_csv(input_csv_path, delimiter=';', encoding='utf-8')
    except UnicodeDecodeError:
        df = pd.read_csv(input_csv_path, delimiter=';', encoding='ISO-8859-1')
    df['Lyrics URL'] = ''  # Initialize the Lyrics URL column only if starting fresh
    print("Starting from scratch.")


for index, row in df.iterrows():
    if pd.isna(row['Lyrics URL']) or row['Lyrics URL'] == '':
        artist = row[1]  
        title = row[2]  
        lyrics_url = search_song_lyrics_url(artist, title, access_token)
        df.at[index, 'Lyrics URL'] = lyrics_url

        if (index + 1) % 1000 == 0:
            df.to_csv(checkpoint_path, sep=';', index=False, quotechar='"', quoting=0)
            print(f"Processed {index + 1} songs. Checkpoint saved.")

# Save the final DataFrame to the output CSV, replacing the checkpoint if full process completes
df.to_csv(output_csv_path, sep=';', index=False, quotechar='"', quoting=0)
os.remove(checkpoint_path)  # Remove checkpoint file after successful completion
