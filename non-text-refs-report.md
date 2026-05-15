# 非文本引用扫描报告

## 扫描范围

- 中文翻译: `/home/kita/code/open-music-theory-zh/src/` (143个 .md 文件)
- 英文原文: `/home/kita/code/knowledge/music/open-music-theory/` (142个 .md 文件)

---

## 1. 图片引用

### 中文翻译 (src/)
- **本地图片文件**: 95 个 (位于 `src/Graphics/app/uploads/sites/12/` 下)
- **Markdown 图片引用**: 97 处 (97个 `![]()` 标记)
- **引用模式**: 统一使用 `[![中文alt文本](../Graphics/...)](https://viva.pressbooks.pub/...)` 格式
  - 即：Markdown中显示本地图片，但**点击后跳转到Pressbooks远程URL**
- **涉及的章节**: fundamentals (最多, ~50+张), counterpoint, chromaticism, 20th-century-techniques, ear-training, form, orchestration, twelve-tone-music

### 英文原文 (knowledge/)
- **本地图片**: 无 (所有图片都是远程引用)
- **Markdown 图片引用**: 97 处
- **引用模式**: 统一使用 `![alt文本](https://viva.pressbooks.pub/...)` 格式（直接远程引用）
- 与中文版相比：**图片总数一致(97)**，但英文原文有少数几张图片没有alt文本

### 对比结论
| 项目 | 中文翻译 | 英文原文 |
|------|---------|---------|
| 图片引用总数 | 97 | 97 |
| 本地缓存图片 | 95 (完整) | 0 |
| 远程图片引用 | 97 (点击跳转) | 97 (直接显示) |

**差异**: 英文原文所有图片引用都是原始Pressbooks URL；中文版下载了95个本地副本（在Graphics/目录），但Markdown中仍通过点击跳转链接指向Pressbooks。少数图片的alt文本长度有差异（中文版有些截断了）。

---

## 2. 音频文件 (.mp3)

### 中文翻译
- **本地点播音频引用**: 3个有效MP3链接
  - `ear-training/01-basics-sight-singing-dictation.md` - 2个MP3
  - `form/08-sonata-form.md` - 1个MP3（莫扎特奏鸣曲）
- **文本中提及.mp3**: 3处（在fundamentals/19-roman-numerals.md的作业描述中提及，无实际链接）

### 英文原文
- **完全一致**: 3个有效MP3链接，与中文版完全对应
- **文本中提及.mp3**: 3处，相同

---

## 3. 视频引用 (YouTube/Vimeo)

### 中文翻译
- **YouTube**: 3处
  - `form/04-expansion-and-contraction.md` - 2个YouTube链接
  - `popular-music/10-four-chord-schemas.md` - 1个YouTube频道链接
- **Vimeo**: 1处
  - `popular-music/06-verse-chorus-form.md` - SMT-V视频

### 英文原文
- **完全一致**: 4处，与中文版完全对应

---

## 4. 交互式练习 & 网络应用

### 中文翻译
- **提及的外部Web应用** (在作业描述中):
  - `splitter.fm` — 音频分离工具
  - `Auralayer` — 织体可视化工具
  - `BriFormer` — 曲式图工具
  - `Tonnetz Master` — 音调网络工具
- **MuseScore文件 (.mscz/.mscx/.mxl)**: ~100次提及（作业附件格式）
- **MuseScore.com**: 多处提及

### 英文原文
- **完全一致**: 所有Web应用和MuseScore引用都与中文版对应

---

## 5. PDF文件引用

### 中文翻译
- 约200+次提及 `.pdf` 作为作业附件格式
- 所有PDF都是远程资源（无本地缓存）

### 英文原文
- 约287次提及 `.pdf` — 比中文版多约87次
- **差异原因**: 英文原文的作业描述更详细，列出了更多PDF变体

---

## 6. Spotify链接

### 中文翻译
- 约15+个 Spotify 链接（作为音乐示例时间戳）

### 英文原文
- 完全一致

---

## 7. 外部链接 (除上述之外)

### 中文翻译
- **Grove Music Online (DOI links)**: 大量学术引用 (~40+)
- **mtosmt.org**: 约5处
- **Pressbooks原文链接**: 每章末尾的"原文: [...] | CC BY-SA"链接 (~60+)
- **IMSLP**: 1处
- **MuseScore.com**: 2处
- **其他DOI/URL**: 约20处学术引用

### 英文原文
- 完全一致

---

## 8. iframe / HTML嵌入

### 中文翻译
- **iframe标签**: 0处

### 英文原文
- **iframe标签**: 0处

