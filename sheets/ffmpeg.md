# ffmpeg

デモ動画とか圧縮率10くらいで他人に送ってる。

```sh
ffmpeg -i example_original.mp4 -crf 10 example_compressed.mp4
```

Faster option for Mac:

```sh
ffmpeg -i example_original.mp4 -c:v h264_videotoolbox -crf 10 example_compressed.mp4
```

## Reference

- [FFmpegの動画圧縮・変換コマンドの使い方 – Mankind Inc. https://mankindinc.jp/2018/03/14/ffmpeg%E3%81%AE%E5%8B%95%E7%94%BB%E5%9C%A7%E7%B8%AE%E3%83%BB%E5%A4%89%E6%8F%9B%E3%82%B3%E3%83%9E%E3%83%B3%E3%83%89%E3%81%AE%E4%BD%BF%E3%81%84%E6%96%B9/]
- [ffmpeg で動画を変換して 1TB 節約した話 - azukipochette's weblog https://azukipochette.hatenablog.com/entry/2020/02/24/051410]
