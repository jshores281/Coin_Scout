from pycoingecko import CoinGeckoAPI
from datetime import date
import time, os, sys, smtplib, datetime
import subprocess, traceback, getpass



COIN_LOG = "COIN-LOG.txt"
FILE = os.path.join(os.getcwd(), COIN_LOG)


ct = datetime.datetime.now()
cur_time = ct.strftime("%H:%M:%S")
today = date.today()
d1 = today.strftime("%m/%d/%Y")



cg = CoinGeckoAPI()
def coinprice(coin_price):
	exc_type, exc_value, exc_traceback = sys.exc_info()
	S_DTAILS = repr(traceback.format_tb(exc_traceback))
	#print(S_DTAILS)
	cntr = 0
	COIN_NAME3 = coin_price.get(cred_coin.COIN[:])
	VALUE0 = float(COIN_NAME3.get(cred_coin.CURRENCY[:]))
	while True:
		# MAKE TIME CHECK VARIABLE
		time.sleep(1)
		price1 = coin_price.get(cred_coin.COIN[:])
		VALUE = price1.get(cred_coin.CURRENCY[:])
		# find percentage difference or compare to percentage increase 

		if VALUE > VALUE0 + cred_coin.PRICE_POINT:
			INC_PRICE = VALUE-VALUE0
			cp = float('{0:.3f}'.format(((float(VALUE)-float(VALUE0))/float(VALUE0))*100))
			perc = str("%")
			for COIN_NAME2 in coin_price:
				PRICE_REPORT = "\n***%s***\nOriginal value = %s\n\n-INCREASED BY: \n%s or +%s%s \n~~~SELL~~~ \n" % (COIN_NAME2,VALUE0,INC_PRICE,cp,perc)
			try:
				coin_price = cg.get_price(ids=cred_coin.COIN, vs_currencies=cred_coin.CURRENCY)
				COIN_NAME1 = coin_price.get(cred_coin.COIN[:])
				VALUE0 = COIN_NAME1.get(cred_coin.CURRENCY[:])
				
				PRICE_UPDATE = "\nUPDATING STARTING PRICE: \n%s = %s\n" % (COIN_NAME2, VALUE0) 
				#STATUS_UPDATE = (f'{PRICE_REPORT}{PRICE_UPDATE}')
				print(f'-----------------------------\n{PRICE_REPORT}{PRICE_UPDATE}\n-----------------------------\n',
					f'ATTEMPING TO SEND PRICE ALERT MSG')			
				
				SUBJECT = str("COIN SCOUTING: %s \n\n" % COIN_NAME2)
				BODY = str(PRICE_REPORT + PRICE_UPDATE)
				notify_user(cred_enter.EMAIL_ADDR, 
							cred_enter.EMAIL_PASS, 
							cred_enter.EMAIL_SRVR, 
							cred_enter.EMAIL_PORT, 
							cred_enter.RECV_ADDR, 
							SUBJECT, BODY)
			except OSError:
				dis_con313 = ("DISCONNECTED: 313~~RETRYING CONNECTION~~")
				exc_type, exc_value, exc_traceback = sys.exc_info()
				S_DTAILS = repr(traceback.format_tb(exc_traceback))
				ct = datetime.datetime.now()
				cur_time = ct.strftime("%H:%M:%S")
				today = date.today()
				d1 = today.strftime("%m/%d/%Y")
				with open(FILE, "a") as file:
					file.write(f'[{d1}]::[{cur_time}]::[COM=CONNECTION-STATUS]~~~~ERROR == {dis_con313}\n[DETAILS]::{S_DTAILS}\n')
				print(f'{dis_con313}')

		if VALUE < VALUE0 - cred_coin.PRICE_POINT:
			DEC_PRICE = VALUE0-VALUE
			cp = float('{0:.3f}'.format(((float(VALUE)-float(VALUE0))/float(VALUE0))*100))
			perc = str("%")
			for COIN_NAME2 in coin_price:
				PRICE_REPORT = "\n***%s***\nOriginal value = %s\n\n-DECREASED BY: \n%s or %s%s \n~~~BUY~~~ \n" % (COIN_NAME2,VALUE0,DEC_PRICE,cp,perc)
			try:
				coin_price = cg.get_price(ids=cred_coin.COIN, vs_currencies=cred_coin.CURRENCY)
				COIN_NAME1 = coin_price.get(cred_coin.COIN[:])
				VALUE0 = COIN_NAME1.get(cred_coin.CURRENCY[:])
				
				PRICE_UPDATE = "\nUPDATING STARTING PRICE: \n%s = %s\n" % (COIN_NAME2, VALUE0)
				#STATUS_UPDATE = (f'{PRICE_REPORT}{PRICE_UPDATE}')
				print(f'-----------------------------\n{PRICE_REPORT}{PRICE_UPDATE}\n-----------------------------\n',
					f'ATTEMPING TO SEND PRICE ALERT MSG')
				SUBJECT = str(f"COIN SCOUTING: {COIN_NAME2} \n\n")
				BODY = str(PRICE_REPORT + PRICE_UPDATE)
				notify_user(cred_enter.EMAIL_ADDR, 
							cred_enter.EMAIL_PASS, 
							cred_enter.EMAIL_SRVR, 
							cred_enter.EMAIL_PORT, 
							cred_enter.RECV_ADDR, 
							SUBJECT, BODY)
			except OSError:
				dis_con323 = ("DISCONNECTED: 323~~RETRYING CONNECTION~~")
				exc_type, exc_value, exc_traceback = sys.exc_info()
				S_DTAILS = repr(traceback.format_tb(exc_traceback))
				ct = datetime.datetime.now()
				cur_time = ct.strftime("%H:%M:%S")
				today = date.today()
				d1 = today.strftime("%m/%d/%Y")
				with open(FILE, "a") as file:
					file.write(f'[{d1}]::[{cur_time}]::[COM=CONNECTION-STATUS]~~~~ERROR == {dis_con323}\n[DETAILS]::{S_DTAILS}\n')
				print(f'{dis_con323}')
		for COIN_NAME1 in coin_price:
			for CRNCY1 in price1:
				yield cntr, COIN_NAME1, CRNCY1, VALUE0, VALUE
				cntr += 1
				print(f"LOOP COUNT = {cntr}",'\n'*5)

				if cntr % 10==False:
					try:
						print(f'-----------------------------\n~~!!~~STARTING PRICE------1\n{COIN_NAME1}\n{VALUE0}')
						coin_price = cg.get_price(ids=cred_coin.COIN, vs_currencies=cred_coin.CURRENCY)
						COIN_NAME = coin_price.get(cred_coin.COIN[:])
						VALUE = COIN_NAME.get(cred_coin.CURRENCY[:])
						print(f'\n~~!!~~UPDATED PRICE------2\n{COIN_NAME1}\n{VALUE0}\n')
						time.sleep(2)
					except OSError:
						dis_con333 = ("CONNECTION DISCONNECTED: 333~~RETRYING CONNECTION~~")
						exc_type, exc_value, exc_traceback = sys.exc_info()
						S_DTAILS = repr(traceback.format_tb(exc_traceback))
						ct = datetime.datetime.now()
						cur_time = ct.strftime("%H:%M:%S")
						today = date.today()
						d1 = today.strftime("%m/%d/%Y")
						with open(FILE, "a") as file:
							file.write(f'[{d1}]::[{cur_time}]::[COM=CONNECTION-STATUS]~~~~ERROR == {dis_con333}\n[DETAILS]::{S_DTAILS}\n')
						while True:
							print(f'{dis_con333}')
							time.sleep(1)
							api_call(cred_coin.COIN, cred_coin.CURRENCY)
				
