import os
from shutil import copyfile
import glob
import urllib.request
import string

homedir = os.getcwd()

URL = "https://www.goethe-verlag.com/book2/"
ShortLang = ['PX', 'ES', 'EM', 'FR', 'IT', 'DE']

def downloadbla():
	for L2 in ShortLang:
		if not os.path.exists(homedir+"/get002"):
            os.mkdir(homedir+"/get002")
		for L1 in ShortLang:
			if not L2 != L1:
				#os.system("C:\Windows\System32\curl $(curl -u username:password -s https://api.example.com/v1.1/reports/11111?fields=download | jq '.report.download' -r) > 'C:\sample.zip'")
				os.system("C:\Windows\System32\curl $(curl -k 'https://www.goethe-verlag.com/book2/'"+L2+'/'+L2+L1+'/'+L2+L1+'002.HTM') > homedir+'/get002/'+L2+L1+'txt+audio.HTM')
				copyfile(homedir+"/get002/"+L2+"txt+audio.HTM", homedir+"/get002/"+L2+L1+"txt.HTM")

def downloadphrases():
	for L1 in ShortLang:
		for L2 in ShortLang:
			if L1 != L2:
				for	x in range(3, 104, 10):
					if len(str(x)) == 1:
						y = str("00" + str(x))
					elif len(str(x)) == 2:
						y = str("0" + str(x))
					elif len(str(x)) == 3:
						y = str(x)

					print(homedir+"/phrases/"+L1+L2+"/"+y)
					#os.mkdir(homedir + "/phrases/" + L1 + L2 + "/" + y)
					os.system("C:\Windows\System32\curl $(curl -k 'https://www.goethe-verlag.com/book2/'"+L1+'/'+L1+L2+'/'+L1+L2+y+'.HTM' > homedir+'/phrases/'+L1+L2+'/'+y+'/'+L1+L2+y+'.HTM')

def downloadvocab():
	for L1 in ShortLang:
		for L2 in ShortLang:
			if L1  != L2:
				for x in range(1, 43):
					if len(str(x)) == 2:
						y="0"+str(x)
					elif len(str(x)) == 3:
						y=str(x)

					os.mkdir(homedir+"/vocab/"+L1+L2)
					os.mkdir(homedir+"/vocab/"+L1+L2+"/"+y)
					os.system("C:\Windows\System32\curl $(curl -k 'https://www.goethe-verlag.com/book2/_VOCAB/'"+L1+"/"+L1+L2+"/"+y+".HTM" > homedir+"/vocab/"+L1+L2+"/"+y+"/"+y+".HTM")

def clean002():
	for L in ShortLang:
		for dir in glob.glob(homedir+'/get002/'+L+"*HTM"):
			if len(dir) == 0:
				exit
			for F in dir:
				NewF = str(F).split('.')[0]
				pattern='<a href="'+L
				with open(F, 'a+') as inNewF:
					for line in inNewF:
						if pattern in line:
							with open(homedir+'/goodvocab/get002/'+L+'/'+NewF+'.clean', 'a+') as inNewF:
								line = line.replace('s#<a href=','').replace('"><span class="gray">', ';').replace(' </span>', ';').replace('</a>', '')
								inNewF.write(line)

def changenum002():
	for L in ShortLang:
		for dir in glob.glob(homedir+'/goodvocab/get002/'+L+'*clear'):
			if len(dir) == 0:
				exit
			for F in dir:
				NewF = str(F).split('.')[0]
				with open(F, 'r+') as inNewF:
					for line in inNewF:
						p = line.split(';')[0]
						x = line.split(':')[1]
						n = line.split(';')[2]
						if len(x) == 2:
							y = "00"+"x"
						elif len(x) == 2:
							y = "0"+"x"
						elif len(x) == 2:
							y="x"

						with open(NewF+".num", 'a+') as outNewF:
							outNewF.write(p+";"+y+";"+n)

