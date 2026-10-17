# Free AI API List · 免费 AI API 资料清单

面向中文用户与 AI Agent 的免费 AI API 导航：区分当前免费模型、周期免费档、新人试用与附带购买条件的服务。**不承诺永久免费，不提供 Key 或公共中转。**

**资料可免费查看、复制、分享、修改和商用，支持程序自动读取。** 原创文档与数据采用 [CC0 1.0](LICENSE)；第三方服务与模型仍受其官方条款约束。

[平台详情](docs/platforms.md) · [机器可读 JSON](data/platforms.json) · [贡献指南](CONTRIBUTING.md)

> 整理日期：2026-10-17。共 23 个托管服务平台（含待核实、非免费参考和已退役项）及 4 个自建网关，并非 27 个可用的免费 API。本轮只检查公开文档，没有注册、领取额度或调用推理 API。
>
> 已纠正：Hugging Face 免费账号无月赠积分；GitHub Models 已退役。商汤公测、魔搭额度、智谱具体免费型号等尚待核实，请勿直接用于费用规划。

## 怎么用

1. 从下表选平台，点名称查看领取步骤、条件、地区、期限和官方来源。
2. 在官方站注册并确认目标模型的当前价格、免费余额和使用条款，再自行创建 Key。
3. 只选明确免费的模型；能设置时启用“额度用完即停”和消费上限。试用耗尽可能停止服务，也可能转付费。

**资料可以商用，不代表每个平台的免费服务可商用。** 例如 Cohere Trial Key 明确禁止商业和生产用途。`OpenAI 兼容`只指部分接口形式相似，不保证工具调用、模型参数与流式行为完全一致。

## 当前免费档 / 免费模型

