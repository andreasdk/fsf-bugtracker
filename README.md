[![Build Status](https://travis-ci.org/andreasdk/fsf-bugtracker.svg?branch=master)](https://travis-ci.org/andreasdk/fsf-bugtracker)

![Django](https://img.shields.io/badge/django-2.2.6-092E20) ![Python](https://img.shields.io/badge/python-3.6.8-%2333AAFF)

# [Bug Tracker](https://bugtracker-fsf.herokuapp.com/)

<img src="#" alt="Bug Tracker Home Page" width="800">

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
    - [**Acknowledgements**](#acknowledgements)

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


### Features Left to Implement


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


### Compatibility


### Validators

**HTML**
- [W3C HTML Validator](https://validator.w3.org) - WC3 does not understand the Jinja templating language, so throws up errors for that. Other than the Jinja errors, the code is validated.


**CSS**
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) - WC3 does not recognize CSS variables, and also threw up errors for some -webkit pseudo element selectors. The rest of the CSS validates without error.


**JavaScript**


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

### Acknowledgements

##### back to [top](#table-of-contents)