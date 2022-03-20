NER_DATASETS = {
    "ncbi": {
        # "data_dir": "/home/suching/scibert/data/ner/NCBI-disease/",
        "data_dir": "datasets/NCBI-disease/"
    },
    "sciie": {
        # "data_dir": "/home/suching/scibert/data/ner/sciie/"
        "data_dir": "datasets/sciie/"
    },
    "jnlpba": {
        # "data_dir": "/home/suching/scibert/data/ner/JNLPBA/"
        "data_dir": "datasets/jnlpba/"
    },
    "bc5cdr": {
        # "data_dir": "/home/suching/scibert/data/ner/bc5cdr/"
        "data_dir": "datasets/bc5cdr/"
    }
}


CLASSIFICATION_DATASETS = {
    "hatespeech": {
        # "data_dir": "s3://suching-dev/textcat/twitter/hatespeech/",
        "data_dir": "datasets/hatespeech/"
    },
    "ag": {
        # "data_dir": "s3://suching-dev/textcat/news/ag/"
        "data_dir": "datasets/ag/"
    },
    "scicite": {
        # "data_dir": "s3://suching-dev/textcat/science/sci-cite/",
        "data_dir": "datasets/sci-cite/"
    },
    "citation_intent": {
        #"data_dir": "s3://suching-dev/textcat/science/citation_intent/"
        "data_dir": "datasets/citation_intent/"
    },
    "chemprot": {
        # "data_dir": "s3://suching-dev/textcat/science/chemprot/"
        "data_dir": "datasets/chemprot/"
    },
    "sciie": {
        # "data_dir": "s3://suching-dev/textcat/science/sciie/",
        "data_dir": "datasets/sciie/"
    },
    "hyperpartisan_news": {
        # "data_dir": "s3://suching-dev/textcat/news/hyperpartisan_by_article/",
        "data_dir": "datasets/hyperpartisan_news/"
    },
    "biased_news": {
        # "data_dir": "s3://suching-dev/textcat/news/biased_news/",
        "data_dir": "datasets/biased_news/"
    },
    "imdb": {
        # "data_dir": "s3://suching-dev/textcat/reviews/imdb/",
        "data_dir": "datasets/imdb/"
    },
    "amazon": {
        # "data_dir": "s3://suching-dev/textcat/reviews/amazon/",
        "data_dir": "datasets/amazon/"
    },
    "yelp": {
        # "data_dir": "s3://suching-dev/textcat/reviews/yelp/",
        "data_dir": "datasets/yelp/"
    },
    "twitter_sentiment": {
        # "data_dir": "s3://suching-dev/textcat/twitter/semeval_2017_ task_4A/",
        "data_dir": "datasets/semeval_2017_ task_4A/"
    },
    "twitter_irony_task_a": {
        # "data_dir": "s3://suching-dev/textcat/twitter/semeval_2018_task3_irony_detection/task_a/",
        "data_dir": "datasets/semeval_2018_task3_irony_detection/"
    },
    "twitter_irony_task_b": {
        # "data_dir": "s3://suching-dev/textcat/twitter/semeval_2018_task3_irony_detection/task_b/",
        "data_dir": "datasets/semeval_2018_task3_irony_detection/"
    },
    "rct-20k": {
        # "data_dir": "s3://suching-dev/textcat/science/rct-20k/",
        "data_dir": "datasets/rct-20k/"
    },
    "cs-abstruct": {
        # "data_dir": "s3://suching-dev/textcat/science/csabstruct-reformat/",
        "data_dir": "datasets/csabstruct-reformat/"
    }
}


DATASETS = {"NER": NER_DATASETS, "CLASSIFICATION": CLASSIFICATION_DATASETS}
