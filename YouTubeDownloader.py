from pytube import YouTube


def videoDownloader(url, quality):
    yt = YouTube(url)

    print("Video initializing...")
    print("Title: ", yt.title)

    downloader = yt.streams.filter(res=f"{quality}p").first()

    if downloader:
        print("Calculating size...")
        print(f"Size: {downloader.filesize / (1024*1024):.2f} MB")
        print("Download Started...")
        print("Please wait to finish...")
        print("Kill the terminal to stop downloading!")

        downloader.download(output_path="YouTubeDownloads")

        print("Successfully Downloaded!")
        print("Please find the video in the folder: 'YouTubeDownloads'")
    else:
        print(f"Error: {quality}p video not found.")


if __name__ == "__main__":
    url = input("Enter the URL : ")
    quality = int(input("Enter the required resolution : "))

    videoDownloader(url, quality)
