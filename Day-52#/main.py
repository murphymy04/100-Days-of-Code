from insta_follower import InstaFollower
with open("data.env", "r") as password:
    SIMILAR_ACCOUNT = "president"
    USERNAME = "pi1984_"
    PASSWORD = password.read()

bot = InstaFollower()

