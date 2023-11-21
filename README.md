# SYSC5405: Pattern Analysis and Experiment Design

## Assignment 4 

> Due: `11:59 pm Monday 20 Nov 2023`
> #### Instructions:
>
> * Submit a `single PDF` file with all your answers, discussion, plots, etc on `BrightSpace and Feedback Fruits`
> * `Include your code` either inline or in appendix

> You are given a 3-class dataset of 300 homes labelled by their overall energy efficiency: 0=low, 1=med, 2=high. 
> Each home is described using five features that can be measured from an instrumented vehicle parked on the street in front of the home. 
> Our goal is to develop a diagnostic tool that will classify each house.

### Part 1:
Load the dataset in `A4.txt`. 
The column names correspond to the five features plus the class ID: `colNames = ['Thermal', 'Area', 'Glazing', 'Clading', 'Roofing', 'Efficiency']`

### Part 2:
Split your data into train/test using a `75/25` split and `stratified sampling`. 
Report the number of samples from each class in your train and test subsets.

### Part 3:
Using the training set, for each feature, `plot` the feature distribution for each class. 
You can either use five histograms or five 1D kernel density plots. Label each sub-plot by the feature `name`. 
The distribution of feature values should be visible for all three (potentially overlapping) classes on each of the five plots.
`Which feature looks most useful and why`?
`Which home efficiency class do you think 
will have the lowest accuracy and why`? 
(`60 words max`)

### Part 4:
Complete 5-fold-cross-validation over the train subset using an SVM classifier with a polynomial kernel with degree=3 and C=0.8. 
Report the accuracy over each fold, the average accuracy across all five folds, and the standard deviation across the five accuracy measurements.

### Part 5:
Train another SVM model (same kernel & C) on all of your training samples. 
Test on the test subset. 
Report the accuracy on the test subset. Does it fall within 1 standard deviation of the average accuracy observed in [Part 4](https://github.com/AbdulMutakabbir/SYSC5405-pattern-analysis-and-experiment-design/tree/assignment_4#part-4)?

### Part 6:
For this question only, assume that the misclassification costs are as follows:

|            |      |      |Actual|      |
|------------| :--: | :--: | :--: | :--: |
|            |      | Low  | Med  | High |
|            | Low  |  0   |  1   |  2   | 
| Prediction | Med  |  1   |  0   |  1   | 
|            | High |  2   |  1   |  0   | 

1. What is your total misclassification cost for the test set predictions from [Part 5](https://github.com/AbdulMutakabbir/SYSC5405-pattern-analysis-and-experiment-design/tree/assignment_4#part-5) above?
2. How could you incorporate this loss information into your classifier design? (`60 words`)

### Part 7:
Using 5-CV across only the training subset, perform a hyperparameter sweep of the number of hidden nodes in a 3-layer feedforward neural network. 
Report your accuracy for `numH=[1, 10, 100]` hidden nodes. 
Use the ‘adam’ solver, a hyperbolic tangent activation function for the hidden layers.

### Part 8:
Returning to [Part 3](https://github.com/AbdulMutakabbir/SYSC5405-pattern-analysis-and-experiment-design/tree/assignment_4#part-3), compare a naïve Bayes classifier trained using only the ‘most useful’ feature to a naïve Bayes classifier trained using all five features. 
Describe how you split/used your data, how you tested the hypothesis (null hypothesis, alternative hypothesis, test metric, etc.), what p-value you 
obtained, and your conclusion.

