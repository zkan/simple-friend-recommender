#!/bin/bash

docker-compose up -d
cd survey && docker-compose -f local.yml up -d
