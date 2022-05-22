from mne_realtime import MockLSLStream
import bbtools as bbt


# this is the host id that identifies your stream on LSL
host = 'localhost'
# this is the max wait time in seconds until client connection
wait_max = 5

# data
raw = bbt.read_csv(
    "../../data/Rubert_14_may/Rubert_mordida_1/EEG.csv",
    ['Fp1', 'Fp2', 'F3', 'F4', 'C1', 'C3', 'C2', 'C4', 'CP1', 'CP3', 'CP2', 'CP4', 'Cz', 'O1', 'O2', 'Pz']
)

def startMockServer():
    # For this example, let's use the mock LSL stream.
    stream = MockLSLStream(host, raw, 'eeg', time_dilation=20)
    stream.start()

if __name__ == '__main__':
    startMockServer()