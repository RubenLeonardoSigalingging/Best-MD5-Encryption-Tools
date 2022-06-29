#!/usr/bin/env python3


def MD5(created_by="Ruben Leonardo Sigalingging."):
	import tkinter as tk
	from os import system
	from pyfiglet import figlet_format
	import hashlib
	from time import time,sleep
	system("clear")
	system("pip install pyfiglet")
	system("pip install tk")
	system("clear")
	# THIS CODE OR PROGRAM WAS CREATED BY RUBEN LEONARDO SIGALINGGING.
	# THIS CODE OR PROGRAM WAS WRITTEN AND DONE ON WEDNESDAY, JUNE 29, 2022, 11:55 P.M.
	# USING THE PYTHON PROGRAMMING LANGUAGE VERSION 3.8.10
	judul=figlet_format("MD5",font="slant")
	print(judul)
	print("[!] Dibuat Oleh: Ruben Leonardo Sigalingging.")
	print("[!] Dibuat Pada: Rabu, 29 Juni 2022, Pukul 23:55 PM.")
	print("[!] Fungsi: Untuk Mengenkripsi Kata Sandi dan Pesan.\n")


	# BUAT FUNGSI UNTUK MENGENKRIPSI MD5.
	def program_atau_alat_pengenkripsi_kata_sandi_dan_pesan(created_by="Ruben Leonardo Sigalingging"):
		import os
		from os import system
		import tkinter as tk
		import hashlib
		ubah_ke_kode_md5 = kata_sandi_dan_pesan.get()
		gas_ubah_ke_kode_md5=hashlib.md5()
		gas_ubah_ke_kode_md5.update(ubah_ke_kode_md5.encode("ascii"))
		variabel_penampung_string_dari_user.set(str(gas_ubah_ke_kode_md5.hexdigest()))
		# simpan_hasilnya = open("HasilEnkripsiMD5.txt", "w")
		# simpan_hasilnya.write(variabel_penampung_string_dari_user)
		# simpan_hasilnya.write("\n")
		label_program_pengenkripsi_md5_ke_2.config(font=("Helvetica",18,"bold","italic"),fg="green")


	jendela_program=tk.Tk()
	# BUAT JUDUL PROGRAM, YAITU: MD5 Encryption
	jendela_program.title("MD5 Encryption")
	


	# UBAH UKURAN ALAT ATAU PROGRAM NYA, DENGAN CARA GEOMETRY("LEBAR X TINGGI")
	jendela_program.geometry("500x500")


	# UBAH LABEL PROGRAM ATAU TOOLS NYA, DENGAN METODE tk.Label
	from tkinter import font
	# label_program_pengenkripsi_md5=tk.Label(jendela_program,text="\n")
	label_program_pengenkripsi_md5=tk.Label(jendela_program,text="MD5 Encryption Tools By Ruben Leonardo Sigalingging.",font=("Helvetica",15,"roman","bold","italic"))
	# BUAT LABEL PROGRAM NYA, DENGAN METODE: pack()
	# pack = mengemas
	label_program_pengenkripsi_md5.pack()


	# BUAT VARIABEL UNTUK USER MENGINPUTKAN KATA SANDI ATAU PESAN YANG INGIN DIENKRIPSI
	# GASSSSS CODEEEEEE
	kata_sandi_dan_pesan=tk.Entry(jendela_program,font=("Helvetica",12,"roman","bold","italic"),width=9,justify=tk.CENTER)
	kata_sandi_dan_pesan.pack()


	# BUAT TOMBOL UNTUK USER MENGINPUTKAN KATA SANDI ATAU PESAN, YANG INGIN DI ENKRIPSI,
	# METODE NYA ADALAH: tk.Button()
	tombol_penginput_program_pengenkripsi_md5=tk.Button(jendela_program,text="Encryption",command=program_atau_alat_pengenkripsi_kata_sandi_dan_pesan,font=("Helvetica",12,"roman","bold","italic"),fg="green")
	tombol_penginput_program_pengenkripsi_md5.pack()


	# BUAT VARIABEL, UNTUK MENAMPUNG VARIABEL STRING DARI USER, DENGAN METODE: tk.StringVar()
	variabel_penampung_string_dari_user=tk.StringVar()
	variabel_penampung_string_dari_user.set("MD5 Encryption Results")


	# UBAH LABEL PROGRAM ATAU TOOLS NYA LAGI, DENGAN METODE tk.Label
	from tkinter import font
	# label_program_pengenkripsi_md5=tk.Label(jendela_program,text="\n")
	label_program_pengenkripsi_md5_ke_2=tk.Label(jendela_program,text="MD5 Encryption Results",font=("Helvetica",15,"roman","bold","italic"),textvariable=variabel_penampung_string_dari_user,fg="darkcyan")
	# BUAT LABEL PROGRAM NYA, DENGAN METODE: pack()
	# pack = mengemas
	label_program_pengenkripsi_md5_ke_2.pack()


	# BUAT SUPAYA PROGRAM ATAU ALAT INI TIDAK BERHENTI BERJALAN, DENGAN CARA:
	jendela_program.mainloop()
MD5()