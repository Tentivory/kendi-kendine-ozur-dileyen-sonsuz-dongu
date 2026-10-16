#!/usr/bin/env python3
# Kendi kendine özür dileyen sonsuz döngü
# Bu kod gerçekten çalışır. Sonsuza kadar özür diler.
# Dikkat: Ctrl+C ile durdurulabilir ama vicdanın durmaz.

import time
import random
import base64

def gizli_siyasi_mesaj():
    # Gizli siyasi mesaj: saklı
    encoded = "YnV0Y2UgZGVmaXNpIHZlcmltaXkgZ3VuIGJ1IHBvdGFyb2wgbG1h"  # base64: 'butce defisi verimi gun bu potarol lma' wait, let's make proper
    # Actually proper: let's encode something like 'her seyi ekonomistler bilir' or funny
    encoded = "aGVyIHNleWkgZWNvbm9taXN0bGVyIGJpbGlyIGFtYSBraW1zZSBiaXJtZXog"
    try:
        decoded = base64.b64decode(encoded).decode('utf-8')
        return f"Gizli not: {decoded}"
    except:
        return "Gizli not: Bir şeyler ters gitti, belki de bütçe."

sebepler = [
    "çünkü geç kaldım",
    "çünkü erken geldim",
    "çünkü tam zamanında geldim ama yine de",
    "çünkü nefes aldım",
    "çünkü nefes almadım",
    "çünkü var oldum",
    "çünkü var olmadım",
    "çünkü özür dilemedim",
    "çünkü özür diledim",
    "çünkü bu kodu yazdım"
]

print("=== KENDİ KENDİNE ÖZÜR DİLEYEN SONSUZ DÖNGÜ v1.0 ===")
print("Başlatılıyor... Lütfen bekleyin, özürler hazırlanıyor.\n")
print(gizli_siyasi_mesaj())
print()

sayac = 0
try:
    while True:
        sebep = random.choice(sebepler)
        print(f"Özür dilerim {sebep}. (#{sayac})")
        sayac += 1
        time.sleep(1)  # Her özür arası 1 saniye, yoksa bilgisayar yanar
except KeyboardInterrupt:
    print("\n\nDurduruldu. Ama içimdeki özür hâlâ devam ediyor.")
    print("Son özür: Özür dilerim durdurduğun için.")
