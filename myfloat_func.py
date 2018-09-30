a=([8,6,5,5,7,6,"+"],[8,4,5])
b=([8,6,5,5,"+"],[3,4])



a[0].insert(len(a[0])-1,0)
b[0].insert(len(b[0])-1,0)
enta=list(reversed(a[0])) #Parte entera de a
entera=a[0]
deca=a[1] #Parte decimal de a
decia=list(reversed(a[1]))
entb=list(reversed(b[0])) #Parte entera de b
enterb=b[0]
decb=b[1] #Parte decimal de b
decib=list(reversed(b[1]))
lea=len(enta)
lda=len(deca)
leb=len(entb)
ldb=len(decb)
maxe=max(lea,leb)
mine=min(lea,leb)
maxd=max(lda,ldb)
mind=min(lda,ldb)


		
print decia
print decib		

print entera
print enterb

def imprimir(a):

	for i in enta:
		print i, 
	print ",",
	for j in deca:
		print j,
			
print "a= ",
imprimir(a)

def imprimir(b):

	for i in entb:
		print i, 
	print ",",
	for j in decb:
		print j,
			
print "y b= ",
imprimir(b)


def suma(a,b):
	ents=[]
	decs=[]
	i=0
	if (enta[0]=="+" and entb[0]=="+") or (enta[0]=="-" and entb[0]=="-"): #suma signos iguales
					
			if lda>=ldb: #decimal a > decimal b
				i=0
				while i>=0 and i<(lda-ldb):
					decib.insert(i,0)
					i=i+1
											
				j=0							
				while j<(lda-1):
					sumar=decia[j]+decib[j]
					if sumar>=10:
						sumar=sumar-10
						decia[j+1]=decia[j+1]+1
					else:
						sumar=sumar
					j=j+1
					decs.append(sumar)
					
				if decia[lda-1]+decib[lda-1]>=10:
					entera[0]=entera[0]+1
					decs.append(decia[lda-1]+decib[lda-1]-10)
				else:
					decs.append(decia[lda-1]+decib[lda-1])
				
				decss=list(reversed(decs))
				
				if lea>=leb: #decimal a > decimal b y entera a > entera b 
					i=leb
					while i>=leb and i<lea:
						enterb.insert(i-1,0)
						i=i+1
					j=0
					while j<(lea-1):
						sumar=entera[j]+enterb[j]
						if sumar>=10:
							sumar=sumar-10
							entera[j+1]=entera[j+1]+1
				
						else:
							sumar=sumar
						j=j+1
						ents.append(sumar)
					entss=list(reversed(ents))	
				else: #decimal a > decimal b y entera a < entera b	
					i=lea
					while i>=lea and i<leb:
						entera.insert(i-1,0)
						i=i+1		
					j=0
					while j<(leb-1):
						sumar=entera[j]+enterb[j]
						if sumar>=10:
							sumar=sumar-10
							enterb[j+1]=enterb[j+1]+1
				
						else:
							sumar=sumar
						j=j+1
						ents.append(sumar)
					entss=list(reversed(ents))
					

					
			else: # decimal a < decimal b
				i=0
				while i>=0 and i<(ldb-lda):
					decia.insert(i,0)
					i=i+1
				j=0
				while j<ldb-1:
					sumar=decia[j]+decib[j]
					if sumar>=10:
						sumar=sumar-10
						decia[j+1]=decia[j+1]+1
					else:
						sumar=sumar
					j=j+1
					decs.append(sumar)
								
				if decia[ldb-1]+decib[ldb-1]>=10:
					entera[0]=entera[0]+1
					decs.append(decia[ldb-1]+decib[ldb-1]-10)
				else:
					decs.append(decia[ldb-1]+decib[ldb-1])
				
				decss=list(reversed(decs))		
																																																																																															
				if lea>=leb: #parte decimal a < decimal b y entera a > entera b
					i=leb
					while i>=leb and i<lea:
						enterb.insert(i-1,0)
						i=i+1
							
					j=0
					while j<(lea-1):
						sumar=entera[j]+enterb[j]
						if sumar>=10:
							sumar=sumar-10
							entera[j+1]=entera[j+1]+1
				
						else:
							sumar=sumar
						j=j+1
						ents.append(sumar)
					entss=list(reversed(ents))
				
				else:#parte decimal a < decimal b y entera a < entera b
					i=lea
					while i>=lea and i<leb:
						entera.insert(i-1,0)
						i=i+1
							
					j=0
					while j<(leb-1):
						sumar=entera[j]+enterb[j]
						if sumar>=10:
							sumar=sumar-10
							enterb[j+1]=enterb[j+1]+1
				
						else:
							sumar=sumar
						j=j+1
						ents.append(sumar)
					entss=list(reversed(ents))	
	
