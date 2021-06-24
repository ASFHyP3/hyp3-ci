#!/bin/bash --login
set -e
conda activate hyp3-ci
exec python -um hyp3_ci "$@"
