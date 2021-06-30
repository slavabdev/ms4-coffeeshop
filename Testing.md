# Testing
The W3C Markup Validator and W3C CSS Validator Services were used in the project to ensure there were no syntax errors.
* [W3C Markup Validator](https://validator.w3.org/nu/) 
    ***some issues indicated comming from bootstrap5***
* [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
* [JSHint](https://jshint.com/)
* [PEP8](http://pep8online.com/) 

### Manual testing of all elements and their functionality.

- **NAVIGATION BAR**:
    - Click on the logo to make sure that it links to the homepage.
    - Click all the navbar items to verify that they work and lead the user to correct pages.
    - Make a query to the searchbar and verify that it works.
    - Change the screen size from desktop to tablet and from tablet to mobile to make sure that the navigation bar switches from the inline menu to burger dropdown menu. Check all menu items to verify that they are clickable, on the correct place  works well.

- **FOOTER**:
    - Hover over each social media icon and make sure that colour change expected.
    - Click on each icon to confirm that the link opens in a separate tab.
    - Play with the window width to verify that the footer is responsive and looks good for different screen sizes
    - Confirm that footer code is the same on all HTML pages.
- **HOME PAGE**
    - Open the page in different browsers and scroll it down to make sure that everything displays correctly. 
    - Carousel
        - Click on the dots and arrows to verify that the carousel works correctly and all slides are displayed accurately.
        - Hover over the buttons to make sure that they change the colour.
        - Click the buttons to verify that they link with the correct sections/pages.
        - Expand and reduce a screen size to verify that slider looks good on different screen widths. 
- Categories section
    - Expand and reduce a screen size to verify that this section looks good on different screen widths.
    - Confirm that all images and text are display properly.
    - Click on them to verify that they link to the right pages, which opens using correct filtering.
- About section 
    - Expand and reduce a screen size to verify that section looks good on different screen widths. 
    
- **PRODUCTS PAGE**
    - Confirm that all products are visible.
    - Expand and reduce a screen size to verify that the page and all the components looks good on a different screen widths. 
- Search
    - Confirm that page title display the correct value ('category name' if came by the category link from the fome page; or 'All products') 
    - Print the text that is exactly in some of products and check if search will find it.
    - Print the text that is not in products and check if search will return '0 items found' message.
- Products
    - Verify that all products data display properly
    - Click on the product to confirm it links to a particular product page.

- **AUTHENTIFICATION**
    - Confirm that all content is visible
    - Expand and reduce a screen size to verify that the page and all the components looks good on a different screen widths. 
    - Confirm that un-registered/unauthorised user can't see the information the shouldn't see: add comment, manage profile and ect.
    - Confirm that registered/authorised user can't see the 'Register' and 'Login' items on the navbar.
- Register 
    - Confirm that it is unable to register without filling the whole registration form.
    - Confirm that it is unable to register with the existing users username.
    - Confirm that after registration user get a conirmation letter with link.
- Login
    - Verify that it is unable to login without filling the whole  form.
    - Verify that it is enable to login using google account. 
    - Confirm that it is unable to login with the adding incorrect username/password
    - Confirm that after log in user get a corresponding message.
- Logout    
    - Confirm that after clicking a 'logout' in the navigation section user will be popped out of the session, get a corresponding message.
- **PROFILE**
    - Confirm that all content is visible
    - Expand and reduce a screen size to verify that the page and all the components looks good on a different screen widths.
    - Confirm that all section in the profile block works well. 
- **PRODUCT**
    - Make sure that only product display correctly and get the correct content from database.
    - Confirm favourites button works properly (add to favourite (red heart) - add item to Profile favourites and remove item  - remove the item from favourites)
    - Make sure that comments work properly (display to all users; edit only registered, delete - superuser)
    *** if superuser ***
        Make sure that only superuser can add, edit and delete produts, and delete comments
- **PAYMENT**
    - Make sure that products are getting to cart with correct price and value.
    - Confirm that quantity of items can be changed and the price will be updated.
    - Confirm that delivery price will be 0 if order on 30euro or higher.
    - Confirm that order safely renders on checkout page. 
    - Confirm that payment system works well.

## **Testing User Stories from User Experience (UX) Section**
- As a **new visitor**, I want to understand what this website about and what its purpose. 
    - Upon entering the site, the user sees the company logo on the navigation bar and a slider with themed images and сall to action content. When scrolling down the home page, the user can easily understand what the website purpose.
- As a **new visitor**, I want to easily navigate the site to get a content what I need;
    - The website has a clear and understandable, responsive and fixed navigation bar, which allow to user navigate the pages and sections easily.
    - User can navigate the website using navigation bar as well as buttons located on pages. 
- As a **new visitor**, I want to see a website, which works properly on my device;
    - Website is made fully responsive, so it’s convenient to browse on a desktop, laptop, tablet and mobile devices. 
    - Website works stably with different browsers as well.
-	As a **new visitor**, I want to have an ability browse all products on the site;
    - There are few options how user can browse the products:
        - They can check All products on the website by clicking a corresponded link on the navigation bar, or the button on the Home Page (on slider)
        - They can check products by chosing a specific category from the category list on the Home page.
- As a **new visitor**, I want to be able to filter products by categories, sort them by different criteria and search them using keywords;
    -  For users convenience they can filter products by category by clicking a particular button on the home page (category section).
    -  Users can search the product by title or description through all the recipe page. Also user can filter products by name, price and category, using special selector.
- As a **new visitor**, I want to see a modern website with a pleasant colour palette.
    - The website (including the buttons, forms and content) is made in one style and using pleasant colour palette.

*	As an **interested visitor** I want to easily and safely purchase products I need;
    - The website has a clear purchase navigtion with pop-ups amd messages, which allow user to pass the purchase process easily.
    - The sefety of payment is guaranted by Stripe. Webhooks will help to avoid accidental money transactions.
*	As an **interested visitor** I want to easily create an account and login using 3rd party profile(ex. Google);
    - Website provides 2 options: fill the small form and register localy, or login with user's existing Google account.
*	As an **interested visitor** I want to see detailed description of the products and read an add comments (for making decision);
    - Every product page includes detailed information about the product and other related information including comments, written by other loggedin users.
*	As an **interested visitor** I want to have an ability to add/edit/delete products in my shopping cart;
    - The shopping cart functionality allows to manipulate with products in it (edit/delete). When user update products in the cart, the can see the new total price at the same moment. 
*	As an **interested visitor** I want to have an option to save some products to favorites;
    - Loggedin users have an ability to add any product to favourites. Then they can go to profile (favourites section) and revise them.
*	As an **interested visitor** I want to have a profile page, where I can keep see the history of my orders and other user-related information;
    - Every loggedin/Registered user will have a personal profile with dashboard. This dashbourd includes the information about user's shipping address, favourite products and all their purchases.
* As a **superuser**, I want have an ability to add, edit and remove content and products on/from the website.
    - A superuser or admin can manipulate content on the website. He will use edit/delete buttons, which regular users can't see. And also superuser will get an access to the product management page, whe they can add new product.


- As an **interested visitor** I want to easily create an account on the site;
    - User can easily access to the registration page by clicking a corresponding link on the navigation bar or by clicking call to action butoon on the slider. Registration process is quick and doesn't require a multiple actions.
- As an **interested visitor** I want to have an ability to add/edit/delete my recipes on/from the website;
    - Every registered user have an ability to upload, edit and delete their own recipes. For users convenience, all these actions can be held from the Profile page. 
- As an **interested visitor** I want to easily navigate through recipes I posted;
    - All recipes posted by user will appear on the users profile page.
- As an **interested visitor** I want to get more information about the 'Easy Peasy' company and check their social media pages
    - All links to the Easy Peasy social media pages are located in the footer of every page of the website.
- As an **interested visitor**, I want to see the most popular recipes on the website.
    - Top 3 recipes are located on the bottom part of the home page and have a corresponding title.

*	As an **interested visitor** I want to easily and safely purchase products I need;
*	As an **interested visitor** I want to easily create an account and login using 3rd party profile(ex. Google);
*	As an **interested visitor** I want to see detailed description of the products and read an add comments (for making decision);
*	As an **interested visitor** I want to have an ability to add/edit/delete products in my shopping cart;
*	As an **interested visitor** I want to have an option to save some products to favorites;
*	As an **interested visitor** I want to have a profile page, where I can keep see the history of my orders and other user-related information;
*	As an **interested visitor** I want to get more information about the “Coffee Cup” company and check their social media pages.

As a **superuser**, I want have an ability to add, edit and remove content and products on/from the website sort them by different criteria and search them using keywords;

### Further testing
- The website was tested on the following browsers:
    * Google Chrome;
    * Opera;
    * Mozilla Firefox; 
    * Microsoft Edge; 
    * Safari.
- To be sure that website is responsive, it was viewed on such devices as desktops, laptops, tablet (Samsung galaxy tab A), and mobile (Iphone 6, IPhone X, IPhone XS Max, IPhone11 PRO MAX, Samsung Galaxy S10) .
- All buttons, forms and links have been tested several times to make sure they work correctly.
- Friends and family members reviewed the website from their devices to make sure that website is displaying well and all functions are working properly. 
### Known Bugs
- Bugs wasn't found.