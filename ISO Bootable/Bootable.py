import os
import sys
import textwrap
import time
import pyttsx3

none_type = None 
engine = pyttsx3.init()

def main():
	os.system("clear")
	engine.say("Welcome to this application")
	engine.runAndWait()
	print ("THANKS TO JSAMR on GITHUB")
	print ("Welcome to ISO Bootable \n Ketik Satu dan Dua")
	print ("##############")
	print ("# 1.Bootable #")
	print ("# 2.Exit     #")
	print ("##############")
main()

def boot():
	print ("For Linux Only")
	engine.setProperty('rate', 140)
	engine.setProperty('volume', 1.0)
	engine.say("For Linux Only")
	print ("Please Input ur Directory ISO file \n Ex: /home/arya/ISO/myiso.iso")
	engine.say("Please Input ur Directory ISO file, Example /home/arya/ISO/myiso.iso")
	engine.runAndWait()	
	file_iso = input("> ")
	print ("Where is ur USB Drive? or anything? \n you can check it by typing lsblk on terimal")
	engine.say("Where is ur USB Drive? or anything?, you can check it by typing lsblk on terimal")
	engine.runAndWait()	
	print ("Example : /dev/sdb")
	of = input("> ")
	bs = ("bs=4m")
	gabung = ("sudo dd if={0}{1}{2}".format(file_iso,of,bs))
	os.system(gabung)
	engine.runAndWait()


# def install():
	#pilih = input("Apakah sudah install GIT? sudah/belum ")
	#if pilih.lower() == ("b") == ("belum"):
	#os.system("sudo apt-get install git")
	#print ("Before to Download, Please make sure u are at the right Directory otherwise it will difficult to fid this Download \n Relax this is safe BootISO")
	#print ("if u wanna Stop this just Press CTRL+C or CTRL+Z")
	#pilih_lagi = input("Apakah anda mengizinkan aplikasi ini untuk install bootiso? yes/no ")
	#if pilih_lagi.lower() == ("y") == ("yes"):
	#os.system("sudo git clone https://github.com/jsamr/bootiso.git")
	#else:
		#sys.exit()
	#os.system("cd bootiso/")
	#os.system("sudo chmod +x bootiso")
	#time.sleep(0.6)
	#os.system("mv bootiso /usr/local/bin")

def opsi():
	user = input ("> ")
	if user.lower() == ("satu"):
		print (boot())
	if user.lower() == ("dua"):
		sys.exit()

if none_type is None:
	print ("Silahkan Dipilih")

opsi()