def mon_run():
	for cntr, COIN_NAME1, CRNCY1, VALUE0, VALUE in api_call.coin_mon:
		print(f'\n-----------------------------\n',
			f'\nCOIN SCOUT: MONITOR-MODE\n\n'
			f"~COIN LIST\n"
			f"\nCOIN NAME = {COIN_NAME1}\n", 
			f"CURRENCY  = {CRNCY1}\n",
			f"CURRENT VALUE = {VALUE}\n", 
			f"+/- PRICE POINT = {cred_coin.PRICE_POINT}\n\n",
			f"COIN = {COIN_NAME1}\n",
			f"START PRICE = {VALUE0}\n\n",
			f'-----------------------------\n')

# email to sms function
def notify_user(EMAIL_ADDR, EMAIL_PASS, EMAIL_SRVR, EMAIL_PORT, RECV_ADDR, SUBJECT, BODY):
	with smtplib.SMTP(cred_enter.EMAIL_SRVR, cred_enter.EMAIL_PORT) as smtp:
		smtp.ehlo()
		smtp.starttls()
		smtp.ehlo()
		smtp.login(cred_enter.EMAIL_ADDR, cred_enter.EMAIL_PASS)
		login_log = smtp.login(cred_enter.EMAIL_ADDR, cred_enter.EMAIL_PASS)
		print("SERVER LOGIN RESPONSE: ",'\n',login_log)
		subject = SUBJECT
		body = BODY
		MSG = ("From: %s\r\n" % cred_enter.EMAIL_ADDR
             + "To: %s\r\n" % cred_enter.RECV_ADDR
             + "Subject: %s\r\n" % subject
             + "\r\n"
             + body)
		smtp.sendmail(cred_enter.EMAIL_ADDR, cred_enter.RECV_ADDR, MSG)
		print("\nSENDING EMAIL TO %s\n" % cred_enter.RECV_ADDR)
		time.sleep(5)


