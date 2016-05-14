FROM tiangolo/uwsgi-nginx:latest

MAINTAINER YUX <yu.xiao.fr@gmail.com>

RUN pip install --upgrade pip
RUN pip install flask
RUN pip install requests

# Add app configuration to Nginx
COPY nginx.conf /etc/nginx/conf.d/

# Copy sample app
COPY ./app /app
