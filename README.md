# RssCheckPush

这是一个基于 `Github Actions` 的 Youtube RSS 订阅内容筛选并通知的自动化脚本

可实现自定义订阅链接以及关键词通知内容，以及通过 [Push Deer](http://www.pushdeer.com/) 实现的通知推送


## 使用方法

1. `Fork` 本 Repo，修改 `config.json` 中的 feed 以及 keywords 为你想要的内容，keywords 支持多个关键词

2. 在 `Repo Settings -> Secrets -> Actions` 中新建一个 `Name` 为 `PUSH_TOKEN` 的 `Secret`，`Secret` 填写你的 `Push Deer Token`

3. 最后在 `Actions` 中手动运行一次 `RssCheckPush`，之后就会每 `6` 小时自动检测一次 Rss feed

## 其他说明

由于我本人懒狗，目前推送服务只支持了 Push Deer，如果有别的需求欢迎提交 `Issues`

`6` 小时一次的检测是写死在 `main.py` 和 `RssCheckPush.yml` 中的，代码量非常之少，有需求可以自行更改
