# -*- coding: utf-8 -*-

import tools

class Biua: 
    def __init__(self, number):
        self.setResourceName('BI UA')
        self.setRequestUrl('https://bi.ua/api/v1/accounts')
        self.setRequestUserAgent('')
        self.setRequestType('POST')
        self.setRequestCookie()
        self.setRequestData('')
        self.setRequestJson( {'grand_type': 'call_code', 'stage':'1', 'login':tools.DefaultTools().randomFirstName(), 'phone': str(number[1:]) })

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