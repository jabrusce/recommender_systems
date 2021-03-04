# Recommender Systems and Natural Language Processessing

### Problem Statement
> This project explores the use of natural language processessing to provide recommendations to a user. Specifically, it uses a dataset of album reviews and uses natural language processesing techniques to create a set of albums a user may be interested in by exploring the similarities and sentiments of the text in the album reviews.

### Executive Summary
> Can we use the text of user reviews to predict the scores of music albums and recommend other user albums?

> The dataset used for NLP in this project consists of over 18,000 album reviews from Pitchfork. The recommender system makes use of natural language processessing (NLP) techniques and cleaning functions to explore similarity in the text reviews. Similarities are calculated using Spacy's similaritiy score. Sentiment and polarity scores are calculated using the Valence Aware Dictionary and sEntiment Reasoner (Vader) library.

> This project also analyzes how well machine learning methods can predict the scores and sentiment of reviews through several regression models.

> Recommendation systms for books and board games based on user reviews was also created using collaborative filtering. These functions were included in a streamlit app for recommending books and board games.

<br>

### File Structure

#### Data Sources
**Music Data**

Pitchfork Reviews dataset: 
- https://www.kaggle.com/nolanbconaway/pitchfork-data

Amazon Music Reviews dataset:
- https://s3.amazonaws.com/amazon-reviews-pds/readme.html

**Book Data**
- Goodreads Book Datasets with User Rating 10M:
- https://www.kaggle.com/bahramjannesarr/goodreads-book-datasets-10m?select=user_rating_0_to_1000.csv
- Dataset consists of 51,945 user reviews, 834 unique users, and 24,094 books.

**Board Game Data**
- BoardGameGeek Reviews:
- https://www.kaggle.com/jvanelteren/boardgamegeek-reviews
- Due to memory issues and file sizes, data used in recommender consists of 100K of the 15M reviews, 62,902 unique reviews, and 1,743 board game titles.


##### Python notebook files:
 - 01 Music Dataset
     - 01a_music_data_collection.ipynb
     - 01b_music_eda.ipynb
     - 01c_music_recommender.ipynb
     - 01d_music_modeling.ipynb
 - 02 Book Dataset
     - 02a_book_data_collection.ipynb
     - 02b_book_eda.ipynb
     - 02c_book_recommender.ipynb
 - 03 Board Game Dataset
     - 03a_game_data_collection.ipynb
     - 03b_game_eda.ipynb
     - 03c_game_recommender.ipynb
 - 04 Music Dataset (user reviews)
     - 04a_music_user_rev_collection.ipynb
     - 04b_music_user_rev_recommender.ipynb

<br>

##### Data files contained in the project folder:
Data Folder:
- Raw data was downloaded from the above sources. The large datafile for the Amazon music reviews was opened and cleaned in Google Colab.
- Due to the large file sizes associated with recommender systems, the dataframes were created locally and pickled. These files were larger than Github's maximum 100MB limit, so they are not included in this repo. 
- For the Streamlit app, pickle files were created in 02c_book_recommender and 03c_game_recommender.
 
##### Data Dictionaries
<br>

|Feature|Type|Dataset|Description|
|---|---|---|---|
|**reviewid**|*int*|music|Review ID|
|**score**|*float*|music|Review Score (1-5)| 
|**title**|*object*|music|Album Title| 
|**artist**|*object*|music|Artist| 
|**url**|*object*|music|Web address of review| 
|**content**|*object*|music|Review (raw text)| 
|**genre**|*object*|music|Genre of album|
|**year**|*float*|music|Year Released|
|**cleaned_content**|*float*|music|Review (cleaned text)|
|---|---|---|---|
|**book_name**|*object*|books|Book Title|
|**book_id**|*int*|books|Book ID| 
|**user_id**|*int*|books|User Id| 
|**rating**|*int*|books|User Rating| 
|---|---|---|---|
|**book_name**|*object*|books|Book Title|
|**book_id**|*int*|books|Book ID| 
|**user_id**|*int*|books|User Id| 
|**rating**|*int*|books|User Rating| 
|---|---|---|---|
|**user**|*int*|board games|User ID|
|**rating**|*float*|board games|User rating| 
|**comment**|*object*|board games|User comment| 
|**ID**|*int*|board games|Board Game ID| 
|**name**|*object*|board games|Board Game Title|
|**minplayers**|*int*|board games|Minimum Players| 
|**maxplayers**|*int*|board games|Maximum Players| 
|**playingtime**|*int*|board games|Recommended Playing Time| 
|**usersrated**|*int*|board games|Number of user ratings| 
|**average**|*float*|board games|Average user rating| 

<br>

### Data Cleaning

Due to the large file sizes and natural language processessing libraries, most data collection and cleaning was done using Google Colab. Most dataframes were relatively clean. Most dataframes had to be scaled down to run locally in the recommender functions.

