
import os,sys,time
from rich import print as prints
from rich.panel import Panel


os.system('clear')
prints(Panel('[deep_pink3]                   •••  Tools Cek Cuaca   ••• \n                          By Ery Devs'))
kota = input('Nama Kota : ')
prints(Panel('Tunggu.....'))
os.system('curl http://wttr.in/{}'.format(kota))
