# Noodle World
Many people enjoy eating noodles and pasta. There may be some recipes already shared on the Internet, but many people have their noodles and pasta recipes. The purpose of this project is to make it easy to upload their recipes and share them with others. 

## UX 

### Preview (*)
- Desktop 

![desktop_index](https://user-images.githubusercontent.com/53374745/83000187-4f5f8a80-a00a-11ea-9d7e-843b032e8a75.JPG)

- Tablet 

![table_index](https://user-images.githubusercontent.com/53374745/83000543-ceed5980-a00a-11ea-9f7b-cb38a5cebc03.JPG)

- Mobile 

![mobile_index](https://user-images.githubusercontent.com/53374745/83000558-d280e080-a00a-11ea-9a63-223b1409a356.jpg)

### User scenario
1. An external user wants to see noodles recipes.
 - Ability to view the recipes : READ
2. An external user wants to add and share a recipe.
 - Use an add recipe form. : CREATE
3. An external user wants to edit a recipe.
 - Every page has an “Edit Recipe” button and it has an edit form. : UPDATE
4. An external user wants to remove a recipe.
 - If the password is correct, anyone remove the recipe. : DELETE
5. An external user can send a message.
 - Use EmailJS 

### Mockup (*)
- [Desktop](https://github.com/ss00831/milestone2/files/4668180/ms2.pdf)
- [Tablet](https://github.com/ss00831/milestone2/files/4668179/ms2.-.tablet.pdf)
- [Mobile](https://github.com/ss00831/milestone2/files/4668178/ms2.-.mobile.pdf)


## Features
 
### Existing Features 
- Preview: Maximum 4 recipes are shown on the main page(index.html).
- Recipes: List of the added recipes. I have used image cards.
- Add recipe: Create a new recipe.
- Edit recipe: Change and Update a recipe.
- Delete recipe
- Send Message : Use EmailJS API.


### Features Left to Implement
- Login function


## Information Architecture (*)
 - xxxxxx

## Technologies Used

### Language
- HTML5
- CSS3 
- JavaScript
- Python

### Tools & Libraries 
- Flask 1.1.2 (https://flask.palletsprojects.com/en/1.1.x/)
- MongoDB 4.2.8 (https://www.mongodb.com/)
- JQuery 3.5.0 (https://jquery.com)
- Materializecss 1.0.0 (https://materializecss.com/)
- Fontawesome 5.12.1 (https://fontawesome.com/)
- Google font (https://fonts.google.com/)
- Github (https://github.com/)
- Gitpod (https://www.gitpod.io/)
- Heroku (https://www.heroku.com/) : For deployment

### APIs
- Email JS (http://emailjs.com/)


## Testing (*)
0. Device / Browser spec
- For Usability testing

    ![device_spec](https://user-images.githubusercontent.com/53374745/84033367-06f48500-a999-11ea-847e-a179bb27ce0c.JPG)

1. Code validation
- html (https://validator.w3.org/, Validate by URI) : No error
- CSS (https://jigsaw.w3.org/css-validator/, Validate by direct input) : No error
- JS (https://jshint.com/) : 11 warnings
- Python (http://pep8online.com/) : x error

2. Usability Test
- All functional test cases (26 items) : Pass
- All data test cases (real-time date - 2 items, input data - 6 items) : Pass

3. Responsive & Browser Test
- Pass condition :
    1. Must be resized to the image and content by the window sizes and resolutions
    1. All links need to work like the Full test 
    1. All images/contents/links must not be broken.

    ![browsertest](https://user-images.githubusercontent.com/53374745/78868081-8b329680-7a42-11ea-9b15-7a15dc172e3f.PNG)
- For responsive & browser testing

    ![Browser_info](https://user-images.githubusercontent.com/53374745/84033370-0825b200-a999-11ea-9794-02977dbbee79.JPG)

4. The detailed result : Please refer the test sheet as below.
- Result: [rev03_testcases_20200605.xlsx](https://github.com/ss00831/milestone2/files/4746075/rev03_testcases_20200605.xlsx)

5. The past test results
- xx Jul 2020: [rev02_testcases_20200602.xlsx](https://github.com/ss00831/milestone2/files/4717157/rev02_testcases_20200602.xlsx)


### Testing history (example, modify)
1. 27 Jul 2020 - Usability Testing
2. 02 Aug 2020 - Usability Testing / Responsive & Browser Test

## Deployment

### My Milestone2 page address : Heroku blah~~~~

### To deploy this page to GitHub Pages from its GitHub repository (https://github.com/ss00831/milestone2) :
1. From the menu items near the top of the page, select [Settings].
2. Scroll down to the [GitHub Pages] section.
3. [Source] - click the drop-down menu labelled None - select [Master Branch].
4. The page will automatically be refreshed, and the website is deployed.
 (If this step is failed, refresh the settings page and try again the "step 3".)
5. If the deployment is succeeded, you can see a message as "Your site is published at https://ss00831.github.io/milestone2/". Try to retrieve the link to the deployed website.

### How to run this project locally

To clone this project from GitHub :
1. Click [Clone or download] on the repository page.
2. In the "Clone with HTTPS" section, click the copy button (next of the address) and copy the clone URL for the repository.
3. Open Git Bash on your local IDE.
4. (Optional) Change the current working directory to the location where you want the cloned directory to be made.
5. Type "git clone", and then paste the URL you copied in Step 3.
```
git clone https://github.com/ss00831/milestone2.git
```
6. Press Enter and check the directory where you located on Step 4.


## Credits

### Content
1. Short information about noodle : https://en.wikipedia.org/wiki/Noodle

### Media
1. Main image : https://pixabay.com/sv/photos/nudlar-om-mat-ramen-gravy-1962270/

2. Short information background : https://pixabay.com/sv/photos/pasta-nudlar-livsmedel-k%C3%B6k-549108/

3. e-mail icon background: https://www.netclipart.com/down/wThTii_e-mail-png-free-download-transparent-background-emails/

### Acknowledgements

1. How to create inline list in materialize css 
 - https://stackoverflow.com/questions/42884750/how-to-create-inline-lists-in-materializecss
2. Add/Remove Input Fields Dynamically with jQuery 
 - https://www.sanwebe.com/2013/03/addremove-input-fields-dynamically-with-jquery
3. How TO - Position Text Over an Image 
 - https://www.w3schools.com/howto/tryit.asp?filename=tryhow_css_image_text