#!/bin/sh

set -e

postgres_host=$1
postgres_port=$2
shift
shift

exec ./wait-for-it.sh $postgres_host:$postgres_port -t 0 && sleep 20

exec "$@"