| 平台 | 免费政策 / 当前状态 | 核查 |
| --- | --- | --- |
| [OpenRouter](docs/platforms.md#openrouter) | 提供 :free 模型及 openrouter/free 免费模型路由；并非所有模型免费。 | 部分核实 |
| [硅基流动 SiliconFlow](docs/platforms.md#siliconflow) | 实名后可调用平台标为免费的模型，费用为 0；免费模型限流固定。 | 部分核实 |
| [GroqCloud](docs/platforms.md#groq) | 存在 Free Plan；例：openai/gpt-oss-20b 与 120b 为 30 RPM、1000 RPD、8000 TPM、200000 TPD。 | 部分核实 |
| [Google AI Studio / Gemini API](docs/platforms.md#gemini) | 新账号从 Free Tier 开始，只覆盖部分模型；实际限额在 AI Studio 查看。 | 部分核实 |
| [Cloudflare Workers AI](docs/platforms.md#cloudflare) | Workers AI 每日免费 10,000 Neurons；部分模型要求付费方式，不在普通免费范围内。 | 部分核实 |
| [Mistral AI](docs/platforms.md#mistral) | Free mode 可创建 API Key，使用含在计划中的月度用量；没有统一公开数值。 | 部分核实 |
| [讯飞星火 Spark](docs/platforms.md#spark) | HTTP 官方文档列 Lite 支持免费使用；QPS、每日限额未统一确认。 | 部分核实 |

## 新人 / 评估 / 限时试用

| 平台 | 免费政策 / 当前状态 | 核查 |
| --- | --- | --- |
| [B.AI（Bank of AI）](docs/platforms.md#bai) | 积分制聚合；1 USD 对应 1,000,000 Credits；注册或活动赠额数量未统一确认。 | 部分核实 |
| [Cohere](docs/platforms.md#cohere) | Trial Key 每月 1000 次 API 调用；所列 Chat 模型试用限流为 20 次/分钟。 | 部分核实 |
| [阿里云百炼 Model Studio](docs/platforms.md#aliyun) | 参与新人活动的模型通常各有 100 万 Token；不同模型额度独立，不保证所有模型参与。 | 部分核实 |
| [Cerebras Inference](docs/platforms.md#cerebras) | 添加有效支付方式后可获一次性 $5 促销积分。 | 部分核实 |

## 附带购买条件的免费服务

| 平台 | 免费政策 / 当前状态 | 核查 |
| --- | --- | --- |
| [Gitee AI / 模力方舟](docs/platforms.md#gitee-ai) | 免费体验访问令牌提供每用户每天 100 次体验；正式调用标为免费的 API 需先购买任意金额全模型资源包。 | 部分核实 |

## 免费资格待核实

| 平台 | 免费政策 / 当前状态 | 核查 |
| --- | --- | --- |
| [商汤日日新 SenseNova](docs/platforms.md#sensenova) | 原稿称 Token Plan 公测 ¥0/月；当前公测价格及资格待核实。 | 待核实 |
| [魔搭 ModelScope API-Inference](docs/platforms.md#modelscope) | 原稿称有免费推理额度；2000 次/天与每日魔粒是不同历史口径，当前规则待核实。 | 待核实 |
| [NVIDIA NIM（build.nvidia.com）](docs/platforms.md#nvidia-nim) | 原稿称 build.nvidia.com 提供开发试用/预览；本轮未确认统一免费额度。 | 待核实 |
| [智谱 BigModel](docs/platforms.md#bigmodel) | 原稿列 GLM-4.7-Flash 与 GLM-4.6V-Flash 输入/输出/缓存免费；当前价格未完成核实。 | 待核实 |
| [百度千帆](docs/platforms.md#baidu) | 原稿称新人可获选定模型体验 Token；本轮未确认当前赠额。 | 待核实 |

## 非免费主列表 · 对照参考

| 平台 | 免费政策 / 当前状态 | 核查 |
| --- | --- | --- |
| [Hugging Face Inference Providers](docs/platforms.md#huggingface) | 免费账号无月赠积分；PRO 每月含 $2 计算积分，属于付费订阅权益。 | 部分核实 |
| [Together AI](docs/platforms.md#together) | 原稿引用的 get-credits 活动页面明确标为已过期；未确认通用免费档。 | 部分核实 |
| [Fireworks](docs/platforms.md#fireworks) | Serverless 推理按预付积分计费；原稿约 $1 注册赠额未核实。 | 部分核实 |
| [DeepInfra](docs/platforms.md#deepinfra) | 官方价格页按用量计费；未确认面向所有人的免费推理额度。 | 部分核实 |
| [SambaNova Cloud](docs/platforms.md#sambanova) | 套餐虽名为 Free，官方页面要求添加支付方式并购买积分后才能首次请求。 | 部分核实 |

## 已退役

| 平台 | 免费政策 / 当前状态 | 核查 |
| --- | --- | --- |
| [GitHub Models](docs/platforms.md#github-models) | GitHub Models 已退役；不能再按原稿的免费原型服务接入。 | 文档事实已确认 |

## 自建网关 · 不提供算力

| 平台 | 免费政策 / 当前状态 | 核查 |
| --- | --- | --- |
| [LiteLLM](docs/platforms.md#litellm) | 自建统一接口与路由，不提供免费算力。 | 部分核实 |
| [freellmpool](docs/platforms.md#freellmpool) | 自建多供应商路由与故障转移，本身不拥有免费算力。 | 部分核实 |
| [FreeLLMAPI-Extended](docs/platforms.md#freellmapi-extended) | 自建免费档聚合与自动回退，不保证上游免费服务持续可用。 | 部分核实 |
| [cn-freellm](docs/platforms.md#cn-freellm) | 自建国内多模型统一入口与故障转移，不提供额外免费额度。 | 部分核实 |

## AI Agent / 程序读取

发布到 `main` 后，可匿名读取下列 GitHub Raw URL，无需本仓库的 API Key：

- [README 原文](https://raw.githubusercontent.com/Tkkdy/Free-AI-API-List/main/README.md)
- [平台详情原文](https://raw.githubusercontent.com/Tkkdy/Free-AI-API-List/main/docs/platforms.md)
- [平台 JSON](https://raw.githubusercontent.com/Tkkdy/Free-AI-API-List/main/data/platforms.json)

首次发布前这些地址可能返回 404。读取清单不需要调用任何收费推理服务；真正使用各平台 API 需另行获得账号与授权。

可对 Agent 说：“读取上述 JSON，先检查 `updated_at`、`category`、`verification.scope` 和 `verification.pending`；列出候选服务及待确认条件，引用官方来源。不得把未知条件当作无需绑卡或允许商用，不自动注册、付费或调用模型。”

JSON 根对象含 `schema_version`、`updated_at`、`source`、`categories`、`platforms`。平台以稳定 `id` 标识，含额度说明、领取步骤、期限、地区、支付要求、商用约束、接入线索、来源和核查状态。额度是带单位和条件的文字，不宜直接拿来计算自动付费预算。

| 字段 | 含义 |
| --- | --- |
| `category` | `free_tier` 当前免费档；`trial` 试用；`conditional` 有购买前提；`unverified` 核心权益待核实；`non_free_reference` 非免费对照；`retired` 退役；`gateway` 自建工具 |
| `payment_method_required` / `commercial_use` | `true` / `false` / `null`；`null` 表示未知或不适用，务必同时读取对应说明 |
| `verification.status` | `documented` 限定文档事实已确认；`partial` 部分核实；`unverified` 核心免费权益尚未确认 |
| `last_checked_at` / `last_verified_at` | 最后检查日期 / `scope` 中限定事实的核实日期；后者可为 `null`，不等于整个平台已验证 |
| `api_base_urls` | 原稿中的接入线索；不是密钥、不保证当前可用，也不证明所有接口兼容 |

日期采用 `YYYY-MM-DD`。Agent 应保守筛选，排除退役项；待核实、付费参考和网关不能自动当成免费 API。商业任务还须核对官方服务条款与模型许可证。

更新采用 GitHub Issue / PR 人工核对官方文档，不承诺实时同步，不自动领取或刷新第三方额度。修改 `data/platforms.json` 后运行：

```sh
python scripts/render.py
python scripts/render.py --check
```

只需 Python 3.10+ 标准库。JSON 为唯一数据源，脚本生成 README 与详情文档；请先在 JSON 修改再生成。`--check` 只比较文件，不联网、不调用平台 API。程序可合理缓存 Raw 文件、降低轮询频率；需复现时，将 URL 中 `main` 换成确定的提交 SHA，并记录该 SHA。Git 历史与平台核查日期用于追踪更新。

## 来源与核查边界

初始线索来自维护者提供的 AI 整理稿 `free-ai-api-hubs.md`（原稿日期 2026-10-15）；来源文件哈希保存在 JSON，原稿本身未打包发布。公开版重新组织和表述事实，逐条保留官方链接；不复制第三方文档全文、品牌图片或代码。

本轮检查公开网页，区分“能访问”“内容可提取”“政策有明确证据”。动态渲染、登录后可见的额度和地区准入不能据此验证。各平台所有模型、账号实际余额、API 调用与生产稳定性均未实测。发现冲突时优先采用官方当前说明；不能确认的保留为待核实。

不收录来源不清的个人中转站，也不对具体未审查站点作侵权、窃密等指控。不要上传 API Key、Cookie、验证码或私人账单。自建网关不会增加免费算力，也不应被用于绕过上游限额。

## 贡献、许可与项目标签

通过 [Issue](https://github.com/Tkkdy/Free-AI-API-List/issues) 报错，或按 [CONTRIBUTING.md](CONTRIBUTING.md) 提交 PR；请附官方链接和检查日期。

原创文档、事实数据整理采用 [CC0 1.0 Universal](LICENSE)，可无偿商业再利用，无需署名；欢迎自愿保留来源。独立编写的 `scripts/*.py` 以及本 README 中原创程序示例适用 [MIT](LICENSE-MIT)。第三方商标、文档、代码、模型、服务与外链内容不因此重新授权，也不因列入清单而获得背书。

建议仓库 Topics：`free-api`、`ai-api`、`free-ai`、`llm`、`awesome-list`、`chinese`、`open-data`。标签需由维护者在 GitHub 仓库 About 中设置；写在这里不会自动更改仓库设置。
