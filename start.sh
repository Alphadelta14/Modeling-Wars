#!/bin/bash
CDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

export PYTHONPATH=$CDIR
python web/main.py