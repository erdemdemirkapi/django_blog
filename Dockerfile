FROM python:3.7

# Ensure that Python outputs everything that's printed inside 
# the application rather than buffering it
ENV PYTHONUNBUFFERED 1

# Creation of the workdir
RUN mkdir /django_blog
WORKDIR /django_blog

# Add requirements.txt file to container
ADD requirements.txt /django_blog/

# Install requirements
RUN pip install --upgrade pip
RUN pip install -r /django_blog/requirements.txt

# Add the current directory(the web folder) to Docker container
ADD . /django_blog/