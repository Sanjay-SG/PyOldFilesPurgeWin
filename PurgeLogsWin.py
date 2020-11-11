import os
import sys
import time

import logging

import datetime

# from datetime import datetime


#Create and configure logger 
logging.basicConfig(filename="C:/Users/GunagiSa/OneDrive - Unisys/Documents/ssg/cmd/PurgeSSIMFilesWin/prd/individual_client/log/purgessimlog_individual.log", 
                    format='%(asctime)s %(message)s', 
                    filemode='a') 
  
#Creating an object 
logger=logging.getLogger() 
  
#Setting the threshold of logger to DEBUG 
logger.setLevel(logging.DEBUG) 



#----------------------------------------------------------------------
def remove(path):
    """
    Remove the file or directory
    """
    '''
    if os.path.isdir(path):
        try:
            os.rmdir(path)
        except OSError:
            print ("Unable to remove folder: %s" % path)
            logging.error("Unable to remove folder: %s" % path)
    else:
    '''
    try:
        if os.path.exists(path):
            os.remove(path)
    except OSError:
        print ("Unable to remove file: %s" % path)
        logging.error("Unable to remove file: %s" % path)

#----------------------------------------------------------------------

def cleanup(number_of_days, path):
    """
    Removes files from the passed in path that are older than or equal 
    to the number_of_days
    """
    totalSizeInBytes = 0
    time_in_secs = time.time() - (number_of_days * 24 * 60 * 60)
    for root, dirs, files in os.walk(path, topdown=False):
        for file_ in files:
            full_path = os.path.join(root, file_)
            stat = os.stat(full_path)
            
            if stat.st_mtime <= time_in_secs:
                sizeInBytes = os.path.getsize(path)
                totalSizeInBytes = totalSizeInBytes + sizeInBytes
                # totalSize = totalSizeInBytes/(1024*1024*1024)
                t = os.path.getmtime(full_path)
                lastModifiedDate = datetime.datetime.fromtimestamp(t)
                logging.info("Removing.. %s ......... %s ......... %s", full_path, lastModifiedDate, sizeInBytes)
                remove(full_path)
        '''   
        if not os.listdir(root):
            logging.info("Removing.. %s", root)
            # remove(root)
        '''
    # return totalSizeInBytes
    '''
    totalSize = (totalSizeInBytes/(1024*1024*1024))
    logging.info("-----------------------------------------------------------")
    logging.info("Total size for : %s is %s", path, totalSize)
    logging.info("-----------------------------------------------------------")
    '''
    return totalSizeInBytes


            
#----------------------------------------------------------------------
if __name__ == "__main__":
    # days, path = int(sys.argv[1]), sys.argv[2]

    # n = len(sys.argv) 
    # logging.info("Total arguments passed:", n)
    logging.info(sys.argv[0])

    logging.info(sys.argv[1])

    days = int(sys.argv[1])

    dir_path = sys.argv[2]

    logging.info(days)

    logging.info(dir_path)

    # days = 45 --->without cmd ln args
    # cleanup(days, path)

    totalSize = cleanup(days, dir_path)
    logging.info("-----------------------------------------------------------")
    # logging.info("Total size for : [%s] is %s", dir_path, totalSize(1024*1024*1024))
    logging.info("-----------------------------------------------------------")
    # totalSize = (totalSizeInBytes/(1024*1024*1024))
    # logging.info("-----------------------------------------------------------")
    # logging.info("Total size for : %s is %s", path, totalSize)
    # logging.info("-----------------------------------------------------------")