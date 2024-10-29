import logging  # Import the logging library for logging messages to a file
from pytubefix import YouTube  # Import the YouTube class from the pytubefix library to handle YouTube videos
from pytubefix.cli import on_progress  # Import the on_progress function for tracking download progress

# Configure logging to write messages to 'logfile.txt' with a logging level of INFO
logging.basicConfig(filename='logfile.txt', level=logging.INFO)

def main():
    input_file = 'videos.txt'  # Define the name of the input file containing the YouTube video URLs
    with open(input_file, 'r') as file:  # Open the input file in read mode
        urls = file.readlines()  # Read all lines from the file into a list

    for url in urls:  # Iterate through each URL in the list
        url = url.strip()  # Remove any surrounding whitespace or newline characters from the URL
        if url:  # Ensure the URL is not empty
            link = url  # Assign the cleaned URL to a variable 'link'
            yt = YouTube(link, on_progress_callback=on_progress)  # Create a YouTube object for the link with a progress callback
            print("Title:", yt.title)  # Print the title of the video
            print("Length of video:", yt.length, "seconds")  # Print the length of the video in seconds
            yt.streams.get_audio_only().download(mp3=True)  # Download the audio stream as an MP3 file
            print("MP3 successfully downloaded from", link)  # Print a success message
            logging.info(f"{yt.title} successfully downloaded")  # Log the success message with the video title

# Entry point of the program; calls the main function if the script is run directly
if __name__ == "__main__":
    main()

