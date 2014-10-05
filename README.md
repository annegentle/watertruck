watertruck
==========

Simple Flask App with javascript/jquery HTML that shows a number of truck icons based on random number of trucks returned by the app.

Use Mac or Linux computer with Python 2.7 and virtualenv installed.

Note: When you are done with the virtual environment, just run:

    deactivate

The deactivate command returns you to your "normal" environment.

Now clone the humanitarian workshop repo to get the libcloud deployment code:

    git clone http://github.com/rackerlabs/humanitarian-workshop

Run the libcloud code itself to deploy to the Rackspace Cloud with credentials provided in a libcloud.conf file copied from the template:

    cd humanitarian-workshop
    cp participants/code/libcloud.conf.template participants/code/libcloud.conf
    vi participants/code/libcloud.conf
    virtualenv venv
    source /venv/bin/activate
    pip install -r requirements.txt
    python humanitarian-workshop.py


In about ten minutes you'll have a load balancer, two web servers, and a database server deployed. You can then enter the load balancer's public IP address returned the script in your web browser and see the Flask app. It should show a random number of truck icons with each reload.
