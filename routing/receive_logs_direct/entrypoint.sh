#!/bin/bash

set -e

exec python3 receive_logs_direct.py info warning error
