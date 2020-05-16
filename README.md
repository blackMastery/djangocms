# Simple e-learning platform with CMS


## Introductions
Content management system (CMS) for an Online learning platforms are a great example of applications where you need to provide tools to generate content with flexibility in mind, it will demonstrator building functionality users to create course content( text, video, audio) and manage the content of the courses in a versatile and efficient manner.


## Setup

`python -m venv env/educa`

`source env/educa/bin/activate`

`git clone https://github.com/blackMastery/djangocms.git`

`cd djangocms`

`pip install -r requirements.txt`

`python manage.py makemigrations`

`python manage.py migrate`

`python manage.py runserver`


# Usage

## Development

Want to contribute? Great!

To fix a bug or enhance an existing module, follow these steps:

- Fork the repo
- Create a new branch (git checkout -b improve-feature)
- Make the appropriate changes in the files
- Add changes to reflect the changes made
- Commit your changes (git commit -am 'Improve feature')
- Push to the branch (git push origin improve-feature)
- Create a Pull Request

## What was Done
- Use model inheritance
- Create custom model fields
- Use class-based views and mixins
- Build formsets
- Manage groups and permissions
- Create a CMS

- Build Rest API
  - Retrieve subjects
  - Retrieve available courses
  - Retrieve course contents
  - Enroll on a course

- Rendering and Caching Content
  - Create public views for displaying course information
  - Build a student registration system
  - Manage student enrollment onto courses
  - Render diverse content for course modules
  - Install and configure Memcached
  - Cache content using the Django cache framework
  - Monitor Memcached using the django-memcache-status




## To-do list:
- Add Channels to your project
- Build a WebSocket consumer and appropriate routing
- Implement a WebSocket client
- Enable a channel layer with Redis
- Make your consumer fully asynchronous


## Technologies
- Postgres
- Django Rest framework
- Django Braces
- django embed video
- memcache
  