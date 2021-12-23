from method import *;


start = True;
method = method(); 


print('Program Data Sederhana'.center(80,' '));

while (start):
    print('(T) Tambah Data, (U) Ubah Data, (H) Hapus Data, (S) Tampilkan Data, (E) Exit Program');

    inputUser = str(input('Pilih Menu: '));
    inputs = inputUser.lower();

    if inputs == 't':
        method.tambah();

    elif inputs == 'u':
        inputNamaUpdate = str(input('Masukan Nama: '));
        method.ubah(inputNamaUpdate);

    elif inputs == 'h':
        inputNamaUpdate = str(input('Masukan Nama: '));
        method.hapus(inputNamaUpdate);

    elif inputs == 's':
        method.tampilkan();
            
    elif inputs == 'e':
        print("Program dihentikan");
        start = False;
    
    else:
        print('Input Salah!');