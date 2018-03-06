# Use an official Python runtime as a parent image
FROM django

# Copy the current directory contents into the container at /app
ADD . /app

# Set the working directory to /app
WORKDIR /app

# Install any needed packages specified in requirements.txt
RUN pip3 install -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Run app.py when the container launches
CMD [ "django-admin", "startproject webapp" ]
CMD ["python3", "./manage.py runserver 0.0.0.0:8000"]
