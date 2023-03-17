# Backend part of my recipe webapp
<h1 align="center">Hi 👋, I'm Hùng</h1>
<h3 align="center">I'm just a newbie developer trying new things</h3>

<h3 align="left">About the project</h3>
This is designed to make cooking and baking at home not only easier and more enjoyable but also healthier. With a vast collection of recipes, you'll never run out of meal ideas or inspiration, and you'll also have access to the nutritional value of each dish.
<p>To get started, simply navigate to our website and you'll have access all of the recipe, which are sorted by category, cuisine, cooktime and more.  </p>
<p>Each recipe page includes a detailed list of ingredients, step-by-step instructions to guide you through the cooking process. You'll also see the nutritional value of each dish, including calories, fat, protein, and carbs. </p>
<p>You will also have the opportunity to contribute to our recipe collection by simply create an account and submit your own recipe.
All recipes submitted to our website will go through a verification process and this process may take some time. If your recipe is approved, it will be published on our website for our users to try. We appreciate your contribution and look forward to sharing your delicious recipe with our users.
</p>

<h3 align="left">Languages and Tools</h3>
<p align="left"> <a href="https://aws.amazon.com" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/amazonwebservices/amazonwebservices-original-wordmark.svg" alt="aws" width="40" height="40"/> </a> <a href="https://flask.palletsprojects.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/pocoo_flask/pocoo_flask-icon.svg" alt="flask" width="40" height="40"/> </a> <a href="https://www.postgresql.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/postgresql/postgresql-original-wordmark.svg" alt="postgresql" width="40" height="40"/> </a> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> 
<a href="https://www.docker.com/" target="_blank" rel="noreferrer"> <img src="https://www.docker.com/wp-content/uploads/2022/03/vertical-logo-monochromatic.png" alt="docker" width="40" height="40">
</a></p>

<h3 align="left">How to run this locally </h3>
You will have to install Python, Flask, PostgreSQL,Pgadmin4 and Docker for this. You also need an amazon aws account with s3 bucket for storing image.

<pre>
Step 1: Pull image from Docker hub with command "docker pull <"image name created later">"
Step 2: Once the image is downloaded, create a new container from image with command: 
<br>"docker run --name <"your container name"> -e POSTGRES_PASSWORD=<"your password"> -e POSTGRES_USER=<"your username"> -p 5432:5432 -d <"to do : add image name later"> </br>
Step 3: Run this command to check for postgres url for this project 
<br>'docker exec <"your container name"> sh -c 'echo "postgresql://<"your username">:<"your password">@localhost:5432/RecipeRepo" '</br>
Step 4: Connect PgAdmin4 to Postgresql in container (can use this site as a guide : https://dykraf.com/blog/how-to-connect-pgadmin4-and-postgresql-server-on-docker-container)
Step 5: Sign up for api key at this site :https://fdc.nal.usda.gov/api-key-signup.html
Step 6: Create s3 Bucket aws (can use this site as a guide : https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html)
Step 7: Add .env file and config with the same format as file "env-example.txt"
To run, use command : "flask run"
Use Postman API to try this API in blueprint of each folder or running this frontend application : frontendrepository.com
</pre>




