import requests
from bs4 import BeautifulSoup

def scrape_video_url(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        
        # Check if request was successful
        if response.status_code == 200:
            # Parse HTML content
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Find the video tag
            video_tag = soup.find('video')
            
            # Extract the URL from the data-src-url attribute
            if video_tag:
                video_url = video_tag.get('data-src-url')
                if video_url and video_url.startswith("//s2.krakenfiles.com/video/uploads/"):
                    return "https:" + video_url
                
            # If video tag or valid URL not found, return None
            return None
            
        else:
            # If request was unsuccessful, print error message
            print("Failed to retrieve webpage:", response.status_code)
            return None
        
    except Exception as e:
        print("An error occurred:", e)
        return None

# Example usage
if __name__ == "__main__":
    url = "https://krakenfiles.com/view/6NyeH6D4G6/file.html"  # Replace with the URL of the webpage you want to scrape
    video_url = scrape_video_url(url)
    if video_url:
        print("Video URL found:", video_url)
    else:
        print("Video URL not found.")
