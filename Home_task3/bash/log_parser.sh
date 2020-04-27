#!/bin/bash
echo
echo -n "Enter the path "
echo ""
read path
echo "The path is $path"
echo ""
while [ -n "$1" ]
do
case "$1" in
-a) wc -l $path > ./res/res-a.txt
  shift;;
-b) echo "Found the -b option" ;;
-c) echo "Found the -c option" ;;
*) echo "$1 is not an option" ;;
esac
echo "Done!"
echo ""
shift
done