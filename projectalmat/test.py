import ica018

def main():
    A = []
    B = []
    pilih = 0
    while pilih !=5:
        print("\n 1.input nilai")
        print(" 2. transpose matriks")
        print(" 3. jumlahkan matriks")
        print(" 4. kalikan matriks")
        print(" 5. keluar")
        try:
            pilih = int(input("\n pilih menu :"))
        except ValueError:
            print("Input tidak valid!")
            continue
    
        if pilih == 1:
            print("\nmasukkan elemen matriks A")

            barisA = int(input("masukkan jumlah baris matriks A:"))
            kolomA = int(input("masukkan jumlah kolom matriks A:"))

            A = []
            for i in range (barisA):
                row = []
                for j in range (kolomA):
                    nilai = int(input(f"A[{i}][{j}] = "))
                    row.append(nilai)
                A.append(row)
    
            print("\nmasukkan elemen matriks B")

            barisB = int(input("masukkan jumlah baris matriksB:"))
            kolomB = int(input("masukkan jumlah kolom matriksB:"))

            B = []
            for i in range (barisB):
                row = []
                for j in range (kolomB):
                    nilai = int(input(f"B[{i}][{j}] = "))
                    row.append(nilai)
                B.append(row)

        if pilih == 2:
            hasil = ica018.transpose_matriks(A)
            hasil = ica018.transpose_matriks(B)

            print("\nHasil Transpose Matriks A:")
            for baris in hasil:
                print(baris)

                print("\nHasil Transpose Matriks B:")
            for baris in hasil:
                print(baris)

            print("\nHasil Transpose Matriks :B")
            for baris in hasil:
                print(baris)


        elif pilih == 3:
            hasil = ica018.penjumlahan_matriks(A, B)

            print("\nHasil Penjumlahan:")
            if isinstance(hasil, str):
                print(hasil)
            else:
                for baris in hasil:
                    print(baris)
                return
            
        elif pilih == 4:
            hasil = ica018.perkalian_matriks(A, B)

            print("\nHasil Perkalian:")
            if isinstance(hasil, str):
                print(hasil)
            else:
                for baris in hasil:
                 print(baris)
        
        elif pilih == 5:
            print("Program selesai.")
            return

if __name__ == "__main__":
    main()