# 中国高速铁路运营路线图 2026

基于 OpenSeadragon 的高清中国高铁线路图浏览器，支持无限缩放浏览。

## 在线浏览

直接打开 [public/index.html](public/index.html) 即可查看。

## 技术栈

- **OpenSeadragon 6.1.0** — 深度缩放 (Deep Zoom) 图片浏览器
- **DZI 切片** — Python + Pillow 生成，支持从缩略图到原图的多级加载

## 项目结构

```
├── 2601ZH442.png              # 原始高铁图 (19845x14032)
├── pyramidio.py               # DZI 切片生成工具
├── public/
│   ├── index.html               # 查看器页面
│   ├── favicon.svg
│   └── 2601ZH442/
│       ├── 2601ZH442.dzi          # Deep Zoom 描述文件
│       └── 2601ZH442_files/       # 多级切片 (16级, 5931张)
│           ├── 0/                   # 缩略图
│           │   ...
│           └── 15/                  # 原图切片
└── README.md
```

## 切片脚本用法

```
python pyramidio.py <input> [-o OUTPUT] [--tile-size 254] [--overlap 1] [--quality 85]
```

示例：

```bash
python pyramidio.py 2601ZH442.png -o public/2601ZH442
python pyramidio.py input.jpg -o output --tile-size 512 --quality 90
```

### 备用切片工具
pyramidio-cli-1.1.0.jar
https://github.com/usnistgov/pyramidio


## 更新地图

1. 将新图放入项目根目录
2. 运行 `python pyramidio.py <图片名>.png -o public/<图片名>`
3. 更新 `public/index.html` 中的路径和尺寸
4. 提交推送

## 图片信息

| 项目 | 值 |
|------|-----|
| 版本 | 2026年1月版 |
| 尺寸 | 19845 x 14032 像素 |
| 切片 | 16级, 5931张 JPG |
| tile大小 | 254x254, overlap 1px |
| 制作人 | 陶岸君，东南大学建筑学院副教授 |

## 更新日志

- **2026-08** — OpenSeadragon 升级至 6.1.0
- **2026-01** — 更新至2026版路线图, OpenSeadragon 升级至 6.0.2
- **2025-01** — 初始版本 (2501ZH442)
