from flask import Flask, request
import africastalking
import os

app = Flask(__name__)

username = "sandbox"
api_key = ""

africastalking.initialize(username, api_key)
sms = africastalking.SMS

@app.route('/', methods = ['POST', 'GET'] )
def ussd_callback():
	global response
	session_id = request.values.get("sessionId", None)
	service_code = request.values.get("serviceCode", None)
	phone_number = request.values.get("phoneNumber", None)
	text = request.values.get("text", "default")
	sms_phone_number = []
	sms_phone_number.append(phone_number)


	#USSD logic
	if text == "" or text == "111":
		#print main menu
		response = "CON Welcome to FarmCulture!\n"
		response += "LEARN & PRACTICE PROFESSIONAL FARMING\n"
		response += "1. GET STARTED\n"
		response += "000. EXIT\n"

	elif text == "1":
		#print menu for option 1
		response = "CON What would you like to LEARN?\n"
		response += "1. Horticultural farming\n"
		response += "2. Dairy Farming\n"
		response += "3. Beef Farming\n"
		response += "4. Poultry Farming\n"
		response += "5. Bee keeping\n"
		response += "111. Go Back\n"
		response += "000. EXIT\n"

	elif text == "000": 
		#print menu for option 2
		response = "END Thank you and Goodbye. See you soon.\n"
		

	elif text == "1*1": 
		#print menu for horticulture option
		response = "CON LEARN HORTICULTURE:\n"
		response += "1. How to cultivate Purple Tea\n"
		response += "2. How to cultivate Maize\n"
		response += "3. How to cultivate Wheat\n"
		response += "4. How to cultivate Tomatoes\n"
		response += "5. How to cultivate Kales/Sukuma Wiki\n"
		response += "6. How to cultivate Green Grams\n"
		response += "7. How to cultivate Cabbage\n"
		response += "8. How to cultivate Spinach\n"
		response += "9. How to cultivate Macademia nuts\n"
		response += "10. How to cultivate Groundnuts\n"
		response += "111. Go Back\n"
		response += "000. EXIT\n"

	elif text == "1*2":
		#print menu for dairy farming option
		response = "CON LEARN DAIRY FARMING:\n"
		response += "1. How to Dairy Cow Farming\n"
		response += "2. How to Dairy Goat Farming\n"
		response += "111. Go Back\n"
		response += "000. EXIT\n"
			
	elif text == "1*3":
		#print menu option for beef farming 
		response = "CON LEARN BEEF FARMING:\n"
		response += " .... ... .. . \n"
		response += "000. EXIT\n"

	elif text == "1*4":
		#print menu for poultry farming
		response = "CON LEARN POULTRY FARMING:\n"
		response += "1. How to Layers Farming \n"
		response += "2. How to Broiler Farming \n"
		response += "111. Go Back\n"
		response += "000. EXIT\n"

	elif text == "1*5":
		#print menu for bee keeping
		response = "CON LEARN BEE KEEPING:\n"
		response += " .... ... .. . \n"
		response += "000. EXIT\n"

	elif text == "1*1*1":
		#send an SMS to user and print success message
		pass 

	elif text == "1*1*2":
		#send an SMS to user and print success message
		pass

	else:
		response = "END Invalid input. Try again."


	return response

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=os.environ.get("PORT"), debug="true")

