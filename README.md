Project Overview
I have create Web App From Scratch Using Python Flask with Azure that lets users to calculate their BMI value, to know their ideal weight. can you access this : https://calculatorb.azurewebsites.net/

This Web Application includes 2 pages, switched by the routes of Flask server. How to use in the local service: 

1. Downlod or clone this repo on local device.  
2. I use scratch python with Flask in web app. This must also be installed.
3. Install Flask:

 - If you are on Mac OS X or Linux, chances are that one of the following two commands will work for you:

	$ sudo easy_install virtualenv
	or even better:

	$ sudo pip install virtualenv
	One of these will probably install virtualenv on your system. Maybe it’s even in your package manager. 
	If you use Ubuntu, try:

	$ sudo apt-get install python-virtualenv
	If you are on Windows and don’t have the easy_install command, you must install it first. Check the pip and 	setuptools on Windows section for more information about how to do that. Once you have it installed, run the same 	commands as above, but without the sudo prefix.

	Once you have virtualenv installed, just fire up a shell and create your own environment. I usually create a 	project folder and a venv folder within:

	$ mkdir myproject
	$ cd myproject
	$ virtualenv venv
	New python executable in venv/bin/python
	Installing setuptools, pip............done.
	Now, whenever you want to work on a project, you only have to activate the corresponding environment. On OS X and 	Linux, do the following:

4. $ . venv/bin/activate
   If you are a Windows user, the following command is for you:

   $ venv\scripts\activate
   Either way, you should now be using your virtualenv (notice how the prompt of your shell has changed to show the active    environment).

   And if you want to go back to the real world, use the following command:

  $ deactivate
  After doing this, the prompt of your shell should be as familiar as before.

  Now, let’s move on. Enter the following command to get Flask activated in your virtualenv:

  $ pip install Flask
  A few seconds later and you are good to go.

  System-Wide Installation This is possible as well, though I do not recommend it. Just run pip with root privileges:

 $ sudo pip install Flask
(On Windows systems, run it in a command-prompt window with administrator privileges, and leave out sudo.)

Install Flask-Script with pip:

$ pip install Flask-Script
However, no further configuration our setup is required, as the database is fully contained in the db directory in this repository.

Once these prerequisites are installed, the application can be run locally:

$ python app.py
$ flask run
Once the application is running, it can be accessed by pointing your browser at http://127.0.0.1:5000/ .

5. Architecture This web application runs in Python 3 using the Flask web micro-framework with simple scratch and this Webb application can running in app service azure with azure Devops. 