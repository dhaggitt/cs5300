# Homework 1
Below are instructions for running these tests on your machine. Since I don't know your entire environment, this assumes you also need to run DevEDU on Docker locally, and set up the virtual environment in python.
The Dockerfile copies over the requirements.txt to the home directory, and the docker run will initialize you in the home directory.
## Running DevEDU in Docker locally
First, we build the Docker image:
``` docker build -t cs5300-devedu . ```
Once the image is built, we can run it using:
``` docker run --name cs5300 -d -p 80:80 -p 3000:3000 cs5300-devedu```
These steps create an image named "cs5300-devedu" and a container named "cs5300".

To execute from the container, we create an interactive shell using: 
```docker exec -it cs5300 /bin/bash```

Otherwise, we can connect to ```localhost``` on our web browser, which takes us to the running container (and the dev environment)

## Running the virtual environment
Once connected to ```localhost```, we then open a terminal and run the following commands:

```
python3 -m venv cs5300-venv
source cs5300-venv/bin/activate
python3 -m pip install -r requirements.txt
```

This will create the virtual environment, allow us to connect, then install the packages specified in the supplied ```requirements.txt```

## Running the tests
The ```homework1/src``` directory contains ```__init__.py```, which allows us to import our task files as a package. We move over to the homework1 directory first using:

```
cd homework1
```

We can then run the test files using:

```
python3 -m pytest tests
```

Currently, this shows that all unit tests for each task pass.
