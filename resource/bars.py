# -*- coding: utf-8 -*-

import tools

class Bars: 
    def __init__(self, number):
        self.setResourceName('BARSGroup')
        self.setRequestUrl('https://barsgroup.com.ua/api/sendSms')
        self.setRequestUserAgent()
        self.setRequestType('POST')
        self.setRequestCookie('token=')
        self.setRequestData('')
        self.setRequestJson({"phoneNumber": number})

    def setResourceName(self, resourceName):
        self.resourceName = resourceName

    def setRequestUrl(self, requestUrl):
        self.requestUrl = requestUrl

    def setRequestUserAgent(self, requestUserAgent = None):
        if requestUserAgent != None:
            self.requestUserAgent = requestUserAgent
        else:
            self.requestUserAgent = tools.DefaultTools().randomUserAgent()

    def setRequestType(self, requestType):
        self.requestType = requestType

    def setRequestCookie(self, requestCookie):
        self.requestCookie = tools.DefaultTools().reparseCookie(requestCookie)

    def setRequestData(self, requestData):
        self.requestData = requestData

    def setRequestJson(self, requestJson):
        self.requestJson = requestJson