#!/bin/bash
echo
echo -n "Enter the path "
echo ""
read path
echo "The path is $path"
echo ""
filetype="*.log"
while [ -n "$1" ]
do
case "$1" in

-a)
  if [ -f "$path" ]; then
      echo "$path" > ./res/res-a.txt
      cat "$path" | wc -l >> ./res/res-a.txt
  elif [ -d "$path" ]; then
      echo "$path/$filetype" > ./res/res-a.txt
      cat $path/$filetype | wc -l >> ./res/res-a.txt
  else
    echo "Error: $path is bad"
    echo ""
  fi
  shift;;


-b)
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
    echo "Error: $path is bad"
    echo ""
  fi
  shift;;


*) echo "$1 is not an option" ;;
esac
echo "Finished!"
echo ""
shift
done
