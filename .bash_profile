# .bash_profile

# Get the aliases and functions

if [ -f /etc/bashrc ]; then
		     . /etc/bashrc
fi

PATH=$PATH:$HOME/bin:./:/bin/:/usr/bin:/sbin:/usr/local/CodeSourcery/Sourcery_G++_Lite:/usr/local/CodeSourcery/Sourcery_G++_Lite/bin:/opt/Ikanos-toolchain/staging_dir/usr/bin:/opt/accton-build-tools/mips_be:/home/nick_huang/WeChat/RT8198C-2.3-Trunk-Merge/MERGE_RT8198C_HG6006-AG/LAST_BUILD/trunk/staging_dir/toolchain-mips_24kec_gcc-4.8-linaro_uClibc-0.9.33.2/bin:/home/nick_huang/WeChat/sdk/rtl819x-SDK-v3.4.7.1-full-package/rtl819x/toolchain/msdk-4.4.7-mips-EB-3.10-0.9.33-m32t-131227b/bin:/home/nick_huang/WR8006A/trunk/platform/Freescale/Toolchain/freescale/usr/local/gcc-4.3.74-eglibc-2.8.74-dp-2/powerpc-none-linux-gnuspe/bin


#PATH=$PATH:$HOME/bin:./:/usr/bin:/sbin:/usr/local/CodeSourcery/Sourcery_G++_Lite:/usr/local/CodeSourcery/Sourcery_G++_Lite/bin:/opt/Ikanos-toolchain/staging_dir/usr/bin:/opt/accton-build-tools/mips_be:/opt/accton-build-tools/arm_be/bin:/opt/accton-build-tools/EAP1028NB-FLF-APL-toolchain/cross_compile/gcc-linaro-arm-linux-gnueabihf-4.7-2013.04-20130415_linux/bin/

#LD_LIBRARY_PATH=$LD_LIBRARY_PATH

#STAGING_DIR=/home/nick_huang/WeChat/RT8198C-2.3-Trunk-Merge/MERGE_RT8198C_HG6006-AG/trunk/staging_dir
#export STAGING_DIR 
#export PATH
#export LD_LIBRARY_PATH 
unset USERNAME

BACKUP_LIST="work_menu.sh .vim  .*.sh .vimrc .bash_profile linux_tools"

alias sr='find -type f -print0 | xargs -r0 grep -F '
alias s='find -maxdepth 1 -type f | xargs grep -F '
alias dir='ls -alF'
alias f='find ./ -name '
alias update=' ctags -R --fields=+iaS  --extra=+q * --c++-kinds=+pf  cscope -Rbqk'
alias pd='pushd ./'
alias opd='popd'
alias CO='chown -R abrother:abrother'
alias BE='tar -vcf env.tar $BACKUP_LIST'
alias SYNC='rsync -av -e ssh $name@$ip:srcdirfile/ ./'

# User specific environment and startup programs
export PATH
