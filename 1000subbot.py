    # DISCLAIMER: YOU MUST GIVE BOT MOD ON YOUR SUBREDDIT

    # SETTINGS

    CLIENT_ID = ""                  # Type the gibberish under the app's name between the quotes.

    CLIENT_SECRET = ""              # Type the gibberish labeled "secret" on the app between the quotes.

    BOT_NAME = "1000 Sub Bot"      # Feel free to change this, it won't affect anything.

    USERNAME = ""                   # The username of the bot account.

    PASSWORD = ""                   # The password of the bot account.

    SUBREDDIT = ""                  # Your subreddit you want the bot to comment in.

    NOTIFY_NAME = ""                # Your username so the bot can notify you when the sub hits 1000.

    # CODE

    import praw, time

    num = 1
    posts = []

    reddit = praw.Reddit(client_id=CLIENT_ID,
                        client_secret=CLIENT_SECRET,
                        user_agent=BOT_NAME,
                        username=USERNAME,
                        password=PASSWORD)

    while True:
        start_time = time.time()
        for submission in reddit.subreddit(SUBREDDIT).stream.submissions():
            if not (submission.created_utc < start_time) and not (submission.title in posts):
                if submission.selftext == "":
                    if num == 1000:
                        c = submission.reply("This has been the submission #"+str(num)+" of 1000!\nThe challenge is now over@");
                    else:
                        c = submission.reply("This has been the submission #"+str(num)+" of 1000!");
                    c.mod.distinguish(how='yes', sticky=True)
                if num == 1000:
                    reddit.redditor(NOTIFY_NAME).message("Challenge Finished!", "One thousand posts have been posted and the challenge is over! I will now automatically turn off.");
                    exit()
                num += 1
                posts.append(submission.title)