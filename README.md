# 概要
- linuxの仕組み(2018 武内覚 技術評論社)の写経
- vscodeでのgitの操作方法確認
- vscode remote containerの練習

## chapter4

### 大体のコマンド

`taskset -c 0,3 ./shced 2 100 1`
`taskset -c 0 ./shced 1 10000 10000`
`time taskset -c 0 ./shced 1 10000 10000`

`time taskset -c 0 ./shvced_nice 2 10 1`

###　グラフ作成用

`python plot.py --filename ファイル名`