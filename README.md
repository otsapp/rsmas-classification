# Coral classification on RSMAS dataset

- Basic coral image classification with pytorch pre-trained model and without class localisation.

#### Download Data:
`https://data.mendeley.com/datasets/86y667257h/2`
(use RSMAS directory)

#### TODO:
 - Adapt prepare_directory.py and Makefile to split images from a docker volume for local run.
 - Add logging.
 - Adapt predict module.
 - Add s3 connection for data.
 - Create AWS api endpoint.