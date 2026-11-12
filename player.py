class Song:
    def __init__(self, title, rating):
        self.title = title
        self.rating = rating
        self.next = None
        self.prev = None

class MusicPlayer:
    def __init__(self):
        self.head = self.tail = self.current = None
        self.hash_table = {}
        self.bst_root = None

    def add_song(self, title, rating):
        new_song = Song(title, rating)
        
        # 1. Linked List
        if not self.head:
            self.head = self.tail = self.current = new_song
        else:
            self.tail.next, new_song.prev, self.tail = new_song, self.tail, new_song
        
        # 2. Hash Table
        self.hash_table[title.lower()] = new_song
        
        # 3. BST
        self.bst_root = self._insert_bst(self.bst_root, new_song)
        print(f"✅ '{title}' əlavə olundu!")

    def _insert_bst(self, root, song):
        if not root: return {"song": song, "left": None, "right": None}
        if song.rating < root["song"].rating:
            root["left"] = self._insert_bst(root["left"], song)
        else:
            root["right"] = self._insert_bst(root["right"], song)
        return root

    def next_song(self):
        if self.current and self.current.next:
            self.current = self.current.next
            print(f"▶️ Oxunur: {self.current.title} (Bal: {self.current.rating})")
        else: print("⚠️ Siyahının sonundasan!")

    def prev_song(self):
        if self.current and self.current.prev:
            self.current = self.current.prev
            print(f"▶️ Oxunur: {self.current.title} (Bal: {self.current.rating})")
        else: print("⚠️ Siyahının əvvəlindəsən!")

    def search_song(self, title):
        song = self.hash_table.get(title.lower())
        print(f"✅ Tapıldı: {song.title} - Bal: {song.rating}" if song else "❌ Tapılmadı.")

    def display_bst(self):
        print("\n--- Reytinq Sıralaması (BST) ---")
        self._display_recursive(self.bst_root)

    def _display_recursive(self, root):
        if root:
            self._display_recursive(root["right"])
            print(f"🎵 {root['song'].title} (Bal: {root['song'].rating})")
            self._display_recursive(root["left"])

# --- MENYU ---
player = MusicPlayer()
player.add_song("Sarı Gəlin", 95)
player.add_song("Believer", 80)

while True:
    print("\n1. Mahnı Əlavə Et | 2. Növbəti | 3. Əvvəlki | 4. Axtar | 5. Sırala | 0. Çıxış")
    secim = input("Seçiminizi yazın: ")
    
    if secim == "1":
        player.add_song(input("Ad: "), int(input("Bal: ")))
    elif secim == "2": player.next_song()
    elif secim == "3": player.prev_song()
    elif secim == "4": player.search_song(input("Axtarılan ad: "))
    elif secim == "5": player.display_bst()
    elif secim == "0": break
    else: print("Yanlış seçim!")