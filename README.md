Flask Cloud
============

<pre><code>

                                           i#######t                       
                                        ;#############W                    
                                      .#################K                  
                                     #####################                 
                                    #######################                
                                   #########################f              
                   .###L          ###########################              
                t##########      #############################             
              .##############   K##############################            
             #################  ###############################            
            ####################################################           
           :####################################################           
           #####################################################G          
          #######################################################          
          #######################################################          
          #######################################################          
         D#######################################################          
         ########################################################          
         ########################################################          
         ########################################################          
         W#######################################################          
          ##################W########################:###########          
        L#################   ######################   ############D        
      ;#######         L##   ######################   ##############j      
     ##########  ##### ####  #######################  ################     
    ###########  ##########  #######################  #################    
   ############  ##########  #######################  ##################   
  :############  ####E#####  #######################  ##################t  
  #############  #### #####  ######   ######    ####  ## ;ffE############  
 K#############      f#####  ####  ##  #### ### ####  ###  ############### 
 ##############  ### f#####  #### ###  ###W ####D###  ## ################# 
 ##############  ####f#####  ########  ####   ######  # ################## 
E##############  ##########  ######    #####    ####     ##################
###############  ##########  ####  ##  #######  .###  #G .#################
###############  ##########  ###  ###  ### ####  ###  ##  K################
###############  ##########  ###  G#G   ,#  ### E###  ###  t###############
##############     #######     ##   ## G###    W###     ##   ##############
###########################################################################
E##########################################################################
 ######################################################################### 
 ######################################################################### 
 E######################################################################## 
  #######################################################################  
  :#####################################################################i  
   #####################################################################   
    ###################################################################    
     #################################################################     
      :#############################################################i      
        j#########################################################L        
           G###################################################D    

</code></pre>


What is this?
-------------

A template to get your [Flask](http://flask.pocoo.org/) app running on
[DotCloud](https://www.dotcloud.com/) as fast as possible. For added
convenience, the templates use [Twitter's Bootstrap CSS
framework](http://twitter.github.com/bootstrap/) to help you, as a
developer, go from an idea to a working site.

All of the CSS stylesheets are written using the [Less
CSS](http://lesscss.org/) syntax. If you're using Mac OS X for
development, make sure to check out [incident57's
Less.app](http://incident57.com/less/).

Alternatively, there's a Less binary compiler that works similarly on
the commandline, or you can always use the [`less.js`
script](https://raw.github.com/cloudhead/less.js/master/dist/less-1.1.4.js)
in your website otherwise -- it's incredibly fast. For instance, if you
visit the [Less CSS site](http://lesscss.org), notice that it doesn't
link to any CSS files. **NOTE**: You can hotlink the [minified
less.js](http://cdnjs.cloudflare.com/ajax/libs/less.js/1.1.3/less-1.1.3.min.js)
from [CDN JS](http://www.cdnjs.com/).


Why should I use this?
----------------------

Everything I've learned from writing and maintaining the [Flask
Engine](https://github.com/zachwill/flask-engine) template for Google
App Engine has made its way into this repo, too. The goal is to make a
simple repo that can be cloned and added to for the majority of projects
going forward, while also staying minimal in size and complexity.

As an added bonus, while this repo does cater to DotCloud's hosting
service, the `bootstrap.py` file was created to help others clone this
repo and use Flask with other hosting providers (such as Amazon, Heroku, and
Rackspace).


Instructions
------------

First, you'll need to clone the repo.

    $ git clone git@github.com:zachwill/flask-cloud.git
    $ cd flask-cloud

Second, let's download `pip`, `virtualenv`, and the DotCloud CLI.

    $ sudo easy_install pip
    $ pip install virtualenv
    $ pip install dotcloud

Now, you can setup an isolated environment with `virtualenv`.

    $ virtualenv --no-site-packages env
    $ source env/bin/activate

Then, let's get the requirements installed in your isolated test
environment.

    $ pip install -r requirements.txt

Now, you can run the application locally.

    $ python bootstrap.py

You can easily specify which port you'd like to run your application on, too:

    $ python bootstrap.py 5555

To upload your application to DotCloud, you'll first need to do the
following:

    $ dotcloud create <my_application_name>
    $ dotcloud push <my_application_name> .

This should return a URL, and you can then view your application in
your web browser of choice.

And, to deactivate `virtualenv` (once you've finished coding), you
simply run the following command:

    $ deactivate


Adding Requirements
-------------------

In the course of creating your application, you may find yourself
installing various Python modules with `pip` -- in which case you'll
need to update the `requirements.txt` file. One way that this can be
done is with `pip freeze`.

    $ pip freeze > requirements.txt


Rather Use Heroku?
------------------

If you'd rather use Heroku for hosting, I've authored a near exact
[boilerplate skeleton](http://github.com/zachwill/flask_heroku), as well.


Other Hosting Environments
--------------------------

In case you're wanting to host your application on another environment
(the use case I'm imagining currently is Amazon's AWS), you could always
install `pip` and then uncomment `gevent` from the `requirements.txt`
file (or whatever server you plan on using).

We'll first setup our isolated environment like before:

    $ sudo easy_install pip
    $ pip install virtualenv
    $ virtualenv --no-site-packages env
    $ source env/bin/activate

You then should have no problem installing the packages.

    $ pip install -r requirements.txt

The idea then is that your application could be served with `gevent` by
envoking the `bootstrap.py` file like so:

    $ python bootstrap.py --gevent

Currently, this is more of a general idea than a working implementation
-- I'm sure you'd want to put `nginx` in front of your configuration to
serve up static files and media.
