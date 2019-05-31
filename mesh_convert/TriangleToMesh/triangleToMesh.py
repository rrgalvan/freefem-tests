#!/usr/bin/python3

from sys import argv, exit
verbosity = 1

if(len (argv) <2):
    print(f"""
    Usage: {argv[0]} <base name of Triangle .node, .ele, .edge files>
    """);

base_name = argv[1]

# 1. Read .node file
try:
    node_file_name = base_name+".node"
    node_file = open(node_file_name, 'r')
    line = node_file.readline()
    n_nodes = line.split()[0]
    n_nodes = int(n_nodes)
    xy = {}
    for i in range(n_nodes):
        line = node_file.readline()
        index = int(line.split()[0])
        xy[index] = line.split()[1:3]
    if verbosity:
        print("n_nodes:", n_nodes)
        for i in xy.keys():
            print (f"  {i}:", xy[i])
except IOError:
    print ("Could not read file:", node_file_name)
    exit()

# 2. Read .ele file
try:
    ele_file_name = base_name+".ele"
    ele_file = open(ele_file_name, 'r')
    line = ele_file.readline()
    n_ele = int(line.split()[0])
    ijk = {} # Index of three vertices
    for i in range(n_ele):
        line = ele_file.readline()
        index = int(line.split()[0])
        ijk[index] = line.split()[1:4]
    if verbosity:
        print("n_ele:", n_ele)
        for i in ijk.keys():
            print (f"  {i}:", ijk[i])
except IOError:
    print ("Could not read file:", ele_file_name)
    exit()

# 3. Read .edge file
try:
    edge_file_name = base_name+".edge"
    edge_file = open(edge_file_name, 'r')
    line = edge_file.readline()
    n_edge = line.split()[0]
    n_edge = int(n_edge)
    ijb = {} # index_of_vertex1, index_of_vertex2, boundary_marker
    for i in range(n_edge):
        line = edge_file.readline()
        index = int(line.split()[0])
        ijb[index] = line.split()[1:4]
    if verbosity:
        print("n_ele:", n_edge)
        for i in ijb.keys():
            print (f"  {i}:", ijb[i])
except IOError:
    print ("Could not read file:", edge_file_name)
    exit()

# 4. Write FreeFem++ .msh file
boundary_label = 1 # See FreeFem++ manual, table 5.1
region_label = 0 # See FreeFem++ manual, table 5.1
try:
    msh_file_name = base_name+".msh"
    msh_file = open(msh_file_name, 'w')
    msh_file.write(f"{n_nodes} {n_ele} {n_edge}\n\n")
    for i in xy.keys():
        msh_file.write(f"{xy[i][0]}  {xy[i][1]} \t {boundary_label}\n")
    msh_file.write("\n")
    for i in ijk.keys():
        msh_file.write(f"{ijk[i][0]}  {ijk[i][1]}  {ijk[i][2]}\t {region_label}\n")
    msh_file.write("\n")
    for i in ijb.keys():
        msh_file.write(f"{ijb[i][0]}  {ijb[i][1]}  \t {ijb[i][2]}\n")
except IOError:
    print ("Could not open file for writting:", msh_file_name)
    exit()