#-----------------------------------------------------------------------------------------------------------------------	
	elif (enta[0]=="+" and entb[0]=="-") or (enta[0]=="-" and entb[0]=="+"): #suma signos diferentes
		r=0
		while i>=0 and i<1: 
			if lda>=ldb and (lea>leb or (lea==leb and entera[len(entera)-3-r]>enterb[len(entera)-3-r])): #decimal a > decimal b
				i=0
				while i>=0 and i<(lda-ldb):
					decib.insert(i,0)
					i=i+1						
				j=0							
				while j<(lda-1):
					restar=decia[j]-decib[j]
					if restar<0:
						restar=restar+10
						decia[j+1]=decia[j+1]-1
					else:
						restar=restar
					j=j+1
					decs.append(restar)
					
				if decia[lda-1]-decib[lda-1]<0:
					entera[0]=entera[0]-1
					decs.append(decia[lda-1]-decib[lda-1]+10)
				else:
					decs.append(decia[lda-1]-decib[lda-1])
				
				decss=list(reversed(decs))
			
			
				i=leb
				while i>=leb and i<lea:
					enterb.insert(i-1,0)
					i=i+1
				j=0
				while j<(lea-2):
					restar=entera[j]-enterb[j]
					if restar<0:
						restar=restar+10
						entera[j+1]=entera[j+1]-1
				
					else:
						restar=restar
					j=j+1
					ents.append(restar)
				entss=list(reversed(ents))
				
				if enta[0]=="+" and entb[0]=="-":
					print "+",
				elif enta[0]=="-" and entb[0]=="+":
					print "-"

			
			elif lda>=ldb and (leb>lea or (lea==leb and entera[len(entera)-3-r]<enterb[len(enterb)-3-r])):		
				i=0
				while i>=0 and i<(lda-ldb):
					decib.insert(i,0)
					i=i+1						
				j=0							
				while j<(lda-1):
					restar=decib[j]-decia[j]
					if restar<0:
						restar=restar+10
						decib[j+1]=decib[j+1]-1
					else:
						restar=restar
					j=j+1
					decs.append(restar)
					
				if decib[lda-1]-decia[lda-1]<0:
					enterb[0]=enterb[0]-1
					decs.append(decib[lda-1]-decia[lda-1]+10)
				else:
					decs.append(decib[lda-1]-decia[lda-1])
				
				decss=list(reversed(decs))
			
			
				i=lea
				while i>=lea and i<leb:
					entera.insert(i-1,0)
					i=i+1
				j=0
				while j<(leb-2):
					restar=enterb[j]-entera[j]
					if restar<0:
						restar=restar+10
						enterb[j+1]=enterb[j+1]-1
				
					else:
						restar=restar
					j=j+1
					ents.append(restar)
				entss=list(reversed(ents))
				print "-",
				
				
				
			elif lda<ldb and (leb>lea or (lea==leb and entera[len(entera)-3-r]<enterb[len(enterb)-3-r])):
				i=0
				while i>=0 and i<(ldb-lda):
					decia.insert(i,0)
					i=i+1						
				j=0							
				while j<(ldb-1):
					restar=decib[j]-decia[j]
					if restar<0:
						restar=restar+10
						decia[j+1]=decia[j+1]-1
					else:
						restar=restar
					j=j+1
					decs.append(restar)
					
				if decib[ldb-1]-decia[ldb-1]<0:
					enterb[0]=enterb[0]-1
					decs.append(decib[ldb-1]-decia[ldb-1]+10)
				else:
					decs.append(decib[ldb-1]-decia[ldb-1])
				
				decss=list(reversed(decs))
				
				i=lea
				while i>=lea and i<leb:
					entera.insert(i-1,0)
					i=i+1
				j=0
				while j<(leb-2):
					restar=enterb[j]-entera[j]
					if restar<0:
						restar=restar+10
						enterb[j+1]=enterb[j+1]-1
				
					else:
						restar=restar
					j=j+1
					ents.append(restar)
				entss=list(reversed(ents))
				
			elif lda<ldb and (lea>leb or (lea==leb and entera[len(entera)-3-r]>enterb[len(entera)-3-r])):
				i=0
				while i>=0 and i<(ldb-lda):
					decia.insert(i,0)
					i=i+1						
				j=0							
				while j<(ldb-1):
					restar=decia[j]-decib[j]
					if restar<0:
						restar=restar+10
						decia[j+1]=decia[j+1]-1
					else:
						restar=restar
					j=j+1
					decs.append(restar)
					
				if decia[ldb-1]-decib[ldb-1]<0:
					enterb[0]=enterb[0]-1
					decs.append(decia[ldb-1]-decib[ldb-1]+10)
				else:
					decs.append(decia[ldb-1]-decib[ldb-1])
				
				decss=list(reversed(decs))
				
				i=leb
				while i>=leb and i<lea:
					enterb.insert(i-1,0)
					i=i+1
				j=0
				while j<(lea-2):
					restar=entera[j]-enterb[j]
					if restar<0:
						restar=restar+10
						entera[j+1]=entera[j+1]-1
				
					else:
						restar=restar
					j=j+1
					ents.append(restar)
				entss=list(reversed(ents))
				
			elif (lda>=ldb) and (lea==leb and entera[len(entera)-3-r]==enterb[len(entera)-3-r]):
				i=0
				while i>=0 and i<(lda-ldb):
					decib.insert(i,0)
					i=i+1						
				j=0							
				while j<(lda-1):
					restar=decia[j]-decib[j]
					if restar<0:
						restar=restar+10
						decia[j+1]=decia[j+1]-1
					else:
						restar=restar
					j=j+1
					decs.append(restar)
					
				if decia[lda-1]-decib[lda-1]<0:
					decs.append(decia[lda-1]-decib[lda-1]+10)
				else:
					decs.append(decia[lda-1]-decib[lda-1])
				
				decss=list(reversed(decs))
					
				i=leb
				while i>=leb and i<lea:
					enterb.insert(i-1,0)
					i=i+1
				j=0
				while j<(lea-2):
					restar=entera[j]-enterb[j]
					if restar<0:
						restar=restar+10
						entera[j+1]=entera[j+1]-1
				
					else:
						restar=restar
					j=j+1
					ents.append(restar)
				entss=list(reversed(ents))	
				
			elif (lda<ldb) and (lea==leb and entera[len(entera)-3-r]==enterb[len(entera)-3-r]):
				i=0
				while i>=0 and i<(ldb-lda):
					decia.insert(i,0)
					i=i+1						
				j=0							
				while j<(ldb-1):
					restar=decia[j]-decib[j]
					if restar<0:
						restar=restar+10
						decia[j+1]=decia[j+1]-1
					else:
						restar=restar
					j=j+1
					decs.append(restar)
					
				if decia[ldb-1]-decib[ldb-1]<0:
					decs.append(decia[ldb-1]-decib[ldb-1]+10)
				else:
					decs.append(decia[ldb-1]-decib[ldb-1])
				decss=list(reversed(decs))
				
				i=leb
				while i>=leb and i<lea:
					enterb.insert(i-1,0)
					i=i+1
				j=0
				while j<(lea-2):
					restar=entera[j]-enterb[j]
					if restar<0:
						restar=restar+10
						entera[j+1]=entera[j+1]-1
				
					else:
						restar=restar
					j=j+1
					ents.append(restar)
				entss=list(reversed(ents))
			r=r+1
 #------------------------------------------------------------------------
			
 
	
	if enta[0]=="+" and entb[0]=="+":				
		print "+",
	elif enta[0]=="-" and entb[0]=="-":
		print "-",
	
					
																
	for k in entss:
		print k,
	print ",",
	for k in decss:
		print k,

				
print " "
print "a+b= ",
suma(a,b)		
	

def resta(a, b):
    pass


def multiplicacion(a, b):
    pass



def division(a, b):
    pass


def comparacion(a, b):
    pass

