import os

import requests
from flask import Flask, send_file, Response
from bs4 import BeautifulSoup

app = Flask(__name__)


def get_fact():

    response = requests.get("http://unkno.com")

    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")

    return facts[0].getText()


@app.route('/')
def home():
    the_fact = get_fact()
    data = {"input_text":the_fact}
    response = requests.post("https://hidden-journey-62459.herokuapp.com/piglatinize/", data=data)
    display_text = response.content.decode()
    replacement_text = f'<br><a href="{response.url}">{response.url}</a></body>'
    new_display_text = display_text.replace("</body>", replacement_text)
    return new_display_text


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)

