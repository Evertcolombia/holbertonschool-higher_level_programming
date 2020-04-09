#!/usr/bin/env bash
# script that sendt a request  POST wuth variables
curl "$1" -X POST -d "email=hr@holbertonschool.com" -d "subject=I will always be here for PLD"
