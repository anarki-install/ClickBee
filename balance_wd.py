try:
  from telethon import TelegramClient, sync, events
  from telethon.tl.functions.messages import GetHistoryRequest, GetBotCallbackAnswerRequest, ImportChatInviteRequest
  from telethon.tl.functions.channels import JoinChannelRequest
  from telethon.errors import SessionPasswordNeededError
  from telethon.errors import FloodWaitError, UserAlreadyParticipantError
  from time import sleep
  import json,re,sys,os,requests,time,random,colorama,threading,itertools
  from bs4 import BeautifulSoup
except:
  print ("\n\n\033[1;32mExcecute : \n\n\033[1;33m$ python -m pip install bs4\n$ python -m pip install telethon\n$ python -m pip install rsa asyncio requests\n$ python -m pip install rsa async_generator colorama\n ")
  exit(1)
  
c = requests.Session()
banner = f"""\033[1;35m\n                                              \neeeee  eeeee e    e eeee eeeee       e  eeeee \n8   8  8   8 8    8 8    "   8       8  8   8 \n8eee8e 8eee8 8eeee8 8eee eeee8       8e 8e  8 \n88   8 88  8   88   88   88          88 88  8 \n88   8 88  8   88   88ee 88ee8       88 88ee8 \n                               eeeee\n\033[1;36m=============================================\n\033[1;32m ~ anthesphong1998@gmail.com (+6282195663814)\n\033[1;36m=============================================\n"""

def tunggu(x):
  sys.stdout.write("\r")
  sys.stdout.write("                                                               ")
  for remaining in range(x, 0, -1):
    sys.stdout.write("\r")
    sys.stdout.write("\033[1;35mSTATUS VIEW\t:\033[1;36m Tunggu \033[1;0m{:2d} \033[1;36mdetik".format(remaining))
    sys.stdout.flush()
    sleep(1)
    
  
           
def bot():
  
  os.system("cls" if os.name == "nt" else "clear")
  print(banner)
  
  try:
    #location
    e = requests.get('https://ipinfo.io/json')
    data = json.loads(e.text)
    lokasi = data['region']
    kota = data['country']
    #exec
    sys.stdout.write(f"\033[1;35mYOUR LOCATION\t: \033[1;36m{lokasi} ({kota})\n\033[1;35mFORUM DISKUSI\t: \033[1;36mt.me/anarki\n\033[1;35mUPDATE\t\t: \033[1;36m20 juni 2020\n\033[1;35mCREATOR\t\t: \033[1;36manarki ganteng\n\033[1;35mSCRIPT NUYUL\t: \033[1;36mClickBee Tele v4\n\033[1;35mSUB YOUTUBE\t: \033[1;36myoutube.com/c/RAYEZID\n\n")
  except:
    sys.stdout.write("\r\033[1;30m[\033[1;31mx\033[1;30m] \033[1;31mCek koneksi internet / configmu ... !\n")
    sys.exit()
  f = open("list.txt", "r")
  jumlah = len(f.readlines())
  for i in range (jumlah):
    try:
      def mengetik(s):
        for c in s + '\n':
          sys.stdout.write(c)
          sys.stdout.flush()
          time.sleep(random.random() * 0.1) 
      f = open("list.txt", "r") 
      if not os.path.exists("session"):
        os.makedirs("session")
      phone_number = f.readlines()[i].strip()
      mengetik("\033[1;36m=============================================\n")
      print(f"\033[1;35mNOMOR AKUN\t:\033[1;36m {phone_number}")
      ua={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win32; x86) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}
      api_id = 800812
      api_hash = "db55ad67a98df35667ca788b97f771f5"
      client = TelegramClient("session/" + phone_number, api_id, api_hash)
      client.connect()
      if not client.is_user_authorized():
        try:
          client.send_code_request(phone_number)
          me = client.sign_in(phone_number, input('\033[1;35mKODE VERIF\t:\033[1;36m '))
        except SessionPasswordNeededError:
          me = client.start(phone_number,input("\033[1;35m2FA CODE\t:\033[1;36m "))
      myself = client.get_me()
      
      try:
        channel_entity = client.get_entity("@ClickBeeBot")
        client.send_message(entity=channel_entity,message="💰 Balance")
        sleep(1)
        posts = client(GetHistoryRequest(peer=channel_entity,limit=1,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
        reward = re.findall( r'([\d.]*\d+) TRX', posts.messages[0].message)[0]
        ball = re.findall( r'([\d.]*\d+) TRX', posts.messages[0].message)[1]
        sys.stdout.write(f"\r\033[1;35mSISA BALANCE\t:\033[1;36m {reward} TRX | {ball} TRX\n")
        client.send_message(entity=channel_entity,message="➖ Withdraw")
        sleep(2)
        total = float(ball)
        if total > 30:
          client.send_message(entity=channel_entity,message=ball)
          sleep(2)
          wallet = input("\033[1;35mINPUT WALLET\t:\033[1;36m ")
          client.send_message(entity=channel_entity,message=wallet)
          sleep(2)
          client.send_message(entity=channel_entity,message="🔙 Back")
          sys.stdout.write(f"\r\033[1;35mSTATUS WD\t:\033[1;36m {ball} TRX has sent to {wallet}\n\n")
        if total < 30:
          sys.stdout.write(f"\r\033[1;35mSTATUS WD\t:\033[1;36m {ball} TRX belum cukup untuk wd\n\n")
        
      finally:
        client.disconnect()
      sleep(2)
    except FloodWaitError as e:
      sys.stdout.write(f"\r\033[1;35mSTATUS AKUN\t:\033[1;36m Flood error tunggu {e.seconds} detik\n\n")
      sleep(2)
    except Exception as e:
      sys.stdout.write(f"\r\033[1;35mSTATUS AKUN\t:\033[1;36m {e}\n\n")
      sleep(2)
    
bot()
