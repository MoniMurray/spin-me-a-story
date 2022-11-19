##Credits

When I decided to create a story generator based on my daughter's favourite activity, being told a random made-up story, I turned to Google to find out which other genius had worked on this before me.  And I found this!
https://towardsdatascience.com/fantasy-story-prompt-generator-2f56bf98dbfa

I needed to force an exit from the program when the user chose option 'n' when asked "Would you like to write a story, {username}?".  I Googled to find a suitable option and found this 

https://www.askpython.com/python/examples/exit-a-python-program 

and chose to import sys and use the sys.exit() method.

![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome Monica Murray,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **August 17, 2021**

## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!