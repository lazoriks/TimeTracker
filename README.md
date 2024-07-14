# Time Tracker
# Project Introduction

## Title

Time Tracking work hours - Check IN/ Check OUT

## Description

The application is designed to enter working hours. Using the Django framework, we developed models for entering working hours. The main login page. If the user is a superuser, a form for editing users and passwords opens. The Generate report button is also available.
If the user is another and is already in the database, a form opens to enter the login hour or exit hour.

![amiresponsive](https://raw.githubusercontent.com/lazoriks/time_tracking_project/static/images/mush.jpg)

## Link to Live Site

This site was built using [Heroku](https://time-tracking-project-py-e169061c7261.herokuapp.com/)

## User Experience

### First-Time User Experience

Registration and Login: Ensure users can register and log in.
Guided Instructions: Provide instructions on the dashboard or use tooltips to guide the user.
Clear Navigation: Make sure the navigation is intuitive and easy to understand.
Optional: User Registration
If user registration is required, you can add a registration view and template.

### User Stories (PP4 & PP5)

#### 1. User Registration and Authentication

As a first-time user,
I want to be able to register for an account,
So that I can start using the time tracking application.

Acceptance Criteria
* A registration page where I can input my username, email, and password.
* A login page where I can authenticate using my username and password.
* An option to logout of the application.

#### 2. Check IN

As a registered user,
I want to be able to check in,
So that I can record the start time of my work.

Acceptance Criteria
* A dashboard with a "Check In" button.
* Clicking the "Check In" button records the current date and time as the check-in time.
* Confirmation message or visual feedback that my check-in was successful.

#### 3. Check OUT

As a registered user,
I want to be able to check out,
So that I can record the end time of my work and track my work hours.

Acceptance Criteria
* A dashboard with a list of my active sessions.
* An option to check out for each active session.
* Clicking the "Check Out" button records the current date and time as the check-out time.
* Confirmation message or visual feedback that my check-out was successful.
* Calculation of the total time spent based on check-in and check-out times.

#### 4. View Work Sessions

As a registered user,
I want to see a list of all my work sessions,
So that I can review my work history and hours worked.

Acceptance Criteria
* A dashboard displaying a list of all my work sessions in reverse chronological order.
* Each session shows the check-in time, check-out time, and total duration.
* Sessions where I have not yet checked out should have an option to check out.

## Technologies Used

* [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML) was used as the foundation of the site.
* [CSS](https://developer.mozilla.org/en-US/docs/Web/css) - was used to add the styles and layout of the site.
* [CSS Flexbox](https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Flexbox) - was used to arrange items simmetrically on the pages.
* [CSS Grid](https://developer.mozilla.org/en-US/docs/Web/CSS/grid)- was used to make "gallery" and "contact" pages responsive.
* [CSS roots](https://developer.mozilla.org/en-US/docs/Web/CSS/:root) was used to declaring global CSS variables and apply them throughout the project.
* [VSCode](https://code.visualstudio.com/) was used as the main tool to write and edit code.
* [Git](https://git-scm.com/) was used for the version control of the website.
* [GitHub](https://github.com/) was used to host the code of the website.
* [GIMP](https://www.gimp.org/) was used to make and resize images for the README file.
* [Python](python.org) was used to write code.
* [Django](https://www.djangoproject.com/) was used to build application.
* [Postgresql](https://www.postgresql.org/) was used tocreate database.

## Design

### Wireframes

Initial wireframes were created to plan the layout and structure of the site.

### Site Structure

The site follows a one-page structure with distinct sections Login page, Check In/Check OUT page, User managment page.

### Imagery Used

High-quality images are used for the background and section headers.
Relevant icons and images complement the content.

### Colour Scheme

The colour scheme includes shades of green and earthy tones for a professional and cohesive look.

### Typography

Arial and sans-serif fonts for a clean and easily readable interface.

## Features

### Navigation

Clear navigation menu at the top for easy section access.
Each section has a link to its dedicated page for more detailed information.


## Future Features

When learning Javascript, you will add dynamics and actions to the site

## Testing

### Code Validation

HTML and CSS were validated using W3C validators.

![Check HTML](https://raw.githubusercontent.com/lazoriks/Portfolio/main/docs/checkwc.png)

![Check CSS](https://raw.githubusercontent.com/lazoriks/Portfolio/main/docs/checkcss.png)

### Responsiveness

The site is designed to be responsive and tested on various devices.



### Lighthouse Testing

Lighthouse testing ensures optimal performance, accessibility, SEO, and best practices.



### Accessibility Testing

The site follows best practices for accessibility, ensuring inclusivity.

### Manual Testing

Extensive manual testing on different browsers and devices.

### Bugs

#### Bugs Fixed


#### Known Bugs



HTML5, CSS3
FontAwesome for icons

Steps on Deploying, Cloning, and Forking

Include step-by-step instructions for deploying, cloning, and forking the project.

## Deployment

The process we went through to place the project on the hosting platform (Heroku)
* The site was deployed to Heroku pages.


## Credits

### Content and text



### Media

* Open sites and sources of images and emblems(Sorry, I forgot links these pictures;))
* Code institute for the deployment process
* Translated with www.DeepL.com/Translator and Grammarly for Windows

## Acknowledgements

* Special thanks to [Laura Mayock](https://www.linkedin.com/in/laura-mayock/) and Julia Konovalova for the call and conversation that helped me, after the second unsuccessful attempt, to find the strength in the first place and to understand my shortcomings in the project and complete it. 
* Code Institute tutors and Slack community members for their support and help.
