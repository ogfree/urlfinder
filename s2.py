import requests
from bs4 import BeautifulSoup

def scrape_video_info(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        
        # Check if request was successful
        if response.status_code == 200:
            # Extract cookies
            cookies = response.cookies

            # Parse HTML content
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Find the video tag
            video_tag = soup.find('video')
            
            # Extract the URL from the data-src-url attribute
            if video_tag:
                video_url = video_tag.get('data-src-url')
                if video_url and video_url.startswith("//s2.krakenfiles.com/video/uploads/"):
                    return video_url, cookies
                
            # If video tag or valid URL not found, return None
            return None, None
            
        else:
            # If request was unsuccessful, print error message
            print("Failed to retrieve webpage:", response.status_code)
            return None, None
        
    except Exception as e:
        print("An error occurred:", e)
        return None, None

def create_html_page(video_url, cookies):
    # Create HTML content with video URL and cookies
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Video Page</title>
    </head>
    <body>
        <h1>Video Page</h1>
        <video controls>
            <source src="{video_url}" type="video/mp4">
            Your browser does not support the video tag.
        </video>
        <p>Cookies:</p>
        <pre>{cookies}</pre>
    </body>
    </html>
    """
    return html_content

# Example usage
if __name__ == "__main__":
    url = "https://krakenfiles.com/view/khgM1Lu5y6/file.html"  # Replace with the URL of the webpage you want to scrape
    video_url, cookies = scrape_video_info(url)
    
    if video_url:
        # Create HTML page with video URL and cookies
        html_page = create_html_page(video_url, cookies)
        
        # Write HTML content to a new file
        with open("video_page.html", "w") as file:
            file.write(html_page)
        
        print("Video URL and cookies extracted and saved to video_page.html.")
    else:
        print("Video URL not found.")
