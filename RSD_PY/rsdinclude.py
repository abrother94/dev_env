
pinclude=[]
pinclude.append("/home/nick_huang/Intel_RSD/intelRSD-master-2.1.3/PSME/common/agent-framework/include")
pinclude.append("/home/nick_huang/Intel_RSD/intelRSD-master-2.1.3/PSME/agent/chassis/include")
pinclude.append("/home/nick_huang/Intel_RSD/intelRSD-master-2.1.3/PSME/common/configuration/include")
pinclude.append("/home/nick_huang/Intel_RSD/intelRSD-master-2.1.3/PSME/lui/OS/rootfs/opt/intel/rackscale/include")
pinclude.append("/home/nick_huang/Intel_RSD/intelRSD-master-2.1.3/PSME/agent/storage/include")
pinclude.append("/home/nick_huang/Intel_RSD/intelRSD-master-2.1.3/PSME/agent/pnc/include")
pinclude.append("/home/nick_huang/Intel_RSD/intelRSD-master-2.1.3/PSME/agent/network/include")
pinclude.append("/home/nick_huang/Intel_RSD/intelRSD-master-2.1.3/PSME/agent/compute/include")
pinclude.append("/home/nick_huang/Intel_RSD/intelRSD-master-2.1.3/PSME/common/ssdp/include")
pinclude.append("/home/nick_huang/Intel_RSD/intelRSD-master-2.1.3/PSME/common/md5/include")
pinclude.append("/home/nick_huang/Intel_RSD/intelRSD-master-2.1.3/PSME/common/base64/include")
pinclude.append("/home/nick_huang/Intel_RSD/intelRSD-master-2.1.3/PSME/common/net/include")
pinclude.append("/home/nick_huang/Intel_RSD/intelRSD-master-2.1.3/PSME/common/fru_eeprom/include")
pinclude.append("/home/nick_huang/Intel_RSD/intelRSD-master-2.1.3/PSME/common/include")
pinclude.append("/home/nick_huang/Intel_RSD/intelRSD-master-2.1.3/PSME/common/netlink/include")
pinclude.append("/home/nick_huang/Intel_RSD/intelRSD-master-2.1.3/PSME/common/json-cxx/include")
pinclude.append("/home/nick_huang/Intel_RSD/intelRSD-master-2.1.3/PSME/common/agent-framework/include")
pinclude.append("/home/nick_huang/Intel_RSD/intelRSD-master-2.1.3/PSME/common/logger/include")
pinclude.append("/home/nick_huang/Intel_RSD/intelRSD-master-2.1.3/PSME/application/include")

def get_rsd_include():
    return  "-isystem," + pinclude[0]

def get_rsd_include1():
    return  pinclude[1]

def get_rsd_include2():
    return  pinclude[2]

