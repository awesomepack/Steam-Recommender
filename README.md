# Steam Review Predictor

Train a basic neural network on the data available from [Steam's own API](https://partner.steamgames.com/doc/webapi) and [steamspy API](https://steamspy.com/api.php) - an API service that stores data compiled from more complicated queries to Steam's API - and come up with predictions on whether games will have received mostly positive or negative reviews overall.  

## Data review

Before beginning, visualize the data several ways to try and eyeball if there are clusters or related variables.
[Tableu](https://public.tableau.com/app/profile/aidan.lucero/viz/final-steam-data/Story1?publish=yes)

# Data Storage

## Data

 Used a modified version of a [scraper found on Github](https://github.com/nik-davis/steam-data-science-project) to collect data from both the Steam and Steamspy APIs on 10/22/2021

The data can be found [here](https://www.dropbox.com/sh/w11p1f0q3wr1el3/AAADSXS2Znz-EBehVpXSNDNMa?dl=0)

## PostgreSQL

The use of a relational database management system (PostgreSQL) was chosen to host our data because the structure was pre-defined by our API source. Since the number of records does not exceed a million records storing the dataset in the cloud was overwritten.

## Database Script

[create_schemas.py](create_schemas.py):

* Initialize user's local instance of PostgreSQL with database `Steam_Recommender`
* Creates and populates Tables in `Steam_Recommender` by looping through csv files in a datafolder
  * Default datafolder is `./data`
  * Tables primary key expected to be `appid`

# Machine Learning

## [Jupyter Notebook](ratings_ratio_predictions.ipynb)

In this section we applied machine learning after preprocessing the data on the ratio column to predict which games would succeed or rather have a better positive to negative review ratio.

* At the start of this part of the project we experienced several issues with our data being too big/messy resulting in extremely large dummy data and as such our results produced extremely low accuracy scores after training

* After fixing an issue with the columns being unable to be trained and preproccessing the data again we were able to produced a better accuracy score

* Eventually we were able to clean up our data further by dropping more columns, applying filters, creating bins, and creating a function to deal with the columns with lists. This allowed us to achieve an even greater accuracy.

# Data Summary

<details>
  <summary>App List</summary>

| Column Name | DataType | Source | Description |
| --- | --- | --- | --- |
| **appid** | *integer* | both | Identifier for game |
| **name** | *string* | both | Name of game |

</details>

<details>
  <summary>Steam Data</summary>

| Column Name | DataType | Source | Description |
| --- | --- | --- | --- |
| **appid** | *integer* | both | Identifier for game |
| **required_age** | *integer* | Steam | Minimum age the game is appropriate for based on ESRB recommendations |
| **supported_languages** | *string array* | Steam | List of supported languages |
| **developers** | *string array* | Steam | Company(s) that developed the game |
| **publishers** | *string array* | Steam | Company(s) that published the game |
| **categories** | *string array* | Steam | List of categories the game belongs to |
| **genres** | *string array* | Steam | List of genres the game belongs to |
| **achievements** | *integer* | Steam | Count of achievements available in the game |
| **linux** | *integer* | Steam | 1 if the game has Linux support, 0 otherwise |
| **mac** | *integer* | Steam | 1 if the game has MacOS support, 0 otherwise |
| **windows** | *integer* | Steam | 1 if the game has Windows support, 0 otherwise |
| **price** | *integer* | Steam | Price in US Cents to buy the game |
| **coming_soon** | *boolean* | Steam | Flag for if the game is coming soon |
| **date** | *date* | Steam | Release date |

</details>

<details>
  <summary>Steam Description</summary>

| Column Name | DataType | Source | Description |
| --- | --- | --- | --- |
| **appid** | *integer* | both | Identifier for game |
| **detailed_description** | *string* | Steam | Full description of the game |
| **about_the_game** | *string* | Steam | Short description of the game |
| **short_description** | *string* | Steam | First 350 characters of **detailed_description** |

</details>

<details>
  <summary>Steam Media</summary>

| Column Name | DataType | Source | Description |
| --- | --- | --- | --- |
| **appid** | *integer* | both | Identifier for game |
| **header_image** | *string* | Steam | URL of image to use for the header image |
| **screenshots** | *JSON* | Steam | Set of IDs and URLs for screenshots |
| **background** | *string* | Steam | URL of image to use for the background image |
| **movies** | *JSON* | Steam | Set of IDs and URLs for movies |

</details>

<details>
  <summary>Steam Requirements</summary>

| Column Name | DataType | Source | Description |
| --- | --- | --- | --- |
| **appid** | *integer* | both | Identifier for game |
| **pc_requirements** | *JSON* | Steam | --- |
| **mac_requirements** | *JSON* | Steam | --- |
| **linux_requirements** | *JSON* | Steam | --- |
| **minimum** | *string* | Steam | --- |
| **recommended** | *string* | Steam | --- |

</details>

<details>
  <summary>Steam Support Info</summary>

| Column Name | DataType | Source | Description |
| --- | --- | --- | --- |
| **appid** | *integer* | both | Identifier for game |
| **website** | *string* | Steam | --- |
| **support_url** | *string* | Steam | --- |
| **support_email** | *string* | Steam | --- |

</details>

<details>
  <summary>Steamspy Data</summary>

| Column Name | DataType | Source | Description |
| --- | --- | --- | --- |
| **appid** | *integer* | both | Identifier for game |
| **positive** | *integer* | SteamSpy | Count of positive reviews on Steam |
| **negative** | *integer* | SteamSpy | Count of negative reviews on Steam |
| **owners** | *string* | SteamSpy | Integer range of total purchases for the game on Steam |
| **average_forever** | *integer* | SteamSpy | Average playtime since March 2009, in minutes |
| **average_2weeks** | *integer* | SteamSpy | Average playtime in the last two weeks, in minutes |
| **median_forever** | *integer* | SteamSpy | Median playtime since March 2009, in minutes |
| **median_2weeks** | *integer* | SteamSpy | Median playtime in the last two weeks, in minutes |
| **price** | *integer* | SteamSpy | Current US price in cents |
| **initialprice** | *integer* | SteamSpy | Original US price in cents |
| **discount** | *integer* | SteamSpy | Current discount in percents |
| **languages** | *string* | SteamSpy | List of supported languages |
| **genre** | *string* | SteamSpy | List of genres |
| **ccu** | *integer* | SteamSpy | Peak concurrent users in the previous day |
| **tags** | *JSON* | SteamSpy | Game's tags with vote counts |

</details>
