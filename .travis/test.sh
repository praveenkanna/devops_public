#!/bin/bash -e
find . -name "*.py" | xargs pylint -E
