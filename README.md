# 概要
- linuxの仕組み(2018 武内覚 技術評論社)の写経
- vscodeでのgitの操作方法確認
- vscode remote containerの練習

## chapter4

### 大体のコマンド

`cc -o sched sched.c`

`taskset -c 0,3 ./shced 2 100 1`

`taskset -c 0 ./shced 1 10000 10000`

`time taskset -c 0 ./shced 1 10000 10000`

`time taskset -c 0 ./shvced_nice 2 10 1`

### グラフ作成用

`python plot.py --filename ファイル名`

## chapter5

### スワップ領域の確認

`swapon --show`

### スワップの監視

`sar -W 1`


### スワッシングの監視

`sar -S 1`

## chapter6

### cache.cの実験

`for i in 4 8 16 32 64 128 256 512 1024 2048 4096 8192 16382 32768; do ./cache $i; done`
