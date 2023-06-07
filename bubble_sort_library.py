book = [
    {"Judul" : "Harry Potter and The Sorcerer's Stone" , "Penulis" : "J.K.Rowling", "Halaman" : "320"},
    {"Judul" : "To Kill a Mockingbird", "Penulis" : "Harper Lee", "Halaman" : "281"},
    {"Judul" : "The Great Gatsby", "Penulis" : "F.Scott Fitzgerald", "Halaman" : "180"},
    {"Judul" : "Pride and Prejudice", "Penulis" : "Jame Austen", "Halaman" : "432"},
    {"Judul" : "1984", "Penulis" : "George Orwell", "Halaman" : "328"}
]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j]["Halaman"] > arr[j+1]["Halaman"]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

bubble_sort(book)

for book in book:
    print(f"Judul : {book['Judul']}, Penulis : {book['Penulis']}, Jumlah Halaman : {book['Halaman']}")           