# Noodle World
Many people enjoy eating noodles and pasta. There may be some recipes already shared on the Internet, but many people have their noodles and pasta recipes. The purpose of this project is to make it easy to upload their recipes and share them with others. 

## UX 

### Preview
- Desktop 

![MS_Capture_desktop](https://user-images.githubusercontent.com/53374745/88457662-8de9b800-ce88-11ea-9c50-5c635bcbfe5f.jpg)

- Tablet 

![MS_Capture_tablet](https://user-images.githubusercontent.com/53374745/88457670-9a6e1080-ce88-11ea-9f77-a94a91ccacf5.jpg)

- Mobile 

![MS_Capture_mobile](https://user-images.githubusercontent.com/53374745/88457664-8fb37b80-ce88-11ea-8259-ca105d38e06f.jpg)


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

### Mockup
- [ms3-tablet.pdf](https://github.com/ss00831/milestone3/files/4977466/ms3-tablet.pdf)
- [ms3-desktop.pdf](https://github.com/ss00831/milestone3/files/4977467/ms3-desktop.pdf)
- [ms3-mobile.pdf](https://github.com/ss00831/milestone3/files/4977468/ms3-mobile.pdf)


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
- JS (https://jshint.com/) : 19 warnings
- Python (http://pep8online.com/) : No error

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

### My Milestone2 page address : https://noodleworld-ms3.herokuapp.com/

### To deploy this page to GitHub Pages from its GitHub repository (https://github.com/ss00831/milestone3) :
1. Create "requirements.txt" file
```
pip3 freeze > requirements.txt
```
2. Create "Procfile" file
```
echo web: python3 app.py > Procfile
```
3. Login heroku
4. Setting Config Vars 
: Heroku homepage - Select "noodleworld-ms3" project - Setting - Click "Reveal Config Vars" - Create Config Vars as below and save
![heroku_setting](https://user-images.githubusercontent.com/53374745/88460288-62bc9400-ce9b-11ea-895b-32e483e55d29.JPG)

* You can find the ["MONGO_URI"] value as below
: Login MongoDB - Select your cluster - click "CONNECT" button - click "Connect your application" - Select your driver and version - Copy the url - Paste in the env.py file
+) The url example: "mongodb+srv://root:xxxx@myfirstcluster-xxxxx.mongodb.net/COLLECTIONNAME?retryWrites=true&w=majority".
5. Deploy to Heroku
: git add . -> git commit -m "commit comment" -> git remote -v -> git push -u heroku master
6. To scale dynos 
```
heroku ps:scale web=1 
```
7. Run the webpage: Click "Open app" button on the Heroku dashboard page or write https://noodleworld-ms3.herokuapp.com/ on your web browser.

### How to run this project locally

To clone this project from GitHub :
1. Click [Code] - [Download ZIP] on the repository page.
2. Unzip the milestone3-master.zip file.
3. Open Git Bash on your local IDE.
4. (Optional) Change the current working directory to the location where you want the cloned directory to be made.
5. Move to the milestone3-master folder
6. Install the requirement files as below.
```
pip3 install -r requirements.txt
```
* If you need, update pip.
```
python -m pip install --upgrade pip
```
7. Make "env.py" file and write as below in the file.
```
import os

os.environ["SECRET_KEY"] = "YOUR_SECRET_KEY"
os.environ["MONGO_DBNAME"] = "MONGO_DB_COLLECTION_NAME"
os.environ["MONGO_URI"] = "your_mongodb_url"
```

* You can find the ["MONGO_URI"] value as below
: Login MongoDB - Select your cluster - click "CONNECT" button - click "Connect your application" - Select your driver and version - Copy the url - Paste in the env.py file
+) The url example : "mongodb+srv://root:xxxx@myfirstcluster-xxxxx.mongodb.net/COLLECTIONNAME?retryWrites=true&w=majority".

8. Execute the command as below for running app.py. 
```
flask run
```
9. Open a web browser and write this address as below.
```
http://127.0.0.1:5000/
```
## Credits

### Content
1. Short information about noodle : https://en.wikipedia.org/wiki/Noodle

### Media
1. Main image : https://pixabay.com/sv/photos/nudlar-om-mat-ramen-gravy-1962270/

2. Short information background : https://pixabay.com/sv/photos/pasta-nudlar-livsmedel-k%C3%B6k-549108/

3. E-mail icon background: https://www.netclipart.com/down/wThTii_e-mail-png-free-download-transparent-background-emails/

4. Alternative image for recipe : https://icon-icons.com/download/124121/PNG/512/

### Acknowledgements

1. How to create inline list in materialize css 
 - https://stackoverflow.com/questions/42884750/how-to-create-inline-lists-in-materializecss
2. Add/Remove Input Fields Dynamically with jQuery 
 - https://www.sanwebe.com/2013/03/addremove-input-fields-dynamically-with-jquery
3. How TO - Position Text Over an Image 
 - https://www.w3schools.com/howto/tryit.asp?filename=tryhow_css_image_text
4. Use an alt image for img HTML tags 
 - https://coderwall.com/p/hxauyq/use-an-alt-image-for-img-html-tags
5. Check if a given key already exists in a dictionary
 - https://stackoverflow.com/questions/1602934/check-if-a-given-key-already-exists-in-a-dictionary
6. How to append existing array in existing collection in mongodb using java with new values
 - https://stackoverflow.com/questions/31956696/how-to-append-existing-array-in-existing-collection-in-mongodb-using-java-with-n
7. loop backwards using template 
 - https://stackoverflow.com/questions/12680691/loop-backwards-using-django-template
8. materialize grid s12 not working in mobile view 
 - https://stackoverflow.com/questions/42891630/materialize-grid-s12-not-working-in-mobile-view/42912833
9. How to validate select option for a Materialize dropdown?
 - https://stackoverflow.com/questions/34248898/how-to-validate-select-option-for-a-materialize-dropdown
