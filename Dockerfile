FROM python:alpine
# install ffmpeg
RUN sudo apt install ffmpeg

# set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# expose port
EXPOSE 8000

# create and change the working directory
WORKDIR /code

# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# copy project
COPY . /code/