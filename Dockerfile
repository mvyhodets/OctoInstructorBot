FROM alpine:latest
RUN apk add --no-cache nginx
COPY nginx.conf /etc/nginx/nginx.conf
COPY ./webapp /app
EXPOSE 8080
WORKDIR /app
CMD nginx -g 'daemon off;'