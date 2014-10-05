watertruck
==========

Simple Flask App with javascript/jquery HTML that shows a number of truck icons based on random number of trucks returned by the app.

You can deploy to the Rackspace Cloud with the included libcloud deployment example. 

First, rename libcloud.conf.template to libcloud.conf::
cd deployment
cp libcloud.conf.template libcloud.conf. 

Enter your username and API key in the credential line of libcloud.conf.

Once your conf file is ready, get a virtual environment started by::
virtualenv venv
source /venv/bin/activate

..note: When you are done with the virtual environment, just run::
deactivate

to get back to your "normal" environment. 

Next, install the needed requirements for the app::
cd deployment
pip install -r requirements.txt

Now run the libcloud code itself to deploy to the Rackspace Cloud with the credentials provided in libcloud.conf::
python humanitarian-workshop.py

In about ten minutes you'll have a load balancer, two web servers, and a database server deployed. You can then enter the load balancer's public IP address returned the script in your web browser and see the Flask app. It should show a random number of truck icons with each reload.
