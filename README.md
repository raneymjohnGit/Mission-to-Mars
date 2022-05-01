# Mission-to-Mars
For learning Web Scraping with HTML/CSS from Module 10

## Project Overview
Robin's web app is looking good and functioning well, but she wants to add more polish to it. She had been admiring images of Mars’s hemispheres online and realized that the site is scraping-friendly. She would like to adjust the current web app to include all four of the hemisphere images. To do this, you’ll use BeautifulSoup and Splinter to scrape full-resolution images of Mars’s hemispheres and the titles of those images, store the scraped data on a Mongo database, use a web application to display the data, and alter the design of the web app to accommodate these images.

## Resources
- Anaconda, Jupyter notebook, Visual Code
- splinter, BeautifulSoup, ChromeDriverManager, Pandas

## Challenge Overview
Prerequisite:
1.  Download the Mission_to_Mars_Challenge_starter_code.ipynb file and index.html


## Deliverable 1:  Scrape Full-Resolution Mars Hemisphere Images and Titles

Follow the instructions below to complete Deliverable 1.

1.  Use your browser to visit the Mars Hemispheres website to view the hemisphere images..
2.  Create a list to hold the .jpg image URL string and title for each hemisphere image.
3.  Write code to retrieve the full-resolution image URL and title for each hemisphere image. The full-resolution image will have the .jpg extension.
4.  Loop through the full-resolution image URL, click the link, find the Sample image anchor tag, and get the href.
5.  Save the full-resolution image URL string as the value for the img_url key that will be stored in the dictionary you created from the Hint.
6.  Save the hemisphere image title as the value for the title key that will be stored in the dictionary you created from the Hint.
7.  Before getting the next image URL and title, add the dictionary with the image URL string and the hemisphere image title to the list you created in Step 2.
8.  Print the list of dictionary items.
    ![image_name](https://github.com/raneymjohnGit/Mission-to-Mars/blob/main/Resources/hemisphere_image_url.png)
9.  Quit the browser.


## Deliverable 2: Update the Web App with Mars Hemisphere Images and Titles

Follow the instructions below to complete Deliverable 2.

1.  Export the Mission_to_Mars_Challenge.ipynb file as a Python file, and save it as Mission_to_Mars_Challenge.py..
2.  In the def scrape_all() function in your scraping.py file, create a new dictionary in the data dictionary to hold a list of dictionaries with the URL string and 
    title of each hemisphere image..
3.  Below the def mars_facts() function in the scraping.pyfile, create a function that will scrape the hemisphere data by using your code from the              
    Mission_to_Mars_Challenge.py file. At the end of the function, return the scraped data as a list of dictionaries with the URL string and title of each hemisphere image
4.  Run the app.py file, then check your Mongo database to make sure that you are retrieving all of the data.
5.  Modify the index.html file to access your database, and retrieve the img_url and title as you loop through the dictionary in the database using {% for 
    hemisphere in mars.hemispheres %}. The dictionary in the mars hemispheres database is the dictionary that was created from the Hint after Step 3 in Deliverable1.
6.  Run the app.py file, open the index.html file, and click the "Scrape New Data" button.
7.  After you have scraped the data, confirm that your webpage has the full-resolution images and the titles of the four hemisphere
8.  Save your Mission_to_Mars_Challenge.ipynb file, the updated scraping.py file, and the updated index.html file.

    ![image_name](https://github.com/raneymjohnGit/Mission-to-Mars/blob/main/Resources/Mars_Hemispheres1.png)


## Deliverable 3: Add Bootstrap 3 Components

Follow the instructions below to complete Deliverable 2.

1.  Use the Bootstrap 3 grid systemLinks to an external site. examples to update your index.html file so your website is mobile-responsive. Use the DevTools to test 
    the responsiveness of your website.
    -   Click on the Toggle Device Toolbar icon to open the UI that enables you to simulate responsiveness.
    -   Choose a device to test your webpage, as shown in the following image:
        ![image_name](https://github.com/raneymjohnGit/Mission-to-Mars/blob/main/Resources/simulate_responsiveness.png)

2.  Add two other Bootstrap 3 components from this listLinks to an external site.. Examples include:
    -   Styling the "Scrape New Data" button.
    -   Customizing the facts table.
    -   Adding the hemisphere images as thumbnails, like the image below.
        ![image_name](https://github.com/raneymjohnGit/Mission-to-Mars/blob/main/Resources/Mars_Hemispheres2.png)