# Selenium_demo
Demo of Selenium Webdriver - remote automation of a webpage for testing purposes

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Features](#features)
* [Examples of Use](#examples-of-use)
* [Status](#status)
* [Sources](#sources)

## General Info
This project is a demonstration of Selenium Webdriver. The code could be adapted to remotely automatically test a website.

## Technologies
This project is created with

Python 3.8

Selenium Webdriver

## Setup
To run this project install it locally using npm:

```
$ cd ../lorem
$ npm install
$ npm start
```

## Features
* Check title of a webpage (udemy.com)
* Input search term in search box (send keys method)
* Send the form
* Check a webpage redirects to search URL
* Check search matches the search term

### To do:
* Reuse this code to more extensively test a website

## Examples of Use

Usage: 

Run the code and the test will run in command line. Any assertion errors are reported to the user.

Code example:

Command line
`$ python3 auto_udemy.py`

## Status
Basic test functionality is complete.
Since this was written the Udemy search is no longer working with Selenium for some reason. It redirects to the main page. This is reported as an assertion error.

## Sources
This project is inspired by Andrei Neagoie Python Zero to Mastery course:

https://www.udemy.com/course/complete-python-developer-zero-to-mastery
