
############### 第一种方法 ####################
1. The three folds are needed.
1.1. prebuildbase_win10_x64_vc14.7z
1.2. 20170911_mxnet_x64_vc14_cpu.7z
1.3. cudnn-8.0-windows10-x64-v6.0.zip

2. unpack the first to MXNet, then unpack the second to MXNet
(rewrite the folder if there are folders with the same name),
## no need of the 1.3.then unpack cudnn-8.0-windows10-x64-v6.0.zip, copy files to \MXNet\3rdparty\cudnn;

3. move all of the .dll files to \MXNet\build, (totally 13 .dll files), 
and add the \MXNet\build to the path of the computer;

4. go into cmd environment, as the Administrator, then active the gluon environment(if 
there is no an environment conda create --name gluon python=3.6), keep the cmd alive;

5. close down the virus defense, right click setupenv.cmd (which is in D:\pylibpack\MXNet), 
run with the Administrator;

6. in cmd environment, go into the folder which contains 'setup.py' file, by cd D:\pylibpack\MXNet\python

7. still in cmd environment, by python setup.py install, then check, type ipython, then import mxnet as mx;

8. finish!

####### 另一种安装mxnet的方式 #222222222222222#### 推荐用这一种方法 ####

1. cmd run as the Administrator, then we are in the cmd environment;
2.
conda info

d：

cd jupyter\gluon-tutorials-zh\

dir

(之前已经修改过environment.yml 并提前下载.whl文件, mxnet 0.11.1b20170925 下载地址
https://pypi.python.org/pypi/mxnet/0.11.1b20170925
)

conda env create -f environment.yml
(if we have already create the gluon environment, returns the errors:
CondaValueError: prefix already exists: C:\ProgramData\Miniconda3\envs\gluon
如果此环境gluon已经存在，删掉重新来，不然报错。。。很无语！！
)

conda info -e

activate gluon

ipython

import mxnet as mx


############################################
PS:
1. 下载地址
mxnet 0.11.1b20170924 
https://pypi.python.org/pypi/mxnet/0.11.1b20170924


2. 本地文件whl安装，只能用pip
pip install mxnet-0.11.1b20170924-py2.py3-none-win_amd64.whl

{
conda install mxnet-0.11.1b20170924-py2.py3-none-win_amd64.whl (不成功)
conda install mxnet-0.11.1b20170924-py2.py3-none-win_amd64.whl
Fetching package metadata .............

PackageNotFoundError: Packages missing in current channels:

  - mxnet-0.11.1b20170924-py2.py3-none-win_amd64.whl

We have searched for the packages in the following channels:

  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/win-64
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/noarch
  - https://repo.continuum.io/pkgs/free/win-64
  - https://repo.continuum.io/pkgs/free/noarch
  - https://repo.continuum.io/pkgs/r/win-64
  - https://repo.continuum.io/pkgs/r/noarch
  - https://repo.continuum.io/pkgs/pro/win-64
  - https://repo.continuum.io/pkgs/pro/noarch
  - https://repo.continuum.io/pkgs/msys2/win-64
  - https://repo.continuum.io/pkgs/msys2/noarch

}



############ 第一种方法 #111111111111111111###
1.2 下载地址，每日更新的
https://github.com/yajiedesign/mxnet/releases



########### 第一种方法 #111111 new version ###############

1. The three folds are needed.
1.1. prebuildbase_win10_x64_vc14_v2.7z
1.2. 20170925_mxnet_x64_vc14_cpu.7z


2. unpack the first to MXNet, then unpack the second to MXNet
(rewrite the folder if there are folders with the same name),

3. add to the path of the computer;
D:\pylibpack\MXNet\3rdparty\bin
D:\pylibpack\MXNet\build

4. go into cmd environment, as the Administrator, then active the gluon environment(if 
there is no an environment conda create --name gluon python=3.6), keep the cmd alive;

5. close down the virus defense, right click setupenv.cmd (which is in D:\pylibpack\MXNet), 
run with the Administrator;


6. in cmd environment, go into the folder which contains 'setup.py' file, 
(goal is cd D:\pylibpack\MXNet\python)
step by step is
d:
cd pylibpack
.....


7. still in cmd environment, by python setup.py install, then check, type ipython, then import mxnet as mx;

8. finish!

################
