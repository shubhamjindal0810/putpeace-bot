import string
import random
import requests
import json
import re
import time
import csv

RESERVATIONID = "jind" #5to6-character reservation ID
APITOKEN = "ab116b3dffe84d4f9a7d63c61c18fe41" # Mailinator API Token

def generateString():
	return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))



while(True):
	currentEmail = generateString()
	timestamp = str(int(time.time())*1000)
	requestURL = "http://iitm.cloudapp.net/api/register/"
	verifyURL = "http://iitm.cloudapp.net/api/verify/"
	name = currentEmail
	pswd = "shubhamjindal"
	email =  currentEmail + "@mailinator.com"
	data = { 'email':email, "password":pswd, 'name':name }
	print("Signing up on " + email )
	res = requests.post(requestURL, data = data)

	#mailinatorInbox = "https://api.mailinator.com/api/inbox?to=" + currentEmail + "&token=" + APITOKEN
	print("Verifying " + email)

	json_data = json.loads( res.text )
	respo = json_data[0]
	key = respo["fields"]["verification_key"]

	url = verifyURL + key
	res2 = requests.get( url )

	print("verification done")
	with open( 'data.csv' , 'a' ) as myfile:
		myfile.write( email + '\n')
	#time.sleep(5)



	#time.sleep(5)
	#response = requests.get(mailinatorInbox)
	#while not response:
	#	time.sleep(2)
	#	response = requests.get(mailinatorInbox)
	#
	#json_data = json.loads(response.text)

#	emailID = None
#	for i in range(0, 5):
#		response = requests.get(mailinatorInbox)
#		json_data = json.loads(response.text)
#
#		for message in json_data["messages"]:
#			if message["subject"] == "PutPeace.com please verify your email to get Rs.20 Signup bonus.":
#				emailID = message["id"]
#
#		if emailID:
#			break
#
#		time.sleep(1)
#
#	if not emailID:
#		continue
#
#	mailinatorMessage = "https://api.mailinator.com/api/email?id=" + emailID + "&token=" + APITOKEN
#	response = requests.get(mailinatorMessage)
#	json_data = json.loads(response.text)
#	content = json_data["data"]["parts"][0]["body"]
#
#	m = re.search('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', content)
#	newURL = m.group(0).rstrip(".")
#	print("Sending confirmation request to " + newURL)
#	res = requests.get(m.group(0).rstrip("."))
#	print("Referral sucessfully spoofed")
#	print()
#	'1443516520-19215552-shubhamjindal0810'
#	4bd6e126-ce84-45b7-8b2d-ffcbf00c3745