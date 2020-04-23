# ML_Model_for_customer_segmentation_to_define_marketing_strategy
Author: Parameswara rao

Date: 05 April 2020

I implimented clustering model by using CC GENERAL.csv data set to develop a customer segmentation to define marketing strategy. This project is organized as follows:

(a) extract features from data set.
(b) data preprocessing and split into train and test data for model.
(c) basic K-means clustering model implimentation.
(D) anlyse clustering errors and segmentation process.

CC GENERAL.csv:  data set for given model.

Result:

Cluster 0 : Youth / New Working professionals
Low balance but the balance gets updated frequently ie. more no. of transactions. No of purchases from the account are also quite large and majority of the purchases are done either in one go or in installments but not by paying cash in advance.

Cluster 1 : Retired Professionals/Pensioners
Comparitively high balance but the balance does not get updated frequently ie. less no. of transactions. No. of purchases from account are quite low and very low purchases in one go or in installments. Majority of purchases being done by paying cash in advance. Purchase frequency is also quite low.

Cluster 2 : Industrialist
Balance is very high and it gets updated very frequently as well. No. of purchases are comparitively less and almost all the purchases are done with cash in advance. Purchase frequency is also quite low.

Cluster 3 : High level Businessmen
Balance is very high and it gets updated very frequently as well. no. of purchases are extremely high and majority of their purchases are done either in one-go or in installments. Purchase frequency also very high indicating purchasing happening at high frequency. Also, these have the highest credit limit.
