#!/bin/bash

docker-compose -f docker-compose.mac.yml up -d
cd survey && docker-compose -f local.yml up -d
