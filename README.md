# VirusShare-Search
Downloads VirusShare hashes ([for more information click here!][2]) and searches them for specified MD5 hash values.

## Description
[VirusShare][1] is an awesome virus sharing site. The site contains collections of malware samples, contained in large zip archives for download. The problem is that there is no easy way to determine which collection has a specific sample you're looking for.

So, to fix this problem, this script will download each of the collections corresponding text files (that state what hashes are contained within), and will search them for specified MD5 hashes.

**NOTE:** I have since found that by using the search bar (located after logging in, on the homepage), specific malware samples can be downloaded by clicking the 'green malware download' button located in the top lefthand corner of the table.

## How-to
1. `git clone https://github.com/AdamGreenhill/VirusShare-Search.git`
2. `python VirusShare-Search.py --update all`   # this will download all the files containing hashes

    alternatively `-u missing/number range (e.g. 10-200)/specific numbers (e.g. 10,11,12)`

3. `python VirusShare-Search.py --search 2d75cc1bf8e57872781f9cd04a529256 e7ae40d25a6da15cdd3712f4f55153ac`

    alternatively `-s hash1 hash2 hash3 etc.`
 
## Configuration
- `-d` or `--directory`: sets the working directory (e.g. where the search takes place, and where the hash files are downloaded to)
- `-l` or `--latest`: sets the latest hash repository. As of writing, the latest is 220. This is used when updating the local repository of hash files

## Compatibility
- Python 3.4
- Platform independent

[1]: https://virusshare.com/
[2]: https://virusshare.com/hashes.4n6
