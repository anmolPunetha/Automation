import time
# delete config folder to run
bot = Bot()
time.sleep(5)
bot.login(username="account", password="pswd here")
time.sleep(5)
print(1)
followers = bot.get_user_followers('account to be searched')
time.sleep(5)
print(2)
following = bot.get_user_following('account to be searched')

defaulters = []
defaulter_names = []
for x in following:
    if x in followers:
        pass
    else:
        defaulters.append(x)

for follower in defaulters:
    name = bot.get_username_from_user_id(follower)
    defaulter_names.append(name)
    print(name)

print(defaulter_names)
print(followers)
print(following)