def clearphrases():
	#for x in {3..102}; do
	#	if [ $(echo $x | wc -c) == 2 ]; then
	#		y="00$x"
	#	elif [ $(echo $x | wc -c) == 3 ]; then
	#		y="0$x"
	#	elif [ $(echo $x | wc -c) == 4 ]; then
	#		y="$x"
	#	fi
	#done
	for dir in glob.glob(homedir+'/goodvocab/get002/'+L+'*.HTM'):
		if len(dir) == 0:
			exit
		for F in dir:
			output = str(F).split('.')[0] + ".clean"
			with open(homedir+'/Podcasts/podcast101/removecarriage.txt', 'rb') as infile:
				with open(homedir+'/Podcasts/podcast101/removecarriage.clean', 'a+') as outfile:
				for line in infile:
					line = line.replace('\n', '').replace('\r', '')
					line = line.replace('<title>', '\n')
					line = line.replace('<source src="https', '\n')
					line = line.replace('<span class="Stil36"><b>', '\n')
					line = line.replace('<span class="Stil36">', '\n')
					line = line.replace('</span><br /><br /></div></td></tr>', '##\n')
					line = line.replace('</b></span></div></td></tr></table>', '##\n')
					line = line.replace('<span class="Stil36"><b>', '\n###')
					line = line.replace('<tr><td><div class="Stil35">', '\n##')
					line = line.replace('</b></span></div></td></tr>', '##\n')
					line = line.replace('</div></td><td><div class=', '##\n')
					line = line.replace('" type="audio/mpeg" /></audio></td></tr>', '##\n')
					outfile.write(line)

			with open(homedir+'/Podcasts/podcast101/removecarriage.clean', 'a+') as outfile:
				for line in outfile:
					if not line.startswith('##') or not line.endswith('##'):
						outfile.write(line)
			with open(homedir+'/Podcasts/podcast101/removecarriage.clean', 'a+') as outfile:
				for line in outfile:
					line = line.replace('\n', '').replace('\r', '')
					line = line.replace('.mp3####', '.mp3\n')
					line = line.replace('####', '|')
					outfile.write(line)

