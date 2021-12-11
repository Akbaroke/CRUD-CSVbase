import os
import csv

list_nim = []
list_nama = []
list_kelas = []
list_prodi = []
list_ipk = []
list_wa = []
list_email = []

### >>>>>> Program CRUD CSVbase By Akbaroke >> https://github.com/Akbaroke/ <<<<<< ###

# Fungsi Untuk Menambah Data Mahasiswa
def tambahdata():
    os.system('cls')
    print('='*71)
    print('|         SILAHKAN MASUKAN NIM UNTUK PENCARIAN DATA MAHASISWA         |')
    print('='*71)
    with open('datamahasiswa.csv', mode='a', newline='') as csv_file:
        datamahasiswa =['nim', 'nama', 'kelas', 'prodi', 'ipk', 'wa', 'email']
        writer = csv.DictWriter(csv_file, fieldnames=datamahasiswa)
        print('Input Biodata Mahasiswa')
        nama = input('Nama\t\t: ')
        nim = input('Nim\t\t: ')
        kelas = input('Kelas\t\t: ')
        prodi = input('Prodi\t\t: ')
        ipk = input('IPK\t\t: ')
        wa = input('No.Whatsapp\t: ')
        email = input('Alamat Email\t: ')
        print(f'\n\t>> Data Berhasil Tersimpan <<')

        writer.writerow({'nama': nama, 'nim': nim, 'kelas': kelas, 'prodi': prodi, 'ipk': ipk, 'wa': wa, 'email': email})
        csv_file.close()
                
        back = input('\nKembali Ke Menu Utama <y/n> ? ')
        if back == 'y':
            csv_file.close()
            menuutama()
        else:
            csv_file.close()
            tambahdata()

