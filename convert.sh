#!/bin/bash
for filename in raw/*.ipynb; do
    jupyter nbconvert --to markdown --output-dir='raw' $filename
    done