<br>

### EDA & Recommender Systems

##### Music Reviews
>Scores are distributed farily normally, skewed to the left (most scores fall between 6 and 8). Data has imbalanced genre class - most reviews are from "rock", followed by "electronic" music. Most reviews are approximately 3,000 - 4,000 words long and consist of approximately 700 words.

>The most common words accross all reviews (note that this is taken from a subset of the full dataset, n=2000) are words such as: 'album', 'music', 'band', etc. The most common bigrams consist of words such as: 'sounds like', 'hip hop', 'sounds like', and 'title track'. The most common trigrams consist of words such as 'self titled debut' and 'new york city'.

>In addition, after trial and error, it seems that if you split the reviews into 4 distinct groups using the LDA technique (lambda = ~0.2), where we can see clear groupings of reviews: electronic/dance, rap/hip hop, metal, indie/country, with overlap between the metal and country categories.

##### Book Recommendations
>The dataset contained 834 unique users and 24094 book titles. Most ratings were a 3 or higher.

Similarities between the recommender and books found similar on Goodreads.com:
> To Kill a Mockingbird -- *The Great Gatsby, The Catcher in the Rye, Animal Farm, Lord of the Flies*

>1984 -- *Catcher in the Rye Fahrenheit 451 Brave New World Lord of the Flies*

>The Fellowship of the Ring -- *The Two Towers, The Hobbit, or There and Back Again*

>Life of Pi -- *The Kite Runner, Memoirs of a Geisha, The Curious Incident of the Dog in the Night-Time, Water for Elephants*

##### Board Game Recommendations
>The distribution of ratings was fairly normal and skewed to the left. This dataset had 283,232 unique reviwes and contained 18,889 board game titles. When building the recommendation system, the size of the dataframe was reduced to 100,000 reviews (62,815 unique reviewers and 1,743 board game titles.)

> Compared to boardgamegeek's website and similar games/'fans also like', this recommender had slightly different results. There were some similar results such as searching for '7 Wonders' had similar results by recommending 'Dominion'. Overall, the differences in recommendations may be due to scaling the data due to memoriy issue and file sizes. In addition, this recommender does not take into account the 'type' of board game. Future work may include adding a board game "type" filter.

### NLP Recommendation System & Modeling

>The music recommender is able to recommend other titles based on the review text. This recommender makes use of the Spacy library to find 'similarities' in the review text. A vector is created between the user input album title and all other album titles. The recommender then points to the 5 highest 'similarity' scores. There is also a genre filter so the recommendations are within the same genre as the user input.

>When testing this against some well known albums, there seem to be recommendations that would be expected. For example, with Daft Punk's album Random Access Memories as the input, the recommender has an album by Justice, a similar electronic artist. Similarly, an input of Kendrick Lamar's album recommends albums by Run the Jewels, Kanye West, and Macklemore. An input of Bon Iver recommends another band with similar members, Volcano Choir.

>The second recommendation includes a 'sentiment' score. This recommender system analyzes the overall sentiment and polarity score using the Vader libary. This function creates an overall 'enginered score' that is a combination of the similarity score, sentiment score, and polarity score. This gives interesting results because the polarity and sentiment score may affect an albums' overall score in relation to another album.

>Overall these recommendations may be subjective so future work may include testing between different user preferences. To validate some of the NLP discussed, regression and classification models were used to predict review score based on the review text, as discussed below.

##### Null Model
>The null model was calculated to have a rmse score of 0.54 and a balanced accuracy score of 0.5 when modeling on a sampled subset of the larger dataframe. When balanced classes are used for modeling, the Null model was calculated to have an rmse score of 0.71 and a balanced accuracy score of 0.5.

##### Modeling
>The modeling was conducted as a regression problem as well as a classificaiton problem. In the regression models, the scores were rounded and set to a scale of 1-5. 5000 samples were collected for modeling. For the classificaiton models, a score of 4 or 5 was class 1 and a score of 1 to 3 was class 0. 2500 reviews were collected from each class for these models. The best model made use of lemmatization and a Tfidf function with stop words. This was passed through a pipeline with Logistic Regression and had an rmse score of 0.49 and a balanced accuracy score of 0.61. These metrics are better than the null model. Other models used included Kneighbors Classifier with CountVectorizer, Voting Classifier, and KMeans

<br>

### Conclusions and Recomendations
>NLP can be a viable option in recommendation systems. The output for this NLP recommender may be subjective to the user whether or not they are 'good' recommendations. However, this method of content-based filtering may be an alternative to collaborative filtering based on the use case or data available. In addtion, there may be other uses for this type of NLP as well such as evaluating text based reviews into potential metrics for companies to evaluate customer happiness, for example. Future work may include increasing the model performances, adding more 'filters' to the recommendation system, and improving the model based on user feedback.