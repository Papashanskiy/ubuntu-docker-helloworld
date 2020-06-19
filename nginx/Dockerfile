FROM nethacker/ubuntu-18-04-nginx:1.17.1
RUN apt-get update
RUN apt-get install -y apt-transport-https
RUN apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/list/*
COPY nginx.conf /etc/nginx/nginx.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]