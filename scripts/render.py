# SPDX-License-Identifier: MIT
"""Render Markdown from the catalogue using Python 3.10+ standard library."""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATUS = {'documented': '文档事实已确认', 'partial': '部分核实', 'unverified': '待核实'}
BT = chr(96)

def build(data):
    entries = data['platforms']
    assert len({p['id'] for p in entries}) == len(entries), 'Duplicate platform IDs'
    overview = []
    details = ['# 平台详情', '', '> 数据日期：' + data['updated_at'] + '。本文件从 data/platforms.json 生成；修改数据后运行 python scripts/render.py。', '', '“已核实范围”只覆盖明确列出的事实。页面能访问不等于已领到额度；所有 API 均未实测。', '']
    for cat in data['categories']:
        group = [p for p in entries if p['category'] == cat['id']]
        overview += ['## ' + cat['label'], '', '| 平台 | 免费政策 / 当前状态 | 核查 |', '| --- | --- | --- |']
        details += ['## ' + cat['label'], '']
        for p in group:
            offer = p['offer'].replace('|', '/')
            overview.append(f"| [{p['name']}](docs/platforms.md#{p['id']}) | {offer} | {STATUS[p['verification']['status']]} |")
            details += [f'<a id="{p["id"]}"></a>', '', '### ' + p['name'], '']
            fields = [('政策 / 额度', 'offer'), ('有效期 / 重置', 'validity'), ('领取 / 使用', 'claim_steps'), ('使用条件', 'requirements'), ('地区', 'regions'), ('支付 / 绑卡', 'payment_notes'), ('商用', 'commercial_notes'), ('注意', 'cautions')]
            details += [f"- **{label}**：{p[key]}" for label, key in fields]
            bases = '、'.join(BT + x + BT for x in p['api_base_urls']) or '未提供公共可调用地址。'
            details += ['- **API 接入线索**：' + bases + ' ' + p['api_notes'], '- **来源**：' + ' · '.join('['+s['label']+']('+s['url']+')' for s in p['sources'])]
            v = p['verification']
            details += [f"- **核查状态**：{STATUS[v['status']]}；最后检查 {v['last_checked_at']}；限定事实最后核实 {v['last_verified_at'] or '未完成'}。", '- **已核实范围 / 检查说明**：' + v['scope'], '- **待核实**：' + ('；'.join(v['pending']) if v['pending'] else '该退役事实无待核实项；不表示核查过其他服务。'), '']
        overview.append('')
    replacements = {
        '__DATE__': data['updated_at'],
        '__HOSTED__': str(sum(p['kind'] == 'hosted_service' for p in entries)),
        '__GATEWAYS__': str(sum(p['kind'] == 'self_hosted_gateway' for p in entries)),
        '__TOTAL__': str(len(entries)),
    }
    header = HEADER.replace('§', BT)
    for token, value in replacements.items():
        header = header.replace(token, value)
    footer = FOOTER.replace('§', BT)
    return {'README.md': header + '\n'.join(overview) + '\n' + footer,
            'docs/platforms.md': '\n'.join(details).rstrip() + '\n'}

