import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

def get_lyrics_from_url(url):
    page = requests.get(url)
    html = BeautifulSoup(page.text, 'html.parser')
    lyrics_containers = html.find_all('div', class_='Lyrics__Container-sc-1ynbvzw-1')
    lyrics = ""
    for container in lyrics_containers:
        if container.get('data-lyrics-container') == 'true':
            section_text = container.get_text(separator='|')
            lyrics += section_text + '|'
    return lyrics.strip('|') if lyrics else "Lyrics not found."

'''
data_directory = '/data/'
checkpoint_file = os.path.join(data_directory, 'processing_checkpoint.txt')


if not os.path.exists(data_directory):
    os.makedirs(data_directory)

input_csv_path = os.path.join(data_directory, 'Songs_sentiment_list_filtered.csv')

print("Attempting to access:", input_csv_path)
print("Current working directory:", os.getcwd())

if os.path.exists(input_csv_path):
    print("File exists.")
else:
    print("File does not exist.")

'''

checkpoint_file = os.path.join('processing_checkpoint.txt')
input_csv_path = 'Lyrics not found List.csv'

def update_checkpoint(index, file_count):
    with open(checkpoint_file, 'w') as f:
        f.write(f"{index},{file_count}")

def get_last_processed_info():
    if os.path.exists(checkpoint_file):
        with open(checkpoint_file) as f:
            index, file_count = f.read().split(',')
            print(f"Resuming from part {int(file_count)+1} with songs up to index {int(index)+1}.")
            return int(index), int(file_count)
    return -1, 0  # Return -1, 0 if no checkpoint exists


# Load the input CSV into a pandas DataFrame
df = pd.read_csv(input_csv_path, delimiter=';', encoding='utf-8')
df['Lyrics'] = ''  # Add a new column for lyrics

last_processed_index, file_count = get_last_processed_info()
part_counter = file_count  # Continue from the last file count

update_frequency = 500  # Number of rows after which to update the current output file
rows_per_file = 10000  # Number of rows after which to save to a new file and start a new one

# Calculate the starting point for the current chunk based on the last processed index
# When resuming, this should align with the start of the chunk containing the last processed song
chunk_start_index = (last_processed_index + 1) - ((last_processed_index + 1) % rows_per_file)
if (last_processed_index + 1) % rows_per_file == 0:  # If exactly at the end of a chunk, start new chunk
    chunk_start_index = last_processed_index + 1


for index, row in df.iterrows():
    if index <= last_processed_index:  # Skip already processed songs
        continue

    url = row[5]  # Assuming the URL is in the 6th column
    lyrics = get_lyrics_from_url(url)
    df.at[index, 'Lyrics'] = lyrics
    
    # Update the current chunk's output file every 500 songs
    if (index - chunk_start_index + 1) % update_frequency == 0 or (index + 1) % rows_per_file == 0:
        interim_output_path = os.path.join(f'Song_names_with_lyrics_interim_part{part_counter+1}.csv')
        df.iloc[chunk_start_index:index+1].to_csv(interim_output_path, sep=';', index=False, quotechar='"', encoding='utf-8')
        print(f"Updated {interim_output_path} with songs up to index {index+1}.")
        update_checkpoint(index, part_counter)
    
    # Save and start a new file every 1000 rows, resetting the chunk start index
    if (index + 1) % rows_per_file == 0:
        part_counter += 1
        final_output_path = os.path.join(f'Song_names_with_lyrics_not_found_part{part_counter}.csv')
        df.iloc[chunk_start_index:index+1].to_csv(final_output_path, sep=';', index=False, quotechar='"', encoding='utf-8')
        print(f"Saved {final_output_path}")
        os.remove(interim_output_path)
        print(f"Deleted the temporary file {interim_output_path}")
        chunk_start_index = index + 1

# Save any remaining rows not yet saved in the last chunk
if (index - chunk_start_index + 1) > 0:
    part_counter += 1
    remaining_output_path = os.path.join(f'Song_names_with_lyrics_part{part_counter}.csv')
    df.iloc[chunk_start_index:index+1].to_csv(remaining_output_path, sep=';', index=False, quotechar='"', encoding='utf-8')
    print(f"Saved remaining songs to {remaining_output_path}")
    update_checkpoint(index, part_counter)

os.remove(checkpoint_file) # Cleanup checkpoint file after successful completion
print("Processing complete.")