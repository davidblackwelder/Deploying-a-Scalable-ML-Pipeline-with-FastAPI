# Repo link
[Githup repo](https://github.com/davidblackwelder/Deploying-a-Scalable-ML-Pipeline-with-FastAPI)



# Environment Set up (pip or conda)
- Fork the repo from above and clone the copy of the repository locally:
`git clone https://github.com/[your github username]/Deploying-a-Scalable-ML-Pipeline-with-FastAPI.git`

* Option 1: use the supplied file `environment.yml` to create a new environment with conda
* Option 2: use the supplied file `requirements.txt` to create a new environment with pip

## Project
This project contains all the files and folders you need:

`data/` : contains a `census.csv` file
`ml/` : preprocess the data
`data.py`: a script for data pre-processing
`model.py`: contains functions that train, test, and save the model
`model/` : folder to store the trained model
`model_card.md` documents the model
`environment.yml`: conda environment for setting up the environment
`train_model.py`: a script for an ML pipeline to take in the data, train the model, and save it.
`main.py`: used for creating a RESTful API using FastAPI
`local_api.py`: uses the requests module to do one POST on your live API.
`test_ml.py`: tests on the data or the model

## Run the ML pipeline
```
> python train_model.py
```
It will output log messages and performance metrics in the terminal. It will also store the performance of model slices in `slice_output.txt`.

## Run the unit tests
```
> pytest test_ml.py -v
```

## Interact with the API locally
In the terminal, run the app using the following:
```
> uvicorn main:app --reload
```

Once the API is running, open another terminal and run:
```
> python local_api.py
```