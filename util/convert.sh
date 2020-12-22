#!/bin/bash

rm raw/*.md

for filename in raw/*.ipynb; do
    jupyter nbconvert --to markdown --output-dir='raw' $filename
    done
