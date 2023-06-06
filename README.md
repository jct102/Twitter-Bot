# Twitter-Bot
A Twitter bot created using the NASA Mars Rover Photo's API, Twitter API, and the Tweepy library

Link to Twitter bot: https://twitter.com/RoverImagesBot

# How It's Made
Tech used: Python, Twitter API, NASA Mars Rover Photo's API, Tweepy library

The program generates a random Mars sol day and gets JSON data from the API endpoint. It then parses through the data to find the photo and saves it as a temporary JPEG. Using the Tweepy library,
the program authenticates the user's Twitter information and uploads the image along with it's corresponding data to the user's account. After the tweet has been successfully published, a link
to it is printed in the terminal window.