# Fungsi Untuk Mencari Atau Membuka Data Mahasiswa
def caridata():
    listidnim = []
    with open('datamahasiswa.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                list_nim.append(row[0])
                list_nama.append(row[1])
                list_kelas.append(row[2])
                list_prodi.append(row[3])
                list_ipk.append(row[4])
                list_wa.append(row[5])
                list_email.append(row[6])
    stop = False
    while(not stop):
        os.system('cls')
        print('='*71)
        print('|         SILAHKAN MASUKAN NIM UNTUK PENCARIAN DATA MAHASISWA         |')
        print('='*71)
        idnim = input('Masukan nim : ')
        listidnim.append(idnim)
        if listidnim[0] in list_nim:
            a = 0
            with open('datamahasiswa.csv') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                for row in csv_reader:
                    list_nim.append(row[0])
                while a < len(list_nim):
                    if idnim in list_nim[a]:
                        print('Berikut datanya >>')
                        print('Nama\t\t:',list_nama[a])
                        print('Nim\t\t:',list_nim[a])
                        print('Kelas\t\t:',list_kelas[a])
                        print('Prodi\t\t:',list_prodi[a])
                        print('IPK\t\t:',list_ipk[a])
                        print('No.Whatsapp\t:',list_wa[a])
                        print('Alamat Email\t:',list_email[a])
                        print('\n'+'='*35)
                        a += len(list_nim)
                    else:
                        a += 1
            stop = True
        else:
            stop = False
        
        print('\n\n\n\n\n*Note : Jika Nim Merasa Sudah Didaftarkan\n\tTetapi Tidak dapat DiCari Silahkan \n\tBuka Menu Utama Lalu Cari Ulang.. \n\tTrimakasih :)')
        back = input('\n>> Kembali Ke Menu Utama <y/n> ? ')
        
        if back == 'y':
            menuutama()
        else:
            csv_file.close()
            caridata()

# Fungsi Untuk Menghapus Data Mahasiswa
def hapusdata():
    listdata_hapus = []
    listhapus = []
    with open('datamahasiswa.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                list_nim.append(row[0])
                list_nama.append(row[1])
                list_kelas.append(row[2])
                list_prodi.append(row[3])
                list_ipk.append(row[4])
                list_wa.append(row[5])
                list_email.append(row[6])
    stop = False
    while(not stop):
        os.system('cls')
        print('='*53)
        print('|         SELAMAT DATANG DI MENU HAPUS DATA         |')
        print('='*53)
        idnim = input('Masukan nim : ')
        listdata_hapus.append(idnim)
        if listdata_hapus[0] in list_nim:
            a = 0
            with open('datamahasiswa.csv') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                for row in csv_reader:
                    list_nim.append(row[0])
                while a < len(list_nim):
                    if idnim in list_nim[a]:
                        print('Berikut datanya >>')
                        print('Nama\t\t:',list_nama[a])
                        print('Nim\t\t:',list_nim[a])
                        print('Kelas\t\t:',list_kelas[a])
                        print('Prodi\t\t:',list_prodi[a])
                        print('IPK\t\t:',list_ipk[a])
                        print('No.Whatsapp\t:',list_wa[a])
                        print('Alamat Email\t:',list_email[a])
                        listhapus.append(list_nim[a])
                        listhapus.append(list_nama[a])
                        listhapus.append(list_kelas[a])
                        listhapus.append(list_prodi[a])
                        listhapus.append(list_ipk[a])
                        listhapus.append(list_wa[a])
                        listhapus.append(list_email[a])
                        print('\n'+'='*35)
                        csv_file.close()
                        hapus = input('Hapus Data Sekarang <y/n> ? ')
                        if hapus == 'y':
                            with open('datamahasiswa.csv', 'r') as f:
                                lines = f.readlines()
                            with open('datamahasiswa.csv', 'w') as f:
                                for line in lines:
                                    if line.strip('\n') != listhapus[0]+','+listhapus[1]+','+listhapus[2]+','+listhapus[3]+','+listhapus[4]+','+listhapus[5]+','+listhapus[6]:
                                        f.write(line)
                            print('\n>>> DATA BERHASIL TERHAPUS <<<')

                        a += len(list_nim)
                    else:
                        a += 1
            stop = True
        else:
            stop = False
        
        print('\n\n\n\n\n*Note : Jika Nim Merasa Sudah Didaftarkan\n\tTetapi Tidak dapat DiCari Silahkan \n\tBuka Menu Utama Lalu Cari Ulang.. \n\tTrimakasih :)')
        back = input('\n>> Kembali Ke Menu Utama <y/n> ? ')
        
        if back == 'y':
            csv_file.close()
            f.close()
            menuutama()
        else:
            csv_file.close()
            f.close()
            hapusdata()

# Fungsi Untuk Mengedit atau Update Data Mahasiswa
def editdata():
    listidnim = []
    listhapus = []
    with open('datamahasiswa.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                list_nim.append(row[0])
                list_nama.append(row[1])
                list_kelas.append(row[2])
                list_prodi.append(row[3])
                list_ipk.append(row[4])
                list_wa.append(row[5])
                list_email.append(row[6])
    stop = False
    while(not stop):
        os.system('cls')
        print('='*52)
        print('|         SELAMAT DATANG DI MENU EDIT DATA         |')
        print('='*52)
        idnim = input('Masukan nim : ')
        listidnim.append(idnim)
        if listidnim[0] in list_nim:
            a = 0
            with open('datamahasiswa.csv') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                for row in csv_reader:
                    list_nim.append(row[0])
                while a < len(list_nim):
                    if idnim in list_nim[a]:
                        listhapus.append(list_nim[a])
                        listhapus.append(list_nama[a])
                        listhapus.append(list_kelas[a])
                        listhapus.append(list_prodi[a])
                        listhapus.append(list_ipk[a])
                        listhapus.append(list_wa[a])
                        listhapus.append(list_email[a])
                        print('='*35)
                        csv_file.close()
                        print('PILIH DATA YANG ANDA INGIN DIEDIT')
                        print('1) Nama\n2) Nim\n3) Kelas\n4) Prodi\n5) IPK\n6) No.Whatsapp\n7) Alamat Email')
                        pilihan = input('Pilih Salah Nomor Untuk Mengedit data : ')
                        print('='*35)
                        listupdate = []
                        listdatabaru = []
                        if pilihan == '1':
                            namabaru = input('Nama\t\t : ')
                            listupdate.append(namabaru)
                            listdatabaru.append(list_nim[a])
                            listdatabaru.append(listupdate[0])
                            listdatabaru.append(list_kelas[a])
                            listdatabaru.append(list_prodi[a])
                            listdatabaru.append(list_ipk[a])
                            listdatabaru.append(list_wa[a])
                            listdatabaru.append(list_email[a])
                            print(listdatabaru[0]+','+listupdate[0]+','+listdatabaru[2]+','+listdatabaru[3]+','+listdatabaru[4]+','+listdatabaru[5]+','+listdatabaru[6], file= open('datamahasiswa.csv', 'a'))
                            with open('datamahasiswa.csv', 'r') as f:
                                lines = f.readlines()
                            with open('datamahasiswa.csv', 'w') as f:
                                for line in lines:
                                    if line.strip('\n') != listhapus[0]+','+listhapus[1]+','+listhapus[2]+','+listhapus[3]+','+listhapus[4]+','+listhapus[5]+','+listhapus[6]:
                                        f.write(line)
                                f.close()
                            print('\n>>> DATA BERHASIL DI UPDATE <<<')
                        elif pilihan == '2':
                            namabaru = input('Nim\t\t : ')
                            listupdate.append(namabaru)
                            listdatabaru.append(listupdate[0])
                            listdatabaru.append(list_nama[a])
                            listdatabaru.append(list_kelas[a])
                            listdatabaru.append(list_prodi[a])
                            listdatabaru.append(list_ipk[a])
                            listdatabaru.append(list_wa[a])
                            listdatabaru.append(list_email[a])
                            print(listupdate[0]+','+listdatabaru[1]+','+listdatabaru[2]+','+listdatabaru[3]+','+listdatabaru[4]+','+listdatabaru[5]+','+listdatabaru[6], file= open('datamahasiswa.csv', 'a'))
                            with open('datamahasiswa.csv', 'r') as f:
                                lines = f.readlines()
                            with open('datamahasiswa.csv', 'w') as f:
                                for line in lines:
                                    if line.strip('\n') != listhapus[0]+','+listhapus[1]+','+listhapus[2]+','+listhapus[3]+','+listhapus[4]+','+listhapus[5]+','+listhapus[6]:
                                        f.write(line)
                                f.close()
                            print('\n>>> DATA BERHASIL DI UPDATE <<<')
                        elif pilihan == '3':
                            namabaru = input('Kelas\t\t : ')
                            listupdate.append(namabaru)
                            listdatabaru.append(list_nim[a])
                            listdatabaru.append(list_nama[a])
                            listdatabaru.append(listupdate[0])
                            listdatabaru.append(list_prodi[a])
                            listdatabaru.append(list_ipk[a])
                            listdatabaru.append(list_wa[a])
                            listdatabaru.append(list_email[a])
                            print(listdatabaru[0]+','+listdatabaru[1]+','+listupdate[0]+','+listdatabaru[3]+','+listdatabaru[4]+','+listdatabaru[5]+','+listdatabaru[6], file= open('datamahasiswa.csv', 'a'))
                            with open('datamahasiswa.csv', 'r') as f:
                                lines = f.readlines()
                            with open('datamahasiswa.csv', 'w') as f:
                                for line in lines:
                                    if line.strip('\n') != listhapus[0]+','+listhapus[1]+','+listhapus[2]+','+listhapus[3]+','+listhapus[4]+','+listhapus[5]+','+listhapus[6]:
                                        f.write(line)
                                f.close()
                            print('\n>>> DATA BERHASIL DI UPDATE <<<')
                        elif pilihan == '4':
                            namabaru = input('Prodi\t\t : ')
                            listupdate.append(namabaru)
                            listdatabaru.append(list_nim[a])
                            listdatabaru.append(list_nama[a])
                            listdatabaru.append(list_kelas[a])
                            listdatabaru.append(listupdate[0])
                            listdatabaru.append(list_ipk[a])
                            listdatabaru.append(list_wa[a])
                            listdatabaru.append(list_email[a])
                            print(listdatabaru[0]+','+listdatabaru[1]+','+listdatabaru[2]+','+listupdate[0]+','+listdatabaru[4]+','+listdatabaru[5]+','+listdatabaru[6], file= open('datamahasiswa.csv', 'a'))
                            with open('datamahasiswa.csv', 'r') as f:
                                lines = f.readlines()
                            with open('datamahasiswa.csv', 'w') as f:
                                for line in lines:
                                    if line.strip('\n') != listhapus[0]+','+listhapus[1]+','+listhapus[2]+','+listhapus[3]+','+listhapus[4]+','+listhapus[5]+','+listhapus[6]:
                                        f.write(line)
                                f.close()
                            print('\n>>> DATA BERHASIL DI UPDATE <<<')
                        elif pilihan == '5':
                            namabaru = input('IPK\t\t : ')
                            listupdate.append(namabaru)
                            listdatabaru.append(list_nim[a])
                            listdatabaru.append(list_nama[a])
                            listdatabaru.append(list_kelas[a])
                            listdatabaru.append(list_prodi[a])
                            listdatabaru.append(listupdate[0])
                            listdatabaru.append(list_wa[a])
                            listdatabaru.append(list_email[a])
                            print(listdatabaru[0]+','+listdatabaru[1]+','+listdatabaru[2]+','+listdatabaru[3]+','+listupdate[0]+','+listdatabaru[5]+','+listdatabaru[6], file= open('datamahasiswa.csv', 'a'))
                            with open('datamahasiswa.csv', 'r') as f:
                                lines = f.readlines()
                            with open('datamahasiswa.csv', 'w') as f:
                                for line in lines:
                                    if line.strip('\n') != listhapus[0]+','+listhapus[1]+','+listhapus[2]+','+listhapus[3]+','+listhapus[4]+','+listhapus[5]+','+listhapus[6]:
                                        f.write(line)
                                f.close()
                            print('\n>>> DATA BERHASIL DI UPDATE <<<')
                        elif pilihan == '6':
                            namabaru = input('No.Whatsapp\t : ')
                            listupdate.append(namabaru)
                            listdatabaru.append(list_nim[a])
                            listdatabaru.append(list_nama[a])
                            listdatabaru.append(list_kelas[a])
                            listdatabaru.append(list_prodi[a])
                            listdatabaru.append(list_ipk[a])
                            listdatabaru.append(listupdate[0])
                            listdatabaru.append(list_email[a])
                            print(listdatabaru[0]+','+listdatabaru[1]+','+listdatabaru[2]+','+listdatabaru[3]+','+listdatabaru[4]+','+listupdate[0]+','+listdatabaru[6], file= open('datamahasiswa.csv', 'a'))
                            with open('datamahasiswa.csv', 'r') as f:
                                lines = f.readlines()
                            with open('datamahasiswa.csv', 'w') as f:
                                for line in lines:
                                    if line.strip('\n') != listhapus[0]+','+listhapus[1]+','+listhapus[2]+','+listhapus[3]+','+listhapus[4]+','+listhapus[5]+','+listhapus[6]:
                                        f.write(line)
                                f.close()
                            print('\n>>> DATA BERHASIL DI UPDATE <<<')
                        elif pilihan == '7':
                            namabaru = input('Alamat Email\t : ')
                            listupdate.append(namabaru)
                            listdatabaru.append(list_nim[a])
                            listdatabaru.append(list_nama[a])
                            listdatabaru.append(list_kelas[a])
                            listdatabaru.append(list_prodi[a])
                            listdatabaru.append(list_ipk[a])
                            listdatabaru.append(list_wa[a])
                            listdatabaru.append(listupdate[0])
                            print(listdatabaru[0]+','+listdatabaru[1]+','+listdatabaru[2]+','+listdatabaru[3]+','+listdatabaru[4]+','+listdatabaru[5]+','+listupdate[0], file= open('datamahasiswa.csv', 'a'))
                            with open('datamahasiswa.csv', 'r') as f:
                                lines = f.readlines()
                            with open('datamahasiswa.csv', 'w') as f:
                                for line in lines:
                                    if line.strip('\n') != listhapus[0]+','+listhapus[1]+','+listhapus[2]+','+listhapus[3]+','+listhapus[4]+','+listhapus[5]+','+listhapus[6]:
                                        f.write(line)
                                f.close()
                            print('\n>>> DATA BERHASIL DI UPDATE <<<')
                        else:
                            stop = False
                        a += len(list_nim)
                    else:
                        a += 1
            stop = True
        else:
            stop = False
        
        print('\n*Note : Silahkan Restart Program ini Agar Data Dapat Tersimpan Dengan Baik ...\n\tTrimakasih :)')

        print('\n\n\n\n*Note : Jika Nim Merasa Sudah Didaftarkan\n\tTetapi Tidak dapat DiCari Silahkan \n\tBuka Menu Utama Lalu Cari Ulang.. \n\tTrimakasih :)')

        back = input('\n>> Kembali Ke Menu Utama <y/n> ? ')
        
        if back == 'y':
            menuutama()
        else:
            editdata()

# Fungsi Untuk Membuka Menu Utama Data Mahasiswa
def menuutama():
    os.system('cls')
    print('### Program CRUD CSVbase By Akbaroke >> https://github.com/Akbaroke/ ###\n')
    print('==========================================================================')
    print('SELAMAT DATANG DI MENU UTAMA PROGRAM CRUD BIODATA MAHASISWA')
    print('PILIHAN AKSES PROGRAM : \n1) MENU \n2) PENCARIAN DATA \n3) TAMBAH DATA MAHASISWA \n4) EDIT DATA \n5) HAPUS DATA \n6) TUTUP')
    print('==========================================================================')
    pilihan = input('Pilih Satu Nomor Akses diatas : ')
    if pilihan == '1':
        menuutama()
    elif pilihan == '2':
        caridata()
    elif pilihan == '3':
        tambahdata()
    elif pilihan == '4':
        editdata()
    elif pilihan == '5':
        hapusdata()
    else:
       input('\n\n>> TERIMAKASIH TELAH MENGUNAKAN PROGRAM INI SEE YOU AGAIN BYEE ...')

menuutama()