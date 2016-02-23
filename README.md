# VirusShare-Search
Downloads VirusShare hashes ([for more information click here!][2]) and searches them for specified MD5 hash values.

## Background
[VirusShare][1] is an awesome virus sharing site. Unfortunately, as far as I was able to find, there isn't an easy way to find what file contains a specific hash. 

**Note:** if there is a way to perform this functionality, let me know!

## How-to
1. `git clone https://github.com/AdamGreenhill/VirusShare-Search.git`
2. `python VirusShare-Search.py --update all`   # this will download all the files containing hashes

    alternatively `-u missing/number range (e.g. 10-200)/specific numbers (e.g. 10,11,12)`

3. `python VirusShare-Search.py --search 2d75cc1bf8e57872781f9cd04a529256 e7ae40d25a6da15cdd3712f4f55153ac`

    alternatively `-s hash1 hash2 hash3 etc.`
 
## Configuration
- `-d` or `--directory`: sets the working directory (e.g. where the search takes place, and where the hash files are downloaded to)
- `-l` or `--latest`: sets the latest hash repository. This is primarily used when updating the local repository of hash files

## Compatibility
- Python 3.4
- Platform independent

[1]: https://virusshare.com/
[2]: https://virusshare.com/hashes.4n6
