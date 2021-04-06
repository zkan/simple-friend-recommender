#!/bin/bash

docker-compose -f docker-compose.mac.yml stop
cd survey && docker-compose -f local.yml stop
