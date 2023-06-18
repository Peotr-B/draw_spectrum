# show_rnd
 WinPython/FilePy/Spektrometr_na_Pytone/draw_spectrum/github

 6сен18
 @Biriuk
  peotr60@mail.ru

https://github.com/Peotr-B/draw_spectrum.git

18июн23
Обновление для возобновления работы
=============================================================

 https://marsohod.org/11-blog/326-draw-spectrum
N.b!
//
// test_waves.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#define _USE_MATH_DEFINES
#include <math.h>

#define NUM_SAMPLES 1024 
int _tmain(int argc, _TCHAR* argv[])
{
	char arr_sin[NUM_SAMPLES];
	char arr_saw[NUM_SAMPLES];
	char arr_imp[NUM_SAMPLES];

	double sin_step=2*M_PI*32/NUM_SAMPLES;
	for(int i=0; i<NUM_SAMPLES; i++)
	{
		arr_saw[i]=(i&0x3F)*4-127;
		arr_imp[i]=(i&0x40) ? 127 : -127;
		arr_sin[i]=127*sin(sin_step*i);
	}

//Описание FILE * pFile; см. на:
// https://marsohod.org/11-blog/326-draw-spectrum
//https://ru.wikipedia.org/wiki/Файловый_ввод-вывод_в_языке_Си

	FILE * pFile;
	errno_t err = fopen_s(&pFile,"samples_sin.bin","wb");
	fwrite(arr_sin,1,NUM_SAMPLES,pFile);
        fclose (pFile);
	err = fopen_s(&pFile,"samples_saw.bin","wb");
	fwrite(arr_saw,1,NUM_SAMPLES,pFile);
        fclose (pFile);
	err = fopen_s(&pFile,"samples_imp.bin","wb");
	fwrite(arr_imp,1,NUM_SAMPLES,pFile);
        fclose (pFile);
	return 0;
}

