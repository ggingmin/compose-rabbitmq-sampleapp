#!/bin/bash

set -e

for i in {1..10}
do
    python3 new_task.py Message-$i
done

