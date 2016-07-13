#!/usr/bin/env python
# encoding: utf-8

from locust import HttpLocust, TaskSet

def index(l):
    l.client.get("/dev/")


class UserBehavior(TaskSet):
    tasks = {index:2}

    def on_start(self):
        index(self)

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait=5000
    max_wait=9000
