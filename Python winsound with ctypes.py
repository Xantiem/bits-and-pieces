# Very basic reimplementation of winsound (Windows only) using Ctypes

import ctypes

winmm = ctypes.WinDLL('winmm.dll')

if winmm.PlaySound(b"sound.wav", None, 0x20000):

    print('Sound has played')
