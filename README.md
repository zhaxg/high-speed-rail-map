# 中国高速铁路运营路线图 2026

基于 OpenSeadragon 的高清中国高铁线路图浏览器，支持无限缩放浏览。

![高铁图预览](2601ZH442.png)

## 在线浏览

直接打开 [public/index.html](public/index.html) 即可查看。

## 技术栈

- **OpenSeadragon 6.0.2** — 深度缩放 (Deep Zoom) 图片浏览器
- **DZI 切片** — Python + Pillow 生成，支持从缩略图到原图的多级加载

## 项目结构

`
├── 2601ZH442.png          # 原始高铁图 (19845×14032)
├── public/
│   ├── index.html         # 查看器页面
│   ├── favicon.svg
│   └── 2601ZH442/
│       ├── 2601ZH442.dzi  # Deep Zoom 描述文件
│       └── 2601ZH442_files/  # 多级切片 (16级, 5931张)
│           ├── 0/         # 缩略图
│           ├── ...
│           └── 15/        # 原图切片
└── README.md
`

## 更新地图

1. 将新图放入项目根目录，命名为 YYYYMMDDHH.png
2. 运行 Python 脚本生成 DZI 切片：

`python
from PIL import Image
import os, math

Image.MAX_IMAGE_PIXELS = None
img = Image.open('YYYYMMDDHH.png')
w, h = img.size
tile_size, overlap = 254, 1

# 生成 DZI + 切片 ...
`

3. 更新 public/index.html 中的路径和尺寸
4. 更新 README.md 标题和预览图
5. 提交推送

## 图片信息

| 项目 | 值 |
|------|-----|
| 版本 | 2026年1月版 (2601ZH442) |
| 尺寸 | 19845 × 14032 像素 |
| 切片 | 16级, 5931张 JPG |
| tile大小 | 254×254, overlap 1px |
| 来源 | tie 中国高铁运营路线图 |

## 更新日志

- **2026-01** — 更新至2026版路线图, OpenSeadragon 升级至 6.0.2
- **2025-01** — 初始版本 (2501ZH442)

## 许可

图片来源: [tie中国高速铁路运营路线图](https://tie.jpg) © 2026