# Capstone: Recommender Systems and Natural Language Processessing

### Problem Statement
1. Can we use the text of user reviews to predict the scores of music albums and recommend other user albums?

### Executive Summary
Can we use the text of user reviews to predict the scores of music albums and recommend other user albums?

### File Directory / Table of Contents
Data was collected using the Pushshift API to collect posts and comments from r/science and r/technology.

##### Python notebook files:
 - 01 Data Collection for posts and comments for both subreddits:
     - 01a_Data_Collection_posts.ipynb
     - 01b_Data_Collection_comments.ipynb
 - 02 Data Cleaning
     - 02a_Data_Cleaning_posts.ipynb
     - 02b_Data_Cleaning_comments.ipynb
 - 03 EDA
     - 03a_EDA_posts.ipynb
     - 03b_EDA_comments.ipynb
 - 04 Modeling
     - 04a_Modeling_Logistic_Regression.ipynb
     - 04b_Modeling_Naive_Bayes.ipynb
     - 04c_Modeling_Decision_Trees.ipynb
     - 04d_Modeling_Boosting.ipynb

##### Files contained in the 'clen data' folder:
   - 'comments_combined_clean.csv' - Combined comment data from comments in r/science and r/technology
   - 'posts_combined_clean.csv'- Combined post data from comments in r/science and r/technology
   - 'reddit_science_clean.csv' - r/science post data after cleaning
   - 'reddit_technology_clean.csv'- r/technology post data after cleaning
   - 'science_comments_clean.csv' - r/science comment data after cleaning
   - 'technology_comments_clean.csv' - r/technology comment data after cleaning
 
### Data Dictionaries
posts_combined_clean Data Dictionary
<br>

|Feature|Type|Dataset|Description|
|---|---|---|---|
|**subreddit**|*object*|posts|Subreddit|
|**title**|*object*|posts|Post Title| 
|**author**|*object*|posts|Post Author| 
|**created_utc**|*int*|posts|Time & date of post| 
|**upvote_ratio**|*float*|posts|Ratio of upvotes to downvotes| 
|**full_link**|*object*|posts|URL link of post| 
|**num_comments**|*int*|posts|Number of comments on post at time of pull|
|**num_crossposts**|*int*|posts|Number of crossposts on post at time of pull|
|**total_awards_received**|*int*|posts|Number of awards received on post at time of pull|
|**score**|*int*|posts|Score of post at time of pull|

### Data Cleaning

The data collected with the Pushshift API created mostly-clean dataframes. There were a few columns with mostly null-values that were dropped. Duplicate posts, including a large amount of "test posts" and comments were also dropped for EDA and modeling.

### EDA

##### Posts

##### Comments

### Modeling
##### Base Model

##### Logistic Regression

##### Naive Bayes Model

##### Decision Tree Model

##### AdaBoost Model

##### Gradient Boost Model

### Conclusions and Recomendations
- The gradient boost model provides a fairly accurate classification and can be used to classify post titles from r/science and r/technology with an approximate 89% accuracy. This model performed better than the other models tested, including a Logistic Regression Model, Naive Bayes Model, Decision Tree Model, and an AdaBoost model.
- There is slightly more emphasis on politics in r/technology comments than in r/science.
- This model may aid someone looking to post in or browse these specific subreddits.
- To improve the model, we can:
    - Collect more data
    - Look at other tokenizers
    - Analyze n-grams further

### Sources
- Book Ratings Dataset:
https://www.kaggle.com/bahramjannesarr/goodreads-book-datasets-10m

- Board Game Ratings Dataset:
https://www.kaggle.com/jvanelteren/boardgamegeek-reviews

- Music Review Dataset:
Oramas, S., Espinosa-Anke L., Lawlor A., Serra X., & Saggion H. (2016).  Exploring Customer Reviews for Music Genre Classification and Evolutionary Studies. 17th International Society for Music Information Retrieval Conference (ISMIR'16).

