#!/bin/bash

while getopts c:n:t: flag
do
    case "${flag}" in
        c) doc_class=${OPTARG};;
        n) doc_name=${OPTARG};;
	t) doc_type=${OPTARG};;
    esac
done


echo "Document Class: $doc_class"
echo "Document Name: $doc_name"
echo "Document Type: $doc_type"

if [[ -d "docs/$doc_class" ]]
then
  mkdir "docs/$doc_class/$doc_name"
  mkdir "docs/$doc_class/$doc_name/$doc_name"
  cp partials/doc_index_1.html "docs/$doc_class/$doc_name/index.html"
  touch "docs/$doc_class/$doc_name/$doc_name/index.html"	
  cp partials/doc_index_2.html "docs/$doc_class/$doc_name/$doc_name/index.html"
  sed -i "s/FILENAME/$doc_name.$doc_type/" "docs/$doc_class/$doc_name/$doc_name/index.html"
else
  echo "Error: could not find folder for $doc_class"
fi

