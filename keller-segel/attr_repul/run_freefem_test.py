#!/usr/bin/python3

# This program run FreeFem++ test and filter its result.
# Lines starting with characters "->" are assumed to be followed by yaml
# statements. This yaml data is processed and stored in a file.

from subprocess import Popen, PIPE, check_output
import sys
import re
import time
import yaml


freefem_interpreter = "FreeFem++"
freefem_test = "attractive_repulsive.edp"

def define_default_args():
    test_args = {
        "dt": 0.001,
        "nt": 50,
        "tau": 1,
        "nx": 40,
        "ChiAttraction": 1,
        "XiRepulsion": 1,
        "alpha": 1,
        "beta": 1,
        "gamma": 1,
        "delta": 1,
        "r": 1,
        "s": 1.7,
        "C0": 100,
        "C1": 50,
        "infU": 1,
        "errAdapt": 0.001
    }
    return test_args

def run_test(test_args):
    print(f"Running FreeFem++ test: {freefem_test}")

    # Load test specific arguments
    arg_list = []
    for key in test_args:
        arg_list.extend( (f"-{key}", str(test_args[key])) )
    arg_string = " ".join(arg_list)
    print(f"With arguments: {arg_string}")

    # Run test
    command = [freefem_interpreter, '-nw', '-ne', freefem_test]

    output_yaml_file = time.strftime("%Y%m%d-%H%M%S.yaml")
    print(f"Saving to file {output_yaml_file}")
    command.extend(['-outf', output_yaml_file])

    command.extend(arg_list)
    ps_freefem = Popen(command)

    # ps_freefem = Popen(command, stdout=PIPE, stderr=PIPE)

    # # Filter results using grep (via a pipe), looking for lines with string '->'
    # grep_command = "grep -e ->".split(' ')
    # ps_grep = Popen(grep_command, stdin=ps_freefem.stdout,
    #                 stdout=PIPE, stderr=PIPE)

    # # Filter again, using cut, to obtain second column
    # cut_command = "cut -d > -f 2".split(' ')
    # output = check_output(cut_command, stdin=ps_grep.stdout, stderr=PIPE)
    # output = output.decode(sys.stdout.encoding)
    # print(output)

    # Read data as yaml
    # yaml_dict = yaml.load(output)
    # k = 'Test data'
    # data_string = yaml.dump({k: yaml_dict[k]} , default_flow_style=False)
    # k = 'Test iterations'
    # iterations_string = yaml.dump({k: yaml_dict[k]} , default_flow_style=False)
    # k = 'Test summary'
    # summary_string = yaml.dump({k: yaml_dict[k]} , default_flow_style=False)
    # with open(output_yaml_file, 'w') as f:
    #     f.write("---\n")
    #     f.write(output)
        # f.write(data_string)
        # f.write(summary_string)
        # f.write(iterations_string)

    # with open(output_yaml_file, 'w') as f:
    #     f.write("---\n")
    #     f.write(output)

if __name__ == '__main__':
    test_args = define_default_args()
    run_test(test_args)
