
# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd



# Set the executable path and initialize Splinter
executable_path = {"executable_path": ChromeDriverManager().install()}
browser = Browser("chrome", **executable_path, headless=False)


# Visit the mars nasa news site
url = "https://redplanetscience.com"
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css("div.list_text", wait_time=1)



# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, "html.parser")
slide_elem = news_soup.select_one("div.list_text")

slide_elem.find("div", class_="content_title")


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find("div", class_="content_title").get_text()



# Use the parent element to find the paragraph text
news_p = slide_elem.find("div", class_="article_teaser_body").get_text()


# ### Featured Images


# Visit URL
url = "https://spaceimages-mars.com"
browser.visit(url)


# Find and click the full image button
full_image_elem = browser.find_by_tag("button")[1]
full_image_elem.click()


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, "html.parser")



# Find the relative image url
img_url_rel = img_soup.find("img", class_="headerimage fade-in").get("src")


# Use the base URL to create an absolute URL
img_url = f"https://spaceimages-mars.com/{img_url_rel}"


# ## Mars Facts

df = pd.read_html("https://galaxyfacts-mars.com")[0]
df.columns=["description", "Mars", "Earth"]
df.set_index("description", inplace=True)




df.to_html()


# ## D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres

# 1. Use browser to visit the URL 
url = "https://marshemispheres.com/"
browser.visit(url)


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
# Parse the resulting html with soup

html = browser.html
home_soup = soup(html, "html.parser")
results = home_soup.find_all("div", class_="item")

#To get the image tag for the hemisphere images 
#(after "inpect" ing the image tag that corresponds to the image in question appears at the 4th position (0,1,2,3))
#So i =3
i = 3
for result in results:
    hemispheres = {}
    # Find and click the full image
    full_image_elem = browser.find_by_tag('img')[i]
    full_image_elem.click()
    # Parse the resulting html with soup
    html = browser.html
    img_soup = soup(html, "html.parser")
    img_url_rel = img_soup.find('ul').find('li').find('a')['href']
    full_image_url  = f"{url}{img_url_rel}"
    title = img_soup.find("div", class_="cover").h2.get_text().strip()
    hemispheres["img_url"] = full_image_url
    hemispheres["title"] = title
    hemisphere_image_urls.append(hemispheres)
    browser.back()
    i += 1



# 4. Print the list that holds the dictionary of each image url and title.
print(hemisphere_image_urls)




#Quit the browser
browser.quit()

