

#JoinLeavespammer
import amino
import concurrent.futures
emails=["shun00700@outlook.com"]
client = amino.Client()
for email in emails:
	try:
		client.login(email=email, password='10billie01')
		print("Logged in using ",email)
	except:
		print("Action not allowed")
	f=input("Enter chat link :-")
	fok=client.get_from_code(f)
	id=client.get_from_code(f).objectId
	cid=fok.path[1:fok.path.index("/")]

	print()
	try:
		client.join_community(comId=cid)
		subclient=amino.SubClient(comId=cid,profile=client.profile)
		k=input("enter nickname: ")
		subclient.edit_profile(nickname=k)

	except:
		print("Id banned")
def spam(ch):
	try:
		subclient.join_chat(chatId=ch)
		subclient.leave_chat(chatId=ch)
		print("\033[1;93mspaming...",)
	except:
			print("Id blocked by host")
def thread():
	     with concurrent.futures.ThreadPoolExecutor() as executor:
	     	_ = [executor.submit(spam,id) for _ in range(15000)]
while True:
	 thread()
import amino
import concurrent.futures
emails=["shun00700@outlook.com"]
client = amino.Client()
for email in emails:
	try:
		client.login(email=email, password='******')
		print("Logged in using ",email)
	except:
		print("Action not allowed")
	f=input("Enter chat link :-")
	fok=client.get_from_code(f)
	id=client.get_from_code(f).objectId
	cid=fok.path[1:fok.path.index("/")]

	print()
	try:
		client.join_community(comId=cid)
		subclient=amino.SubClient(comId=cid,profile=client.profile)
		k=input("enter nickname: ")
		subclient.edit_profile(nickname=k)

	except:
		print("Id banned")
def spam(ch):
	try:
		subclient.join_chat(chatId=ch)
		subclient.leave_chat(chatId=ch)
		print("\033[1;93mspaming...",)
	except:
			print("Id blocked by host")
def thread():
	     with concurrent.futures.ThreadPoolExecutor() as executor:
	     	_ = [executor.submit(spam,id) for _ in range(15000)]
while True:
	 thread()