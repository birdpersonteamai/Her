# Twitter Dataset
twitter dataset link:
https://github.com/Marsan-Ma/chat_corpus/raw/master/twitter_en.txt.gz

Paste the text file for the dataset in this folder.

For example, for twitter dataset: place twitter-en.txt to this folder.

# Reddit Dataset
## Original Texts

If you prefer modify the current way to clean and categrize data, the raw data link is at:
https://mega.nz/#!2PIRQDzC!8ip7GxOV-flXERLsh-lGnC6bD9OBuQSA_pRRIoKBx7s

Heades are:

```
'text', 'id', 'subreddit', 'meta_label', 'time', 'author', 'ups', 'downs', 'authorlinkkarma', 'authorcommentkarma', 'authorisgold'
```

- `text`: text of the comment
- `id`: unique ID of the comment
- `subreddit`: subreddit that the comment belongs to
- `meta_label`: meta tag assigned to the subreddit of the comment
- `time`: timestamp of the comment
- `author`: username of the author of the comment
- `ups`: number of ups the comment has received
- `downs`: number of downs the comment has received
- `authorlinkkarma`: the author's link karma
- `authorcommentkarma`: the author's comment karma
- `authorisgold`: `1` if the author has gold status, `0` otherwise

Unzip the zip file and place the file `raw_reddit_data.csv` in this folder, and you can
modify file `clean_reddit_data.py` to get customized clean data.

If nothing is modified from the `clean_reddit_data.py` , execute it and you will get the cleaned data
that are saved in the folder called `reddit_dataset`.

More details of cleaned data are described in below.


## Cleaned Data

Cleaned Reddit dataset link:
https://mega.nz/#!fCRwxY6I!Ei9ZOPviuUq6K-zJVRcr9jbylOwFEzqCR9lKfXR0s3o

Unzip the zip file and paste the folder `reddit_dataset` in this folder.

The `.txt` files are categorized by meta label with subreddit and named as `<meta_label>_<subreddit>.txt`.
- `meta_label`: meta tag assigned to the subreddit of the comment
- `subreddit`: subreddit that the comment belongs to

The contents of each file now only contain id and text.

Headers are:
```
'id', text
```

- `id`: unique ID of the reddit comment
- `text`: text of the comment
