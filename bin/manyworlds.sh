#!/bin/bash

TOP=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)

export LOGDIR=$HOME/.manyworlds

# create the log directory if it doesn't exist
#
if [ ! -d "$LOGDIR" ]
then
	mkdir -p "$LOGDIR"
fi

# run the manyworlds python script with the parameters from this script appended.
#
export PYTHONPATH=$TOP
#
$TOP/bin/manyworlds $*
