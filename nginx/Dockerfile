FROM nginx:alpine
EXPOSE 80 443
# TODO: really need to expose?

RUN apk add certbot certbot-nginx
COPY nginx.conf /etc/nginx/templates/default.conf.template
COPY docker-entrypoint.d/ /docker-entrypoint.d/
RUN echo "0 0,12 * * * root certbot renew -q" | tee -a /etc/crontab > /dev/null

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["nginx", "-g", "daemon off;"]