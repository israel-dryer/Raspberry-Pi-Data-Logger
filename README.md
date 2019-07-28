# Raspberry-Pi-Data-Logger
Example scripts to collect and log data with the Raspberry PI with CSV or SQLite

## Overview
These are example scripts where the logger functions can be adapted to any source of data that you are collecting. These scripts are part of a [video tutorial]() which you can follow along with if you wish.

The scripts use the **psutil** library to collect information about the Raspberry Pi. To install this library: 
```
sudo apt-get update
sudo apt-get upgrade
sudo pip3 install psutil
```
The tutorial assumes that there is a folder called **data** inside the directory where the script is being run.

The **sqlite** version required that sqlite be install. It will come with python already. However, if you want to work with sqlite outside of python to create and query the day, you may need to install with `sudo apt-get install sqlite3`. When you open up a connect to a SQLite database, the database will be created if it does not exist. To open the database from the command prompt, navigate to the database directly and type `sqlite3 DBNAME.db` where DBNAME is the name of your database. You can [find more information](https://sqlite.org/index.html) about SQLite on their database.

SQLite is the database that I used in this example, but you can substitute any other type of database in the script that I've provided. Typically a connection string is required in more traditional databases in the `connect()` call. However, you should consult the API of the database you would like to use for more details about connection methods.

## NOTE !!
This code uses f-string formatting. So if you are using a version of Python < 3.6, then you'll need to change the f-string to the str.format().
