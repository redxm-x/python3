import subprocess
import time


class Terminal:
    def __init__(self):
        super(Terminal, self).__init__()
        self.output = []  # can be omitted, logger can be used as substitute

    def _execute(self, cmd, shell=True, exec_as_root=False):
        cmd = f'sudo su -c "{cmd}"' if exec_as_root is True else cmd
        process = subprocess.Popen(cmd, shell=shell,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)

        out, err = process.communicate()
        out = out.decode()
        err = err.decode()
        level = 'ERROR' if err else 'DEBUG'
        mess = f'[{time.ctime(time.time())} {level}] Command: {cmd}, exited with: {err}, output: {out}'
        print(mess)
        self.output.append(mess)

        return [out, err]

    def example_usage_of_execute(self, arg):
        out, err = self._execute(f'mkdir {arg}')
        if not err:
            return out
