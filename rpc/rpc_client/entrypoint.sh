#!/bin/bash

set -e

for i in {1..10}
do
    python3 rpc_client.py
done