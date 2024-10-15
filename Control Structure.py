#no 1
def evaluate_performance(percentage):   #mendefinisikan fungsi yang bernama evaluate_performance yang hanya menerima satu parameter yaitu percentage
    if percentage >= 90:        #jika nilai lebih lebih besar atau sama dengan 90 maka kode ini dijalankan
        print ("Excellent performance")     #jika nilai terpenuhi maka program akan mencetak Excellent performance
    #elif digunakan untuk memeriksa jika kondisi nilai sebelumnya belum terpenuhi
    elif percentage >= 80:      #jika nilai lebih lebih besar atau sama dengan 80 maka kode ini dijalankan
        print ("Very Good performance")     #jika nilai terpenuhi maka program akan mencetak Very Good performance
    elif percentage >= 70:      #jika nilai lebih lebih besar atau sama dengan 70 maka kode ini dijalankan
        print ("Good performance")          #jika nilai terpenuhi maka program akan mencetak Good performance
    elif percentage >= 60:      #jika nilai lebih lebih besar atau sama dengan 60 maka kode ini dijalankan
        print ("Average performance")       #jika nilai terpenuhi maka program akan mencetak Average performance
    
percentage = float(input("Enter the student's percentage:"))   #memasukan nilai presentase siswa lalu dikonversi menjadi tipe data float karena bisa jadi bilangan desimal
print(evaluate_performance(percentage))     #memanggil dan mencetak hasil yang telah dimasukan prsentasenya

#no 2
def bilangan_terbesar(a,b,c):    #mendefinisikan fungsi yang bernama bilangan terbesar yang menerima tiga parameter a,b,c nantinya untuk menemukan angka terbesar diantara tiga angka tersebut
    if a >= b and  a >= c:      #mengecek apakah nilai a lebih besar atau sama dengan nilai b dan c. and mengahruskan kedua kondisi bernilai true, jika a benar angka terbesar kode if dijalankan
        return a                #jika a angka terbesar maka akan mengembalikan nilai a
    elif b >= a and b >= c:     #jika pada yang pertama tidak terpenuhi maka akan memeriksa nilai b lebih besar atau sama dengan a dan c
        return b                #jika b angka terbesar maka akan mengembalikan nilai b
    else:               #jika kedua kondisi sebelumnya tidak terpenuhi, berarti angka terbesar adalah c
        return c        #jika c angka terbesar maka akan mengembalikan nilai c
    
a = float(input("Masukan angka pertama: "))     #memasukan angka pertama menggunakan tipe data float
b = float(input("Masukan angka pertama: "))     #memasukan angka kedua menggunakan tipe data float
c = float(input("Masukan angka pertama: "))     #memasukan angka ketiga menggunakan tipe data float
print("Bilangan terbesar adalah:", bilangan_terbesar(a, b, c))      #memanggil dan mencetak hasil angka terbesar dari perbandingan tiga angka tersebut

#no 3
def fibonacci(n):       #mendefinisikan fungsi yang bernama fibonacci yang menerima satu parameter n : batas nilai sampai mana deret fibonacci dicetak
    fib_series =[]      #list kosong untuk menyimpan angka-angka
    a, b = 0, 1         #dua angka pertama
    while a <= n:       #deret akan dihasilkan hingga nilai a mencapai atau melebihi nilai n
        fib_series.append(a)    #menambahkan nilai a ke dalam fib_series
        a, b = b, a + b     #setiap angka berikutnya merupakan hasil penjumlahan dua angka sebelumnya
    return fib_series       #mengembalikan list fib_series yang berisi semua angka dalam deret fibonacci hingga batas n
n = int(input("Masukkan jumlah angka Fibonacci yang ingin dicetak: "))  #memasukkan nilai n angka fibonacci yang akan dihitung lalu dikonversi menggunakan tipe data int karena bilangan bulat
print("fibonacci series up to", n, ":", fibonacci(n))   #mencetak deret fibonacci sampai angka ke-n dengan memanggil fibonacci(n) lalu hasil akan ditampilkan

#no 4
def print_odd_numbers(n):       #mendefinisikan fungsi yang menerima satu parameter n : batas nilai sampai mana bilangan ganjil dicetak
    for i in range(1, n+1):     #menghasilkan urutan angka mulai dari 1 sampai n. n+1 digunakan agar batas atasnya adalah n, karena fungsi range() tidak termasuk angka terakhirnya 
        if i % 2 != 0:          #mengecek i apakah bilangan ganjil dengan if. % menghitung sisa bagi jika i % 2 tidak sama dengan 0, artinya angka tersebut adalah ganjil
            #i % 2 != 0 mengecek apakah angka i tidak habis dibagi 2, yang berarti i adalah bilangan ganjil
            print(i, end=" ")   #jika if terpenuhi angka ganjil maka akan mencetak i. lalu memastikan hasil dipisahkan spasi dan tidak dibaris baru menggunakan parameter end=" "
n = int(input("Masukan nilai n:")) #memasukan nilai n dan menggunakan tipe data in karena bilangan bulat
print("bilangan ganjil hingga", n, ":") #menampilkan pesan yang memberi tahu bahwa bilangan ganjil hingga angka ke-n akan dicetak
print_odd_numbers(n) #memanggil fungsi print odd numbers(n) dan nanti akan menjalankan kode dan mencetak hasil

#no 5
def print_pattern(n): #mendefinisikan fungsi print pattern yang hanya menerima satu parameter n yang mewakili jumlah baris pola yang dicetak
    for i in range(1, n + 1):       #perulangan for yang mengulangi nilai i dari 1 hingga n. fungsi range(1, n+1) akan menghasilkan angka dari 1 hingga n
        print((str(i) + " ") * i)   #mencetak angka i sebanyak i kali setiap iterasi lalu angka i diubah menjadi tipe string karena ingin mencetak angka berulang kali sebagai teks
                                    #str(i) + " " memastikan bahwa angka i dipisahkan oleh spasi di antara angka-angka lainnya. * i artinya string i diulang sebanyak i kali
n = int(input("masukan nilai n: ")) #memasukan nilai n jumlah baris yang akan dicetak, lalu dikonversi menjadi tipe data int karena bil. bulat
print_pattern(n)    #memanggil fungsi print_pattern(n) dengan parameter n. lalu menjalankan code diatas



 