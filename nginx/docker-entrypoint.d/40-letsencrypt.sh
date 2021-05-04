#!/bin/sh
# certbot --nginx -n -d $HOST --email $EMAIL --agree-tos
certbot certonly --standalone -n -d $HOST --email $EMAIL --agree-tos