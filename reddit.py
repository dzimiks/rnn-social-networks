# Downloads the top 15 posts from a
# subreddit and puts them into a text file

import praw
import json

keys = json.load(open("keys.json", "r"))

reddit = praw.Reddit(client_id     = keys["reddit"]["client_id"],
                     client_secret = keys["reddit"]["client_secret"],
                     username      = keys["reddit"]["username"],
                     password      = keys["reddit"]["password"],
                     user_agent    = keys["reddit"]["user_agent"])
appended_data = []
subreddit = reddit.subreddit("NBA")
top_python = subreddit.top(limit=15)

for submission in top_python:
    if not submission.stickied:
        appended_data.append(submission.selftext)

print("Fetching complete!")
file = open("reddit-output.txt", "w")

for item in appended_data:
    file.write("%s\n" % item)

print("Done!")