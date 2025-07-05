from models.art_classes import Painting, Poem, ArtManager

def main():
    manager = ArtManager()

    while True:
        print("\n=== ArtLog Menu ===")
        print("1. Tambah Lukisan")
        print("2. Tambah Puisi")
        print("3. Lihat Semua Karya")
        print("0. Keluar")
        choice = input("Pilih: ")

        if choice == '1':
            title = input("Judul: ")
            date = input("Tanggal (YYYY-MM-DD): ")
            mood = input("Mood saat membuat: ")
            medium = input("Media (cat air, digital, dll): ")
            painting = Painting(title, date, mood, medium)
            manager.add_artwork(painting)
            print("Lukisan ditambahkan.")
        elif choice == '2':
            title = input("Judul: ")
            date = input("Tanggal (YYYY-MM-DD): ")
            mood = input("Mood saat menulis: ")
            theme = input("Tema puisi: ")
            poem = Poem(title, date, mood, theme)
            manager.add_artwork(poem)
            print("Puisi ditambahkan.")
        elif choice == '3':
            for art in manager.artworks:
                print(art.display_info())
        elif choice == '0':
            print("Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
