"""把公开仓库的最近更新写进 README 的 recent 标记之间。

只用标准库。需要环境变量 GITHUB_TOKEN（Actions 自带的即可，只读公开数据）。
用法：python3 scripts/update_recent.py [README 路径]
"""

import json
import os
import re
import sys
import urllib.request
from datetime import datetime, timedelta, timezone

LOGIN = "Hai-qq"
LIMIT = 5  # 列出几条
TZ = timezone(timedelta(hours=8))  # 日期按北京时间显示
START, END = "<!-- recent:start -->", "<!-- recent:end -->"

# 依赖升级之类的例行提交不算「更新」
SKIP_HEADLINE = re.compile(r"^(bump |chore\(deps|merge pull request .*dependabot)", re.I)

QUERY = """
query($login: String!) {
  user(login: $login) {
    repositories(first: 30, privacy: PUBLIC, ownerAffiliations: OWNER, isFork: false,
                 orderBy: {field: PUSHED_AT, direction: DESC}) {
      nodes {
        name
        url
        isArchived
        latestRelease { tagName publishedAt url }
        defaultBranchRef {
          target {
            ... on Commit {
              history(first: 15) {
                nodes { committedDate messageHeadline url author { name } }
              }
            }
          }
        }
      }
    }
  }
}
"""


def graphql(token):
    body = json.dumps({"query": QUERY, "variables": {"login": LOGIN}}).encode()
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=body,
        headers={"Authorization": f"bearer {token}", "User-Agent": "profile-readme"},
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.load(resp)
    if data.get("errors"):
        raise SystemExit(f"GraphQL error: {data['errors']}")
    return data["data"]["user"]["repositories"]["nodes"]


def escape(text):
    # 提交信息里的 Markdown/HTML 符号转义，避免把 README 排版弄乱
    return re.sub(r"([\\`*_\[\]<>|])", r"\\\1", text)


def day(iso):
    return datetime.fromisoformat(iso.replace("Z", "+00:00")).astimezone(TZ).strftime("%Y-%m-%d")


def latest_event(repo):
    """返回这个仓库最近一次值得列出的更新：(时间, Markdown 文本)。"""
    events = []
    rel = repo.get("latestRelease")
    if rel and rel.get("publishedAt"):
        events.append((rel["publishedAt"], f"发布 Released [{escape(rel['tagName'])}]({rel['url']})"))
    target = (repo.get("defaultBranchRef") or {}).get("target") or {}
    for c in (target.get("history") or {}).get("nodes", []):
        if "[bot]" in (c["author"]["name"] or "") or SKIP_HEADLINE.search(c["messageHeadline"]):
            continue
        events.append((c["committedDate"], f"[{escape(c['messageHeadline'])}]({c['url']})"))
        break
    return max(events) if events else None


def render(repos):
    items = []
    for repo in repos:
        if repo["name"].lower() == LOGIN.lower() or repo["isArchived"]:
            continue
        ev = latest_event(repo)
        if ev:
            items.append((ev[0], f"- **[{repo['name']}]({repo['url']})** · {day(ev[0])} — {ev[1]}"))
    items.sort(reverse=True)
    return "\n".join(line for _, line in items[:LIMIT])


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "README.md"
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if not token:
        raise SystemExit("缺少 GITHUB_TOKEN")
    readme = open(path, encoding="utf-8").read()
    if START not in readme or END not in readme:
        raise SystemExit("README 里没有 recent 标记")
    block = f"{START}\n{render(graphql(token))}\n{END}"
    new = re.sub(re.escape(START) + r".*?" + re.escape(END), lambda _: block, readme, flags=re.S)
    if new != readme:
        open(path, "w", encoding="utf-8").write(new)
        print("README 已更新")
    else:
        print("没有变化")


if __name__ == "__main__":
    main()
