"""
Main.py
Auteur: Bruno DELATTRE
Date : 12/08/2016
"""

from lib import com_email, com_gpio

# from lib import com_config

# com_config.setConfig()

#com_email.send_mail_gmail('tes', 'texte')
#if com_email.getIFFT() != '':
#    pass

gpio = com_gpio.GPIO('GPIO', 'log_gpio.txt')
gpio.setmodeBOARD()