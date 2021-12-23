from tabulate import tabulate;

datas = [{
    'nama' : 'No Data Found!'    
    }];

class method:
    
    def tambah(self):
        inputNama = str(input('Masukan Nama: '));
        inputNik = int(input('Masukan NIK: '));
        inputNilaiTugas = int(input('Masukan Nilai Tugas: '));
        inputNilaiUTS = int(input('Masukan Nilai UTS: '));
        inputNilaiUAS = int(input('Masukan Nilai UAS: '));
        
        nilaiAkhir = (inputNilaiTugas * 0.30) + (inputNilaiUAS * 0.35) + (inputNilaiUTS * 0.35);
        
        if datas[0]['nama'] == 'No Data Found!':
            del datas[0];
            
        dataAppend = {'nama' : inputNama, 'nik' : inputNik, 'nTugas' : inputNilaiTugas, 'nUTS' : inputNilaiUTS, 'nUAS' : inputNilaiUAS, 'nAkhir' : nilaiAkhir};    
        datas.append(dataAppend);
        print('Data Telah Terinput');
        # print(datas);

    def tampilkan(self):
        if datas[0]['nama'] == 'No Data Found!':
            print(tabulate([datas], tablefmt='fancy_grid', stralign='center'));
        else:
            rows =  [x.values() for x in datas];
            headers = ['Nama', 'NIK', 'Nilai Tugas', 'Nilai UTS', 'Nilai UAS', 'Nilai Akhir'];
            print(tabulate(rows, headers=headers, tablefmt='fancy_grid', stralign='center'));
            
    
    def hapus(self, nama):
        print('Data akan dihapus, silahkan masukan nama dari data dibawah ini: ');
        
        rows =  [x.values() for x in datas];
        headers = ['Nama', 'NIK', 'Nilai Tugas', 'Nilai UTS', 'Nilai UAS', 'Nilai Akhir'];
        print(tabulate(rows, headers=headers, tablefmt='fancy_grid', stralign='center'));
        
        for i in range(0, len(datas)):
            
            if datas[i]['nama'] == nama:
                del datas[i]['nama'];
                del datas[i]['nik'];
                del datas[i]['nTugas'];
                del datas[i]['nUTS'];
                del datas[i]['nUAS'];
                del datas[i]['nAkhir'];
                # datas.append({'nama' : inputNama, 'nik' : inputNik, 'nTugas' : inputNilaiTugas, 'nUTS' : inputNilaiUTS, 'nUAS' : inputNilaiUAS});
                print('Data Telah Dihapus');
                datas[0] = {'nama' : 'No Data Found!' };
                print(datas);

    def ubah(self, nama):
        print('Data Akan diubah, silahkan masukan nama dari data dibawah ini: ');
        
        rows =  [x.values() for x in datas];
        headers = ['Nama', 'NIK', 'Nilai Tugas', 'Nilai UTS', 'Nilai UAS', 'Nilai Akhir'];
        print(tabulate(rows, headers=headers, tablefmt='fancy_grid', stralign='center'));
        
        for i in range(0, len(datas)):
            
            if datas[i]['nama'] == nama:
                inputNilaiTugas = int(input('Masukan Nilai Tugas: '));
                inputNilaiUTS = int(input('Masukan Nilai UTS: '));
                inputNilaiUAS = int(input('Masukan Nilai UAS: '));
                nilaiAkhir = (inputNilaiTugas * 0.30) + (inputNilaiUAS * 0.35) + (inputNilaiUTS * 0.35);

                datas[i]['nTugas'] = inputNilaiTugas;
                datas[i]['nUTS'] = inputNilaiUTS;
                datas[i]['nUAS'] = inputNilaiUAS;
                datas[i]['nAkhir'] = nilaiAkhir;
                # datas.append({'nama' : inputNama, 'nik' : inputNik, 'nTugas' : inputNilaiTugas, 'nUTS' : inputNilaiUTS, 'nUAS' : inputNilaiUAS});
                print('Data Telah Terupdate');
                # print(datas);
            else:
                print("\DATA TIDAK DI TEMUKAN!")



