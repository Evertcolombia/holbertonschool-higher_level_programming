#!/usr/bin/env bash
# send a header variable with a request "X-HolbertonSchool-User-Id"
curl "$1" -X GET -H "X-HolbertonSchool-User-Id: 98"
