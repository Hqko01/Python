import instaloader

bot = instaloader.Instaloader()

profile = instaloader.Profile.from_username(bot.context, 'hqkko')

print("Username:", profile.username)
print("User ID", profile.userid)

print("# of followers:", profile.followers)
print("# of followees", profile.followees)