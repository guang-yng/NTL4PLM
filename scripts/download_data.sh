dataset=$1

mkdir -p $(pwd)/datasets/${dataset}
curl -Lo $(pwd)/datasets/${dataset}/train.jsonl https://allennlp.s3-us-west-2.amazonaws.com/dont_stop_pretraining/data/${dataset}/train.jsonl
curl -Lo $(pwd)/datasets/${dataset}/dev.jsonl https://allennlp.s3-us-west-2.amazonaws.com/dont_stop_pretraining/data/${dataset}/dev.jsonl
curl -Lo $(pwd)/datasets/${dataset}/test.jsonl https://allennlp.s3-us-west-2.amazonaws.com/dont_stop_pretraining/data/${dataset}/test.jsonl
