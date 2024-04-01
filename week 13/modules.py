#Module types

## 1) Standard/in-built: part of the language itself. Like Random
## 2) External: not part of the language, has to be installed before importing. Pandas and Numpy
## 3) Custom: Not to be shared with anyone else, usually stored in a seperate file, built by the devs who need to use them for the specific use cases

#import find_index_mod
#req_idx = find_index_mod.find_index(["apple", "kiwi", "mango", "orange"], 'mango')

#same as below, just changining name to make typing easier

#import find_index_mod as fim
#req_idx = fim.find_index(["apple", "kiwi", "mango", "orange"], 'mango')
#print(req_idx)
#print(fim.test_var)


#to import only specific things

from find_index_mod import find_index as fi
req_idx = fi(["apple", "kiwi", "mango", "orange"], 'mango')
print(req_idx)

print('Running modules intro: ', __name__)