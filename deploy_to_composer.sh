#!/bin/bash

gsutil -m rsync -d -r ./dags gs://"${COMPOSER_BUCKET}"/dags