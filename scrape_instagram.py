from instagrapi import Client
import instagrapi
import time
import random

cl = Client()
try:
    cl.login("username", "password")
except instagrapi.exceptions.PleaseWaitFewMinutes:
    print("Couldn't login please wait for 5 minutes")
    time.sleep(60*30)
codes = list()
with open("posts.txt", 'r') as f:
    codes = f.read().split()
random.shuffle(codes)
with open("data.csv", 'a') as f:
    for c in codes[:150]:
        print(c)
        try:
            media_code = cl.media_pk_from_code(c)
            data = (cl.media_info(media_code))
        except instagrapi.exceptions.MediaNotFound:
            print("Media not found")
            continue
        except instagrapi.exceptions.MediaUnavailable:
            print("Media unavailable")
            continue
        except instagrapi.exceptions.ChallengeUnknownStep:
            print("Login error aaaaaaaaaaaaaa...")
            continue
        except instagrapi.exceptions.PleaseWaitFewMinutes:
            print("Rated limited!!!!")
            time.sleep(30)
            continue
        print(data.code+','+str(data.like_count)+','+data.user.username+','+str(time.time())+'\n')
        f.write(data.code+','+str(data.like_count)+','+data.user.username+','+str(time.time())+'\n')
        time.sleep(1)

