from flask import Flask, request
import requests
import json

############## Bot details ##############

bot_name = 'psychobot@webex.bot'
#roomId = 'Y2lzY29zcGFyazovL3VzL1JPT00vZGFjMzdkZTItMTg3Ny0zMmJjLTlhM2UtZjQ4NWNiYzE5YmU5'
token = 'NzUxNzU1OTgtYTQzYy00ZDk4LWEzMzEtYjliN2EwNmVhNjczN2JiODQxNzItNjM0_PF84_ebdf3b62-c327-4af2-8733-10d8711bb8cd'
header = {"content-type": "application/json; charset=utf-8",
          "authorization": "Bearer " + token}

############## Flask Application ##############
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def sendMessage():
	webhook = request.json
	url = 'https://webexapis.com/v1/messages'
	msg = {"roomId": webhook["data"]["roomId"]}
	sender = webhook["data"]["personEmail"]
	message = getMessage()
	if (sender != bot_name):

		if (message == "Hi"):
			msg["markdown"] = "Welcome to **Psycho Bot**!  \n I am here to help you to improve your psychological state and to cheer you up :-) \n Please choose your current mood from the list below: \n- Happy \n- Sad \n- Depressed \n- Anxious \n- Excited \n- Relaxed \n- Angry"
		elif (message == "Help"):
			msg["markdown"] = "\n- Happy \n- Sad \n- Depressed \n- Anxious \n- Excited \n- Relaxed \n- Angry"
		elif (message == "Angry"):
			msg["markdown"] = "Here is a piece of advice to cope with anger"
			msg["files"] = "https://www.verywellmind.com/thmb/X5nn__vUZfc4rw6D2JA477tT7sM=/1500x1000/filters:no_upscale():max_bytes(150000):strip_icc()/anger-management-strategies-4178870-478b9bc1a2b648a7b4bcbe7934591cf5.png"
		elif (message == "Anxious"):
			msg["markdown"] = "Here is a piece of advice to cope with anxiety"
			msg["files"] = "https://www.verywellmind.com/thmb/t45CRRuibSKE7oZow0JPm9j-yq4=/1500x1000/filters:fill(ABEAC3,1)/manage-your-anxiety-2584184-01-07daf91ba6de41d19f827cf65ceef07a.png"
		elif (message == "Depressed"):
			msg["markdown"] = "Here is a piece of advice to cope with depression"
			msg["files"] = "https://www.verywellmind.com/thmb/jvPSqUAQQWqTqoYHrpKgBPk3JW4=/1500x1000/filters:no_upscale():max_bytes(150000):strip_icc()/tips-for-living-with-depression-1066834_final-ee85ce7306304e3ba1577ca31c04e266.png"
		elif (message == "Sad"):
			msg["markdown"] = "Here is a piece of advice to cope with sadness"
			msg["files"] = "https://www.fabhow.com/wp-content/uploads/2017/05/intro-how-to-deal-with-sadness.jpg"
		elif (message == "Happy"):
			msg["markdown"] = "Great! Keep it up!"
			msg["files"] = "https://64.media.tumblr.com/e1a4d453da642002131dc30f843f69c2/tumblr_oizh2rEtjC1v1z098o1_400.gifv"
		elif (message == "Excited"):
			msg["markdown"] = "Happy to share your excitement!"
			msg["files"] = "https://shelliekennedy.files.wordpress.com/2019/01/UnrealisticFilthyBullfrog-size_restricted.gif"
		elif (message == "Relaxed"):
			msg["markdown"] = "The time to relax is when you don't have time for it!"
			msg["files"] = "https://media.tenor.com/images/215f59b653aa5693e03be0117f97021f/tenor.gif"
		else:
			msg["markdown"] = "Sorry! Try to choose the mood that correspond the most to your current state. \n Type **Help** to see the list of available commands."
		requests.post(url,data=json.dumps(msg), headers=header, verify=True)

def getMessage():
	webhook = request.json
	url = 'https://webexapis.com/v1/messages/' + webhook["data"]["id"]
	get_msgs = requests.get(url, headers=header, verify=True)
	message = get_msgs.json()['text']
	return message

app.run(debug = True)
