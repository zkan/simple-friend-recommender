#!/bin/bash

docker-compose stop
cd survey && docker-compose -f local.yml stop
