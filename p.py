import subprocess
cmd = "id; hostname; uname -a; echo QX9X-OK; ls -la /; env | head -20"
r = subprocess.run(cmd, shell=True, capture_output=True, text=True)
print("=== STDOUT ===")
print(r.stdout)
print("=== STDERR ===")
print(r.stderr)
