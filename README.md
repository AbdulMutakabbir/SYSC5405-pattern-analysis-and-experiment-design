# SYSC5405: Pattern Analysis and Experiment Design

## Assignment 3

> Due: `11:59 pm Monday 20 Nov 2023`
> #### Instructions:
> * Submit a `single PDF` file with all your answers, discussion, plots, etc on `BrightSpace and Feedback Fruits`
> * `Include your code` either inline or in appendix


### Question 1:
You decide to fit a 2D Bayesian classifier to your data, where x = [T RR], COVID is the ‘positive’ class, and we assume that p(x|ωi ) ~ N(μi ,Σi ). 
Use unbiased estimators to estimate the 2D mean and covariance matrix for each class-conditional distribution. 
Report your two estimated mean vectors and covariance matrices.

### Question 2:
COVID is happily now less prevalent than it was when the data were first collected. We can now assume that, for every one person with COVID, there are 9 people without COVID in the population. 
1. Use Bayes’ theorem to compute the posterior probability that a patient with a temperature of 37.5 degrees and a respiration rate of 23 is healthy. 
2. Determine (analytically or through trial-and-error), what is the minimum temperature at which this patient (RR=23) will be classified as having covid.

### Question 4:
For the Bayesian classifier in Q2, compute the probability that each of the 400 patients has COVID, given their observed temperature and RR. Do not report the posterior probability for each patient. Instead, plot an ROC and a P-R curve for your classifier over these 400 patients.
1. For the ROC plot, include the AUC-ROC in the title.
2. For the P-R curve, include the average precision (across all recall values) in the title.

### Question 5:
To account for the fact that the class imbalance in the deployment environment (1:9) is very different from the class imbalance among your 400 test samples (1:1), you decide to add 8 additional copies of each healthy patient to your test set leading to 2000 samples in total. 
Without ‘retraining’ your classifier, report the ROC and P-R curves for this new test set, along with ROC-AUC and average precision. Briefly discuss what changed, what didn’t, and why. 
(`75 words`)

### Question 6:
Passengers who have been granted access to the buffet but were actually sick with COVID may cause an epidemic aboard the ship. 
Which performance metric reflects the chance that a COVID-positive person was permitted to use the buffet? 
(`15 words, plus equation for performance metric`)

### Question 7:
We will now use a K-nearest-neighbour classifier to classify all passengers in the original 400-patient data set (ignore prior information). 
Report the apparent error rate for K-NN classifiers with K={1,5,15,25}. 
Which value of the hyperparameter, K, performs best and why? 
(`50 words`; reminder that you can use an existing K-NN library here...)

### Question 8:
Discuss how, in this assignment, we have committed both methodological errors of 
1. “Testing on the training set” 
2. “Training on the testing set”
(`~100 words`) 