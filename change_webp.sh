#!/bin/bash

# すべての jpg ファイルを検索して、それらを webp に変換する
fd -e jpg -x bash -c 'cwebp -quiet -mt -af "$0" -o "${0%.*}.webp"' {} \;