def api_call(COIN, CURRENCY):
	exc_type, exc_value, exc_traceback = sys.exc_info()
	S_DTAILS = repr(traceback.format_tb(exc_traceback))
	#all_dtails = traceback.print_stack()
	try:
		while True:
			pinger = cg.ping()
			con_msg = ("CONNECTED TO COINGECKO!!!  LETS GOOOOO")
			if pinger == pinger:
				print(con_msg, pinger)
				time.sleep(2)
			ct = datetime.datetime.now()
			cur_time = ct.strftime("%H:%M:%S")
			today = date.today()
			d1 = today.strftime("%m/%d/%Y")
			with open(FILE, "a") as file:
				file.write(f'[{d1}]::[{cur_time}]::[COM=CONNECTION-STATUS]~~~~SUCCESS == {con_msg}{pinger}\n[DETAILS]::{S_DTAILS}\n')#[ALL-DETAILS]::{all_dtails}')
			coin_price = cg.get_price(ids=COIN, vs_currencies=CURRENCY)
			api_call.coin_mon = coinprice(coin_price)
			mon_run()
	except OSError:
		dis_con2 = ("DISCONNECTED: 2~~NO INTERNET CONNECTION~~")
		exc_type, exc_value, exc_traceback = sys.exc_info()
		S_DTAILS = repr(traceback.format_tb(exc_traceback))	
		#all_dtails = traceback.print_stack()	
		ct = datetime.datetime.now()
		cur_time = ct.strftime("%H:%M:%S")
		today = date.today()
		d1 = today.strftime("%m/%d/%Y")
		with open(FILE, "a") as file:
			file.write(f'[{d1}]::[{cur_time}]::[COM=CONNECTION-STATUS]~~~~ERROR == {dis_con2}\n[DETAILS]::{S_DTAILS}\n')#[ALL-DETAILS]::{all_dtails}')
		while True:
			print(f"{dis_con2}")
			time.sleep(1)
			api_call(COIN, CURRENCY)
			break



