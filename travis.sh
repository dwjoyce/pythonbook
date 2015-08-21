#!/bin/bash

if [ "$BUILD_MODE" = "build" ];
    then
        echo "Building"
        bash deploy.sh
        exit $?
fi;

if [ "$BUILD_MODE" = "test" ];
    then
        echo "Testing"
        make pythontest
        exit $?
fi;
