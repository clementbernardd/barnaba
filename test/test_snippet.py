import barnaba as bb
import os
import filecmp
import glob


cwd = os.getcwd()
outdir = "%s/test/tmp" % cwd
refdir = "%s/test/reference/" % cwd
os.system("mkdir -p %s" % (outdir))

fname = "%s/test/data/1S72.pdb" % cwd

def test_snippet():
    bb.snippet(fname,"AAANU",outdir="%s" % outdir)
    for f in glob.glob("%s/1S72*.pdb" %outdir):
        nf = f.replace("tmp","reference")
        assert(filecmp.cmp("%s" % f,"%s" % nf)==True)
