# Steam Review Predictor

Train a basic neural network on the data available from [Steam's own API](https://partner.steamgames.com/doc/webapi) and [steamspy API](https://steamspy.com/api.php) - an API service that stores data compiled from more complicated queries to Steam's API - and come up with predictions on whether games will have received mostly positive or negative reviews overall.  

## Data review

Before beginning, visualize the data several ways to try and eyeball if there are clusters or related variables.
[Tableu](https://public.tableau.com/app/profile/aidan.lucero/viz/final-steam-data/Story1?publish=yes)

## Data

 Used a modified version of a [scraper found on Github](https://github.com/nik-davis/steam-data-science-project) to collect data from both the Steam and Steamspy APIs on 10/22/2021

The data can be found [here](https://www.dropbox.com/sh/w11p1f0q3wr1el3/AAADSXS2Znz-EBehVpXSNDNMa?dl=0)

<details>
  <summary>Data Summary</summary>

| Column Name | DataType | Source | Description |
| --- | --- | --- | --- |
| **appid** | *integer* | both | Identifier for game |
| **name** | *string* | both | Name of game |
| **developers** | *string Array* | Steam | Company(s) that developed the game |
| **publishers** | *string Array* | Steam | Company(s) that published the game |
| **positive** | *integer* | SteamSpy | Count of positive reviews on Steam |
| **negative** | *integer* | SteamSpy | Count of negative reviews on Steam |
| **owners** | *String* | SteamSpy | Integer range of total purchases for the game on Steam |
| **average_forever** | *integer* | SteamSpy | Average playtime since March 2009, in minutes |
| **average_2weeks** | *integer* | SteamSpy | Average playtime in the last two weeks, in minutes |
| **median_forever** | *integer* | SteamSpy | Median playtime since March 2009, in minutes |
| **median_2weeks** | *integer* | SteamSpy | Median playtime in the last two weeks, in minutes |
| **price** | *integer* | SteamSpy | Current US price in cents |
| **initialprice** | *integer* | SteamSpy | Original US price in cents |
| **discount** | *integer* | SteamSpy | Current discount in percents |
| **languages** | *String* | SteamSpy | List of supported languages |
| **genre** | *String* | SteamSpy | List of genres |
| **ccu** | *integer* | SteamSpy | Peak concurrent users in the previous day |
| **tags** | *JSON* | SteamSpy | Game's tags with vote counts |

</details>


## Machine Learning 

Attempt 1: 

We combined data from steam and steamspy (steamspy being another dataset with a focus on user averages and reviews separated into positive and negative columns). 

We thought the data was cleaned and when combined and dummied the data became too big. 
We also noticed that the column for supported_language in the steam data had issues regarding how languages or groups of languages were labeled creating an error when initializing standardscaler.

Attempt 2A: 

- This attempt is dropping supported_languages along with other columns in the preprocessing step. 

- Result: Failed

Attempt 2B: 

- Filtering supported_languages and grouping all occurrences of languages that occur less than 100 amount into an  “Other” category.

- Result: It failed as a similar Error occurred where string could not be converted to float


Attempt 3: 

- Filtered supported_languages, genres, and categories column and dummied them

- Realized that the original columns were still there and that was what cause the previous errors so the originals were dropped from the merge steam df

- Dropped owners column 

- Result: Code runs. Accuracy is low plateauing at around 0.046 which is extremely low. Data now has to be preprocessed further. 

Attempt 4: 

- Dropped [‘owners’, ‘average_2weeks’,’average_forever’,’median_2weeks’,’median_forever’]

- Added 2 more layers (5 total)

- Result: Accuracy ended up being the same as Attempt 3. 

Attempt 5: 

- Dropped ['required_age','supported_languages','developers','publishers','achievements','linux','mac','windows','date','owners','average_forever','average_2weeks','median_forever','median_2weeks','ccu','name']

- Created a new column called ratio(positive/negative reviews)

- Applied bins to ratio column (‘very bad’, ‘bad’, ‘below average’, ‘average’, and ‘good’)

- Created code to help dummy the columns with list 

- Realized that the original columns [‘supported_languages’, ‘genres’, ‘categories’] still remained in the new dataframe and dropped them. This fixed the error (‘String could not be converted to float’)

- Dummied the remaining columns and focused on the binned ratio column. Labeled as y_columns

- Created layers with one being a dropout layer

- Set (n2.compile(loss="mse", optimizer="adam", metrics=["accuracy"]))

- Trained model and produced accuracy of 0.42

Final Cleanup:

- Code now connect to postgres with help from helpers.py 

- dropcolumns = ['required_age','supported_languages','developers','publishers','achievements','linux','mac','windows','date','owners','average_forever','average_2weeks','median_forever','median_2weeks','ccu','name']

- Filtered out rows for column ‘Coming soon”

- Filtered out rows that did not have enough data to do predictions with 

- Bin ratio column and create bin based on results

- Convert columns with list to dummy

- Dummy remaining columns 

- Train test split

- Standardscaler

- Use a ColumnTransformer so we don't have to pass the dummy columns into the scale

- Neural networks: 

- 5 Dense layers with first four being ‘relu’ and the last being sigmoid
- The sixth layer is a dropout layer

- Result: Accuracy score is .80 or 80% accurate



