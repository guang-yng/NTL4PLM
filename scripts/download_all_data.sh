#!/bin/bash
for dataset in chemprot rct-20k citation_intent sciie hyperpartisan_news ag amazon imdb 
do
    bash $(pwd)/scripts/download_data.sh $dataset
done