# WRETCH

一個基於 Django 的部落格/文章管理系統

## 專案簡介

WRETCH 是一個使用 Django 5.2.4 開發的網站專案，主要功能包含文章管理和靜態頁面展示。

## 功能特色

- 📝 **文章管理系统**
  - 文章的新增、編輯、刪除、查看
  - 文章詳細頁面
  - 文章列表頁面

- 📄 **靜態頁面**
  - 首頁
  - 關於我們
  - 聯絡我們

- 🔧 **管理後台**
  - Django Admin 介面
  - 完整的內容管理功能

## 技術規格

- **後端框架**: Django 5.2.4
- **資料庫**: SQLite
- **Python 版本**: >= 3.13
- **套件管理**: uv

## 安裝與執行

### 1. 安裝相依套件

```bash
uv sync
```

### 2. 資料庫遷移

```bash
uv run python manage.py makemigrations
uv run python manage.py migrate
```

### 3. 創建超級使用者（可選）

```bash
uv run python manage.py createsuperuser
```

### 4. 啟動開發伺服器

```bash
uv run python manage.py runserver
```

網站將在 `http://127.0.0.1:8000/` 運行

## 網址結構

- `/` - 首頁
- `/articles/` - 文章列表
- `/articles/new/` - 新增文章
- `/articles/<id>/` - 文章詳細頁面
- `/about/` - 關於我們
- `/contact/` - 聯絡我們
- `/admin/` - 管理後台

## 開發指令

### 快速啟動（使用 Makefile）

```bash
make run       # 啟動開發伺服器
make migrate   # 執行資料庫遷移
make shell     # 進入 Django shell
```

### 資料庫相關

```bash
# 建立遷移檔案
uv run python manage.py makemigrations

# 執行遷移
uv run python manage.py migrate

# 查看 SQL 語句
uv run python manage.py sqlmigrate articles 0001
```

## 專案結構

```
WRETCH/
├── articles/           # 文章應用
│   ├── models.py      # 文章模型
│   ├── views.py       # 視圖邏輯
│   ├── urls.py        # URL 路由
│   └── templates/     # 模板檔案
├── pages/             # 靜態頁面應用
│   ├── views.py       # 視圖邏輯
│   ├── urls.py        # URL 路由
│   └── templates/     # 模板檔案
├── templates/         # 共用模板
├── wretch/           # 專案設定
│   ├── settings.py   # Django 設定
│   └── urls.py       # 主要 URL 配置
├── manage.py         # Django 管理指令
└── README.md         # 專案說明
```

## 開發狀態

目前專案處於開發階段，已完成基本的文章管理功能和頁面結構。

## 貢獻

歡迎提出 Issue 或 Pull Request 來改善這個專案。

## 授權

此專案採用 MIT 授權條款。