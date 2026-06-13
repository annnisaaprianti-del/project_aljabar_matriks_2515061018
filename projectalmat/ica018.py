def penjumlahan_matriks(a, b):

    if len(a) != len(b) or len(a[0]) != len(b[0]):
        return ("Penjumlahan tidak dapat dilakukan, ukuran matriks berbeda") 
    hasil = []
    for i in range(len(a)):
        baris = []

        for j in range(len(a[0])):
            baris.append(a[i][j] + b[i][j])
        hasil.append(baris)
    

def transpose_matriks(m):

    if len(m) == 0:
        return ("Matriks kosong")

    hasil = []
    for j in range(len(m[0])):
        baris = []

        for i in range(len(m)):
            baris.append(m[i][j])
        hasil.append(baris)
    return hasil

def perkalian_matriks(a, b):
    if len(a[0]) != len(b):
        return("perkalian tidak dapat dilakukan, matriks tidak sesuai aturan")
    hasil = []
    for i in range (len(a)):
        baris = []
        for j in range(len(b[0])):
            total = 0
            for k in range(len(a[0])):
                total += a[i][k] * b[k][j]
            baris.append(total)
        hasil.append(baris)
    return hasil