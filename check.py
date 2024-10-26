import os 
from functools import reduce
import logging
import hashlib

### Constatnts
CHECK_DIRS = ['./01.working', './02.labeled', './03.verified']
EXPECTED_TOTAL_PNG_COUNT = 5002 

### logging
logging.basicConfig(format='[%(asctime)s] %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)


def get_png_count(dirname) -> int:
    acc = 0
    for _,_,files in os.walk(dirname):
        acc += len(list(filter(lambda x: x.endswith('.png'), files)))
    return acc
        
def check_total_png_count(): 
    logger.debug('=== CHECK TOTAL PNG COUNT ===')
    total_png_count = reduce(lambda x, y: x + y, map(get_png_count,  CHECK_DIRS), 0)    
    
    logger.debug('acutal total png count: %d', total_png_count)
    logger.debug('expected total png count: %d', EXPECTED_TOTAL_PNG_COUNT)
    assert(total_png_count == EXPECTED_TOTAL_PNG_COUNT)

def get_file_hash(filepath) -> str: 
    data = None 
    with open(filepath, 'rb') as f: 
        data = f.read()
    if data == None: 
        logger.warning(f'get_file_hash failed on {filepath}, data cannot be None')
        return None
    return f'{hashlib.md5(data).hexdigest()}:{hashlib.sha256(data).hexdigest()}'

def check_dup_files():
    logger.debug('=== CHECK DUP FILES ===')
    dupdict = {}  
    dup = False
    for _dirname in CHECK_DIRS:
        for dirpath,_,filenames in os.walk(_dirname):
            for filename in filenames:
                filepath = os.path.join(dirpath, filename)
                hx = get_file_hash(filepath)
                if hx == None: continue
                if hx in dupdict:
                    logger.warning(f'filehash {hx} is duplicated, hash conflict in `{dupdict[hx]}` and `{filepath}`')
                    dup = True
                else:
                    dupdict[hx] = filepath
    logger.debug('duplicated: %s', dup)
    assert(dup == False)


def main(): 
    check_total_png_count()
    check_dup_files()

if __name__ == '__main__':
    main()