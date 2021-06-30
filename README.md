<h1 align="center">COFFEE CUP COFFEESHOP WEBSITE</h1>

<div align="center">

[View the project here.]( https://ms4-coffee-cup.herokuapp.com/)
</div>

<h2 align="center"><a href="https://ibb.co/zRbcNZz"><img src="https://i.ibb.co/tscf3D9/website.png" alt="website" border="0"></a><h2 align="center">


### **Legend**:
This is a website of **Coffee Cup coffeeshop** – for people who like to drink coffee and want to have everything they need for a good cup of coffee at home.

### Core audience of the website (CA):
-  People who love coffee and brew it at home;
-  People who want to order coffee beans and equipment online.

### Website business goals
*   Increase sales by proposing online shopping for “Coffee Cup” customers;
*   Increase market coverage by launching online sales;
*   Build a “Coffee Cup” brand awareness among the CA representatives;
*   Build a community around “Coffee Cup” brand;

## UX
### User stories:
*	As a **new visitor**, I want to understand what this website about and what its purpose.
*	As a **new visitor**, I want to easily navigate the site to get a content what I need;
*	As a **new visitor**, I want to see a website, which works properly on my device;
*	As a **new visitor**, I want to have an ability browse all products on the site;
*	As a **new visitor**, I want to be able to filter products by categories, sort them by different criteria and search them using keywords;
*	As a **new visitor**, I want to see a modern website with a pleasant colour palette.

*	As an **interested visitor** I want to easily and safely purchase products I need;
*	As an **interested visitor** I want to easily create an account and login using 3rd party profile(ex. Google);
*	As an **interested visitor** I want to see detailed description of the products and read an add comments (for making decision);
*	As an **interested visitor** I want to have an ability to add/edit/delete products in my shopping cart;
*	As an **interested visitor** I want to have an option to save some products to favorites;
*	As an **interested visitor** I want to have a profile page, where I can keep see the history of my orders and other user-related information;

As a **superuser**, I want have an ability to add, edit and remove content and products on/from the website. 

### Design
- Color Scheme:
One of the main task was to make website pleasing to the eye. By this reason the accent were made on the following colors: 
    - ![#ea8b4b](https://via.placeholder.com/15/ea8b4b/?text=+) - `#ea8b4b`
    - ![#f9f8f6](https://via.placeholder.com/15/f9f8f6/?text=+) - `#f9f8f6` 
    - ![#000](https://via.placeholder.com/15/000/?text=+) - `#000`  

- Typorgaphy:
  - There are two fonts used in the website Lato and OpenSans– convenient and frequently used in web design. 
    - The Open Sans font (with Sans Serif in case of fallback) is predominately used for all the headings and subheadings on the website. 
    - The Lato font (with Sans Serif in case of fallback) used text and the main text of the sections. 
### Wireframe
  - [View the website wireframe.](https://drive.google.com/drive/folders/1prBtff-UMab9psUBGXce17aB75zmASO9?usp=sharing)
### Database structure
- Categories
    - name
    - slug
    - category_img
- Products
    - id
    - category (ForeignKey)
    - name
    - slug 
    - description 
    - has_sizes 
    - price 
    - image 
    - favourites
- Users
    - id
    - user
    - phone_number
    - street_address1
    - street_address2
    - town_or_city 
    - county
    - postcode
    - country
- Order
    - order_number
    - user_profile (Foreign key)    
    - full_name 
    - email 
    - phone_number 
    - country
    - postcode 
    - town_or_city 
    - street_address1 
    - street_address2
    - county 
    - date cost                                       
    - order_total                                     
    - grand_total                                    
    - original_shopbag 
    - stripe_pid 
- OrderLineItem
    - order (Foreign key)
    - product (Foreign key)
    - product_size 
    - quantity 
    - lineitem_total
- Review
    - product (Foreign key)
    - user (Foreign key)
    - review_title                              
    - review_body
    - date_added

- **Website summary**
  - Website consist of the following blocks, which available for all users: [Home](https://ms4-coffee-cup.herokuapp.com/), [Shop](https://ms4-coffee-cup.herokuapp.com/products/), [Profile](https://ms4-coffee-cup.herokuapp.com/profile/), [Authentification](https://ms4-coffee-cup.herokuapp.com/accounts/signup/) and [Payment](https://ms4-coffee-cup.herokuapp.com/shopbag/),
    - For user’s comfortable navigation, every page and section inside the pages has a large and perceptible heading.
### The website features are:
- **Navigation bar**
  - The website use customized Bootstrap 5 navigation bar. It is a navbar with a logo placing on the top-left and menu items on the top-right. In the middle of bar search bar located. When browsing the website from mobile devices, menu item list becoming a burger-button with a fall-back list. All items, except profile and cart goes to the list. 
  - For user’s convenient navigation, navigation bar has a fixed position. 
- **Footer**
  - The website use a simple and clear footer with social media icons with *hover   effect* and active links to the social media pages. At the current moment, social media links lead to the home page of the particular social media websites. 
    lso footer includes a dynamic copyright caption. Which updates the year, based on the current date.
- **Authentification**
    - Authentification logic provided by Django allauth package.The visual part was customized according the website design.
    -  Becide the local athentification option user can login using their Google account. 
- **HOME PAGE**
    - Besides navigation bar and footer **Home page** consists of **3 sections**: 
    1. - Bootstrap 5 Carousel. There are 2 slides in carousel. Every slide includes heading and call to action button for convenient navigation to shop and shop categories . 
    2. Categories
        - The Categories section is made with Bootstrap grid system to be concisely and responsive depending on a screen size.  There are a three categories of products that user can find. Every category has a call to action button, which lead to the Shop page and filter all items by chosen category. 
    3. About section
        - The About section is made with Bootstrap grid system to be concisely and responsive depending on a screen size.  The section includes picture and text 
- **SHOP**
    - The shop page can be displayed in the following ways:
    - **All products** (default option). User can see all the products published on the website (retrieve from database and renders on page).
    - **By categories** (when user was redirected to all product page by choosing a particular category on a Home page). In this case only products from the corresponding categories render to the page.
    - The title of the page will be changed as well according the above mentioned.
    Also user can filter shop items by name, category and price using the selector button.   
    **Search**  
    - The search takes a text input, it retrieves all products from the database which have the inputted reference in either the name or description, otherwise it returns the information that nothing found.
- **PRODUCTS**
    - A product section is made with Bootstarp grid system to be concisely and responsive depending on a screen size.  Every item has an image, title, description, price, size (if has), quantity selector and add to bag button. 
    - Beside the basic actions, registerd user can add product to favourites as well as add and edit their comments.
    - ***Superuser (admin)*** can edit and delete (using the specific buttons, seen only for superuser) products and content on the page. For example, using EDIT button user gets an access to the form, where they can edit the product.

- **MY PROFILE**
    - This page renders a dashboard with the information connected to a particular user.
    This page includes following:
        - The main page of the dashboard shows the user information and the number of order they made. 
        - There ae also 3 tabs which display the users "favourites", delivery address and all orders that user made.
    -  Using the manage products option ***Superuser (admin)*** getting a chance to add a new product to the shop.
- **PAYMENT**
    - This section includes 2 main payment blocks:
        - Cart, which getting all the user orders.
        - Checkout, which allows user to add their shipping details and  make a secure payment with stripe.

### Things to implement in future
- Add ability (for registered users) to rate products.
- Add a chatbot on the page.
- connect paypall
- Add more details to product model.

## Technologies used
- **Languages Used:**
  - [HTML5](https://en.wikipedia.org/wiki/HTML5)
  - [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
  - [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
  - [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
    - [Django](https://en.wikipedia.org/wiki/Django_(web_framework)) 
    - [Jinja](https://en.wikipedia.org/wiki/Jinja_(template_engine))
- **Frameworks, Libraries & Programs Used:**
1.	[Bootstrap 5](https://getbootstrap.com/docs/5.0/getting-started/introduction/)
     - Bootstrap was used to assist with the responsiveness and styling of the website.
2.  [Google Fonts](https://fonts.google.com/):
    - Google fonts were used to import fonts into the style.css file which are used on the website.
3.	[Font Awesome](https://fontawesome.com/): 
     - Font Awesome was used to add icons to locations page and footer of the website.
4.	[jQuery](https://jquery.com/):
    - Used throughout the site to target and manipulate HTML elements    
5.	[Git](https://git-scm.com/):
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
6.	[GitHub](https://github.com/):
    - GitHub is used to store the projects code after being pushed from Git. 
7.	[Figma](https://www.figma.com//):
    - Figma was used to create the wireframe.
8.	[GitPod](https://gitpod.io/):
    - GitPod was used as an IDE to develop a project. A project was built on a gitpod template of the Code institute.
9. [Heroku](https://www.heroku.com/)
    - Heroku was used a hosting for the project deployment.
10. [Stripe](https://stripe.com/) 
    - payment system used in the project 
## Testing
All-testing has been documented [Testing.md](https://github.com/slavabdev/ms4-coffeeshop/blob/master/Testing.md)
## Deployment
This project was developed using the GitPod, committed to Git and pushed to [GitHub repository](https://github.com/slavabdev/ms4-coffeeshop/).
- The following GIT commands were used throughout deployment:
```console
    - git status ------ used to check the status of files and any changes made / untracked.
    - git add ------ to stage files ready to commit.
    - git commit -m " " ------ to commit the files.
    - git push ------ to push the files to the master branch of the GitHub repo.
```
### Hosting on Heroku

- The deployed site on Heroku will update automatically upon new commits to the master branch in the [GitHub Repository](https://github.com/slavabdev/ms4-coffeeshop/)

To deploy the project to Heroku the following steps were taken:
*	Create a Heroku account at https://signup.heroku.com/
*	In Heroku click the New buton and create a new app with apropriate title and choose region closest to user.
*	Once the app is created click on the Resources button and choose the Heroku Postgres(free) to attach a postgres database to your project.
*	To use Postgres user need to install in local enviroment one need to install dj-databas-url to connect with PostgreSQL and Psycopg2(PostgreSQL adapter)
```console
pip install dj-database_url, Psycopg2
```
*	Create requirements.txt file in workspace for Heroku to understand installation files to run app.
```console
pip freeze > requirements.txt.
```
*	To connect to database Postgres in Heroku, user need to make the following changes in settings.py:
```console
1.	Import dj_database_url
import dj_database_url
2.	To comment out
DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
and insert:
DATABASES = {
        'default': dj_database_url.parse(insert db  url from heroku config variable)
    }
```    
Now, we can connect to Herku db and run migrations
```console
python manage.py showmigrations
python manage.py makemigrations
python manage.py migrate
```
•	The next step is to transfer database to Heroku using the following commands:
```console
python manage.py loaddata categories.py
python manage.py loaddata products.py
```
•	Once DB has been transfered we need to create superuser(admin)in Heroku
python manage.py createsuperuser
•	The next step us to delete the herku DB url and uncomment django db url to make sure our database is not commited to github. Once its done please commit and push to github.
•	After commiting we can use if statement to make sure that local Database used in local development and Postgress in Heroku:
```console
if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
```
•	To add Gunicorn which will act as webserver and freeze it
```console
pip install gunicorn
pip freeze > requirements.txt
```
•	Create Procfile to tell Heroku to create web dyno, which will run gunicorn and serve our Django app
web: gunicorn coffeeshop.wsgi:application
•	To login to Heroku from the CLI, use the command
heroku login
•	We need to disable static to prevent heroku to collect static files from our project, in CLI:
```console
heroku config:set DISABLE_COLLECTSTATIC = 1 --app YOUR APP NAME
```
•	To add heroku host address to allowed hosts in settings.py
``console
   ALLOWED_HOSTS = ['ms4-coffee-cup.herokuapp.com', '127.0.0.1']
```
•	Next step is to deploy app in heroku first by commiting to github and then to heroku using:
```console
heroku git:remote -a NAME OF PROJECT
```
git push heroku master
•	In Heroku to connect to github and enbla automatic deployment.
•	To add SECRET_KEY in HEROKU and in settings.py
```console
SECRET_KEY = os.environ.get('SECRET_KEY', '')
```
and set DEBUG to True if DEVELOPMENT in os
DEBUG = 'DEVELOPMENT' in os.environ
and commit again.
•	To store static files an images we can create account and use Amazon service S3:
1.	in Amazon S3 create new bucket
2.	uncheck block all public access and acknowldge it public.
3.	create bucket
4.	create static website hosting and insert(index.html and error.html and save)
5.	permissions tab 5.1. CORS configuration 5.2. Policy tab - create S3 Bucket Policy( principal *, Actions - Get Object) 5.3. Copy ARN from CORS to permission and create policy 5.4. Copy policy into Bucket Policy and save 5.5. Access control - Everyone
6.	Go to Amazon AIM service 6.1. Create Group 6.2. Click policies and in JSON tab to import S3 full access policy and copy and paste bucket ARN into json resources tab twice. 6.3. Click review policy and add name and description and then click create policy. 6.4. attach policy to the group. 6.5. Create user and attach to the group.
7.	Download .csv file containing access and secret access key.
•	After creating AWS service we can connect it to Django and Heroku
We need to install two packages:
```console
pip install boto3
pip install django-storages
```
and freeze it and add 'storages' to Install APPS in settings.py
•	In Heroku to enter in all your variables into Heroku's Config Vars.
```console
AWS_SECRET_ACCESS_KEY	
AWS_ACCESS_KEY_ID	
USE_AWS
```
inside the Django setting.py you need to set up the AWS configs so the static files could be connected to AWS
```console
if 'USE_AWS' in os.environ:
    # Cache control
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
    }

    AWS_STORAGE_BUCKET_NAME = 'ms4-coffee-cup'
    AWS_S3_REGION_NAME = 'eu-west-1'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

    # Static and media files
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    # Override static and media URLs in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
else:
    STATIC_URL = '/static/'
    STATICFILES_DIRS =(os.path.join(BASE_DIR, 'static'),)

    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
Remove collect static in heroku variables and in local development to create folder 'custom_storages.py and insert:
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
```
Then to push to Heroku and we will see in the log that all static files were collected succesfully an we will see folders created in S3.
•	Next step is to upload media files in S3
1.	Create folder Media
2.	Select all files and choose all images
3.	Click next and in manage public permission to choose to add public access and upload.
•	In admin we need to confirm superuser email address
•	In Heroku to add stripe variables
•	With all this complete the project is fully deployed.


### Forking the GitHub Repository
A forking the GitHub Repository is used for copying of the original depository to  GitHub account. It allows viewing or making changes in the project without affecting the original repository. It can be done using the following steps: 
1.	Log in to GitHub and go to the GitHub Repository.
2.	At the top-right of the page, just below the GitHub navigation bar, the "Fork" Button is located.
3.	Click the “Fork” button and get a copy of the original repository to a GitHub account. 
### Run project locally
1.	Log in to GitHub and locate the GitHub Repository.
2.	Click a “Code” dropdown button, which located just under the “Settings”.
3.	To clone the repository using HTTPS, copy the link with clone URL.
4.	Open Git Bash in your local IDE.
5.	Change the current working directory to the location where you want the cloned directory to be made.
6.	Type git clone, and then paste the URL you copied before.
```console
git clone https://github.com/SLAVABDEV/REPOSITORY
```
7.	Press Enter. Your local clone will be created.
```console
$ git clone https://github.com/slavabdev/ms4-coffeeshop
> Cloning into `Spoon-Knife`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```
### Content
- All content (except product description) was written by the developer.
### Media
- All images (ecxept the products) were taken from [unplush](https://unsplash.com).
- All product images and descriptions were taken from [SOMA](https://somacoffeecompany.ie) and [3FE](https://3fe.com)
    
### Acknowledgements
- Friends and family for helpful feedback.
- My Mentor and Code Institute tutors for support and useful feedback.
- Code Institute for teaching me how to make coding magic.
