# Model Card

## Model Details
David Blackwelder created the model on Feb 6, 2024. It uses the sklearn (1.0.2) [RandomForestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier) for the model.

## Intended Use

### Primary intended uses
This model can be used to predict the probabiliyt of individuals earning over $50K annually based on the provided census data.

### Primary intended users:
This model is intended to be used as a learning resource on building machine learning models for students and other individuals interested in learning about machine learning.

### Out-of-scope uses:
This model should not be used for research or for help in making decisions in real-life.

## Training Data
The original dataset from Udacity consisted of 32,561 rows, and a 80-20 split was used to break this into a train and test set. The features used included: "workclass", "education", "marital-status", "occupation", "relationship", "race", "sex", and "native-country".

## Evaluation Data

### Dataset
The data was obtained from Udacity which was a subset of the [Census Income dataset](https://archive.ics.uci.edu/dataset/20/census+income).

## Metrics
The metrics used were precision, recall, and F1.
Precision: 0.7279
Recall: 0.6246
F1: 0.6723
The file `slice_output.txt` contains the metrics for each individual slice.

## Ethical Considerations
This model does take into account several features that could add biases such as race and sex.

This dataset is not a representation of the population as a whole.

The F1 score of 0.6723 shows that the model does not get the predictions on income correct all the time. Therefore, this model should not be used to make assumptions about the population as a whole.

## Caveats and Recommendations
This dataset contains historical data and may not represent the current trend.
Bias in the data could lead to skewed predicitions which could impact underrepresented groups.

Users should use the results of the model's predictions only in the context of the current limitations and biases.