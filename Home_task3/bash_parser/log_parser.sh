#!/bin/bash
echo


filetype="*.log"

function read_the_path() {
  echo -n "Enter the path "
  echo
  # shellcheck disable=SC2162
  read path
}

function error_with_path() {
  echo "Error: $path is bad"
  echo ""
}


while [ -n "$1" ]
do
case "$1" in

  -a)
    read_the_path
    if [ -f "$path" ]; then
        echo "$path" > ./res/res-a.txt
        cat "$path" | wc -l >> ./res/res-a.txt
    elif [ -d "$path" ]; then
        echo "$path/$filetype" > ./res/res-a.txt
        cat $path/$filetype | wc -l >> ./res/res-a.txt
    else
      error_with_path
    fi
    shift;;

  -b)
    read_the_path
    request_methods=("GET" "HEAD" "POST" "PUT" "DELETE" "TRACE" "OPTIONS" "CONNECT" "PATCH")
    if [ -f "$path" ]; then
        echo "$path" > ./res/res-b.txt
        # shellcheck disable=SC2068
        for t in ${request_methods[@]}; do
          echo "$t"  >> ./res/res-b.txt
          # shellcheck disable=SC2126
          cat "$path" | grep "$t" | wc -l >> ./res/res-b.txt
        done
    elif [ -d "$path" ]; then
        echo "$path/$filetype" > ./res/res-b.txt
        # shellcheck disable=SC2068
        for t in ${request_methods[@]}; do
          echo "$t"  >> ./res/res-b.txt
          # shellcheck disable=SC2126
          cat $path/$filetype | grep "$t" | wc -l >> ./res/res-b.txt
        done
    else
      error_with_path
    fi
    shift;;

  -c)
    read_the_path
    if [ -f "$path" ]; then
        # shellcheck disable=SC1003
        echo "$path" > ./res/res-c.txt
        grep '\\' $path | awk '{print($7, $9, $10)}' | sort -r -k 3 -n | head -10 >> ./res/res-c.txt
    elif [ -d "$path" ]; then
        echo "$path/$filetype" > ./res/res-c.txt
        grep -r '\\' $path | awk '{print($7, $9, $10)}' | sort -r -k 3 -n | head -10 >> ./res/res-c.txt
    else
      error_with_path
    fi
    shift;;

  -d)
    read_the_path
    if [ -f "$path" ]; then
        echo "$path" > ./res/res-d.txt
        grep '\\' $path | awk '($9 ~ /[4][0-9][0-9]/)' | awk '{print $7, $9}' | sort | uniq -c | sort -rn |head -10 >> ./res/res-d.txt
    elif [ -d "$path" ]; then
        echo "$path/$filetype" > ./res/res-d.txt
        grep -r '\\' $path | awk '($9 ~ /[4][0-9][0-9]/)' | awk '{print $7, $9}' | sort | uniq -c | sort -rn |head -10 >> ./res/res-d.txt
    else
      error_with_path
    fi
    shift;;

  -e)
   read_the_path
    if [ -f "$path" ]; then
        echo "$path" > ./res/res-e.txt
        grep '\\' $path | awk '($9 ~ /[4][0-9][0-9]/)' | awk '{print $7, $9, $10}' | sort -r -k 3 -n | head -10 >> ./res/res-e.txt
    elif [ -d "$path" ]; then
        echo "$path/$filetype" > ./res/res-e.txt
        grep -r '\\' $path | awk '($9 ~ /[4][0-9][0-9]/)' | awk '{print $7, $9, $10}' | sort -r -k 3 -n | head -10 >> ./res/res-e.txt
    else
      error_with_path
    fi
    shift;;

  -h)
    echo
    echo "Nginx logs parser"
    echo
    echo "Keys:"
    echo "-a - Total number of requests"
    echo "-b - Number of queries by type"
    echo "-c - Top 10 Biggest Queries"
    echo "-d - Top 10 quantity requests that ended with a client error"
    echo "-e - Top 10 requests that ended with a client error by size"
    echo "-h - help"
    echo
    shift ;;

*) echo "$1 is not an option" ;;

esac
echo
echo
echo "Finished!"
echo
echo
shift
done
