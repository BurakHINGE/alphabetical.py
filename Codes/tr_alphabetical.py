while True:
	def alfabetik_siralama():
		a = input("Kelimeleri birer boşluk bırakarak giriniz: ").split()
		a.sort()

		print("Alfabetik sıralama: ",a)

	alfabetik_siralama()
