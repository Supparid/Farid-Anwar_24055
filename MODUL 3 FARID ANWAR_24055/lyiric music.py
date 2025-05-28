import tkinter as tk
import time
from threading import Thread

# ingput Lirik 
lirik = [
    "But I crumble completely when you cry",
    "It seems like once again you've had to greet me with goodbye",
    "I'm always just about to go and spoil a surprise",
    "Take my hands off of your eyes too soon",
    "I'm going back to 505",
    "If it's a seven-hour flight or a 45-minute drive",
    "In my imagination, you're waiting lying on your side",
    "With your hands between your thighs and a smile"
]

class KaraokeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🎵")
        self.root.configure(bg="#121212")
        self.root.geometry("700x300")
        
        self.label = tk.Label(
            root,
            text="Klik 'Play'!",
            font=("Courier New", 20, "bold"),
            fg="#00FF99",
            bg="#121212",
            wraplength=650,
            justify="center"
        )
        self.label.pack(pady=40)

        self.btn_frame = tk.Frame(root, bg="#121212")
        self.btn_frame.pack()

        self.start_button = tk.Button(
            self.btn_frame, text="▶ Play", font=("Helvetica", 14),
            bg="#00AA88", fg="white", padx=20, command=self.start_karaoke
        )
        self.start_button.pack(side="left", padx=10)

        self.pause_button = tk.Button(
            self.btn_frame, text="⏸ Pause", font=("Helvetica", 14),
            bg="#FFA500", fg="white", padx=20, command=self.pause
        )
        self.pause_button.pack(side="left", padx=10)

        self.quit_button = tk.Button(
            self.btn_frame, text="✖ Exit", font=("Helvetica", 14),
            bg="#AA0033", fg="white", padx=20, command=root.quit
        )
        self.quit_button.pack(side="left", padx=10)

        self.running = False
        self.paused = False

    def start_karaoke(self):
        if not self.running:
            self.running = True
            self.paused = False
            thread = Thread(target=self.tampilkan_lirik)
            thread.start()
        else:
            self.paused = False  # Lanjutkan jika sedang pause

    def pause(self):
        self.paused = True

    def tampilkan_lirik(self):
        for baris in lirik:
            while self.paused:
                time.sleep(0.1)
            if not self.running:
                break
            self.ketik_per_huruf(baris)
            for _ in range(int(1.8 / 0.1)):
                if self.paused:
                    break
                time.sleep(0.1)

        self.label.config(text="🎤 Selesai! Klik 'Play' untuk ulangi.")
        self.running = False

    def ketik_per_huruf(self, teks):
        self.label.config(text="")
        for i in range(len(teks) + 1):
            if self.paused:
                break
            self.label.config(text=teks[:i])
            time.sleep(0.08)

# output runnnya
if __name__ == "__main__":
    root = tk.Tk()
    app = KaraokeApp(root)
    root.mainloop()
