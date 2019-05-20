# sentiment-analysis
Perform sentiment analysis on tweets using a twitter API.

Analyze the pubic sentiment about Stefanos Tsitsipas and Roger Federer.
The tennis match took place on January 20 2019, so the considered dates for this task were from January 16 to January 22, 
in order to have a picture on how the public feels about those two players before and after the match.
The tweets were extracted using the tweepy library and some key featured were stored in an SQLite database.
The sentiment was extracted using the TextBlob library.
