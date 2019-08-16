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

`for i in 4 8 16 32 64 128 256 512 1024 2048 4096 8192 16382 32768; do ./cache $i; done >> cache-result.txt`

### 1Gのファイル作成についてのtips

`dd if=/dev/zero of=testfile bs=1M count=1k`

`oflag=dicet`は削除しないと動かない。

oflagオプションが付いていると下記エラーが発生。

`dd: failed to open 'testfile': Invalid argument`

なんかdocker使っているせいな気がするが、詳細不明。
なので、手動でキャッシュをクリアする。

`sudo bash -c "echo 1 > /proc/sys/vm/drop_caches"`

が、エラー

`bash: /proc/sys/vm/drop_caches: Read-only file system`

dockerの権限周りの問題らしい。ここは実験を諦めて、読むだけにした。

- 参考
    - https://stackoverflow.com/questions/21014080/dd-fail-to-write-to-tmpfs
    - https://qiita.com/toshihirock/items/e2d187e91ee5446c7a69
    - https://unix.stackexchange.com/questions/209244/which-linux-capability-do-i-need-in-order-to-write-to-proc-sys-vm-drop-caches