# mypkg:課題2

## 1.概要
ROSのプログラミングの練習です。大きな変更点はありませんが実効速度が10㎐から5㎐になっています。また、一辺が[データ値]の立方体の体積&[生成されたデータ値]半径の円の面積を表示します。

## 2.実行環境

ハードウェア

・Panasonic CF-19


ソフトウェア

・Ubuntu 18.04

・ROS melodic

## 3.前提条件

・ROSがインストール済みであること

・catkinワークスペースのディレクトリを作成済みであること

## 4.インストール＆実行手順

・`catkin_ws/src`に移動しリポジトリgit@github.com:Sugar310-system/mypkg.gitをgit cloneする。

・`~/catkin_ws`で`catkin_make`をする。

・新しい端末で`roscore`と入力しROSを起動しておく。

・新しい端末を開きそれぞれの端末で`cd ~/mypkg/scripts`に移動し`chmod +x count.py`、`chmod +x cube.py`、`chmod +x pi.py`とパーミッションを予め設定しておく。

・`rosrun mypkg cube.py`と`rosrun mypkg pi.py`を最初に実行しておき待機状態にしておく。

・新しい端末を開き`rostopic echo /count_up`で同じく待機状態にしておく。

・最後に`rosrun mypkg count.py`を実行する

## 5.実行の様子

## 6.ライセンス
BSD 3-Clause "New" or "Revised" License
