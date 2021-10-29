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

In this section we applied machine learning after preprocessing the data on the ratio column to predict which games would succeed or rather have a better positive to negative review ratio.

- At the start of this part of the project we experienced several issues with our data being too big/messy resulting in extremely large dummy data and as such our results produced extremely low accuracy scores after training (ranging around 0.046)

- After fixing an issue with the columns being unable to be trained and preproccessing the data again we were able to produced a better accuracy score ranging around 40-60% 

- Eventually we were able to clean up our data further by dropping more columns, applying filters, creating bins, and creating a function to deal with the columns with lists. This in turn allowed us to achieve an accuracy score of 80%

- Result of Final Code: Accuracy score is .80 



