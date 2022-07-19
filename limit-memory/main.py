import subprocess
import resource

MAX_VIRTUAL_MEMORY = 10 * 1024 * 1024 # 10 MB 
  
def limit_virtual_memory():
    # The tuple below is of the form (soft limit, hard limit). Limit only
    # the soft part so that the limit can be increased later (setting also
    # the hard limit would prevent that).
    # When the limit cannot be changed, setrlimit() raises ValueError.
    resource.setrlimit(resource.RLIMIT_AS, (MAX_VIRTUAL_MEMORY, resource.RLIM_INFINITY))

p = subprocess.Popen(
    ['python3', '--version'],
    # preexec_fn is a callable object that will be called in the child process
    # just before the child is executed.
    preexec_fn=limit_virtual_memory,
    stdout=subprocess.PIPE
)
stdout, stderr = p.communicate()
print("stdout", stdout)
print("stderr", stderr)

# source) limit-virtual-memory-of-subprocess.py, https://gist.github.com/welcomehyunseo/be1c7136fcad15a0612927a1eb6643c4