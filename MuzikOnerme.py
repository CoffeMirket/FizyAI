#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import random

veri_seti = pd.read_excel('C:/Users/Inovamarket/Desktop/Sarkilar.xlsx')

meslek = input('Mesleğinizi giriniz: ')
yas = int(input('Yaşınızı giriniz: '))
cinsiyet = input('Cinsiyetinizi giriniz: ')
muzik_zevki = input('Müzik zevkinizi giriniz: ')

zevkine_uygun_kullanicilar = veri_seti[veri_seti['Müzik Zevki'] == muzik_zevki].copy()

def benzerlik_puani(kullanici):
    puan = 0
    if kullanici['Meslek'] == meslek:
        puan += 3
    if abs(kullanici['Yaş'] - yas) <= 10:
        puan += 2
    if kullanici['Cinsiyet'] == cinsiyet:
        puan += 1
    return puan

zevkine_uygun_kullanicilar['Benzerlik Puanı'] = zevkine_uygun_kullanicilar.apply(benzerlik_puani, axis=1)

sirali_kullanicilar = zevkine_uygun_kullanicilar.sort_values(by='Benzerlik Puanı', ascending=False)

secilen_sarkilar = []
for _, kullanici in sirali_kullanicilar.iterrows():
    sarkilar = kullanici['Şarkılar'].split(', ')
    random.shuffle(sarkilar)
    secilen_sarkilar.extend(sarkilar)

oneri_listesi = secilen_sarkilar[:10]

print('Sizin için önerilen şarkılar:')
for sarki in oneri_listesi:
    print(sarki)


# In[ ]:




