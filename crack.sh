hashcat -m0 -a0 -o crack_file1.txt Hashes/archivo_1 diccionarios/diccionario_1.dict diccionarios/diccionario_2.dict --potfile-disable
hashcat -m10 -a0 -o crack_file2.txt Hashes/archivo_2 diccionarios/diccionario_1.dict diccionarios/diccionario_2.dict --potfile-disable
hashcat -m10 -a0 -o crack_file3.txt Hashes/archivo_3 diccionarios/diccionario_1.dict diccionarios/diccionario_2.dict --potfile-disable
hashcat -m1000 -a0 -o crack_file4.txt Hashes/archivo_4 diccionarios/diccionario_1.dict diccionarios/diccionario_2.dict --potfile-disable
hashcat -m1800 -a0 -o crack_file5.txt Hashes/archivo_5 diccionarios/diccionario_1.dict diccionarios/diccionario_2.dict --potfile-disable
