#!/bin/bash
# This script takes in a URL, sends a DELETE request to the URL, and displays the body of the response
curl -sL "$1" -X DELETE
