#!/bin/bash
# This script takes in a URL and displays all HTTP methods the server will accept
curl -sI "$1" | grep -i Allow | awk '{print $2, $3, $4}' # The -i option makes the search case-insensitive
