#library Fungsi Animasi Teks
import random
import time
import sys

def animate_text(text, delay=0.03 ):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()
    
# Fungsi utama Tebak Angka
def tebak_angka():
    animate_text('👾WELCOME TO GUEST NUMBER GAMES!!👾')
    animate_text('_______________________________')
    
# leVEL
    animate_text('choose difficulty level (pilih level kesulitan)')
    animate_text('1. Easy 😊(1-10, 5 nyawa)')
    animate_text('2. Normal 😈(1-50, 4 nyawa)')
    animate_text('3. Hard ☠️(1-100, 3 nyawa)')

    while True:
        try:
            level = int(input('Masukan pilihan (1-3):'))
            if level == 1:
                max_num = 10
                nyawa = 5
                break
            elif level == 2:
                max_num = 50
                nyawa = 4
                break
            elif level == 3:
                max_num = 100
                nyawa = 3
                break
            else:
                animate_text('pilihan tidak valid. Silahkan pilih (1-3)!')
        except ValueError:
                animate_text('input harus angka!')
            
 #Angka Rahasia dan variable game
    angka_rahasia = random.randint( 1,max_num )  
    skor = 100 * level  # Skor berdasarkan nilai yg kita dapat
    tebakan_terdekat = max_num
    sudah_tebak = []
    
    # logika Tebakan Game
    animate_text(f'\n 🔥LEVEL {'Easy' if level == 1 else 'Normal' if level == 2 else 'Hard'} GAME START!! 🔥')
    animate_text(f'Saya telah memilih angka antara 1-{max_num}, Tebak YA!')
    
    while nyawa > 0:
        animate_text(f'\n ❤️ nyawa: {'❤️'* nyawa}')
        animate_text(f' Skor saat ini : {skor}')
        animate_text(f' Tebakan sebelumnya: {sudah_tebak if sudah_tebak else '-'}')
        
        try:
            tebakan = int(input('Tebak angka: '))
            
            if tebakan< 1 or tebakan > max_num:
                animate_text(f'Tebakan harus antara 1-{max_num}')
                continue
            if tebakan in sudah_tebak:
                animate_text('Anda sudah menebak angka ini sebelumnya')
                continue
            
            sudah_tebak.append(tebakan)
        
    # petunjuk Menentukan kemenanangan
    # HItung selisih Twbakan
            selisih = abs(angka_rahasia - tebakan)

            if tebakan == angka_rahasia:
                animate_text(f'Benar! Angka rahasianya adalah {angka_rahasia}')
                animate_text (f"Skor akhir anda {skor}")
                time.sleep(1)
                animate_text(f'\n 🔥🔥🔥YOU WIN !!!🔥🔥🔥')
                break 
            else:
                nyawa -= 1
                skor -= 20
        
        #Petunjuk
                if selisih<= 5:
                    Petunjuk = "YOURe Close! hampir Benar"
                elif selisih <= 15:
                    Petunjuk = "aLMOST..."
                else:
                    Petunjuk = "mNEhh :(("

    # Update tebakan terdekat
                if selisih< abs(angka_rahasia - tebakan_terdekat):
                    tebakan_terdekat = tebakan
                animate_text('ini tebakan terdekatmu sejauh ini!')
                
    #Hasil Akhir dan memaikan ulang
                if nyawa == 0:
                    animate_text(f'GAme OVER! Angka Rahasianya: {angka_rahasia}')
                    animate_text(f'Skor akhir anda: {skor}')
                    time.sleep(1)
                    animate_text('\n Jangan Nyerah!! Coba Lagi WKWKW')
                    
        except ValueError:
            animate_text("input harus angka!")
            continue

#Main Program
while True:
    tebak_angka()
    
    play_again = input('\n Main Lagi? (y/n): ').lower()
    if play_again != 'y':
        animate_text('\n Terima kasih telah bermain! Good bye!')
        time.sleep
        break
    
  
        