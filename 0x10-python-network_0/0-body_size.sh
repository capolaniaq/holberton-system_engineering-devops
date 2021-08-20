#!/bin/bash
# Put the cotent legnt
curl -si "$1" | grep Content-Length | cut -d " " -f2