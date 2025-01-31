### SITE ESTÁ ACESSÍVEL? ###

import urllib
import urllib.error
import urllib.request

try:
    site = urllib.request.urlopen('https://eduardo-rodrigues.vercel.app/')
except urllib.error.URLError:
    print('\033[31mO site Eduardo Rodrigues não está acessível no momento.\033[m')
else:
    print('\033[32mConsegui acessar o site Eduardo Rodrigues com sucesso!\033[m')
    # print(site.read())
    