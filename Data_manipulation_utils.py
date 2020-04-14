import numpy as np
from scipy import signal
import scipy


def local_averaging(sequence, wind_size, label, shuffle = True):
    
    for i in range(len(sequence)):
        sequence = np.hstack((sequence, np.mean(sequence[:, i:i+wind_size], 1).reshape(sequence.shape[0], 1)))
        
    if shuffle == True:
        np.random.shuffle(sequence.T)
    
    return sequence, np.ones((1,sequence.shape[1]))*label


def time_domain_features_from_rawdata(rwdata):

    temp_list = []

    for i in range(0, len(rwdata), 256):

        mean = np.mean(rwdata[i:i+512], 0)
        variance = np.var(rwdata[i:i+512], 0)
        rms = np.sqrt(sum(np.square(rwdata[i:i+512]), 0))
        rng = rwdata[i:i+512].max(0) - rwdata[i:i+512].min(0)       # I think, Range and peak-to-peak are the same thing
        skew = scipy.stats.skew(rwdata[i:i+512], 0)
        kurtosis = scipy.stats.kurtosis(rwdata[i:i+512], 0)
        median = np.median(rwdata[i:i+512], 0)
        ptp = np.ptp(rwdata[i:i+512], 0)
        iqr = scipy.stats.iqr(rwdata[i:i+512], 0)
        crestf = rwdata[i:i+512].max(0)/np.sqrt(sum(np.square(rwdata[i:i+512])))

        tfeatures_1 = np.hstack((mean, variance, rms, rng, skew, kurtosis, median, ptp, iqr, crestf))

        temp_list.append(tfeatures_1)

    tfeatures = np.array(temp_list)
    
    return tfeatures[:-2, :].T


def feature_extraction_from_rawdata(raw_array, label, S, L):
        
    acc = raw_array[:, :3]
    gry = raw_array[:, 3:]
        
    ax, ay, az = acc[:, 0], acc[:, 1], acc[:, 2]
    gx, gy, gz = gry[:, 0], gry[:, 1], gry[:, 2]
    
    fax, tax, Sax = signal.spectrogram(ax, fs = 1, window = signal.get_window('hann', 512), nperseg = 512, noverlap = 256)
    fay, tay, Say = signal.spectrogram(ay, fs = 1, window = signal.get_window('hann', 512), nperseg = 512, noverlap = 256)
    faz, taz, Saz = signal.spectrogram(az, fs = 1, window = signal.get_window('hann', 512), nperseg = 512, noverlap = 256)

    fgx, tgx, Sgx = signal.spectrogram(gx, fs = 1, window = signal.get_window('hann', 512), nperseg = 512, noverlap = 256)
    fgy, tgy, Sgy = signal.spectrogram(gy, fs = 1, window = signal.get_window('hann', 512), nperseg = 512, noverlap = 256)
    fgz, tgz, Sgz = signal.spectrogram(gz, fs = 1, window = signal.get_window('hann', 512), nperseg = 512, noverlap = 256)
    
    Sacc = np.vstack((Sax, Say, Saz))
    Sgry = np.vstack((Sgx, Sgy, Sgz))

    if( (S + L) > Sacc.shape[0]):
        print("Error! S + L > total features .")
        return
    
    for i in range(Sacc.shape[1]):
        Sacc[:, i] = np.sort(Sacc[:, i])
        Sgry[:, i] = np.sort(Sgry[:, i])
    
    Sacc = np.vstack((Sacc[:S, :], Sacc[-L:, :]))
    Sgry = np.vstack((Sgry[:S, :], Sgry[-L:, :]))
    
    Sfeatures = np.vstack((Sacc, Sgry))
    
    # Creating Labels
    labels = np.ones(( 1, Sfeatures.shape[1]))
    labels = labels*label
    
    return Sfeatures, labels



def split_data_labelwise(X, Y):
    
    x1 = []
    x2 = []
    x3 = []
    x4 = []
    x5 = []
    x6 = []
    x7 = []
    x8 = []
    x9 = []
    x10 = []
    x11 = []
    x12 = []
    
    for i in range(len(Y)):

        if(Y[i] == 1):
            x1.append(X[i, :])

        if(Y[i] == 2):
            x2.append(X[i, :])

        if(Y[i] == 3):
            x3.append(X[i, :])

        if(Y[i] == 4):
            x4.append(X[i, :])

        if(Y[i] == 5):
            x5.append(X[i, :])

        if(Y[i] == 6):
            x6.append(X[i, :])

        if(Y[i] == 7):
            x7.append(X[i, :])

        if(Y[i] == 8):
            x8.append(X[i, :])

        if(Y[i] == 9):
            x9.append(X[i, :])

        if(Y[i] == 10):
            x10.append(X[i, :])

        if(Y[i] == 11):
            x11.append(X[i, :])

        if(Y[i] == 12):
            x12.append(X[i, :])
            
    return np.array(x1), np.array(x2), np.array(x3), np.array(x4), np.array(x5), np.array(x6), np.array(x7), np.array(x8), np.array(x9), np.array(x10), np.array(x11), np.array(x12)
