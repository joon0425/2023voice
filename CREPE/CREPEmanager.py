import os,sys
import numpy as np
print(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import crepe

def verify_f0(FILE):
    FILE = os.path.splitext(FILE)[0]
    FILE += ".f0.csv"
    result = np.loadtxt(FILE, delimiter=',', skiprows=1)
    #assert np.mean(result[:, 2] > 0.5) > 0.98 # it should be confident enough about the presence of pitch in every frame
    #assert np.corrcoef(result[:, 1]) > 0.99 # the frequencies should be linear
    #os.remove(FILE)
    return result

def test_sweep(FILE):
    """
    models = {
    'tiny': None,
    'small': None,
    'medium': None,
    'large': None,
    'full': None
}
    """
    crepe.process_file(FILE,step_size=100,model_capacity='medium')
    return verify_f0(FILE)

def test_sweep_cli(FILE):
    assert os.system("crepe {}".format(FILE)) == 0
    return verify_f0(FILE)
    
def FR_mP(FILE): # Full-Range mean of Pitch
    a = np.array(test_sweep(FILE))
    a = a.transpose((1,0))
    num = (a[2]>0.8).sum()
    return (a[1]*(a[2]>0.8)).sum()/num

