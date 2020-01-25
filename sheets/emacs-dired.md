# Emacs Dired Cheat Sheet

- [Emacs Wiki - Dired Mode](https://www.emacswiki.org/emacs/DiredMode)

## Basic Commands

|   | Key Binding  |
|:--|:-------------|
| m | mark         |
| u | unmark       |
| v | view         |
| R | rename, move |
| C | copy         |
| D | delete       |

- `d` で削除フラグをつける、`u` で削除フラグを消すなどがあるが、`m` で mark してからやりたいことを指定するように統一したほうが分かりやすい。
- これだけ使えれば多分充分。圧縮とか symbolic link とかもできるけど、バッチ操作するようなことではないので、dired の操作を覚えるよりも shell でやったほうがコスパ良さそう。

## Customized Commands

<https://github.com/pn11/dotfiles/blob/master/.emacs> 参照。

|                | Key Binding                                                                                                            |
|:---------------|:-----------------------------------------------------------------------------------------------------------------------|
| p              | `dired-up-directory`： 上の directory へ (p は default だと上の行へ移動)                                               |
| n, o, C-o, C-j | `dired-find-file`: file を開く。 (n は default では下の行へ移動、o, C-o は file の表示)                                |
| SPC            | `dired-display-file)`: file の表示。Mac の Quick Look リスペクトで SPC に割り当てる。(SPC は default では下の行へ移動) |

## Example

### 複数ファイルを移動する

1. `m` で mark する
2. `R` (rename) で移動先を指定
