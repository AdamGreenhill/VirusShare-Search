# VirusShare.py
#   download VirusShare hashes and search for specified hashes
# Author: Sent1ent
# Version: 1.0
# Date: February 22nd, 2016
import argparse
import os
import time
from urllib.request import urlopen

def downloader(directory, iteration):
	# Downloads given URL
	url = 'https://virusshare.com/hashes/VirusShare_%05d.md5' % iteration
	exists = os.path.isfile(directory + ("\VirusShare_%05d.md5" % iteration))
	
	if not exists:
		print("  Downloading {0} into {1}...".format(url, directory))

		file_path = os.path.join(directory, os.path.basename(url))
		contents = urlopen(url)
		file_output = open(file_path,'wb')
		file_output.write(contents.read())
		file_output.close()
	else: 	print("Skipping " + directory + ("\VirusShare_%05d.md5" % iteration))

	time.sleep(1)


def find_missing(directory, latest):
	# find all files, parse files for end number, remove any files from 'to_find'
	to_find = list(range(0,latest+1))
	for i in os.listdir(directory):
		to_find.remove(int(''.join(c for c in i if c.isdigit())[:5]))
	return to_find

def parse_amount(amount):
	to_find = []
	try:
		if ',' in amount:
			# if a comma seperation (e.g. 10,11,12) is specified
			temp = amount.split(',')
			for i in temp:
				to_find.append(int(i))
			return to_find
		elif '-' in amount:
			# if a range (e.g. 10-20) is specified
			temp = amount.split('-')
			for i in range(int(temp[0]),int(temp[1]) + 1):
				to_find.append(i)
			return to_find
		else:
			# if a single number (e.g. 123) is specified
			to_find.append(int(amount))
			return to_find
	except ValueError:
		print("  ERROR: incorrect value given for update range.")
		exit()

def update(directory, amount, latest):
	try:
		l = int(latest)
	except ValueError:
		print("  ERROR: incorrect value given for latest hash release.")
		exit()

	if amount == "all":
		# Downloads all md5 files
		for i in range(0,l):
			downloader(directory,i)
	elif amount == "missing":
		# Finds all md5 files not in a directory
		to_find = find_missing(directory, l)
		for i in to_find:
			downloader(directory,i)
	else:
		# Parses amount...
		to_find = parse_amount(amount)
		for i in to_find:
			downloader(directory,i)

def search(directory, term):
	counter = 1
	for file_to_search in os.listdir(directory):
		full_file_path = os.path.join(directory, file_to_search)
		if os.path.isfile(full_file_path):
			with open(full_file_path) as f:
				for line in f:
					if term in line:
						print('FOUND|{0}|{1}|{2}'.format(term,file_to_search, counter))
						return
					counter += 1
		counter = 1
	print('     |{0}|{1}|{2}'.format(term,"None                ", -1))

def main():
	parser = argparse.ArgumentParser(description='tool to download VirusShare hash files and search them for specified hashes')
	parser.add_argument('-s','--search', help='hash to search for in local repository (hint: specify any number of hashes)', nargs="+")
	parser.add_argument('-u','--update', help='updates local hash containing files (--update all/missing/10,11,12/0-20)')
	parser.add_argument('-l','--latest', help='sets latest VirusShare file released (default: 371)', default='371')
	parser.add_argument('-d','--directory', help='sets working directory (default: VirusShare_Hashes)', default='VirusShare_Hashes')

	args = parser.parse_args()
	directory = args.directory
	latest = args.latest

	if not os.path.exists(directory):
		os.makedirs(directory)

	if args.update is not None:
		update(directory, args.update, latest)

	if args.search is not None:
		print("     | Hash                           | File               | Line")
		for t in args.search:
			search(directory, t)

	if args.search is None and args.update is None:
		parser.print_help()

if __name__ == "__main__":
	main()
