# Item Catalog Project

**Note: If you already have a vagrant machine installed from previous Udacity courses skip to the 'Fetch the Source Code and VM Configuration' section**

This project I put in practice CRUD operations and I implemented third party authentication system provided by Facebook. In general 
this application is a web app where users can browse for restaurants and if they want the can create their own restaurants.
The app has APIs available to use, allowing other apps to communicate using RESTful Web services.  

### Flask

I used the python web framework flask which is a small lightweight framework used by many companies due to the freedon this can offer
if you want to know more about flask you can visit it is official [website](http://flask.pocoo.org/)

####Extesions Used

* Flask-WTF
* flask-sqlalchemy
* flask-bootstrap

### VirtualBox

VirtualBox is the software that actually runs the VM. [You can download it from virtualbox.org, here.](https://www.virtualbox.org/wiki/Downloads)  Install the *platform package* for your operating system.  You do not need the extension pack or the SDK. You do not need to launch VirtualBox after installing it.


### Vagrant

Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem.  [You can download it from vagrantup.com.](https://www.vagrantup.com/downloads) Install the version for your operating system.

**Windows Note:** The Installer may ask you to grant network permissions to Vagrant or make a firewall exception. Be sure to allow this.

## Clone the source code. 

From the terminal, run:

    git clone https://github.com/etp19/item_catalog.git

This will give you a directory named **item_catalog** complete with the source code for the flask application, a vagrantfile, and requirements.txt.
Install the necessary tools by typing the following:

    pip install -r sample_app/requirements.txt

## Run the virtual machine!

Using the terminal, change directory to item_catalog (**cd item_catalog**), then type **vagrant up** to launch your virtual machine.


## Running the Restaurant Menu App
Once it is up and running, type **vagrant ssh**. This will log your terminal into the virtual machine, and you'll get a Linux shell prompt. When you want to log out, type **logout** at the shell prompt.  To turn the virtual machine off (without deleting anything), type **vagrant halt**. If you do this, you'll need to run **vagrant up** again before you can log into it.


Now that you have Vagrant up and running type **vagrant ssh** to log into your VM.  change to the /vagrant directory by typing **cd /vagrant**. This will take you to the shared folder between your virtual machine and host machine.

Type **ls** to ensure that you are inside the directory that contains project.py, database_setup.py, and two directories named 'templates' and 'static'

Note: **python database_setup.py** is no longer necessary to initialize the database.  The database will be initialized at run time.

Type **python lotsofmenus.py** to pre-populate the database with restaurants and menu items. (Optional)  You may need to run this command twice, the first time it may fail.

Type **python run.py** to run the Flask web server. In your browser visit **http://localhost:5000** to view the restaurant menu app.  You should be able to view, add, edit, and delete menu items and restaurants.


###Note

- You will probably notice that this project does not have the best style or design that it could have because it is not the real focus on this project however, I use scss to make the structure cleaner, more organized and better for large amount of templates.
  
- In order to use scss files you can setup a grunt or gulp file, I personally use pycharm file watchers. The scss files are organize in two folders, global and modules and have a file named style that has all imports from the 2 folders, I implemented this way because is easier for the developer to change scss styles in small modules rather than in the whole css file.

- You may also notice that in the restaurant list there will be a filter button, this is a feature that I want to implement but so far is just a work in progress, images also will be part of the implementation.  