def cred_enter():
	# GLOBAL VARIABLES
	os.system("cls")
	print("""
--------------------------------------
 COIN SCOUT CRYPTO MONITORING SYSTEM 
--------------------------------------
""")	
	print("~ENTER YOUR EMAIL OR SMS INFO~", '\n'*2)


	EMAIL_SENDER = input("EMAIL: ")
	EMAIL_PASSWORD = getpass.getpass(prompt="Password: ", stream=None)
	pass_len = ("#"*len(EMAIL_PASSWORD))
	EMAIL_SMTP_SRVR = input("SMTP SERVER: ")
	EMAIL_SMTP_PORT = input("SMTP SERVER PORT: ")
	


	RECV_PHONES = input("ENTER EMAILS OR CELL # WITH SMS-GATEWAY: ")
	# can now add multiple receiptant address's (more than one emails)
	RECV_PHONES = RECV_PHONES.split(",")

	cred_enter.EMAIL_ADDR = EMAIL_SENDER
	cred_enter.EMAIL_PASS = EMAIL_PASSWORD
	cred_enter.EMAIL_SRVR = EMAIL_SMTP_SRVR
	cred_enter.EMAIL_PORT = EMAIL_SMTP_PORT
	cred_enter.RECV_ADDR = RECV_PHONES
	# RECV_ADDR = f'{RECV_PHONE}{SMS_GATE}'


	print("\n","---------------------------------------","\n",
		"CONFIRMATION FORM","\n"*2,
		"EMAIL = %s" % cred_enter.EMAIL_ADDR,"\n",
		"PASSWORD = %s" % pass_len,"\n",
		"SERVER = %s" % cred_enter.EMAIL_SRVR,"\n",
		"PORT = %s" % cred_enter.EMAIL_PORT,"\n",
		"PHONE & SMS-GATEWAY = %s" % cred_enter.RECV_ADDR,"\n")
	acc = input("Send test email = [ENTER]; Re-enter credintials = [B]: ")
	print('\n')
	acc = acc.upper()
	try:
		if acc == "B":
			cred_enter()
		if acc=="":
			print("---------------------------------------",
				"\nATTEMPING TO SEND TEST MSG")
			notify_user(
				cred_enter.EMAIL_ADDR, cred_enter.EMAIL_PASS, 
				cred_enter.EMAIL_SRVR, cred_enter.EMAIL_PORT, 
				cred_enter.RECV_ADDR, "TEST", "TEST")
			pass
	except OSError:
		econ1 = ("EMAIL TEST FAILED 1.0~~")
		ct = datetime.datetime.now()
		cur_time = ct.strftime("%H:%M:%S")
		today = date.today()
		d1 = today.strftime("%m/%d/%Y")
		with open(FILE, "a") as file:
			file.write(f'[{d1}]::[{cur_time}]::[COM=CONNECTION-STATUS]~~~~EMAIL-ERROR=={econ1}::ADDRESS=={RECV_PHONES}\n')
		input(f"{econ1}: [PRESS ENTER]")
		cred_enter()
	test_suc = input("Test email sent. Continue = [ENTER]; Re-enter credintials = [B]: ")
	print('\n')
	test_suc = test_suc.upper()
	if test_suc== "B":
		cred_enter()
	if test_suc=="":
		print("Enter was pressed. Moving to next menu")
		print(time.sleep(3))
		os.system('cls')
		cred_coin()
		



def cred_coin():
	print("""
--------------------------------------
 COIN SCOUT CRYPTO MONITORING SYSTEM 
--------------------------------------
       ~~ API DATA ENTERY ~~          
--------------------------------------
""")
	cred_coin.COIN = input("ENTER FULL DIGITAL COIN NAME: ")
	cred_coin.CURRENCY = input("ENTER CURRENCY ABBREVIATION: ")
	coin_price = cg.get_price(ids=cred_coin.COIN, vs_currencies=cred_coin.CURRENCY)
	print(coin_price)
	acc = input("Correct coin returned? Yes[Y]/No[N]: ")
	coin_acc = acc.upper()
	if coin_acc == "N":
		cred_coin()
	if coin_acc=="Y":
		pass
	cred_coin.PRICE_POINT = int(input("ENTER YOUR +/- DEVIATION PRICE POINT: "))
	COIN = cred_coin.COIN
	CURRENCY = cred_coin.CURRENCY
	PRICE_POINT = cred_coin.PRICE_POINT

	api_call(COIN, CURRENCY)










