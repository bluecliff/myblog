Title: ubuntu12.04 64位系统安装校园网客户端inodeClient
Date: 2013-01-12 10:20
Tags: ubuntu12.04, inodeClient,linux应用, 校园网
Slug: inodeClient_install
Author: lijsf
Summary: linux安装inode的过程记录 

# 主要步骤

	
 (1).  下载安装包,解压到相应目录。
 
 (2).  64位系统，需要先安装32位的运行库：
 
	:::bash 
	apt-get install ia32-libs* getlibs
 
 若源中找不到getlibs库，可去http://forum.ubuntu.org.cn/viewtopic.php?t=205525下载deb包安装。
 
 (3).  进入inodeClient目录，修改iNodeCLient根目录下的enablecards.ps。将其中第二行cd /etc/sysconfig/network-scripts
 修改为cd /etc/network,再运行install.sh。注意install.sh的权限。
 
 (4).  安装后可通过 
 
	:::bash
	ps -e|grep A 
	
命令查看是否安装成功，结果类似于：1694 ?        00:00:00 AuthenMngServic
表示安装成功。若无该服务进程，则安装不成功。
 
 (5). 安装后， 若运行不成功，多会提示缺少libtiff.so.3和libjpeg.so.62两个库文件，32位的系统可以直接通过下面的命令建立软链接：
 
	:::bash
	ln -s /usr/lib/libtiff.so.3 /usr/lib/i386-linux-gnu/libtiff.so.4.x.	x
	
libjpeg.so.62也可类似处理。若找不到对应的较新的库的位置，可用命令locate libtiff.so查找其位置。
 
 (6).  对64位系统，在处理litfiff或者libjpeg库时可能建立软链接后因为库inode不识别64位的libtiff和libjpeg而不能运行。可以去
 微盘下载这两个文件，放到/usr/lib目录下即可。
