from flask import Flask
import requests

app = Flask(__name__)

@app.route("/", methods=["GET"])
def get_chuck_norris_jokes():
    api_url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(api_url).json()
    img_url = "<img src =" + response["icon_url"] + " alt = 'chuck_img'>"
    return"<strong>Random joke from chuck norrris:</strong>" + response["value"] + img_url


if __name__ == "__main__":
    app.run()

