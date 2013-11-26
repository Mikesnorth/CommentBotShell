import praw # you will need to download and install praw - easily done with pip
import time
import sys

# Original Author : Mike North
# Free for use by anyone for any non commercial legal purpose
# Designed as a shell to be customized and expanded upon
# For help, check the PRAW documentation at https://praw.readthedocs.org/en/latest/genindex.html
  
print("initializing")
number_of_comments_posted = 0
r_object = praw.Reddit(user_agent='bot_name_here version by /u/user_name_here') # a proper user agent prevents getting banned
time.sleep(5) # sleep to prevent hitting rate limits
print("logging in")
r_object.login('user_name', 'password') # works best if account has been verified to avoid captcha
time.sleep(5)
print("sending pm")
r_object.send_message('recipient', 'subject', 'comment bot has been activated') # optional notification that the bot is turned on
time.sleep(5)
user_to_stalk = r_object.get_redditor('user_name') # the user who's comments will be monitored
last_comment = None
new_comment = None
for comment in user_to_stalk.get_comments(limit=1): # grab their most recent comment and store it
    last_comment = comment
while True:
    time.sleep(45) # sleep to prevent hitting rate limits
    try:
        print('checking for new comment')
        for another_comment in user_to_stalk.get_comments(limit=1):
            new_comment = another_comment
        if new_comment.body != last_comment.body:
            new_comment.reply('comment to leave') # post a reply to the new comment
            last_comment = new_comment
            print('reply posted')
            number_of_comments_posted += 1
            print('Comments posted:', number_of_comments_posted)
        else:
            print('no new comment found')
    except:
        print('Error: ', sys.exc_info()[0])
r_object.send_message('recipient', 'subject', 'comment bot has been deactivated') # optional noficication that the bot has been terminated
print("Finished")
