import subprocess
try:
    r = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=8)
    print("OUT:" + (r.stdout or "")[-3000:])
    print("ERR:" + (r.stderr or "")[-3000:])
    print("RC:", r.returncode)
except Exception as e:
    print("EXC:", repr(e))
