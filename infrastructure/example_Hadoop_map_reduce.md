#                                                ASSIGNMENT 3 -   MAP REDUCE WITH HADOOP 

## 1. Setup the VBox Instance :


### Download and install VirtualBox from - https://www.virtualbox.org/


### Set up a new virtualbox instance with the below configuration:

* Name: Linux Ubuntu 64 bit 
* 3 GB RAM 
* VDI disk -Dynamically allocated 

![UbuntuVM](https://github.com/vu-bigdata-2020/example-notebooks/blob/master/infrastructure/VM-installation.png)

## 2. Installation of Ubuntu Linux on VirtualBox VM and other prereqs for Hadoop:

### Download an image for Ubuntu Linux OS 18.4 LTS from -
https://ubuntu.com/download/desktop

* Point to the Ubuntu OS image you downloaded and install Ubuntu on the VM 


### Install Java 8 on Ubuntu Linux. This is a prerequisite for Hadoop.

$ sudo apt-get install openjdk-8-jre


### Install OpenSSH server

$ sudo apt-get install openssh-server 


## 3. Standalone version install of hadoop 

### Set the below env variable

JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/

### update the sudo /etc/profile with below lines

JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/
PATH=$PATH:$HOME/bin:$JAVA_HOME/bin
export JAVA_HOME
export JRE_HOME
export PATH

### Also open file /etc/hadoop in hadoop install folder and update file at its end -
JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/


### Create a passwordless ssh

* generates the key

$ ssh-keygen

* copy it

$ ssh-copy-id -i /home/<uname>/.ssh/id_rsa.pub <uname>@localhost

* Check if you can ssh localhost without password 

$ ssh localhost


## 4. Download and unzip the hadoop

### Download Hadoop from http://www.apache.org/dyn/closer.cgi/hadoop/common/

### In the unpacked Hadoop directory ,open hadoop-env.sh

$vim etc/hadoop/hadoop-env.sh

### Update the JAVA_HOME to your java home directory

JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/


### In your bash profile, update the environment variables 

export HADOOP_HOME=<Your hadoop home directory path>
export PATH=$PATH:$HADOOP_HOME/bin


## 5. Running Map Reduce programs on Standalone Hadoop

### The hadoop streaming library is located in below path from the hadoop installation folder

$HADOOP_INSTALLATION_FOLDER/share/hadoop/tools/lib/hadoop-streaming-2.10.0.jar

### cmd to run map reduce on local machine with Hadoop streaming -

cd $HADOOP_HOME

./bin/hadoop jar ./share/hadoop/tools/lib/hadoop-streaming-2.10.0.jar  -input <input-data-file> -output <output-data-path> -mapper <mapper.py> -reducer <reducer.py>
  
## Example Map Reduce program for Word count

### Download the movielens ml-100k.zip dataset from https://grouplens.org/datasets/movielens/100k/ and unzip in $HADOOP_HOME 

cd $HADOOP_HOME

$ wget http://files.grouplens.org/datasets/movielens/ml-100k.zip

$ unzip  ml-100k.zip

./bin/hadoop jar ./share/hadoop/tools/lib/hadoop-streaming-2.10.0.jar  -input ./ml-100k/u.item -output myoutput -mapper /home/nithin/hadoop-2.10.0/mapper.py -reducer /home/nithin/hadoop-2.10.0/reducer.py


## Example Map Reduce program to run using python MRJob lib

### install the mrjob python library

pip install mrjob

### run the Map reduce using mrjob python library

python WordCount.py ./ml-100k/u.item


## 6. Assignment

TBD





  
  






