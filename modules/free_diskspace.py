import ctypes
import os
import platform
import sys

def run(**args):
    """Cross-Platform Method to return folder/drive free space (in gigabytes)."""
    if platform.system() == 'Windows':
        free_bytes = ctypes.c_ulonglong(0)
        ctypes.windll.kernel32.GetDiskFreeSpaceExW(ctypes.c_wchar_p(dirname),None, None, ctypes.pointer(free_bytes))
        free_mb = free_bytes.value / 1024 / 1024 / 1024
        return str(free_mb) + "GB"
    else:
        st = os.statvfs(dirname)
        free_mb = st.f_bavail * st.f_frsize / 1024 / 1024 / 1024
        return str(free_mb) + "GB"
