a=([7,4,3,5,4,5,"-"],[5,8,9,9,7])
b=([6,3,3,8,"+"],[5,8,9,9])



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
					
			if lda>=ldb: #decimal a > decimal b (check)
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
				
				if lea>=leb: #decimal a > decimal b y entera a > entera b (check)
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
					if enta[0]=="+" and entb[0]=="+":
						ents.append("+")
					elif enta[0]=="-" and entb[0]=="-":
						ents.append("-")
					entss=list(reversed(ents))	
				else: #decimal a > decimal b y entera a < entera b	(check)
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
					if enta[0]=="+" and entb[0]=="+":
						ents.append("+")
					elif enta[0]=="-" and entb[0]=="-":
						ents.append("-")
					entss=list(reversed(ents))
					

					
			else: # decimal a < decimal b (check)
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
																																																																																															
				if lea>=leb: #parte decimal a < decimal b y entera a > entera b (check)
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
						
					if enta[0]=="+" and entb[0]=="+":
						ents.append("+")
					elif enta[0]=="-" and entb[0]=="-":
						ents.append("-")	
					
					entss=list(reversed(ents))
				
				else:#parte decimal a < decimal b y entera a < entera b (check)
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
						
					if enta[0]=="+" and entb[0]=="+":
						ents.append("+")
					elif enta[0]=="-" and entb[0]=="-":
						ents.append("-")
					entss=list(reversed(ents))	
	
#-----------------------------------------------------------------------------------------------------------------------	
	elif (enta[0]=="+" and entb[0]=="-") or (enta[0]=="-" and entb[0]=="+"): #suma signos diferentes
		 	
			if lda>=ldb and lea>leb: #decimal a > decimal b
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
					
				if (enta[0]=="+" and entb[0]=="-"):
					ents.append("+")
				elif (enta[0]=="-" and entb[0]=="+"):
					ents.append("-")
				entss=list(reversed(ents))
				
				
			
			elif lda>=ldb and leb>lea:		
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
					
				if enta[0]=="-" and entb[0]=="+":
					ents.append("+")
				elif enta[0]=="+" and entb[0]=="-":
					ents.append("-")
					
				entss=list(reversed(ents))

				
				
				
			elif lda<ldb and leb>lea:
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
					
				if enta[0]=="+" and entb[0]=="-":
					ents.append("-")
				elif enta[0]=="-" and entb[0]=="+":
					ents.append("+")
				entss=list(reversed(ents))
				
			elif lda<ldb and lea>leb:
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
				if enta[0]=="-" and entb[0]=="+":
					ents.append("-")
				elif enta[0]=="+" and entb[0]=="-":
					ents.append("+")
				entss=list(reversed(ents))
#-----------------------------------------------------------------------------------------------------------

		
			elif (lda>=ldb) and lea==leb:
				i=0
				while i>=0 and i<(lda-ldb):
					decib.insert(i,0)
					i=i+1	
						
				m=0
				while m>=0 and m<(lea-2):

					if enta[m+2]>entb[m+2]:
						
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
						
						if enta[0]=="-" and entb[0]=="+":
							ents.append("-")
						elif enta[0]=="+" and entb[0]=="-":
							ents.append("+")
						entss=list(reversed(ents))
						break
						
					
					elif enta[m+2]<entb[m+2]:
					
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
							
						if enta[0]=="-" and entb[0]=="+":
							ents.append("+")
						elif enta[0]=="+" and entb[0]=="-":
							ents.append("-")	
						entss=list(reversed(ents))
						break	
					m=m+1
#---------------------------------------------------------------------------------------------------					
				
			elif (lda<ldb) and lea==leb:
				i=0
				while i>=0 and i<(ldb-lda):
					decia.insert(i,0)
					i=i+1	
						
				m=0
				while m>=0 and m<(leb-2):

					if enta[m+2]>entb[m+2]:
						
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
							enterb[0]=enterb[0]+1
							decs.append(decia[ldb-1]-decib[ldb-1]+10)
						else:
							decs.append(decia[ldb-1]-decib[ldb-1])
				
						decss=list(reversed(decs))
			
			
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
						if enta[0]=="-" and entb[0]=="+":
							ents.append("-")
						elif enta[0]=="+" and entb[0]=="-":
							ents.append("+")
						entss=list(reversed(ents))
						
						break
	
					elif enta[m+2]<entb[m+2]:
					
						j=0							
						while j<(ldb-1):
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
							
						if enta[0]=="-" and entb[0]=="+":
							ents.append("+")
						elif enta[0]=="+" and entb[0]=="-":
							ents.append("-")	
						entss=list(reversed(ents))
						break
					m=m+1
							
 #------------------------------------------------------------------------
			
			
 	for k in entss:
		print k,
	print ",",
	for k in decss:
		print k,	
																


				
print " "
print "a+b= ",
suma(a,b)		
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------	

