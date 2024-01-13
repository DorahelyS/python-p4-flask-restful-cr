'''
Key Vocab
Representational State Transfer (REST): a convention for developing applications that use HTTP in a consistent, human-readable, machine-readable way.
Application Programming Interface (API): a software application that allows two or more software applications to communicate with one another. Can be standalone or incorporated into a larger product.
HTTP Request Method: assets of HTTP requests that tell the server which actions the client is attempting to perform on the located resource.
GET: the most common HTTP request method. Signifies that the client is attempting to view the located resource.
POST: the second most common HTTP request method. Signifies that the client is attempting to submit a form to create a new resource.
PATCH: an HTTP request method that signifies that the client is attempting to update a resource with new information.
PUT: an HTTP request method that signifies that the client is attempting to update a resource with new information contained in a complete record.
DELETE: an HTTP request method that signifies that the client is attempting to delete a resource.


Example REST Workflow
For a real world case study, let us pretend that you have a newsletter application. The following is a high-level view of how such an app might work:

You fill out the form on the 'New Newsletter' page and click submit.
Data concerning you as the author, your newsletter content, and any additional information such as multimedia items is sent to the application server.
The server interprets the information, recognizes that the request is for a new newsletter, generates the new record in the database, and performs background tasks (updating the newsletter counter, sending notification emails, etc).
Next, the server sends a response back to the cilent. This does not necessarily mean that the newsletter was posted. The response could be that there was an error posting, or something along those lines. However, in this example we will say that the post went through properly, so the server sends a 201 response code and tells the browser which page to go to and render.
Lastly, the browser receives the server information and shows you a message saying that your newsletter was successfully posted.
RESTful Conventions in Flask
Flask is lightweight, well-documented, and has a large community online (which gives you a wide population of people to provide help as you implement new tools in your Flask applications). Additionally, Flask provides native support for all HTTP request methods and makes it very easy to define routes- with these features, we can say that Flask natively supports REST conventions.

Let's take a look at how this would work for our newsletter application. RESTful routes fall into four familiar categories: Create, Read, Update, and Delete. These will roughly translate to five routes:

Categories of Routes and Their Actions
Category	Action
Create	Create the new newsletter instance.
Retrieve All (Index)	Display a list of all newsletters.
Retrieve One	Display an individual newsletter.
Update	Update the newsletter instance.
Delete	Delete an existing newsletter instance

HTTP Request Methods and RESTful Routes
To implement each of the above actions, we combine an HTTP request method (or HTTP verb) such as GET or POST with a route. Flask then maps each method/route combination to the appropriate view in the Flask application. The table below shows the HTTP request method and route we could use for this RESTful newsletter app:

RESTful Routes for a "Newsletters" API
HTTP Request Method	Route	Description
GET	/newsletters	Show all newsletters.
POST	/newsletters	Create a new newsletter.
GET	/newsletters/<int:id>	Show a specific newsletter.
PATCH or PUT	/newsletters/<int:id>	Update a specific newsletter.
DELETE	/newsletters/<int:id>	Delete a specific newsletter.
Note that even though we have five separate actions, we only have two routes defined in our application: /newsletters and /newsletters/<int:id>.

Review of HTTP Request Methods
So what do GET, POST, et al. represent? These HTTP verbs give each HTTP request unique behavior. Below is an explanation of each verb:

GET: The GET method retrieves whatever information is identified by the Request URI. This means if you go to /newsletters, you will get all of the newsletter posts that the application has.

POST: The POST method is used to send data enclosed in the request to the server. The server is expected to use this data to create some new resource.

PATCH/PUT: The PATCH and PUT methods are both used to update existing resources. Sending either a PATCH or PUT request to /newsletters/1 will update the post with an id of 1. PUT is used when we want to replace an entire resource. PATCH is used when we want to update a specific part of a resource

DELETE: The DELETE method requests that the server delete the resource identified by the Request URI. This means… that it deletes the record. It's nice and explicit.

Things to Keep in Mind throughout this Module
Below are a few keys to remember when thinking about REST:

REST is an architectural design pattern, not a framework or code in itself. Many other web frameworks utilize RESTful design principles in some form or another. By using RESTful principles, Flask apps are able to have a clear and standardized naming structure for routes and actions.

RESTful routes have a clear mapping between the URL resource and the corresponding actions carried out by the backend.

There are five RESTful route options we will commonly use as API developers






'''