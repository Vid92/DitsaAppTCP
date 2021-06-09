
class NameOrdened():
	def __init__(self,nameList):
		self.nameList = nameList

		self.listDig = list()
		self.listAlp = list()
		self.listF = list()
		self.listT = list()
		self.listAux = list()
		self.aux = list()
		self.anx = list()
		self.aux2 = list()
		self.aux3 = list()
		self.aux4 = list()
		self.indx = list()
		self.num = list()

	def cod(self):
		x = sorted(self.nameList)
		#print("x:",x)

		for i in range(len(x)):
			list1 = x[i]

			if '-' in list1 != False:
				#print("CON -")
				y = list1.rpartition('-')
				v = list1.rindex('-')
				if list1[v] == '-':
					cmb = y[2]
					digT = len(cmb)
					midig = digT - 2 
					tmp1 = cmb[0:midig]
					tmp = cmb[midig:digT]
					#print("tmp1:",tmp1)
					#print("tmp:",tmp)

					if tmp.isdigit():
						self.listAlp.append(list1)
						
					elif tmp.isalpha():
						self.listAlp.append(list1)

					elif tmp.isalnum():
						self.listAlp.append(list1)

			else:
				#print("SIN -")
				if list1.isdigit():
					self.listDig.append(int(list1))

				elif list1.isalpha():
					self.listAlp.append(list1)

				elif list1.isalnum():
					self.listAlp.append(list1)

		#print("listD:",sorted(self.listDig)) # se realiza orden de numeros
		#print("listAlp:",sorted(self.listAlp))

		if len(self.listAlp) != 0:
			#print("no esta vacio")

			for i in range(len(self.listAlp)):
				dat = self.listAlp[i]
				#print("dat:",dat)

				for j in range(len(dat)):
					if dat[j].isdigit():
						#print("digit")
						self.aux.append(dat[j])
						self.listAux.append("dig")

					elif dat[j].isalpha():
						#print("letra")
						self.aux.append(dat[j])
						self.listAux.append("let")
					
					elif dat[j] == '-':
						#print("letra")
						self.aux.append(dat[j])
						self.listAux.append("let")	
				
				#print("aux:",self.aux)
				#print("listAux:",self.listAux)

				for i in range(0,len(self.listAux)):
					if self.listAux[i] == 'let':
						self.indx.append(i)	

				t = 0
				count = 0
				for j in range(len(self.indx)):
					t+= 1
					if self.indx[j] == t-1:
						count +=1
				
				for k in range(count):
					self.aux2.append(self.aux[k])
					
				if count == len(self.indx):
					part = ''.join(self.aux2)
					self.aux2.clear()
					part2 = dat.partition(part)
					#print("part2:",part2)

				else:
					self.aux.insert(0,'')
					part2 = tuple(self.aux)
					#print("part2E:",part2)

				#print("count:",count)
				#print(len(part2))
				
				for x in range(1,len(part2)):
					flagInt = False
					if part2[x].isdigit():
						nm = part2[x]
						if nm[0] == '0' and len(part2[x]) != 1:
							for i in range(len(nm)):
								self.num.append(int(nm[i])) 
						else:
							self.anx.append(int(part2[x]))
						flagInt = True
					
					if flagInt != True:
						self.anx.append(part2[x])

				#print("num:",self.num)
				#print("anx:",self.anx)

				tup = tuple(self.anx+self.num)
				#print("tup:",tup)

				self.num.clear()
				self.listF.append(tup)
				#print("listF:",listF)

				self.anx.clear()
				self.listAux.clear()
				self.aux.clear()
				self.aux2.clear()
				self.indx.clear()

			k = min(self.listF)
			#print("k:",k)

			final = len(self.listF)
			#print("len:",final)

			t = 0
			while t<final:
				t += 1
				#print("t:",t)
				remov =min(self.listF)
				#print("remove:",remov)
				self.aux.append(min(self.listF))
				for i in range(len(self.listF)):
					if not self.listF[i] == remov:
						self.aux2.append(self.listF[i])	

				self.listF = self.aux2[:]
				#print("y:",y)
				#print("len:",len(aux2))
				self.aux2.clear()

			#print("AUX:",self.aux)

			for j in range(len(self.aux)):
				tup2 = self.aux[j]
				#print("tup2:",tup2)

				for k in range(len(tup2)):
					self.aux4.append(str(tup2[k]))
					#aux2.append(tup[0]+str(tup[1]))

				#print("aux2:",aux2)
				vv = ''.join(self.aux4[:])
				self.aux4.clear()
				#print("vv:",vv)
				self.aux3.append(vv)

			self.listT = sorted(self.listDig[:]) + self.aux3[:]
			#print("listT:",self.listT)

			self.aux.clear()
			self.aux3.clear()
			self.listDig.clear()

			return self.listT

		else:
			#print("vacio")
			self.listT = sorted(self.listDig[:])
			#print("listT:",self.listT)

			self.aux.clear()
			self.aux3.clear()
			self.listDig.clear()

			return self.listT 

if __name__ == '__main__':
	print("name Ord")
	#copia = ['L-K2','L-K1','L-2','L-1','L-3','KL3','L-10','K20','10','11','22','1','2','8','K22','R11','T2','T10','T3','R9','R1','K0-L3','KL01','T02']
	#copia = ['1','11','18','2','4','7']
	#copia = ['L-K2','L-K1','L-2','L-1','L-3','KL3','L-10','K20','K22','R11','T2','T10','T3','R9','R1','K0-L3','KL01','T02']

	nm = NameOrdened(copia)
	x = nm.cod()

	print("x:",x)