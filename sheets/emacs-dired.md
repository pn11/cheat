# Emacs Dired Cheat Sheet

- [Emacs Wiki - Dired Mode](https://www.emacswiki.org/emacs/DiredMode)

## Basic Commands

| Key Binding  |   |
|:--|:--|
| m | mark         |
| u | unmark       |
| v | view         |
| R | rename, move |
| D | delete       |

- `d` で削除フラグをつける、`u` で削除フラグを消すなどがあるが、`m` で mark してからやりたいことを指定するように統一したほうが分かりやすい。
- これだけ使えれば多分充分。圧縮とか symbolic link とかもできるけど、バッチ操作するようなことではないので、dired の操作を覚えるよりも shell でやったほうがコスパ良さそう。

## Example

### 複数ファイルを移動する

1. `m` で mark する
2. `R` (rename) で移動先を指定
