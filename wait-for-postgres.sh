#!/bin/sh

postgres_host=$1
postgres_port=$2

exec ./wait-for-it/wait-for-it.sh $postgres_host:$postgres_port -t 0
