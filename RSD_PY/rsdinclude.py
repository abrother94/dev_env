MP="/home/nick_huang/Intel_RSD_Test/ORG_B/2.1.3/rsd/PSME"
pinclude=[]
pinclude.append("-isystem")
pinclude.append(MP+"/common/agent-framework/include")
pinclude.append("-isystem")
pinclude.append(MP+"/agent/chassis/include")
pinclude.append("-isystem")
pinclude.append(MP+"/common/configuration/include")

def get_rsd_include():
    return  pinclude
