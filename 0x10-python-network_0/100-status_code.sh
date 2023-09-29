#!/bin/bash
# Bash script sends a request to a URL passed as an argument, and displays only the status code of the response
curl -sL -w "%{http_code}" "$1"