def API_loop():

    import requests
    from PIL import Image

    import urllib.request
    import json

    url = "https://thatcopy.pw/catapi/rest/"
    print(url)

    response = requests.get(url)
    result = response.json()
    picture = result['webpurl']
    #######
    filename ="cat_pic.png"
    urllib.request.urlretrieve(picture, filename)
    image = Image.open(filename)
    #image.show()

#API_loop()
