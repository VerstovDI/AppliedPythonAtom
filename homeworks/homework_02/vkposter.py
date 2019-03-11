#!/usr/bin/env python
# coding: utf-8


from homeworks.homework_02.heap import MaxHeap
from homeworks.homework_02.fastmerger import FastSortedListMerger


class VKPoster:

    def __init__(self):
        self.p_posts = dict()  # Dict: "Key: user_id, Value: post_id"
        self.r_posts = dict()  # Dict: "Key: user_id, Value: post_id"
        self.subs = dict()  # Dict: "Key: follower_id, Value: followee_id"

    def user_posted_post(self, user_id: int, post_id: int):
        if user_id not in self.p_posts:
            self.p_posts.setdefault(user_id, [])
            self.p_posts[user_id].append(post_id)
        else:
            self.p_posts.setdefault(user_id, [])
            self.p_posts[user_id].append(post_id)

    def user_read_post(self, user_id: int, post_id: int):
        if user_id not in self.r_posts:
            self.r_posts.setdefault(user_id, [])
            self.r_posts[user_id].append(post_id)
        else:
            temp = list(self.r_posts.pop(user_id))
            if post_id not in temp:
                temp.append(post_id)
                self.r_posts[user_id] = temp
            else:
                self.r_posts[user_id] = temp

    def user_follow_for(self, follower_user_id: int, followee_user_id: int):
        if follower_user_id not in self.subs:
            self.subs.setdefault(follower_user_id, [])
            self.subs[follower_user_id].append(followee_user_id)
        else:
            self.subs.setdefault(follower_user_id, [])
            self.subs[follower_user_id].append(followee_user_id)

    def get_recent_posts(self, user_id: int, k: int)-> list:
        tape_list = []
        followees_list = self.subs.get(user_id)
        for i in followees_list:
            if i in self.p_posts:
                tape_list += self.p_posts.get(i)

        tape_list.sort()
        tape_list = tape_list[-k:]
        tape_list = tape_list[::-1]
        return tape_list

    def get_most_popular_posts(self, k: int) -> list:
        tmp_list = []
        res_list = []
        for i in self.r_posts:
            temp_list = self.r_posts.get(i)
            res_list += self.r_posts.get(i)

        res_list.sort()
        frequency = dict.fromkeys(res_list, 0)
        cnt = 0
        for j in res_list:
            if j in frequency:
                cnt = frequency.get(j) + 1
                frequency.update({j: cnt})

        tmp_list = list(frequency.items())
        tmp_list = \
            sorted(tmp_list, key=lambda tup: (tup[1], tup[0]), reverse=True)
        tmp_list = [x[0] for x in tmp_list]
        output_list = tmp_list[:k]
        return output_list
