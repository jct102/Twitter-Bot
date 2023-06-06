import tweepy
import random
import requests

access_token = ''
access_token_secret = ''
API_key = ''
API_secret_key = ''
client_id = ''
client_secret = ''

num = random.randint(0, 1000)

rover_params = {
    'sol': num,
    'camera': 'FHAZ',
    'page': 1,
    'api_key': ''
}

auth = tweepy.OAuth1UserHandler(API_key, API_secret_key)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


def twitter_auth():
    client = tweepy.Client(
        consumer_key=API_key, consumer_secret=API_secret_key,
        access_token=access_token, access_token_secret=access_token_secret
    )
    return client


def rover_auth():
    request_url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?'
    response = requests.get(request_url, rover_params)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error")


def get_image():
    data = rover_auth()
    image = data['photos'][1]['img_src']
    file_name = 'temp.jpg'
    image_url = image
    image_data = requests.get(image_url).content
    with open('temp.jpg', 'wb') as handler:
        handler.write(image_data)
    media = api.media_upload(file_name)
    return media


def get_data():
    data = rover_auth()
    sol = str(data['photos'][1]['sol'])
    text = "Sol: " + sol
    return text


def tweet():
    client = twitter_auth()
    media = get_image()
    text = get_data()
    response = client.create_tweet(text=text, media_ids=[media.media_id])

    print(f"https://twitter.com/user/status/{response.data['id']}")


tweet()
