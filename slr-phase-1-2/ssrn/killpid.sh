# Kill by all logged PIDs (safe - 'kill' only kills if the PID exists and is yours)
for pid in $(awk '{print $1}' ~/slr/ssrn/pid.txt); do
    kill -0 $pid 2>/dev/null && kill $pid && echo "killed $pid"
done
