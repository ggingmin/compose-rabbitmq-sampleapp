#!/bin/bash

set -e

for i in {1..10}
do
    python3 rpc_server.py
done