def resta(a, b):
	ents=[]
	decs=[]
	i=0
	if (enta[0]=="+" and entb[0]=="-") or (enta[0]=="-" and entb[0]=="+"): #suma signos iguales
					
			if lda>=ldb: #decimal a > decimal b (check)
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
				
				if lea>=leb: #decimal a > decimal b y entera a > entera b (check)
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
					if enta[0]=="+" and entb[0]=="-":
						ents.append("+")
					elif enta[0]=="-" and entb[0]=="+":
						ents.append("-")
					entss=list(reversed(ents))	
				else: #decimal a > decimal b y entera a < entera b	(check)
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
					if enta[0]=="+" and entb[0]=="-":
						ents.append("+")
					elif enta[0]=="-" and entb[0]=="+":
						ents.append("-")
					entss=list(reversed(ents))
					

					
			else: # decimal a < decimal b (check)
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
																																																																																															
				if lea>=leb: #parte decimal a < decimal b y entera a > entera b (check)
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
						
					if enta[0]=="+" and entb[0]=="-":
						ents.append("+")
					elif enta[0]=="-" and entb[0]=="+":
						ents.append("-")	
					
					entss=list(reversed(ents))
				
				else:#parte decimal a < decimal b y entera a < entera b (check)
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
						
					if enta[0]=="-" and entb[0]=="+":
						ents.append("-")
					elif enta[0]=="+" and entb[0]=="-":
						ents.append("+")
					entss=list(reversed(ents))	
	
#-----------------------------------------------------------------------------------------------------------------------	
	elif (enta[0]=="+" and entb[0]=="+") or (enta[0]=="-" and entb[0]=="-"): #suma signos diferentes
		 	
			if lda>=ldb and lea>leb: #decimal a > decimal b
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
					
				if (enta[0]=="+" and entb[0]=="+"):
					ents.append("+")
				elif (enta[0]=="-" and entb[0]=="-"):
					ents.append("-")
				entss=list(reversed(ents))
				
				
			
			elif lda>=ldb and leb>lea:		
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
					
				if enta[0]=="-" and entb[0]=="-":
					ents.append("+")
				elif enta[0]=="+" and entb[0]=="+":
					ents.append("-")
					
				entss=list(reversed(ents))

				
				
				
			elif lda<ldb and leb>lea:
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
					
				if enta[0]=="+" and entb[0]=="+":
					ents.append("-")
				elif enta[0]=="-" and entb[0]=="-":
					ents.append("+")
				entss=list(reversed(ents))
				
			elif lda<ldb and lea>leb:
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
				if enta[0]=="-" and entb[0]=="-":
					ents.append("-")
				elif enta[0]=="+" and entb[0]=="+":
					ents.append("+")
				entss=list(reversed(ents))
#-----------------------------------------------------------------------------------------------------------

		
			elif (lda>=ldb) and lea==leb:
				i=0
				while i>=0 and i<(lda-ldb):
					decib.insert(i,0)
					i=i+1	
						
				m=0
				while m>=0 and m<(lea-2):

					if enta[m+2]>entb[m+2]:
						
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
						
						if enta[0]=="-" and entb[0]=="-":
							ents.append("-")
						elif enta[0]=="+" and entb[0]=="+":
							ents.append("+")
						entss=list(reversed(ents))
						break
						
					
					elif enta[m+2]<entb[m+2]:
					
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
							
						if enta[0]=="-" and entb[0]=="-":
							ents.append("+")
						elif enta[0]=="+" and entb[0]=="+":
							ents.append("-")	
						entss=list(reversed(ents))
						break	
					m=m+1
#---------------------------------------------------------------------------------------------------					
				
			elif (lda<ldb) and lea==leb:
				i=0
				while i>=0 and i<(ldb-lda):
					decia.insert(i,0)
					i=i+1	
						
				m=0
				while m>=0 and m<(leb-2):

					if enta[m+2]>entb[m+2]:
						
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
							enterb[0]=enterb[0]+1
							decs.append(decia[ldb-1]-decib[ldb-1]+10)
						else:
							decs.append(decia[ldb-1]-decib[ldb-1])
				
						decss=list(reversed(decs))
			
			
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
						if enta[0]=="-" and entb[0]=="-":
							ents.append("-")
						elif enta[0]=="+" and entb[0]=="+":
							ents.append("+")
						entss=list(reversed(ents))
						
						break
	
					elif enta[m+2]<entb[m+2]:
					
						j=0							
						while j<(ldb-1):
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
							
						if enta[0]=="-" and entb[0]=="-":
							ents.append("+")
						elif enta[0]=="+" and entb[0]=="+":
							ents.append("-")	
						entss=list(reversed(ents))
						break
					m=m+1
							
 #------------------------------------------------------------------------
			
			
 	for k in entss:
		print k,
	print ",",
	for k in decss:
		print k,	
																


				
print " "
print "a-b= ",
resta(a,b)		

print " "    


def multiplicacion(a, b):

	if enta[0]=="+" and entb[0]=="+":
		enta.remove("+")
		entb.remove("+")
		enta.pop(0)
		entb.pop(0)
	elif enta[0]=="+" and entb[0]=="-":
		enta.remove("+")
		entb.remove("-")
		enta.pop(0)
		entb.pop(0)		
	elif enta[0]=="-" and entb[0]=="+":
		enta.remove("-")
		entb.remove("+")
		enta.pop(0)
		entb.pop(0)		
	elif enta[0]=="-" and entb[0]=="-":
		enta.remove("-")
		entb.remove("-")
		enta.pop(0)
		entb.pop(0)		
		
	ap=enta+deca
	bp=entb+decb
	mul=[]
	t=0
	listas=[]
	x=0
	for i in ap:
		listas.append([])
		for j in bp:
			if i*j<10:
				listas[x].append(i*j+t)
				t=0
			elif i*j>=10:
				
				listas[x].append(i*j%10+t)
				t=i*j//10	
		if(t!=0):
			listas[x].append(t)
			t=0
		x+=1
	for i in listas:
		print i	
		
				
multiplicacion(a,b)



def division(a, b):
    pass


def comparacion(a, b):
    pass

