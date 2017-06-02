'''
@Description : This tool helps to test replace_allele_counts
@Created :  03/23/2017
@Updated : 03/23/2017
@author : Ronak H Shah

'''

import filecmp
import os
from subprocess import Popen
import shlex
import nose
import logging

def setup_module(): 
    this_dir, this_filename = os.path.split(__file__)
    new_dir = os.path.dirname(this_dir)
    inputFileMaf = os.path.join(new_dir, "data", "sample_input", "sample_input.maf")
    inputFillMaf = os.path.join(new_dir, "data", "sample_input", "sample_input_fill.maf")
    outFileMaf = os.path.join(new_dir, "sample_output.maf")
    cmpFileMaf = os.path.join(new_dir, "data", "sample_output", "sample_output.maf")
    scriptFile = os.path.join(new_dir, "replace_allele_counts.py")
    cmd = "python " + scriptFile + " -v -imaf " + inputFileMaf + " -ifill " + inputFillMaf + " -omaf " + outFileMaf
    args = shlex.split(cmd)
    if(os.path.isfile(outFileMaf)):
        os.remove(outFileMaf)
        
    try:
        proc = Popen(args)
        proc.wait()
        retcode = proc.returncode
        if(retcode >= 0):
            pass
    except:
        e = sys.exc_info()[0]
        logging.info("Running of python command: %s \n has failed. The exception produced is %s Thus we will exit",cmd,e)
        sys.exit(1)
             
def teardown_module():
    this_dir, this_filename = os.path.split(__file__)
    new_dir = os.path.dirname(this_dir)
    outFileMaf = os.path.join(new_dir, "sample_output.maf")
    if(os.path.isfile(outFileMaf)):
        os.remove(outFileMaf)

def test_maf_fileSimilarity():
    this_dir, this_filename = os.path.split(__file__)
    new_dir = os.path.dirname(this_dir)
    outFileMaf = os.path.join(new_dir, "sample_output.maf")
    cmpFileMaf = os.path.join(new_dir, "data", "sample_output", "sample_output.maf")
    nose.tools.ok_(filecmp.cmp(outFileMaf, cmpFileMaf), msg="The current result text file and the original result text file for replace_allele_counts are not the same") 

if __name__ == '__main__':
    nose.main()
