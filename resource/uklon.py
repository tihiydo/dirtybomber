# -*- coding: utf-8 -*-

import tools

class Uklon: 
    def __init__(self, number):
        self.setResourceName('Uklon')
        self.setRequestUrl('https://rider.uklon.com.ua/api/v1/phone/send-code')
        self.setRequestUserAgent('')
        self.setRequestType('POST')
        self.setRequestCookie()
        self.setRequestData('')
        self.setRequestJson( {'username': number} )

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