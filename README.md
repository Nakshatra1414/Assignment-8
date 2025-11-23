# Assignment-8
Purpose of the Program

The purpose of this program is to process a large Spotify dataset and generate a new, simplified CSV file that shows each unique artist along with their associated track names. The program is designed for learning and practicing Python data structures such as lists, sets, tuples, and dictionaries, while avoiding all import statements.
By writing the CSV parsing manually, the program reinforces skills in string manipulation, file handling, and data organization.

What the Program Does
Input

The program takes one input file:

A Spotify dataset in CSV format
(example: spotify-2023.csv)

The dataset must contain at least the following columns:

track_name

artist(s)_name

Processing

The program:

Reads the CSV file manually using basic file operations.

Splits each line into fields using string .split(",").

Uses:

a dictionary to store artists,

sets to collect unique track names for each artist,

lists to process lines and headers.

Eliminates duplicate track entries (because sets store each value only once).

Writes all artist–track pairs into a new CSV file.

Output

The program generates one output file:

artist_tracks.csv

This file contains two columns:

artist,track


Each row represents one unique combination of an artist and a track.

How to Use the Program

Place the Spotify dataset in your computer (for example, in Downloads).

Update the file paths in the function call:

create_artist_track_csv(
    r"C:\Users\khush\Downloads\spotify-2023.csv",
    r"C:\Users\khush\Downloads\artist_tracks.csv"
)


Run the Python script.

After execution, go to the folder specified in the output path.
You will find the new file:

artist_tracks.csv


You can open it in Excel, Google Sheets, or any text editor to see each artist and their associated tracks.