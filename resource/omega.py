# -*- coding: utf-8 -*-

import tools

class Omega: 
    def __init__(self, number):
        self.setResourceName('Omega TV')
        self.setRequestUrl('https://api.omegatv.ua/auth/in')
        self.setRequestUserAgent()
        self.setRequestType('POST')
        self.setRequestCookie()
        self.setRequestData({"phone": 380995338068, "retoken": "03ADUVZwC0VfAyiFmUyQ1U2JcPeAfLQsXD8hY9dIxpcekRNR_0udIoUoVsjkNuYuBxXSjN4vWXzzAdxchopevBS675EmPsW11_oheM_hfQe8DQHw-dEZT1KmjS_9K-iEcwgHBbL44QVHArEGwMup-CPSU28OF-P5BqzYuOo-36tRaCf6Tk7HUTTB18_XSZfDW-OVr0ge-_7Wdk5aEqHt7fIl-Xz1JDscBGucqF0Ged55Dnaysd6rBHQvLFoKhFmDEC9JObEnCAWBLWHuASOKfTR8abWzRJkmWAUd4CwYn2fvyc6lz3YEWp2LHOrYYcYfp2YuxDedgcXdUimvMBitKky_cqYZInpQ0OkNTqFcaIDAlEKZtElpp44kqV-gnkiIHEGqxnh1RghcNgHNjXA5JUNtkG8ZJ5fRybMLQjJUG4xoBTs11esUccNvs8LMdg342aUMxu75FBoOiMFeIgtZ-oJVzfezQqnjjQTqdoPCpEYxnjS2A3IzPWL6V_BMtGgjmcxy70vKldd8-6N1-JPpLQb3KzkvGSFPBWig"})
        self.setRequestJson('')

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