# ALL ACCEPTED CRYPTO-COINS + CURRENCIES
# ADD TO EXPANDABLE HELP MENU IN GUI
def coin_show():
	while True:
		os.system("cls")
		os.system("title ~~~~COIN_SCOUT~~~~")
		print("""
--------------------------------------
--- COIN SCOUT ALL COINS SHOW PAGE ---
--------------------------------------
""")	
		try:
			coin_list = str(input("\nSHOW COINS = [Y]; EXIT = [PRESS ENTER]: "))
			coin_list = coin_list.upper()
			if coin_list == '':
					print(f"\nEnter was pressed. EXITTING TO MENU")
					del coin_list
					time.sleep(1)
					coin_menu()
			if coin_list == "Y":
				coins = cg.get_coins_list()
				coins = enumerate(coins)
				for num, coin in coins:
					num = num+1
					coin = coin['name']
					print(num, coin)
					if num % 20==False:
						_next = input("\nNEXT = [ENTER]; EXIT = [E]: ")
						_next = _next.upper()
						print("\n")
						if _next == "E":
							return coin_show()
			else:
				break
		except OSError:
			dis_con11 = ("DISCONNECTED: 1.1~~NO INTERNET CONNECTION~~")
			exc_type, exc_value, exc_traceback = sys.exc_info()
			S_DTAILS = repr(traceback.format_tb(exc_traceback))
			ct = datetime.datetime.now()
			cur_time = ct.strftime("%H:%M:%S")
			today = date.today()
			d1 = today.strftime("%m/%d/%Y")
			with open(FILE, "a") as file:
				file.write(f'[{d1}]::[{cur_time}]::[COM=CONNECTION-STATUS]~~~~ERROR == {dis_con11}\n[DETAILS]:{S_DTAILS}\n')
			while True:
				print(f"{dis_con11}")
				time.sleep(1)
				coin_show()
				break


def cur_show():		
	os.system("cls")
	os.system("title ~~~~COIN_SCOUT~~~~")
	print("""
--------------------------------------
--- COIN SCOUT CURRENCY SHOW PAGE ----
--------------------------------------
""")	
	while True:
		try:	
			sup_curs = cg.get_supported_vs_currencies()
			cur_list = str(input("\nSHOW SUPPORTED CURRENCIES = [Y]; EXIT = [PRESS ENTER]: "))
			cur_list = cur_list.upper()
			if cur_list == '':
					print(f"\nEnter was pressed. EXITTING TO MENU")
					del sup_curs
					time.sleep(1)
					coin_menu()
			if cur_list == "Y":
				for curs in enumerate(sup_curs):
					print(curs)
			else:
				pass
		except OSError:
			dis_con12 = ("DISCONNECTED: 1.2~~NO INTERNET CONNECTION~~")
			ct = datetime.datetime.now()
			cur_time = ct.strftime("%H:%M:%S")
			today = date.today()
			d1 = today.strftime("%m/%d/%Y")
			with open(FILE, "a") as file:
				file.write(f'[{d1}]::[{cur_time}]::[COM=CONNECTION-STATUS]~~~~ERROR == {dis_con12}\n')
			while True:
				print(f"{dis_con12}")
				time.sleep(1)
				cur_show()
				break				
	
def coin_search():
	os.system("cls")
	os.system("title ~~~~COIN_SCOUT~~~~")
	print("""
--------------------------------------
----- COIN SCOUT COIN SEARCH PAGE-----
--------------------------------------
""")	
	while True:
		try:
			coinsearch = input("\nSEARCH COINS = [coin1,coin2,ect]; EXIT = [PRESS ENTER]: ")
			coinsearch = coinsearch.split(",")
			coins = cg.get_coins_list()
			if coinsearch == ['']:
				print("\nEnter was pressed. EXITTING TO MENU")
				del coinsearch
				time.sleep(1)
				coin_menu()
			print(f'\n\n~SEARCHING COINGECKO DATABASE FOR: {coinsearch}')
			print(f"\n\nRESULTS:")
			for coin in coins:
				coin1 = coin['name']
				for inp_coin in coinsearch:
					if inp_coin == coin1:
						print(f"\nCOIN(S) FOUND: *(EXACT MATCH)* \nINFO: {coin1} =",coin,"\n")
			else:
				pass
		except OSError:
			dis_con13 = ("DISCONNECTED: 1.3~~NO INTERNET CONNECTION~~")
			ct = datetime.datetime.now()
			cur_time = ct.strftime("%H:%M:%S")
			today = date.today()
			d1 = today.strftime("%m/%d/%Y")
			with open(FILE, "a") as file:
				file.write(f'[{d1}]::[{cur_time}]::[COM=CONNECTION-STATUS]~~~~ERROR == {dis_con13}' + "\n")
			while True:
				print(f"{dis_con13}")
				time.sleep(1)
				coin_search()
				break

