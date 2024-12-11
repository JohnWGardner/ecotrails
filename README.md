![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

**Students:** John Gardner  
**Date:** 25/11/2024  
**Cohort:** WECA - Full Stack Software Developer: Skills Bootcamp  
**Project:** Travel Blog: HTML, CSS, Bootstrap, JS, Python, Django

---

# Project Goals

![AgilePlanning](static/images/README/Agile_Planning.jpg)

## 1. Understand the Purpose:

- Provide users with 
- Present information in a straightforward, organized format that is easy to understand and navigate.

## 2. Developer Key Goals:

- Fetch  data and a simple, easy-to-digest .
- Design and implement the webpage using Bootstrap 4.6 for responsiveness and layout.

---

# Features

## 1. Home Page

- A  search form using Bootstrap components, allowing users to input .

- A real-time display of data, 

- A , using Bootstrap cards, showing 



## 2. Additional Features:

- Responsiveness ensured using Bootstrap 4.6, so the app works across various screen sizes.
- Clear navigation and intuitive UI with accessible forms.
- Fetching data dynamically
- Error handling with messages 

---

# UX/UI

## 1. Target Audience

- Users who want 

## 2. User Stories

### Real-time Weather Data

**As a user**, I want to input my city name and get the current weather data so that I can plan my immediate activities.

- **Acceptance Criteria**:
  - User can enter a city name into a search box.
  - Upon submitting, the current weather data for the specified city is displayed.
  - Data includes temperature, weather conditions, humidity, and wind speed.
  - Information updates in real-time.

**As a user**, I want to see the current temperature, so I know how to dress appropriately.

- **Acceptance Criteria**:
  - The temperature is displayed in degrees Celsius.
  - The temperature updates to reflect real-time data.

**As a user**, I want to see the current weather conditions (e.g., sunny, rainy, cloudy), so I can decide if I need an umbrella or sunglasses.

- **Acceptance Criteria**:
  - Weather conditions are displayed using descriptive text and relevant icons.
  - The information updates to reflect real-time conditions.

### 5-day Weather Forecast

**As a user**, I want to see the temperature forecast for the next five days, so I can plan my week ahead.

- **Acceptance Criteria**:
  - The 5-day forecast is displayed upon request.
  - Each day's forecast includes the temperature, weather conditions, humidity, and wind speed.
  - The forecast updates regularly to reflect accurate data.

### Interactive Map

**As a user**, I want to be able to click on a map to select my location, so I can get weather data for that specific point.

- **Acceptance Criteria**:
  - An interactive map is available for users to select their location.
  - Selecting a location on the map updates the weather data to that specific point.

### Integration with Weather API

**As a user**, I want the weather data to update in real-time, so I always have the latest information.

- **Acceptance Criteria**:
  - The site pulls real-time data from a reliable weather API.
  - Data refreshes at regular intervals to ensure accuracy.

**As a user**, I want the weather data to be accurate, so I can rely on the information provided by the site.

- **Acceptance Criteria**:
  - Weather data is sourced from a trusted and reliable weather API.
  - API error handling is implemented to manage data retrieval failures.

### User Interface and Experience

**As a user**, I want the site to be visually appealing, so it's pleasant to use.

- **Acceptance Criteria**:
  - The site's design is clean and modern with weather icons and graphics.
  - Visual elements are aligned and consistent.

**As a user**, I want the weather information to be presented in a clear and easy-to-read format, so I can quickly understand the data.

- **Acceptance Criteria**:
  - Weather data is displayed in a structured and organized manner.
  - Fonts, colors, and layout enhance readability.

**As a user**, I want the site to load quickly, so I don't have to wait long to get the information I need.

- **Acceptance Criteria**:
  - The site is optimized for fast loading times.
  - Performance is regularly monitored and improved.

**As a user**, I want the site to work well on my smartphone, so I can check the weather on the go.

- **Acceptance Criteria**:
  - The site is fully responsive, adapting to various screen sizes.
  - All functionalities work seamlessly on both desktop and mobile devices.

### Site Owner Stories

#### API Integration

**As a site owner**, I want to integrate a reliable weather API, so I can provide accurate weather data.

- **Acceptance Criteria**:
  - The weather API is integrated and functional.
  - API requests are managed efficiently and handle errors gracefully.

#### User Interface

**As a site owner**, I want to design a clean and intuitive interface, so users can easily navigate the site.

- **Acceptance Criteria**:
  - The interface is user-friendly and intuitive.
  - Navigation is straightforward and consistent.

#### Performance and Reliability

**As a site owner**, I want the site to be optimized for speed, so users have a fast experience.

- **Acceptance Criteria**:
  - The site is optimized for quick load times.
  - Regular performance checks and optimizations are in place.

**As a site owner**, I want the site to be reliable and have minimal downtime, so users can access it whenever they need.

- **Acceptance Criteria**:
  - The site is hosted on a reliable platform.
  - Downtime is minimized through regular maintenance and monitoring.

---

# Technologies Used

- **HTML5**: For the basic structure of the app.
- **CSS3**: For layout, color schemes, and basic styles.
- **Bootstrap 4.6**: For responsive layout, styling, and form components.
- **JavaScript (ES6+)**: For the dynamic weather display and API integration.
- **GitHub Pages**: For deployment of the live app.

---

# Design Choices

ERD design:

ecotrails/destinations/models.py - ERD:

+-------------------+                  +-------------------+
| User              |                  | Destination       |
|-------------------|                  |-------------------|
| - id (PK)         |<------------1--->| - id (PK)         |
| - username        |                  | - title           |
| - email           |                  | - slug            |
| ...               |                  | - author (FK)     |
|                   |                  | - continent       |
+-------------------+                  | - country         |
                                       | - content         |
                                       | - created_on      |
                                       | - status          |
                                       | - excerpt         |
                                       | - updated_on      |
                                       +-------------------+
                                                   |
                                                   N
                                                   |
                                                   |
                                                   |
                                                   |
                                       +----------------------+
                                       | Recommendation       |
                                       |----------------------|
                                       | - id (PK)            |
                                       | - user (FK)          |
                                       | - destination (FK)   |
                                       | - place_name         |
                                       | - description        |
                                       | - created_on         |
                                       | - approved           |
                                       +----------------------+
ecotrails/about/models.py - ERD:

+-------------------+
| About             |
|-------------------|
| - id (PK)         |
| - title           |
| - profile_image   |
| - updated_on      |
| - content         |
+-------------------+


## Color Scheme

- bright sunny color scheme used to enhance visual appeal.

## Fonts

- Standard fonts for readability and consistent design.
- Slightly larger, bold fonts for key information to improve visibility.

## Wireframes

- Wireframes were created to design the Travel Blog layout:  
![Home_Wireframe](static/images/README/home.jpg)


---

# Testing

## HTML Validation

- Initial HTML validation was done using the W3C Markup Validation Service.

 ![HTML validation](static/images/README/HTML_Test.jpg)

## CSS Validation

- CSS validation was performed using W3C's CSS Validator.

![CSS validation](static/images/README/CSS_Test.jpg)

## Manual Testing against user story compliance:

| User Story | MoSCoW | Status | CI Criteria | Validation Test |
|---|---|---|---|---|
| Admin: Create a New Blog Post | Must Have | Done | TRUE | TRUE |
| Admin: Edit Blog Posts | Must Have | Done | TRUE | TRUE |
| Admin: Delete Blog Posts | Must Have | Done | TRUE | TRUE |
| Admin: Moderate user comments on posts | Must Have | Done | TRUE | TRUE |
| Admin: Moderate user recommendations for travel | Must Have | Done | TRUE | TRUE |
| User: View list of blog posts | Must Have | Done | TRUE | TRUE |
| User: View an Individual Blog Post | Must Have | Done | TRUE | TRUE |
| User Authentication: register an account | Must Have | Done | TRUE | TRUE |
| User Authentication: log in and log out of account | Must Have | Done | TRUE | TRUE |
| User: Post Comments on a Blog Post | Must Have | Done | TRUE | TRUE |
| User: Delete my Comments on a Blog Post | Must Have | Done | TRUE | TRUE |
| User: Edit my Comments on a Blog Post | Must Have | Done | TRUE | TRUE |
| User: Post my recommendations for travel | Must Have | Done | TRUE | TRUE |
| User: Delete my recommendations for travel | Must Have | Done | TRUE | TRUE |
| User: Edit my recommendations for travel | Must Have | Done | TRUE | TRUE |
| User: View Post Excerpts | Could Have | Done | FALSE | TRUE |
| User: Social Sharing | Could Have | Done | FALSE | TRUE |
| User: browse travel recommendations by categories (continents) | Should Have | Done | FALSE | TRUE |
| User: search blog posts by keywords | Could Have | Not Done | FALSE | FALSE |
| User: e-commerce Integration | Won't Have | Not Done | FALSE | FALSE |
| Admin: Advanced Analytics | Won't Have | Not Done | FALSE | FALSE |

## Criteria met:

- At least one original custom model with associated functionalities, markedly different from those present in the Hello, Django! or Codestar Blog walkthrough projects if they have been used in your project.	Answer = (ecotrails/destinations/models.py) and (ecotrails/about/models.py)
	
- At least one form on the front end, which provides either admin or regular users with CRUD functionality without having to access the admin panel. Answer = (ecotrails/destinations/forms.py) and (ecotrails/blog/forms.py)
	
- At least one UI element on the front end, which allows either admin or regular users to delete records in the database without having to access the admin panel.	Answer = (ecotrails/destinations/templates/destinations/destination_list.html) and (ecotrails/blog/templates/blog/post_detail.html)
	
- Evidence of agile methodologies followed during the development of your project in the GitHub repository.	Answer = ecotrails/static/images/README/Agile Planning.jpg
	
- DEBUG mode set to False.	Answer: DEBUG = False
	
- Working functionality for users to register and log in and out of the application without issues.	Answer = (django.contrib.auth.models import User)
	
- Detailed testing write ups, beyond results of validation tools.	Answer = inc testing against user story compliance

## Accessibility

- Google Lighthouse audit reports an accessibility score of 87%, ensuring users with disabilities can access the site effectively.

## Browser and Device Testing

- Tested on multiple devices and browsers for responsiveness:
  - iPhone
  - Desktop
  - Chrome Developer Tools (simulating various devices)
  - Browsers: Chrome, Edge, and Safari
- Site functioned as expected across all tested platforms.

---

# Bugs


# Deployment

The app was deployed using **GitHub Pages**:

1. In the GitHub repository, navigate to **Settings**.
2. Select **Pages** from the left-hand menu.
3. Choose the **Main Branch** as the source, then save.
4. The page will automatically be published.

- **Live App URL:** [ecotrails App](https://ecotrails-54f65842ae68.herokuapp.com/)

- Agile methodology was used, with early deployment to see every change live, aiding the development process.

---

# Future Enhancements:
- More emphasis on design for leaving travel recommendations, as it doesn't work as well as I would like on a mobile device.

---

# Credits


- **Bootstrap**: For layout, components, and responsive design.
- **Code Institute**: For project templates and guidance.
- **Font Awesome**: For fonts.
- **Favicon**: For favicon image.
- **Freepik**: For hero image.

---
