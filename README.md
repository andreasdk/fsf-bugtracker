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
- [FontAwesome](https://fontawesome.com/) For the icons used through the Whisk Recipes website.

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



**CSS**


**JavaScript**


 ### Known Issues

##### back to [top](#table-of-contents)

---

## Deployment

### Local Deployment


### Instructions


### Remote Deployment


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