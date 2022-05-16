import numpy as np

def filters(raw, fmin = 0.5, fmax = 100., notch = 50., sampling_rate = 250, fir_design = 'firwin'):

    '''Apply high/low-pass and notch filters:

        === Args ===
        * raw - mne Raw object: object to apply filters on
        * fmin, fmax - float: bandpass frequencies
        * notch - float: powerline (AC current) frequecy
        * ny_freq - float: Nyquist frequency. Half of the sampling rate
        * fir_design: str: Notch filter type. See mne doc for more details
        * sampling_rate - int, float: sampling rate of the measured data

        === Returns ===
        * raw_c - mne Raw object: Processed Raw copy
        '''
    raw_c = raw.copy()
    raw_c.filter(l_freq = fmin, h_freq = fmax)
    raw_c.notch_filter(np.arange(notch, sampling_rate/2, notch), fir_design=fir_design)
    return raw_c