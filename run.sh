#!/bin/bash

mkdir -p logs

source venv/bin/activate || exit 1
pip install -r requirements.txt || exit 1

logfile=./logs/gunicorn_"$(date '+%F_%H-%M')".txt

echo "logging to: $logfile"
echo "running on: http://127.0.0.1:9289"

gunicorn \
	--workers 4 \
	--bind 127.0.0.1:9289 \
	--log-level=info \
	'main:app' &> "$logfile"

	# --log-file=./logs/gunicorn.error.log \
	# --access-logfile=./logs/gunicorn.access.log \
