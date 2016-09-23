import os
import commands
import subprocess
import sys
def ftp_eos_data(YYYY, DOY, HHMM, ftpuser, ftppwd, destinationROOT, FTPHOST='ftp://nrt1.modaps.eosdis.nasa.gov', FTPDIR='allData/1/MYD00F'):
    '''This forms up an wget request to the nasa eosdis ftp site and uses wget to get the files.

    This site only keeps a few days of data.

    example input:
        FTPHOST='ftp://nrt1.modaps.eosdis.nasa.gov'
        FTPDIR='allData/1/MYD00F'
        YYYY, DOY = futs.datestring_to_YYYY_DOY(date) # YYYY='2016', DOT='223'
        ftpuser='rjohnson'
        ftppwd = <as a string...>
        destinationROOT='/Users/rjohnson/'
        HHMM = '2330' # this is the granule time.
        remoteFTPPath=os.path.join(FTPHOST, FTPDIR, YYYY, DOY)
        ftppathtofile = '%s/MYD00F.A%s%s.%s.001.NRT' % (remoteFTPPath,YYYY,DOY,HHMM)
        destinationPath=os.path.join(destinationROOT, YYYY, DOY)

    This will return a bunch of text that is the output form the wget. You can then look for key words or pharses in it to see what happened:
        'Remote file no newer than local file' in pipe_output
        'No such file' in pipe_output
        'No such directory' in pipe_output

    '''
    remoteFTPPath=os.path.join(FTPHOST, FTPDIR, YYYY, DOY)
    destinationPath=os.path.join(destinationROOT, YYYY, DOY)
    CMD = 'mkdir -p %s' % destinationPath
    result = commands.getstatusoutput(CMD)
    assert result[0] is 0, "Failed to create destinationPath (%s)" % destinationPath
    del CMD #do some cleaning up.
    del result
    ftppathtofile = '%s/MYD00F.A%s%s.%s.001.NRT' % (remoteFTPPath,YYYY,DOY,HHMM)
    print ftppathtofile
    CMD1 = "wget -N --user=%s --password=%s --ignore-length --tries=3 --progress=dot:mega  %s -P %s" % (ftpuser, ftppwd, ftppathtofile, destinationPath)
    print "CMD1 = %s" % CMD1
    # result = commands.getstatusoutput(CMD1) # trying to run the wget command.
    # assert result[0] is 0, "Failed to wget the file (%s)" % result
    command = CMD1.split()
    try:
        pipe = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE)
        pipe_output, _  = pipe.communicate()
    except:
        print "Error executing the wget CMD = %s" % CMD1
        print "Error msg was:"
        e = sys.exc_info() # Return information about the most recent exception caught by an except clause in the current stack frame or in an older stack frame.
        print e
    print(pipe_output)
    del CMD1 #do some cleaning up.
    return pipe_output
