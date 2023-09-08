# -*- coding: utf-8 -*-

import tools

class Vodafone: 

    def __init__(self, number):
        self.setResourceName('Vodafone')
        self.setRequestUrl('https://registration.vodafone.ua/api/v1/process/smsCode')
        self.setRequestUserAgent('')
        self.setRequestType('POST')
        self.setRequestCookie('session_personification=eyJpdiI6ImQvRGJhcXByVmJsMEJMODJVMzFFMVE9PSIsInZhbHVlIjoia001ME9QTDd0cXg1ZU1hLzRSdjF6QWgvQnFyRDk1VHYwaUhvV3pDWlRzRW9vL2ZWd2FRY1hHQktidGFTVE9hMFBxbEkxVllFYlVNRFhYa1lKS1lPQzVHVVlFa0FaQ1gzblBNa3IwRUVOdm89IiwibWFjIjoiOWVlZDVhNGRjOTY1ZmVmMzZkNmJmMGM2MTE5NGMzZGQ1NzBhZmIzNGI5NmM4M2JkMmY1YzY0ZTFlMzhlMTcwYyJ9; session_statistic_msisdn=eyJpdiI6IjhBMUl0eTVOd1VHWHNUS1dGdTNjNVE9PSIsInZhbHVlIjoiMXNDT3M0VU40VEovOGRVR0VZZjFaUDEvcWEzVGtDZmwvblpIVnVnKzl2cUNwSlBqbjBLU3ZoUTMzYVAyZUxuNjV0UFBvNUsvd2NNajE5TUVtN2pNVkRXQ002KzJsTnQ5WmQvVXBlT0gxNnM9IiwibWFjIjoiNTAxOWQzNTg0NzI0ZmQ5MjRmMzc5NDU2NGI3YzAyMDM1NjQyYzRjNGMyN2RiODI4N2JiYjQzMmZhMDlhNjM2MyJ9; XSRF-TOKEN=eyJpdiI6ImhsYmFqSnJWMUlPckRvQy96N3dYTFE9PSIsInZhbHVlIjoiZk91a2hWaElPQ0VTUUFxZGNUakszSmV4VnN0d0lXdWZ1S0NycVdVVHh5SFVteFdsYW5BNW9QQm93Q3FZL0VHbVRLYTk4OE1Oam1rQjhTaHpuVXg5eGZVc1ZrK0NlQzdzSFUwVHlVM05HNXcwNk0xMGVqbG9NQmJyMUZnOVlaMjAiLCJtYWMiOiIwNjMyNzdhNTY4ODFiMmUyOGU3Y2E4MDEzNTNjNzY3YzQwZGU3Zjk1M2E5MmEwMDdjOTE4M2U5ZWIxN2JiMDM4In0%3D; www_vodafone_ua_session=eyJpdiI6InJneWF3RjUxaVlaakV0QzNYQnF1RFE9PSIsInZhbHVlIjoiZVpMRHJTN3dXeTh2UkkweG9QcVo3a28xNlJXOFJ0d1loQVhmcnh6cHlDVDg3SVpTRXM5L2NETzhrZkVaL2NiYzJvenY4ZzkrUWg1Wklybkpxc3lGeFc2aFNCa0kwbUdFdks2TGpXbzV0cmE0dnBvaFJjdlNHT090bU9hZzlKNWkiLCJtYWMiOiI0ZTdlNTJlNzU0YjJhZjljMTFjNWU2NTY0NTQ1ODc2ZGU5ZjZkMWI1YzE0YTU5OTFmYmFjZmUwOWRjNzY0N2Y5In0%3D; TS01c19c0a=01289bfb4a6978d04f8d568f1e766ae9be691cdb512e16ea7eda14aaf74c5f3a4e58da0703c4efc1eb7a2e18302a75015c984a8433; _gcl_au=1.1.705683163.1668781251; _ga_XG0CR9VP14=GS1.1.1668781251.1.0.1668781255.0.0.0; _ga=GA1.2.1948763779.1668781252; _gid=GA1.2.155816310')
        self.setRequestData('')
        self.setRequestJson({"number" : number[1:]})

    def setResourceName(self, resourceName):
        self.resourceName = resourceName

    def setRequestUrl(self, requestUrl):
        self.requestUrl = requestUrl

    def setRequestUserAgent(self, requestUserAgent):
        if requestUserAgent:
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