### 注意:
英文原文仓库来自Pressbooks的原始导出，Pressbooks通常使用短代码（shortcodes）而非直接iframe来嵌入内容。这些短代码在导出为Markdown时可能被剥离或未转换。常见Pressbooks嵌入式功能包括:
- H5P交互式练习
- 嵌入式MuseScore播放器
- Hypothes.is批注
- Pressbooks内部的术语表弹窗 (`[pb_glossary]`)

**检测到的残留**: 两仓库中各有一处 `[pb_glossary id=` 短代码残留在图片alt文本中（chromaticism/12-neo-riemannian-progressions.md），说明Pressbooks的术语表短代码未完全转换。

---

## 9. 远程资源URL汇总 (去重)

### 按类型统计

| 类型 | 数量 |
|------|------|
| 图片 (viva.pressbooks.pub) | ~97个唯一URL |
| 音频MP3 (viva.pressbooks.pub) | 3个 |
| YouTube | 3个 |
| Vimeo | 1个 |
| Spotify | ~15个 |
| DOI/Grove Music Online | ~40+个 |
| mtosmt.org | ~10个 |
| 其他学术引用 | ~20个 |
| Musescore.com | ~5个 |
| IMSLP | 1个 |

---

## 10. 主要发现

### 10.1 图片引用差异
中文翻译将所有图片的Markdown语法从英文原文的 `![](远程URL)` 改成了 `[![alt](../Graphics/本地路径)](远程URL)` 格式。好处是本地有缓存，坏处是用户在阅读时看到的是本地图片，但点击后会跳转到Pressbooks原站。

### 10.2 缺失的元素类型
中文翻译和英文原文仓库**都没有**以下Pressbooks原站可能有的元素:
- **H5P交互式练习** — Pressbooks原生支持，但导出为Markdown时丢失
- **嵌入式MuseScore播放器** — 原文 `front-matter/00-introduction.md` 提到"带有嵌入式MuseScore播放器的谱例"，但仓库中无对应HTML/iframe
- **Hypothes.is批注层** — Pressbooks集成
- **Pressbooks术语表弹窗** — `[pb_glossary]` 短代码未转换，只残留一处
- **交互式练习播放列表** — 多处提到"练习播放列表"但URL不可点击，可能是Pressbooks内建功能
- **MathJax/LaTeX公式** — 仓库中有少量LaTeX（如 `$(\\hat3)$`），但Pressbooks原站可能使用MathJax渲染

### 10.3 格式转换损耗
从Pressbooks导出为Markdown时，以下内容类型可能丢失:
- 内嵌H5P交互内容
- 内嵌MuseScore乐谱播放器
- Pressbooks特有的短代码（shortcodes）
- 交互式练习的链接可能是Pressbooks内部页面，导出后失效

### 10.4 中文翻译特有的问题
- 部分图片的alt文本比英文原文短（截断）
- 本地Graphics目录有95个文件，但Markdown中引用了97张图片——有2张图片可能缺失本地副本（或引用了相同图片的不同尺寸）
- 所有图片链接都指向远程Pressbooks URL，这可能导致构建后的网页在无网络时无法显示图片

---

## 总结

| 元素类型 | 中文翻译 (src/) | 英文原文 (knowledge/) | 差异 |
|---------|----------------|----------------------|------|
| 图片引用 | 97 | 97 | 模式不同，数量一致 |
| 本地图片缓存 | 95 | 0 | 中文特有 |
| MP3音频 | 3 | 3 | 一致 |
| YouTube视频 | 3 | 3 | 一致 |
| Vimeo视频 | 1 | 1 | 一致 |
| Spotify链接 | ~15 | ~15 | 一致 |
| iframe/HTML嵌入 | 0 | 0 | 一致(均无) |
| PDF引用 | ~200 | ~287 | 英文更多变体 |
| Musescore文件引用 | ~100 | ~100 | 一致 |
| Web应用引用 | ~5 | ~5 | 一致 |
| H5P交互练习 | 0 | 0 | 导出时丢失 |
| 嵌入式MuseScore播放器 | 0 | 0 | 导出时丢失 |
| Pressbooks短代码残留 | 1处 | 1处 | 一致 |

**整体结论**: 中文翻译的非文本引用与英文原文高度一致（图片、音频、视频、外部链接均完整保留）。主要差异在于:
1. 图片引用模式不同（中文版做成本地缓存+点击跳转）
2. PDF引用数量英文版稍多
3. Pressbooks原站的H5P交互、嵌入式MuseScore播放器等高级功能在Markdown导出中丢失，两仓库情况相同
