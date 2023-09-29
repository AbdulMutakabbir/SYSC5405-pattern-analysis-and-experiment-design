# BIOM/SYSC5405 – Pattern Classification and Experiment Design

## Assignment 2

> Due: `11:00 pm Wednesday 11 Oct 2023`
> #### Instructions:
>
> * Submit a `single PDF` file with all your answers, discussion, plots, etc
> * `Include your code` either inline or in appendix
> * All plots should have `title` and `both axis` `LABELED`
> * Answers should be `ordered` from Q1 to Q6.

> Consider two possible features for a new `COVID` classification system: temperature (`T`) and respiration rate (`RR`).
> Sample data for each feature is provided in `A2Q2.csv`.
> T and RR measurements are given for 200 healthy patients and 200 covid-positive patients.
> (The file A2Q2.csv columns are: `T_healty`, `T_covid`, `RR_healty`, and `RR_covid`)


### Q1

Let’s focus on our `healthy` patients for this question. 

Create a categorical version of the temperature feature data using the rule:
```
if T_healthy <= 36.8:
  T_cat = t-normal
else:
  T_cat = t-fever
```

Now create an ordinal version of the respiration rate feature data using the rule:
```
if RR_healthy < 19.0:
  RR_ord = RR-low
else if RR_healthy < 23.0:
  RR_ord = RR-med
else:
  RR_ord = RR-high
```

Create a `contingency table` for your new data and use a `χ2 test` to check if `t_cat` is significantly correlated with `RR_ord`. 
Report your null hypothesis H0 (~15 words), your alternate hypothesis H1, your χ2 value, your degrees of freedom, your p-value, and your conclusion (~20 words).


### Q2

Compute the inter-quartile range and the `10% trimmed mean` of `T_healthy`. 
(10% means dropping the top and bottom 5% of samples)


### Q3
