#!/bin/bash
# Set query parameters using post request
curl -sd "email=test@gmail.com&subject=I will always be here for PLD" "$1"
