#!/bin/bash

echo "Generating flags"
echo "============================";

echo "How long should the flag be?"
read -p "> " LEN

echo "Flags per user?"
read -p "> " COUNT

echo "Filename?"
read -p "> " FILE

if [ "$FILE" = "$(basename "$0")" ]
then
	echo "Lol nice try"
	exit
fi

for USER in `ls /home/`; do

	echo "============================" >> $FILE;
	echo "Flags for $USER ..." >> $FILE

	for i in $(seq 1 $COUNT); do
		CONTENT=`head -c 20 /dev/urandom | sha256sum | cut -d' ' -f1 | head -c $LEN`;

		echo "$i. flag{${CONTENT}}" >> $FILE;
	done;
done
