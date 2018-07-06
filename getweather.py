import feedparser
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

RSS_FEEDS = {'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
             'cnn': 'http://rss.cnn.com/rss/edition.rss',
             'fox': 'http://feeds.foxnews.com/foxnews/latest',
             'iol': 'http://www.iol.co.za/cmlink/1.640'}

@app.route("/", methods=['GET', 'POST'])
def get_news():
    weather = get_weather("London,UK")
    return render_template("weather.html", articles=feed["entries"], weather=weather)

if __name__ == '__main__':
    app.run(port=5000, debug=True)