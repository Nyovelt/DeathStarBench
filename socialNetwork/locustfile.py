from locust import HttpUser, task, between
import random
import string
import time

START_TIME = time.time()


class MyUser(HttpUser):
    host = "http://localhost:8080"
    wait_time = between(0.1, 3)
    max_user_index = 962

    @staticmethod
    def string_random(length):
        if length > 0:
            return MyUser.string_random(length - 1) + random.choice(string.ascii_letters + string.digits)
        else:
            return ""

    @staticmethod
    def dec_random(length):
        if length > 0:
            return MyUser.dec_random(length - 1) + random.choice(string.digits)
        else:
            return ""

    @task(5)
    def compose_post(self):
        user_index = random.randint(0, self.max_user_index - 1)
        username = f"username_{user_index}"
        user_id = str(user_index)
        now = time.time()
        elapsed_time = now - START_TIME  # Calculate elapsed time since the start
        text = ""
        # Only prepend "1145141919810" to the text after 12 minutes and before 15 minutes have elapsed since the start
        if 720 <= elapsed_time < 900:  # 11 * 60 seconds = , 13 * 60 seconds = 
            text = "1145141919810"
        text += self.string_random(256)
        num_user_mentions = random.randint(0, 5)
        num_urls = random.randint(0, 5)
        num_media = random.randint(0, 4)
        media_ids = '['
        media_types = '['

        for _ in range(num_user_mentions):
            user_mention_id = random.randint(0, self.max_user_index - 1)
            while user_index == user_mention_id:
                user_mention_id = random.randint(0, self.max_user_index - 1)
            text += f" @username_{user_mention_id}"

        for _ in range(num_urls):
            text += f" http://{self.string_random(64)}"

        for _ in range(num_media):
            media_id = self.dec_random(18)
            media_ids += f'"{media_id}",'
            media_types += '"png",'

        media_ids = media_ids[:-1] + "]"
        media_types = media_types[:-1] + "]"

        payload = {
            "username": username,
            "user_id": user_id,
            "text": text,
            "media_ids": media_ids,
            "media_types": media_types,
            "post_type": "0"
        }

        self.client.post("/wrk2-api/post/compose", data=payload)

    @task(5)
    def read_user_timeline(self):
        user_id = str(random.randint(0, self.max_user_index - 1))
        # start = str(random.randint(0, 100))
        # stop = str(int(start) + 10)

        start = str(0)
        stop = str(10)

        params = {
            "user_id": user_id,
            "start": start,
            "stop": stop
        }

        self.client.get("/wrk2-api/user-timeline/read", params=params)

    @task(5)
    def read_home_timeline(self):
        user_id = str(random.randint(0, self.max_user_index - 1))
        # start = str(random.randint(0, 100))
        # stop = str(int(start) + 10)

        start = str(0)
        stop = str(10)

        params = {
            "user_id": user_id,
            "start": start,
            "stop": stop
        }

        self.client.get("/wrk2-api/home-timeline/read", params=params)

    @task(1)
    def upload_follow(self):
        user_0 = f"username_{random.randint(0, self.max_user_index - 1)}"
        user_1 = f"username_{random.randint(0, self.max_user_index - 1)}"
        payload = {
            "user_name": user_0,
            "followee_name": user_1
        }
        self.client.post("/wrk2-api/user/follow", data=payload)
