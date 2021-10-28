# Steam-Recommender

Recommend new video games based of user data and other users with similar tastes

Our group will make a model that will take data and predict whether a game will do well. It
will use STEAMSPY API as a data source. We will scrape data from the STEAMSPY API such as critic score, game sales, genre, system requirements, tags for multiplayer, etc.
Using this data we will apply ML to predict whether a game will be successful or not as determine by either scores or sales.
We will then use Tableau to demonstrate our results.
We will use ML(scikit learn), pandas, postgress, and visualization using Tableau.

Tableu link: https://public.tableau.com/app/profile/aidan.lucero/viz/final-steam-data/Story1?publish=yes

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


