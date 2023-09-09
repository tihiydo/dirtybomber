# -*- coding: utf-8 -*-

import tools

class Apteka24: 
    def __init__(self, number):
        self.setResourceName('Apteka 24')
        self.setRequestUrl('https://ucb.z.apteka24.ua/api/send/otp')
        self.setRequestUserAgent('')
        self.setRequestType('POST')
        self.setRequestCookie()
        self.setRequestData('')
        self.setRequestJson( {"phone":"380995338068"} )

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

    def setRequestCookie(self, requestCookie = None):
        if requestCookie != None:
            self.requestCookie = tools.DefaultTools().reparseCookie(requestCookie)
        else:
            self.requestCookie = ""

    def setRequestData(self, requestData):
        self.requestData = requestData

    def setRequestJson(self, requestJson):
        self.requestJson = requestJson