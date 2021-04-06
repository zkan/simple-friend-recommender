#!/bin/bash

IP_ADDRESS=$(ip addr show | grep "\binet\b.*\bdocker0\b" | awk '{print $2}' | cut -d '/' -f 1) docker-compose up -d
cd survey && docker-compose -f local.yml up -d
