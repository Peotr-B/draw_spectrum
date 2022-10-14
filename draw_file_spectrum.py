import numpy as np
from pylab import *
from scipy import *

#Лучше всего применять import os вместо from os import *. 
#Это предохранит встроенную функцию open() от замещения функцией os.open(), 
#имеющей несколько иное назначение.
#https://pep8.ru/doc/tutorial-3.1/10.html

#import pylab
#import scipy
import os

def read_bin_file(filename):
 f=open(filename, 'rb')
 values = np.fromfile(f,dtype="int8")
 return values

def plotSpectrum(y,Fs):
 n = len(y) # length of the signal
 k = arange(n) #scipy
# k = np.arange(n) - может, так надо?
 T = n/Fs
 
# print('\n')
# print('n= ',n)
# print('\n')
# print('k= ',k)
# print('\n')
# print('T= ',T)

 frq = k/T # two sides frequency range
 frq = frq[range(int(n/2))] # one side frequency range

 Y = fft(y)/n # fft computing and normalization
# print('\n')
# print('fft= ','\n',fft(y))
# print('\n')
# print('fft[8]= ','\n',fft(y)[8])
# print('\n')
# print('Yfft/n= ','\n',Y)
# print('\n')
# print('Yfft8/n= ','\n',Y[8])
 Y = Y[range(int(n/2))]
 
# print('\n')
# print('range(int(n/2))= ','\n',range(int(n/2)))
 
# print('\n')
# print('Y= ','\n',Y)
# print('\n')
# print('abs(Y)= ','\n',abs(Y))
# print('\n')
 
 plot(frq,abs(Y),'r') # plotting the spectrum
# plot(frq,Y,'r') # plotting the spectrum
 xlabel('Freq (Hz)')
 ylabel('|Y(freq)|')

Fs=1024.0
y = read_bin_file("samples_imp.bin")
#y = read_bin_file("samples_saw.bin")
#y = read_bin_file("samples_sin.bin")
#y = read_bin_file("samples_rnd.bin")
t = arange(0,len(y),1) # time vector

#см. https://jenyay.net/Matplotlib/Subplot
subplot(2,1,1)
plot(t,y)
#plot(t,y,'g')
xlabel('Time')
ylabel('Amplitude')
subplot(2,1,2)
plotSpectrum(y,Fs)

# красиво расположить области с отступами 
# http://acm.mipt.ru/twiki/bin/view/Cintro/PythonGraphs#__q__ql_i_chkm_
plt.subplots_adjust(left=0.1, right=0.95, bottom=0.1, top=0.95, wspace=0.1,
hspace=0.5)

show()
