# Code Samples

Three samples covering causal inference, predictive modeling, and data linking/analysis in Python.

## 1. `IV_analysis.ipynb`: Effect of Grid Electricity on Small-Firm Revenue (Causal Inference)

Compares naive, exact-matching, and instrumental variables (2SLS) estimates of the effect of grid connection on revenue for 2,500 small and medium enterprises, using a randomly assigned connection subsidy as the instrument. Covers covariate balance, the first stage (instrument strength), the reduced form, and the limits of the IV estimate (LATE, exclusion restriction, external validity).

Built for a Program Evaluation course using an instructional dataset. Tools: pandas, statsmodels, linearmodels.

## 2. `logistic_regression_ML.ipynb`: Predicting Mental Health Treatment-Seeking in Tech (Machine Learning)

Logistic regression model predicting whether tech workers have sought mental health treatment, using the OSMI Mental Health in Tech survey (~1,100 responses). Includes train/test evaluation, a regularization check with cross-validation, and interpretation of coefficients. This is my portion of a team project that also compared random forest and XGBoost models. Tools: pandas, scikit-learn.

## 3. `index.py`: Green Space Accessibility in Chicago (Data Linking & Analysis)

A geospatial data-linking and scoring pipeline I built with three team members, to measure green space access for ~500 affordable housing units in Chicago. Combines spatial buffering and fuzzy name matching (Jaro-Winkler) to link park polygons to Yelp/Google review data, then computes a composite accessibility score weighted by park size and review quality.

Full project + repo: https://github.com/begumakkas/Green-Space-Access
