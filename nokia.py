
print ( """
--------Menu Functions--------

1. Phone book
2. Messages
3. Chat
4. Call register
5. Tones
6. Settings
7. Call divert
8. Music
9. Games
10. Calculator
11. Reminders
12. Clock
13. Profiles
14. Services
15. SIM services
""")

menu_function = int(input('Choose your preferred option: '))

match menu_function:
    case 1:
		print ("""
--------PHONE BOOK MENU-------- 

1. Search
2. Service Nos.
3. Add name
4. Erase
5. Edit
6. Copy
7. Assign tone
8. Send b’card
9. Options
10.Speed dials
11. Voice tags
""")

		phonebook_menu = int(input('Choose your preferred option: '))

		match phonebook_menu:

			case 1;
				print("This is your desired name and phone number")
			case 2:
				print("Your service number is 09035521486")
			case 3:
				print("Name and Phone number saved successfully")
			case 4:
				print("Name and Phone number deleted successfully")
			case 5:
				print("Name and Phone number edited successfully")
			case 6:
				print("Name and Phone number copied successfully")
			case 7:
				print("Your desired ringing tone has been assigned successfully")
			case 8:
				print("Your desired name and phone number as a business card")
			case 9:
				print("""
---OPTIONS MENU---
1.Memory in use
2.Type of view
3.Memory status
""")


				option_menu = int(input('Choose your preferred option: '))

				match option_menu:

					case 1 -> System.out.println("Select your choice of memory either your phone SIM card")
					case 2 -> System.out.println("Select your choice of display mode for your saved phone nymbers and names")
					case 3 -> System.out.println("This the number of times you can still save names and phone numbers and the ones you've saved in your Phone and SIM card")

						
					
			case 10:
			    print("Select your desired number for speed dial")
			case 11:

				print("""
-------VOICE TAGS MENU-------

1. Record a voice tag
2. Make a call using a voice

							
				voice_tags = int(input('Choose your preferred option: '))
				match voice_tags:
				
					case 1:
					    print("Select your desired name and phone number and record a voice tag");
					case 2:
					    print("Say your desired voice tag")

						
				
	case 2: 	
		print ("""

----------MESSAGE MENU----------

1. Write messages
2. Inbox
3. Outbox
4. Picture messages
5. Templates
6. Smileys
7. Message settings
8. Info service
9. Voice mailbox number 
10. Service command edit

""")
					
		message_menu = int(input('Choose your preferred option: '))

		match message_menu:
		
			case 1:
			    print("Write and send a message")
			case 2:
			    print("These are your inbox messages")
			case 3:
			    print("These are your outbox messages")
			case 4:
			    print("You can send and view picture messages")
			case 5:
			    print("These are your message templates")
			case 6:
			    print("These are your smileys")
			case 7:
						
				print("""

---Message settings menu---

1. Set 1. Message centre number
2. Messages sent as
3. Message valid1
2. Common
""")

				message_settings = int(input('Choose your preferred option: '))

				match message_settings:
                    case 1:
						print("""

---------SET 1 MENU---------

1. Message centre number
2. Messages sent as
3. Message validity

""")

						set1_menu = int(input('Choose your preferred option: '))

						match set1_menu:

							case 1:
							    print("This is your message centre number")
							case 2:
							    print("Select your preferred message format")
							case 3:
							    print("Select your preferred validity period")
						
							
                    case 2:

						print("""

---------COMMON MENU--------

1. Delivery reports
2. Reply via same centre
3. Character su

""")

						common_menu = int(input('Choose your preferred option: '))

			            match common_menu:
							case 1:
							    print("Request the network for your message delivery reports")
							case 2:
							    print("Allow to send replies through the same centre")
							case 3:
							    print("Allow the sending of messages using special characters")
									
						
								
            case 8:
                print("This is the information service")
			case 9:
			    print("This is your voice mailbox number")
			case 10:
			    print("Send service request to your service provider")
						
				
					
			
			
    case 3:
        print("You can start a conversation")

	case 4:
		print ("""

-----CALL REGISTER MENU-----

1. Missed calls
2. Received calls
3. Dialled numbers
4. Erase recent call lists
5. Show call duration
6. Show call costs
7. Call cost settings
8. Prepaid credit
""")
 
		call_register = int(input('Choose your preferred option: '))

		match call_register:
			case 1:
			    print("Your missed calls")
			case 2:
			    print("Your received calls")
			case 3:
			    print("Numbers you have Dialed")
			case 4:
			    print("Delete your recent call list")
			case 5:
			   			print("""
-------CALL DURATION MENU--------

1. Last call duration
2. All calls’ duration
3. Received calls’ duration
4. Dialled calls’ duration
5. Clear timers
""")
                
				call_duration = int(input('Choose your preferred option: '))

				match call_duration:
					case 1:
						print("This is the time spent on the last call")
					case 2:
						print("This is the time spent on all calls")
					case 3:
						print("This is the time spent on calls answered")
					case 4:
						print("This is the time spent on calls you made")
					case 5:
						print("Reset call timers")

			case 6:
			    print("""
-----CALL COSTS MENU-----

1. Last call cost
2. All calls’ cost
3. Clear counters
""")
        		call_costs = int(input('Choose your preferred option: '))

		        match call_costs:
			        case 1:
				        print("This is the amount spent on the last call")
			        case 2:
				        print("This is the amount spent on all calls")
			        case 3:
				        print("Reset cost counter")

			case 7:
			    print("""
						
----CALL COST SETTING MENU----
1. Call cost limit
2. Show costs in
""")

				call_costs_settings = int(input('Choose your preferred option: '))

				match call_costs_settings:
					case 1:
						print('Choose your preferred call cost limit')
					case 2:
						print('Choose your charging unit(units of currency)')
			
			case 8:
				print("This is your prepaid credit page")
				
    case 5:
		print ("""

------TONES MENU------

1. Ringing tone
2. Ringing volume
3. Incoming call alert
4. Message alert tone
5. Keypad tones
6. Warning tones
7. Vibrating alert
8. Screen saver
""")

		tones_menu = int(input('Choose your preferred option: '))

		match tones_menu:
			case 1:
			    print("Choose your preferred ringing tone")
			case 2:
			    print("Adjust your ringing volume")
			case 3:
			    print("Adjust your incoming call alert")
			case 4:
			    print("Choose your preferred message alert tone")
			case 5:
			    print("Adjust your keypad volume")
			case 6:
			    print("Choose your warning tones")
			case 7:
			    print("Adjust your vibrating alert")
			case 8:
			    print("Choose your preferred picture shown on standby mode")
				
				
    case 6 -> {
		print ("""

-----SETTINGS MENU------

1. Call settings
2. Phone settings
3. Security settings
4. Restore factory settings
""")

		
 
		settings_menu = int(input('Choose your preferred option: '))

		match settings_menu:
			case 1:
                print("""
-----CALL SETTINGS MENU-----

1. Automatic redial
2. Speed dialling
3. Call waiting options
4. Own number sending
5. Phone line in use
6. Automatic answer 
""")
 
				call_settings = int(input('Choose your preferred option: '))

				match call_settings:

					case 1:
					    print("Set automatic redial");
					case 2:
					    print("Turn speed dialing on or off");
					case 3:
					    print("Manage your call waiting options");
					case 4:
					    print("Choose whether your number is shown when you call");
					case 5:
					    print("Choose which phone line to use");
					case 6:
					    print("Set your phone to answer an incoming call after one ring")
					
			case 2 -> {
				print("""

-----PHONE SETTINGS MENU-----

1. Language
2. Cell info display
3. Welcome note
4. Network selection
5. Confirm SIM service actions
""")
 
				phone_settings = int(input('Choose your preferred option: '))

				match phone_settings:

					case 1:
					    print("Select your preferred language")
					case 2:
					    print("Set phone to show when it is used in a cellular network")
					case 3:
					    print("YWrite a welcome note to be displayed when your phone is switched on")
					case 4:
					    print("Select your preferred network")
					case 5:
					    print("Set the phone to show or hide confirmation messages when you use SIM services")
					
					
			case 3:
				print("""

-----SECURITY SETTINGS MENU-----

1. PIN code request
2. Call barring service
3. Fixed dialling
4. Closed user group
5. Security level
6. Change access codes
""")

 
				security_settings = int(input('Choose your preferred option: '))

				match security_settings:
					case 1:
					    print("Set your PIN")
					case 2:
					    print("Manage the call barring service")
					case 3:
					    print("Turn fixed dialling on or off")
					case 4:
					    print("Choose who you can call and who can call you")
					case 5:
					    print("Set security level for new SIM cards")
					case 6:
					    print("Change the security code, PIN code, PIN2 code, or barring password")
						
					
					
			case 4:
			    print("Restore your phone to its factory settings")
			
			
	case 7:
	    print("Divert your calls")

	case 8:
	    print("""
-----MUSIC MENU-----

1. Music player
2. Radio
3. Recorder
4. Track list
""")
        music_menu = int(input('Choose your preferred option: '))

		match music_menu:
		    case 1:
		        print("Turn the music player on or off")
		    case 2:
		        print("Listen to the radio. \nConnect a headset first")
		    case 3:
		        print("Choose how to record audio")
		    case 4:
		        print("This is your track list")
				
			
	case 9:
	    print("This is the games application")
			
	case 10:
	    print("This is the calculator")

	case 11:
	    print("These are your reminders")

	case 12:
        print ("""

------CLOCK MENU------
1. Alarm clock
2. Clock settings
3. Date setting
4. Stopwatch
5. Countdown timer
6. Auto update of date and time
""")

		clock_menu = int(input('Choose your preferred option: '))

		match clock_menu

			case 1:
			    print("Set your alarm")
			case 2:
			    print("Adjust your clock settings")
			case 3:
			    print("Set the correct date")
			case 4:
			    print("Start the stopwatch")
			case 5:
			    print("Set the counter to sound an alarm when it reaches your selected time")
			case 6:
			    print("Turn auto update of time and date on or off")
			
	case 13:
	    print("Manage your profiles")

	case 14:
	    print("""
----------------WAP SERVICES----------------

1. Basic steps for accessing and using a WAP service
2. Setting up the phone for a WAP ervice
3. Making a connection to a WAP service
4. Browsing the pages of a WAP service
5. Ending a WAP connection
6. Adjusting the appearance settings of WAP pages 
7. Saving and managing bookmarks
8. Emptying the cache memory 
9. Having a WAP connection and a voice call in progress at the same time
10. Security certificates
""";
 
		wap_services = int(input('Choose your preferred option: '))

        match wap_services:
			case 1:
			    print("These are the basic steps for accessing and using a WAP service")
			case 2:
			    print("Set up the phone for a WAP service")
			case 3:
			    print("Choose to activate your preferred WAP service")
			case 4:
			    print("These are the pages of a WAP service")
			case 5:
			    print("End a WAP connection")
			case 6:
			    print("Adjust the appearance settings of WAP pages");
			case 7:
			    print("Save and manage your bookmarks")
			case 8:
			    print("Empty the cache memory")
			case 9:
			    print("Use a WAP connection during a voice call(available only for USSD bearers)")
			case 10 :
			    print("These are the security certificates")	
					
			
	case 15:
		print("These are your SIM services")






