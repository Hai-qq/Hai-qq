<p><a href="https://haiyi-yee.pages.dev"><img src="assets/brand/yee-banner.svg" width="100%" alt="Yee. — Research / Build / Observe；暖纸上的太阳，与个人网站呼应"></a></p>

### 亥一 / Yee

**研究能源系统。构建工具，记录 AI。**<br>
**Researching energy systems. Building tools. Documenting AI.**

上海交通大学能源动力硕士在读（2028 届），目前在施耐德电气做 AI 软件开发实习。主线是物理约束下的智能决策：用离线强化学习调度储能；也把 Agent 和 LLM 训练里容易出错的环节做成可复核的工具。平时在抖音、小红书和 B 站讲 AI 产品与科技科普。

Master's student in energy and power engineering at Shanghai Jiao Tong University (class of 2028), currently an AI software development intern at Schneider Electric. My research is decision-making under physical constraints, mainly offline RL for energy-storage dispatch. I also build checkable tools for the parts of agent and LLM training that tend to go wrong, and make videos explaining AI products and science.

[个人网站 Website](https://haiyi-yee.pages.dev) · [抖音 Douyin](https://www.douyin.com/user/MS4wLjABAAAAyBOI3mpE3w3bYaR08iZ3EhXNvZwm4JpVQpjU6ZFzL1hr9hwgniHzEn5gk7eEdmy-) · [小红书 Xiaohongshu](https://www.xiaohongshu.com/user/profile/63798f12000000001f01e4e3) · [B 站 Bilibili](https://space.bilibili.com/30639604) · [X](https://x.com/haiyi11011) · [Email](mailto:gqing2297@gmail.com)

#### Agent 与 LLM 工程 · Agent & LLM engineering

- **[SchedNav](https://github.com/Hai-qq/SchedNav)** — 让 GPU 调度建议经得起仿真与审计：Agent 只提有边界的策略，由确定性仿真执行、硬 SLO 审核。目前是研究阶段，未接真实集群。<br>
  <sub>Makes GPU scheduling suggestions checkable: agents propose bounded policies, a deterministic simulator runs them and hard SLOs gate the result. Research stage, not connected to a real cluster.</sub>
- **[RolloutCheck](https://github.com/Hai-qq/rolloutcheck)** — 检查多轮 LLM rollout 的历史 token 漂移，在 Qwen3-0.6B 真实轨迹和单卡 SGLang/CUDA 上验证过（alpha）。<br>
  <sub>Detects history-token drift in multi-turn LLM rollouts; checked on real Qwen3-0.6B traces and a single-GPU SGLang/CUDA setup (alpha).</sub>
- **[energy-centre-dispatch](https://github.com/Hai-qq/tb3-energy-centre-dispatch)** — 一道 Terminal-Bench 3 评测任务：让 Agent 修复医院冷热电三联供的日前调度工具。<br>
  <sub>A Terminal-Bench 3 task: the agent repairs the day-ahead dispatch tool of a hospital trigeneration energy centre.</sub>

#### 强化学习 · Reinforcement learning

- **[WalkerCmd](https://github.com/Hai-qq/WalkerCmd)** — MuJoCo 双足速度跟踪，从零实现 PPO，用 5 个种子和置换检验评估域随机化带来了什么。<br>
  <sub>Biped velocity tracking in MuJoCo with PPO written from scratch; 5 seeds and permutation tests on what domain randomization actually buys.</sub>

#### 设计与工具 · Design & tools

- **[Humanist](https://github.com/Hai-qq/humanist-frontend)** — 从 Anthropic 与 Kimi 的公开设计实践中提炼的界面规范和 Agent Skill。<br>
  <sub>Interface guidelines and an agent skill distilled from Anthropic's and Kimi's public design practice.</sub>
- **[间歇 Interlude](https://github.com/Hai-qq/Interlude)** — 一只手绘胖雀住在菜单栏，提醒你离开屏幕片刻（macOS）。<br>
  <sub>A hand-drawn chubby sparrow in your menu bar that reminds you to step away from the screen (macOS).</sub>
- **[Visual Inspection](https://github.com/Hai-qq/visual-inspection-test-deployment)** — Windows 工业视觉检测工作台：ONNX 检测、规则判定、可交付的测试序列。<br>
  <sub>A Windows workbench for industrial visual inspection: ONNX detection, rule-based verdicts and deliverable test sequences.</sub>
- **[Marginalia](https://github.com/Hai-qq/marginalia-worksheets)** — 给英语老师的 A4 练习单排版：写 Markdown，出可打印的 PDF。<br>
  <sub>Editorial A4 worksheets for English teachers: write Markdown, get a print-ready PDF.</sub>

#### 最近更新 · Recently updated

<!-- recent:start -->
- **[tb3-energy-centre-dispatch](https://github.com/Hai-qq/tb3-energy-centre-dispatch)** · 2026-10-21 — [Docs: HARDENING's pointer to tasks/ and README's results/ row brought…](https://github.com/Hai-qq/tb3-energy-centre-dispatch/commit/15fc800a5c48e8e348db0ce0337ec7facb629b9f)
- **[Interlude](https://github.com/Hai-qq/Interlude)** · 2026-10-16 — [docs: refresh third-party notices after dependency updates](https://github.com/Hai-qq/Interlude/commit/8a2cfb7be4d04af4aac1cba1a27f48f9e3956e27)
- **[WalkerCmd](https://github.com/Hai-qq/WalkerCmd)** · 2026-10-16 — [docs: add MIT license and neutral limitations heading](https://github.com/Hai-qq/WalkerCmd/commit/9786e06f7a12d6b1d2ad5283d3f6435af111b34a)
- **[humanist-frontend](https://github.com/Hai-qq/humanist-frontend)** · 2026-10-16 — [Redesign the editorial-warm and precise-light palettes](https://github.com/Hai-qq/humanist-frontend/commit/0dcfca8948cd01a6642dd978c2b45459567b9bb2)
- **[SchedNav](https://github.com/Hai-qq/SchedNav)** · 2026-10-15 — [Rework the project homepage and add contributor docs, quickstart and …](https://github.com/Hai-qq/SchedNav/commit/3c08ad91db43327eb5a1676a4d6ab3f98a45553c)
<!-- recent:end -->

<sub>安装方式、支持范围和验证证据见各项目 README；问题和建议欢迎开 Issue。<br>
Setup, scope and evidence are in each project's README. Issues and suggestions are welcome.</sub>
