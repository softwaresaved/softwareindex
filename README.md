# softwareindex

softwareindex is a framework that enables a number of metrics relating to software to be gathered and displayed.

It is written in Python and uses the Flask framework.

## Installation

Clone the repository: git clone https://github.com/softwaresaved/softwareindex.git

## Configuration

These should be placed in a file called config.py in the same directory as the softwareindex.py file

* Flask secret key: note this is required at present! You can use any random string you like.
   * SECRET_KEY 

* SlideShare handler: requires API key and shared secret - register at http://www.slideshare.net/developers/applyforapi
   * SLIDESHARE_KEY
   * SLIDESHARE_SECRET
   
* CORE handler: requires API key - register at http://core.ac.uk/api-keys/register
   * COREAPI_KEY
   
## Running

Start the webapp by typing:
python softwareindex.py

Load a web browser - the server is running on http://127.0.0.1:5000/

Requests can be made by going to URLs of the form http://127.0.0.1:5000/index/<handler>/<identifier>

Where _handler_ is one of:
* core: search the core.ac.uk catalogue
* stackoverflow: search for mentions in stackoverflow
* slideshare: search for mentions in slideshare
* test: count the length of the software name (!)
* results: a consolidated results page

And _identifier_ is the software search term

## Contributors

This originated from an [idea](https://docs.google.com/document/d/1VbWG5ftvS09RnK9RYJJYSSwS_RgB5jpnfBKH1GJzRAc/edit) proposed at the Collaborations Workshop 2015 by Joe Parker, Peter Burlingson, Yannick Wurm, and Jochen Farwer. It was then [expanded](https://docs.google.com/document/d/1diezPpMLdXhs_R_STKpzo9UyafZguqvycqxhHKmz_oc/edit?usp=sharing) by Neil Chue Hong, Martin Hammitzsch, and Alessandro Felder. The first implementation was developed by Alessandro Felder, Neil Chue Hong and Jez Cope, and presented at the Collaborations Workshop 2015 Hackday.
