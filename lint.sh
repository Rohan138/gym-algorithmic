#!/usr/bin/env bash

python3 -m pip install pytest black
python3 -m black .
python3 -m pytest .
