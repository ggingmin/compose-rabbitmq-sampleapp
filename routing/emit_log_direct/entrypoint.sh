#!/bin/bash

set -e

for i in {1..10}
do
    python3 emit_log_direct.py
done