#!/bin/bash

while getopts c:n:f:t: flag
do
    case "${flag}" in
        c) doc_class=${OPTARG};;
        n) doc_name=${OPTARG};;
	f) doc_file=${OPTARG};;
	t) doc_type=${OPTARG};;
    esac
done


echo "Document Class: $doc_class"
echo "Document Name: $doc_name"
echo "Document File: $doc_file"
echo "Document Type: $doc_type"

if [[ -d "docs/$doc_class" ]]
then
  mkdir "docs/$doc_class/$doc_file"
  mkdir "docs/$doc_class/$doc_file/$doc_file"
  cp partials/doc_index_1.html "docs/$doc_class/$doc_file/index.html"
  touch "docs/$doc_class/$doc_file/$doc_file/index.html"	
  cp partials/doc_index_2.html "docs/$doc_class/$doc_file/$doc_file/index.html"
  sed -i "s/FILENAME/$doc_file.$doc_type/" "docs/$doc_class/$doc_file/$doc_file/index.html"
  echo "$doc_file, $doc_name, None, None" >> docs/$doc_class/docs.csv
else
  echo "Error: could not find folder for $doc_class"
fi

