# FinalProject - Short-term Rentals Search
An application searches the potential short-term rentals near schools in the City of Calgary

## Instructions
**1. Initialization:**
  run the flask in your CMD

     set FLASK_APP=app.py

     set DATABASE_URL=postgres://wuovjxqrbkjvoq:e6efef85f6352e007cb1be099191ce544516f7286535d13e71e8e7b16d34e2e4@ec2-34-239-33-57.compute-1.amazonaws.com:5432/d1s2dtpanknqv3

     flask run 
  copy and paste the http link to your browser.

**2. Filter School:**
Enter the name of School that you are interested in at the Search box. If you are not sure what to enter, click the layer and check the school name. Choose your distance and enter into the "Enter Search Radius" box and click Search button. More details can be found by clicking the Residences layers.

**3. Routing:**
  Enter the school name to search for the directions of any locations near the selected school.

**4. RESTful api:**
  By adding "/api/<string: business id of Residences>" to the end of Url will move
  you to the Residences layer.
***
## Files

### app.py
An application file that contains all the .html pages.

### index.html
The start-up page that contains the leaflet map with school layers. Routing and Filter School functions are available in the Navbar.

### result.html
The Filter School result page that displays all Residences layers. Euclidean distance can be measured using draw button.

### routing.html
The direction page using *leaflet routing machine* plugin to dispaly the routes between two locations.

### static/
Folders for layer icons.
