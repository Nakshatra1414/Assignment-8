def create_artist_track_csv(input_file, output_file):
    # Read the entire CSV manually
    with open(input_file, "r", encoding="latin-1") as f:
        lines = f.readlines()

    # Extract header row and split by comma
    header = lines[0].strip().split(",")

    # Find the correct column indexes in your dataset
    artist_index = header.index("artist(s)_name")
    track_index = header.index("track_name")

    # Dictionary: artist → set of track names
    artist_tracks = {}

    # Process each row manually
    for line in lines[1:]:
        parts = line.strip().split(",")

        # Skip rows that are malformed
        if len(parts) <= max(artist_index, track_index):
            continue

        artist = parts[artist_index].strip()
        track = parts[track_index].strip()

        # Ensure dictionary entry exists
        if artist not in artist_tracks:
            artist_tracks[artist] = set()

        # Add track to artist's set
        artist_tracks[artist].add(track)

    # Write output CSV manually
    with open(output_file, "w", encoding="latin-1") as out:
        out.write("artist,track\n")

        for artist in artist_tracks:
            for track in artist_tracks[artist]:
                out.write(artist + "," + track + "\n")


# ---- RUN THE FUNCTION ----
create_artist_track_csv(
    r"C:\Users\khush\Downloads\spotify-2023.csv",
    r"C:\Users\khush\Downloads\artist_tracks.csv"
)
