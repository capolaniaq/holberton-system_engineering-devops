# 0x1A. Application server

By Sylvain Kalache, co-founder at Holberton School

## Tasks

### 0. Set up development with Python	

Let’s serve what you built for  [AirBnB clone v2 - Web framework](https://intranet.hbtn.io/rltoken/EJw7FG9Zmwlu6qo9RggPfw "AirBnB clone v2 - Web framework")  on  `web-01`. This task is an exercise in setting up your development environment, which is used for testing and debugging your code before deploying it to production.

Requirements:

-   Make sure that  [task #3](https://intranet.hbtn.io/rltoken/eL5390Y6rOrrSCYeBBdzlw "task #3")  of your  [SSH project](https://intranet.hbtn.io/rltoken/9r-2ODIpnVNWJp5OUl7JRA "SSH project")  is completed for  `web-01`. The checker will connect to your servers.
-   Git clone your  `AirBnB_clone_v2`  on your  `web-01`  server.
-   Configure the file  `web_flask/0-hello_route.py`  to serve its content from the route  `/airbnb-onepage/`  on port  `5000`.
-   Your Flask application object must be named  `app`  (This will allow us to run and check your code).

### 1. Set up production with Gunicorn

Now that you have your development environment set up, let’s get your production application server set up with `Gunicorn` on `web-01`, port `5000`. You’ll need to install `Gunicorn` and any libraries required by your application. Your `Flask` application object will serve as a [WSGI](https://intranet.hbtn.io/rltoken/alKO4HKARCTOB7W_fpRnTA "WSGI") entry point into your application. This will be your production environment. As you can see we want the production and development of your application to use the same port, so the conditions for serving your dynamic content are the same in both environments.

### 2. Serve a page with Nginx

Building on your work in the previous tasks, configure `Nginx` to serve your page from the route `/airbnb-onepage/`


### 3. Add a route with query parameters

Building on what you did in the previous tasks, let’s expand our web application by adding another service for `Gunicorn` to handle. In `AirBnB_clone_v2/web_flask/6-number_odd_or_even`, the route `/number_odd_or_even/<int:n>` should already be defined to render a page telling you whether an integer is odd or even. You’ll need to configure `Nginx` to proxy HTTP requests to the route `/airbnb-dynamic/number_odd_or_even/(any integer)` to a `Gunicorn` instance listening on port `5001`. The key to this exercise is getting `Nginx` configured to proxy requests to processes listening on two different ports. You are not expected to keep your application server processes running. If you want to know how to run multiple instances of `Gunicorn` without having multiple terminals open, see tips below.


### 4. Let's do this for your API


Let’s serve what you built for  [AirBnB clone v3 - RESTful API](https://intranet.hbtn.io/rltoken/o_uAVsuNqXbJIgw7-ZmiYQ "AirBnB clone v3 - RESTful API")  on  `web-01`.

Requirements:

-   Git clone your  `AirBnB_clone_v3`
-   Setup  `Nginx`  so that the route  `/api/`  points to a  `Gunicorn`  instance listening on port  `5002`
-   `Nginx`  must serve this page both locally and on its public IP on port  `80`
-   To test your setup you should bind  `Gunicorn`  to  `api/v1/app.py`
-   It may be helpful to import your data (and environment variables) from  [this project](https://intranet.hbtn.io/rltoken/r3mnHZ7LoLJVF8JNxstDrQ "this project")
-   Upload your  `Nginx`  config file as  `4-app_server-nginx_config`

### 5. Serve your AirBnB clone

Let’s serve what you built for  [AirBnB clone - Web dynamic](https://intranet.hbtn.io/rltoken/qOjECpMUaEXf4D0uoqHmQw "AirBnB clone - Web dynamic")  on  `web-01`.

Requirements:

-   Git clone your  `AirBnB_clone_v4`
-   Your  `Gunicorn`  instance should serve content from  `web_dynamic/2-hbnb.py`  on port  `5003`
-   Setup  `Nginx`  so that the route  `/`  points to your  `Gunicorn`  instance
-   Setup  `Nginx`  so that it properly serves the static assets found in  `web_dynamic/static/`  (this is essential for your page to render properly)
-   For your website to be fully functional, you will need to reconfigure  `web_dynamic/static/scripts/2-hbnb.js`  to the correct IP
-   `Nginx`  must serve this page both locally and on its public IP and port  `5003`
-   Make sure to pull up your Developer Tools on your favorite browser to verify that you have no errors
-   Upload your  `Nginx`  config as  `5-app_server-nginx_config`
