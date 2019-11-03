#!/bin/bash

docker build -t kendalls-flask-sandbox .
docker run -d -p 5000:5000 kendalls-flask-sandbox
