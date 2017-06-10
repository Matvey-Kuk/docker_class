#!/usr/bin/env bash

sudo /etc/init.d/nginx start;

sudo service memcached restart;

uwsgi --socket /tmp/uwsgi.sock --module Project.wsgi --chmod-socket=777 --processes=10

while true; do
sleep 300
done
