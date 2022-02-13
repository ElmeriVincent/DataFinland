<h2 align="center">Data Finland</h2>

<h3>Using Streamlit to create and deploy an app</h3>

- Collecting data
- Choosing database
- Configuring connections
- Visualizing data
- Making our app interactive
- Deploying it on Streamlit

<h3 align="center">Checkout The App!
 </h3>

<h3 align="center">
  
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_red.svg)](https://share.streamlit.io/elmerivincent/datafinland/main/app.py)

</h3>

### What is Streamlit?
<p>"Streamlit is an open-source Python library that makes it easy to create and share beautiful, custom web apps for machine learning and data science. In just a few minutes you can build and deploy powerful data apps" -streamlit </p>

### Installing Streamlit

https://streamlit.io/

##### Terminal:
`pip install streamlit`

`streamlit hello`

### Starting With Streamlit

`import streamlit`

Remember 

`pip install (yourImports)`

##### Viewing your app:

`streamlit run [filename]`

<br>

### Starting with Data

- Where I got my data: https://data.worldbank.org/country/FI
- Decide where you want to handle your data(mysql, mongoDB, Excel, etc...)

<br>

#### Using Excel

Example how to potray your data:

![readmee](https://user-images.githubusercontent.com/77973084/134701782-a252f0db-90a1-47fd-b0ce-e2910d26ca18.png)

- Remember to format the "year" to the Year format.
  - Right click the year 
  - Number Format
  - Own
  - Then select the year format

 <br>
 
 
 #### Using MySQL
 
 First time with MySQL? To get started https://dev.mysql.com/doc/mysql-getting-started/en/#mysql-getting-started-installing
 
 *In MySQL WorkBench:*
 
 ![example](https://user-images.githubusercontent.com/77973084/140620794-6f23ef5e-eeac-46ab-8149-429517bbb28a.png)
 
 When you got your data ready and mysql server running, go to docs and follow the guide on how to use mysql in streamlit
 https://docs.streamlit.io/knowledge-base/tutorials/databases/mysql#add-username-and-password-to-your-local-app-secrets
 
 - creating .streamlit/secrets.toml
 - Add secrets to cloud
 - add `mysql-connector-python==x.x.x` to requirements.txt
 
 <br>

 #### What is requirements.txt?
 is used for specifying what python packages are required to run the project you are looking at.
 
 Lets say you have `import plost` in your app.py
 
 in requirements.txt we would want to have the current version for example `plost==0.1.0`
 
 <br>
 
<h4 align="left">
 Streamlit Version: 1.0.0

 <br>
 

<h3 align="center">

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

[![PyPi license](https://badgen.net/pypi/license/pip/)](https://pypi.com/project/pip/)

</h3>
 



    

    
  



  
   
  

