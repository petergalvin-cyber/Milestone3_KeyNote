
# Milestone 3 : Orator Library 
This application creates a site that promotes and sells high profile Keynote speakers for various corporate events. The application reads, updates, creates and deletes Keynote speaker information that is populated in a MongoDB database. The high profile orators will entice the user and encourage them to reserve an speaker. 

The user can search for Keynote speakers under the following categories:
1. Business & Management
2. Celebrities, Arts & Culture
3. Economics & Finance
4. Future & Technology
5. Government & Politics
6. Innovation & Creativity
7. Leadership & Motivation
8. Society & Education

The above categories can be updated and deleted. Additional catgegories can also be created. 


# UX
The site promtes KeyNote speakers profiles and encourages them to be booked by companies in order to inspire their employees to excel. The KeyNote speakers are high profile Business people, Artists and Celebrities. The level of excitement surrounding these individuals aims to attract bookings for corporate events and generate profit for the site.

The user should get easy access to information about their selected speakers and have it presented in an attractive manner to generate a booking.


## Strategy
Generate sufficient interest for users to book speakers and promote speakers through appropriate information display.


## Scope
Focus on the speaker's celebrity status and have their information easily obtained to generate bookings from users.


## Skeleton
Speaker profiles are presented by selecting speaker categories in the home page. Speakers are presented in a card format and on clicking individual cards a complete speaker biography is revealed where the user can select to amend or delete the speakers details.

In the home page the user can select to add a new speaker or create a new category. Within categories the user can also amend or delete categories. 

At all times the user is given information to contact the site to make a booking in the header and footer. The user can select to return to the home page at all times. 

The wireframe design was based on a landing page obtained from the Bootstrap theme site: https://startbootstrap.com/themes/landing-page/


## Surface
Use masthead orator photo present the site's ethos. Large spaces and padding are used to focus on speaker information. The option to reserve a speaker is presented throughout the site.

## Data
The data for the project sits in MongoDB cluster 'Cluster-Peter'; database 'SpeakerHub'; collections 'Category' and 'Speakers'. Individual categories are stored as documents in the 'category' collection within ID (Object) and Category(string) fields. Individual Speakers are stored as documents using ID(Object), name(string), bio(string), banner(string), photo(string), category (array of strings).  

Validation in the Speaker creation form ensures that no empty Speaker profiles can be created. When deleting any information the user is asked to confirm before proceeding.

## Technologies
1. HTML
2. CSS
3. Javascript and Jquery
4. Python using Flask framework
5. Mongo DB Atlas NoSQL database


## Testing
This application's backend contained the most complexity consisting of database communication and flask routing between HTML pages. The front-end was relatively easy to implement by using a Bootstrap template. Therefore, the majority of testing focussed on the backend.

1. Speaker Category: Test the **C**reate, **R**ead, **U**pdate and **D**elete functions operate.

  * [Display Categories - Read](testing/A_Test1_Read_Category_list.png)
  * [Create Category - "Farming"](testing/A_Test2_Create_Category_list.png)
  * [Update Category - "Farming & Stuff"](testing/A_Test3_Amend_Category_list.png)
  * [Delete Category - "Farming & Stuff"](testing/A_Test4_Delete_Category_list.png)


2. Speaker Information: Test the **C**reate, **R**ead, **U**pdate and **D**elete functions operate.

  * [Data Entry : Display Speaker Info under "Leadership & Motivation" category](testing/B_Test1_Read_Speaker.png)
  * [Test Results : Display Speaker Info under "Leadership & Motivation" category](testing/B_Test1_Read_Speaker_Result.png)
  * [Data Entry : Create Speaker under "Leadership & Motivation" category](testing/B_Test1_Create_Speaker.png)
  * [Test Results : Create Speaker under "Leadership & Motivation" category](testing/B_Test1_Create_Speaker_Result.png)
  * [Data Entry : Update Speaker under "Leadership & Motivation" category](testing/B_Test1_Update_Speaker.png)
  * [Test Results : Update Speaker under "Leadership & Motivation" category](testing/B_Test1_Update_Speaker_Result.png)
  * [Data Entry : Delete Speaker under "Leadership & Motivation" category](testing/B_Test1_Delete_Speaker.png)
  * [Test Results : Delete Speaker under "Leadership & Motivation" category](testing/B_Test1_Delete_Speaker_Result.png)

Manaul tests were performed in the front end to ensure the application was responsive for all devices and is compatible with Chrome, Safari, Firefox and Edge but not with IE 10 or less. Tests were performed on the Speaker creation form to verify form validations operate effectively.


## Deployment
### Github
#### Github repository - 

To run locally you can download direct from GitHub as follows:
1. Find the underlying link behind the green "Clone or download" button. 
1. In your local workspace enter wget link obtained in 1. 
2. Unzip the zip file.
3. In mongoDB database create a database called project with two collections category and speakers the specifics of the collections can be found in the database schema. 
5. Run the application entering python3 app.py in the command line.

### Heroku

#### Heroku Deployment - xxxxxx


# Credits
Ideas for the site were obtained from the [London Speaker Bureau] (www.londonspeakerbureau.com). This contained all the speaker information used in the application.




