def changehtmlcodes():
	def block1():
		for dir in glob.glob(homedir+'/phrases/*.clean':
			if len(dir) == 0:
				exit
			for file in dir:
				if file.find('&#'):
					with open(file, 'rt') as infile:
						with open(homedir+'/lines.tmp', 'a+') as outfile:
							for line in infile:
								outfile.write(str(file)+"|"+line)
						
						dir/lines.tmp

		if os.path.isfile(homedir+'/lines.tmp'):
			with open(homedir+'/lines.tmp', 'rt') as infile:
				for line in infile:
					Fname = line.split('|')[0]
					Code = line.split('|')[1]
					URL = line.split('|')[2]
					x = len(line.find('|'))
					for y in range(1, x + 1):
						i = ( y * 2)
						gotcode = line.split('& |;')[i]
						with open(homedir+'/changecodes.log', 'a+') as outfile:
							outfile.write(Fname+"|"+gotcode+';|'+URL)

	def block2():
		with open(homedir+'/changecodes.log', 'rt') as infile:
			for line1 in infile:
				Fname = line1.split('|')[0]
				Code = line1.split('|')[1]
				URL = line1.split('|')[2]
				codefile = homedir+'/htmlcodes'
				if codefile.find(Code):
					with open(homedir+'/htmlcodes', 'rt') as codelist:
						for line2 in codelist:
							if Code in line2:
								mycode = lines2.split('|')[0]
					openf = open(Fname, 'r+')
						for line3 in openf.readlines()
							string.replace(line3, Code, mycode)
					openf.close()
				else:
					with open(homedir+'/changehtmlcodes.err', 'a+') as codeerror:
						codeerror.write(Fname+'|'+mycode+'|Code not found')
	block1
	block2

def clearphrases2():
	dir = glob.glob(homedir+'/phrases/*.clean')
	for file in dir:
		with open(file, 'r+') as infile:
			with open(file, 'r+') as outfile:
				for line1 in infile:
					moveline1 = line.startswith('##').split('|')[1]
					getline2 = line.startswith('https')
					for line2 in outfile:
						line.replace("|"+moveline1+"|", "|")
						line.startswith("https").replace("https", moveline1+"|https")
						line.replace('##', '')

def rename():
	os.remove(homedir+'/rename.out')
	for L1 in ShortLang:
		for L2 in ShortLang:
			if L1 != L2:
				with glob.glob(homedir+"/phrases")
				for F in $(find $homedir/phrases/ -type f -name "$L1$L2*.clean"); do
					NewF=$(basename $F | cut -d. -f1)
					Dir=$(dirname $F)
					LF=$(echo $NewF | cut -c 1-4)
					NF=$(echo $NewF | cut -c 5-7)
					NewNF=$(expr $NF - 2)
					if [ $(echo $NewNF | wc -c) == 2 ]; then
						NewNF="00$NewNF"
					elif [ $(echo $NewNF | wc -c) == 3 ]; then
						NewNF="0$NewNF"
					elif [ $(echo $NewNF | wc -c) == 4 ]; then
						NewNF="$NewNF"
					fi
					newDir=$homedir/phrases/$LF/$NewNF-$(cat $F | awk 'NR==2' | awk -F"|" '{print $1}' | sed 's/ /_/g')
					newFName="$NewNF$LF-$(cat $F | awk 'NR==2' | awk -F"|" '{print $1}' | sed 's/ /_/g').txt"
					#newFName=$(echo $newFName | sed 's/ /_/g')
					mkdir $homedir/phrases/$LF
					mkdir $newDir
					mv $F $newDir/$newFName | tee -a $homedir/rename.out
					mv $Dir/*.mp3 $newDir
					#exit
				done
			fi
			#exit
		done
		#exit
	done
}

makebook(){
	if [ -f mypolibook.csv ]; then rm mypolibook.csv ; fi
	for line in $(cat PXFR002.num); do
		num=$(echo $line | awk -F";" '{print $2}')
		pxnom=$(grep ";$num;" PXFR002.num | awk -F";" '{print $3}')
		emnom=$(grep ";$num;" EMPX002.num | awk -F";" '{print $3}')
		frnom=$(grep ";$num;" FRPX002.num | awk -F";" '{print $3}')
		denom=$(grep ";$num;" DEPX002.num | awk -F";" '{print $3}')
		esnom=$(grep ";$num;" ESPX002.num | awk -F";" '{print $3}')
		itnom=$(grep ";$num;" ITPX002.num | awk -F";" '{print $3}')
		echo "$num;$pxnom;$emnom;$frnom;$denom;$esnom;$itnom" >> mypolibook.csv
	done
}

nada(){



	#<tr><td><div class="Stil35">eu</div></td><td>
	#<tr><td><div class="Stil35">I</div></td><td>
	#<audio id="3"><source src="https://www.book2.nl/book2/EM/SOUND/0003.mp3" type="audio/mpeg" /></audio></td>
	#<audio id="3"><source src="https://www.book2.nl/book2/PX/SOUND/0003.mp3" type="audio/mpeg" /></audio></td>


	while IFS=";" read file path; do 
		mkdir $path
		cd $path
		wget --no-check-certificate https://www.goethe-verlag.com/book2/PX/PX$L/$file
		for line in $(grep -o 'https://www.book2.nl/book2/ZH/SOUND/........' $file); do
			wget --no-check-certificate $line
		done
		cd ..
	done < chindex
}




#download002
#downloadphrases
#downloadvocab
#clean002
#changenum002
#clearphrases
#changehtmlcodes
#clearphrases2
rename
#changehtmlcodes
#####makebook
