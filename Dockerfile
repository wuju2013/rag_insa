# Use an official Python runtime as a parent image
FROM python:3.11.5-bookworm

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Define environment variable
#ENV NAME World

# Run app.py when the container launches
CMD streamlit run streamlit_app.py