HEADER = """# Free AI API List · 免费 AI API 资料清单

面向中文用户与 AI Agent 的免费 AI API 导航：区分当前免费模型、周期免费档、新人试用与附带购买条件的服务。**不承诺永久免费，不提供 Key 或公共中转。**

**资料可免费查看、复制、分享、修改和商用，支持程序自动读取。** 原创文档与数据采用 [CC0 1.0](LICENSE)；第三方服务与模型仍受其官方条款约束。

[平台详情](docs/platforms.md) · [机器可读 JSON](data/platforms.json) · [贡献指南](CONTRIBUTING.md)

> 整理日期：__DATE__。共 __HOSTED__ 个托管服务平台（含待核实、非免费参考和已退役项）及 __GATEWAYS__ 个自建网关，并非 __TOTAL__ 个可用的免费 API。本轮只检查公开文档，没有注册、领取额度或调用推理 API。
>
> 已纠正：Hugging Face 免费账号无月赠积分；GitHub Models 已退役。商汤公测、魔搭额度、智谱具体免费型号等尚待核实，请勿直接用于费用规划。

## 怎么用

1. 从下表选平台，点名称查看领取步骤、条件、地区、期限和官方来源。
2. 在官方站注册并确认目标模型的当前价格、免费余额和使用条款，再自行创建 Key。
3. 只选明确免费的模型；能设置时启用“额度用完即停”和消费上限。试用耗尽可能停止服务，也可能转付费。

**资料可以商用，不代表每个平台的免费服务可商用。** 例如 Cohere Trial Key 明确禁止商业和生产用途。§OpenAI 兼容§只指部分接口形式相似，不保证工具调用、模型参数与流式行为完全一致。

"""
FOOTER = """## AI Agent / 程序读取

发布到 §main§ 后，可匿名读取下列 GitHub Raw URL，无需本仓库的 API Key：

- [README 原文](https://raw.githubusercontent.com/Tkkdy/Free-AI-API-List/main/README.md)
- [平台详情原文](https://raw.githubusercontent.com/Tkkdy/Free-AI-API-List/main/docs/platforms.md)
- [平台 JSON](https://raw.githubusercontent.com/Tkkdy/Free-AI-API-List/main/data/platforms.json)

首次发布前这些地址可能返回 404。读取清单不需要调用任何收费推理服务；真正使用各平台 API 需另行获得账号与授权。

可对 Agent 说：“读取上述 JSON，先检查 §updated_at§、§category§、§verification.scope§ 和 §verification.pending§；列出候选服务及待确认条件，引用官方来源。不得把未知条件当作无需绑卡或允许商用，不自动注册、付费或调用模型。”

JSON 根对象含 §schema_version§、§updated_at§、§source§、§categories§、§platforms§。平台以稳定 §id§ 标识，含额度说明、领取步骤、期限、地区、支付要求、商用约束、接入线索、来源和核查状态。额度是带单位和条件的文字，不宜直接拿来计算自动付费预算。

| 字段 | 含义 |
| --- | --- |
| §category§ | §free_tier§ 当前免费档；§trial§ 试用；§conditional§ 有购买前提；§unverified§ 核心权益待核实；§non_free_reference§ 非免费对照；§retired§ 退役；§gateway§ 自建工具 |
| §payment_method_required§ / §commercial_use§ | §true§ / §false§ / §null§；§null§ 表示未知或不适用，务必同时读取对应说明 |
| §verification.status§ | §documented§ 限定文档事实已确认；§partial§ 部分核实；§unverified§ 核心免费权益尚未确认 |
| §last_checked_at§ / §last_verified_at§ | 最后检查日期 / §scope§ 中限定事实的核实日期；后者可为 §null§，不等于整个平台已验证 |
| §api_base_urls§ | 原稿中的接入线索；不是密钥、不保证当前可用，也不证明所有接口兼容 |

日期采用 §YYYY-MM-DD§。Agent 应保守筛选，排除退役项；待核实、付费参考和网关不能自动当成免费 API。商业任务还须核对官方服务条款与模型许可证。

更新采用 GitHub Issue / PR 人工核对官方文档，不承诺实时同步，不自动领取或刷新第三方额度。修改 §data/platforms.json§ 后运行：

§§§sh
python scripts/render.py
python scripts/render.py --check
§§§

只需 Python 3.10+ 标准库。JSON 为唯一数据源，脚本生成 README 与详情文档；请先在 JSON 修改再生成。§--check§ 只比较文件，不联网、不调用平台 API。程序可合理缓存 Raw 文件、降低轮询频率；需复现时，将 URL 中 §main§ 换成确定的提交 SHA，并记录该 SHA。Git 历史与平台核查日期用于追踪更新。

## 来源与核查边界

初始线索来自维护者提供的 AI 整理稿 §free-ai-api-hubs.md§（原稿日期 2026-10-15）；来源文件哈希保存在 JSON，原稿本身未打包发布。公开版重新组织和表述事实，逐条保留官方链接；不复制第三方文档全文、品牌图片或代码。

本轮检查公开网页，区分“能访问”“内容可提取”“政策有明确证据”。动态渲染、登录后可见的额度和地区准入不能据此验证。各平台所有模型、账号实际余额、API 调用与生产稳定性均未实测。发现冲突时优先采用官方当前说明；不能确认的保留为待核实。

不收录来源不清的个人中转站，也不对具体未审查站点作侵权、窃密等指控。不要上传 API Key、Cookie、验证码或私人账单。自建网关不会增加免费算力，也不应被用于绕过上游限额。

## 贡献、许可与项目标签

通过 [Issue](https://github.com/Tkkdy/Free-AI-API-List/issues) 报错，或按 [CONTRIBUTING.md](CONTRIBUTING.md) 提交 PR；请附官方链接和检查日期。

原创文档、事实数据整理采用 [CC0 1.0 Universal](LICENSE)，可无偿商业再利用，无需署名；欢迎自愿保留来源。独立编写的 §scripts/*.py§ 以及本 README 中原创程序示例适用 [MIT](LICENSE-MIT)。第三方商标、文档、代码、模型、服务与外链内容不因此重新授权，也不因列入清单而获得背书。

建议仓库 Topics：§free-api§、§ai-api§、§free-ai§、§llm§、§awesome-list§、§chinese§、§open-data§。标签需由维护者在 GitHub 仓库 About 中设置；写在这里不会自动更改仓库设置。
"""

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Compare without writing files')
    args = parser.parse_args()
    data = json.loads((ROOT / 'data/platforms.json').read_text(encoding='utf-8'))
    for name, content in build(data).items():
        path = ROOT / name
        if args.check:
            if not path.exists() or path.read_text(encoding='utf-8') != content:
                raise SystemExit(f'Out of sync: {name}; run python scripts/render.py')
        else:
            path.write_text(content, encoding='utf-8', newline='\n')
    print('PASS: Markdown matches JSON' if args.check else 'Rendered README.md and docs/platforms.md')

if __name__ == '__main__':
    main()
