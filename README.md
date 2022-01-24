# mypkg:課題2
ROSのプログラミングの練習です。大きな変更点はありませんが実効速度が10㎐から5㎐になっています。また、一辺が[データ値]の立方体の体積&[生成されたデータ値]半径の円の面積を表示します。

## 実行環境

ハードウェア

・Panasonic CF-19


ソフトウェア

・Ubuntu 18.04

・ROS melodic

## 前提条件

・ROSがインストール済みであること

・catkinワークスペースのディレクトリを作成済みであること

## インストール＆実行手順

・catkin_ws/srcに移動しリポジトリgit@github.com:Sugar310-system/mypkg.gitをgit cloneする。

・~/catkin_wsでcatkin_makeをする。

・新しい端末でroscoreと入力しROSを起動しておく。

・新しい端末を開きそれぞれの端末でcd ~/mypkg/scriptsに移動しchmod +x count.py、chmod +x cube.py、chmod +x pi.pyとパーミッションを予め設定しておく。

・rosrun mypkg cube.pyとrosrun mypkg pi.pyを最初に実行しておき待機状態にしておく。

・新しい端末を開きrostopic echo /count_upで同じく待機状態にしておく。

・最後にrosrun mypkg count.pyを実行する

## 実行の様子


