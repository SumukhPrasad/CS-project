# --- Launch script for arm64e (Apple Silicon) devices ---
# 
# FOR APPLE SILICON MAC DEVICES
#
# ENSURE Xcode CLT AND Rosetta2 are installed:
#   $ xcode-select -v
#   $ arch

echo "Trying to run main.py with Rosetta2 on $(arch) arch on $(machine) machine with $(sysctl -n machdep.cpu.brand_string)..."
echo

arch -x86_64 python3.10 main.py --sqlpass $1