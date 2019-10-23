def makeUrl(urlId):
        base_url = "http://leetcode.com/problems/"
        return base_url + urlId

def getText(question):
        name = question["name"]
        url = makeUrl(urlId = question['urlId'])
        text = name + "\n" + "URL: " + url
        return text

def sendMessage(context,chat_id, text):
    return context.bot.send_message(chat_id, text)