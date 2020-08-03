#!/bin/bash

if [[ "$1" == "full" ]]; then
    echo level full-speed | sudo tee /proc/acpi/ibm/fan
elif [[ "$1" == "auto" ]]; then
    echo level auto | sudo tee /proc/acpi/ibm/fan
else
    echo "something wrong"
fi