def mc_price():
	os.system("cls")
	os.system("title ~~~~MC_PRICE~~~~")
	print("""
--------------------------------------
----- COIN SCOUT PRICE CHECK PAGE-----
--------------------------------------
""")
	print("\n\n")
	while True:
		try:
			COIN = input("\nENTER CRYPTO-COIN BY ID = [COIN-ID1,COIN-ID2,ect]; EXIT = [PRESS ENTER]: ")
			COIN = COIN.split(",")
			if COIN == ['']:
				print("\nEnter was pressed. EXITTING TO MENU")
				del COIN
				time.sleep(1)
				coin_menu()
			CURRENCY = input("\nENTER CURRENCY ABBREVIATION: ")
			print(f"\nRETRIEVING PRICE FOR {COIN}")
			
			for COINS in COIN:
				time.sleep(1)
				coin_price = cg.get_price(ids=COINS, vs_currencies=CURRENCY)
				
				for p_id, p_info in coin_price.items():
					print("\nCOIN NAME:", p_id)
					for key in p_info:
						int_chk = p_info[key]
						if isinstance(int_chk, int):
							print(key + ':', p_info[key])
						if isinstance(int_chk, float):
							print(key + ':', '{0:.8f}'.format(p_info[key]))
				#print("\n",coin_price)

			restart = input("\n\n\n\n\nRESTART = [Y]; EXIT = [PRESS ENTER]:  ")
			restart.upper()
			if restart=="":
				print("\nEnter was pressed. EXITTING TO MENU")
				del (COIN,restart)
				time.sleep(1)
				coin_menu()
			if restart=='Y':
				return mc_price()
			else:
				return mc_price()
		except OSError:
			dis_con10 = ("DISCONNECTED: 1.0~~NO INTERNET CONNECTION~~")
			ct = datetime.datetime.now()
			cur_time = ct.strftime("%H:%M:%S")
			today = date.today()
			d1 = today.strftime("%m/%d/%Y")
			with open(FILE, "a") as file:
				file.write(f'[{d1}]::[{cur_time}]::[COM=CONNECTION-STATUS]~~~~ERROR == {dis_con10}' + "\n")
			while True:
				print(f"{dis_con10}")
				time.sleep(1)
				mc_price()
				break

def coin_menu():
	os.system("cls")
	os.system("title ~~~~COIN_SCOUT~~~~")
	while True:
		try:
			print("""
--------------------------------------------------------------------------------------
-----  COIN SCOUT MENU PAGE  ---------------------------------------------------------
--------------------------------------------------------------------------------------
                                                                                      
                                                                                      
         __,.,---'''''''''''''''''''''''''--..._                                       
      ,-'             .....:::''::.:            '`-,                                  
     |           ...:::.....       '                ;                                 
     |           ''':::'''''       .               ,,                                 
     |'-.._           ''''':::..::':          __,,-_;                                 
      '-.._''`---.....______________.....---''__,,-                                   
           ''`---.....______________.....---''                                        
                                                                                      

[1] - COIN-SHOW = show all supported crypto-coins in coin geckos exchange              

[2] - CURRENCY-SHOW = show all supported currencies in coin geckos exchange            

[3] - COIN-SEARCH = search for crypto-coins in coin geckos exhcnage                    

[4] - COIN-SCOUT = monitors a single coin with price notifications (email/sms-gateway) 

[5] - MC-COIN-SCOUT = multiple coin price search                                       

			""")
			MENU_CHOICE = input("Choose an options: ")
			if MENU_CHOICE=="1":
				coin_show()
			if MENU_CHOICE=="2":
				cur_show()
			if MENU_CHOICE=="3":
				coin_search()
			if MENU_CHOICE=="4":
				cred_enter()
			if MENU_CHOICE=="5":
				mc_price()
			else:
				input("invalid option - PRESS ENTER")
				coin_menu()
		except OSError:
			dis_con0 = ("DISCONNECTED: 0~~NO INTERNET CONNECTION~~")
			ct = datetime.datetime.now()
			cur_time = ct.strftime("%H:%M:%S")
			today = date.today()
			d1 = today.strftime("%m/%d/%Y")
			with open(FILE, "a") as file:
				file.write(f'[{d1}]::[{cur_time}]::[COM=CONNECTION-STATUS]~~~~ERROR == {dis_con0}' + "\n")
			while True:
				print(f"{dis_con0}")
				time.sleep(1)
				coin_menu()
				break

coin_menu()
