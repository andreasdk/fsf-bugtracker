[![Build Status](https://travis-ci.org/andreasdk/fsf-bugtracker.svg?branch=master)](https://travis-ci.org/andreasdk/fsf-bugtracker)

![Django](https://img.shields.io/badge/django-2.2.6-092E20) ![Python](https://img.shields.io/badge/python-3.6.8-%2333AAFF)

# [Bug Tracker](https://bugtracker-fsf.herokuapp.com/)
I chose to build an issue tracker in Django as the full-stack project assessment at Code Institute. The idea behind this project was to deliver a website where users of a fictional product can create bug reports and make new feature requests. Each report and request can be voted for by users to indicate they either have or support this issue. Voting for bugs is free, but voting for features costs a fee. Users can also leave comments under each report and request. Each bug and feature can be set by admin to a different status (New, In Progress, Closed, Completed) so users can follow progress and have a resolution to their posts.
---

## Table of Contents
1. [**UX**](#ux)
    - [**User Stories**](#user-stories)
    - [**Design**](#design)
        - [**Framework**](#framework)
        - [**Color Scheme**](#color-scheme)
        - [**Icons**](#icons)
        - [**Typography**](#typography)
    - [**Wireframes**](#wireframes)

2. [**Features**](#features)
    - [**Existing Features**](#existing-features)
    - [**Features Left to Implement**](#features-left-to-implement)

3. [**Technologies Used**](#technologies-used)
    - [**Libraries**](#Libraries)
    - [**Front-End Technologies**](#front-end-technologies)
    - [**Back-End Technologies**](#back-end-technologies)

4. [**Testing**](#testing)
    - [**Validators**](#validators)
    - [**Compatibility**](#compatibility)
    - [**Known Issues**](#known-issues)

5. [**Deployment**](#deployment)
    - [**Local Deployment**](#local-deployment)
    - [**Remote Deployment**](#remote-deployment)

6. [**Credits**](#credits)
    - [**Content**](#content)
    - [**Media**](#media)
    - [**Code**](#code)

---

## UX

This project is the assessment of the Django modules for the Full Stack Software Development degree at [Code Institute](https://codeinstitute.net/). I chose to create a web application that allows users to create bug reports and request new features. Each user should be able to  **C**reate, **R**ead, **U**pdate, and **D**elete (**CRUD**) their own bugs or feature requests. Users can also leave comments on each bug and feature request, upvote bugs for free and features for a fee.

### User Stories

"**As a user, I want:**"
- *to view the site* on my preferred device (mobile, tablet, desktop).
- *to create my own account*
- *to update my profile picture*
- *to create bug reports/feature requests*
- *to edit my own bug reports/feature requests*
- *to delete my own bug reports/feature requests*
- *to upvote bugs free of charge*
- *to upvote features for a fee*
- *to view feature upvotes in a cart*
- *to pay for feature upvotes*.


### Design

This site was built using Bootstrap, as well as refactored designs I used in my previous milestone projects.
#### Framework

- [Bootstrap 4.3.1](https://getbootstrap.com//)
    - I chose Bootstrap for its ease of use, its minimal use of classes compared to other front-end libraries, and its ability to be easily customized.
- [jQuery 3.3.1](https://code.jquery.com/jquery/)
    - I am using the version of jQuery recommended with Bootstrap for features like the navbar.
- [Django 2.2.6](https://www.djangoproject.com/)
    - I've used the Python framework to create apps, routes, functions and templates for the back-end of the website.


#### Color Scheme

I used a charcoal color for the navbar and header, and then a mid green color (#57ba98) as the primary color for headings, buttons, and backgrounds. My goal was to use different tones of one color as the primary colors so that the overall design is cohesive.

- ![#57BA98](https://placehold.it/15/57BA98/57BA98) `#57BA98` (**mid-green** - *primary-color*)
- ![#65CCB8](https://placehold.it/15/65CCB8/65CCB8) `#65CCB8` (**light green** - *primary-color-light*)
- ![#3B945E](https://placehold.it/15/3B945E/3B945E) `#3B945E` (**dark green** - *primary-color-dark*)
- ![#ff0000](https://placehold.it/15/ff0000/ff0000) `#ff0000` (**red** - *secondary-color*)
- ![#f7f7f7](https://placehold.it/15/f7f7f7/f7f7f7) `#f7f7f7` (**light grey** - *grey-color-light-1*)
- ![#777](https://placehold.it/15/777/777) `#777` (**dark grey** - *grey-color-dark-1*)
- ![#999](https://placehold.it/15/999/999) `#999` (**dark grey** - *grey-color-dark-2*)
- ![#333](https://placehold.it/15/333/333) `#333` (**charcoal grey** - *grey-color-dark-3*)
- ![#fff](https://placehold.it/15/fff/fff) `#fff` (**white** - *white-color*)


#### Icons
- [Font Awesome](https://fontawesome.com/)
    - I used Font Awesome icons for the navbar and footer. I used them in the navbar to give a visual clue as to what page each link leads to. In the footer, the icons direct to my GitHub and LinkedIn accounts. I also used icons in card, to display votes, views, and remove from cart button.


#### Typography

- I specified two fonts from [Google Fonts](https://fonts.google.com/) in my CSS variables. Roboto Condensed is used as the primary font of the website, and Cabin is used paragraphs and form labels. I chose only two so that the website content would be easily readable.
    - [Roboto Condensed](https://fonts.google.com/specimen/Roboto+Condensed)
    - [Cabin](https://fonts.google.com/specimen/Cabin)



### Wireframes


##### back to [top](#table-of-contents)


---

## Features

### Existing Features

**Navbar**
- The navbar is displayed on the homepage, bugs page, features page, single bug/feature page, cart, checkout, and the profile page. In its logged out state, it displays links to the home page, the bugs page, features page, the login page, and the register page. Each link has an icon to give a visual clue as to the linked page content. On desktop,
the links have a hover effect which causes the background and text color to invert via a right side sliding animation. On smaller tablet and mobile screens, the navbar is accessed via a toggler and the nav links are centred.

- Visitors who are not logged in, or who have no account see the following navbar links.
    1. Home
    2. Bugs
    3. Features
    4. Login
    4. Register 

- Logged in users see the following navbar links.
    1. Home
    2. Bugs
    3. Features
    4. Cart
    5. Profile
    6. Logout

**Account Registration**
- A user can register an account by creating a username and a password, and inputting an email address. The username input field has a red bottom border while unvalidated, which changes to the primary color (#57BA98) when validated. The same validation style applies to the password fields, which must match in order for a registration to be successful. If the username is not unique or the passwords do not match, the website will redirect to the register page, and a flash message appears to guide the user. This page does not have a navbar, but can be closed by clicking the close icon in the top right corner. This redirects to the homepage.

**Account Login**
- A user can  log in to their account by inputting their username and password. The username input field has a red bottom border while unvalidated, which changes to the primary color (#57BA98) when validated. The same validation style applies to the password field. Validation in the login form means that both fields must be filled in. If the user inputs the wrong username and/or password, they are redirected back to the form. A flash message appears to give them feedback about why login was not successful. This page does not have a navbar, but can be closed by clicking the close icon in the top right corner. This redirects to the homepage.

**Account Logout**
- When a user logs in, the login and registration links no longer appear on the navbar. Instead, the user sees links to their cart, their profile page, and to log out. On clicking logout, the session is ended and the user is redirected to the homepage.


**View All Bugs**
- On the bugs page, bug cards are displayed from oldest to most recent. There is pagination, with a limit of 8 bugs per page. A user can click on a bug card to be directed to the individual bug report page.


**View All Features**
- On the features page, feature cards are displayed from oldest to most recent. There is pagination, with a limit of 8 features per page. A user can click on a feature card to be directed to the individual feature request page.

**View A Single Bug**
- A user can click on a bug card from the the bugs page to access a single bug report. A bug report displays the bug title, description, author, ID number, views, and votes. There is also a comment section below each bug report, and bug authors can see edit and delete buttons on this page. A user can vote for a bug here free of charge.

**View A Single Feature Request**
- A user can click on a feature card from the the features page to access a single feature request. A feature requesr displays the feature title, description, author, ID number, views, and votes. There is also a comment section below each feature request, and request authors can see edit and delete buttons on this page. A user can vote for a request here for a 10 euro fee.


**Create A Bug Report**
- A logged in user is able to create a bug report by clicking on the 'Add Bug' link on the Bugs page. They are then invited to fill in a form with the relevant bug data.

**Edit A Bug Report**
- A logged in user who is also the bug author is able to edit a bug report by clicking on the 'Edit' button on the specific bug page. They are then invited to fill in a form with the relevant bug data.

**Create A Feature Request**
- A logged in user is able to create a feature request by clicking on the 'Add Feature' link on the Features page. They are then invited to fill in a form with the relevant data.

**Edit A feature request**
- A logged in user who is also the request author is able to edit a feature request by clicking on the 'Edit' button on the specific feature page. They are then invited to fill in a form with the relevant data.

**Cart**
- A logged in user can vote for feature requests, which is then added to their cart. In the cart, they can view the contents and delete items. There is a link to the checkout.

**Checkout**
- A logged in user can proceed to the checkout, where they can see a summary of their order and the total price. They are invited to fill out a personal info form and a card info form. Upon submit, their order is either validated and the votes are added to the corresponding features or the payment fails and they are redirected back to the checkout. 



### Features Left to Implement

Due to time constraints, there are some additional features I wasn't able to implement.

**Bug/Feature Type**
- I think that in their current state, the bug and feature apps have a lot of similar code. I would like to make it more DRY by using one app instead, and a user can select whether they are creating a bug or a feature request

##### back to [top](#table-of-contents)

---

## Technologies Used
- [Git](https://git-scm.com/) Used for version control of project code.
- [GitHub](https://github.com/) - Used to remotely store project code.
- [VS Code](https://code.visualstudio.com/) - The IDE I used for developing this project.


### Libraries
- [Bootstrap 4.3.1](https://getbootstrap.com/) Used for its responsive design framework.
- [JQuery 3.4.1](https://jquery.com) Used for simplified DOM manipulation.
- [Google Fonts](https://fonts.google.com/) Used to import custom fonts.
- [FontAwesome](https://fontawesome.com/) For the icons used through the Bug Tracker website.

### Front-End Technologies
- [HTML](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5) - Used to write markup text.
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS3) - Used to create custom styles.
- [Stripe](https://stripe.com/docs/api) - Used to process feature vote payments.
- [AWS S3](https://aws.amazon.com/) - Used to host static and media folders and files as they cannot be hosted on Heroku

### Back-End Technologies
- **Python**    
    - [Python 3.6.8](https://www.python.org/) - Used as the back-end programming language.

- **Django**
    - [Django 2.2.6](https://www.djangoproject.com/) - To create the various apps that make up this website.
    
- **Heroku**
    - [Heroku](https://www.heroku.com) - This app is hosted via Heroku.

- **PostgreSQL**
    - [Heroku](https://www.postgresql.org/) - PostgreSQL is used as the relation database   


##### back to [top](#table-of-contents)

---

## Testing

In addition to automated tests, I manually tested the website with debugger.

**User Registration**
I created my own account and tested website features with it. I can log in, update my email and profile image, add, edit, and delete my own tests and features. I also made test accounts to see if it was possible to delete or edit another user's recipes from another account.

**Add A Bug/Feature**
I made dummy bug reports and feature requests to test the create functions. I attempted to submit the forms without some required fields, but it wasn't possible.

**Update A Bug/Feature**
I tested a number of bug reports and feature requests to make sure the edit functions were working correctly. When the form is successfully validated, the bug reports and feature requests update with the new data.

**Delete A Bug/Feature**
I tested the delete function on dummy bug reports and feature requests, and it removes the selected bug reports and feature requests from the database as well as all related data.

**Read A Bug/Feature**
Individual bug reports and feature requests were tested by clicking on the bug and feature cards. The bug and feature data is successfully displayed on screen. The votes, views, author, status and ID are all displayed. The comment section also displays comments, and accepts new ones.

**Profile Page**
The account page successfully shows user details such as username and join date. Users can successfully update their email and profile image here.

**Cart**
I viewed the empty cart, and it shows as empty with a link to view features. I added feature votes to the cart, and they are displayed there and can be removed as well.

**Checkout**
I used the Strip test card number to fill in the payment form, and a successful payment results in votes to be added to the corresponding features. 

### Compatibility

I tested across a range of browsers using [BrowserStack](https://www.browserstack.com/). 

- Chrome *v.74*
- Edge *v.18*
- Firefox *v.67*
- Safari *v.12* (Mojave)
- Opera *v.62*
- Internet Explorer *v.11*

I also tested responsiveness using a Lenovo Yoga in laptop and tablet mode, as well as on a Huawei P20 phone. The website renders poorly on Internet Explorer, but renders as intended on modern browsers. I noticed a play button appeared in the homepage header video in iOS, so I set a bg-image for the video container in case the video didn't render.

### Validators

**HTML**
- [W3C HTML Validator](https://validator.w3.org) - WC3 does not understand the Jinja templating language, so throws up errors for that. Other than the Jinja errors, the code is validated.


**CSS**
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) - WC3 does not recognize CSS variables, and also threw up errors for some -webkit pseudo element selectors. The rest of the CSS validates without error.


**JavaScript**
- [JSHint](https://jshint.com/) 
  - **stripe.js**:
        - METRICS:
            - There are 3 functions in this file. Function with the largest signature take 2 arguments, while the median is 0. Largest function has 11 statements in it, while the median is 4. The most complex function has a cyclomatic complexity value of 2 while the median is 1.
        - UNDEFINED VARIABLES:
            - `Stripe`
            - `$`
    - **scripts.js**:
        - METRICS:
            - There is only one function in this file. It takes no arguments. This function contains only one statement. Cyclomatic complexity number for this function is 1.
        - UNDEFINED VARIABLES:
            - `$`


### Automated Testing

I used Django's testing framework to carry out 27 tests on app forms, models and views. Tests can be run with the following command:
    - `python manage.py test`

I also used Travis CI to test continuous integration. I found this very useful as sometimes builds would fail and the log helped me pinpoint where the error was.

In addition to those, I also used coverage to find out the overall coverage of my tests, and it currently reaches 73%.

<details>
<summary>Clickto expand the full <b>Coverage Report</b></summary>

| **Name** | **Stmts** | **Miss** |  **Cover** |
| :--- | ---: | ---: | ---: |
| *accounts/__init__.py* | 0 | 0 | **100%** |
| accounts/admin.py* | 1 | 0 | **100%** |
| accounts/apps.py*  | 3 | 3 | **0%** |
| accounts/forms.py* | 42 | 2 | **95%** |
| *accounts/models.py* | 14 | 1 | **93%** |
| *accounts/tests.py* | 65 | 0 | **100%** |
| *accounts/urls.py | 4 | 0 | **100%** |
| *accounts/urls_reset.py | 4 | 0 | **100%** |
|accounts/views.py* | 61 | 39 | **36%** |
| *bugs/__init__.py* | 0 | 0 | **100%** |
| *bugs/admin.py* | 45 | 0 | **100%** |
| *bugs/apps.py*   | 3 | 3 | **0%** |
| *bugs/forms.py*  | 13 | 0 | **100%** |
| *bugs/models.py* | 13 | 3 | **90%** |
| *bugs/tests.py*  | 45 | 0 | **100%** |
| *bugs/urls.py*  | 3 | 0 | **100%** |
| *bugs/views.py* | 83 | 54 | **35%** |
| *cart/__init__.py* | 0 | 0 | **100%** |
| *cart/admin.py* | 1 | 0 | **100%** |
| *cart/apps.py*  | 3 | 3 | **0%** |
| *cart/contexts.py* | 13 | 4 | **69%** |
| *cart/models.py* | 1 | 0 | **100%** |
| *cart/tests.py*  | 18 | 0 | **100%** |
| *cart/urls.py* | 3 | 0 | **100%** |
| *cart/views.py* | 21 | 14 | **33%** |
| *checkout/__init__.py* | 0 | 0 | **100%** |
| *checkout/admin.py* | 7 | 0 | **100%** |
| *checkout/apps.py*  | 3 | 3 | **0%** |
| *checkout/forms.py* | 14 | 0 | **100%** |
| *checkout/models.py* | 19 | 2 | **89%** |
| *checkout/tests.py* | 1 | 0 | **100%** |
| *checkout/urls.py*  | 2 | 0 | **100%** |
| *checkout/views.py* | 43 | 32 | **26%** |
| *custom_storages.py* | 6 | 0 | **100%** |
| *features/__init__.py* | 0 | 0 | **100%** |
| *features/admin.py | 4 | 0 | **100%** |
| *features/apps.py*  | 3 | 3 | **0%** |
| *features/forms.py* | 13 | 0 | **100%** |
| *features/models.py* | 27 | 2 | **93%** |
| *features/tests.py* | 45 | 0 | **100%** |
| *features/urls.py*  | 3 | 0 | **100%** |
| *features/views.py* | 74 | 46 | **38%** |
| *main/__init__.py* | 0 | 0 | **100%** |
| *main/settings.py* | 46 | 2 | **96%** |
| *main/urls.py*  | 14 | 2 | **86%** |
| *main/views.py* | 3 | 0 | **100%** |
| *main/wsgi.py*  | 4| 4 | **0%** |
| :--- | ---: | ---: | ---: |
| **TOTAL** | **829**  | **224** | **73%** |

</details>


##### back to [top](#table-of-contents)

---

## Deployment

### Local Deployment

I developed this project using a virtual environment, and would recommend it.

To run this project locally, you need the following:
- An IDE. I used [Visual Studio Code](https://code.visualstudio.com/) but you are free to use one of your choice.

The following **must be installed** on your machine:
- [PIP](https://pip.pypa.io/en/stable/installing/)
- [Python 3](https://www.python.org/downloads/)
- [Git](https://git-scm.com/)

### Instructions
- Save a copy of this GitHub repository by clicking the 'Clone or download' button at the top of the page, then on 'Download ZIP'. Extract the ZIP file to the folder you will be working in. Alternatively, if you have Git installed locally, you can clone the repository with the following command:
    - `git clone https://github.com/andreasdk/fsf-bugtracker.git`.
- Open a terminal window and change directory (cd) to the directory you extracted the files to.
- Create a **env.py** file with your credentials (SECRET_KEY for example)
- Install all required modules with the command:
    - `sudo -H pip3 -r requirements.txt`
- In a terminal window, with the virtual environment running and from the src folder, run the following command:
    - `python manage.py runserver`
- You should now be able to view the website in browser on localhost (http://127.0.0.1:8000 )
- Then you need to run migrations on the app models:
    - `python manage.py makemigrations`
    - `python manage.py migrate`
- To access the admin panel, you must create an admin user:
    - `python manage.py createsuperuser`



### Remote Deployment

The app can be deployed via [Heroku](https://www.heroku.com/). To deploy, you need to do the following:
- In the terminal from the src directory, create a `requirements.txt` file using the command `pip freeze > requirements.txt`.
- In the terminal from the src directory, create a `Procfile` by running the `echo web: gunicorn main.wsgi:application > Procfile` command.
- Create a new app on [Heroku dashboard](https://dashboard.heroku.com/apps), give it a name and set the region to whichever is closest to you.
- On the Heroku website, navigate to *Resources* , then *Add-Ons*, and search for *Heroku Postgres*. Once selected , update your *env.py* with the postgres database credentials:
    - os.environ.setdefault("DATABASE_URL", "DATABASE_URL_GOES_HERE")
- Navigate to*Settings* on Heroku,  and click on *Reveal Config Vars*. Here, you must enter all the values from your *env.py* file.
- As this project is in a subdirectory, you can deploy it to Heroku using the following commands:
    - `npm install -g heroku`
    - `heroku login`
    - `heroku git:remote -a my-app` (in this case, my-app is the name of your Heroku project)
- Then navigate to the root project folder and run
    - `git subtree push --prefix src heroku master`
- The static and media folders cannot be hosted on Heroku, so you must host this via [Amazon AWS](https://aws.amazon.com/) You need to create a unique bucket for this project from the *S3 buckets* section.
- You will also need to sign up for a [Stripe](https://stripe.com) account to process the payment functionality of the checkout app. Navigate to the *Developers* section, then to *API KEYS*.
Update your *env.py* file with those values.
    - os.environ.setdefault("STRIPE_PUBLISHABLE", "STRIPE_PUBLISHABLE_GOES_HERE")
    - os.environ.setdefault("STRIPE_SECRET", "STRIPE_SECRET_GOES_HERE")
- It should now be possible to launch the app via Heroku.

##### back to [top](#table-of-contents)

## Credits

### Content


### Media

The website images were taken from the following sources:

- **Index page images** : [Unsplash](https://unsplash.com/)
- **Default profile pic** : [Google Image Search](https://static2.scirra.net/avatars/256/631b148a2bab5d3a41ac79151b83674e.png)


### Code

- **Navbar animation, user registration form styles, heading styles, utilities styles** [Jonas Schmedtman Advanced CSS & Sass](https://www.udemy.com/advanced-css-and-sass)
- **Try Django 2.2** - [CodingEntrepreneurs](https://www.youtube.com/watch?v=-oQvMHpKkms)
- **Profile Image Model, Profile Update Model** - [Corey Schafer](https://github.com/CoreyMSchafer/code_snippets/blob/master/Django_Blog/09-Update-User-Profile/django_project/users/models.py)
- **Comment form and section** - [Daniel MV](https://codepen.io/danmv/pen/VBVKOV)
- **Pagination** - [simpleisbetterthancomplex.com](https://simpleisbetterthancomplex.com/tutorial/2016/08/03/how-to-paginate-with-django.html)
- **Unique User Voting** - [Code Institute Slack](https://code-institute-room.slack.com/files/U9BLGCDQU/FHQSA4ZQD/are_you_managing_votes_or_counting_views_of_a_blog_.py)


##### back to [top](#table-of-contents)