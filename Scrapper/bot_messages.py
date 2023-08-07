def greeting(firstname, lastname):
    return f'''
Greetings, <b>{firstname} {lastname}</b>! 
We warmly welcome you. Your path to searching for books on Amazon 
and generating CSV files begins with the /search command. 
We wish you a productive exploration!
'''


def mail_body(firstname, lastname):
    return f'''
    Hello, {firstname} {lastname},\n
    You've made a great choice by selecting @AmazonScrapperBot! 
We extend a warm welcome to you. Thank you! \n
    Best regards,
    Your @AmazonScrapperBot
'''
