# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.7-slim

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

# Install production dependencies.
#RUN apt-get update
#RUN apt-get install -y libglib2.0-0 libsm6 libxext6 libxrender-dev
RUN apt-get update
RUN apt-get install -y libsm6 libxext6 libxrender-dev libgl1-mesa-glx libglib2.0-0
RUN pip install Flask gunicorn chardet click dominate future idna itsdangerous MarkupSafe numpy Pillow==7.2.0 requests==2.24.0 torch torchvision urllib3==1.25.10 Werkzeug==1.0.1 opencv-python scipy


# Run the web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 1000 app:app