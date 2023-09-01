# Ylytic-assignment
create a search API on top of the existing API which will serve the below set of requirements:  1. (search_author field)  2. (at_from and at_to search fields)  3.  (like_from, like_to, reply_from, reply_to fields) 4.searched with a search string 5. All the above searches can be done within the same request as well.


steps to follow

1.Set up the Environement
  Create a new directory for your project and navigate to it.
  Set up a virtual environment: **`python -m venv venv`**
  Activate the virtual environment: source **`venv/bin/activate`**
  Install Flask: **`pip install Flask**`**
2.codeimplementation
  Create a file named app.py in your project directory and implement the Flask application
3.Deploy to AWS Lambda
  Deploying a Flask app on AWS Lambda involves several steps, including packaging and configuring AWS services like API Gateway. For detailed instructions, you      can follow the guide provided by AWS: Deploying a Serverless Web Application.
  
4.Testing
  Once deployed, you can use tools like curl or Postman to test your API using the specified query parameters. 
