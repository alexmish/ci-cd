#!/bin/bash
OS_VER=$(cat /etc/issue)
OS_ARCH=$(uname -m)
SCRIPT_PATH="/tmp/zip_job.py"



print_welcome() {

    echo "#############################################################"
    echo "Welcome you running ${OS_VER} ${OS_ARCH}" # do better message
    echo "#############################################################"

}

checkout_for_files() {

    [ -f "${SCRIPT_PATH}" ] && { echo "File ${SCRIPT_PATH} exists"; }

}

checking_java_installed() {

    java -version /dev/null 2&>1
    [ "$?" -ne "0" ] && { echo "Java NOT found exiting " ; exit 1 ; }

}


### printing message | checking for files and java | running SSH for jenkins commenication (user apss is set in docker file)
print_welcome
checkout_for_files || { echo "Error zip_job.py is missig " ; exit 1 ; }
checking_java_installed

exec /usr/sbin/sshd -D
exec "$@"

