from flask import Flask, render_template, redirect
import pymongo
import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup
import requests
import time

#These funcionts were defined in the python notebook
# I like this one better because I don't have to wait for the browser to open/load

# this user agent is necessary as the python version does not have these classes
request_headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"}

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=True)

def mars_nasa_scrape():
    browser = init_browser()
    listings = {}

    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    
    time.sleep(5)

    listings["headline"] = soup.find("div", class_="content_title").get_text()
    listings["teaser"] = soup.find("div", class_="rollover_description_inner").get_text()
    
    return listings


def jpl_image_scrape():
    browser = init_browser()
    url="https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    JPL_img=soup.find("a", id="full_image")    
    url_path=JPL_img['data-fancybox-href']
    full_url=f"https://www.jpl.nasa.gov{url_path}"
    print(full_url)
    return full_url

def weather_scrape():
    url="https://twitter.com/marswxreport?lang=en"
    response=requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    weather=soup.find("p",class_="tweet-text").get_text()
    weather=weather.split("pic.twitter.com")[0]
    weather=weather.replace("\n", " ")
    print(weather)
    return weather

def mars_wiki():
    pandas_url="https://space-facts.com/mars/"
    mars_facts=pd.read_html(pandas_url)[0]
    mars_facts.columns=["Description", "Value"]
    mars_facts.set_index("Description", inplace=True)
    print(mars_facts.to_html())
    return mars_facts.to_html()

def mars_hamisphere():
    hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg"},
    {"title": "Cerberus Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg"},
    {"title": "Schiaparelli Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg"},
    {"title": "Syrtis Major Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg"},
    ]
    print(hemisphere_image_urls)
    return hemisphere_image_urls

app = Flask(__name__)

# Create connection variable
conn = 'mongodb://localhost:27017'

# Pass connection to the pymongo instance.
client = pymongo.MongoClient(conn)
db = client.mars
collection = db.mars_data

@app.route('/')
def home():
    scraped_data=[]
    scraped_data=list(db.collection.find())
    return render_template("index.html", mars_data=scraped_data)

@app.route('/scrape')
def scrape():
    scraped_data={
        "News": mars_nasa_scrape(),
        "Image": jpl_image_scrape(),
        "Weather": weather_scrape(),
        "Facts" : mars_wiki(),
        "Hemispheres" : mars_hamisphere()
    }
    db.collection.insert_one(scraped_data)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
