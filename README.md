# ONLINE COURSE ENGAGEMENT PREDICTION

## Prerequisites
 *Python 3.x*
 *Pip (Python package installer)*
 *AWS CLI*
 *AWS Elastic Beanstalk CLI*

### Table of Contents
*1.Project Overview*
*2.Features*
*3.Installation*
*4.Usage*
*5.Deploymnet to AWS*
*6.Contributing*



## Project Overview
The purpose of the application is to predict whether a particular student completed a particular course online
## Installation
->To run this project locally, you need to have Python and the necessary libraries installed.
**1.Clone the repo.;**
        git clone https://github.com/steve601/course.git
        cd course
**2.Create a virtual environment and activate it:**
        python -m venv venv
        source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
**3.Install the required packages:**
        pip install -r requirements.txt

## Usage
=>Load the Model,then run the onlinecourse.py file on localhost then perform your prediction

## Deployment to AWS Elastic Beanstalk
**1.Initialize Elastic Beanstalk:**
      eb init
  Follow the prompts to configure your application. Choose the appropriate region and platform (Python).
**2.Create an Elastic Beanstalk environment:**
      eb create flask-env
**3.Deploy the application:**
      eb deploy
**4.Access the application:** After deployment, access your application using the URL provided by Elastic Beanstalk.

## Configuration File: .ebextensions/python.config
=>Ensure your configuration file is set up correctly:
       option_settings:
         aws:elasticbeanstalk:container:python:
           WSGIPath: onlinecourse:app
## Contributing
Contributions are welcome!

