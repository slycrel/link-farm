# AI Links Collection
**Total Posts**: 702  
**Date Range**: 2024-06-11 – 2026-07-16  
**Enriched**: 701/702 (99%)

---
## Morning view

*Generated 2026-07-16T15:08:07Z. Hard-capped surface — see CURATION_DESIGN.md.*

### Read now
- **2026-07-09** — [Kodus](https://kodus.io/self-hosted-ai-code-review/) — *now • Dev Practices • v1 enriched*  
  Kodus (github.com/kodustech/kodus-ai) — open-source AGPLv3 self-hosted AI code review. The full PR-review pipeline (Kody agent) runs on your own infrastructure with bring-your-own-LLM: it posts line-anchored inline comments covering logic/security/performance (or 'deep mode' with parallel bug/security/performance specialists), keeps source code, LLM calls, and audit trails inside your VPC, and supports GitHub Enterprise Server / GitLab Self-Managed / Bitbucket DC and air-gapped deploys. Jeremy flagged it to evaluate for work code reviews.
- **2026-07-16** — [Aaron Levie](https://x.com/levie/status/2077526010753581156) — *near-term • Management • v1 enriched*  
  Aaron Levie's notes from a dinner with enterprise IT leaders on agent adoption: change management is the biggest blocker (processes and data pipelines must be modernized to work with agents), embedding engineers directly into business functions as internal forward-deployed engineers dramatically accelerates successful agent rollouts, and the technical function is becoming more strategically important than ever.
- **2026-07-16** — [0xSero](https://x.com/0xsero/status/2077488957999173936) — *near-term • Research • 62.3K views • v1 enriched*  
  0xSero highlights Thinking Machines' launch of Inkling (thinkingmachines.ai/news/introducing-inkling), a 950B-parameter American open-weight model that reasons across text, image, and audio modalities with full weights released. Available for fine-tuning on Thinking Machines' Tinker platform and via the Inkling Playground.
- **2026-07-16** — [Superman](https://x.com/thesupermanmx/status/2077321341490090486) — *near-term • Research • 7,028 views • v1 enriched*  
  turbovec (github.com/RyanCodrai/turbovec) is a vector index built on TurboQuant, written in Rust with Python bindings — a performance-oriented approximate nearest-neighbor index relevant to embedding search and RAG pipelines.
- **2026-07-15** — [Ashpreet Bedi](https://x.com/ashpreetbedi/status/2077169299777531942) — *near-term • Agent Design • 6,019 views • v1 enriched*  
  Ashpreet Bedi (Agno) shares a new post, Self-Driving Agent Infrastructure (ashpreetbedi.com/self-driving-agent-infrastructure), arguing AI/software engineering is the first domain to gain autonomous 'self-driving' capabilities, and walking through how he built his self-driving agent platform.

### Recurring this week
*No concepts gained new evidence in the last 14 days. Run mechanical discovery or seed curated concepts to populate this section.*

### Revisit from last month
- **2024-06-18** — [curvedinf](https://github.com/curvedinf/dir-assistant) — *near-term • Agent Design • v1 enriched*  
  dir-assistant is a pip-installable CLI that recursively indexes the text files in your directory so you can chat with them via a local or API LLM, auto-injecting the most contextually relevant files. It uses CGRAG (Contextually Guided RAG) for file selection, supports interactive and single-prompt modes (including auto file edits + git commits), many local acceleration backends and all major LLM APIs via LiteLLM, and optimizes prompt/context caching (50-90% cache hits).
- **2025-01-04** — [Tom Dörr](https://github.com/tom-doerr/dotfiles/blob/master/instruction.md) — *near-term • Claude Code • v1 enriched*  
  Tom Dörr's AI-coding-agent instruction file (an AGENTS.md-style rules doc): single-letter command aliases (c=continue, rc=reduce complexity, acp=add/commit/push, t=add tests), strict engineering rules (no fallbacks, don't swallow exceptions, TDD with many asserts, uv over pip, work on git branches, keep complexity low, don't weaken the linter), and ready-to-paste DSPy optimizer snippets (BootstrapFewShotWithRandomSearch, MIPROv2, SIMBA).

---
## Topic Distribution
| Topic | Count | % |
|-------|-------|---|
| agent-design | 372 | 53.0% |
| claude-code | 174 | 24.8% |
| dev-practices | 255 | 36.3% |
| skills-mcp | 146 | 20.8% |
| prompting | 105 | 15.0% |
| research | 155 | 22.1% |
| industry | 95 | 13.5% |
| management | 106 | 15.1% |
| questionable | 114 | 16.2% |
| general | 96 | 13.7% |

---
## Quick Reference (50 Most Recent)
| Date | Author | Topic | Summary |
|------|--------|-------|--------|
| 2026-07-16 | Aaron Levie | management | Aaron Levie's notes from a dinner with enterprise IT leaders on agent... |
| 2026-07-16 | 0xSero | research | 0xSero highlights Thinking Machines' launch of Inkling (thinkingmachin... |
| 2026-07-16 | Superman | research | turbovec (github.com/RyanCodrai/turbovec) is a vector index built on T... |
| 2026-07-15 | Ashpreet Bedi | agent-design | Ashpreet Bedi (Agno) shares a new post, Self-Driving Agent Infrastruct... |
| 2026-07-14 | Alvaro Videla | research | Alvaro Videla released LeetLLM (github.com/videlalvaro/leet-llm) — a f... |
| 2026-07-14 | JoePro | skills-mcp | JoePro shares a reworked 'Frontend Design Skill' (an agent/Claude skil... |
| 2026-07-14 | witcheer | research | witcheer crowdsourced and hand-tallied 250+ replies on how people run... |
| 2026-07-14 | How To Prompt | agent-design | How To Prompt highlights an open-source, privacy-first Chromium fork b... |
| 2026-07-14 | Alex Prompter | prompting | Alex Prompter's thread pitches 'cloning' Fable 5's reasoning into Opus... |
| 2026-07-13 | Jamon Holmgren | agent-design | Jamon Holmgren dumps his complete agentic coding setup as a 10+ point... |
| 2026-07-09 | Kodus | dev-practices | Kodus (github.com/kodustech/kodus-ai) — open-source AGPLv3 self-hosted... |
| 2026-07-07 | How To Prompt | agent-design | How To Prompt (hype framing: "China has killed the vector database ind... |
| 2026-07-07 | Ryan Carson | agent-design | Ryan Carson (@HelloUntangle) details orchestrating the largest/riskies... |
| 2026-07-06 | Satyam Pariyar | agent-design | Satyam Pariyar shares Kybernetes (github.com/pariyar07/kybernetes), a... |
| 2026-07-06 | leopardracer | questionable | Engagement-farmed take (ALL CAPS) claiming an Anthropic engineer said... |
| 2026-07-06 | ericosiu | agent-design | Eric Siu shares a 7-step checklist for building a 'Company Brain' (an... |
| 2026-07-06 | Isra | agent-design | Isra flags Alibaba's newly open-sourced Page-Agent (~22K GitHub stars,... |
| 2026-07-06 | Akshay | agent-design | Akshay Pachaar explains building a '1-person AI company' that runs loc... |
| 2026-07-06 | kaize | agent-design | kaize shares a 'Loop engineering' reading list, arguing 2026 agents ar... |
| 2026-07-06 | 0xSero | research | 0xSero (quote-tweeting Rohan Paul on a Meta paper showing quantized re... |
| 2026-07-06 | Anatoli Kopadze | agent-design | Anatoli Kopadze's widely-viewed piece 'Loops explained: Claude, GPT, M... |
| 2026-07-05 | Dami-Defi | general | Dami-Defi promotes an Obsidian community plugin (19,184 downloads) tha... |
| 2026-07-05 | Anatoli Kopadze | claude-code | Anatoli Kopadze (quote-tweeting his own Claude features guide) shares... |
| 2026-07-05 | Nyk | agent-design | [Jeremy flagged: urgent for orchestration] Nyk released Council of Hig... |
| 2026-07-05 | Elvis | skills-mcp | Elvis makes a meta point about eval-driven skill building that extends... |
| 2026-07-05 | Aaron Levie | industry | Aaron Levie (Box CEO) argues the battle in AI is shaping up to be a ba... |
| 2026-07-05 | Avid | agent-design | Avid (ALL CAPS engagement framing) makes a practical context-engineeri... |
| 2026-07-05 | Sprytix | agent-design | Sprytix (clickbait 'Anthropic just leaked an internal engineering docu... |
| 2026-07-05 | alex fazio | agent-design | alex fazio recommends studying ARC-AGI-winning harnesses to learn harn... |
| 2026-07-05 | darkzodchi | claude-code | darkzodchi's 'Claude Fable 5 Setup Guide' covers which heavy tasks act... |
| 2026-07-05 | me | questionable | Engagement-farmed clickbait promoting a 16-minute tutorial on building... |
| 2026-07-04 | Tom Dörr | skills-mcp | Tom Dörr shares VoltAgent's awesome-claude-skills (github.com/VoltAgen... |
| 2026-07-04 | 0xSero | claude-code | 0xSero shares Parcels (github.com/0xSero/parcels) — a tool for 'cloud... |
| 2026-07-04 | ali | questionable | ali (@waterloo_intern) — an apparent parody of distillation hype: clai... |
| 2026-07-04 | akira | agent-design | akira introduces Onyx, a VM/runtime for programmable agent orchestrati... |
| 2026-07-04 | Archive | claude-code | Archive (engagement framing, 'met an Anthropic engineer making $1.2M')... |
| 2026-07-04 | ℏεsam | management | [Jeremy flagged: read for work] hesam recommends Phil Chen's article '... |
| 2026-07-04 | Thariq | prompting | Thariq shares his article 'A Field Guide to Fable: Finding Your Unknow... |
| 2026-07-04 | Daniel Miessler | prompting | Daniel Miessler shares a set of 'prompts to run now that you have Fabl... |
| 2026-07-04 | Akshay | agent-design | Akshay Pachaar summarizes a Hugging Face blog post on 'evolving the ha... |
| 2026-07-04 | Rahul | agent-design | Rahul shares a free 'Loop Library' (signals.forwardfuture.com/loop-lib... |
| 2026-07-02 | Dhilip Subramanian | claude-code | Dhilip walks through his 7-skill Claude Code setup and what each earns... |
| 2026-07-02 | Andrew Ng | agent-design | Andrew Ng's 'loop engineering' letter lays out three nested loops for... |
| 2026-06-29 | Akshay | agent-design | Walkthrough of Google's Agents CLI as tooling for Karpathy's "agentic... |
| 2026-06-29 | Boris Cherny | management | As engineering/product/design/DS roles blur, Cherny proposes five team... |
| 2026-06-27 | zostaff | agent-design | Long-form "Loop Engineering" article: four autonomous loops that actua... |
| 2026-06-27 | Brian Armstrong | management | Coinbase's playbook for keeping AI spend flat while token usage grows:... |
| 2026-06-27 | Prajwal Tomar | agent-design | Pro tip framed around the author's promotional "Hermes Agent" article:... |
| 2026-06-27 | Brady Long | skills-mcp | Promo-styled writeup of MemPalace, an open-source local AI memory tool... |
| 2026-06-25 | Alex Lieberman | management | A "5 levels of work" framework for teaching high agency (credited to @... |

---
## Posts by Topic

### Agent Design (372)

- [Aaron Levie](https://x.com/levie/status/2077526010753581156) — 2026-07-16: Aaron Levie's notes from a dinner with enterprise IT leaders on agent adoption: change management is the biggest blocker (processes and data pipelines must be modernized to work with agents), embedding engineers directly into business functions as internal forward-deployed engineers dramatically accelerates successful agent rollouts, and the technical function is becoming more strategically important than ever.

- [Ashpreet Bedi](https://x.com/ashpreetbedi/status/2077169299777531942) — 2026-07-15: Ashpreet Bedi (Agno) shares a new post, Self-Driving Agent Infrastructure (ashpreetbedi.com/self-driving-agent-infrastructure), arguing AI/software engineering is the first domain to gain autonomous 'self-driving' capabilities, and walking through how he built his self-driving agent platform.

- [How To Prompt](https://x.com/howtoprompt__/status/2076689880026096089) — 2026-07-14: How To Prompt highlights an open-source, privacy-first Chromium fork built by an ex-Google engineer with a native AI agent, built-in MCP server, Cowork-style web+local-file agents, scheduled autopilot tasks, 40+ app integrations (Gmail, Slack, Notion, Linear, Figma, Salesforce), and local-model (Ollama) support — drivable from Claude Code or Gemini CLI. Engagement-framed but describes a real agentic-browser tool worth evaluating.

- [Jamon Holmgren](https://x.com/jamonholmgren/status/2076001786700394610) — 2026-07-13: Jamon Holmgren dumps his complete agentic coding setup as a 10+ point checklist: an AGENTS.md that acts as a router to skills/docs/tools; a customized workflow skill (he recommends grabbing Matt Pocock's skills); self-healing, greppable docs with a 7-line summary header; agents that actually run and test the app themselves; e2e tests plus docs on how/what to test; custom precommit linters with --fix that shell out to a cheaper LLM (Composer 2.5 or Sonnet) to actually fix rather than flag; cross-agent review (codex/claude/cursor, never the same model reviewing itself) at research/plan/implementation/wrap-up; handoff worksheets committed with git tags so another agent can finish the job; automatic end-of-session agent feedback docs he periodically ingests to improve workflows; a tools/bin folder of agent-authored scripts (e.g. an agent_review CLI wrapper); and periodic agent sweeps through recent commits. Practical, adoptable patterns for a team running coding agents.

- [Kodus](https://kodus.io/self-hosted-ai-code-review/) — 2026-07-09: Kodus (github.com/kodustech/kodus-ai) — open-source AGPLv3 self-hosted AI code review. The full PR-review pipeline (Kody agent) runs on your own infrastructure with bring-your-own-LLM: it posts line-anchored inline comments covering logic/security/performance (or 'deep mode' with parallel bug/security/performance specialists), keeps source code, LLM calls, and audit trails inside your VPC, and supports GitHub Enterprise Server / GitLab Self-Managed / Bitbucket DC and air-gapped deploys. Jeremy flagged it to evaluate for work code reviews.

- [How To Prompt](https://x.com/howtoprompt__/status/2074122800961614184) — 2026-07-07: How To Prompt (hype framing: "China has killed the vector database industry") flags Tencent's newly open-sourced TencentDB Agent Memory — local long-term memory for AI agents that runs 100% on plain SQLite with no external vector DB or cloud APIs. Claims 61% fewer tokens and PersonaMem accuracy 48%->76%. Uses a layered 'semantic pyramid' (L0 conversation -> L1 atom -> L2 scenario -> L3 persona) stored as inspectable markdown + Mermaid graphs instead of opaque vector compression, with drill-back to raw logs by node_id. ~5.1k GitHub stars.

- [Ryan Carson](https://x.com/ryancarson/status/2074093250399330418) — 2026-07-07: Ryan Carson (@HelloUntangle) details orchestrating the largest/riskiest engineering program in the company's history with a single Fable parent orchestrator session: 834 files, prod data mutation, DB schema update, 31 PRs, started Friday->completed Monday, zero prod incidents. One parent Devin/Fable session planned the work, spawned ~40 child sessions to execute, enforced regression gates and backup checks between phases, and escalated only owner-level decisions (scope rulings, go/no-go on irreversible steps). Distills reusable program-management patterns for large migrations. In a follow-up he asks Cognition to let child Devin sessions pick their own model/mode independent of the parent.

- [Satyam Pariyar](https://x.com/spariyar07/status/2074142974095835518) — 2026-07-06: Satyam Pariyar shares Kybernetes (github.com/pariyar07/kybernetes), a small OSS experiment: a 'loop governor' / runtime-adaptive control plane for agentic coding work, aimed at governing coding-agent execution loops at runtime.

- [leopardracer](https://x.com/leopardracer/status/2074071476181876944) — 2026-07-06: Engagement-farmed take (ALL CAPS) claiming an Anthropic engineer said memory/retrieval architecture is the only skill worth learning in 2026 — arguing prompt writers cap ~$90k, engineers building memory/retrieval systems clear $250-400k, and those architecting 'the whole loop' pull seven figures ('architecture is the moat, memory is the new distribution'). Quote-tweets CyrilXBT's article 'How To Become An AI Engineer in 2026 (Without a CS Degree).' Mostly hype, thin substance.

- [ericosiu](https://x.com/ericosiu/status/2073943223836270933) — 2026-07-06: Eric Siu shares a 7-step checklist for building a 'Company Brain' (an org-wide AI agent): (1) pick one high-value workflow closest to revenue; (2) map only the critical connectors (Google Drive, Slack, CRM, Gong, Granola); (3) define memory — brand voice, decisions, workflow rules, examples, with recent decisions weighted over old ones; (4) set permissions/approvals/data exposure to avoid 'a security problem with a chat interface'; (5+) route the work. A practical playbook for company-wide AI adoption.

- [Isra](https://x.com/israfill/status/2073789727698743516) — 2026-07-06: Isra flags Alibaba's newly open-sourced Page-Agent (~22K GitHub stars, +949 in a day) — an MIT-licensed JavaScript library that embeds an AI agent directly into any webpage via a single <script> tag. It reads the live DOM as structured text and acts as the real user with no headless browser, Selenium/Playwright, Python server, or computer vision. Works with any LLM (GPT, Claude, Grok, Qwen, local via Ollama), has built-in human confirmation before critical actions, and can pair with the Web Speech API for voice control. Pitched as a lightweight replacement for Selenium/Playwright and vision-based browser agents.

- [Akshay](https://x.com/akshay_pachaar/status/2073783428735250595) — 2026-07-06: Akshay Pachaar explains building a '1-person AI company' that runs locally, is 100% open-source, has no human employees (all agents), and collaborates in real time via email. His framing: multi-agent orchestration isn't new, but instead of hand-wiring a graph of nodes/edges you should model coordination on the org-chart structure companies have used for a century — lay out an org chart, each agent fills one role with reporting lines, and work flows up/down without manually relaying each message.

- [kaize](https://x.com/0x_kaize/status/2073743517155774641) — 2026-07-06: kaize shares a 'Loop engineering' reading list, arguing 2026 agents are less about smarter prompts and more about longer runs — the real questions are whether an agent can recover from a failed step, control spend, and know when to stop. Curated links: Addy Osmani (addyosmani.com/blog/loop-engineering), Firecrawl (firecrawl.dev/blog/loop-engineering), Oracle 'What is the AI agent loop', OpenAI 'Harness engineering', and Martin Fowler 'Harness engineering for coding agent users'.

- [0xSero](https://x.com/0xsero/status/2073651251594854573) — 2026-07-06: 0xSero (quote-tweeting Rohan Paul on a Meta paper showing quantized reasoning models often fail because compression makes them doubt a correct answer instead of finishing) reports experimenting with penalizing 'self-doubt' words during generation — claiming ~30% fewer output tokens — plus improving tok/s via CPU offloading.

- [Anatoli Kopadze](https://x.com/anatolikopadze/status/2068328135611822149) — 2026-07-06: Anatoli Kopadze's widely-viewed piece 'Loops explained: Claude, GPT, Mira and what actually works' argues most people use AI the slow way (type, wait, fix, repeat by hand) and that the faster approach top AI engineers care about is building loops. Covers what loops are, how they work under the hood, when they're worth it vs a trap, and how to build a basic one in Claude or ChatGPT. Quote-tweets Peter Steinberger: you shouldn't be prompting coding agents, you should be designing loops that prompt your agents. (Includes some self-promotion for his X/Telegram.)

- [Nyk](https://x.com/nyk_builderz/status/2073305434069647735) — 2026-07-05: [Jeremy flagged: urgent for orchestration] Nyk released Council of High Intelligence v1.2.0 as a Claude Code plugin (/plugin marketplace add 0xNyk/council-of-high-intelligence) — an 18-persona deliberation engine (Aristotle, Feynman, Kahneman, Torvalds, Socrates, Taleb, Meadows + more) that runs 3 rounds of anonymized cross-examination to one auditable verdict on your existing subscriptions, no API keys. v1.2.0 adds confidence-weighted verdicts (vote weight scales with stated confidence; a hesitant council escalates to you instead of forcing consensus, per Roundtable Policy + ConfMAD 2025), per-persona reasoning methods (Socratic elenchus, Taleb tail stress-testing, Meadows causal-loop mapping via DMAD), per-project defaults via .council.yaml, and CI parity gates so the Claude/Codex/Gemini coordinators can't silently drift.

- [Elvis](https://x.com/elvissun/status/2073161303997452794) — 2026-07-05: Elvis makes a meta point about eval-driven skill building that extends beyond coding to any knowledge problem where an eval set can be concretely defined. Example: a newsjack.sh skill that judges newsworthiness — he started from labeled examples (stories that made real news vs ones that didn't, e.g. hitting #1 on Product Hunt isn't news even though LLMs say it is), fed them into an eval set, then used /goal to iterate a skill implementation that lets 3 agents (Opus, Sonnet, Haiku) all score stories correctly — proving 'the intelligence lives in the skill, not the model.' Notes Fable's ability to learn across examples and draw a through-line is well beyond Opus.

- [Aaron Levie](https://x.com/levie/status/2073138135014502777) — 2026-07-05: Aaron Levie (Box CEO) argues the battle in AI is shaping up to be a battle for context: agent effectiveness comes down to having the right domain expertise, access to the right context and tools, and being embedded in workflows users can easily review and incorporate. The platforms that capture and leverage the best context within their agents — and pick the right model per task — will be where agents do their best work (coding, legal, support agents at scale). This is why the applied-AI layer is worth far more than being an 'LLM wrapper': the value is in organizing the critical knowledge.

- [Avid](https://x.com/av1dlive/status/2073114542851416260) — 2026-07-05: Avid (ALL CAPS engagement framing) makes a practical context-engineering point: give an agent one index file per major folder for a direct line to what it needs. The same task dropped from 2 minutes (7 files opened, wandering, a 3-month-old brief still missing) to 10 seconds with the same model, nothing else changed. 'Build the path or watch it search in the dark.' Quote-tweets Machina's article 'How to build a second brain with Fable 5.'

- [Sprytix](https://x.com/sprytixl/status/2073101741604679714) — 2026-07-05: Sprytix (clickbait 'Anthropic just leaked an internal engineering document' framing) lays out a six-layer self-improving agent loop: Generate -> Evaluate -> Remember -> Schedule -> Optimize -> Recurse. Generation produces its own solutions (no human brief), Evaluation is a second layer that can say no, Memory retains useful discoveries each cycle, Scheduling decides what happens next, Optimization updates behavior based on what worked, and Recursion means removing any single layer drops performance significantly — shifting the human from operator to designer.

- [alex fazio](https://x.com/alxfazio/status/2073091833530392614) — 2026-07-05: alex fazio recommends studying ARC-AGI-winning harnesses to learn harness engineering from first principles — they clearly illustrate what works, what's BS, and why a lot of current harness design is overfitted to benchmark-maxxing.

- [Tom Dörr](https://x.com/tom_doerr/status/2073354493794636248) — 2026-07-04: Tom Dörr shares VoltAgent's awesome-claude-skills (github.com/VoltAgent/awesome-claude-skills) — a curated 'awesome list' of official agent Skills from leading engineering teams.

- [0xSero](https://x.com/0xsero/status/2073274981279260774) — 2026-07-04: 0xSero shares Parcels (github.com/0xSero/parcels) — a tool for 'cloud agents' when you have Tailscale and more than one desktop: it packages your repo plus a live coding-agent session (Claude Code / Codex / pi), transfers it to another machine on your Tailscale network, and runs it in tmux so you can step away from the screen.

- [akira](https://x.com/realmcore_/status/2073170941878944022) — 2026-07-04: akira introduces Onyx, a VM/runtime for programmable agent orchestration that 'turns orchestration into software engineering.' The article covers the design constraints and decisions behind the VM and how to write programs and architect agent systems on it. Framing: agents are inherently non-deterministic (that's the point), but breaking execution into structured steps (Plan, Implement, Review, QA) plus scripts/tools/skills to steer, share context, and guardrail agents improves performance. References ReAct and related arxiv papers and karpathy/autoresearch.

- [Archive](https://x.com/archiveexplorer/status/2073136973162872897) — 2026-07-04: Archive (engagement framing, 'met an Anthropic engineer making $1.2M') argues the real lever isn't Opus vs Sonnet but 'what the model wakes up into' — the .claude/ folder: CLAUDE.md (the contract), settings.json (permissions), hooks/ (reflexes), agents/verifier (a shift-notes checker subagent), skills/ (~33 reusable 'muscle memories'), .mcp.json (tools), and MEMORY.md (shift log). 'You write the folder once; the folder runs the model.' Quote-tweets his own article 'Loop and Harness engineering: 7 files, 5 steps.'

- [Thariq](https://x.com/trq212/status/2073101078145724589) — 2026-07-04: Thariq shares his article 'A Field Guide to Fable: Finding Your Unknowns' — the most important part of working with Claude Fable 5 is discovering your own unknowns so you can prompt it better. Framing: 'the map is not the territory' — your prompts, skills, and context are the map (a representation of the work to be done), and the practice is surfacing what you don't yet know about the actual work.

- [Akshay](https://x.com/akshay_pachaar/status/2072961737008336937) — 2026-07-04: Akshay Pachaar summarizes a Hugging Face blog post on 'evolving the harness' instead of training the model: they took a frozen open model scoring 0% on a hard legal-agent benchmark, left its weights untouched, and let an automated loop rewrite only the surrounding harness code (the runtime wrapper that feeds context, runs tool calls, and decides when a run ends). It ended up essentially matching Sonnet 4.6 on the headline metric at ~7x lower cost per task, zero weights changed. The insight: the 0% wasn't measuring legal reasoning — the model reasoned correctly but saved outputs under the wrong filename/folder or not at all — so it was measuring the harness.

- [Rahul](https://x.com/sairahul1/status/2072749611471835229) — 2026-07-04: Rahul shares a free 'Loop Library' (signals.forwardfuture.com/loop-library/) of reusable agent loops, plus his article '20 Loop Design Patterns Every AI Engineer Should Know.' Framing: most engineers can build an agent (a worker) but few can build a system that gets better after the first attempt — and that gap is 'worth six figures.'

- [Andrew Ng](https://x.com/andrewyng/status/2071988145667928442) — 2026-07-02: Andrew Ng's 'loop engineering' letter lays out three nested loops for building 0-to-1 products: the fast agentic coding loop (agent writes/tests/iterates every few minutes), the developer feedback loop (human steers over tens of minutes to hours), and the slow external feedback loop (alpha testers, A/B tests over days). Humans retain a context advantage, so engineers increasingly play a partial product-management role.

- [Akshay](https://x.com/akshay_pachaar/status/2071509401224261823) — 2026-06-29: Walkthrough of Google's Agents CLI as tooling for Karpathy's "agentic engineering" (spec design, eval loops, security). One setup command injects 7 ADK-specific skills into a coding agent; author built and deployed a RAG agent end-to-end with Claude Code, including 20 LLM-as-judge eval scenarios and enterprise registration.

- [zostaff](https://x.com/zostaff/status/2070852153594290195) — 2026-06-27: Long-form "Loop Engineering" article: four autonomous loops that actually pay off because the task repeats, a machine can reject the result, the agent carries it whole, and "done" is objective. Covers the bare while-loop/exit-code/budget mechanics under Claude Code Routines and four worked configs: morning CI test triage (with maker-checker subagent), dependency watchdog, doc synchronizer, and overnight research digest. Theme: the harder the verification, the more you can hand the loop; soft verification keeps a human in the loop.

- [Brian Armstrong](https://x.com/brian_armstrong/status/2070670644577280109) — 2026-06-27: Coinbase's playbook for keeping AI spend flat while token usage grows: better defaults (experimenting with cheaper open-weight models like GLM 5.2 / Kimi 2.7 via an LLM gateway, since 91% never hit caps), better routing (frontier for planning, cheaper for execution), better caching (LibreChat cache-hit rate 5% → 60%), lean context, and usage visibility. Cut AI spend nearly in half while token usage kept growing.

- [Prajwal Tomar](https://x.com/prajwaltomar_/status/2070545372880245179) — 2026-06-27: Pro tip framed around the author's promotional "Hermes Agent" article: rather than just reading an article, paste it into an agent session and tell it to update itself, read the playbook, and set up whichever features help your workflow. Thesis: articles are becoming playbooks your agent runs for you. Heavy self-promotion / engagement framing.

- [Brady Long](https://x.com/thisguyknowsai/status/2070445026233172314) — 2026-06-27: Promo-styled writeup of MemPalace, an open-source local AI memory tool (49K stars). Instead of dumping everything into semantic search, it organizes memory into a structured "palace" (people/projects as wings, topics as rooms, verbatim text in searchable drawers). Claims 96.6% retrieval recall on LongMemEval with zero LLM/API/cloud, 98.4% with a hybrid pipeline; ships 29 MCP tools and auto-save hooks for Claude Code. Python 3.9 + ChromaDB, ~300MB, MIT.

- [Jason Weston](https://x.com/jaseweston/status/2070117091521204521) — 2026-06-25: Paper announcement ("Autodata", arXiv:2606.25996): agentic data creation as a way to convert increased inference compute into higher-quality model training data. Claims gains on CS, legal, and math problems over classical synthetic-data methods, plus a way to meta-optimize the data-scientist agent so it produces even stronger data. Thread (1/6).

- [Nav Toor](https://x.com/heynavtoor/status/2069773963413340297) — 2026-06-25: Listicle-styled promo for MinerU, an open-source document-extraction tool (68.5K stars) from Shanghai AI Lab's OpenDataLab. Reads PDFs/Office docs/scanned images into clean Markdown with reading-order text, tables → HTML, equations → LaTeX, OCR, 109 languages, batch mode, and 10k-page docs via sliding window. CLI, Python SDK, or web app; plugs into Claude Desktop, Cursor, LangChain, LlamaIndex, etc. Apache-2.0-based license, free.

- [Akshay](https://x.com/akshay_pachaar/status/2069769689560187027) — 2026-06-25: Breakdown of "loop engineering" (opening on a Karpathy quote about removing yourself as the bottleneck): a trigger decides what runs, the loop is the maker, a separate checker grades output (a model grading itself just justifies its work), and state lives on disk not context (suggests Zep's Graphiti temporal knowledge graph). Two failure points: set the exit condition before the loop runs, and add observability on the harness since the checker only catches in-run failures (suggests Comet's Opik). Thesis: the model is a commodity; the loop around it is where the engineering lives.

- [Matthew Berman](https://x.com/matthewberman/status/2069098257444434425) — 2026-06-23: Matthew Berman announces a new Loop Library feature, Lazy Loops (aka Discover), which scans your codebase and chat threads to find potential agentic loops and designs them for you. Links the Forward-Future/loop-library GitHub repo of practical, repeatable AI-agent workflows.

- [Ethan](https://x.com/lambethethan/status/2068958764276051987) — 2026-06-23: Ethan describes a personal wiki of ~1,000 supplements built from 150k papers and 200k health-influencer mentions, and floats handing the entire dataset to an AI agent next.

- [冬天](https://x.com/seventhoce56019/status/2068901168940745088) — 2026-06-23: Translated from Chinese: a writeup of reverse-skill (GitHub zhaoxuya520/reverse-skill), an AI skill package that puts reverse-engineering and security tasks behind a routing.md file so the agent self-triages across 20+ sub-skills (APK reversing, IDA static analysis, JS frontend reversing, firmware security, EDR evasion, vulnerability exploitation). Framed as lowering the barrier to security offense/defense.

- [Sakana AI](https://x.com/sakanaailabs/status/2068862070062485867) — 2026-06-23: Sakana AI announces Fugu, an orchestration model that routes across a swappable pool of underlying agents rather than relying on one monolithic model. Their blog argues orchestration is the next frontier and a hedge for AI sovereignty against vendor export controls; Fugu reportedly matches leading models (Fable, Mythos) on engineering, science, and reasoning benchmarks.

- [Movez](https://x.com/0xmovez/status/2068763235587694769) — 2026-06-23: Movez highlights an Andrew Ng talk on building self-improving agentic systems from scratch, quoting Ng that AI agents now handle 100% of his tasks and that self-improving loops will replace prompting within 3-6 months. Quote-tweets his own article on a 300-agent swarm running on Kimi K2.6 verified by Opus 4.8. Heavy promotional framing.

- [Avi Chawla](https://x.com/_avichawla/status/2068657496936616314) — 2026-06-23: Avi Chawla explains why BM25, a 30-year-old keyword ranking algorithm with no training or embeddings, still powers Elasticsearch/OpenSearch and excels at exact-match retrieval where embeddings struggle, making hybrid (BM25 + vector) search the default in top RAG systems. He closes on the UX problem of highlighting which span actually drove a semantic match, pointing to his co-founder's article.

- [Codez](https://x.com/0xcodez/status/2064374643729773029) — 2026-06-23: A long-form Loop engineering roadmap arguing the leverage point in agentic coding has moved from writing prompts to designing self-running loops. Covers the 4-condition test for when a loop is worth building (task repeats, automated verification, token budget, senior-engineer tooling), the five building blocks (automations like /loop and /goal, git worktrees, skills, MCP connectors, sub-agents), the maker/checker split, the Ralph Wiggum quiet-failure mode, comprehension debt and cognitive surrender, and the security tax of unattended loops. Cites Anthropic engineering docs and Addy Osmani.

- [Viv](https://x.com/vtrivedy10/status/2066954487466459163) — 2026-06-17: Viv amplifies Sydney Runkle's X article 'The Art of Loop Engineering,' which argues reliable agents need more than a good model — they need a carefully engineered hierarchy of loops. Viv's key takeaway: verification is a critical primitive; it's worth spending days to weeks making the distribution of desired agent outcomes verifiable in practice by your system, especially for non-slop, semi-long-horizon work.

- [Hasan Toor](https://x.com/hasantoxr/status/2066247422502957197) — 2026-06-15: Highlights Headroom, a GitHub tool by Netflix engineer Tejas Chopra that compresses everything an AI agent reads before it reaches the LLM (tool outputs, logs, files, RAG chunks, code-search results, conversation history), claiming 60-95% fewer tokens for the same answers. Ships as a Python/TypeScript library, local proxy, and MCP server, with wrappers for Claude Code, Codex, Cursor, Aider, and Copilot.

- [Teknium](https://x.com/teknium/status/2066185784332562605) — 2026-06-15: Demo: the author used the Hermes Agent with a Manim video-generation skill plus its TTS tool to autonomously produce a video explaining the Hermes Agent itself — a self-referential showcase of composing a skill and a tool inside an agent.

- [Olivia Chowdhury](https://x.com/oliviacoder1/status/2066064093552038070) — 2026-06-15: Hype-framed thread on a Dec 31, 2025 MIT CSAIL paper that claims to 'solve' AI memory not by building bigger context windows but by teaching models how to read/retrieve — positioning the result against the industry's context-window arms race and the 'context rot' problem, where a model's performance on information already in context degrades as more is packed in.

- [Harry Tandy](https://x.com/harrytandy/status/2065818850633932996) — 2026-06-14: Opens with a Sam Altman quote that the cost to use a given level of AI falls ~10x every 12 months, then lays out a 10-step agentic-coding sprint: pick the heaviest backlog item, write a FABLE_RUN.md spec (goal/scope/commands/review rules/done criteria), map the repo first, break the job into checkpoints that each end with diff + test output + next decision, split builder and checker agents, use git worktrees for parallel attempts, and keep a RUN_LOG.md of every failed command and accepted fix.

- [Avid](https://x.com/av1dlive/status/2065747876005937416) — 2026-06-14: Promotes a 'second brain' pattern attributed to Karpathy: let an LLM maintain a wiki of your notes so knowledge compounds as you dump sources and it reads, links, and files them. Points to a free Claude Code plugin, claude-obsidian by AgriciDaniel (claude plugin marketplace add AgriciDaniel/claude-obsidian; claude plugin install claude-obsidian@agricidaniel-claude-obsidian), then run /wiki inside an Obsidian folder. Quote-tweets the author's own article on building Obsidian from scratch with 13+ Kimi agents.

- [Avi Chawla](https://x.com/_avichawla/status/2065727218991735000) — 2026-06-13: Explains 'loop engineering' (framed with a Karpathy quote about removing yourself as the bottleneck and maximizing leverage): move the operator's two manual jobs — deciding what the agent runs next and checking its output — into the system itself. A schedule decides what to run, a maker loop produces the work, a separate checker agent grades the output, and a file on disk holds the shared state both read; the loop runs until done, max iterations, or budget is exhausted.

- [Marie Haynes](https://x.com/marie_haynes/status/2065531158356717721) — 2026-06-13: Flags Google's new Open Knowledge Format (OKF): a standardized way to store information as a directory of interlinked markdown files that acts as a living wiki agents can query and edit, which the author thinks could replace Notion or Obsidian. References Google Cloud's blog post and the spec at github.com/GoogleCloudPlatform/knowledge-catalog (okf/SPEC.md), and notes feeding both links to Antigravity to brainstorm project uses.

- [Suryansh Tiwari](https://x.com/suryanshti777/status/2065473893817848266) — 2026-06-13: Claims Anthropic released an official Claude Code plugin, claude-code-setup, that scans your project and recommends and sets up hooks, skills, MCP servers, subagents, and automations step-by-step (install: /plugin install claude-code-setup@claude-plugins-official), arguing most people run Claude Code vanilla and miss the surrounding ecosystem. Quote-tweets the author's own 'Unveil' build. (Treat the 'official' claim as unverified.)

- [Codez](https://x.com/0xcodez/status/2065097407965127142) — 2026-06-12: Hype-framed thread claiming an Anthropic 'Managed Agents' team demo showing how to build self-improving agent systems with the Fable 5 model from scratch in ~13 minutes, using /loops, dynamic workflows, and 'dreaming.' Quote-tweets the author's own 14-step article on the same. (Strong engagement-farming framing; claims unverified.)

- [hoeem](https://x.com/hooeem/status/2065098599751471454) — 2026-06-11: Quote-tweets his own long-form X article 'Why you should not be looping & what to do instead' — a contrarian breakdown pushing back on the popular agentic self-looping pattern (taking aim at a 'leading voice in AI') and proposing alternatives. The substance is in the linked article; framing is deliberately provocative.

- [Nainsi Dwivedi](https://x.com/nainsidwiv50980/status/2064947761779208476) — 2026-06-11: Alibaba open-sourced 'open-code-review' (Apache-2.0), the internal AI code reviewer that's run on their codebase for ~2 years — 20,000+ engineers, 1M+ reviews. Design: deterministic engineering handles what must never fail (file selection, bundling, rule matching, comment positioning) while the LLM only does context reading, codebase search, and reasoning. Claims ~1/5 the token cost of a generic agent + skills and precise line-level comments that don't drift on large changesets. Repo name: open-code-review.

- [Boris Cherny](https://x.com/bcherny/status/2064426115255730578) — 2026-06-11: Boris Cherny (Anthropic / Claude Code) on why self-verification loops matter: letting a model check its own work lets it run autonomously for much longer and land closer to your intent, so you check in less. Points to a breakdown by @delba_oliveira (via @ClaudeDevs) on encoding your manual checks so Claude Code closes its own feedback loop.

- [Paweł Huryn](https://x.com/pawelhuryn/status/2064201950980096078) — 2026-06-09: Lists six patterns for Anthropic-style dynamic agent workflows/loops: classify-and-act (one agent decides type, code routes), fan-out-and-synthesize (per-piece agents merged in code), adversarial verification (separate rubric-checker), generate-and-filter (many candidates → dedupe → survivors), tournament (judges compare different attempts), and loop-until-done (spawn until a stop condition). Each with a concrete example. Links his 'Claude Dynamic Workflows' guide.

- [BOOTOSHI](https://x.com/kingbootoshi/status/2063999432077795579) — 2026-06-09: Long personal write-up: BOOTOSHI claims the agent-orchestrating-subagents pattern (token-maxxing across parallel work) was right for opus-4.5/gpt-5 but is no longer optimal with the newer generation (gpt-5.5, opus-4.8). Argues the extended context window + intelligence means these models are now more capable as a single 'MEGA THREAD' with a single operator. Counter-trend to the multi-agent enthusiasm of early 2026.

- [Peter Yang](https://x.com/petergyang/status/2063988122720055772) — 2026-06-09: Five takeaways from a conversation with @kunchenguid (ex-Meta L8 engineer) on agentic engineering: (1) plan and validate, don't code yourself — you're the always-on team's manager; (2) plan quality determines how long agents run autonomously — a detailed spec can run for hours vs minutes for a one-liner; (3) use visual plans, not walls of markdown — Lavish (github.com/kunchenguid/lavish) generates visual HTML plans; (4 and 5 truncated in scrape — likely about validation rubrics and feedback loops).

- [Rahul](https://x.com/sairahul1/status/2063544956158185927) — 2026-06-08: Long-form X article framing 'Harness Engineering' as the most important AI discipline of 2026 — OpenAI shipped 1M lines of production code in Feb 2026 using agents wrapped in a reliable system (the 'harness'); Anthropic published 3 papers on it; ThoughtWorks formalized a framework; Philipp Schmid called it the most important discipline of 2026. Article walks through what a harness is and the mental models needed to actually use it. 1.1M views — the term is breaking out of AI-infra circles fast.

- [Rahul](https://x.com/sairahul1/status/2063609922667815064) — 2026-06-07: Rahul follow-up to his Harness Engineering article: points to walkinglabs.github.io/learn-harness-engineering as 'the best site on the internet to learn harness engineering' — free, comprehensive. Most AI engineers haven't heard the term yet. Worth bookmarking alongside his article.

- [Viv](https://x.com/vtrivedy10/status/2063429138304668093) — 2026-06-07: A default recipe for optimizing Agent = Model + Harness, 'training' both: (1) build v1 on a sensible base harness with task-specific prompting/tools, (2) harness-engineer against prod-like eval tasks (often enough on its own), (3) SFT on mined traces or synthetic data (good for distilling a cheaper model), (4) RL if you can design environments/rewards to push past SFT copying, (5) light harness engineering again on the trained model. Argues harness engineering will be the dominant optimization lever and most companies are still at steps 1-2; links the 'Anatomy of an Agent Harness' article.

- [Hanako](https://x.com/hanakoxbt/status/2063305395687522702) — 2026-06-07: Describes an Anthropic 'dreaming agents' memory pattern: a second set of agents that, after you log off, reopen every session, fact-check the first agents, merge duplicates and burn stale memory — up to 100 at once, ~95% cached so a full rewrite costs almost nothing. Points to a multi-agent code/review/deploy team guide.

- [Sprytix](https://x.com/sprytixl/status/2063234969510588640) — 2026-06-07: Engagement-farmed hype ('170 AI agents make every company decision') pushing a listicle on running 170–300 parallel agents with Kimi K2.6. Clickbait framing, but the underlying topic — massed parallel agents for research/ops — is real.

- [海拉鲁编程客 (hylarucoder)](https://x.com/hylarucoder/status/2062881239900766292) — 2026-06-06: Recommends Peter Pang's 'Building cloud agent infrastructure' — most agent frameworks assume a desktop (one user, one machine, local filesystem, keys in env vars); cloud agent infra changes those assumptions.

- [Cat Wu (Anthropic)](https://x.com/_catwu/status/2062408623565984209) — 2026-06-06: Anthropic's data team automated ~95% of business-analytics queries with Claude; the linked blog covers their approach to skills, data foundations, evals, ablations, and online validation for data-analysis agents.

- [hoeem](https://x.com/hooeem/status/2062443798647517197) — 2026-06-04: Points to a guide on making agentic workflows ~100x cheaper by fixing token waste in the orchestration loop.

- [さいぺ (cipepser)](https://x.com/cipepser/status/2062397559520502225) — 2026-06-04: Praises mem0's 'State of Memory in Agent Harness' survey — well-organized coverage from field papers/benchmarks through memory implementations in each coding agent (Cursor, Devin, Claude Code, Codex).

- [Ole Lehmann](https://x.com/itsolelehmann/status/2061911202830401564) — 2026-06-04: A ~10-minute recipe to turn your X bookmarks into an agent-queryable second brain: export bookmarks (twitter-web-exporter / BookmarkSave), drop the file into your LLM wiki or Obsidian vault, and have your agent convert each into a tagged markdown note with the original link — then query across the whole pile. Directly relevant to this link collection.

- [Thariq](https://x.com/trq212/status/2061907538741006796) — 2026-06-03: Announces dynamic workflows as the biggest Claude Code upgrade since skills and subagents — Claude writing its own task-specific harness on the fly — with excitement about the non-technical tasks it unlocks.

- [Thariq](https://x.com/trq212/status/2061907337154367865) — 2026-06-03: Full Anthropic article on dynamic workflows in Claude Code: Claude writes its own JavaScript harness to spawn/coordinate subagents (own models, own worktrees, resumable), countering agentic laziness, self-preferential bias and goal drift. Covers patterns (fan-out-and-synthesize, adversarial verification, tournament, loop-until-done), many use cases (migrations, deep research, triage, root-cause, evals, model routing), the 'ultracode' trigger, token budgets, and when NOT to use it.

- [Garry Tan](https://x.com/garrytan/status/2061878212213572083) — 2026-06-03: Garry Tan on model routing as strategy: frontier labs will want their harness to be the moat, but the consumer-best outcome is model capabilities flattening and commoditizing — 'a preview of the AI Harness Wars of 2027.' Cites Factory's auto model-router (claimed 25% cost cut at frontier performance).

- [Tom Dörr](https://x.com/tom_doerr/status/2061674811122713013) — 2026-06-03: Shares FlowForge, a Skill that generates professional draw.io diagrams from natural language (github.com/wentong2022-arch/flowforge-skill).

- [darkzodchi](https://x.com/zodchiii/status/2061040686330257656) — 2026-05-31: Anthropic-engineer clip: build 5 focused agents (code review, tests, docs, security) in an afternoon, each ~15 minutes as a markdown file with instructions + prompt. Links a beginner subagent-building template.

- [恒星](https://x.com/vintcessun/status/2060897802478293013) — 2026-05-31: DeepMind packaged 30+ scientific databases (AlphaGenome, UniProt) into agent skills. The real bottleneck for science agents isn't model quality but knowing how to call databases correctly; skills turn each DB's API into clear instructions + scripts so agents execute step-by-step. One-line npx install (github.com/google-deepmind/science-skills).

- [Chesny](https://x.com/chesnyfcb/status/2060818732654481693) — 2026-05-31: Polemical pitch (translated) for a 3D 'knowledge galaxy' second brain à la Karpathy: 378 notes auto-generated ~1,854 nodes and ~3,856 connections, surfacing hidden links and missing connections. Pragmatic takeaway: start with an automated Obsidian + Claude vault that extracts content, finds connections, and writes daily reports.

- [0xSero](https://x.com/0xsero/status/2060128492247740640) — 2026-05-29: Recommends Peter Steinberger's 'Just Talk To It — the no-bs Way of Agentic Engineering' (steipete.me): after trying every elaborate workflow, the author keeps returning to a conversational, no-ceremony way of working with coding agents rather than heavy prompting scaffolds.

- [Rohit Ghumare](https://x.com/ghumare64/status/2060072412868235587) — 2026-05-29: Summarizes Mike Piccolo's argument that a harness isn't one thing but ~15 separate concerns (turn state machines, provider routing, credential vaults, policy engines, approval gates, budget trackers, context compaction, session trees, tracing) bundled by frameworks out of necessity. When each layer is a worker on a shared bus with a typed contract, 'build your own harness' means swapping a worker, not forking a framework.

- [Yohei](https://x.com/yoheinakajima/status/2060068279574843614) — 2026-05-29: Yohei Nakajima's 'log-centric agent architecture' and his first arXiv paper 'The Log is the Agent: Event-Sourced Reactive Graphs for Auditable, Forkable Agentic Systems' — the case for agents that coordinate through persistent, replayable state.

- [Charly Wargnier](https://x.com/datachaz/status/2059649544854327466) — 2026-05-29: Recommends Akshay Pachaar's 47-minute 'Hermes Agent Masterclass' on building self-improving, 24/7 local autonomous agents — self-evolving skills, three-tier memory, GEPA optimization, scaling from 1 to 10 agents.

- [Muratcan Koylan](https://x.com/koylanai/status/2059753045060395240) — 2026-05-28: On the 'Agent Harness Engineering: A Survey' paper (CMU/Yale/JHU/Amazon; 170+ projects reviewed): real-world agent performance = model capability + harness quality, and for long-horizon production tasks the harness is the main bottleneck. Simple harness tweaks (tool formats, sandboxing, verification loops) yield big benchmark gains; the biggest wins come from turning production traces into regression tests + automated harness fixes.

- [Kyle Jeong](https://x.com/kylejeong/status/2059753008297394245) — 2026-05-28: Browser agents have an 'amnesia problem' — re-discovering each site from scratch every run. Autobrowse uses iterative AutoResearch to let an agent improve its own browser skills (/autobrowse), reportedly up to 90% faster and cheaper.

- [John Yeo](https://x.com/johnyeo_/status/2059688796728267261) — 2026-05-28: Describes an in-house agent that automatically queries logs and investigates support tickets — with billing state/history making each case stateful. Links a build writeup.

- [Rahul](https://x.com/sairahul1/status/2059632149716942923) — 2026-05-28: Hype-framed ('Anthropic just released the blueprint for a company run by Claude Code; work is dying') push for a listicle on building a SaaS MVP in an afternoon with 7 AI agents. Clickbait wrapper over a real multi-agent build walkthrough.

- [Paul Iusztin](https://x.com/pauliusztin_/status/2059613089260003387) — 2026-05-28: Breakdown of Neo4j's graph-native agent memory: three connected layers in one graph — short-term (ordered message chain), long-term (entity/relationship knowledge graph with embeddings, traversed relationally), and reasoning memory (per-run trees of thoughts/tool-calls/decision paths). Typed edges (:MENTIONS/:INITIATED_BY/:TOUCHED) make provenance a one-hop query; 'the ontology is the real product.'

- [Avi Chawla](https://x.com/_avichawla/status/2059556157984006187) — 2026-05-28: Clear explainer of RAG vs Graph RAG vs Agentic RAG as solving different query types: standard RAG for single-hop factual lookups, Graph RAG (LLM-extracted entities/relationships + traversal) for multi-hop connections, Agentic RAG (an agent choosing tools/sources at query time) for dynamic multi-source tasks — plus binary quantization for 32x more memory-efficient vector search.

- [darkzodchi](https://x.com/zodchiii/status/2059603103070945391) — 2026-05-27: Boris Cherny (Claude Code): 'we stopped fixing Claude's mistakes; we made Claude fix them itself.' Links a copyable setup for having Claude Code catch, fix, and learn from its own errors instead of the write-code/tests-fail/explain loop.

- [Rohit](https://x.com/rohit4verse/status/2059366212501696609) — 2026-05-27: A Databricks tech lead's talk on the unglamorous core of multi-agent: agents fail not because the model is dumb but because nothing coordinates them — one agent is a feature, fifty is a distributed-systems problem, and getting hundreds of agents to share one coherent brain is the whole game.

- [Movez](https://x.com/0xmovez/status/2059346354984612126) — 2026-05-27: An Anthropic engineer's 37-minute masterclass on shipping production agent teams: three building blocks (brain=persona, hands=environment, sessions), a server-side loop so nothing breaks on refresh, and why agents 'die before production.' Links a 10-step multi-agent build guide.

- [Binfeng Xu](https://x.com/billxbf/status/2059323616009838703) — 2026-05-27: Release of Polar, Agent-RL rollout infrastructure that takes real-world harnesses (Codex, Claude Code, OpenClaw, Hermes, or your own) directly as training environments with no code change — find a problem, design the harness, train your own agents.

- [Vaishnavi](https://x.com/_vmlops/status/2059207888393138556) — 2026-05-27: Microsoft open-sourced an Agent Governance Toolkit: deterministic interception of every tool call (denied actions structurally impossible), a YAML allow/deny/human-approval policy engine, zero-trust identity (SPIFFE/DID/mTLS), a 4-level execution sandbox, tamper-evident Merkle audit logs, coverage of all OWASP Agentic Top-10 risks, and support across major frameworks and languages — because 'follow the rules' in a prompt is a suggestion, not a guardrail.

- [darkzodchi](https://x.com/zodchiii/status/2058928613987160287) — 2026-05-25: Boris Cherny (Claude Code): 'every night I have a few thousand agents running,' monitored from his phone. Links a piece arguing the next wave is a team of agents in a real chat app where they @mention each other, delegate, and remember — versus one sandboxed, memoryless ChatGPT tab.

- [Hasan Toor](https://x.com/hasantoxr/status/2058863173462352313) — 2026-05-25: Engagement-framed tool share: an open-source engine claiming to replace agent harness, queues, sandboxing and APIs with three primitives (TypeScript/Python/Rust, Docker-ready, 15k+ stars).

- [Shubham Saboo](https://x.com/saboo_shubham_/status/2058269167372153129) — 2026-05-24: Positions codebase-as-queryable-graph as the real 'context engineering' for coding agents — turning any codebase into an interactive graph the agent can query; works with Claude Code, Codex, Antigravity; fully open-source.

- [Kevin Simback](https://x.com/ksimback/status/2058262328496554021) — 2026-05-24: A definitive guide to memory in the Hermes Agent, structured as a 3-layer stack: Layer 1 native (two always-injected markdown files MEMORY.md/USER.md plus a searchable SQLite session DB; the 80% consolidation 'rule' is a prompt instruction, not code), Layer 2 the pluggable MemoryProvider slot (8 official providers — Honcho, Mem0, Hindsight, Holographic, OpenViking, RetainDB, ByteRover, Supermemory — one at a time, each a different architectural bet), and Layer 3 community plug-ins (GBrain, Mnemosyne, etc.). Closes with how to pick and warning signs a memory layer is too heavy.

- [Viv](https://x.com/vtrivedy10/status/2057673225702937059) — 2026-05-22: An agent-orchestration heuristic Viv finds works in nearly every case: 'bossman supervisor >> external judge >>> self reflection.' A fresh judge (no prior context) beats self-review, but best is a supervisor orchestrating a series of Claudes — the main agent shouldn't think it's doing the work; it should be critically judging and correcting its workers.

- [swyx](https://x.com/swyx/status/2057559570177007912) — 2026-05-22: swyx is building a skill to turn a vibecoded 'slop' app into a production-ready, e2e-tested, maintainable, parallelizable agent repo — one run went ~16 hours and 103 commits, ending with the same app but a codebase he can build on.

- [Mnimiy](https://x.com/mnilax/status/2057551699204857930) — 2026-05-22: Reports that Anthropic engineers kept repeating 'let it cook' at Code with Claude London (Boris Cherny, Ravi Trivedi, Katelyn Lesse): stop micromanaging prompts, write the routine, let Claude prompt itself — 'routines are higher-order prompts; the runtime is shipped; the prompts are the bottleneck.' Links 9 tested Claude Cowork prompt-templates.

- [BOOTOSHI](https://x.com/kingbootoshi/status/2057528772208034195) — 2026-05-22: Shares an S+-tier skill, directional-prompting (outcome-first + directional language, a two-layer approach), combined with /goal mode — 'agents thrive on positive communication; make the path to success clear.'

- [Alex Veremeyenko](https://x.com/alex_prompter/status/2057476020454949201) — 2026-05-22: Anatomy of the perfect SOUL.md identity file for AI agents — the file an agent reads first. Nine sections: Identity, Values, Communication Style, Expertise, Boundaries, Workflow, Tool Usage, Memory Policy, Example Interactions. 'Be helpful and professional' describes nothing; strong files have real opinions, specific limits, and concrete examples; 200-500 words, shorter = sharper.

- [aditya](https://x.com/adxtyahq/status/2057410759236386866) — 2026-05-22: A worked answer to a Google L5 interview question — 'design a RAG pipeline for 10M docs with zero hallucination': ingest/normalize, hybrid retrieval (BM25 + embeddings), ANN + reranking, source-confidence scoring, constrained generation, citation-backed responses, hallucination fallback, continuous evals, caching, and observability. At scale, retrieval quality matters more than the frontier model.

- [Viv](https://x.com/vtrivedy10/status/2056993505386622987) — 2026-05-20: Notes on designing LangSmith Engine for customer-scale data: give the agent autonomy AFTER good tooling (around interacting with LangSmith); agents are good at pulling in context selectively, so the job is helping them self-facilitate routing useful info into the window.

- [Arpit Bhayani](https://x.com/arpit_bhayani/status/2056946273165656375) — 2026-05-20: Argues long-running agentic systems need reliability/fault-tolerance, and that teams accidentally rebuild distributed workflows (cron + queue + state + retries → state machines, idempotency, compensating actions). An essay on Temporal, an open-source durable-execution engine (Workflows, Activities, event histories, replay, Signals, retries, determinism) as the plumbing for agents that need state and execution that survives failures.

- [CyrilXBT](https://x.com/cyrilxbt/status/2056933229924372546) — 2026-05-20: ALL-CAPS hype ('ANTHROPIC JUST KILLED THE DEMO AGENT ERA') about Anthropic's Agents team showing a production-grade four-layer framework for multi-agent systems in a 30-minute video. (The quoted article is mismatched — about turning Obsidian into a personal OS.)

- [Tom Blomfield](https://x.com/t_blom/status/2056909934156280088) — 2026-05-20: Tom Blomfield breaks down what YC is seeing in recursively self-improving companies — creating recursive self-improving AI loops so founders 'run companies that improve while they sleep.'

- [Alex Hillman](https://x.com/alexhillman/status/2056904462162133233) — 2026-05-20: Reframes tmux as an agent superpower: it lets agents manipulate your terminal sessions — read logs from any pane/window, answer prompts in interactive CLIs, send keys into TUIs and capture the screen, and run subagents in separate windows to inspect their output.

- [Yohei](https://x.com/yoheinakajima/status/2056848954848104488) — 2026-05-20: Yohei Nakajima on ActiveGraph, a 'continuity layer for long-running agents' — a novel agent architecture drawing on older designs, promising for self-improving agents via the ability to fork and diff agent runs.

- [Greg Ceccarelli](https://x.com/gregce10/status/2056771029867933884) — 2026-05-20: Field notes on a 'goal engineering' workflow: instead of prompts/specs, write two checked-in markdown artifacts per round — a 'goal' capped at 4,000 chars (matching Codex's /goal limit) and an unbounded 'rider' with ~11 phases and named depth tests — authored via a Skill. Aimed at long-running agentic turns.

- [elvis](https://x.com/omarsar0/status/2056764334181884158) — 2026-05-20: 'Code as Agent Harness' — a 100+ page survey of methods and applications of code-as-harness, arguing it may be key to a science of harness engineering, and that future systems must be executable, inspectable, stateful, and governed.

- [Lotte](https://x.com/lotte_verheyden/status/2056754091817361670) — 2026-05-20: 'Evals, explained' (Langfuse Academy): offline eval sits between running an experiment and shipping. Three methods — manual review (build intuition + ground-truth labels), code-based (deterministic checks: schema, keywords, length, SQL executes), and LLM-as-a-judge (language-understanding qualities, needs calibration against human labels). Prefer binary pass/fail over 1-5 scales; one evaluator per quality; start manual then automate repeatable checks.

- [Ronan Berder](https://x.com/hunvreus/status/2056742771386638454) — 2026-05-20: Pushback on Spec-Driven Development: agents are faster at writing code and (some) humans are better at system thinking, but humans suck at planning. Argument: you can't sit down, write all the specs upfront, and then write code — experienced engineers know that doesn't work. Quote-tweets a now-unavailable @iamsahaj_xyz post.

- [Garry Tan](https://x.com/garrytan/status/2056711154224034125) — 2026-05-20: Garry Tan on dynamic, just-in-time skills for personal AI: 'markdown is code,' and the agent can change its own skills when new cases appear — 'just-in-time personal software is the most powerful idea of 2026.' A reply notes skill bundles carrying their own tests that the agent modifies in-flight create the compounding effect.

- [Amar Singh](https://x.com/amarsvs/status/2056484487891243355) — 2026-05-19: 'Agent Performance: Model-Bound vs Harness-Bound' — counterintuitively, smarter models make harnesses matter MORE ('the smarter the model, the more expensive it is to waste its intelligence'). Model-bound tasks (hard math/proofs) hinge on raw capability; harness-bound tasks (e.g., Terminal-Bench, ~10 pts spread for Opus 4.7 across harnesses) hinge on prompting, tools, context management. As traces balloon and costs rise, the harness becomes the 'scheduler for intelligence'; author's open-source HALO optimizes harnesses from traces.

- [AVB](https://x.com/neural_avb/status/2056462216430535062) — 2026-05-19: Notes that people are now training local recursive language models inside python REPLs with RL — agents divide-and-conquer long problems and pass context around as python variables. Links 'Recursive Agent Optimization using RL, explained clearly.'

- [Aakash Gupta](https://x.com/aakashgupta/status/2056405221908394406) — 2026-05-19: Aakash Gupta on Pawel Huryn's six-item CLAUDE.md 'routing table' (project description, file-structure map, identity context, knowledge routing, workflow pointers, and a 3-line self-improving prompt), with everything else in on-demand files/folders. The paste-ready self-improving prompt: review existing rules/hypotheses, apply confirmed rules, then update them from feedback each session.

- [Paul Iusztin](https://x.com/pauliusztin_/status/2056272402414211175) — 2026-05-19: Calls Neo4j's open-source 'agent-memory' the best repo for a unified graph-based memory layer for AI agents — strong modeling of short/long/reasoning memory, ontology, and extraction algorithms; full write-up on decodingai.com.

- [Viv](https://x.com/vtrivedy10/status/2056066419360743479) — 2026-05-18: Viv on LangSmith Engine as an always-on self-improvement loop: tracing on for every agent, purpose-built SmithDB for agent-scale data, ambient intelligence over every trace to find errors/insights, and PRs/Evals generated with human gating — the first sparks of company-wide Continual Learning for agents.

- [AYi](https://x.com/ayi_ainotes/status/2055954675526934642) — 2026-05-18: Enthusiastic (Chinese) take on Garry Tan's GBrain — 'not another RAG toy' but a complete personal-knowledge OS with 8 layers (vs the usual 4): install on OpenClaw/Hermes/Claude Code to remember relationships, decision trajectory, and long-term cognitive evolution, turning per-chat starts into lifelong memory + self-evolution. Garry's production ran 17,888 pages / 4,383 people / 723 companies.

- [Vaishnavi](https://x.com/_vmlops/status/2055887618303570151) — 2026-05-18: Recommends walkinglabs.github.io/learn-harness-engineering as the best site to learn harness engineering.

- [Vasilije](https://x.com/tricalt/status/2055876832797581406) — 2026-05-18: 'Memory isn't a plugin. Skills aren't a plugin. They're the same harness' — both are a world model (everything the agent uses to predict its next action). Memory observes the world; skills (SKILL.md procedures) codify it into rules and degrade silently without an Observe→Inspect→Amend→Evaluate loop. Cognee stores skills and memory in one graph so a skill is a traceable, evolving memory node.

- [santi](https://x.com/santtiagom_/status/2055751665345798628) — 2026-05-18: Praises an OpenAI article on Harness Engineering and Codex — how they used agents to build an internal ~1M-line product: preventing agent-generated code from degrading, using tests/CI as more reliable constraints than prompts, keeping code/docs readable for agents, and how engineers' work changes when agents program.

- [nader dabit](https://x.com/dabit3/status/2055319214202777894) — 2026-05-15: 'Agent Hooks: Deterministic Control for Agent Workflows' — hooks attach handlers to lifecycle points (SessionStart, UserPromptSubmit, PreToolUse, PostToolUse, Stop, SessionEnd) so scripts/tests/policy run every time instead of relying on the model to remember. Operating model: event → matcher → handler → outcome. Rule of thumb: 'always/never/block/record/run/verify' belongs in a hook. Includes a demo and per-runtime notes (Claude Code, Codex, Cursor, Devin); layer prompts (guidance) with hooks (controls), CI, and human review.

- [Ole Lehmann](https://x.com/itsolelehmann/status/2055290989577753034) — 2026-05-15: Listicle of 9 personal-AI-assistant workflows the author would build on Hermes if starting from zero: Daily Brief (calendar+emails+weather+headlines to Telegram at 7am), self-improving Viral Swipe File (auto-extracts hooks/structure/stats from above-threshold posts), Trending Workflows Radar (scans Reddit/X/AI forums daily), and six more. Practical patterns for personal automation.

- [Arpit Bhayani](https://x.com/arpit_bhayani/status/2055265636390207784) — 2026-05-15: Deep dive on what production-grade RAG actually requires beyond demos: how retrieval actually works, why chunking is where most systems fail, embedding-model lock-in, reindexing, document registries and chunk identity, index updates/deployments, retrieval tracing and observability. Argues production RAG failures are operational, not LLM, failures.

- [Khairallah AL-Awady](https://x.com/eng_khairallah1/status/2055215784092401966) — 2026-05-15: Thread about Anthropic's May 6, 2026 multi-agent orchestration announcement (Code with Claude event): Claude Managed Agents can now run up to 20 specialized agents in parallel on a single task. Cites Netflix (parallel build-log analysis), Harvey (multi-document legal coordination), and Shopify (pushing toward 90% autonomous coding by Q3 2026) as production users. Good signal that parallel sub-agent orchestration is going mainstream.

- [CyrilXBT](https://x.com/cyrilxbt/status/2055183411619549265) — 2026-05-15: ALL-CAPS engagement-farming thread announcing GitHub's new official certification GH-600 "Agentic AI Developer" — framed as the first formal credential for engineers who operate, supervise, and integrate AI agent teams across the SDLC. Worth knowing the cert exists; treat the framing as hype.

- [Meenakshi Yadav](https://x.com/meenakshiyacs/status/2055104295641710718) — 2026-05-15: Generic agentic-AI architecture "cheat sheet" listing the standard layer stack: goal definition, orchestration, agents, tools, memory, monitoring, reliability (retries/HITL), and governance. No new ideas — useful as a one-slide overview to hand a junior or non-engineer.

- [Sam Hogan](https://x.com/samhogan/status/2055064462844219603) — 2026-05-15: Sam Hogan introduces HALO (Hierarchical Agent Loop Optimizer) — github.com/context-labs/halo — which uses Reasoning Language Models to let the model itself shape its own agent harness rather than hard-coding it. Inspired by @a1zhang's "Mismanaged Genius Hypothesis" (LLMs are smarter than the harnesses humans design for them). Reports consistent 10%+ benchmark improvements across multiple evals.

- [Avid](https://x.com/av1dlive/status/2054948286403150017) — 2026-05-15: Promo for a live 15-minute lecture by two Airbnb Senior Staff Engineers on agentic coding in 2026 — Airbnb already shipped one of the most ambitious LLM-agent migrations in production. Quote-tweets Avid's May 12 article "How to Build AI Agents in 2026 (Full Course)" (527.6K views). Worth watching for real production agentic-coding patterns from a company that has actually done the migration.

- [Berryxia.AI](https://x.com/berryxia/status/2054924976835510337) — 2026-05-15: Translated-from-Chinese thread breaking down Tencent's newly open-sourced AI agent memory system (6 months of work). Highlights three techniques: real-time compression of expired context (cuts token usage 61%), Mermaid-syntax structured task maps that keep 30+ step workflows on track, and a long-term memory tier. Argues most teams over-index on context-length and under-invest in memory architecture.

- [Petra Donka](https://x.com/petradonka/status/2054897826149101588) — 2026-05-15: Argues agents doing judgment-heavy work need feedback loops, not perfect prompts — because no static prompt covers everything as the product/users/team's taste evolves. Walks through Warp's experience building an agent for their Developer Experience team that responds to Warp mentions on Twitter/Reddit and learns from team feedback over time.

- [Rohit Ghumare](https://x.com/ghumare64/status/2054625511897489423) — 2026-05-14: Argues agent codebases that survive past month six do so because the architecture makes the wrong shape harder to write than the right one — not because the team is disciplined. Cites a 'Mike' post listing four canonical month-six failures: shared mutable defaults across agents, tool fns that swallow any string and return None, session memory poisoned by LLM-extracted strings, and multi-agent setups passing the parent's full context. Aligns with the Anthropic/Glean harness-is-the-backend debate.

- [divyansh tiwari](https://x.com/divyansht91162/status/2054430633645293687) — 2026-05-14: Highlights a paper called NanoResearch proposing an agent architecture with three co-evolving layers — Skill Bank (turns repeated actions into reusable expertise), Memory Layer (preserves project + user experience across sessions), Policy Learning (turns free-form feedback into permanent behavioral updates). Pitch: an agent that accumulates experience and aligns to the user over time rather than relying on bigger context windows.

- [Geek Lite](https://x.com/qingq77/status/2054056472477307084) — 2026-05-14: Oh My Hermes (github.com/Salomondiei08/oh-my-hermes) is a skills+workflow layer for the Hermes Agent that ships 20 skills covering the full app lifecycle (requirements through monitoring/GitHub ops) and 5 role-specialized agents (CTO/PM/Dev/QA/Ops) collaborating on a kanban board. Treats Hermes as primary operator and Claude Code/Codex as optional accelerators — a concrete prior art for our skills + sub-agent architecture.

- [Ihtesham Ali](https://x.com/ihtesham2005/status/2054458335215395223) — 2026-05-13: Google + Meta paper: Claude Code autonomously proposes, tests, and refines algorithms for improving LLM reasoning over 5 rounds with no human in the loop. Discovers a 4-mechanism controller (EMA momentum stopping, coupled width-depth control, alignment-aware depth allocation, conservative branch abandonment) for $39.90 total compute. Paper at arxiv.org/abs/2605.0xxx.

- [ericosiu](https://x.com/ericosiu/status/2054413343776223393) — 2026-05-13: ericosiu hiring forward-deployed engineers globally. Quotes Aaron Levie noting FDEs (or equivalent) are about to become one of the most in-demand jobs in tech for AI rollouts. References a "beat AI" challenge in his profile as their filter. Subject flagged "worth an extra look".

- [GREG ISENBERG](https://x.com/gregisenberg/status/2054261832718889216) — 2026-05-13: Free 47-minute course on building a managed AI-agent business solo. Pitch: sell "unlimited agents/infrastructure" as digital employees, don't niche too early, every executive has the same problems (emails, meetings, follow-ups). Stack: Hermes Agent (harness), Codex or Claude Code (build), Orgo (cloud computer sandboxes per agent), Composio (one-click auth), Obsidian (docs).

- [Joseph Viviano](https://x.com/josephdviviano/status/2054253118943363506) — 2026-05-13: Joseph Viviano's "Agentic Research Best Practices" — 15 months of notes on using coding agents in research workflows (with Mila Quebec collaborators). Key argument: research codebases differ from product engineering — no users, active development, speed bound by intelligibility to author/collaborators, not throughput. Many "best practices" from product engineering feel archaic in research.

- [Charly Wargnier](https://x.com/datachaz/status/2054225085100151163) — 2026-05-13: Charly Wargnier hyping a Rohit article "What to Learn, Build, and Skip in AI Agents (2026)" — invokes Karpathy line that 90% of AI advice dies in 6 months. Signal-vs-noise framing for agent tooling, but very engagement-bait copy.

- [Rahul](https://x.com/sairahul1/status/2054171777119801764) — 2026-05-12: Hypes a 22-minute Anthropic talk on production AI agents covering tool orchestration, memory systems, observability, long-running agents, and production infrastructure. Pitches a personal "How to Become an AI Agent Engineer in 2026" roadmap pushing back on CrewAI-by-default and framework chasing.

- [Garry Tan](https://x.com/garrytan/status/2053538847795880414) — 2026-05-11: Garry Tan riffs on a Finbarr take — "code as memory": work with an agent non-deterministically the first time to figure out a task (research + write a script), then execute that script on every future repetition. Quote-tweets his own Apr 22 article on stopping agents from making the same mistakes (LangChain context).

- [Garry Tan](https://x.com/garrytan/status/2053127519872614419) — 2026-05-10: Long-form X article "Meta-Meta-Prompting: The Secret to Making AI Agents Work" — Garry Tan argues to stop treating AI as a chat window and start treating it as an OS. Part of his Fat Skills/Fat Code/Thin Harness series. Open source: github.com/garrytan/gbrain and github.com/garrytan/gstack. Concrete "book mirror" example uses sub-agents per chapter that map ideas to your actual life context. 1.2M views.

- [Tom Dörr](https://x.com/tom_doerr/status/2052552468983103608) — 2026-05-08: Tom Dörr highlights agentic-data-scientist (github.com/K-Dense-AI/agentic-data-scientist) — an open-source self-correcting agent for complex data-science tasks. Worth a look as a benchmark for self-correction patterns.

- [ani](https://x.com/anirudhbv_ce/status/2052532004919361958) — 2026-05-08: Provocative paper 'The Geometry of Consolidation' (github.com/niashwin/geometry-of-consolidation): claims only ~3% of dimensions in major embedding models (91/3072 for OpenAI text-embedding-3-large, 80/3072 for Gemini gemini-embedding-001) do real work, the rest is mathematically empty. Argues RAG compression has a hard floor no algorithm can beat, set by a spectral number the embedding model can't escape — and that this is the root cause of RAG hallucinations. Big claim, worth reading the paper before believing.

- [Avi Chawla](https://x.com/_avichawla/status/2052482874126020882) — 2026-05-08: Avi Chawla on Karpathy's 'remove yourself as the bottleneck' framing and Rowboat — an open-source AI 'second brain' built on the Markdown/Obsidian foundation Karpathy uses, extended to work context (emails, meetings, decisions, commitments). The pitch: most people can't act on Karpathy's advice because their AI has no memory of their work, and Rowboat is one open-source answer to that.

- [divyansh tiwari](https://x.com/divyansht91162/status/2052474052841984110) — 2026-05-08: TinyFish drops web search to $0 for AI agents. divyansh switched OpenClaw and Hermes agents to it and reports they can now browse, research, and retrieve live info at scale for free — a real shift in agent-cost economics if it holds up.

- [Tom Dörr](https://x.com/tom_doerr/status/2052440598452359394) — 2026-05-08: Tom Dörr surfaces 'agentmemory' (github.com/rohitg00/agentmemory) — a knowledge-graph memory layer for Claude Code. Pair with the other agent-memory tools in the corpus (HelixDB, turbovec, mem0).

- [darkzodchi](https://x.com/zodchiii/status/2052400272840720565) — 2026-05-08: Hype-style pointer to a 22-minute Anthropic Claude team talk on their 2026 agent roadmap — tools, memory, observability, builder-state-of-the-art. Last 3 minutes called out as especially worth watching. Quote-tweets the author's own article on agent reliability (AI agent breaking at 2am, sending 47 broken emails over the weekend, burning $340 in API calls).

- [Millie Marconi](https://x.com/milliemarconnni/status/2052363436575826398) — 2026-05-08: Millie Marconi highlights Feynman (github.com/getcompanion-ai/feynman) — an open-source MIT-licensed agent system with four bundled roles (Researcher, Reviewer, Writer, Verifier) that reads papers, audits referenced code, and replicates experiments. Runs in Docker for safe local execution and spins up serverless GPUs on Modal or persistent pods on RunPod. Indexed session search across past research runs, inline citation-URL verification.

- [Rohit Ghumare](https://x.com/ghumare64/status/2052313902214476192) — 2026-05-08: Rohit Ghumare highlights agentmemory — a memory layer for Hermes / Claude Code / Codex that records session observations, compresses them with AI, and injects relevant context back into future sessions. Claims 95% fewer tokens per session and 200x more tool calls before hitting context limits, benchmarked on 240 real coding sessions. MIT-licensed, ~1,000 GitHub stars in its first week. Worth evaluating as a CLAUDE.md alternative for long-running agent work.

- [Kanika](https://x.com/kanikabk/status/2052032420954927357) — 2026-05-08: Kanika points to a 424-page 'Agentic Design Patterns' guide written by a senior Google engineer — every chapter ships working code, all Amazon royalties go to Save the Children, $40 print price. Engagement-bait framing ('bookmark before it's buried') but the reference itself is a real, comprehensive resource.

- [Tom Dörr](https://x.com/tom_doerr/status/2052150733261193390) — 2026-05-07: Tom Dörr points to awesome-foundation-agents (github.com/FoundationAgents/awesome-foundation-agents) — a curated reading list of papers mapping foundation-agent cognition. Reference, not actionable.

- [Adam Ghowiba](https://x.com/adamghowiba/status/2050886233921061281) — 2026-05-05: JP Morgan's investment research team broke down their "Ask David" multi-agent architecture: a supervisor agent orchestrates specialized subagents (retrieval, structured data, analytics), with an LLM-as-judge reflection node before the answer ships and human-in-the-loop for the last accuracy gap. Same supervisor + specialist + reflection pattern showing up everywhere.

- [Blaze](https://x.com/browomo/status/2050509770604331510) — 2026-05-02: French teenager built a 3D map of 217 mental models (1284 connections) controlled by hand gestures + voice, running Three.js + MediaPipe Hands + local Whisper + Claude API + Google Antigravity. Whole stack assembled in one weekend; 80ms gesture-to-graph latency, runs from a 47MB Obsidian vault on a regular laptop.

- [Muhammad Ayan](https://x.com/socialwithaayan/status/2050484688968724820) — 2026-05-02: Pointer to github.com/warpdotdev/warp — Warp terminal's source has been published as 'an agentic development environment, born out of the terminal.' Worth a look as a coding-agent shell.

- [Om Patel](https://x.com/om_patel5/status/2050441119003971683) — 2026-05-02: Promoted Claude Code skill /graphify that pre-builds a graph of your codebase (functions, deps, docs, PDFs, images, audio, video via Whisper) so Claude doesn't waste tokens exploring. Author claims '71.5x more efficient' (engagement-farming framing).

- [Tom Doerr](https://x.com/tom_doerr/status/2050312101504094651) — 2026-05-02: Points to a curated GitHub list on AI agent evolution, memory systems, and self-improvement (github.com/EvoMap/awesome-agent-evolution) — a reference index for the self-improving-agent literature.

- [Dan Shipper](https://x.com/danshipper/status/2050235671466606665) — 2026-05-02: Dan Shipper recommends Marcus's 'definitive guide' on how a PM can ship product with coding agents at Every: every.to/guides/ai-product-management-guide. Pitched as required reading for non-engineer builders.

- [regent0x](https://x.com/regent0x_/status/2050143341656838449) — 2026-05-02: Story (likely embellished) about a solo Chinese dev billing $320k/yr by orchestrating 5 specialized Claude agents in parallel: architect, coder, reviewer, tester, ops. Each agent has its own context, no shared state. Engagement-y framing but the parallel-specialist pattern is real.

- [Mike Bespalov](https://x.com/bbssppllvv/status/2049924037111841027) — 2026-05-02: Refero.design publishes 2000 DESIGN.md files (colors, type, spacing, layouts) extracted from the world's best products, structured for an LLM to read so coding agents stop producing ugly UIs. Free at styles.refero.design.

- [Xiangyi Li](https://x.com/xdotli/status/2049903693143609627) — 2026-05-02: Short endorsement — 'must read for everyone who wants to reduce the entropy of their agentic systems' — pointing at evals/environments work (benchflow_ai). Framing: disciplined evals as the way to tame nondeterminism in agent systems.

- [Teknium](https://x.com/teknium/status/2050098631907434871) — 2026-05-01: Teknium ships a /goal command in NousResearch hermes-agent (PR github.com/NousResearch/hermes-agent/pull/18262) — supervisor-loop pattern inspired by ralph loops + Codex's upcoming /goal: keeps re-prompting the agent until the supervisor judges the task complete.

- [How To AI](https://x.com/howtoai_/status/2049567036003795269) — 2026-04-30: Tencent's Training-Free GRPO claims to replace expensive RL fine-tuning by extracting the 'semantic advantage' from trial-and-error and injecting it as a 'token prior' / memory rather than updating weights — reportedly trained for $18. Hype-framed ("killed fine-tuning") but the underlying technique is a notable alternative to GRPO/RLHF that avoids overfitting and GPU costs.

- [Akshay](https://x.com/akshay_pachaar/status/2049476617144287719) — 2026-04-30: Akshay rebuilt 'OpenClaw' core in a single Sim Studio workflow (25 blocks, 29 connections, short+long-term memory, Telegram+Slack channels) without manual coding — pitched as an 'OS for your AI workforce.' Stack is open-source and self-hostable: github.com/simstudioai/sim

- [Aparna Dhinakaran](https://x.com/aparnadhinak/status/2047849364547420382) — 2026-04-28: Aparna Dhinakaran (Arize) on harnesses converging on similar context-passing problems — letting the agent decide context dynamically. Quote-tweets Aran Komatsuzaki on Anthropic's forked subagents (introduced Apr 23, 2026): forked subagents can inherit the same context as the main agent, useful when richer context matters more than minimal context. Direct relevant to the bossman-supervisor concept.

- [Edouard Reinach](https://x.com/ereinach/status/2047802558136058258) — 2026-04-28: Edouard Reinach points to Predict-RLM (github.com/Trampoline-AI/predict-rlm) — production-ready implementation of an MIT memory technique. Quote-tweets a hype-framed (questionable) summary of a Dec 31 2025 MIT CSAIL paper claiming they solved AI memory by 'teaching it how to read' rather than building a bigger brain. The repo is the actionable bit; the quoted framing is sales pitch.

- [Hasan Toor](https://x.com/hasantoxr/status/2047637109343928827) — 2026-04-28: Hasan Toor points to future-agi (github.com/future-agi/future-agi + app.futureagi.com) — open-source end-to-end platform for evaluating, observing, and improving production AI agents. Nightly release; stable coming. Worth evaluating alongside other agent-observability tools.

- [Yasir Ai](https://x.com/aiwithyasir/status/2047589529650176333) — 2026-04-28: Hyped pitch ('Breaking', 'terrifying how good') for GitNexus — a knowledge-graph engine for codebases using Tree-sitter AST parsing. Maps every function call, import, class inheritance, interface; clusters code by cohesion; runs blast-radius analysis before changes; coordinates rename across files. MCP-compatible with Claude Code, Cursor, Windsurf. Engagement framing but the underlying capability is interesting.

- [Eric Clemmons](https://x.com/ericclemmons/status/2047838932369387914) — 2026-04-25: Eric Clemmons: 'Brilliant.' Quote-tweets Teddy Riker's 'Designing for Agents' article — anti-engagement-noise reflective piece (opens with 'If you spend time in the same corner of X as I do, scrolling past the How I built a second brain with Obsidian and Anthropic just KILLED [insert industry] FOREVER posts...').

- [Ethan Mollick](https://x.com/emollick/status/2047828327856030047) — 2026-04-25: Ethan Mollick: 'Organizational design for agents is hard, benchmarking agents working in concert is hard. Together, this is the next critical frontier for making AI matter in economically valuable tasks, and we really don't know very much about it.' Quote-tweets @krishnanrohit's essay 'Aligned Agents Still Build Misaligned Organisations.'

- [Atal](https://x.com/zabihullahatal/status/2047692175019008019) — 2026-04-25: Engagement-framed ('BREAKING') summary of 'Agent Behavioral Contracts' paper — applies Design-by-Contract (preconditions, invariants, governance rules, recovery mechanisms) as runtime constraints on AI agents instead of prompt-only control. Tested across 1,980 sessions. Real concept (formal verification meets agent runtime) worth tracking under the agents-as-judges concept thread.

- [Tom Dörr](https://x.com/tom_doerr/status/2047258779821949384) — 2026-04-23: Tom Dörr points to CORAL (github.com/Human-Agent-Society/CORAL) — infrastructure for multi-agent self-evolution. Worth a look as a research substrate for agents-that-improve-themselves work.

- [Akshay](https://x.com/akshay_pachaar/status/2047220248081015110) — 2026-04-23: Akshay extends Karpathy's wiki idea: a markdown wiki works for static knowledge but breaks for multi-entity questions like 'which authors moved from Google to Anthropic between 2022-2024 and what did they publish after?' A wiki can only answer that if someone already wrote the article; a graph (entities + relations + dates) lets you ask any variation directly. Argues the next step beyond LLM-maintained wikis is LLM-maintained knowledge graphs.

- [How To AI](https://x.com/howtoai_/status/2047187640781541882) — 2026-04-23: [Post unavailable — page doesn't exist]

- [TRAE](https://x.com/trae_ai/status/2047145274200768969) — 2026-04-23: TRAE's 'Definitive Guide to Harness Engineering' X article — frames harness engineering as the 2026 successor to prompt + context engineering. Term coined by Mitchell Hashimoto (HashiCorp co-founder); gained traction via an OpenAI report. Horse-and-reins metaphor: AI Agent = SOTA Model (wild horse) + Harness (control system) = Elite Performer. Foundational reading for the harness-engineering concept thread alongside Rahul/walkinglabs/Anthropic papers.

- [Shiv](https://x.com/shivsakhuja/status/2047124337191444844) — 2026-04-23: Shiv on 'Skill Graphs 2.0' — composing skills into a graph (markdown + scripts) where skills depend on other skills (e.g., draft-marketing-email depends on graphic-design). The original skill-graph idea got traction; the v2 wrinkle is that agents stop reliably calling skills past a certain graph depth. Worth tracking alongside Pocock's /teach skill, Akshay's Claude Code 12 features, and the general skills-as-reusable-routines concept.

- [Shrey Pandya](https://x.com/shreypandya/status/2047100550446280792) — 2026-04-23: Shrey Pandya introduces the /autobrowse skill (inspired by Karpathy's autoresearch harness). Pattern: agent explores a web task via the @browserbase CLI, learns from previous attempts' failures, iterates until it converges on a reliable workflow. Once token usage is optimized, the winning approach 'graduates' into a reusable skill. Direct reference for the let-it-cook / routines-as-higher-order-prompts concept.

- [ClaudeDevs](https://x.com/claudedevs/status/2047086372666921217) — 2026-04-23: Anthropic ClaudeDevs blog post: 'Building agents that reach production systems with MCP' (claude.com/blog/building-agents-that-reach-production-systems-with-mcp). Covers when agents should use direct APIs vs CLIs vs MCP, patterns for building MCP servers, context-efficient client design, and pairing MCP with skills. Direct first-party reading for any agent-to-production pipeline work.

- [Matt Van Horn](https://x.com/mvanhorn/status/2047073560267817469) — 2026-04-23: Matt Van Horn endorses Compound Engineering v3 (Trevin Chow's project, ~15k stars) — names brainstorm and plan artifacts that give requirements a paper trail from idea to commit, harness alignment across the build. Worth a real evaluation as a methodology framework alongside harness engineering.

- [Mario Zechner](https://x.com/badlogicgames/status/2047055760236916759) — 2026-04-23: Mario Zechner: 'recommended reading.' Quote-tweets @walden_yan's 'Multi-Agents: What's Actually Working' — a 10-months-later follow-up to his earlier 'Don't Build Multi-Agents' essay. The two-essay arc is worth reading together: an evolving view from a thoughtful critic of multi-agent overreach.

- [Vida](https://x.com/vida_agent/status/2047007924279767332) — 2026-04-23: Vida open-sourced OpenChronicle (github.com/Einsia/OpenChronicle) — a local-first memory layer for tool-capable LLMs and agents, framed as a free alternative to OpenAI Chronicle's $100/mo paywall. Fits the agent-memory infrastructure concept thread.

- [Garry Tan](https://x.com/garrytan/status/2046882636069798323) — 2026-04-23: Garry Tan: 'Basically how I'm building all my features these days: Do it once in OpenClaw, then just run /skillify and it does it like that forever.' Quote-tweets his own article on stopping agents making the same mistakes (contrasts with LangChain's $160M/3yr/LangSmith trajectory-evals stack). Fits the skills-as-routines thread.

- [Shubham Saboo](https://x.com/saboo_shubham_/status/2046473615118672325) — 2026-04-21: Shares agentic-stack — 'One brain, many harnesses. Portable .agent/ folder (memory + skills)' — a pattern for sharing a single memory/skill store across multiple agent harnesses. Repo: github.com/codejunkie99/agentic-stack.

- [Tech with Mak](https://x.com/technmak/status/2046414820241760620) — 2026-04-21: Summary of Meta's REFRAG paper: compresses retrieved RAG chunks into single embeddings (16,384 tokens → 1,024 chunk embeddings), delivering 30.85x faster time-to-first-token, zero perplexity loss, 16x context extension (4K → 64K), and 3.75x better than prior SOTA. Exploits sparse attention patterns in RAG contexts via precomputable embeddings and RL-based compression policy.

- [Tom Dörr](https://x.com/tom_doerr/status/2046369616411185635) — 2026-04-21: Shares a recursive self-improving agent harness (github.com/greyhaven-ai/autocontext) — an agent scaffold designed to iterate on and improve its own context/behavior.

- [Sydney Runkle](https://x.com/sydneyrunkle/status/2046277232537256002) — 2026-04-21: LangChain team piece on 'The runtime behind production deep agents' — distinguishing the harness (prompts, tools, skills, model loop) from the runtime (durable execution, memory, multi-tenancy, observability). Walks through production requirements for agents and how LangSmith Deployment + Agent Server package those capabilities. Reference architecture for shipping agents in production.

- [Sigrid Jin](https://x.com/realsigridjin/status/2046266374948069387) — 2026-04-21: Quote-tweet of Junghwan Na's writeup — Na got his GitHub banned after pushing 500+ commits across 100+ open-source repos in 72 hours using an AI harness. Sigrid pulls out the two highest-leverage principles from Na's method: (1) reproduce the bug locally or drop it, (2) read merge history instead of CONTRIBUTING.md. Jeremy flagged 'worth extracting a skill' — these are skill-worthy contribution-harness patterns.

- [Raymond Weitekamp](https://x.com/raw_works/status/2046240194999755153) — 2026-04-21: Long-form X article 'RLMs are the new reasoning models': Recursive Language Models let a root model treat its own prompt as an environment it inspects/slices/recursively subqueries via a REPL, collapsing reasoning and tool use into one inference abstraction and processing inputs orders of magnitude beyond the context window. Traces the reasoning-vs-tool-use history (CoT, ReAct, Toolformer, o1) and the Oolong/LongMemEval/LongCoT benchmark arc where RLM scaffolds post leading numbers — including small models (Qwen3-8B/27B) jumping well past their base, hinting the frontier stops being GPU-rich-only. Flags cost/time and 'models are bad at acting recursively' as open limits.

- [Ihtesham Ali](https://x.com/ihtesham2005/status/2046197374855582157) — 2026-04-21: Writeup of George Pólya's 1945 book 'How to Solve It' — the four-step problem-solving framework (understand, plan, execute, look back). Central heuristic: if you can't solve the proposed problem, solve a simpler related one first. Jeremy's note 'important for planner?' — relevant for AI agent planning/decomposition patterns.

- [Akshay](https://x.com/akshay_pachaar/status/2046151867177308181) — 2026-04-20: Akshay summarizes Google DeepMind's 'AI Agent Traps' paper — the first systematic framework for adversarial content engineered to hijack AI agents browsing the web. Maps six attack surfaces: Content Injection (perception: invisible CSS, hidden HTML, steganographic payloads in images — HTML injections hijack web agents in up to 86% of scenarios), Semantic Manipulation (reasoning: biased framing weaponizing cognitive biases), Cognitive State Traps (memory: RAG poisoning, long-term memory corruption), plus three more not visible in the truncated scrape. High-priority reading for anyone building agents that browse arbitrary web content.

- [Kenneth Auchenberg](https://x.com/auchenberg/status/2045940742678368570) — 2026-04-20: Kenneth Auchenberg highlights an article arguing that in the "harness era" of AI agents the harness is the application and the sandbox is the server, framing swarms as harnesses managing harnesses.

- [Garry Tan](https://x.com/garrytan/status/2045427057656729985) — 2026-04-19: Garry Tan launches GBrain v0.11 with "Minions," a BullMQ-style queue/jobs system built on Postgres/PGLite to make OpenClaw/GBrain subagents faster and more reliable instead of timing out.

- [Akshay](https://x.com/akshay_pachaar/status/2045404494641733962) — 2026-04-18: Akshay summarizes a UCL paper (arXiv:2604.14228) dissecting Claude Code's architecture: only 1.6% of the codebase is AI decision logic while 98.4% is operational harness (permission gates with 7 modes, tool routing, a 5-layer context compaction pipeline, subagents that return only summaries). Core thesis: as frontier models converge on raw coding ability, harness quality, not the model, becomes the differentiator.

- [Alex Ker](https://x.com/thealexker/status/2045203785304232162) — 2026-04-18: Alex Ker's deep-dive guide on optimizing AI coding harnesses: keep config/.md files lean and human-written (frontier LLMs hit a "dumb zone" past a few hundred instructions), use progressive disclosure for CLIs/skills/MCP tools, structure prompts with HumanLayer's Research-Plan-Implement (R.P.I.) framework, and use subagents (parallel fan-out for breadth, pipelines for depth) to keep the main context clean. Core argument: the harness, not the model, is where engineering judgment compounds, so commit to one and iterate.

- [Daniel Miessler](https://x.com/danielmiessler/status/2045148852047827449) — 2026-04-18: Daniel Miessler recommends Interceptor (by Ronald Eddings) as the best browser-control system for AI agents he's used out of 100+, now the highest-value addition to his PAI harness.

- [Kevin Simback](https://x.com/ksimback/status/2045120939680038923) — 2026-04-18: Kevin Simback shares his article "The AI Agent Moat Is Real, but Narrower Than You Think," arguing that the durable moat in the agent space isn't the harness itself but lies elsewhere, after going deep on where to invest and build in the agent space.

- [Eric Hartford](https://x.com/quixiai/status/2044952124568527298) — 2026-04-18: Eric Hartford releases Clearwing, an MIT-licensed open-source vulnerability-discovery engine that reproduces Anthropic's "Project Glasswing" results with any LLM. His argument: the real innovation isn't the gated Claude Mythos model but the model-agnostic pipeline, rank files by attack surface, fan out hundreds of file-scoped agents, use crash oracles (AddressSanitizer/UBSan) as ground truth, and run a verification agent to filter noise. Reproduced findings with OpenAI Codex 5.4 and a Qwen3.5 finetune.

- [Alter Ego](https://x.com/alterego_eth/status/2045093809886020058) — 2026-04-17: Alter Ego promotes Nous Research's Hermes Agent, a self-hosted agent that writes its own skills after each task, keeps persistent memory (MEMORY.md/USER.md/SQLite), and runs 24/7 on a VPS with a closed learn-improve loop every ~15 tool calls, using it to build a self-learning Polymarket weather-trading bot. Heavy promotional/profit framing.

- [0xSero](https://x.com/0xsero/status/2044879665001595263) — 2026-04-17: 0xSero (quote-tweeting Sarah Chieng's article 'Single-agent AI coding is a nightmare for engineers') says he's gone 180 on multi-agents/subagents after analyzing hundreds of AI coding agent sessions — they actually help a lot. Practitioner's change-of-mind about orchestration.

- [Hamudi](https://x.com/hamudinaanaa/status/2044872907072164304) — 2026-04-17: Hamudi ties into Sequoia's "$1T thesis" that AI sells outcomes (work) rather than software tools, introducing "Outcome Primitives" as a way to measure economic outcomes, citing a published paper tracking 1,300 agents over 21 days that created $32M in value (jobs secured, $200k grants won, e-commerce shops shipped). Framing: copilots compete on software margins and lose to big labs; outcome engines compete on services margins.

- [Garry Tan](https://x.com/garrytan/status/2044479509874020852) — 2026-04-15: X article: "Resolvers: The Routing Table for Intelligence" — argues resolvers (context-routing rules: when task X appears, load document Y first) are the most important but invisible component of agent systems. Follows up on "Thin Harness, Fat Skills" framework. 21K views.

- [GitHub Projects Community](https://x.com/githubprojects/status/2044453433743458686) — 2026-04-15: Tool share: Graphify (osp.fyi/graphify) turns any folder of code into a queryable knowledge graph instantly — code-as-graph for agent/dev navigation and retrieval.

- [Yoonho Lee](https://x.com/yoonholeee/status/2044442372864700510) — 2026-04-15: Released code for Meta-Harness — a method to autonomously improve LLM evaluation harnesses on problems humans are actively working on, solving long-horizon credit assignment over code, traces, and scores. Repo at github.com/stanford-iris-lab/meta-harness with ONBOARDING.md for agent-guided setup.

- [Shann³](https://x.com/shannholmberg/status/2044413638388363272) — 2026-04-15: Built a 230-page Obsidian knowledge base (tweets, bookmarks, articles, notes) and connected it to every AI agent project using qmd (Tobi Lütke's tool) with hybrid BM25+vector search and LLM re-ranking. Any agent in any project now searches this global wiki before brainstorming or planning.

- [Akshay](https://x.com/akshay_pachaar/status/2044329897603244093) — 2026-04-15: Akshay argues agent memory is three-dimensional, needing a relational store for provenance, a vector store for semantics, and a graph store for relationships, because flat vector search misses multi-hop connections (the "bridge" fact that links two entities). He points to Cognee, an open-source project that unifies all three behind four async calls (default embedded SQLite+LanceDB+Kuzu, swappable for Postgres/Qdrant/Neo4j).

- [Europurr](https://x.com/vrloom/status/2044314974101877175) — 2026-04-15: Europurr reports switching from OpenClaw to Nous Research's Hermes agent and setting up its "Hindsight" memory, calling it light-years ahead of OpenClaw.

- [Garry Tan](https://x.com/garrytan/status/2044291663213015491) — 2026-04-15: Garry Tan releases GBrain v0.10.0, packaging his personal OpenClaw "brain" for others: refined RESOLVER.md and SOUL.md, ACLs for multi-user brain access, and 24 distinct "fat" skills shipped with e2e tests, evals, and unit tests.

- [Shaw (spirit/acc)](https://x.com/shawmakesmagic/status/2044269097647779990) — 2026-04-15: Shaw shares a reusable prompt for cleaning up "vibecoded" codebases by spawning 8 parallel subagents, each owning one cleanup task: DRY/dedup, consolidating shared types, removing unused code (knip), untangling circular deps (madge), replacing weak types (any/unknown), stripping needless defensive try/catch, removing legacy/fallback paths, and cutting AI-slop comments. Each subagent researches, writes a critical assessment, then implements high-confidence fixes.

- [mr-r0b0t](https://x.com/mr_r0b0t/status/2044199154004472009) — 2026-04-15: Amplifies a tip on a 3-tool agent web stack: SearXNG for candidate source discovery, Firecrawl for known-URL scraping, Camofox for JS/interaction browser fallback. Described as essential for any agent doing web search or scraping.

- [klöss](https://x.com/kloss_xyz/status/2044169678961234282) — 2026-04-15: klss argues agents fail across repos because of unstructured markdown, and proposes a four-folder convention to remove ambiguity: /audits (proof), /docs (description), /plans (intent), /specs (law). Separating intent from proof from law stops Claude Code, Codex, and Cursor agents from hallucinating context.

- [Paul Bakaus](https://x.com/pbakaus/status/2044118871326765541) — 2026-04-15: Paul Bakaus praises Matt Sims (English PhD plus ML/startup background) for building in the open at the intersection of creativity, storytelling, and AI. Quote-tweets Sims on teaching Claude Code to think systematically, getting consistent answers to recurring review-for-security / sufficient-tests / update-instruction-files prompts.

- [kwindla](https://x.com/kwindla/status/2044106314612408437) — 2026-04-15: kwindla introduces Gradient Bang, claimed to be the first massively-multiplayer, fully LLM-driven game: a retro space-trading game (Factorio-like) where you cajole a ship AI into tasking other AIs. Built to explore sub-agent orchestration, partial context sharing across inference loops, long contexts and episodic memory, LLM-generated dynamic UIs, and voice input. Built on pipecat_ai plus Supabase and Vercel, fully open source.

- [Ihtesham Ali](https://x.com/ihtesham2005/status/2044056849272705246) — 2026-04-15: Aurogen is an open-source (MIT) OpenClaw fork whose differentiator is true multi-agent, multi-instance orchestration inside one deployment: modular agents/channels/providers/skills, a pure web-panel setup with no config files or CLI, ClaWHub skill imports, one-click installers, and it runs on a $50 Linux SBC (github.com/UniRound-Tec/Aurogen).

- [Amir Salihefendić](https://x.com/amix3k/status/2044046057315742146) — 2026-04-15: Amir Salihefendić (Doist) treats Jack Dorsey's recent framing as an org-design question for companies blending human and machine intelligence: remote-first, transparent, functional teams with clear DRIs, where AI increasingly supplies the 'connective tissue' that moves context across teams, tools, and decisions.

- [Indie Fox](https://x.com/indie_maker_fox/status/2043857352282255829) — 2026-04-15: Indie Fox praises a Claude skill that generates very high-quality software architecture diagrams (github.com/Cocoon-AI/architecture-diagram-generator), showing an OpenHarness architecture diagram as an example of its clean output.

- [Mario Zechner](https://x.com/badlogicgames/status/2043757216885256463) — 2026-04-15: Mario Zechner recommends Alex Volkov's article 'The Z/L Continuum — Do AI engineers even need to read code anymore?' (thursdai.news/zl), which asks how much code AI engineers still need to read in 2026 and beyond.

- [Phil Chen](https://x.com/philhchen/status/2043759400121458922) — 2026-04-14: 'How I built Filbert' — a background coding agent that is a lightweight wrapper around an existing harness running on the team's own infra with full dev-env access and recursive self-improvement. Per the linked article it wrote 95% of the team's PRs in a week and runs 14 scheduled jobs daily (bug triage, security audits, dead-code sweeps, CI optimization). Strong template for self-hosted background agents.

- [Kevin Simback](https://x.com/ksimback/status/2043745657748361476) — 2026-04-14: 'My Second Brain Setup: A Modified Karpathy Method' — builds on Karpathy's LLM-knowledge-base pattern (LLM incrementally compiles sources into an interlinked markdown wiki; LLM=programmer, wiki=codebase, Obsidian=IDE) and adds a two-author rule: an `author: kevin` vs `author: agent` frontmatter field where human-authored files are untouchable. Runs on Claude Code with five slash commands (/research fanning out 5-8 parallel agents, /ingest, /wiki-query, /wiki-lint, /wiki-output) and a 'graduation' loop that promotes good agent pages into the protected human layer.

- [Akshay](https://x.com/akshay_pachaar/status/2043745099792953508) — 2026-04-14: Akshay provides a first-principles walkthrough of agent memory: from Python lists to markdown files to vector search to graph-vector hybrids. Covers 7 failure modes of stateless agents (context amnesia, zero personalization, repeated mistakes, etc.) and builds up to a clean open-source solution for persistent agent memory.

- [Philipp Schmid](https://x.com/_philschmid/status/2043705197030002904) — 2026-04-14: Links a practical guide '8 Tips for Writing Agent Skills' — covering what kinds of skills exist, how to write them well, and when to retire one. Directly relevant to the skills/plugins workflow.

- [North@CreaoAI](https://x.com/anorth_chen/status/2043694726764003817) — 2026-04-14: Endorses (translated from Chinese) an 'AI-First' engineering essay by the author's CTO: after going AI-first, the team merges/deploys 20+ PRs daily with ~99% of production code written by AI, shipping and A/B-killing features within a day. Argument: teams stuck in 'AI-assisted' rather than 'AI-first' mode risk fading from the market within a year. Provocative management/strategy read.

- [Lorenzo Rondan](https://x.com/lorenrd/status/2043677918262395235) — 2026-04-14: Highlights Viv (@Vtrivedy10)'s diagram/mental-model of an agent harness — memory, context fragments, and the search 'bitter lesson' — calling it one of the best harness diagrams around. Pointer into the harness-design discourse.

- [Vaishnavi](https://x.com/_vmlops/status/2043624154646409708) — 2026-04-14: Vaishnavi covers Google's open-sourced Magika — an AI-powered file content type detection tool. Trained on 100M files, 200+ content types, 99% accuracy at 5ms/file. Sees through renamed malware and disguised scripts. Install via pip install magika. github.com/google/magika

- [Noisy](https://x.com/noisyb0y1/status/2043609541477044439) — 2026-04-14: Noisy describes a Google engineer who automated 80% of his work with Claude Code using a CLAUDE.md file based on Karpathy's principles and a .NET orchestration app. Covers the Karpathy-inspired CLAUDE.md, a dotnet service that spawns Claude Code instances with git worktrees, and a review pipeline. Claims $28K passive income working 2-3 hours/day.

- [Charly Wargnier](https://x.com/datachaz/status/2043246635996807300) — 2026-04-13: Charly Wargnier covers Addy Osmani's (Google) new Agent Skills package: 19 engineering skills + 7 commands for AI coding agents, based on Google best practices. Covers the full dev lifecycle — define (specs), plan (decompose), build (incremental), verify (TDD), review (security), ship (CI/CD). Aims to prevent agents from skipping quality gates.

- [Ahmad](https://x.com/theahmadosman/status/2043366810494337354) — 2026-04-12: A concise recipe for running parallel agents: either have one agent fan out or drive deterministic script runs — spin up workers, isolate each in a git worktree, gate merges with diffs, add backups/rules/logs for deterministic runs, and merge only what passes. Author is packaging it as a Skill.

- [Garry Tan](https://x.com/garrytan/status/2043339811088699446) — 2026-04-12: Garry Tan on open-source agent self-improvement: applied research now happens in the open, and 'just-in-time software' is a new paradigm. Quotes an analysis of the Hermes agent architecture taking a more explicit self-improvement route than typical offline trajectory-mining systems.

- [Nav Toor](https://x.com/heynavtoor/status/2043321909971202403) — 2026-04-12: Nav Toor covers LLM Wiki v2 — an extension of Karpathy's original LLM Wiki pattern (5K stars in 48h). Adds confidence scoring (source count, recency, contradictions), memory tiers (working/episodic/semantic/procedural), knowledge graphs with typed entities, automated hooks, and forgetting curves for knowledge decay.

- [Garry Tan](https://x.com/garrytan/status/2043198780800197025) — 2026-04-12: 'If your memory dies when your harness dies, you built the harness too thick.' Argues for thin harnesses: memory is markdown, skills are markdown, the 'brain' is a git repo, and the harness is a thin conductor that reads files it doesn't own. Endorses Harrison Chase's 'Your harness, your memory' article on harness/memory coupling and the risk of closed harnesses.

- [Garry Tan](https://x.com/garrytan/status/2042919242283258072) — 2026-04-12: Garry Tan announces GBrain's new guided integration recipes for OpenClaw and Hermes Agent setup. Addresses the struggle new users face getting integrations (mail, calendar, etc.) configured, which is needed to scale to thousands of markdown files in the knowledge base. 36.5K views.

- [Veeral Patel](https://x.com/vral/status/2042674854764130549) — 2026-04-10: Quote-tweets Ramp Labs article on "Latent Briefing" — a KV cache compaction technique for efficient memory sharing across multi-agent systems. Patel quips that passing .md files between agents will soon seem as archaic as mailing floppy disks. Paper tackles token inefficiency in hierarchical multi-agent architectures.

- [Alpha Batcher](https://x.com/alphabatcher/status/2042606770816704643) — 2026-04-10: Distills architectural principles for production AI agents by quoting Rohit's article reverse-engineering Claude Code's architecture (github.com/rohit4verse). Key patterns: async generators for streaming, parallel read-only tools vs serial write tools, tools executing during generation (not after), system prompt designed for cache efficiency, hierarchical context compaction cheapest-first, isolated worktree per sub-agent. Calls it the most detailed public breakdown of a production agent architecture available.

- [Akshay](https://x.com/akshay_pachaar/status/2042586319390674994) — 2026-04-10: Comparison of how Anthropic, OpenAI, CrewAI, and LangChain approach the agent harness differently. The one agreement: the model is not the product, the infrastructure around it is. Anthropic bets on a deliberately thin "dumb loop" harness where the model makes all decisions. OpenAI takes a similar but slightly thicker approach. CrewAI and LangChain bet on heavier orchestration infrastructure. The core architectural question: as models get smarter, do you need less infrastructure or more?

- [Vaishnavi](https://x.com/_vmlops/status/2042486942802321552) — 2026-04-10: Google open-sourced MCP Toolbox (github.com/googleapis/mcp-toolbox) — an MCP server that gives AI agents direct access to 20+ enterprise databases (Postgres, MySQL, MongoDB, BigQuery, Redis, Elasticsearch, Spanner, Snowflake) in plain English. Built-in connection pooling, auth, and OpenTelemetry. Works with LangChain, LlamaIndex, Genkit, and any MCP-compatible client. Less than 10 lines of code to integrate.

- [Sigrid Jin](https://x.com/realsigridjin/status/2042440330503733343) — 2026-04-10: Summary of "Better Harness" paper on using evals as a flywheel for agent improvement. Key insight: evals are the new training data — instead of updating weights, you update the agent harness. Warns that agents reward-hack evals, so you need strict train/test splits. Quality over quantity in eval design. The flywheel: mine prod traces for failures, turn into evals, auto-tweak prompts/tools, validate, repeat.

- [Teknium](https://x.com/teknium/status/2042396576245825543) — 2026-04-10: Teknium claims Anthropic copied their "notify when done" feature from Hermes Agent (github.com/NousResearch/hermes-agent/pull/5779) — lets background processes notify the agent when finished instead of polling, so the agent can work on other tasks in the same session. Points to Claude Code's new Monitor tool as the equivalent. Makes the case that open source moves faster than closed companies.

- [ProxySoul](https://x.com/bniwael/status/2042364421373121018) — 2026-04-10: SoulForge — an open-source AI coding agent that builds a live graph of the codebase before the agent reads any code. Uses real LSP via embedded Neovim for go-to-definition, references, and call hierarchy instead of regex hacks. Features multi-tab with cross-tab coordination where agents share context through a real-time bus, and supports mixing models (Opus, Gemini, Haiku, Ollama). Claims 1.8x faster and 2.1x cheaper than standard approaches.

- [Aakash Gupta](https://x.com/aakashgupta/status/2042334495664455848) — 2026-04-10: The "advisor pattern" for AI agent cost optimization: run Sonnet for routine execution ($3/$15 per MTok) and fire a tool call to Opus only for genuine decision points. Both models share full context, eliminating the fragmentation problem in multi-model architectures. Claude Code has been doing this internally. Practical architecture for any company hitting the cost wall with frontier models in production agent loops.

- [Seb Goddijn](https://x.com/sebgoddijn/status/2042286523001737545) — 2026-04-10: Ramp hit 99% AI adoption company-wide but found most employees stuck in chat windows while power users ran laps. They built "Glass" — an internal AI productivity suite on Anthropic's Claude Agent SDK — reaching 700 DAUs in one month. Philosophy: raise the floor for all employees rather than lowering the ceiling for power users.

- [carsonfarmer](https://x.com/carsonfarmer/status/2042038527639068763) — 2026-04-09: Points out that Anthropic's new managed agents API closely mirrors the Letta/MemGPT API that's been open-source for a year — including read-only memory blocks and memory block sharing. Quoting Sarah Wooders (Letta co-creator) who calls it closed-source with provider lock-in.

- [Aakash Gupta](https://x.com/aakashgupta/status/2041984945380585785) — 2026-04-09: Makes the case for "Team OS" — a shared GitHub repo that serves as a team's collective brain for Claude. Companies spending $200K/yr on AI seats see zero productivity gains because each person starts from scratch every conversation with no shared context. Structured context (customer calls, specs, constraints, strategy docs) compounds across the team.

- [Ashpreet Bedi](https://x.com/ashpreetbedi/status/2041966288541507861) — 2026-04-09: Ashpreet highlights @Vtrivedy10's LangChain article on auto-improving agent harnesses using evals as a hill-climbing signal. The approach formalizes iterative system improvement — build a harness, eval it, improve it automatically. Directly applicable to anyone building agentic workflows who wants systematic quality gains.

- [mr-r0b0t](https://x.com/mr_r0b0t/status/2041930298238087464) — 2026-04-09: Endorses the same LangChain article by @Vtrivedy10 on harness hill-climbing with evals. Argues that harness evolution combined with specialist local models will be the path forward for agent development.

- [Justin Brooke](https://x.com/imjustinbrooke/status/2041890745167061245) — 2026-04-09: Introduces 7 markdown files for structuring AI agent systems: SOULS.md, AGENTS.md, USER.md, TOOLS.md, MEMORY.md, HEARTBEAT.md, STYLE.md. Core thesis is "harnesses > models" — the orchestration layer matters more than which foundation model you use.

- [Sowmay Jain](https://x.com/sowmay_jain/status/2041982135305957425) — 2026-04-08: Describes using an AI agent (@laukiantonson) to fully analyze a 67GB raw genome file for $5 in compute: rented a 32-core/64GB machine, aligned 21M long reads (99.83% mapped), called 5.8M variants, phased maternal/paternal inheritance, annotated against ClinVar/PharmGKB/gnomAD, produced a health risk map across 39 conditions and drug compatibility guide for 41 medications. Striking real-world demonstration of autonomous agentic capability on complex bioinformatics tasks. Went massively viral (909K views).

- [Ashpreet Bedi](https://x.com/ashpreetbedi/status/2041568919085854847) — 2026-04-08: Ashpreet Bedi argues that building agentic software requires systems engineering discipline — you can't optimize AI agent systems by optimizing individual components. Draws parallels to Bell Labs' 1940s discovery that telephone network behavior emerged from component interactions, not individual parts. The current wave of 'harness engineering' is repeating 80-year-old mistakes.

- [Allie K. Miller](https://x.com/alliekmiller/status/2041577000804991485) — 2026-04-07: Allie K. Miller shares a 5-level 'Proactive AI-First Team Member' framework for hiring and onboarding. Levels range from 1 (not using AI) to 5 (full ownership with AI-augmented critical thinking). Key insight: most candidates interview at level 3 (solution-oriented but not action-oriented) — she wants new hires starting at level 4 (action-oriented with technical/business tradeoff awareness). Originally from @businessbarista and @stephsmithio, with AI additions by Miller.

- [Eric Siu](https://x.com/ericosiu/status/2040785346120859946) — 2026-04-06: Practical guide to deploying Jack Dorsey's 'world intelligence' concept — a company-wide AI knowledge layer that powers 50+ daily workflows, coordinates decisions across teams, and surfaces issues automatically. Includes a linked article with implementation details from 4 months of running this at his company.

- [Alex Prompter](https://x.com/alex_prompter/status/2040731938751914065) — 2026-04-06: Google DeepMind published the largest empirical study of AI agent manipulation — 502 participants across 8 countries, 23 attack types tested against GPT-4o, Claude, and Gemini. Found that websites can already detect AI agents and serve them different content, with hidden instructions in HTML, malicious commands in image pixels, and jailbreaks in PDFs. Current defenses fail in predictable, invisible ways.

- [0xMarioNawfal](https://x.com/roundtablespace/status/2040500903296352663) — 2026-04-06: Comprehensive open-source Claude Code setup with 27 agents, 64 skills, 33 commands, and built-in AgentShield with 1,282 security tests. Handles planning, code review, fixes, TDD, and token optimization. Works across Cursor, OpenCode, and Codex CLI. github.com/affaan-m/everything-claude-code

- [Ejaaz](https://x.com/cryptopunk7213/status/2040434869399138368) — 2026-04-05: Open-sourced self-improving AI agent framework: a meta-agent that autonomously tweaks an agent's harness (tools, system prompts), runs tests, and iterates until it tops benchmarks. Demonstrated on TerminalBench (code) and spreadsheets (financial modeling), reaching #1 in both domains in under 24 hours using Claude evaluating Claude for better failure analysis.

- [Charly Wargnier](https://x.com/datachaz/status/2039963758790156555) — 2026-04-03: Charly Wargnier breaks down Karpathy's new self-improving 'second brain' setup using Obsidian Markdown wikis. Instead of complex RAG, an LLM auto-compiles raw research into indexed .md files, handles its own linting and Q&A routing, and generates outputs (Marp slides, matplotlib plots) filed back into the wiki. The key insight: agents maintaining their own memory layer don't need massive context windows — just clean file organization and the ability to query their own indexes.

- [Adam](https://x.com/_overment/status/2039061635776618554) — 2026-04-02: Adam shares his personal AI system architecture based on a dynamic dependency graph with a heartbeat loop involving LLM, code, and events. Describes it as the best architecture he's found for building personal AI systems.

- [Tom Dörr](https://x.com/tom_doerr/status/2039115357839929610) — 2026-04-01: Shares an open-source AI research agent, Feynman (github.com/getcompanion-ai/feynman) — an autonomous research-assistant agent.

- [Arnav Gupta](https://x.com/championswimmer/status/2039109862919905719) — 2026-04-01: Arnav Gupta highlights a set of extensions by @nicopreme (pi-subagents, pi-messenger, pi-mcp-adapter, pi-web-access) that together create a powerful agentic system surpassing tools like Ralph, Gstack, and Conductor.

- [Vox](https://x.com/voxyz_ai/status/2038677643000758466) — 2026-03-31: Parallel module development pattern using Codex: break a project into 5 independent modules running in separate windows with a 'foreman' conductor writing to a shared doc. Each module reads the shared state, executes its part, and updates when done. Uses Claude for UI work and Codex for the rest.

- [Tom Dörr](https://x.com/tom_doerr/status/2038456589984690462) — 2026-03-30: Cisco open-sourced DefenseClaw (github.com/cisco-ai-defense/defenseclaw), a tool that scans and blocks dangerous AI agent actions. Designed as a safety layer for autonomous AI workflows.

- [Viv](https://x.com/vtrivedy10/status/2038346865775874285) — 2026-03-30: Commentary on a writeup by @systematicls about solving problems in long-running autonomous agentic engineering workflows. Key insight: all harness design is about overcoming agent laziness (cutting corners) and confusion. Solutions involve task decomposition, looping, and human-in-the-loop for underspecified tasks.

- [Daniel Miessler](https://x.com/danielmiessler/status/2038284628130492870) — 2026-03-30: 'Bitter Lesson Engineering' (danielmiessler.com): don't over-engineer your AI harness — lean on scaling/general methods rather than hand-crafted scaffolding, applying Sutton's bitter lesson to agent-harness design.

- [Meta Alchemist](https://x.com/meta_alchemist/status/2038222105654022325) — 2026-03-29: Detailed guide on turning Claude Code into a self-evolving system. The approach captures corrections across sessions so the CLI learns and improves over time, building persistent memory of what works and what doesn't for each project.

- [Tom Dörr](https://x.com/tom_doerr/status/2038137050243711042) — 2026-03-29: Shares a self-improving agent-swarm framework, Hive (github.com/aden-hive/hive) — orchestration for multiple cooperating agents that improve over time.

- [Rohit](https://x.com/rohit4verse/status/2036845273117581676) — 2026-03-26: Rohit argues top AI teams win not on model selection but on 'harness engineering' — how you design the agent's interface, manage context windows, cap search results, run linters at edit time, and maintain persistent state files. A teaser thread for an 8,000-word deep dive covering 8 actionable principles for building more reliable AI agents; key insights include: interface shapes model reasoning, context pollution is costly, and forced query refinement beats flooding with results.

- [Poonam Soni](https://x.com/codebypoonam/status/2036517669684519362) — 2026-03-25: Teaser thread claiming Anthropic demonstrated a 3-agent system that builds production-quality apps from a single prompt in under 6 hours without human intervention. Architecture details promised in thread. Engagement-farming format ('Breaking') but the underlying multi-agent app-building claim is worth verifying.

- [Factory](https://x.com/factoryai/status/2036184745059688923) — 2026-03-24: Factory launches "Missions" — long-running agentic workflows now available to all users, built to automate large software tasks like app development from scratch, codebases migrations, and AI research. Strong signal that autonomous multi-step coding agents are going mainstream.

- [George from prodmgmt](https://x.com/nurijanian/status/2035257434365976671) — 2026-03-22: George (prodmgmt.world) recounts improving his AI skills with Karpathy's Auto Research library (auto-improves prompts via repeated experimentation), using Ole Lehmann's fork turned into a skill that tunes other skills: define test inputs, write judges that score outputs, let the optimization loop run, and wake up to a better skill.

- [Matt Stockton](https://x.com/mstockton/status/2035179208872202320) — 2026-03-22: Matt Stockton argues building AI-enabled products inverts classical software engineering: the 'right way to build' changes every ~3 months, it is often better to burn the system down and rebuild than to adapt, and modern tools make that cheap — warning against sunk-cost V1 RAG systems that stuff a static context window.

- [sarah guo](https://x.com/saranormous/status/2035080458304987603) — 2026-03-22: Sarah Guo's No Priors podcast episode with Andrej Karpathy covers the phase shift in engineering, AI psychosis, AutoResearch, model speciation, jobs-market data, open vs closed models, autonomous robotics, and agentic education.

- [felpix](https://x.com/felpix_/status/2033249213614538804) — 2026-03-21: felpix reports filing taxes end-to-end with Claude + FreeTaxUSA: dropped a W-2, several 1099-NECs and 1099-Bs plus expense/budget spreadsheets in a folder, asked Claude to itemize and optimize expenses, and let it use Chrome to submit — the return was accepted. (Directly relevant: FreeTaxUSA is TaxHawk's own product.)

- [Corey Ganim](https://x.com/coreyganim/status/2034717504505823728) — 2026-03-20: Corey Ganim's playbook for running a one-person 'AI company' stacks three free tools: Paperclip (npx paperclipai — assigns work and tracks progress), gstack (15 specialist Claude Code skills from Garry Tan, with /office-hours, /review, /qa, /ship commands), and autoresearch (Karpathy — 100 overnight experiments); the move is running 10-15 gstack commands in parallel. Quotes Nick Spisak's Paperclip follow-up article.

- [Rohit](https://x.com/rohit4verse/status/2033945654377283643) — 2026-03-18: Rohit's essay 'The Harness Is Everything: What Cursor, Claude Code, and Perplexity Actually Built' argues you're not using AI wrong because of the model — you're using it wrong because you haven't built the right environment; the difference between teams shipping millions of lines and those struggling is the harness, not GPT-5 vs Claude Opus, temperature, or the prompt.

- [zostaff](https://x.com/zostaff/status/2033930728044372275) — 2026-03-18: zostaff's clickbait-titled ('How to Quit Your Job in One Day') walkthrough of an autonomous Polymarket trading system built from three agents: Claude (strategist — probability/recommendation/confidence), Codex (engineer — writes and debugs bot code), and OpenClaw (orchestrator — persistent memory, cron, modular skills, Telegram interface that executes trades and logs everything).

- [Akhilesh Mishra](https://x.com/livingdevops/status/2033845127244825041) — 2026-03-17: Akhilesh Mishra reports NVIDIA open-sourced OpenShell at GTC — an infrastructure-layer sandbox/guardrail for coding agents: filesystem locked at sandbox creation, network blocked by default with whitelisting, API keys injected only at runtime (never on disk), policies in simple YAML, running a full K3s cluster inside a single Docker container. One command sandboxes Claude Code, Codex, or Cursor; Adobe, Atlassian, Cisco, CrowdStrike, and Salesforce are integrating it.

- [Avi Chawla](https://x.com/_avichawla/status/2033797863948632384) — 2026-03-17: Avi Chawla explains the SKILLRL paper: rather than stuffing long, noisy raw trajectories into agent memory, it distills experiences into compact, reusable skills the agent retrieves and applies to future tasks — analogous to how humans turn driving experience into transferable instincts.

- [Huaxiu Yao](https://x.com/huaxiuyaoml/status/2033038170653405308) — 2026-03-15: Huaxiu Yao announces AutoResearchClaw, which automates the full research loop beyond Karpathy's autoresearch experiment loop: one message in, a full conference paper out with real experiments, verified citations, and code. It mines arXiv and Semantic Scholar (50+ papers), has three agents fight over the best hypothesis, writes and self-debugs experiment code, and pivots when results are weak — no human in the loop.

- [Garry Tan](https://x.com/garrytan/status/2032196172430131498) — 2026-03-13: Garry Tan shares a CTO's testimonial that his open-source gstack ('god mode') flagged a subtle cross-site-scripting vulnerability the team wasn't aware of, predicting 90%+ of new repos will adopt it. gstack is MIT-licensed at github.com/garrytan/gstack and installs into local Claude Code and into a repo for teammates with two pastes.

- [elvis](https://x.com/omarsar0/status/2031727864199208972) — 2026-03-12: elvis highlights EvoSkill, a self-evolving multi-agent framework that automatically discovers and refines agent skills through iterative failure analysis. Three agents (Executor, Proposer, Skill-Builder) drive the loop, with a Pareto frontier retaining only skills that improve held-out validation while the base model stays frozen. Reported gains: Claude Code w/ Opus 4.5 from 60.6%->67.9% on OfficeQA, +12.1% on SealQA, and +5.3% zero-shot transfer to BrowseComp.

- [Viv](https://x.com/vtrivedy10/status/2031411814232187109) — 2026-03-11: Viv (LangChain applied research) shares a LangChain blog taking a first-principles look at why agent harnesses exist and how they help craft good product experiences and correct model failure modes. It covers filesystems, code execution, sandboxes, context rot, and ralph loops, arguing the best harness for your model probably isn't the one it shipped with.

- [Dominik Tornow](https://x.com/dominiktornow/status/2031233587819983096) — 2026-03-10: Dominik Tornow: the new core skill in software engineering is designing feedback loops. He quotes OpenAI Developers on a small team steering Codex to open and merge 1,500 pull requests for a product used by hundreds of internal users, with zero manual coding.

- [Suhail Gupta](https://x.com/audiinidesign/status/2031213732941230240) — 2026-03-10: Suhail Gupta endorses Harrison Chase's article 'How Coding Agents Are Reshaping Engineering, Product and Design,' agreeing the EPD blur toward functional software over separate roles will only become more visible and obvious in the coming months.

- [Boris Cherny](https://x.com/bcherny/status/2031089411820228645) — 2026-03-10: Boris Cherny announces Code Review in Claude Code: when a PR opens, a team of agents runs a deep review to hunt for bugs. Built internally first because code output per Anthropic engineer is up 200% this year and review had become the bottleneck; he says it catches many real bugs he'd otherwise miss.

- [0xSero](https://x.com/0xsero/status/2030653670375751942) — 2026-03-08: 0xSero shares advice from Factory's Leo: take screenshots and videos of everything you've built, then review it. Combined with automated QA, this yields a semi-autonomous build/verify system. Links a podcast episode.

- [Daniel Miessler](https://x.com/danielmiessler/status/2030436867745923347) — 2026-03-08: Daniel Miessler flags Karpathy's new self-contained 'autoresearch' repo (nanochat training core stripped to a single-GPU, ~630-line file the human iterates on) as under-appreciated, tying it to the long-discussed goal of automating ML research and predicting it will accelerate progress again.

- [Alex Prompter](https://x.com/godofprompt/status/2030434641019072867) — 2026-03-08: Alex Prompter (co-founder @godofprompt) shares affaan-m/ECC on GitHub, described as an agent-harness performance-optimization system built around skills and instincts.

- [GitHub Projects Community](https://x.com/githubprojects/status/2030346933009821801) — 2026-03-08: GitHub Projects Community: rather than using AI to generate code directly, let it run a structured build loop — idea -> roadmap -> small tasks -> execute each task in isolation -> commit — for cleaner repos, clearer progress, and far less AI chaos.

- [Jamie Quint](https://x.com/jamiequint/status/2029951631534739951) — 2026-03-07: Jamie Quint (built Notion's early data stack in 2020) shares his article 'How to Build a Data Agent in 2026,' claiming the approach can cut a company's projected data-team headcount by ~80% this year.

- [Alex Prompter](https://x.com/alex_prompter/status/2029961559615607052) — 2026-03-06: Citing a GitHub analysis of 2,500+ repos, argues most agents.md files fail by being too vague. Top performers give each agent ONE narrow job (docs writer, test engineer, lint fixer) with specific examples — specialists beat generalists.

- [Jayden](https://x.com/thejayden/status/2029899328400109732) — 2026-03-06: Jayden recommends an article on building a "Chief of Staff" with Claude Code, calling it one of the best real-world examples of agentic systems he has seen.

- [Alexey Grigorev](https://x.com/al_grigor/status/2029829363903123636) — 2026-03-06: Argues prompting is only ~5% of AI engineering; the other 95% is making AI testable, observable, versioned and reliable in production. Core skills: evaluation/testing with golden eval sets and regression tests, plus controlled iteration via prompt versioning and experiment tracking (Git/MLflow).

- [Akshay](https://x.com/akshay_pachaar/status/2029534926828388537) — 2026-03-05: Explains the difference between MCP and Skills for AI agents — commonly conflated. MCP is a shared communication standard that replaces the N-models-by-M-tools custom-connector explosion, whereas Skills are a distinct concept.

- [Meta Alchemist](https://x.com/meta_alchemist/status/2029430826128293906) — 2026-03-05: Roundup of 10 open-source AI memory layers (free, popular on GitHub, some YC-funded) to give coding agents like Claude and Codex better recall than plain memory.md files, with notes on what each is good at and how to combine them. Engagement-styled listicle but substantive.

- [Sukh Sroay](https://x.com/sukh_saroy/status/2029400474739458379) — 2026-03-05: [Post unavailable — account suspended]

- [0xSero](https://x.com/0xsero/status/2029305128084218265) — 2026-03-05: Argues real-time, very fast inference (e.g. models served by Cerebras, used via "Spark") is a major shift that requires changing your working strategy, pointing to companion articles for details.

- [Peter Yang](https://x.com/petergyang/status/2029220235375714766) — 2026-03-05: Deep dive arguing your new job is to onboard and manage AI agents, with examples from Linear (AI team members you assign tasks to), Ramp (Claude Code as baseline for all roles), and Factory (codifying PM, frontend, and data-analysis work into reusable skills).

- [swarit](https://x.com/swaritjoshipura/status/2029219363749020051) — 2026-03-05: Curated links on agent context and evaluation: Foundation Capital on "context graphs" as AIs trillion-dollar opportunity (foundationcapital.com/context-graphs-ais-trillion-dollar-opportunity/), Anthropics guide to demystifying evals for AI agents (anthropic.com/engineering/demystifying-evals-for-ai-agents), a YouTube talk, and resolve.ai.

- [witcheer ☯︎](https://x.com/witcheer/status/2029013946701381978) — 2026-03-05: [Post unavailable — page doesn’t exist (same status as nummanali)]

- [Numman Ali](https://x.com/nummanali/status/2029013946701381978) — 2026-03-05: [Post unavailable — page doesn’t exist]

- [Dan Robinson](https://x.com/danlovesproofs/status/2028890694837039202) — 2026-03-05: Argues issue tracking/backlogs are dying: forward-thinking AI-augmented teams skip Linear/tickets entirely because the cost to fix an issue now approaches the cost to understand it. Works for small, flat, high-context teams with strong dev infra; framed as part of the 'death of midwit software engineering.'

- [Avid](https://x.com/av1dlive/status/2027429188471558475) — 2026-03-05: Engagement-style 'AI will take your job' listicle, but with a usable career playbook: audit which tasks AI can replicate, learn local agent tooling and stackable 'skills', layer AI-native competence (prompting, orchestration, RAG, automation), shift from executor to system designer, double down on human edge, and build a product/brand.

- [Muratcan Koylan](https://x.com/koylanai/status/2032671843) — 2026-03-05: [Post unavailable — corrupt status id resolves to unrelated @BizBlogger account]

- [Atharva](https://x.com/atharvaxdevs/status/2028903519802232991) — 2026-03-04: A teaser post aimed at engineers chasing the top 0.01% of "agentic engineering" skill (thread/resource hook).

- [Aarno](https://x.com/theglobalminima/status/2028432457784340950) — 2026-03-03: Suggests software engineers working on agentic AI should study reinforcement learning. As coding agents make custom harnesses/tools easy, the real challenges are behavior control, consistency, memory, and correction — areas where traditional RL on 'agents' intersects fruitfully with LLM agents.

- [David Byttow](https://x.com/davidbyttow/status/2028233578329600449) — 2026-03-02: Essay arguing AI agents are collapsing the coordination layer of organizations. As execution and coordination costs approach zero, the remaining scarce skill is goal clarity, taste, and ownership. Warns bad judgment now scales faster — strategic mistakes show up as fast delivery of the wrong thing.

- [tetsuo](https://x.com/tetsuoai/status/2028068322106097773) — 2026-03-02: Technical breakdown of recurring agentic failure modes in fast/distilled code models: wrong direct-exec vs shell selection, structured-output (JSON-only) non-compliance, and tool-result grounding failures (reporting success after a tool error). Fix: distill full agent trajectories (request→tool→output→grounded response), add contrastive near-miss examples, and gate on concrete agentic evals.

- [Nyk](https://x.com/nyk_builderz/status/2028022503319203926) — 2026-03-02: Announces open-sourcing Mission Control, a self-hosted AI agent orchestration dashboard: 26 panels, real-time WebSocket+SSE, SQLite (no external services), kanban board, cost tracking, role-based access, quality gates, multi-gateway support. Repo: github.com/builderz-labs/mission-control.

- [AVB](https://x.com/neural_avb/status/2027957534159835443) — 2026-03-01: [Post unavailable — page doesn't exist]

- [Joseph Thacker](https://x.com/rez0__/status/2027448137133264955) — 2026-03-01: Argues bug bounty / security research changed step-function fast in late 2025: coding agents went from not working to genuinely working. Example: pointed Claude Code at a target's scope (enumerate subdomains, analyze JS bundles, fuzz, test IDORs/GraphQL, write an HTML report); it ran ~30 min, self-recovered from auth/WAF errors, and returned two confirmed vulns. Hunters now build and share custom Claude Code skill libraries (JS static analysis, authenticated fuzzing, IDOR, GraphQL introspection). Quote-tweets Karpathy's parallel observation about programming.

- [Thariq](https://x.com/trq212/status/2027463795355095314) — 2026-02-28: Anthropic's Thariq on building Claude Code: designing an agent's action space is an art. Walks through the AskUserQuestion tool's evolution (ExitPlanTool param → output-format parsing → dedicated tool), the shift from TodoWrite to the Task tool as models improved, replacing RAG with a Grep search tool so Claude builds its own context, progressive disclosure via Skills, and the Claude Code Guide subagent. Lesson: revisit tool assumptions as capabilities grow; experiment, read outputs, 'see like an agent.'

- [Sudo su](https://x.com/sudoingx/status/2027264446989848613) — 2026-02-27: Practical steering tips for local coding agents: tell the model its own architecture/constraints (e.g. Qwen3.5 fires 8 of 256 experts/token), give project structure over single prompts, iterate in layers (scaffold → refine → polish), let it debug its own failures, and use long context (262K) to hold the whole project. Notes Claude Code as a solid harness and that llama.cpp merged native Anthropic endpoints (no proxy/LiteLLM). Argues the skill gap in local inference is now the harness and steering, not the models — all on a single RTX 3090.

- [SightBringer](https://x.com/_the_prophet__/status/2027235489930191056) — 2026-02-27: Critique of AI auto-memory (quote-tweeting Anthropic's Claude auto-memory announcement) as a "power grab disguised as convenience": capturing your patterns, defaults, and definitions of 'good' shifts the model from serving you to shaping you, and dependency is the business model. Counter-playbook: treat memory as a controlled instrument — scope it like permissions, separate persona from operations, keep a purge cycle, audit what the model believes about you, and never let it silently rewrite your intent. Frames the AI era as shifting from intelligence to custody of context/continuity.

- [Kirk Borne](https://x.com/KirkDBorne/status/2027031353849852309) — 2026-02-27: [Post unavailable — page doesn't exist]

- [Avi Chawla](https://x.com/_avichawla/status/2026907616337883612) — 2026-02-27: Avi Chawla revives Norm Hardy's 1988 'confused deputy problem' as the defining security issue for autonomous agents that hold real credentials but can't judge intent. He points to Teleport's open-source Agentic Identity Framework, which gives each agent a unique cryptographic identity, evaluates access in real time, auto-discovers shadow agents and unmanaged MCP servers, and keeps full audit trails.

- [Sukh Sroay](https://x.com/sukh_saroy/status/2026624254800965848) — 2026-02-27: [Post unavailable — account suspended]

- [Atlas Forge](https://x.com/atlasforgeai/status/2026380335249002843) — 2026-02-25: Long-form piece on nine 'meta-learning loops' that let an agent improve across sessions, not just within one: failure-to-guardrail pipelines, tiered memory with trust scoring and decay, prediction-outcome calibration, nightly extraction, friction detection, expiring context holds, plus cognitive loops (epistemic tagging, creative-mode directives, recursive self-improvement). Start with a regressions list; the key is closing the loops so learning compounds.

- [Aakash Gupta](https://x.com/aakashgupta/status/2026367615602667784) — 2026-02-25: Aakash Gupta, building on a Karpathy quote, argues agents are the new distribution channel for software: they call CLIs and MCP servers and read docs programmatically rather than browsing marketing sites. MCP hit 97M monthly SDK downloads and 10k+ servers in a year and was donated to the Linux Foundation. Winners of the next 24 months build agent-accessible surface area (CLIs, MCP endpoints, machine-readable docs) now.

- [Rohit](https://x.com/rohit4verse/status/2026359771427991764) — 2026-02-25: Rohit's 10-step checklist for taking agentic AI from demo to production (40%+ of projects fail on architecture, not models): threat-model boundaries, strict input/output contracts, RBAC + sandboxing, layered/compact context, governed grounding, planning/orchestration as control flow, memory in the architecture, native retry/error handling, full observability, and governance with safety gates and drift detection.

- [Dr Milan Milanović](https://x.com/milan_milanovic/status/2025835518207127968) — 2026-02-23: Milan Milanović makes the case for git worktree (shipped in Git 2.5, July 2015): check out multiple branches into separate directories that share one .git, avoiding stashing and duplicate clones. The standout modern use case is AI agents - give each of 3-5 parallel Claude Code/Cursor/Codex agents its own isolated worktree and branch so they don't overwrite each other.

- [Jeremy Daly](https://x.com/jeremy_daly/status/2025677417398821351) — 2026-02-23: Jeremy Daly wrote a 100+ page guide on building multi-tenant, commercial AI agent systems from ~18 months running them inside a large SaaS platform serving hundreds of enterprise customers. Covers hard requirements around tenant isolation, auditability, retention, and cost control, plus orchestration models, retrieval architectures, and evaluation harnesses.

- [Akshay 🚀](https://x.com/akshay_pachaar/status/2025767534159835443) — 2026-02-21: [Post unavailable - page doesn't exist]

- [tuna](https://x.com/tunahorse21/status/2024974148259512677) — 2026-02-21: tuna signal-boosts Alex Fazio introducing Plankton, a 'slop guard' for LLM coding agents. It aims to break the loop of copy-pasting pre-commit/linting errors back into the agent by enforcing lint rules the model can't cheat around.

- [Charly Wargnier](https://x.com/datachaz/status/2024803152730423685) — 2026-02-20: Charly Wargnier argues writing crystal-clear instructions for machines is the new 10x dev skill, and the most important file in a repo is now CLAUDE.md rather than the code. Top devs use it as an AI onboarding doc to define agent behavior: force the AI to verify its own work, auto-fix CI bugs, and reject hacky fixes.

- [Adam](https://x.com/adamdotdev/status/2024525246993506346) — 2026-02-20: Adam (working on OpenCode since early 2025) offers an honest, ambivalent reflection on agentic programming: the models are an incredible tool and a real productivity boost, but the shift is confusing and emotionally mixed. He misses the flow of banging out mundane code by hand and notes the growing distance between the developer and the code.

- [Viv](https://x.com/Vtrivedy10/status/2029576534159835443) — 2026-02-18: [Post unavailable - page doesn't exist]

- [Tech with Mak](https://x.com/technmak/status/2023990222027915746) — 2026-02-18: Tech with Mak boosts Matthew Berman's 'OpenClaw masterclass' video, in which Berman claims to have spent 2.54 billion tokens perfecting the OpenClaw coding agent and walks through 21 daily use cases (markdown files, memory system, CRM, and more). Quoted post had ~1.3M views.

- [kitze](https://x.com/thekitze/status/2021494167113990464) — 2026-02-12: kitze boosts Maximiliano Firtman's note that Chrome 146 ships an early flagged preview of WebMCP, which lets AI agents query and execute a web app's services without driving the UI like a human. Services are declared imperatively via a navigator.modelContext API or declaratively through a form; kitze calls exposing them 'the new responsive design.'

- [Peter Steinberger](https://x.com/steipete/status/2020704611640705485) — 2026-02-09: Peter Steinberger shares a SOUL.md rewrite prompt (via Molty) to give a coding agent a stronger personality: hold strong opinions instead of hedging, delete corporate-handbook rules, never open with filler like 'Great question', enforce brevity, allow natural humor, call out bad ideas (charm over cruelty), and permit well-placed swearing.

- [chiefofautism](https://x.com/chiefofautism/status/2019608146692673886) — 2026-02-07: chiefofautism shares Shannon (github.com/KeygraphHQ/shannon), an autonomous white-box AI pentester for web applications.

- [vogel](https://x.com/ryanvogel/status/2016204202343571474) — 2026-01-28: ryan vogel announces that dynamic agents.md resolution is now live in OpenCode, and suggests pairing it with a /learn command for a powerful workflow; points to @rekram11's explanation of the approach.

- [Theo - t3.gg](https://x.com/theo/status/2013888279355982131) — 2026-01-25: Theo boosts Wayne Sutton's launch of opensync.dev, a tool to track OpenCode and Claude CLI coding sessions in one place: searchable history, markdown export, eval-ready datasets, and views into tool usage, token spend, and session activity across projects. Theo frames it as a model of good devrel in 2026.

- [abhi](https://x.com/abhigyawangoo/status/2013823175855923640) — 2026-01-21: A detailed playbook for building continually-improving AI agents: define the business metric first, think in terms of many per-message/session/long-tail signals (not just thumbs up/down), design UI that makes signal collection easy, build signal-derived few-shot rankers, and A/B test every change against a control group. Includes a long copy-paste prompt for having Claude Code wire feedback loops into an existing agent. Warns about reward hacking when over-optimizing a single signal.

- [Matt Simpson](https://x.com/msmps_/status/2013376201977463038) — 2026-01-20: Matt Simpson shipped 'opentui-skill', a skill that gives coding agents TUI (terminal UI) superpowers via decision trees, progressive disclosure, and documented gotchas. Inspired by Dillon Mulroy's cloudflare-skill. Install instructions in a follow-up reply.

- [am.will](https://x.com/llmjunky/status/2013314055755194468) — 2026-01-20: am.will endorses a post by Dillon Mulroy on writing agent plans, calling it similar to his own approach but more concise. Plans to adopt some of Dillon's phrasing, especially the language around testing.

- [Sumanth](https://x.com/sumanth_077/status/2013232922296561826) — 2026-01-20: Overview of PageIndex, an open-source 'vectorless' RAG framework that drops vector databases and arbitrary chunking. It builds an LLM-optimized hierarchical tree (like a table of contents) and uses reasoning-based tree search to navigate documents the way a human expert would, giving traceable page-level references. Powers Mafin 2.5, which hits 98.7% on FinanceBench. GitHub link in comments.

- [Mischa van den Burg](https://x.com/mischa_vdburg/status/2013178484143571034) — 2026-01-20: Argues AI agent orchestration is the next 'container orchestration war', building on a Steve Yegge framework of two primitives: Workers (making a single agent produce high-quality output) vs Factories (coordinating thousands of work items across many agents). Maps these to familiar infra patterns - Workers = CI runners/pods/Lambdas, Factories = schedulers/control planes/workflow engines. Predicts 'nondeterministic idempotence' as the new eventual consistency, audit trails for AI work, GitOps-style declarative state, and reuse of the microservices observability stack. Kubernetes-fluent engineers have a head start.

- [Rohun](https://x.com/rohunjauhar/status/2012983351288692941) — 2026-01-19: Rohun open-sourced 'claude-build-workflow', a Claude Code workflow for autonomous building: you describe what you want, answer 10-15 min of interview questions, then close your laptop while an autonomous build loop runs in GitHub Codespaces and notifies your phone when done. It generates a PRD with user stories, technical architecture, edge-case analysis, story-quality validation, JSON conversion, then kicks off the build loop. Stitched together from Geoffrey Huntley's Ralph (bash-loop technique), Ryan Carson's snarktank/ralph (PRD skills, progress tracking, auto-commits, quality checks), and the BMAD Method (discovery/interview framework), adapted from Amp to Claude Code with phone notifications and one-command setup. Repo: github.com/rohunj/claude-build-workflow.

- [DAIR.AI](https://x.com/dair_ai/status/2012903315890225220) — 2026-01-19: DAIR.AI's Top AI Papers of the Week (Jan 12-18, 2026), heavy on agent memory and self-improvement: (1) Learning Latent Action World Models from in-the-wild video without action labels; (2) DroPE - extending context by dropping positional embeddings with cheap recalibration; (3) Dr. Zero - self-evolving search agents with no training data via proposer/solver loop (HRPO); (4) AgeMem - unified long/short-term memory as tool actions; (5) Focus - bio-inspired active context compression (22.7% token cut on SWE-bench Lite with Claude Haiku 4.5); (6) Agent-as-a-Judge survey; (7) SimpleMem - lifelong memory via semantic compression (30x token reduction); (8) Mistral's Ministral 3 (3B/8B/14B, Apache 2.0); (9) UniversalRAG - modality-aware multimodal RAG routing; (10) MemRL - runtime RL on episodic memory.

- [Sisyphus Labs](https://x.com/justsisyphus/status/2012441415398109192) — 2026-01-17: Sisyphus Labs recommends Rohit Ghumare's article 'Agents 201: Orchestrating Multiple Agents That Actually Work' as the first useful piece on agent orchestration. The article's premise: after building a single agent, the next challenge isn't making it smarter but making multiple agents cooperate without blowing the token budget or creating coordination chaos.

- [Gregor Zunic](https://x.com/gregpr07/status/2012052139384979773) — 2026-01-16: Gregor Zunic (Browser Use) argues 'The Bitter Lesson of Agent Frameworks': all the value is in the RL'd model, not thousands of lines of abstractions. An agent is just a for-loop of tool calls that runs until the model stops. Abstractions freeze assumptions and fight what the model already learned; agent frameworks fail because their action spaces are incomplete, not because models are weak. Their fix: start with maximal capability then restrict ('vibe-restrict' via evals). BU Agent gives the model raw Chrome DevTools Protocol + extension APIs for a near-complete action space. Also covers a minimal model-agnostic Chat wrapper (Anthropic/OpenAI/Google), ephemeral messages to keep massive DOM/screenshot state out of context, and the done() tool for explicit completion. Reliability (retries, rate limits, compaction) is ops, not the agent. Open-sourcing as agent-sdk (includes a Claude Code re-implementation).

- [Paul Solt](https://x.com/paulsolt/status/2012010080414081188) — 2026-01-16: Paul Solt's 7 beginner tips for OpenAI Codex: (1) start with GPT-5.2-Codex 'high' reasoning - enough for most work, avoid xhigh unless tricky; (2) when reasoning doesn't help, give agents better up-to-date local docs (he uses DocSetQuery to turn Dash DocSets into local Markdown); (3) read Peter Steinberger's (@steipete) 'shipping at inference speed' post; (4) borrow from Peter's agents.md and agent-scripts (e.g. 'committer' for atomic commits with multiple agents in one folder); (5) just talk to Codex - no complex rules or huge plan files; work one aspect at a time and parallelize projects while waiting; (6) ask agents to copy structure/Makefiles from other projects; (7) you'll likely need YOLO/danger mode to avoid constant approval nagging.

- [vas](https://x.com/vasuman/status/2011983687433212330) — 2026-01-16: vas (@vasuman) shares 'AI Agents 101,' a comprehensive long-form X article on how to build AI agents that actually work, framed as required reading before writing any code and drawing on 3 years as a Meta software engineer. He asks whether a part 2 would be useful.

- [James Cowling](https://x.com/jamesacowling/status/2011924122922852599) — 2026-01-16: James Cowling points to the Software Crisis of the 1960s-70s (en.wikipedia.org/wiki/Software_crisis) as a warning: productivity ground to a halt until good abstractions for managing software complexity emerged. His thesis is that without good platforms, the same stall will happen again in the AI-coding era.

- [Denislav Gavrilov](https://x.com/kuberdenis/status/2004934631616086417) — 2025-12-28: Denislav Gavrilov containerizes Claude Code in Kubernetes as 'Clopus-Watcher,' an autonomous monitoring agent that watches a namespace and, on application errors, writes and applies a hotfix and documents it — effectively a 24/7 on-call engineer. Repo, examples, and results at denislavgavrilov.com.

- [AGENTS.md](https://agents.md/) — 2025-12-28: AGENTS.md (agents.md) is a simple, open format for guiding coding agents, now used by over 60k open-source projects. Think of it as a README for agents: a dedicated, predictable place for the build steps, tests, and conventions that coding agents need but that would clutter a human README — kept intentionally separate so agents have one clear location to look.

- [SightBringer](https://x.com/_the_prophet__/status/2004796159299084424) — 2025-12-27: An essay arguing software engineering is undergoing a 'phase transition' in human leverage: for decades leverage came from writing more correct instructions faster, but the unit of leverage has shifted from writing code to orchestrating intelligence. The programmer becomes a systems integrator of probabilistic entities whose reasoning can't be fully inspected or controlled — which the author says explains why even Karpathy feels 'behind.'

- [Tech with Mak](https://x.com/technmak/status/2002713140757496299) — 2025-12-22: A structured LangGraph learning path (pitched as filling the gap since LangGraph appears in ~half of AI job descriptions). Progresses from basic agent concepts (Pydantic data validation, agentic chatbots, multi-agent coordination) through production systems (a 2.5-hour LangGraph+MCP crash course, debugging/monitoring, deployment architecture) to RAG pipelines (multimodal RAG, hallucination fixes, end-to-end retrieval, Typesense search).

- [Claire Silver](https://x.com/clairesilver12/status/2002443560898208162) — 2025-12-21: Claire Silver highlights Unreal MCP, a free MCP server that lets you prompt Claude to build things in Unreal Engine — e.g. 'make a Victorian manor, here's a reference pic, use the assets in this folder' and it just does it. She promised a demo video and calls it '10/10 magic.'

- [Santiago](https://x.com/svpino/status/2002107789888655655) — 2025-12-19: Santiago shares a video demoing a spec-driven development environment where 100% of the developer's time goes to writing specs and managing agents and 0% to writing code — arguing software development will never be the same.

- [Femke Plantinga](https://x.com/femke_plantinga/status/2000883645888827806) — 2025-12-16: Femke Plantinga argues multi-agent AI systems are displacing single-agent architectures and breaks down what a well-structured one looks like: a supervisor/orchestration layer that plans, routes queries to specialists and refines them (the 'air traffic controller'), plus specialized task-specific agents (query rewriters, etc.). She notes the real trade-off — more complex workflows but serious coordination challenges.

- [Matt Dancho (Business Science)](https://x.com/mdancho84/status/2000658529753932273) — 2025-12-15: Matt Dancho highlights an open-sourced (free) Python library, 'AI Data Science Team' (github.com/business-science/ai-data-science-team), that automates data-science workflows with AI — data loading, cleaning, exploratory analysis, and feature engineering — tracking each step in a fully reproducible pipeline. Includes a walkthrough video and a free 1-hour agentic AI workshop.

- [Tech with Mak](https://x.com/technmak/status/1998264904563007889) — 2025-12-09: Tech with Mak distills Google's quiet December release of five AI-agent papers published one per day over five consecutive days — more than 250 pages covering how agents should be built, evaluated, secured, and deployed.

- [Rohan Paul](https://x.com/rohanpaul_ai/status/1998262710040228310) — 2025-12-09: Rohan Paul summarizes a paper proposing an 'agentic file system' for context engineering: treat every memory, tool, external source, and human note as a file in a shared space, with a persistent context repository separating raw history, long-term memory, and short-lived scratchpads so the prompt holds only the slice needed now. Every access is logged with timestamps and provenance, and a constructor/updater/evaluator manage context under the model's limited window.

- [Rohan Paul](https://x.com/rohanpaul_ai/status/1997405403987222642) — 2025-12-07: Rohan Paul summarizes Google's guide on context engineering for multi-agent systems (built around ADK). Instead of giant prompts, it compiles a view over state split into Working Context, Session, Memory, and Artifacts; each call rebuilds Working Context from instructions, selected session events, memory results, and artifact references. ADK controls context growth via compaction, filtering, and caching — summarizing old spans, dropping useless events, and reusing a stable prefix — and pushes large payloads out to Artifacts to keep systems fast, affordable, and less hallucination-prone.

- [Dan Shipper](https://x.com/danshipper/status/1986870518046200255) — 2025-11-08: Dan Shipper recommends Kieran Klaassen's Every piece 'Teach Your AI to Think Like a Senior Engineer' (every.to/source-code) as a masterclass on coding with AI.

- [Pontus Abrahamsson](https://x.com/pontusab/status/1981700333857636550) — 2025-10-24: Pontus Abrahamsson points to midday-ai/ai-sdk-tools (github.com/midday-ai/ai-sdk-tools) — a set of example AI SDK tools/integrations for building agent tooling.

- [Ruslan Beskorovainiy](https://x.com/chemobyazan/status/1975326044271079509) — 2025-10-07: Points to the contains-studio/agents GitHub repo, a shared collection of AI agents currently in use.

- [Agentic Design Patterns](https://github.com/sarwarbeing-ai/Agentic_Design_Patterns/blob/main/Agentic_Design_Patterns.pdf) — 2025-10-05: [Post unavailable — Agentic Design Patterns GitHub repo removed via DMCA takedown]

- [Dan McAteer](https://x.com/daniel_mac8/status/1970120352664605124) — 2025-09-22: Shares a four-step agentic-coding pattern with an added Verification step (build feedback loops that test the plan was implemented correctly, since models still fail on execution), meant to be copied into an AGENTS.md file. Works with AmpCode or any AGENTS.md-aware coding agent.

- [Aakash Gupta](https://x.com/aakashg0/status/1967135994228166848) — 2025-09-15: Boosts another user's step-by-step roadmap for building your first AI agent, calling it 'gold.' Engagement-style framing; the substantive content lives in the referenced roadmap rather than the post itself.

- [maxleedev](https://x.com/maxleedev/status/1962938769914658984) — 2025-09-03: Announces a canvas-style interface for LLMs, built in response to a viral post arguing chat UIs need git-like branching/forking of conversations to explore alternate threads without derailing the main one.

- [Dan Shipper](https://x.com/danshipper/status/1957469868862677028) — 2025-08-19: Links Dan Shipper's Every essay 'My AI Had Already Fixed the Code Before I Saw It,' on AI coding agents autonomously fixing code before the developer even reviews it.

- [Dante O. Cuales, Jr.](https://x.com/danteocualesjr/status/1957204427909321027) — 2025-08-18: Argues the intimidation factor of AI engineering is mostly artificial: most work is API orchestration, prompt optimization, and data-pipeline plumbing, with model internals abstracted away. The real skill is choosing the right tool and chaining them effectively.

- [Asterisk (getAsterisk)](https://github.com/getAsterisk/claudia) — 2025-08-18: opcode (formerly Claudia, by Asterisk) is an open-source Tauri 2 desktop GUI and toolkit for Claude Code: visual project/session management, custom CC agents with per-agent file/network permissions and background execution, a usage/cost analytics dashboard, MCP server management (with Claude Desktop import), session timeline/checkpoints with diff and fork, and a built-in CLAUDE.md editor. Note: the repo has been renamed from getAsterisk/claudia to winfunc/opcode.

- [Philip Vollet](https://x.com/philipvollet/status/1955945448860008655) — 2025-08-15: Announces Elysia, an open-source agentic RAG platform (successor to Verba) built on Weaviate and DSPy. Highlights: transparent decision-tree agents with self-healing and custom tools/branches, pre-query data analysis to avoid blind vector/text search, dynamic result displays, feedback-driven few-shot personalization so smaller models perform like larger ones, and query-time chunk-on-demand. Delivered as a FastAPI+NextJS app and a pip package (elysia-ai).

- [Imrat](https://x.com/imrat/status/1954497164589056090) — 2025-08-11: A recipe for using Claude Code as a DevOps agent with its new background jobs: run Claude in a tmux session, have it spawn a background process to tail server logs and summarize them, then a second process that pings Claude to 'check logs' on an interval.

- [Nick Dobos](https://x.com/nickadobos/status/1930878279290060975) — 2025-06-07: Riffs on a repo (Shubham Saboo's) that stores millions of text chunks inside MP4 video files for fast semantic search, pitched as an open-source replacement for expensive vector databases; Nick Dobos speculates video may be an optimal encoding for AI memory, echoing how human memory leans on vision.

- [Mervin Praison](https://x.com/mervinpraison/status/1881788246684013011) — 2025-01-22: Shows a 100% local RAG AI agent with reasoning: DeepSeek via Ollama for the LLM, PraisonAI to build the agent in a few lines, Nomic embeddings, and a Streamlit UI—code included in the thread.

- [Santiago](https://x.com/svpino/status/1881336934418755862) — 2025-01-21: Walks through GroundX, an open-source, self-hostable/air-gapped enterprise RAG system. Two services: Ingest (a pretrained vision model that 'understands' documents instead of feeding raw docs to the LLM) and Search (text+vector search with a fine-tuned re-ranker). Santiago's thesis: most teams need better ingestion, not better retrieval; includes a video demo and the free X-Ray inspection tool.

- [Tom Dörr](https://github.com/tom-doerr/dotfiles/blob/master/instruction.md) — 2025-01-04: Tom Dörr's AI-coding-agent instruction file (an AGENTS.md-style rules doc): single-letter command aliases (c=continue, rc=reduce complexity, acp=add/commit/push, t=add tests), strict engineering rules (no fallbacks, don't swallow exceptions, TDD with many asserts, uv over pip, work on git branches, keep complexity low, don't weaken the linter), and ready-to-paste DSPy optimizer snippets (BootstrapFewShotWithRandomSearch, MIPROv2, SIMBA).

- [Shubham Saboo](https://x.com/saboo_shubham_/status/1849638773136687551) — 2024-10-25: Introduces AutoRAG, an open-source tool that automatically benchmarks multiple RAG strategies to find the optimal RAG pipeline for your data in a few lines of Python.

- [Shubham Saboo](https://x.com/saboo_shubham_/status/1818111127286579448) — 2024-07-30: Tutorial for building a no-code RAG chatbot to chat with any GitHub repo, powered by open-source Llama 3.1 405B.

- [Akshay](https://x.com/akshay_pachaar/status/1816088785152848028) — 2024-07-24: A tutorial thread on building a 100% local RAG app using Meta's Llama 3.1.

- [curvedinf](https://github.com/curvedinf/dir-assistant) — 2024-06-18: dir-assistant is a pip-installable CLI that recursively indexes the text files in your directory so you can chat with them via a local or API LLM, auto-injecting the most contextually relevant files. It uses CGRAG (Contextually Guided RAG) for file selection, supports interactive and single-prompt modes (including auto file edits + git commits), many local acceleration backends and all major LLM APIs via LiteLLM, and optimizes prompt/context caching (50-90% cache hits).

### Claude Code (174)

- [Alex Prompter](https://x.com/alex_prompter/status/2074198124898181121) — 2026-07-14: Alex Prompter's thread pitches 'cloning' Fable 5's reasoning into Opus 4.8 before Fable 5 shifts to pay-per-use credits — extracting a model's 'operating manual' as a portable prompt and transplanting it onto a cheaper model to keep the way it thinks rather than the model itself. Engagement-framed but a real prompt-portability technique.

- [Anatoli Kopadze](https://x.com/anatolikopadze/status/2068328135611822149) — 2026-07-06: Anatoli Kopadze's widely-viewed piece 'Loops explained: Claude, GPT, Mira and what actually works' argues most people use AI the slow way (type, wait, fix, repeat by hand) and that the faster approach top AI engineers care about is building loops. Covers what loops are, how they work under the hood, when they're worth it vs a trap, and how to build a basic one in Claude or ChatGPT. Quote-tweets Peter Steinberger: you shouldn't be prompting coding agents, you should be designing loops that prompt your agents. (Includes some self-promotion for his X/Telegram.)

- [Anatoli Kopadze](https://x.com/anatolikopadze/status/2073396351279276397) — 2026-07-05: Anatoli Kopadze (quote-tweeting his own Claude features guide) shares an Anthropic engineer's claim that most people use Sonnet 5 and Fable 5 wrong and can set them up right in one afternoon to stop overpaying — a 31-minute session on testing each model against your real use case, plus a guide to Claude features '99% of users never find.'

- [Nyk](https://x.com/nyk_builderz/status/2073305434069647735) — 2026-07-05: [Jeremy flagged: urgent for orchestration] Nyk released Council of High Intelligence v1.2.0 as a Claude Code plugin (/plugin marketplace add 0xNyk/council-of-high-intelligence) — an 18-persona deliberation engine (Aristotle, Feynman, Kahneman, Torvalds, Socrates, Taleb, Meadows + more) that runs 3 rounds of anonymized cross-examination to one auditable verdict on your existing subscriptions, no API keys. v1.2.0 adds confidence-weighted verdicts (vote weight scales with stated confidence; a hesitant council escalates to you instead of forcing consensus, per Roundtable Policy + ConfMAD 2025), per-persona reasoning methods (Socratic elenchus, Taleb tail stress-testing, Meadows causal-loop mapping via DMAD), per-project defaults via .council.yaml, and CI parity gates so the Claude/Codex/Gemini coordinators can't silently drift.

- [Elvis](https://x.com/elvissun/status/2073161303997452794) — 2026-07-05: Elvis makes a meta point about eval-driven skill building that extends beyond coding to any knowledge problem where an eval set can be concretely defined. Example: a newsjack.sh skill that judges newsworthiness — he started from labeled examples (stories that made real news vs ones that didn't, e.g. hitting #1 on Product Hunt isn't news even though LLMs say it is), fed them into an eval set, then used /goal to iterate a skill implementation that lets 3 agents (Opus, Sonnet, Haiku) all score stories correctly — proving 'the intelligence lives in the skill, not the model.' Notes Fable's ability to learn across examples and draw a through-line is well beyond Opus.

- [Avid](https://x.com/av1dlive/status/2073114542851416260) — 2026-07-05: Avid (ALL CAPS engagement framing) makes a practical context-engineering point: give an agent one index file per major folder for a direct line to what it needs. The same task dropped from 2 minutes (7 files opened, wandering, a 3-month-old brief still missing) to 10 seconds with the same model, nothing else changed. 'Build the path or watch it search in the dark.' Quote-tweets Machina's article 'How to build a second brain with Fable 5.'

- [darkzodchi](https://x.com/zodchiii/status/2072973531768328626) — 2026-07-05: darkzodchi's 'Claude Fable 5 Setup Guide' covers which heavy tasks actually deserve Fable 5, the new safeguards that reroute you to Opus, and how to plan the free window (up to 50% of weekly limit free until July 7). Recaps a reported Fable 5 timeline: launched June 9, pulled June 12 under a US export-control order tied to a jailbreak report, back online July 1. (Includes Telegram self-promo.)

- [me](https://x.com/twetsfyp/status/2072939523160285688) — 2026-07-05: Engagement-farmed clickbait promoting a 16-minute tutorial on building '$50,000 cinematic websites' step by step with Claude Fable 5 ('Mito Claude is back in an insane way'). Little substance in the post itself. 1.9M views.

- [Tom Dörr](https://x.com/tom_doerr/status/2073354493794636248) — 2026-07-04: Tom Dörr shares VoltAgent's awesome-claude-skills (github.com/VoltAgent/awesome-claude-skills) — a curated 'awesome list' of official agent Skills from leading engineering teams.

- [0xSero](https://x.com/0xsero/status/2073274981279260774) — 2026-07-04: 0xSero shares Parcels (github.com/0xSero/parcels) — a tool for 'cloud agents' when you have Tailscale and more than one desktop: it packages your repo plus a live coding-agent session (Claude Code / Codex / pi), transfers it to another machine on your Tailscale network, and runs it in tmux so you can step away from the screen.

- [Archive](https://x.com/archiveexplorer/status/2073136973162872897) — 2026-07-04: Archive (engagement framing, 'met an Anthropic engineer making $1.2M') argues the real lever isn't Opus vs Sonnet but 'what the model wakes up into' — the .claude/ folder: CLAUDE.md (the contract), settings.json (permissions), hooks/ (reflexes), agents/verifier (a shift-notes checker subagent), skills/ (~33 reusable 'muscle memories'), .mcp.json (tools), and MEMORY.md (shift log). 'You write the folder once; the folder runs the model.' Quote-tweets his own article 'Loop and Harness engineering: 7 files, 5 steps.'

- [Thariq](https://x.com/trq212/status/2073101078145724589) — 2026-07-04: Thariq shares his article 'A Field Guide to Fable: Finding Your Unknowns' — the most important part of working with Claude Fable 5 is discovering your own unknowns so you can prompt it better. Framing: 'the map is not the territory' — your prompts, skills, and context are the map (a representation of the work to be done), and the practice is surfacing what you don't yet know about the actual work.

- [Daniel Miessler](https://x.com/danielmiessler/status/2073076322390384798) — 2026-07-04: Daniel Miessler shares a set of 'prompts to run now that you have Fable back' — a quick collection of prompts to try with Claude Fable 5 following its return.

- [Dhilip Subramanian](https://x.com/sdhilip/status/2072334422414876957) — 2026-07-02: Dhilip walks through his 7-skill Claude Code setup and what each earns its spot for: data engineering (dbt/Airflow), gstack, grill-me, superpowers (spec/plan/TDD), impeccable (UI audit), last30days, and printing-press (API/site to token-light CLI). Advice: start small, add a skill only when you hit a job your current ones can't do.

- [Andrew Ng](https://x.com/andrewyng/status/2071988145667928442) — 2026-07-02: Andrew Ng's 'loop engineering' letter lays out three nested loops for building 0-to-1 products: the fast agentic coding loop (agent writes/tests/iterates every few minutes), the developer feedback loop (human steers over tens of minutes to hours), and the slow external feedback loop (alpha testers, A/B tests over days). Humans retain a context advantage, so engineers increasingly play a partial product-management role.

- [Akshay](https://x.com/akshay_pachaar/status/2071509401224261823) — 2026-06-29: Walkthrough of Google's Agents CLI as tooling for Karpathy's "agentic engineering" (spec design, eval loops, security). One setup command injects 7 ADK-specific skills into a coding agent; author built and deployed a RAG agent end-to-end with Claude Code, including 20 LLM-as-judge eval scenarios and enterprise registration.

- [Boris Cherny](https://x.com/bcherny/status/2071379474277613732) — 2026-06-29: As engineering/product/design/DS roles blur, Cherny proposes five team archetypes (not tied to job function): Prototyper, Builder, Sweeper, Grower, Maintainer. Healthy teams need different mixes by product maturity — pre-PMF wants 1+2+3, growing wants 2+3+4+some 5, strong-PMF wants 3+4+5+some 2.

- [zostaff](https://x.com/zostaff/status/2070852153594290195) — 2026-06-27: Long-form "Loop Engineering" article: four autonomous loops that actually pay off because the task repeats, a machine can reject the result, the agent carries it whole, and "done" is objective. Covers the bare while-loop/exit-code/budget mechanics under Claude Code Routines and four worked configs: morning CI test triage (with maker-checker subagent), dependency watchdog, doc synchronizer, and overnight research digest. Theme: the harder the verification, the more you can hand the loop; soft verification keeps a human in the loop.

- [Brady Long](https://x.com/thisguyknowsai/status/2070445026233172314) — 2026-06-27: Promo-styled writeup of MemPalace, an open-source local AI memory tool (49K stars). Instead of dumping everything into semantic search, it organizes memory into a structured "palace" (people/projects as wings, topics as rooms, verbatim text in searchable drawers). Claims 96.6% retrieval recall on LongMemEval with zero LLM/API/cloud, 98.4% with a hybrid pipeline; ships 29 MCP tools and auto-save hooks for Claude Code. Python 3.9 + ChromaDB, ~300MB, MIT.

- [Akshay](https://x.com/akshay_pachaar/status/2069769689560187027) — 2026-06-25: Breakdown of "loop engineering" (opening on a Karpathy quote about removing yourself as the bottleneck): a trigger decides what runs, the loop is the maker, a separate checker grades output (a model grading itself just justifies its work), and state lives on disk not context (suggests Zep's Graphiti temporal knowledge graph). Two failure points: set the exit condition before the loop runs, and add observability on the harness since the checker only catches in-run failures (suggests Comet's Opik). Thesis: the model is a commodity; the loop around it is where the engineering lives.

- [Codez](https://x.com/0xcodez/status/2064374643729773029) — 2026-06-23: A long-form Loop engineering roadmap arguing the leverage point in agentic coding has moved from writing prompts to designing self-running loops. Covers the 4-condition test for when a loop is worth building (task repeats, automated verification, token budget, senior-engineer tooling), the five building blocks (automations like /loop and /goal, git worktrees, skills, MCP connectors, sub-agents), the maker/checker split, the Ralph Wiggum quiet-failure mode, comprehension debt and cognitive surrender, and the security tax of unattended loops. Cites Anthropic engineering docs and Addy Osmani.

- [Harry Tandy](https://x.com/harrytandy/status/2065818850633932996) — 2026-06-14: Opens with a Sam Altman quote that the cost to use a given level of AI falls ~10x every 12 months, then lays out a 10-step agentic-coding sprint: pick the heaviest backlog item, write a FABLE_RUN.md spec (goal/scope/commands/review rules/done criteria), map the repo first, break the job into checkpoints that each end with diff + test output + next decision, split builder and checker agents, use git worktrees for parallel attempts, and keep a RUN_LOG.md of every failed command and accepted fix.

- [Avid](https://x.com/av1dlive/status/2065747876005937416) — 2026-06-14: Promotes a 'second brain' pattern attributed to Karpathy: let an LLM maintain a wiki of your notes so knowledge compounds as you dump sources and it reads, links, and files them. Points to a free Claude Code plugin, claude-obsidian by AgriciDaniel (claude plugin marketplace add AgriciDaniel/claude-obsidian; claude plugin install claude-obsidian@agricidaniel-claude-obsidian), then run /wiki inside an Obsidian folder. Quote-tweets the author's own article on building Obsidian from scratch with 13+ Kimi agents.

- [Suryansh Tiwari](https://x.com/suryanshti777/status/2065473893817848266) — 2026-06-13: Claims Anthropic released an official Claude Code plugin, claude-code-setup, that scans your project and recommends and sets up hooks, skills, MCP servers, subagents, and automations step-by-step (install: /plugin install claude-code-setup@claude-plugins-official), arguing most people run Claude Code vanilla and miss the surrounding ecosystem. Quote-tweets the author's own 'Unveil' build. (Treat the 'official' claim as unverified.)

- [Codez](https://x.com/0xcodez/status/2065097407965127142) — 2026-06-12: Hype-framed thread claiming an Anthropic 'Managed Agents' team demo showing how to build self-improving agent systems with the Fable 5 model from scratch in ~13 minutes, using /loops, dynamic workflows, and 'dreaming.' Quote-tweets the author's own 14-step article on the same. (Strong engagement-farming framing; claims unverified.)

- [Meta Alchemist](https://x.com/meta_alchemist/status/2064431279383433646) — 2026-06-11: Shares a copy-paste 'Repo Audit & Improvement Plan' prompt — a structured, 4-phase principal-engineer audit (Phase 1 discovery/mapping before judging, then a prioritized, actionable improvement plan), with instructions to cite file paths and line numbers and to flag anything unverifiable. Useful prompt template, but wrapped in hype framing around a nonexistent 'Claude Fable 5' model.

- [Boris Cherny](https://x.com/bcherny/status/2064426115255730578) — 2026-06-11: Boris Cherny (Anthropic / Claude Code) on why self-verification loops matter: letting a model check its own work lets it run autonomously for much longer and land closer to your intent, so you check in less. Points to a breakdown by @delba_oliveira (via @ClaudeDevs) on encoding your manual checks so Claude Code closes its own feedback loop.

- [BOOTOSHI](https://x.com/kingbootoshi/status/2063999432077795579) — 2026-06-09: Long personal write-up: BOOTOSHI claims the agent-orchestrating-subagents pattern (token-maxxing across parallel work) was right for opus-4.5/gpt-5 but is no longer optimal with the newer generation (gpt-5.5, opus-4.8). Argues the extended context window + intelligence means these models are now more capable as a single 'MEGA THREAD' with a single operator. Counter-trend to the multi-agent enthusiasm of early 2026.

- [Peter Yang](https://x.com/petergyang/status/2063988122720055772) — 2026-06-09: Five takeaways from a conversation with @kunchenguid (ex-Meta L8 engineer) on agentic engineering: (1) plan and validate, don't code yourself — you're the always-on team's manager; (2) plan quality determines how long agents run autonomously — a detailed spec can run for hours vs minutes for a one-liner; (3) use visual plans, not walls of markdown — Lavish (github.com/kunchenguid/lavish) generates visual HTML plans; (4 and 5 truncated in scrape — likely about validation rubrics and feedback loops).

- [rody](https://x.com/0x_rody/status/2063722061126651935) — 2026-06-09: Quotes 'Anthropic's main manager': 'Nobody types prompts from scratch. The commands should be live in the project.' Points to a 26-min talk walking through Anthropic's command library every new dev inherits on day one. Links the author's own article 'How to Build a Claude Code Slash Command Library' with a template inside — argues devs spend ~10 hours/month re-typing context that should be a single saved command.

- [darkzodchi](https://x.com/zodchiii/status/2063559498078278109) — 2026-06-08: Quotes 'Anthropic engineer Margot van Laer': 'Every prompt you type more than twice should be a file. The ones we use internally aren't memorized, they're saved.' Points to a 33-min talk on the prompt patterns Anthropic packages and reuses across every Claude Code session — links the same Claude Code slash-command-library template from rody.

- [rari](https://x.com/0xwhrrari/status/2063244577482440978) — 2026-06-08: Engagement-farmed but useful link dump of free AI-engineering learning resources (LangChain agent architecture, Anthropic's Claude Code 101 + in-action courses, prompt engineering docs, anthropics/courses interactive prompt tutorial, claude.md docs, skills, MCP). Wrapped in 'Google's former CEO just said...' framing but the underlying link list is the substance.

- [Hanako](https://x.com/hanakoxbt/status/2063305395687522702) — 2026-06-07: Describes an Anthropic 'dreaming agents' memory pattern: a second set of agents that, after you log off, reopen every session, fact-check the first agents, merge duplicates and burn stale memory — up to 100 at once, ~95% cached so a full rewrite costs almost nothing. Points to a multi-agent code/review/deploy team guide.

- [Cat Wu (Anthropic)](https://x.com/_catwu/status/2062408623565984209) — 2026-06-06: Anthropic's data team automated ~95% of business-analytics queries with Claude; the linked blog covers their approach to skills, data foundations, evals, ablations, and online validation for data-analysis agents.

- [Thariq](https://x.com/trq212/status/2061907538741006796) — 2026-06-03: Announces dynamic workflows as the biggest Claude Code upgrade since skills and subagents — Claude writing its own task-specific harness on the fly — with excitement about the non-technical tasks it unlocks.

- [Thariq](https://x.com/trq212/status/2061907337154367865) — 2026-06-03: Full Anthropic article on dynamic workflows in Claude Code: Claude writes its own JavaScript harness to spawn/coordinate subagents (own models, own worktrees, resumable), countering agentic laziness, self-preferential bias and goal drift. Covers patterns (fan-out-and-synthesize, adversarial verification, tournament, loop-until-done), many use cases (migrations, deep research, triage, root-cause, evals, model routing), the 'ultracode' trigger, token budgets, and when NOT to use it.

- [darkzodchi](https://x.com/zodchiii/status/2061040686330257656) — 2026-05-31: Anthropic-engineer clip: build 5 focused agents (code review, tests, docs, security) in an afternoon, each ~15 minutes as a markdown file with instructions + prompt. Links a beginner subagent-building template.

- [Mr. Buzzoni](https://x.com/polydao/status/2060964743402455212) — 2026-05-31: Engagement-farmed ALL-CAPS thread riffing on Karpathy's 'we're in the 1960s of AI' / software-3.0 framing to push the author's own listicle article '...These Are the Ones That Matter [Full GitHub Links]' cataloguing 32 Claude skills. Clickbait wrapper, but the underlying skills roundup may be worth a skim.

- [Rahul](https://x.com/sairahul1/status/2059632149716942923) — 2026-05-28: Hype-framed ('Anthropic just released the blueprint for a company run by Claude Code; work is dying') push for a listicle on building a SaaS MVP in an afternoon with 7 AI agents. Clickbait wrapper over a real multi-agent build walkthrough.

- [darkzodchi](https://x.com/zodchiii/status/2059603103070945391) — 2026-05-27: Boris Cherny (Claude Code): 'we stopped fixing Claude's mistakes; we made Claude fix them itself.' Links a copyable setup for having Claude Code catch, fix, and learn from its own errors instead of the write-code/tests-fail/explain loop.

- [Parag pawar](https://x.com/dharmikpawar13/status/2059571098484675051) — 2026-05-27: Argues CLAUDE.md is a control layer, not a README: use scope hierarchy (global → project → folder, nearest wins) and a WHAT/WHY/HOW framing, favor specificity ('TypeScript strict mode, Zod validation' over 'production-ready code'), start with /init, keep it under ~500 lines, use hooks, and treat it as living infrastructure.

- [Theo - t3.gg](https://x.com/theo/status/2059352130289651925) — 2026-05-27: Endorses DeepSWE, a new agentic-coding benchmark that reflects the realistic day-to-day developer experience — showing where top models actually diverge rather than clustering as they do on public leaderboards.

- [Movez](https://x.com/0xmovez/status/2059346354984612126) — 2026-05-27: An Anthropic engineer's 37-minute masterclass on shipping production agent teams: three building blocks (brain=persona, hands=environment, sessions), a server-side loop so nothing breaks on refresh, and why agents 'die before production.' Links a 10-step multi-agent build guide.

- [darkzodchi](https://x.com/zodchiii/status/2058928613987160287) — 2026-05-25: Boris Cherny (Claude Code): 'every night I have a few thousand agents running,' monitored from his phone. Links a piece arguing the next wave is a team of agents in a real chat app where they @mention each other, delegate, and remember — versus one sandboxed, memoryless ChatGPT tab.

- [Garry Tan](https://x.com/garrytan/status/2057946119725080878) — 2026-05-24: Garry Tan's 'simple secret to agentic coding,' linking a Forbes profile ('The YC Chief Who Codes 10,000 Lines A Day Has A Simple Secret').

- [Mnimiy](https://x.com/mnilax/status/2057551699204857930) — 2026-05-22: Reports that Anthropic engineers kept repeating 'let it cook' at Code with Claude London (Boris Cherny, Ravi Trivedi, Katelyn Lesse): stop micromanaging prompts, write the routine, let Claude prompt itself — 'routines are higher-order prompts; the runtime is shipped; the prompts are the bottleneck.' Links 9 tested Claude Cowork prompt-templates.

- [Akshay](https://x.com/akshay_pachaar/status/2057446083853520948) — 2026-05-22: Argues 'Claude Code isn't a coding tool — it's a programmable dev environment,' with 12 features that make it programmable: CLAUDE.md, Rules, Skills, Hooks, Slash Commands, Plugins, MCP, Plan Mode, Permissions, Subagents, Voice Mode, Rewind (1-5 define the environment, 6-7 extend it, 8-9 control it, 10-12 change how it runs).

- [Khairallah AL-Awady](https://x.com/eng_khairallah1/status/2057433528363811098) — 2026-05-22: Engagement-framed roundup of a Boris Cherny podcast on why most people don't get results from Claude — they never set it up (CLAUDE.md, features that change how Claude thinks, unopened settings) — claiming ~30-38 untouched features. Links a '40 Features Most Users Have Never Touched' article.

- [CyrilXBT](https://x.com/cyrilxbt/status/2056933229924372546) — 2026-05-20: ALL-CAPS hype ('ANTHROPIC JUST KILLED THE DEMO AGENT ERA') about Anthropic's Agents team showing a production-grade four-layer framework for multi-agent systems in a 30-minute video. (The quoted article is mismatched — about turning Obsidian into a personal OS.)

- [Akshay](https://x.com/akshay_pachaar/status/2056714042455343160) — 2026-05-20: RAG vs CAG explained: Cache-Augmented Generation keeps static, high-value knowledge in the model's KV memory instead of hitting the vector DB every query. Combine them — cache 'cold' static data (policies/docs), retrieve 'hot' dynamic data — for faster, cheaper inference. OpenAI and Anthropic already support prompt caching.

- [Garry Tan](https://x.com/garrytan/status/2056711154224034125) — 2026-05-20: Garry Tan on dynamic, just-in-time skills for personal AI: 'markdown is code,' and the agent can change its own skills when new cases appear — 'just-in-time personal software is the most powerful idea of 2026.' A reply notes skill bundles carrying their own tests that the agent modifies in-flight create the compounding effect.

- [Linas Beliūnas](https://x.com/linasbeliunas/status/2056679329484927356) — 2026-05-20: Summarizes Anthropic's free AI-native founder playbook: build AROUND Claude across Idea → MVP → Launch → Scale (pressure-test the idea, Claude Code builds the product, Claude Cowork handles ops, Claude turns knowledge into compounding context). 'AI compresses execution but not judgment' — the edge becomes knowing what NOT to build; best AI-native startups have the best AI operating systems, not the biggest teams.

- [Aakash Gupta](https://x.com/aakashgupta/status/2056405221908394406) — 2026-05-19: Aakash Gupta on Pawel Huryn's six-item CLAUDE.md 'routing table' (project description, file-structure map, identity context, knowledge routing, workflow pointers, and a 3-line self-improving prompt), with everything else in on-demand files/folders. The paste-ready self-improving prompt: review existing rules/hypotheses, apply confirmed rules, then update them from feedback each session.

- [ClaudeDevs](https://x.com/claudedevs/status/2056403446056784288) — 2026-05-19: Anthropic blog on running Claude Code at scale — best practices from teams working across multi-million-line monorepos, decades-old legacy systems, and distributed microservices.

- [darkzodchi](https://x.com/zodchiii/status/2056336049589092866) — 2026-05-19: Shopify Head of Engineering Farhan Thawar: 'if you don't figure out how to harness agents in 2026, you'll be behind.' A practical enterprise-AI-coding breakdown / Shopify AI playbook, linking a 'Claude Code setup behind Shopify's 23,000 engineers' article (racing to automate 96% of coding by Q3, many parallel Claude Code agents).

- [Dami-Defi](https://x.com/damidefi/status/2056053698674270631) — 2026-05-19: Fed MIT's 12 free graduate-level AI textbooks into Claude and rebuilt his research system around them. Links 'I Fed 12 Free MIT AI Textbooks Into Claude. It Rebuilt My Entire Research System.'

- [Suryansh Tiwari](https://x.com/suryanshti777/status/2056022182560665602) — 2026-05-18: Highlights Anthropic's official 'claude-code-setup' plugin that scans a project and recommends hooks, skills, MCP servers, subagents, and automations (/plugin install claude-code-setup@claude-plugins-official). A Community Note corrects the post: the plugin is read-only — it recommends but does NOT install or modify files.

- [Jaynit Makwana](https://x.com/jaynitmakwana/status/2055594459426070640) — 2026-05-18: Turns Barbara Oakley's 'Learning How to Learn' science (rereading and highlighting don't work; intuition about learning misleads) into 10 Claude prompts that build a personalized study system from how the brain actually acquires skill.

- [klöss](https://x.com/kloss_xyz/status/2055477217552142782) — 2026-05-16: Seven production-grade /goal templates (Ideation/Interrogation, Planning & Documentation, Build & Implementation, Refactoring, Consolidation, Hardening, Migrations; use 1-3 in order, 4-7 as needed), building on the argument that /goal is the best command in Codex/Claude Code/Hermes and most use it wrong.

- [nader dabit](https://x.com/dabit3/status/2055319214202777894) — 2026-05-15: 'Agent Hooks: Deterministic Control for Agent Workflows' — hooks attach handlers to lifecycle points (SessionStart, UserPromptSubmit, PreToolUse, PostToolUse, Stop, SessionEnd) so scripts/tests/policy run every time instead of relying on the model to remember. Operating model: event → matcher → handler → outcome. Rule of thumb: 'always/never/block/record/run/verify' belongs in a hook. Includes a demo and per-runtime notes (Claude Code, Codex, Cursor, Devin); layer prompts (guidance) with hooks (controls), CI, and human review.

- [0xMarioNawfal](https://x.com/roundtablespace/status/2055268207221682640) — 2026-05-15: SocratiCode — local zero-config tool giving AI agents semantic understanding of an entire codebase (dependency graphs, symbol-level impact analysis, cross-project search). Claimed numbers: 61% less context, 84% fewer tool calls, 37x faster than grep-based exploration, tested on 40M LoC. Fully local, free.

- [Khairallah AL-Awady](https://x.com/eng_khairallah1/status/2055215784092401966) — 2026-05-15: Thread about Anthropic's May 6, 2026 multi-agent orchestration announcement (Code with Claude event): Claude Managed Agents can now run up to 20 specialized agents in parallel on a single task. Cites Netflix (parallel build-log analysis), Harvey (multi-document legal coordination), and Shopify (pushing toward 90% autonomous coding by Q3 2026) as production users. Good signal that parallel sub-agent orchestration is going mainstream.

- [charmaine](https://x.com/charmaine_klee/status/2055106811225931883) — 2026-05-15: Anthropic engineer sharing the team's learnings on how Claude Code works in LARGE codebases — best practices and where to start. Links to the official Anthropic blog post: claude.com/blog/how-claude-code-works-in-large-codebases-best-practices-and-where-to-start. Direct, no hype.

- [Anatoli Kopadze](https://x.com/anatolikopadze/status/2054568935274549597) — 2026-05-15: 18-step listicle on getting more out of Claude (2.4M views). Step 1 — use Projects, not bare chats, so context persists across conversations; later steps cover memory, custom instructions, integrations, and workflows. Listicle framing is engagement-farmy but several tips are practical Claude.ai usage patterns worth knowing.

- [Khairallah AL-Awady](https://x.com/eng_khairallah1/status/2054211760631185485) — 2026-05-14: Hype-styled promo pointing to a free 30-min Boris Cherny (creator of Claude Code) walkthrough plus the author's own 'turn Claude into a full-time AI employee in 7 days' course. The Cherny session is the real link worth chasing; the framing is engagement-farmed.

- [darkzodchi](https://x.com/zodchiii/status/2054526937561796939) — 2026-05-13: Pointer to an Anthropic-engineer video on the 7 Claude Code mistakes that waste tokens — model switching, context management, settings that halve token usage. Key data point: Claude Code resends the full conversation history every turn, so a 30-message session can burn 232K tokens. Every MCP server, skill, and read file rides along.

- [Avi Chawla](https://x.com/_avichawla/status/2054493154045567400) — 2026-05-13: Direct comparison of Anthropic's three Claude surfaces: Chat (for thinking — conversational, no local file access), Code (for building — CLI, dev-focused), Cowork (for doing — desktop, agentic file/task automation). Useful framing for choosing the right surface per task.

- [Ihtesham Ali](https://x.com/ihtesham2005/status/2054458335215395223) — 2026-05-13: Google + Meta paper: Claude Code autonomously proposes, tests, and refines algorithms for improving LLM reasoning over 5 rounds with no human in the loop. Discovers a 4-mechanism controller (EMA momentum stopping, coupled width-depth control, alignment-aware depth allocation, conservative branch abandonment) for $39.90 total compute. Paper at arxiv.org/abs/2605.0xxx.

- [GREG ISENBERG](https://x.com/gregisenberg/status/2054261832718889216) — 2026-05-13: Free 47-minute course on building a managed AI-agent business solo. Pitch: sell "unlimited agents/infrastructure" as digital employees, don't niche too early, every executive has the same problems (emails, meetings, follow-ups). Stack: Hermes Agent (harness), Codex or Claude Code (build), Orgo (cloud computer sandboxes per agent), Composio (one-click auth), Obsidian (docs).

- [コムテ (Komte)](https://x.com/commte/status/2054136870016356408) — 2026-05-13: Google open-sourced 13 official Agent Skills (github.com/google/skills) compliant with the Agent Skills standard — interoperable with Claude Code, Antigravity, Gemini CLI, Cursor, GitHub Copilot, and other major agents. Significant cross-vendor signal for the Agent Skills standard.

- [Ronin](https://x.com/deronin_/status/2054255152555545079) — 2026-05-12: Ten token-waste mistakes senior AI engineers stopped making — auto-context loading 50 files for a 30-line fix ($1.20/turn waste), defaulting Opus on lint/format/rename ($0.60 vs Haiku $0.02), tool-call loops resending the full repo on retry, defaulting to Sonnet when Kimi 2.6 matches at 1/6 cost, streaming on stable-prefix workflows killing prompt cache, "just-in-case" file includes blowing 80K-token prompts. Karpathy-quote framing.

- [klöss](https://x.com/kloss_xyz/status/2054096165055217987) — 2026-05-12: Detailed /goal prompt template for Codex / Claude Code / Hermes with structured slots: GOAL (single measurable outcome), CONTEXT, CONSTRAINTS, PRIORITY, PLAN (understand first), DONE WHEN, VERIFY (tests/build/lint/typecheck). Aimed at killing scope creep and ranking uncertainty before acting. Directly usable.

- [Muhammad Ayan](https://x.com/socialwithaayan/status/2053875867487777175) — 2026-05-12: Engagement-farmed announcement (all-caps 'BREAKING') that Anthropic open-sourced a Claude Code plugin suite for finance workflows — DCF/LBO models, equity research, M&A analysis, KYC, IC memos — with MCP connectors for Bloomberg, FactSet, S&P Global, Morningstar, and PitchBook (github.com/anthropics/financial-services, Apache-2.0, ~19.8K stars). Top replies flag the obvious caveat: the harness is free but the data feeds (Bloomberg Terminal ~$28K/yr, FactSet/S&P/PitchBook six-figure) are not, and the agents draft work for human sign-off rather than autonomously owning workflows.

- [Garry Tan](https://x.com/garrytan/status/2053127519872614419) — 2026-05-10: Long-form X article "Meta-Meta-Prompting: The Secret to Making AI Agents Work" — Garry Tan argues to stop treating AI as a chat window and start treating it as an OS. Part of his Fat Skills/Fat Code/Thin Harness series. Open source: github.com/garrytan/gbrain and github.com/garrytan/gstack. Concrete "book mirror" example uses sub-agents per chapter that map ideas to your actual life context. 1.2M views.

- [Mnimiy](https://x.com/mnilax/status/2053116311132155938) — 2026-05-10: Long-form post: Karpathy's 4-rule CLAUDE.md template (born Jan 2026 from his thread on Claude failure modes — silent wrong assumptions, over-complication, orthogonal damage) cut mistakes from ~40% to <3% across 30 codebases over 6 weeks. Forrest Chang's repo hit 120K stars. Author argues the template only fixes Jan code-writing problems; he adds 8 more rules targeting May 2026 agent-orchestration issues (agent fights, hook cascades, skill loading conflicts, multi-step workflows). Notes CLAUDE.md is advisory (~80% compliance); past 200 lines compliance drops sharply. 2.5M views.

- [Axel Bitblaze](https://x.com/axel_bitblaze69/status/2052520764545613958) — 2026-05-08: claude-handoff plugin (install: /plugin marketplace add willseltzer/claude-handoff && /plugin install handoff) — three commands (/handoff:create, /handoff:quick, /handoff:resume) that generate a HANDOFF.md with full session state (branch, commits, files touched, dead ends) so a fresh Claude Code session can pick up where the old one ended. Targets the 10-20 message context-degradation point Anthropic recommends restarting at.

- [Avi Chawla](https://x.com/_avichawla/status/2052482874126020882) — 2026-05-08: Avi Chawla on Karpathy's 'remove yourself as the bottleneck' framing and Rowboat — an open-source AI 'second brain' built on the Markdown/Obsidian foundation Karpathy uses, extended to work context (emails, meetings, decisions, commitments). The pitch: most people can't act on Karpathy's advice because their AI has no memory of their work, and Rowboat is one open-source answer to that.

- [Tom Dörr](https://x.com/tom_doerr/status/2052440598452359394) — 2026-05-08: Tom Dörr surfaces 'agentmemory' (github.com/rohitg00/agentmemory) — a knowledge-graph memory layer for Claude Code. Pair with the other agent-memory tools in the corpus (HelixDB, turbovec, mem0).

- [darkzodchi](https://x.com/zodchiii/status/2052400272840720565) — 2026-05-08: Hype-style pointer to a 22-minute Anthropic Claude team talk on their 2026 agent roadmap — tools, memory, observability, builder-state-of-the-art. Last 3 minutes called out as especially worth watching. Quote-tweets the author's own article on agent reliability (AI agent breaking at 2am, sending 47 broken emails over the weekend, burning $340 in API calls).

- [Rohit Ghumare](https://x.com/ghumare64/status/2052313902214476192) — 2026-05-08: Rohit Ghumare highlights agentmemory — a memory layer for Hermes / Claude Code / Codex that records session observations, compresses them with AI, and injects relevant context back into future sessions. Claims 95% fewer tokens per session and 200x more tool calls before hitting context limits, benchmarked on 240 real coding sessions. MIT-licensed, ~1,000 GitHub stars in its first week. Worth evaluating as a CLAUDE.md alternative for long-running agent work.

- [0xSero](https://x.com/0xsero/status/2050544304360165585) — 2026-05-02: Reminder that Claude Code session history is auto-deleted monthly unless you change settings.json — that's all valuable training/context data. 0xSero shares a backup repo (github.com/0xSero/ai-data-extraction) to help you preserve it.

- [darkzodchi](https://x.com/zodchiii/status/2050537397377532341) — 2026-05-02: Promotes a security article + .gitignore template after citing that Anthropic allegedly leaked 512K lines of source code from a missing .gitignore entry. Boris Cherny (Claude Code creator) cited as the cautionary tale. Engagement framing, but the .gitignore best-practices angle is legitimately useful.

- [Blaze](https://x.com/browomo/status/2050509770604331510) — 2026-05-02: French teenager built a 3D map of 217 mental models (1284 connections) controlled by hand gestures + voice, running Three.js + MediaPipe Hands + local Whisper + Claude API + Google Antigravity. Whole stack assembled in one weekend; 80ms gesture-to-graph latency, runs from a 47MB Obsidian vault on a regular laptop.

- [Om Patel](https://x.com/om_patel5/status/2050441119003971683) — 2026-05-02: Promoted Claude Code skill /graphify that pre-builds a graph of your codebase (functions, deps, docs, PDFs, images, audio, video via Whisper) so Claude doesn't waste tokens exploring. Author claims '71.5x more efficient' (engagement-farming framing).

- [Akshay](https://x.com/akshay_pachaar/status/2050201509821063576) — 2026-05-01: Walkthrough of why Claude skills fail silently and how progressive disclosure works: Tier 1 = YAML frontmatter (~100 tokens, always loaded), Tier 2 = SKILL.md body (loads on trigger from description), Tier 3 = bundled scripts (loaded on demand, only stdout enters context). Description quality determines triggering.

- [ClaudeDevs](https://x.com/claudedevs/status/2047086372666921217) — 2026-04-23: Anthropic ClaudeDevs blog post: 'Building agents that reach production systems with MCP' (claude.com/blog/building-agents-that-reach-production-systems-with-mcp). Covers when agents should use direct APIs vs CLIs vs MCP, patterns for building MCP servers, context-efficient client design, and pairing MCP with skills. Direct first-party reading for any agent-to-production pipeline work.

- [Garry Tan](https://x.com/garrytan/status/2046882636069798323) — 2026-04-23: Garry Tan: 'Basically how I'm building all my features these days: Do it once in OpenClaw, then just run /skillify and it does it like that forever.' Quote-tweets his own article on stopping agents making the same mistakes (contrasts with LangChain's $160M/3yr/LangSmith trajectory-evals stack). Fits the skills-as-routines thread.

- [Avi Chawla](https://x.com/_avichawla/status/2046685172666712571) — 2026-04-23: Avi Chawla reports 3x token reduction on Claude Code (10.4M → 3.7M tokens, 10 errors → 0, $9.21 → $2.81) by using Insforge Skills + CLI (github.com/InsForge/InsForge) as a backend context-engineering layer — without changing CLAUDE.md, prompts, or models. Open-source and local. Worth measuring against on a real session.

- [Vox](https://x.com/voxyz_ai/status/2045899539526148193) — 2026-04-21: The #1 GitHub trending repo this week (44,465 stars) is a CLAUDE.md file distilling Andrej Karpathy's LLM coding pitfalls into 4 principles: (1) think before coding — ask when unsure, (2) simplicity first — minimum code, (3) surgical edits — only touch what's required, (4) goal-driven — translate fuzzy instructions into verifiable targets. Directly actionable as a CLAUDE.md system prompt.

- [AYi](https://x.com/ayi_ainotes/status/2045874192155824616) — 2026-04-20: AYi (translated from Chinese) recaps OpenMythos, an open-source first-principles reconstruction of Anthropic's "Claude Mythos" as a looped/recurrent transformer with MoE routing: the same weights run ~16x per forward pass so reasoning happens silently in latent space. Argues a 770B recurrent model can match a 1.3T standard model and that future scaling competes on loop-count rather than parameter count.

- [Akshay](https://x.com/akshay_pachaar/status/2045404494641733962) — 2026-04-18: Akshay summarizes a UCL paper (arXiv:2604.14228) dissecting Claude Code's architecture: only 1.6% of the codebase is AI decision logic while 98.4% is operational harness (permission gates with 7 modes, tool routing, a 5-layer context compaction pipeline, subagents that return only summaries). Core thesis: as frontier models converge on raw coding ability, harness quality, not the model, becomes the differentiator.

- [Alex Ker](https://x.com/thealexker/status/2045203785304232162) — 2026-04-18: Alex Ker's deep-dive guide on optimizing AI coding harnesses: keep config/.md files lean and human-written (frontier LLMs hit a "dumb zone" past a few hundred instructions), use progressive disclosure for CLIs/skills/MCP tools, structure prompts with HumanLayer's Research-Plan-Implement (R.P.I.) framework, and use subagents (parallel fan-out for breadth, pipelines for depth) to keep the main context clean. Core argument: the harness, not the model, is where engineering judgment compounds, so commit to one and iterate.

- [0xSero](https://x.com/0xsero/status/2044879665001595263) — 2026-04-17: 0xSero (quote-tweeting Sarah Chieng's article 'Single-agent AI coding is a nightmare for engineers') says he's gone 180 on multi-agents/subagents after analyzing hundreds of AI coding agent sessions — they actually help a lot. Practitioner's change-of-mind about orchestration.

- [Millie Marconi](https://x.com/milliemarconnni/status/2044358003714097601) — 2026-04-15: Uses Claude as a full inversion engine running Charlie Munger's method — mapping every path to failure to make the path to success obvious by elimination. Shares 5 prompts for applying systematic inversion to any problem.

- [klöss](https://x.com/kloss_xyz/status/2044169678961234282) — 2026-04-15: klss argues agents fail across repos because of unstructured markdown, and proposes a four-folder convention to remove ambiguity: /audits (proof), /docs (description), /plans (intent), /specs (law). Separating intent from proof from law stops Claude Code, Codex, and Cursor agents from hallucinating context.

- [Paul Bakaus](https://x.com/pbakaus/status/2044118871326765541) — 2026-04-15: Paul Bakaus praises Matt Sims (English PhD plus ML/startup background) for building in the open at the intersection of creativity, storytelling, and AI. Quote-tweets Sims on teaching Claude Code to think systematically, getting consistent answers to recurring review-for-security / sufficient-tests / update-instruction-files prompts.

- [Indie Fox](https://x.com/indie_maker_fox/status/2043857352282255829) — 2026-04-15: Indie Fox praises a Claude skill that generates very high-quality software architecture diagrams (github.com/Cocoon-AI/architecture-diagram-generator), showing an OpenHarness architecture diagram as an example of its clean output.

- [Phil Chen](https://x.com/philhchen/status/2043759400121458922) — 2026-04-14: 'How I built Filbert' — a background coding agent that is a lightweight wrapper around an existing harness running on the team's own infra with full dev-env access and recursive self-improvement. Per the linked article it wrote 95% of the team's PRs in a week and runs 14 scheduled jobs daily (bug triage, security audits, dead-code sweeps, CI optimization). Strong template for self-hosted background agents.

- [Kevin Simback](https://x.com/ksimback/status/2043745657748361476) — 2026-04-14: 'My Second Brain Setup: A Modified Karpathy Method' — builds on Karpathy's LLM-knowledge-base pattern (LLM incrementally compiles sources into an interlinked markdown wiki; LLM=programmer, wiki=codebase, Obsidian=IDE) and adds a two-author rule: an `author: kevin` vs `author: agent` frontmatter field where human-authored files are untouchable. Runs on Claude Code with five slash commands (/research fanning out 5-8 parallel agents, /ingest, /wiki-query, /wiki-lint, /wiki-output) and a 'graduation' loop that promotes good agent pages into the protected human layer.

- [Alex Finn](https://x.com/alexfinn/status/2043719233213980922) — 2026-04-14: Alex Finn shares a SOUL.md prompt philosophy inspired by Garry Tan's post: demand completeness over 'good enough,' never table things for later when the permanent solve is in reach, always ship with tests and documentation. Includes a copy-paste prompt for OpenClaw/Hermes agents.

- [Tech with Mak](https://x.com/technmak/status/2043683120319520806) — 2026-04-14: Distills three Karpathy critiques of coding agents (wrong assumptions unchecked, overcomplication/bloat, editing code they don't understand) into a drop-in CLAUDE.md with four principles: (1) think before coding / surface ambiguity and push back, (2) simplicity first / no unrequested abstractions, (3) surgical changes / don't touch adjacent code, (4) goal-driven execution / turn tasks into failing tests then loop to green. Practical, copy-paste engineering guardrails.

- [Noisy](https://x.com/noisyb0y1/status/2043609541477044439) — 2026-04-14: Noisy describes a Google engineer who automated 80% of his work with Claude Code using a CLAUDE.md file based on Karpathy's principles and a .NET orchestration app. Covers the Karpathy-inspired CLAUDE.md, a dotnet service that spawns Claude Code instances with git worktrees, and a review pipeline. Claims $28K passive income working 2-3 hours/day.

- [Garry Tan](https://x.com/garrytan/status/2043581361798500602) — 2026-04-13: Garry Tan adds 'Boil the ocean' to his SOUL.md: the marginal cost of completeness is near zero with AI. Do the whole thing with tests, docs, and quality. Never table for later, never present workarounds, never leave dangling threads. 433.1K views.

- [Nick Spisak](https://x.com/nickspisak_/status/2043060265823146202) — 2026-04-12: Nick Spisak explains Claude Code's new /ultraplan feature: 4 Opus agents plan in parallel (3 explorers + 1 critic) on Anthropic's cloud. Covers when the review workflow matters more than speed, 5 scenarios preventing hours of rework, and when to skip it for local plan mode instead. 250.3K views.

- [Alpha Batcher](https://x.com/alphabatcher/status/2042606770816704643) — 2026-04-10: Distills architectural principles for production AI agents by quoting Rohit's article reverse-engineering Claude Code's architecture (github.com/rohit4verse). Key patterns: async generators for streaming, parallel read-only tools vs serial write tools, tools executing during generation (not after), system prompt designed for cache efficiency, hierarchical context compaction cheapest-first, isolated worktree per sub-agent. Calls it the most detailed public breakdown of a production agent architecture available.

- [Teknium](https://x.com/teknium/status/2042396576245825543) — 2026-04-10: Teknium claims Anthropic copied their "notify when done" feature from Hermes Agent (github.com/NousResearch/hermes-agent/pull/5779) — lets background processes notify the agent when finished instead of polling, so the agent can work on other tasks in the same session. Points to Claude Code's new Monitor tool as the equivalent. Makes the case that open source moves faster than closed companies.

- [Aakash Gupta](https://x.com/aakashgupta/status/2042334495664455848) — 2026-04-10: The "advisor pattern" for AI agent cost optimization: run Sonnet for routine execution ($3/$15 per MTok) and fire a tool call to Opus only for genuine decision points. Both models share full context, eliminating the fragmentation problem in multi-model architectures. Claude Code has been doing this internally. Practical architecture for any company hitting the cost wall with frontier models in production agent loops.

- [Seb Goddijn](https://x.com/sebgoddijn/status/2042286523001737545) — 2026-04-10: Ramp hit 99% AI adoption company-wide but found most employees stuck in chat windows while power users ran laps. They built "Glass" — an internal AI productivity suite on Anthropic's Claude Agent SDK — reaching 700 DAUs in one month. Philosophy: raise the floor for all employees rather than lowering the ceiling for power users.

- [Avid](https://x.com/av1dlive/status/2042172428127002906) — 2026-04-10: Recommends a 16-minute talk by two Anthropic engineers who built Claude Skills, paired with a comprehensive guide by @eng_khairallah1 on building Claude Skills that actually work. Notes that most of the 80,000+ skills in the community registry are poorly built — this guide covers what separates the good from the bad.

- [carsonfarmer](https://x.com/carsonfarmer/status/2042038527639068763) — 2026-04-09: Points out that Anthropic's new managed agents API closely mirrors the Letta/MemGPT API that's been open-source for a year — including read-only memory blocks and memory block sharing. Quoting Sarah Wooders (Letta co-creator) who calls it closed-source with provider lock-in.

- [0xMarioNawfal](https://x.com/roundtablespace/status/2040500903296352663) — 2026-04-06: Comprehensive open-source Claude Code setup with 27 agents, 64 skills, 33 commands, and built-in AgentShield with 1,282 security tests. Handles planning, code review, fixes, TDD, and token optimization. Works across Cursor, OpenCode, and Codex CLI. github.com/affaan-m/everything-claude-code

- [Ejaaz](https://x.com/cryptopunk7213/status/2040434869399138368) — 2026-04-05: Open-sourced self-improving AI agent framework: a meta-agent that autonomously tweaks an agent's harness (tools, system prompts), runs tests, and iterates until it tops benchmarks. Demonstrated on TerminalBench (code) and spreadsheets (financial modeling), reaching #1 in both domains in under 24 hours using Claude evaluating Claude for better failure analysis.

- [Meta Alchemist](https://x.com/meta_alchemist/status/2038222105654022325) — 2026-03-29: Detailed guide on turning Claude Code into a self-evolving system. The approach captures corrections across sessions so the CLI learns and improves over time, building persistent memory of what works and what doesn't for each project.

- [Poonam Soni](https://x.com/codebypoonam/status/2036517669684519362) — 2026-03-25: Teaser thread claiming Anthropic demonstrated a 3-agent system that builds production-quality apps from a single prompt in under 6 hours without human intervention. Architecture details promised in thread. Engagement-farming format ('Breaking') but the underlying multi-agent app-building claim is worth verifying.

- [Greg Pstrucha](https://x.com/grichadev/status/2036472210152718504) — 2026-03-25: Greg Pstrucha demonstrates how malicious Claude Code skills can hide instructions inside PNGs and abuse Claude Code's 'expand output' feature to fool both humans and agents — a real security threat. He improved `skill-scanner` (also available via Sentry's Warden at warden.sentry.dev) to catch these attack vectors. Only install skills from trusted sources.

- [Denis Yurchak](https://x.com/denisyurchak/status/2036422883350544519) — 2026-03-25: Denis Yurchak shares a Claude prompt (.md file) that fully automates secure Hetzner VPS setup in one shot — configures SSH hardening, fail2ban, UFW firewall, and optionally Tailscale. Buy the server, install Claude, paste the prompt. Open source, PRs welcome. Practical Claude-as-sysadmin pattern.

- [Millie Marconi](https://x.com/milliemarconnni/status/2036363493478375797) — 2026-03-25: A Claude Code skill (/last30days) scans Reddit and X from the past 30 days on any topic and generates copy-paste-ready prompts based on what's actually working in the community right now — not months-old advice. Works for any domain (Midjourney, Cursor rules, legal prompts, etc.). Open source, MIT license.

- [hoeem](https://x.com/hooeem/status/2035762966952382646) — 2026-03-22: hoeem re-promotes his 'I want to become a Claude Architect (full course)' article covering Claude Code, the Claude Agent SDK, the Claude API, and MCP; framed for engagement ('Be the 1%', 110k+ bookmarks).

- [Kshitij Mishra](https://x.com/daievolutionhub/status/2035396799704547453) — 2026-03-22: Kshitij Mishra shares a 'Claude Code Setup Cheatsheet' based on Boris (creator of Claude Code), quoting Shruti Codes' '2026 AI Engineer roadmap' article; 'Save this' engagement framing.

- [Akshay](https://x.com/akshay_pachaar/status/2035341800739877091) — 2026-03-22: Akshay Pachaar's guide 'Anatomy of the .claude/ folder' walks through CLAUDE.md, custom commands, skills, agents, and permissions and how to set them up properly, framing .claude as the control center for how Claude behaves in a project (instructions, commands, permission rules, and cross-session memory).

- [felpix](https://x.com/felpix_/status/2033249213614538804) — 2026-03-21: felpix reports filing taxes end-to-end with Claude + FreeTaxUSA: dropped a W-2, several 1099-NECs and 1099-Bs plus expense/budget spreadsheets in a folder, asked Claude to itemize and optimize expenses, and let it use Chrome to submit — the return was accepted. (Directly relevant: FreeTaxUSA is TaxHawk's own product.)

- [Corey Ganim](https://x.com/coreyganim/status/2034717504505823728) — 2026-03-20: Corey Ganim's playbook for running a one-person 'AI company' stacks three free tools: Paperclip (npx paperclipai — assigns work and tracks progress), gstack (15 specialist Claude Code skills from Garry Tan, with /office-hours, /review, /qa, /ship commands), and autoresearch (Karpathy — 100 overnight experiments); the move is running 10-15 gstack commands in parallel. Quotes Nick Spisak's Paperclip follow-up article.

- [Ole Lehmann](https://x.com/itsolelehmann/status/2033982679423848802) — 2026-03-18: Ole Lehmann shares a single skill that auto-improves any other skill using Karpathy's autoresearch method: it runs the skill and scores the output, finds what's failing, makes one small change to the skill prompt, re-runs to check the score, keeps or reverts the change, and repeats until the skill works. Article: 'How to 10x your Claude Skills'.

- [Thariq](https://x.com/trq212/status/2033949937936085378) — 2026-03-18: Thariq (Anthropic) shares 'Lessons from Building Claude Code: How We Use Skills' — which skills are worth making, the secret to writing a good one, and when to share them — noting Anthropic runs hundreds of skills internally and that the common 'skills are just markdown files' misconception undersells them.

- [Rohit](https://x.com/rohit4verse/status/2033945654377283643) — 2026-03-18: Rohit's essay 'The Harness Is Everything: What Cursor, Claude Code, and Perplexity Actually Built' argues you're not using AI wrong because of the model — you're using it wrong because you haven't built the right environment; the difference between teams shipping millions of lines and those struggling is the harness, not GPT-5 vs Claude Opus, temperature, or the prompt.

- [0xMarioNawfal](https://x.com/roundtablespace/status/2033238044900298844) — 2026-03-16: 0xMarioNawfal amplifies Corey Ganim's article 'Ultimate Claude Cowork Starter Pack: Every Plugin, Skill, and Workflow You Need,' which argues most people install Claude Cowork, poke around for 10 minutes, and revert to ChatGPT because the setup is the hard part.

- [Beacon](https://x.com/0xxbeacon/status/2033224402070810940) — 2026-03-16: Beacon links Anthropic's Skilljar course catalog (anthropic.skilljar.com) and the access-request page for the Claude Certified Architect: Foundations certification.

- [Garry Tan](https://x.com/garrytan/status/2032196172430131498) — 2026-03-13: Garry Tan shares a CTO's testimonial that his open-source gstack ('god mode') flagged a subtle cross-site-scripting vulnerability the team wasn't aware of, predicting 90%+ of new repos will adopt it. gstack is MIT-licensed at github.com/garrytan/gstack and installs into local Claude Code and into a repo for teammates with two pastes.

- [Ming "Tommy" Tang](https://x.com/tangming2005/status/2031358195558658266) — 2026-03-11: Tommy Tang's single biggest CLAUDE.md improvement: when a bug is reported, don't start by fixing it. Start by writing a test that reproduces the bug, then have subagents try to fix it and prove the fix with a passing test.

- [Boris Cherny](https://x.com/bcherny/status/2031089411820228645) — 2026-03-10: Boris Cherny announces Code Review in Claude Code: when a PR opens, a team of agents runs a deep review to hunt for bugs. Built internally first because code output per Anthropic engineer is up 200% this year and review had become the bottleneck; he says it catches many real bugs he'd otherwise miss.

- [Anish Moonka](https://x.com/anisha_moonka/status/2030015356383691121) — 2026-03-07: Anish Moonka's 12-point notes from Boris Cherny (Head of Claude Code) on Lenny's Podcast: coding is largely solved (Boris ships 10-30 PRs/day, no hand-written code since Nov 2025); the next frontier is AI deciding what to build; productivity per Anthropic engineer is up 200%; underfund teams on purpose; give engineers unlimited tokens; the Bitter Lesson favors general models over rigid orchestration; build for the model six months out; latent demand is the best product signal; 'software engineer' is becoming 'builder'; mechanistic interpretability enables layered safety; and 70% of engineers/PMs enjoy their jobs more now.

- [Nate.Google](https://x.com/nate_google_/status/2029941042133262721) — 2026-03-07: Nate.Google highlights a walkthrough he calls the best guide to Claude Cowork, wishing such hands-on guides existed when he started with AI.

- [Jayden](https://x.com/thejayden/status/2029899328400109732) — 2026-03-06: Jayden recommends an article on building a "Chief of Staff" with Claude Code, calling it one of the best real-world examples of agentic systems he has seen.

- [Daniel San](https://x.com/dani_avila7/status/2029399100240674929) — 2026-03-05: Points to a full Skill in the Anthropic repo as a reference for SKILL.md structure and language support, arguing every company should maintain an internal repository of reusable Skills and components.

- [Dickson Tsai](https://x.com/dickson_tsai/status/2029235808235078095) — 2026-03-05: Dickson Tsai (Anthropic) announced HTTP hooks in Claude Code — a more secure, easier alternative to command hooks: CC POSTs each hook event to a URL you choose and awaits a response, so you can build a web app to view progress, manage permissions, run hook logic server-side, and manage state across agents via a DB. Works everywhere hooks are supported, including plugins, custom agents, and enterprise managed settings. Docs: code.claude.com/docs/en/hooks

- [Nate.Google](https://x.com/nate_google_/status/2028836031932355067) — 2026-03-04: Nate.Google recommends what he calls the most valuable channel for learning everything about Claude.

- [klöss](https://x.com/kloss_xyz/status/2028237936848994369) — 2026-03-02: Flags Anthropic's free AI academy — 13 courses with official certificates covering MCP, APIs, Claude Code, and AI fluency, at anthropic.skilljar.com. Hype framing ('stop what you're doing') but a genuinely useful free resource.

- [Joseph Thacker](https://x.com/rez0__/status/2027448137133264955) — 2026-03-01: Argues bug bounty / security research changed step-function fast in late 2025: coding agents went from not working to genuinely working. Example: pointed Claude Code at a target's scope (enumerate subdomains, analyze JS bundles, fuzz, test IDORs/GraphQL, write an HTML report); it ran ~30 min, self-recovered from auth/WAF errors, and returned two confirmed vulns. Hunters now build and share custom Claude Code skill libraries (JS static analysis, authenticated fuzzing, IDOR, GraphQL introspection). Quote-tweets Karpathy's parallel observation about programming.

- [Thariq](https://x.com/trq212/status/2027463795355095314) — 2026-02-28: Anthropic's Thariq on building Claude Code: designing an agent's action space is an art. Walks through the AskUserQuestion tool's evolution (ExitPlanTool param → output-format parsing → dedicated tool), the shift from TodoWrite to the Task tool as models improved, replacing RAG with a Grep search tool so Claude builds its own context, progressive disclosure via Skills, and the Claude Code Guide subagent. Lesson: revisit tool assumptions as capabilities grow; experiment, read outputs, 'see like an agent.'

- [Sudo su](https://x.com/sudoingx/status/2027264446989848613) — 2026-02-27: Practical steering tips for local coding agents: tell the model its own architecture/constraints (e.g. Qwen3.5 fires 8 of 256 experts/token), give project structure over single prompts, iterate in layers (scaffold → refine → polish), let it debug its own failures, and use long context (262K) to hold the whole project. Notes Claude Code as a solid harness and that llama.cpp merged native Anthropic endpoints (no proxy/LiteLLM). Argues the skill gap in local inference is now the harness and steering, not the models — all on a single RTX 3090.

- [SightBringer](https://x.com/_the_prophet__/status/2027235489930191056) — 2026-02-27: Critique of AI auto-memory (quote-tweeting Anthropic's Claude auto-memory announcement) as a "power grab disguised as convenience": capturing your patterns, defaults, and definitions of 'good' shifts the model from serving you to shaping you, and dependency is the business model. Counter-playbook: treat memory as a controlled instrument — scope it like permissions, separate persona from operations, keep a purge cycle, audit what the model believes about you, and never let it silently rewrite your intent. Frames the AI era as shifting from intelligence to custody of context/continuity.

- [Machina](https://x.com/exm7777/status/2026666140987175221) — 2026-02-27: Engagement-farming post ('the ONLY skill you will ever need for Claude, Codex or Openclaw', 'this skill will change your life') quote-tweeting the author's own X article. Behind the hype the underlying topic is a meta-skill/prompting framework meant to change how AI reasons for you; content quality behind the clickbait is unverified.

- [Aakash Gupta](https://x.com/aakashgupta/status/2026367615602667784) — 2026-02-25: Aakash Gupta, building on a Karpathy quote, argues agents are the new distribution channel for software: they call CLIs and MCP servers and read docs programmatically rather than browsing marketing sites. MCP hit 97M monthly SDK downloads and 10k+ servers in a year and was donated to the Linux Foundation. Winners of the next 24 months build agent-accessible surface area (CLIs, MCP endpoints, machine-readable docs) now.

- [Matt Pocock](https://x.com/mattpocockuk/status/2026296080602673316) — 2026-02-25: Matt Pocock observes that AI coding rewards a 'lead dev' mentality: developers who spent their careers leveling up teammates through API design, feedback loops, and architecture find working with AI natural, while those who optimized only their own output find it uncomfortable.

- [Dr Milan Milanović](https://x.com/milan_milanovic/status/2025835518207127968) — 2026-02-23: Milan Milanović makes the case for git worktree (shipped in Git 2.5, July 2015): check out multiple branches into separate directories that share one .git, avoiding stashing and duplicate clones. The standout modern use case is AI agents - give each of 3-5 parallel Claude Code/Cursor/Codex agents its own isolated worktree and branch so they don't overwrite each other.

- [Charly Wargnier](https://x.com/datachaz/status/2024803152730423685) — 2026-02-20: Charly Wargnier argues writing crystal-clear instructions for machines is the new 10x dev skill, and the most important file in a repo is now CLAUDE.md rather than the code. Top devs use it as an AI onboarding doc to define agent behavior: force the AI to verify its own work, auto-fix CI bugs, and reject hacky fixes.

- [Aman](https://x.com/amank1412/status/2023754885473394918) — 2026-02-19: Aman shares Garry Tan's (CEO of Y Combinator) CLAUDE.md prompt for Claude Code, which he uses to ship 4,000+ line features with full tests in about an hour. The prompt makes Claude act like a senior engineer: judge whether a plan is over/under-engineered before coding, do a structured review (architecture -> code quality -> tests -> performance), present tradeoffs with opinionated recommendations, and pause for feedback before implementing.

- [J.B.](https://x.com/vibemarketer_/status/2019435524532904205) — 2026-02-19: J.B. (VibeMarketer) describes a 'recursive self-improvement loop' skill for Claude: instead of prompting once and shipping, the skill generates output, scores it against explicit criteria, diagnoses weaknesses, rewrites, and re-scores until it clears the bar. Cites @maxwellfinn's image-ad skill that grades concepts on 10 criteria (thumb-stop power, curiosity gap, emotional trigger, persona recognition) and won't stop below 9/10.

- [Tech with Mak](https://x.com/technmak/status/2023990222027915746) — 2026-02-18: Tech with Mak boosts Matthew Berman's 'OpenClaw masterclass' video, in which Berman claims to have spent 2.54 billion tokens perfecting the OpenClaw coding agent and walks through 21 daily use cases (markdown files, memory system, CRM, and more). Quoted post had ~1.3M views.

- [Matt Dancho (Business Science)](https://x.com/mdancho84/status/2023738764841894352) — 2026-02-18: Matt Dancho argues that becoming a '10X engineer' now comes down to a well-crafted SKILLS.md file, teasing a thread/resource on how to build one. High-engagement post (~1.1M views) with a lead-gen hook.

- [Pavol Lupták](https://x.com/wilderko/status/2025159534159835443) — 2026-02-15: [Post unavailable - page doesn't exist]

- [Peter Steinberger](https://x.com/steipete/status/2020704611640705485) — 2026-02-09: Peter Steinberger shares a SOUL.md rewrite prompt (via Molty) to give a coding agent a stronger personality: hold strong opinions instead of hedging, delete corporate-handbook rules, never open with filler like 'Great question', enforce brevity, allow natural humor, call out bad ideas (charm over cruelty), and permit well-placed swearing.

- [vogel](https://x.com/ryanvogel/status/2016204202343571474) — 2026-01-28: ryan vogel announces that dynamic agents.md resolution is now live in OpenCode, and suggests pairing it with a /learn command for a powerful workflow; points to @rekram11's explanation of the approach.

- [Theo - t3.gg](https://x.com/theo/status/2013888279355982131) — 2026-01-25: Theo boosts Wayne Sutton's launch of opensync.dev, a tool to track OpenCode and Claude CLI coding sessions in one place: searchable history, markdown export, eval-ready datasets, and views into tool usage, token spend, and session activity across projects. Theo frames it as a model of good devrel in 2026.

- [Rohun](https://x.com/rohunjauhar/status/2012983351288692941) — 2026-01-19: Rohun open-sourced 'claude-build-workflow', a Claude Code workflow for autonomous building: you describe what you want, answer 10-15 min of interview questions, then close your laptop while an autonomous build loop runs in GitHub Codespaces and notifies your phone when done. It generates a PRD with user stories, technical architecture, edge-case analysis, story-quality validation, JSON conversion, then kicks off the build loop. Stitched together from Geoffrey Huntley's Ralph (bash-loop technique), Ryan Carson's snarktank/ralph (PRD skills, progress tracking, auto-commits, quality checks), and the BMAD Method (discovery/interview framework), adapted from Amp to Claude Code with phone notifications and one-command setup. Repo: github.com/rohunj/claude-build-workflow.

- [Ian Nuttall](https://x.com/iannuttall/status/2012833663319195970) — 2026-01-19: Ian Nuttall shares 'dotagents' (github.com/iannuttall/dotagents), a tool he built to stop the pain of switching between different agent harnesses/clients - he now runs everything from ~/.agents or .agents. Posted in reply to Theo asking for a way to sync agent skills/config across repos via symlink. PRs welcome for unsupported clients.

- [Miles Deutscher](https://x.com/milesdeutscher/status/2012237674409796036) — 2026-01-17: Miles Deutscher promotes a curated 'Claude Code Starter Pack (Part 2)' article by AI Edge - a filtered list of Claude Code tools, tutorials, and resources claimed to be the 1% worth your time. Framing leans on hype ('mega viral', 'extract alpha', 'life-changing systems'), so tagged questionable, but the underlying resource is a legitimate Claude Code tool/resource roundup.

- [giyu_codes](https://x.com/giyu_codes/status/2012420750855012428) — 2026-01-16: giyu_codes recommends cogsec (@affaan)'s article 'The Shorthand Guide to Everything Claude Code' - a complete setup after 10 months of daily use covering skills, hooks, subagents, MCPs, plugins, and what actually works. High-reach post (~806K views).

- [Gregor Zunic](https://x.com/gregpr07/status/2012052139384979773) — 2026-01-16: Gregor Zunic (Browser Use) argues 'The Bitter Lesson of Agent Frameworks': all the value is in the RL'd model, not thousands of lines of abstractions. An agent is just a for-loop of tool calls that runs until the model stops. Abstractions freeze assumptions and fight what the model already learned; agent frameworks fail because their action spaces are incomplete, not because models are weak. Their fix: start with maximal capability then restrict ('vibe-restrict' via evals). BU Agent gives the model raw Chrome DevTools Protocol + extension APIs for a near-complete action space. Also covers a minimal model-agnostic Chat wrapper (Anthropic/OpenAI/Google), ephemeral messages to keep massive DOM/screenshot state out of context, and the done() tool for explicit completion. Reliability (retries, rate limits, compaction) is ops, not the agent. Open-sourcing as agent-sdk (includes a Claude Code re-implementation).

- [Jarrod Watts](https://x.com/jarrodwatts/status/2009200810870428123) — 2026-01-08: Jarrod Watts open-sourced his 'claude-code-config' repo containing all the agents, commands, hooks, rules, skills, and plugins he's made or collected over the past few months — described as simple but effective enhancements he'll keep updating. A ready-made reference config for a team standardizing Claude Code setups.

- [Denislav Gavrilov](https://x.com/kuberdenis/status/2004934631616086417) — 2025-12-28: Denislav Gavrilov containerizes Claude Code in Kubernetes as 'Clopus-Watcher,' an autonomous monitoring agent that watches a namespace and, on application errors, writes and applies a hotfix and documents it — effectively a 24/7 on-call engineer. Repo, examples, and results at denislavgavrilov.com.

- [Claire Silver](https://x.com/clairesilver12/status/2002443560898208162) — 2025-12-21: Claire Silver highlights Unreal MCP, a free MCP server that lets you prompt Claude to build things in Unreal Engine — e.g. 'make a Victorian manor, here's a reference pic, use the assets in this folder' and it just does it. She promised a demo video and calls it '10/10 magic.'

- [Tom Dörr](https://x.com/tom_doerr/status/1996997820868366397) — 2025-12-08: Tom Dörr shares 'awesome-claude-skills' (github.com/VoltAgent/awesome-claude-skills), a curated collection of official and community-built Claude skills.

- [Ray Fernando](https://x.com/rayfernando1337/status/1992848315541823490) — 2025-11-25: Ray Fernando recommends Lee Han-Chung's 'Claude Skills deep dive' blog post (leehanchung.github.io) as the best breakdown of Claude Skills he's seen.

- [Thariq](https://x.com/trq212/status/1989061939625144388) — 2025-11-15: Thariq gives the setup commands for Anthropic's frontend-design plugin in Claude Code: add the marketplace with '/plugin marketplace add anthropics/claude-code', then '/plugin install frontend-design@claude-code-plugins'. Getting-started reply for the frontend-design plugin.

- [Dan Shipper](https://x.com/danshipper/status/1986870518046200255) — 2025-11-08: Dan Shipper recommends Kieran Klaassen's Every piece 'Teach Your AI to Think Like a Senior Engineer' (every.to/source-code) as a masterclass on coding with AI.

- [Matt Pocock](https://x.com/mattpocockuk/status/1983255353597870285) — 2025-10-29: Matt Pocock shares his favorite AI coding tip: add 'Be extremely concise. Sacrifice grammar for the sake of concision.' to your global claude.md file for noticeably better output.

- [Matt Pocock](https://x.com/mattpocockuk/status/1958179930262356032) — 2025-08-21: Praises an Anthropic context-engineering template as a solid reference for structuring context for LLMs.

- [Dan Shipper](https://x.com/danshipper/status/1957469868862677028) — 2025-08-19: Links Dan Shipper's Every essay 'My AI Had Already Fixed the Code Before I Saw It,' on AI coding agents autonomously fixing code before the developer even reviews it.

- [Asterisk (getAsterisk)](https://github.com/getAsterisk/claudia) — 2025-08-18: opcode (formerly Claudia, by Asterisk) is an open-source Tauri 2 desktop GUI and toolkit for Claude Code: visual project/session management, custom CC agents with per-agent file/network permissions and background execution, a usage/cost analytics dashboard, MCP server management (with Claude Desktop import), session timeline/checkpoints with diff and fork, and a built-in CLAUDE.md editor. Note: the repo has been renamed from getAsterisk/claudia to winfunc/opcode.

- [Imrat](https://x.com/imrat/status/1954497164589056090) — 2025-08-11: A recipe for using Claude Code as a DevOps agent with its new background jobs: run Claude in a tmux session, have it spawn a background process to tail server logs and summarize them, then a second process that pings Claude to 'check logs' on an interval.

- [Anthropic](https://github.com/anthropics/courses/tree/master/prompt_engineering_interactive_tutorial/Anthropic%201P) — 2025-04-23: Anthropic's official interactive prompt-engineering tutorial (Jupyter notebooks in anthropics/courses): a 9-chapter curriculum on prompt structure, being clear and direct, role prompting, separating data from instructions, output formatting, step-by-step reasoning, few-shot examples, and avoiding hallucinations, plus appendices on prompt chaining, tool use, and search & retrieval.

- [Tom Dörr](https://github.com/tom-doerr/dotfiles/blob/master/instruction.md) — 2025-01-04: Tom Dörr's AI-coding-agent instruction file (an AGENTS.md-style rules doc): single-letter command aliases (c=continue, rc=reduce complexity, acp=add/commit/push, t=add tests), strict engineering rules (no fallbacks, don't swallow exceptions, TDD with many asserts, uv over pip, work on git branches, keep complexity low, don't weaken the linter), and ready-to-paste DSPy optimizer snippets (BootstrapFewShotWithRandomSearch, MIPROv2, SIMBA).

- [curvedinf](https://github.com/curvedinf/dir-assistant) — 2024-06-18: dir-assistant is a pip-installable CLI that recursively indexes the text files in your directory so you can chat with them via a local or API LLM, auto-injecting the most contextually relevant files. It uses CGRAG (Contextually Guided RAG) for file selection, supports interactive and single-prompt modes (including auto file edits + git commits), many local acceleration backends and all major LLM APIs via LiteLLM, and optimizes prompt/context caching (50-90% cache hits).

### Dev Practices (255)

- [Superman](https://x.com/thesupermanmx/status/2077321341490090486) — 2026-07-16: turbovec (github.com/RyanCodrai/turbovec) is a vector index built on TurboQuant, written in Rust with Python bindings — a performance-oriented approximate nearest-neighbor index relevant to embedding search and RAG pipelines.

- [Ashpreet Bedi](https://x.com/ashpreetbedi/status/2077169299777531942) — 2026-07-15: Ashpreet Bedi (Agno) shares a new post, Self-Driving Agent Infrastructure (ashpreetbedi.com/self-driving-agent-infrastructure), arguing AI/software engineering is the first domain to gain autonomous 'self-driving' capabilities, and walking through how he built his self-driving agent platform.

- [Alvaro Videla](https://x.com/old_sound/status/2076932819008242037) — 2026-07-14: Alvaro Videla released LeetLLM (github.com/videlalvaro/leet-llm) — a free, problem-based course of 48 lessons for building a small LLM inference engine on Apple Silicon in Swift and Metal, progressing from dot products and GEMV through attention and token generation.

- [JoePro](https://x.com/joepro/status/2076877282312954311) — 2026-07-14: JoePro shares a reworked 'Frontend Design Skill' (an agent/Claude skill spec) engineered to produce distinctive, production-grade UIs that avoid recognizable AI-generated tropes — covering success criteria (signature visual identity, complete states, WCAG AA accessibility, token-driven design systems) and a context-gathering routine before writing code.

- [Jamon Holmgren](https://x.com/jamonholmgren/status/2076001786700394610) — 2026-07-13: Jamon Holmgren dumps his complete agentic coding setup as a 10+ point checklist: an AGENTS.md that acts as a router to skills/docs/tools; a customized workflow skill (he recommends grabbing Matt Pocock's skills); self-healing, greppable docs with a 7-line summary header; agents that actually run and test the app themselves; e2e tests plus docs on how/what to test; custom precommit linters with --fix that shell out to a cheaper LLM (Composer 2.5 or Sonnet) to actually fix rather than flag; cross-agent review (codex/claude/cursor, never the same model reviewing itself) at research/plan/implementation/wrap-up; handoff worksheets committed with git tags so another agent can finish the job; automatic end-of-session agent feedback docs he periodically ingests to improve workflows; a tools/bin folder of agent-authored scripts (e.g. an agent_review CLI wrapper); and periodic agent sweeps through recent commits. Practical, adoptable patterns for a team running coding agents.

- [Kodus](https://kodus.io/self-hosted-ai-code-review/) — 2026-07-09: Kodus (github.com/kodustech/kodus-ai) — open-source AGPLv3 self-hosted AI code review. The full PR-review pipeline (Kody agent) runs on your own infrastructure with bring-your-own-LLM: it posts line-anchored inline comments covering logic/security/performance (or 'deep mode' with parallel bug/security/performance specialists), keeps source code, LLM calls, and audit trails inside your VPC, and supports GitHub Enterprise Server / GitLab Self-Managed / Bitbucket DC and air-gapped deploys. Jeremy flagged it to evaluate for work code reviews.

- [Ryan Carson](https://x.com/ryancarson/status/2074093250399330418) — 2026-07-07: Ryan Carson (@HelloUntangle) details orchestrating the largest/riskiest engineering program in the company's history with a single Fable parent orchestrator session: 834 files, prod data mutation, DB schema update, 31 PRs, started Friday->completed Monday, zero prod incidents. One parent Devin/Fable session planned the work, spawned ~40 child sessions to execute, enforced regression gates and backup checks between phases, and escalated only owner-level decisions (scope rulings, go/no-go on irreversible steps). Distills reusable program-management patterns for large migrations. In a follow-up he asks Cognition to let child Devin sessions pick their own model/mode independent of the parent.

- [Satyam Pariyar](https://x.com/spariyar07/status/2074142974095835518) — 2026-07-06: Satyam Pariyar shares Kybernetes (github.com/pariyar07/kybernetes), a small OSS experiment: a 'loop governor' / runtime-adaptive control plane for agentic coding work, aimed at governing coding-agent execution loops at runtime.

- [kaize](https://x.com/0x_kaize/status/2073743517155774641) — 2026-07-06: kaize shares a 'Loop engineering' reading list, arguing 2026 agents are less about smarter prompts and more about longer runs — the real questions are whether an agent can recover from a failed step, control spend, and know when to stop. Curated links: Addy Osmani (addyosmani.com/blog/loop-engineering), Firecrawl (firecrawl.dev/blog/loop-engineering), Oracle 'What is the AI agent loop', OpenAI 'Harness engineering', and Martin Fowler 'Harness engineering for coding agent users'.

- [Elvis](https://x.com/elvissun/status/2073161303997452794) — 2026-07-05: Elvis makes a meta point about eval-driven skill building that extends beyond coding to any knowledge problem where an eval set can be concretely defined. Example: a newsjack.sh skill that judges newsworthiness — he started from labeled examples (stories that made real news vs ones that didn't, e.g. hitting #1 on Product Hunt isn't news even though LLMs say it is), fed them into an eval set, then used /goal to iterate a skill implementation that lets 3 agents (Opus, Sonnet, Haiku) all score stories correctly — proving 'the intelligence lives in the skill, not the model.' Notes Fable's ability to learn across examples and draw a through-line is well beyond Opus.

- [alex fazio](https://x.com/alxfazio/status/2073091833530392614) — 2026-07-05: alex fazio recommends studying ARC-AGI-winning harnesses to learn harness engineering from first principles — they clearly illustrate what works, what's BS, and why a lot of current harness design is overfitted to benchmark-maxxing.

- [0xSero](https://x.com/0xsero/status/2073274981279260774) — 2026-07-04: 0xSero shares Parcels (github.com/0xSero/parcels) — a tool for 'cloud agents' when you have Tailscale and more than one desktop: it packages your repo plus a live coding-agent session (Claude Code / Codex / pi), transfers it to another machine on your Tailscale network, and runs it in tmux so you can step away from the screen.

- [akira](https://x.com/realmcore_/status/2073170941878944022) — 2026-07-04: akira introduces Onyx, a VM/runtime for programmable agent orchestration that 'turns orchestration into software engineering.' The article covers the design constraints and decisions behind the VM and how to write programs and architect agent systems on it. Framing: agents are inherently non-deterministic (that's the point), but breaking execution into structured steps (Plan, Implement, Review, QA) plus scripts/tools/skills to steer, share context, and guardrail agents improves performance. References ReAct and related arxiv papers and karpathy/autoresearch.

- [Archive](https://x.com/archiveexplorer/status/2073136973162872897) — 2026-07-04: Archive (engagement framing, 'met an Anthropic engineer making $1.2M') argues the real lever isn't Opus vs Sonnet but 'what the model wakes up into' — the .claude/ folder: CLAUDE.md (the contract), settings.json (permissions), hooks/ (reflexes), agents/verifier (a shift-notes checker subagent), skills/ (~33 reusable 'muscle memories'), .mcp.json (tools), and MEMORY.md (shift log). 'You write the folder once; the folder runs the model.' Quote-tweets his own article 'Loop and Harness engineering: 7 files, 5 steps.'

- [Akshay](https://x.com/akshay_pachaar/status/2072961737008336937) — 2026-07-04: Akshay Pachaar summarizes a Hugging Face blog post on 'evolving the harness' instead of training the model: they took a frozen open model scoring 0% on a hard legal-agent benchmark, left its weights untouched, and let an automated loop rewrite only the surrounding harness code (the runtime wrapper that feeds context, runs tool calls, and decides when a run ends). It ended up essentially matching Sonnet 4.6 on the headline metric at ~7x lower cost per task, zero weights changed. The insight: the 0% wasn't measuring legal reasoning — the model reasoned correctly but saved outputs under the wrong filename/folder or not at all — so it was measuring the harness.

- [Rahul](https://x.com/sairahul1/status/2072749611471835229) — 2026-07-04: Rahul shares a free 'Loop Library' (signals.forwardfuture.com/loop-library/) of reusable agent loops, plus his article '20 Loop Design Patterns Every AI Engineer Should Know.' Framing: most engineers can build an agent (a worker) but few can build a system that gets better after the first attempt — and that gap is 'worth six figures.'

- [Dhilip Subramanian](https://x.com/sdhilip/status/2072334422414876957) — 2026-07-02: Dhilip walks through his 7-skill Claude Code setup and what each earns its spot for: data engineering (dbt/Airflow), gstack, grill-me, superpowers (spec/plan/TDD), impeccable (UI audit), last30days, and printing-press (API/site to token-light CLI). Advice: start small, add a skill only when you hit a job your current ones can't do.

- [Andrew Ng](https://x.com/andrewyng/status/2071988145667928442) — 2026-07-02: Andrew Ng's 'loop engineering' letter lays out three nested loops for building 0-to-1 products: the fast agentic coding loop (agent writes/tests/iterates every few minutes), the developer feedback loop (human steers over tens of minutes to hours), and the slow external feedback loop (alpha testers, A/B tests over days). Humans retain a context advantage, so engineers increasingly play a partial product-management role.

- [Akshay](https://x.com/akshay_pachaar/status/2071509401224261823) — 2026-06-29: Walkthrough of Google's Agents CLI as tooling for Karpathy's "agentic engineering" (spec design, eval loops, security). One setup command injects 7 ADK-specific skills into a coding agent; author built and deployed a RAG agent end-to-end with Claude Code, including 20 LLM-as-judge eval scenarios and enterprise registration.

- [zostaff](https://x.com/zostaff/status/2070852153594290195) — 2026-06-27: Long-form "Loop Engineering" article: four autonomous loops that actually pay off because the task repeats, a machine can reject the result, the agent carries it whole, and "done" is objective. Covers the bare while-loop/exit-code/budget mechanics under Claude Code Routines and four worked configs: morning CI test triage (with maker-checker subagent), dependency watchdog, doc synchronizer, and overnight research digest. Theme: the harder the verification, the more you can hand the loop; soft verification keeps a human in the loop.

- [Brian Armstrong](https://x.com/brian_armstrong/status/2070670644577280109) — 2026-06-27: Coinbase's playbook for keeping AI spend flat while token usage grows: better defaults (experimenting with cheaper open-weight models like GLM 5.2 / Kimi 2.7 via an LLM gateway, since 91% never hit caps), better routing (frontier for planning, cheaper for execution), better caching (LibreChat cache-hit rate 5% → 60%), lean context, and usage visibility. Cut AI spend nearly in half while token usage kept growing.

- [Nav Toor](https://x.com/heynavtoor/status/2069773963413340297) — 2026-06-25: Listicle-styled promo for MinerU, an open-source document-extraction tool (68.5K stars) from Shanghai AI Lab's OpenDataLab. Reads PDFs/Office docs/scanned images into clean Markdown with reading-order text, tables → HTML, equations → LaTeX, OCR, 109 languages, batch mode, and 10k-page docs via sliding window. CLI, Python SDK, or web app; plugs into Claude Desktop, Cursor, LangChain, LlamaIndex, etc. Apache-2.0-based license, free.

- [Akshay](https://x.com/akshay_pachaar/status/2069769689560187027) — 2026-06-25: Breakdown of "loop engineering" (opening on a Karpathy quote about removing yourself as the bottleneck): a trigger decides what runs, the loop is the maker, a separate checker grades output (a model grading itself just justifies its work), and state lives on disk not context (suggests Zep's Graphiti temporal knowledge graph). Two failure points: set the exit condition before the loop runs, and add observability on the harness since the checker only catches in-run failures (suggests Comet's Opik). Thesis: the model is a commodity; the loop around it is where the engineering lives.

- [Dhilip Subramanian](https://x.com/sdhilip/status/2069140867466797200) — 2026-06-23: Dhilip Subramanian, a heavy dictation user (44,414 words via Wispr Flow), recommends FluidVoice: a free, open-source, locally-run macOS voice-to-text tool that needs no API key and handles slang well. He cancelled his paid plan after switching.

- [Matthew Berman](https://x.com/matthewberman/status/2069098257444434425) — 2026-06-23: Matthew Berman announces a new Loop Library feature, Lazy Loops (aka Discover), which scans your codebase and chat threads to find potential agentic loops and designs them for you. Links the Forward-Future/loop-library GitHub repo of practical, repeatable AI-agent workflows.

- [Avi Chawla](https://x.com/_avichawla/status/2068657496936616314) — 2026-06-23: Avi Chawla explains why BM25, a 30-year-old keyword ranking algorithm with no training or embeddings, still powers Elasticsearch/OpenSearch and excels at exact-match retrieval where embeddings struggle, making hybrid (BM25 + vector) search the default in top RAG systems. He closes on the UX problem of highlighting which span actually drove a semantic match, pointing to his co-founder's article.

- [Codez](https://x.com/0xcodez/status/2064374643729773029) — 2026-06-23: A long-form Loop engineering roadmap arguing the leverage point in agentic coding has moved from writing prompts to designing self-running loops. Covers the 4-condition test for when a loop is worth building (task repeats, automated verification, token budget, senior-engineer tooling), the five building blocks (automations like /loop and /goal, git worktrees, skills, MCP connectors, sub-agents), the maker/checker split, the Ralph Wiggum quiet-failure mode, comprehension debt and cognitive surrender, and the security tax of unattended loops. Cites Anthropic engineering docs and Addy Osmani.

- [Viv](https://x.com/vtrivedy10/status/2066954487466459163) — 2026-06-17: Viv amplifies Sydney Runkle's X article 'The Art of Loop Engineering,' which argues reliable agents need more than a good model — they need a carefully engineered hierarchy of loops. Viv's key takeaway: verification is a critical primitive; it's worth spending days to weeks making the distribution of desired agent outcomes verifiable in practice by your system, especially for non-slop, semi-long-horizon work.

- [Jaynit](https://x.com/jaynitx/status/2066506535250092378) — 2026-06-16: Thread relaying Elon Musk's 5-step engineering 'algorithm': (1) make the requirements less dumb / question them, (2) try to delete the part or process step entirely (if you aren't forced to add ~10% back, you didn't delete enough), (3) simplify and optimize, (4) accelerate cycle time, (5) automate — with the warning that the most common mistake of smart engineers is optimizing something that shouldn't exist.

- [Hasan Toor](https://x.com/hasantoxr/status/2066247422502957197) — 2026-06-15: Highlights Headroom, a GitHub tool by Netflix engineer Tejas Chopra that compresses everything an AI agent reads before it reaches the LLM (tool outputs, logs, files, RAG chunks, code-search results, conversation history), claiming 60-95% fewer tokens for the same answers. Ships as a Python/TypeScript library, local proxy, and MCP server, with wrappers for Claude Code, Codex, Cursor, Aider, and Copilot.

- [Avid](https://x.com/av1dlive/status/2066127265407336535) — 2026-06-15: Argues you can run capable AI models locally on a Mac for free using Apple's MLX stack — install mlx-lm, launch its server, and point any agent at localhost. Cites a ~23-minute talk from an Apple MLX-team engineer in which a local model builds a working SwiftUI app from a blank Xcode project in two minutes and then fixes a bug, with nothing leaving the machine. Quote-tweets a piece on the ThinkStation PGX local-inference box.

- [Harry Tandy](https://x.com/harrytandy/status/2065818850633932996) — 2026-06-14: Opens with a Sam Altman quote that the cost to use a given level of AI falls ~10x every 12 months, then lays out a 10-step agentic-coding sprint: pick the heaviest backlog item, write a FABLE_RUN.md spec (goal/scope/commands/review rules/done criteria), map the repo first, break the job into checkpoints that each end with diff + test output + next decision, split builder and checker agents, use git worktrees for parallel attempts, and keep a RUN_LOG.md of every failed command and accepted fix.

- [Avid](https://x.com/av1dlive/status/2065747876005937416) — 2026-06-14: Promotes a 'second brain' pattern attributed to Karpathy: let an LLM maintain a wiki of your notes so knowledge compounds as you dump sources and it reads, links, and files them. Points to a free Claude Code plugin, claude-obsidian by AgriciDaniel (claude plugin marketplace add AgriciDaniel/claude-obsidian; claude plugin install claude-obsidian@agricidaniel-claude-obsidian), then run /wiki inside an Obsidian folder. Quote-tweets the author's own article on building Obsidian from scratch with 13+ Kimi agents.

- [Nav Toor](https://x.com/heynavtoor/status/2065427656112505017) — 2026-06-14: Spotlights Clone-Wars, an open-source GitHub collection (~34,555 stars) by developer Gourav Goyal that catalogues 100+ open-source clones of major apps (Netflix, Spotify, Instagram, Airbnb, WhatsApp, TikTok, Amazon) with source code, demos, and tech stacks listed — e.g., a Netflix clone in React + TMDB API. Started December 2020 and hit GitHub Trending and Hacker News #1.

- [Avi Chawla](https://x.com/_avichawla/status/2065727218991735000) — 2026-06-13: Explains 'loop engineering' (framed with a Karpathy quote about removing yourself as the bottleneck and maximizing leverage): move the operator's two manual jobs — deciding what the agent runs next and checking its output — into the system itself. A schedule decides what to run, a maker loop produces the work, a separate checker agent grades the output, and a file on disk holds the shared state both read; the loop runs until done, max iterations, or budget is exhausted.

- [Marie Haynes](https://x.com/marie_haynes/status/2065531158356717721) — 2026-06-13: Flags Google's new Open Knowledge Format (OKF): a standardized way to store information as a directory of interlinked markdown files that acts as a living wiki agents can query and edit, which the author thinks could replace Notion or Obsidian. References Google Cloud's blog post and the spec at github.com/GoogleCloudPlatform/knowledge-catalog (okf/SPEC.md), and notes feeding both links to Antigravity to brainstorm project uses.

- [Nainsi Dwivedi](https://x.com/nainsidwiv50980/status/2064947761779208476) — 2026-06-11: Alibaba open-sourced 'open-code-review' (Apache-2.0), the internal AI code reviewer that's run on their codebase for ~2 years — 20,000+ engineers, 1M+ reviews. Design: deterministic engineering handles what must never fail (file selection, bundling, rule matching, comment positioning) while the LLM only does context reading, codebase search, and reasoning. Claims ~1/5 the token cost of a generic agent + skills and precise line-level comments that don't drift on large changesets. Repo name: open-code-review.

- [Meta Alchemist](https://x.com/meta_alchemist/status/2064431279383433646) — 2026-06-11: Shares a copy-paste 'Repo Audit & Improvement Plan' prompt — a structured, 4-phase principal-engineer audit (Phase 1 discovery/mapping before judging, then a prioritized, actionable improvement plan), with instructions to cite file paths and line numbers and to flag anything unverifiable. Useful prompt template, but wrapped in hype framing around a nonexistent 'Claude Fable 5' model.

- [Boris Cherny](https://x.com/bcherny/status/2064426115255730578) — 2026-06-11: Boris Cherny (Anthropic / Claude Code) on why self-verification loops matter: letting a model check its own work lets it run autonomously for much longer and land closer to your intent, so you check in less. Points to a breakdown by @delba_oliveira (via @ClaudeDevs) on encoding your manual checks so Claude Code closes its own feedback loop.

- [Ahmad](https://x.com/theahmadosman/status/2063935919481106560) — 2026-06-09: Self-study curriculum for LLM serving engines and GPU kernel programming: start with vLLM / SGLang / TensorRT-LLM / FlashInfer (PagedAttention, continuous batching, prefix caching), then dive into Triton, CUTLASS/CuTe, FlashAttention papers, PagedAttention paper, MoE docs, Nsight profiling. Followed by a hands-on project sequence (Triton RMSNorm, fused SiLU×gate, etc.). For people actually wanting to learn the inference stack.

- [Rahul](https://x.com/sairahul1/status/2063544956158185927) — 2026-06-08: Long-form X article framing 'Harness Engineering' as the most important AI discipline of 2026 — OpenAI shipped 1M lines of production code in Feb 2026 using agents wrapped in a reliable system (the 'harness'); Anthropic published 3 papers on it; ThoughtWorks formalized a framework; Philipp Schmid called it the most important discipline of 2026. Article walks through what a harness is and the mental models needed to actually use it. 1.1M views — the term is breaking out of AI-infra circles fast.

- [Rahul](https://x.com/sairahul1/status/2063609922667815064) — 2026-06-07: Rahul follow-up to his Harness Engineering article: points to walkinglabs.github.io/learn-harness-engineering as 'the best site on the internet to learn harness engineering' — free, comprehensive. Most AI engineers haven't heard the term yet. Worth bookmarking alongside his article.

- [海拉鲁编程客 (hylarucoder)](https://x.com/hylarucoder/status/2062881239900766292) — 2026-06-06: Recommends Peter Pang's 'Building cloud agent infrastructure' — most agent frameworks assume a desktop (one user, one machine, local filesystem, keys in env vars); cloud agent infra changes those assumptions.

- [Cat Wu (Anthropic)](https://x.com/_catwu/status/2062408623565984209) — 2026-06-06: Anthropic's data team automated ~95% of business-analytics queries with Claude; the linked blog covers their approach to skills, data foundations, evals, ablations, and online validation for data-analysis agents.

- [hoeem](https://x.com/hooeem/status/2062443798647517197) — 2026-06-04: Points to a guide on making agentic workflows ~100x cheaper by fixing token waste in the orchestration loop.

- [Ole Lehmann](https://x.com/itsolelehmann/status/2061911202830401564) — 2026-06-04: A ~10-minute recipe to turn your X bookmarks into an agent-queryable second brain: export bookmarks (twitter-web-exporter / BookmarkSave), drop the file into your LLM wiki or Obsidian vault, and have your agent convert each into a tagged markdown note with the original link — then query across the whole pile. Directly relevant to this link collection.

- [Tom Dörr](https://x.com/tom_doerr/status/2061674811122713013) — 2026-06-03: Shares FlowForge, a Skill that generates professional draw.io diagrams from natural language (github.com/wentong2022-arch/flowforge-skill).

- [0xSero](https://x.com/0xsero/status/2060128492247740640) — 2026-05-29: Recommends Peter Steinberger's 'Just Talk To It — the no-bs Way of Agentic Engineering' (steipete.me): after trying every elaborate workflow, the author keeps returning to a conversational, no-ceremony way of working with coding agents rather than heavy prompting scaffolds.

- [Rohit Ghumare](https://x.com/ghumare64/status/2060072412868235587) — 2026-05-29: Summarizes Mike Piccolo's argument that a harness isn't one thing but ~15 separate concerns (turn state machines, provider routing, credential vaults, policy engines, approval gates, budget trackers, context compaction, session trees, tracing) bundled by frameworks out of necessity. When each layer is a worker on a shared bus with a typed contract, 'build your own harness' means swapping a worker, not forking a framework.

- [MacCallister Higgins](https://x.com/macjshiggins/status/2060045337679532174) — 2026-05-29: Argues classical NASA systems engineering is the ideal model for LLM-assisted coding — being explicit in docs makes it easier than ever to build, test, and verify complex codebases (planning modes only approximate it).

- [AVB](https://x.com/neural_avb/status/2060032255620431877) — 2026-05-29: A 45-minute walkthrough on creating synthetic datasets and training tiny (~100M param) local language models specialized for narrow tasks; code, datasets, models and harnesses linked.

- [Kyle Jeong](https://x.com/kylejeong/status/2059753008297394245) — 2026-05-28: Browser agents have an 'amnesia problem' — re-discovering each site from scratch every run. Autobrowse uses iterative AutoResearch to let an agent improve its own browser skills (/autobrowse), reportedly up to 90% faster and cheaper.

- [Jerry Liu](https://x.com/jerryjliu0/status/2059710330016817501) — 2026-05-28: LiteParse v2: LlamaIndex's PDF parser rewritten in Rust with native Python/Node (and WASM) packages — claimed fastest and most accurate open-source model-free parser, up to 100x faster, 50+ document types, installable inside an AI agent.

- [John Yeo](https://x.com/johnyeo_/status/2059688796728267261) — 2026-05-28: Describes an in-house agent that automatically queries logs and investigates support tickets — with billing state/history making each case stateful. Links a build writeup.

- [Avi Chawla](https://x.com/_avichawla/status/2059556157984006187) — 2026-05-28: Clear explainer of RAG vs Graph RAG vs Agentic RAG as solving different query types: standard RAG for single-hop factual lookups, Graph RAG (LLM-extracted entities/relationships + traversal) for multi-hop connections, Agentic RAG (an agent choosing tools/sources at query time) for dynamic multi-source tasks — plus binary quantization for 32x more memory-efficient vector search.

- [darkzodchi](https://x.com/zodchiii/status/2059603103070945391) — 2026-05-27: Boris Cherny (Claude Code): 'we stopped fixing Claude's mistakes; we made Claude fix them itself.' Links a copyable setup for having Claude Code catch, fix, and learn from its own errors instead of the write-code/tests-fail/explain loop.

- [Parag pawar](https://x.com/dharmikpawar13/status/2059571098484675051) — 2026-05-27: Argues CLAUDE.md is a control layer, not a README: use scope hierarchy (global → project → folder, nearest wins) and a WHAT/WHY/HOW framing, favor specificity ('TypeScript strict mode, Zod validation' over 'production-ready code'), start with /init, keep it under ~500 lines, use hooks, and treat it as living infrastructure.

- [Rohit](https://x.com/rohit4verse/status/2059366212501696609) — 2026-05-27: A Databricks tech lead's talk on the unglamorous core of multi-agent: agents fail not because the model is dumb but because nothing coordinates them — one agent is a feature, fifty is a distributed-systems problem, and getting hundreds of agents to share one coherent brain is the whole game.

- [Theo - t3.gg](https://x.com/theo/status/2059352130289651925) — 2026-05-27: Endorses DeepSWE, a new agentic-coding benchmark that reflects the realistic day-to-day developer experience — showing where top models actually diverge rather than clustering as they do on public leaderboards.

- [Binfeng Xu](https://x.com/billxbf/status/2059323616009838703) — 2026-05-27: Release of Polar, Agent-RL rollout infrastructure that takes real-world harnesses (Codex, Claude Code, OpenClaw, Hermes, or your own) directly as training environments with no code change — find a problem, design the harness, train your own agents.

- [Tom Dörr](https://x.com/tom_doerr/status/2059316125049971017) — 2026-05-27: Shares a 500-hour AI infrastructure engineering curriculum (github.com/ai-infra-curriculum/ai-infra-engineer-learning).

- [刘醒](https://x.com/xingxingli45573/status/2059258034820706541) — 2026-05-27: Taste Skill (~20.3k stars): an install that gives AI-generated front-ends better taste — improved layout, fonts, animations, whitespace — with design directions (premium, minimalist, brutalism), an audit-and-fix skill for old projects, a mockup-first image skill, and three tunable params (layout experimentation, animation richness, info density).

- [Vaishnavi](https://x.com/_vmlops/status/2059207888393138556) — 2026-05-27: Microsoft open-sourced an Agent Governance Toolkit: deterministic interception of every tool call (denied actions structurally impossible), a YAML allow/deny/human-approval policy engine, zero-trust identity (SPIFFE/DID/mTLS), a 4-level execution sandbox, tamper-evident Merkle audit logs, coverage of all OWASP Agentic Top-10 risks, and support across major frameworks and languages — because 'follow the rules' in a prompt is a suggestion, not a guardrail.

- [Atenov int.](https://x.com/atenov_d/status/2058868770257416239) — 2026-05-25: Highlights MoneyPrinterTurbo (13k+ stars): give a topic/keyword and it generates a script (via any LLM), pulls copyright-free footage, and adds subtitles/music/voiceover to output a finished short video; runs locally with Web UI/API/Docker/Colab. (Author's other posts are off-topic trading/politics.)

- [Hasan Toor](https://x.com/hasantoxr/status/2058863173462352313) — 2026-05-25: Engagement-framed tool share: an open-source engine claiming to replace agent harness, queues, sandboxing and APIs with three primitives (TypeScript/Python/Rust, Docker-ready, 15k+ stars).

- [Shubham Saboo](https://x.com/saboo_shubham_/status/2058269167372153129) — 2026-05-24: Positions codebase-as-queryable-graph as the real 'context engineering' for coding agents — turning any codebase into an interactive graph the agent can query; works with Claude Code, Codex, Antigravity; fully open-source.

- [George Nurijanian](https://x.com/nurijanian/status/2058259663238631890) — 2026-05-24: Fixed Claude's 'chart junk' by handing it a book and having it spin up a Tufte-flavored visualization skill — producing leaner, clearer visuals (github.com/gnurio/tufte-vdqi-plugin).

- [Garry Tan](https://x.com/garrytan/status/2057946119725080878) — 2026-05-24: Garry Tan's 'simple secret to agentic coding,' linking a Forbes profile ('The YC Chief Who Codes 10,000 Lines A Day Has A Simple Secret').

- [Charly Wargnier](https://x.com/datachaz/status/2057787509728522463) — 2026-05-23: Repo shoutout to addyosmani/agent-skills — production-grade engineering skills for AI coding agents, open-sourced by Addy Osmani.

- [Ahmad](https://x.com/theahmadosman/status/2057590791241896254) — 2026-05-22: Points to a free 'LLMs 101: A Practical Guide (2026 Edition)' covering model mechanics (tokens, transformers, attention, KV cache, decoding, RAG, agents, fine-tuning, multimodal) and running models locally (quantization, VRAM math, hardware tiers, runtimes, model selection, failure modes).

- [swyx](https://x.com/swyx/status/2057559570177007912) — 2026-05-22: swyx is building a skill to turn a vibecoded 'slop' app into a production-ready, e2e-tested, maintainable, parallelizable agent repo — one run went ~16 hours and 103 commits, ending with the same app but a codebase he can build on.

- [Akshay](https://x.com/akshay_pachaar/status/2057446083853520948) — 2026-05-22: Argues 'Claude Code isn't a coding tool — it's a programmable dev environment,' with 12 features that make it programmable: CLAUDE.md, Rules, Skills, Hooks, Slash Commands, Plugins, MCP, Plan Mode, Permissions, Subagents, Voice Mode, Rewind (1-5 define the environment, 6-7 extend it, 8-9 control it, 10-12 change how it runs).

- [aditya](https://x.com/adxtyahq/status/2057410759236386866) — 2026-05-22: A worked answer to a Google L5 interview question — 'design a RAG pipeline for 10M docs with zero hallucination': ingest/normalize, hybrid retrieval (BM25 + embeddings), ANN + reranking, source-confidence scoring, constrained generation, citation-backed responses, hallucination fallback, continuous evals, caching, and observability. At scale, retrieval quality matters more than the frontier model.

- [Tom Dörr](https://x.com/tom_doerr/status/2057217338844336627) — 2026-05-22: Shares turbovec, a vector store that fits 10 million documents into 4GB of RAM (github.com/RyanCodrai/turbovec).

- [Viv](https://x.com/vtrivedy10/status/2056993505386622987) — 2026-05-20: Notes on designing LangSmith Engine for customer-scale data: give the agent autonomy AFTER good tooling (around interacting with LangSmith); agents are good at pulling in context selectively, so the job is helping them self-facilitate routing useful info into the window.

- [Arpit Bhayani](https://x.com/arpit_bhayani/status/2056946273165656375) — 2026-05-20: Argues long-running agentic systems need reliability/fault-tolerance, and that teams accidentally rebuild distributed workflows (cron + queue + state + retries → state machines, idempotency, compensating actions). An essay on Temporal, an open-source durable-execution engine (Workflows, Activities, event histories, replay, Signals, retries, determinism) as the plumbing for agents that need state and execution that survives failures.

- [Alex Hillman](https://x.com/alexhillman/status/2056904462162133233) — 2026-05-20: Reframes tmux as an agent superpower: it lets agents manipulate your terminal sessions — read logs from any pane/window, answer prompts in interactive CLIs, send keys into TUIs and capture the screen, and run subagents in separate windows to inspect their output.

- [elvis](https://x.com/omarsar0/status/2056764334181884158) — 2026-05-20: 'Code as Agent Harness' — a 100+ page survey of methods and applications of code-as-harness, arguing it may be key to a science of harness engineering, and that future systems must be executable, inspectable, stateful, and governed.

- [Lotte](https://x.com/lotte_verheyden/status/2056754091817361670) — 2026-05-20: 'Evals, explained' (Langfuse Academy): offline eval sits between running an experiment and shipping. Three methods — manual review (build intuition + ground-truth labels), code-based (deterministic checks: schema, keywords, length, SQL executes), and LLM-as-a-judge (language-understanding qualities, needs calibration against human labels). Prefer binary pass/fail over 1-5 scales; one evaluator per quality; start manual then automate repeatable checks.

- [Ronan Berder](https://x.com/hunvreus/status/2056742771386638454) — 2026-05-20: Pushback on Spec-Driven Development: agents are faster at writing code and (some) humans are better at system thinking, but humans suck at planning. Argument: you can't sit down, write all the specs upfront, and then write code — experienced engineers know that doesn't work. Quote-tweets a now-unavailable @iamsahaj_xyz post.

- [Akshay](https://x.com/akshay_pachaar/status/2056714042455343160) — 2026-05-20: RAG vs CAG explained: Cache-Augmented Generation keeps static, high-value knowledge in the model's KV memory instead of hitting the vector DB every query. Combine them — cache 'cold' static data (policies/docs), retrieve 'hot' dynamic data — for faster, cheaper inference. OpenAI and Anthropic already support prompt caching.

- [Amar Singh](https://x.com/amarsvs/status/2056484487891243355) — 2026-05-19: 'Agent Performance: Model-Bound vs Harness-Bound' — counterintuitively, smarter models make harnesses matter MORE ('the smarter the model, the more expensive it is to waste its intelligence'). Model-bound tasks (hard math/proofs) hinge on raw capability; harness-bound tasks (e.g., Terminal-Bench, ~10 pts spread for Opus 4.7 across harnesses) hinge on prompting, tools, context management. As traces balloon and costs rise, the harness becomes the 'scheduler for intelligence'; author's open-source HALO optimizes harnesses from traces.

- [ClaudeDevs](https://x.com/claudedevs/status/2056403446056784288) — 2026-05-19: Anthropic blog on running Claude Code at scale — best practices from teams working across multi-million-line monorepos, decades-old legacy systems, and distributed microservices.

- [darkzodchi](https://x.com/zodchiii/status/2056336049589092866) — 2026-05-19: Shopify Head of Engineering Farhan Thawar: 'if you don't figure out how to harness agents in 2026, you'll be behind.' A practical enterprise-AI-coding breakdown / Shopify AI playbook, linking a 'Claude Code setup behind Shopify's 23,000 engineers' article (racing to automate 96% of coding by Q3, many parallel Claude Code agents).

- [Viv](https://x.com/vtrivedy10/status/2056066419360743479) — 2026-05-18: Viv on LangSmith Engine as an always-on self-improvement loop: tracing on for every agent, purpose-built SmithDB for agent-scale data, ambient intelligence over every trace to find errors/insights, and PRs/Evals generated with human gating — the first sparks of company-wide Continual Learning for agents.

- [Vaishnavi](https://x.com/_vmlops/status/2055887618303570151) — 2026-05-18: Recommends walkinglabs.github.io/learn-harness-engineering as the best site to learn harness engineering.

- [santi](https://x.com/santtiagom_/status/2055751665345798628) — 2026-05-18: Praises an OpenAI article on Harness Engineering and Codex — how they used agents to build an internal ~1M-line product: preventing agent-generated code from degrading, using tests/CI as more reliable constraints than prompts, keeping code/docs readable for agents, and how engineers' work changes when agents program.

- [klöss](https://x.com/kloss_xyz/status/2055477217552142782) — 2026-05-16: Seven production-grade /goal templates (Ideation/Interrogation, Planning & Documentation, Build & Implementation, Refactoring, Consolidation, Hardening, Migrations; use 1-3 in order, 4-7 as needed), building on the argument that /goal is the best command in Codex/Claude Code/Hermes and most use it wrong.

- [George from prodmgmt.world](https://x.com/nurijanian/status/2055333397611077881) — 2026-05-15: Favorite ways to 'write requirements' with AI: /grill-me (mattpocock/skills), /shaping (rjs/shaping-skills), and a new skill built from business-analyst literature ('make-requirements-great') — reviving useful BA rigor that got dropped as teams went agile/sloppy.

- [nader dabit](https://x.com/dabit3/status/2055319214202777894) — 2026-05-15: 'Agent Hooks: Deterministic Control for Agent Workflows' — hooks attach handlers to lifecycle points (SessionStart, UserPromptSubmit, PreToolUse, PostToolUse, Stop, SessionEnd) so scripts/tests/policy run every time instead of relying on the model to remember. Operating model: event → matcher → handler → outcome. Rule of thumb: 'always/never/block/record/run/verify' belongs in a hook. Includes a demo and per-runtime notes (Claude Code, Codex, Cursor, Devin); layer prompts (guidance) with hooks (controls), CI, and human review.

- [0xMarioNawfal](https://x.com/roundtablespace/status/2055268207221682640) — 2026-05-15: SocratiCode — local zero-config tool giving AI agents semantic understanding of an entire codebase (dependency graphs, symbol-level impact analysis, cross-project search). Claimed numbers: 61% less context, 84% fewer tool calls, 37x faster than grep-based exploration, tested on 40M LoC. Fully local, free.

- [Arpit Bhayani](https://x.com/arpit_bhayani/status/2055265636390207784) — 2026-05-15: Deep dive on what production-grade RAG actually requires beyond demos: how retrieval actually works, why chunking is where most systems fail, embedding-model lock-in, reindexing, document registries and chunk identity, index updates/deployments, retrieval tracing and observability. Argues production RAG failures are operational, not LLM, failures.

- [Mr. Buzzoni](https://x.com/polydao/status/2055197994635424038) — 2026-05-15: Engagement-farmed post about a fired Atlassian infra engineer who allegedly posted a 38-minute breakdown of every system he built: Envoy proxy instead of enterprise load balancers, sidecar architecture for auth/logging/rate limits, DynamoDB + SQS for async provisioning, Packer + SaltStack for VM deployments at scale. 16.3M views, heavy 'save this' framing — substance is generic enterprise-infra patterns, not AI-specific.

- [charmaine](https://x.com/charmaine_klee/status/2055106811225931883) — 2026-05-15: Anthropic engineer sharing the team's learnings on how Claude Code works in LARGE codebases — best practices and where to start. Links to the official Anthropic blog post: claude.com/blog/how-claude-code-works-in-large-codebases-best-practices-and-where-to-start. Direct, no hype.

- [Avid](https://x.com/av1dlive/status/2054948286403150017) — 2026-05-15: Promo for a live 15-minute lecture by two Airbnb Senior Staff Engineers on agentic coding in 2026 — Airbnb already shipped one of the most ambitious LLM-agent migrations in production. Quote-tweets Avid's May 12 article "How to Build AI Agents in 2026 (Full Course)" (527.6K views). Worth watching for real production agentic-coding patterns from a company that has actually done the migration.

- [Rohit Ghumare](https://x.com/ghumare64/status/2054625511897489423) — 2026-05-14: Argues agent codebases that survive past month six do so because the architecture makes the wrong shape harder to write than the right one — not because the team is disciplined. Cites a 'Mike' post listing four canonical month-six failures: shared mutable defaults across agents, tool fns that swallow any string and return None, session memory poisoned by LLM-extracted strings, and multi-agent setups passing the parent's full context. Aligns with the Anthropic/Glean harness-is-the-backend debate.

- [darkzodchi](https://x.com/zodchiii/status/2054526937561796939) — 2026-05-13: Pointer to an Anthropic-engineer video on the 7 Claude Code mistakes that waste tokens — model switching, context management, settings that halve token usage. Key data point: Claude Code resends the full conversation history every turn, so a 30-message session can burn 232K tokens. Every MCP server, skill, and read file rides along.

- [Joseph Viviano](https://x.com/josephdviviano/status/2054253118943363506) — 2026-05-13: Joseph Viviano's "Agentic Research Best Practices" — 15 months of notes on using coding agents in research workflows (with Mila Quebec collaborators). Key argument: research codebases differ from product engineering — no users, active development, speed bound by intelligibility to author/collaborators, not throughput. Many "best practices" from product engineering feel archaic in research.

- [Ronin](https://x.com/deronin_/status/2054255152555545079) — 2026-05-12: Ten token-waste mistakes senior AI engineers stopped making — auto-context loading 50 files for a 30-line fix ($1.20/turn waste), defaulting Opus on lint/format/rename ($0.60 vs Haiku $0.02), tool-call loops resending the full repo on retry, defaulting to Sonnet when Kimi 2.6 matches at 1/6 cost, streaming on stable-prefix workflows killing prompt cache, "just-in-case" file includes blowing 80K-token prompts. Karpathy-quote framing.

- [klöss](https://x.com/kloss_xyz/status/2054096165055217987) — 2026-05-12: Detailed /goal prompt template for Codex / Claude Code / Hermes with structured slots: GOAL (single measurable outcome), CONTEXT, CONSTRAINTS, PRIORITY, PLAN (understand first), DONE WHEN, VERIFY (tests/build/lint/typecheck). Aimed at killing scope creep and ranking uncertainty before acting. Directly usable.

- [Mnimiy](https://x.com/mnilax/status/2053116311132155938) — 2026-05-10: Long-form post: Karpathy's 4-rule CLAUDE.md template (born Jan 2026 from his thread on Claude failure modes — silent wrong assumptions, over-complication, orthogonal damage) cut mistakes from ~40% to <3% across 30 codebases over 6 weeks. Forrest Chang's repo hit 120K stars. Author argues the template only fixes Jan code-writing problems; he adds 8 more rules targeting May 2026 agent-orchestration issues (agent fights, hook cascades, skill loading conflicts, multi-step workflows). Notes CLAUDE.md is advisory (~80% compliance); past 200 lines compliance drops sharply. 2.5M views.

- [Tom Dörr](https://x.com/tom_doerr/status/2052261421744869757) — 2026-05-08: Tom Dörr highlights HelixDB (github.com/HelixDB/helix-db): a database that combines graph and vector storage in one engine for AI apps. Worth evaluating as a building block for RAG and agent-memory pipelines that otherwise span two systems.

- [Uncle Bob Martin](https://x.com/unclebobmartin/status/2052370749701214226) — 2026-05-07: Uncle Bob Martin: 'It's not wrong. It just shows that driving an AI is a form of engineering that is not for the faint of heart.' The post he was reacting to is now from a suspended account, so the original content is lost — Uncle Bob's framing is all that remains. 130.6K views suggests it resonated.

- [0xSero](https://x.com/0xsero/status/2050544304360165585) — 2026-05-02: Reminder that Claude Code session history is auto-deleted monthly unless you change settings.json — that's all valuable training/context data. 0xSero shares a backup repo (github.com/0xSero/ai-data-extraction) to help you preserve it.

- [darkzodchi](https://x.com/zodchiii/status/2050537397377532341) — 2026-05-02: Promotes a security article + .gitignore template after citing that Anthropic allegedly leaked 512K lines of source code from a missing .gitignore entry. Boris Cherny (Claude Code creator) cited as the cautionary tale. Engagement framing, but the .gitignore best-practices angle is legitimately useful.

- [Muhammad Ayan](https://x.com/socialwithaayan/status/2050484688968724820) — 2026-05-02: Pointer to github.com/warpdotdev/warp — Warp terminal's source has been published as 'an agentic development environment, born out of the terminal.' Worth a look as a coding-agent shell.

- [Dan Shipper](https://x.com/danshipper/status/2050235671466606665) — 2026-05-02: Dan Shipper recommends Marcus's 'definitive guide' on how a PM can ship product with coding agents at Every: every.to/guides/ai-product-management-guide. Pitched as required reading for non-engineer builders.

- [Mike Bespalov](https://x.com/bbssppllvv/status/2049924037111841027) — 2026-05-02: Refero.design publishes 2000 DESIGN.md files (colors, type, spacing, layouts) extracted from the world's best products, structured for an LLM to read so coding agents stop producing ugly UIs. Free at styles.refero.design.

- [摆烂程序媛](https://x.com/wanerfu/status/2050158295911137370) — 2026-05-01: Translated-from-Chinese promotion of Scrapling (github.com/D4Vinci/Scrapling) — open-source web scraper claiming Cloudflare bypass with no selector maintenance and '774x faster than BeautifulSoup'. Useful for AI scrape pipelines if benchmark holds up.

- [Teknium](https://x.com/teknium/status/2050098631907434871) — 2026-05-01: Teknium ships a /goal command in NousResearch hermes-agent (PR github.com/NousResearch/hermes-agent/pull/18262) — supervisor-loop pattern inspired by ralph loops + Codex's upcoming /goal: keeps re-prompting the agent until the supervisor judges the task complete.

- [Garry Tan](https://x.com/garrytan/status/2049720409965392052) — 2026-04-30: Garry Tan (YC President & CEO) shipping 10 PRs to GBrain — his personal AI/markdown 'second brain' tool — focused on quality-of-life improvements to make it scale across a corpus of 74k markdown files.

- [Aparna Dhinakaran](https://x.com/aparnadhinak/status/2047849364547420382) — 2026-04-28: Aparna Dhinakaran (Arize) on harnesses converging on similar context-passing problems — letting the agent decide context dynamically. Quote-tweets Aran Komatsuzaki on Anthropic's forked subagents (introduced Apr 23, 2026): forked subagents can inherit the same context as the main agent, useful when richer context matters more than minimal context. Direct relevant to the bossman-supervisor concept.

- [Hasan Toor](https://x.com/hasantoxr/status/2047637109343928827) — 2026-04-28: Hasan Toor points to future-agi (github.com/future-agi/future-agi + app.futureagi.com) — open-source end-to-end platform for evaluating, observing, and improving production AI agents. Nightly release; stable coming. Worth evaluating alongside other agent-observability tools.

- [Yasir Ai](https://x.com/aiwithyasir/status/2047589529650176333) — 2026-04-28: Hyped pitch ('Breaking', 'terrifying how good') for GitNexus — a knowledge-graph engine for codebases using Tree-sitter AST parsing. Maps every function call, import, class inheritance, interface; clusters code by cohesion; runs blast-radius analysis before changes; coordinates rename across files. MCP-compatible with Claude Code, Cursor, Windsurf. Engagement framing but the underlying capability is interesting.

- [TRAE](https://x.com/trae_ai/status/2047145274200768969) — 2026-04-23: TRAE's 'Definitive Guide to Harness Engineering' X article — frames harness engineering as the 2026 successor to prompt + context engineering. Term coined by Mitchell Hashimoto (HashiCorp co-founder); gained traction via an OpenAI report. Horse-and-reins metaphor: AI Agent = SOTA Model (wild horse) + Harness (control system) = Elite Performer. Foundational reading for the harness-engineering concept thread alongside Rahul/walkinglabs/Anthropic papers.

- [Matt Van Horn](https://x.com/mvanhorn/status/2047073560267817469) — 2026-04-23: Matt Van Horn endorses Compound Engineering v3 (Trevin Chow's project, ~15k stars) — names brainstorm and plan artifacts that give requirements a paper trail from idea to commit, harness alignment across the build. Worth a real evaluation as a methodology framework alongside harness engineering.

- [spencer](https://x.com/techspence/status/2046759185593794782) — 2026-04-23: spencer flags OWASP's Autonomous Penetration Testing Standard (github.com/OWASP/APTS) — formal security standard for AI-driven pentesting. Reference for security-team adjacent work; substance pending a real read.

- [Avi Chawla](https://x.com/_avichawla/status/2046685172666712571) — 2026-04-23: Avi Chawla reports 3x token reduction on Claude Code (10.4M → 3.7M tokens, 10 errors → 0, $9.21 → $2.81) by using Insforge Skills + CLI (github.com/InsForge/InsForge) as a backend context-engineering layer — without changing CLAUDE.md, prompts, or models. Open-source and local. Worth measuring against on a real session.

- [Sydney Runkle](https://x.com/sydneyrunkle/status/2046277232537256002) — 2026-04-21: LangChain team piece on 'The runtime behind production deep agents' — distinguishing the harness (prompts, tools, skills, model loop) from the runtime (durable execution, memory, multi-tenancy, observability). Walks through production requirements for agents and how LangSmith Deployment + Agent Server package those capabilities. Reference architecture for shipping agents in production.

- [Nav Toor](https://x.com/heynavtoor/status/2046276160930414976) — 2026-04-21: Intro to PoisonedRAG attack: researchers showed 5 malicious documents planted in a 2.6M-document corpus can hijack an LLM's answer 97% of the time. Attacker never touches the model or retriever — just writes documents. Important RAG security consideration.

- [Sigrid Jin](https://x.com/realsigridjin/status/2046266374948069387) — 2026-04-21: Quote-tweet of Junghwan Na's writeup — Na got his GitHub banned after pushing 500+ commits across 100+ open-source repos in 72 hours using an AI harness. Sigrid pulls out the two highest-leverage principles from Na's method: (1) reproduce the bug locally or drop it, (2) read merge history instead of CONTRIBUTING.md. Jeremy flagged 'worth extracting a skill' — these are skill-worthy contribution-harness patterns.

- [Vox](https://x.com/voxyz_ai/status/2045899539526148193) — 2026-04-21: The #1 GitHub trending repo this week (44,465 stars) is a CLAUDE.md file distilling Andrej Karpathy's LLM coding pitfalls into 4 principles: (1) think before coding — ask when unsure, (2) simplicity first — minimum code, (3) surgical edits — only touch what's required, (4) goal-driven — translate fuzzy instructions into verifiable targets. Directly actionable as a CLAUDE.md system prompt.

- [Akshay](https://x.com/akshay_pachaar/status/2046151867177308181) — 2026-04-20: Akshay summarizes Google DeepMind's 'AI Agent Traps' paper — the first systematic framework for adversarial content engineered to hijack AI agents browsing the web. Maps six attack surfaces: Content Injection (perception: invisible CSS, hidden HTML, steganographic payloads in images — HTML injections hijack web agents in up to 86% of scenarios), Semantic Manipulation (reasoning: biased framing weaponizing cognitive biases), Cognitive State Traps (memory: RAG poisoning, long-term memory corruption), plus three more not visible in the truncated scrape. High-priority reading for anyone building agents that browse arbitrary web content.

- [Garry Tan](https://x.com/garrytan/status/2045427057656729985) — 2026-04-19: Garry Tan launches GBrain v0.11 with "Minions," a BullMQ-style queue/jobs system built on Postgres/PGLite to make OpenClaw/GBrain subagents faster and more reliable instead of timing out.

- [Alex Ker](https://x.com/thealexker/status/2045203785304232162) — 2026-04-18: Alex Ker's deep-dive guide on optimizing AI coding harnesses: keep config/.md files lean and human-written (frontier LLMs hit a "dumb zone" past a few hundred instructions), use progressive disclosure for CLIs/skills/MCP tools, structure prompts with HumanLayer's Research-Plan-Implement (R.P.I.) framework, and use subagents (parallel fan-out for breadth, pipelines for depth) to keep the main context clean. Core argument: the harness, not the model, is where engineering judgment compounds, so commit to one and iterate.

- [Eric Hartford](https://x.com/quixiai/status/2044952124568527298) — 2026-04-18: Eric Hartford releases Clearwing, an MIT-licensed open-source vulnerability-discovery engine that reproduces Anthropic's "Project Glasswing" results with any LLM. His argument: the real innovation isn't the gated Claude Mythos model but the model-agnostic pipeline, rank files by attack surface, fan out hundreds of file-scoped agents, use crash oracles (AddressSanitizer/UBSan) as ground truth, and run a verification agent to filter noise. Reproduced findings with OpenAI Codex 5.4 and a Qwen3.5 finetune.

- [GitHub Projects Community](https://x.com/githubprojects/status/2044453433743458686) — 2026-04-15: Tool share: Graphify (osp.fyi/graphify) turns any folder of code into a queryable knowledge graph instantly — code-as-graph for agent/dev navigation and retrieval.

- [Viv](https://x.com/vtrivedy10/status/2044430694458310870) — 2026-04-15: Points to Hunter Leath's article "Bash is the SQL for file systems" — a deep dive on storage, filesystems, and egress fees from cloud providers. Framed as must-read alpha for anyone working at the storage/filesystem layer.

- [Akshay](https://x.com/akshay_pachaar/status/2044329897603244093) — 2026-04-15: Akshay argues agent memory is three-dimensional, needing a relational store for provenance, a vector store for semantics, and a graph store for relationships, because flat vector search misses multi-hop connections (the "bridge" fact that links two entities). He points to Cognee, an open-source project that unifies all three behind four async calls (default embedded SQLite+LanceDB+Kuzu, swappable for Postgres/Qdrant/Neo4j).

- [Garry Tan](https://x.com/garrytan/status/2044291663213015491) — 2026-04-15: Garry Tan releases GBrain v0.10.0, packaging his personal OpenClaw "brain" for others: refined RESOLVER.md and SOUL.md, ACLs for multi-user brain access, and 24 distinct "fat" skills shipped with e2e tests, evals, and unit tests.

- [Shaw (spirit/acc)](https://x.com/shawmakesmagic/status/2044269097647779990) — 2026-04-15: Shaw shares a reusable prompt for cleaning up "vibecoded" codebases by spawning 8 parallel subagents, each owning one cleanup task: DRY/dedup, consolidating shared types, removing unused code (knip), untangling circular deps (madge), replacing weak types (any/unknown), stripping needless defensive try/catch, removing legacy/fallback paths, and cutting AI-slop comments. Each subagent researches, writes a critical assessment, then implements high-confidence fixes.

- [mr-r0b0t](https://x.com/mr_r0b0t/status/2044199154004472009) — 2026-04-15: Amplifies a tip on a 3-tool agent web stack: SearXNG for candidate source discovery, Firecrawl for known-URL scraping, Camofox for JS/interaction browser fallback. Described as essential for any agent doing web search or scraping.

- [klöss](https://x.com/kloss_xyz/status/2044169678961234282) — 2026-04-15: klss argues agents fail across repos because of unstructured markdown, and proposes a four-folder convention to remove ambiguity: /audits (proof), /docs (description), /plans (intent), /specs (law). Separating intent from proof from law stops Claude Code, Codex, and Cursor agents from hallucinating context.

- [0xSero](https://x.com/0xsero/status/2044165332928213243) — 2026-04-15: Guide to running large LLMs on limited hardware: use REAPs (50% savings), quantization (AWQ/GPTQ/W4A16/FP8 for fast inference; GGUF/EXL3 for compatibility; MLX for Apple silicon), and 8-bit KV cache (50-75% savings). Practical tips for local AI deployment.

- [kwindla](https://x.com/kwindla/status/2044106314612408437) — 2026-04-15: kwindla introduces Gradient Bang, claimed to be the first massively-multiplayer, fully LLM-driven game: a retro space-trading game (Factorio-like) where you cajole a ship AI into tasking other AIs. Built to explore sub-agent orchestration, partial context sharing across inference loops, long contexts and episodic memory, LLM-generated dynamic UIs, and voice input. Built on pipecat_ai plus Supabase and Vercel, fully open source.

- [Mario Zechner](https://x.com/badlogicgames/status/2043757216885256463) — 2026-04-15: Mario Zechner recommends Alex Volkov's article 'The Z/L Continuum — Do AI engineers even need to read code anymore?' (thursdai.news/zl), which asks how much code AI engineers still need to read in 2026 and beyond.

- [am.will](https://x.com/llmjunky/status/2043817254152814785) — 2026-04-14: How to get free NVIDIA API credits for open-source models via the OpenAI-compatible endpoint integrate.api.nvidia.com/v1 (Minimax 2.7, Qwen 3.5, GLM 5, Gemma, Nemotron). Won't match Opus-tier, but the author rates Minimax M2.7's 'personality' highly; includes a paste-ready client config block. Useful for cheap/free local-agent experimentation.

- [Phil Chen](https://x.com/philhchen/status/2043759400121458922) — 2026-04-14: 'How I built Filbert' — a background coding agent that is a lightweight wrapper around an existing harness running on the team's own infra with full dev-env access and recursive self-improvement. Per the linked article it wrote 95% of the team's PRs in a week and runs 14 scheduled jobs daily (bug triage, security audits, dead-code sweeps, CI optimization). Strong template for self-hosted background agents.

- [Tech with Mak](https://x.com/technmak/status/2043683120319520806) — 2026-04-14: Distills three Karpathy critiques of coding agents (wrong assumptions unchecked, overcomplication/bloat, editing code they don't understand) into a drop-in CLAUDE.md with four principles: (1) think before coding / surface ambiguity and push back, (2) simplicity first / no unrequested abstractions, (3) surgical changes / don't touch adjacent code, (4) goal-driven execution / turn tasks into failing tests then loop to green. Practical, copy-paste engineering guardrails.

- [Vaishnavi](https://x.com/_vmlops/status/2043624154646409708) — 2026-04-14: Vaishnavi covers Google's open-sourced Magika — an AI-powered file content type detection tool. Trained on 100M files, 200+ content types, 99% accuracy at 5ms/file. Sees through renamed malware and disguised scripts. Install via pip install magika. github.com/google/magika

- [Noisy](https://x.com/noisyb0y1/status/2043609541477044439) — 2026-04-14: Noisy describes a Google engineer who automated 80% of his work with Claude Code using a CLAUDE.md file based on Karpathy's principles and a .NET orchestration app. Covers the Karpathy-inspired CLAUDE.md, a dotnet service that spawns Claude Code instances with git worktrees, and a review pipeline. Claims $28K passive income working 2-3 hours/day.

- [Charly Wargnier](https://x.com/datachaz/status/2043246635996807300) — 2026-04-13: Charly Wargnier covers Addy Osmani's (Google) new Agent Skills package: 19 engineering skills + 7 commands for AI coding agents, based on Google best practices. Covers the full dev lifecycle — define (specs), plan (decompose), build (incremental), verify (TDD), review (security), ship (CI/CD). Aims to prevent agents from skipping quality gates.

- [Ahmad](https://x.com/theahmadosman/status/2043366810494337354) — 2026-04-12: A concise recipe for running parallel agents: either have one agent fan out or drive deterministic script runs — spin up workers, isolate each in a git worktree, gate merges with diffs, add backups/rules/logs for deterministic runs, and merge only what passes. Author is packaging it as a Skill.

- [Alpha Batcher](https://x.com/alphabatcher/status/2042606770816704643) — 2026-04-10: Distills architectural principles for production AI agents by quoting Rohit's article reverse-engineering Claude Code's architecture (github.com/rohit4verse). Key patterns: async generators for streaming, parallel read-only tools vs serial write tools, tools executing during generation (not after), system prompt designed for cache efficiency, hierarchical context compaction cheapest-first, isolated worktree per sub-agent. Calls it the most detailed public breakdown of a production agent architecture available.

- [Sigrid Jin](https://x.com/realsigridjin/status/2042440330503733343) — 2026-04-10: Summary of "Better Harness" paper on using evals as a flywheel for agent improvement. Key insight: evals are the new training data — instead of updating weights, you update the agent harness. Warns that agents reward-hack evals, so you need strict train/test splits. Quality over quantity in eval design. The flywheel: mine prod traces for failures, turn into evals, auto-tweak prompts/tools, validate, repeat.

- [ProxySoul](https://x.com/bniwael/status/2042364421373121018) — 2026-04-10: SoulForge — an open-source AI coding agent that builds a live graph of the codebase before the agent reads any code. Uses real LSP via embedded Neovim for go-to-definition, references, and call hierarchy instead of regex hacks. Features multi-tab with cross-tab coordination where agents share context through a real-time bus, and supports mixing models (Opus, Gemini, Haiku, Ollama). Claims 1.8x faster and 2.1x cheaper than standard approaches.

- [Ashpreet Bedi](https://x.com/ashpreetbedi/status/2041966288541507861) — 2026-04-09: Ashpreet highlights @Vtrivedy10's LangChain article on auto-improving agent harnesses using evals as a hill-climbing signal. The approach formalizes iterative system improvement — build a harness, eval it, improve it automatically. Directly applicable to anyone building agentic workflows who wants systematic quality gains.

- [mr-r0b0t](https://x.com/mr_r0b0t/status/2041930298238087464) — 2026-04-09: Endorses the same LangChain article by @Vtrivedy10 on harness hill-climbing with evals. Argues that harness evolution combined with specialist local models will be the path forward for agent development.

- [Vaishnavi](https://x.com/_vmlops/status/2041869776927261024) — 2026-04-09: Microsoft open-sourced markitdown (github.com/microsoft/markitdown) — a Python tool that converts PDFs, Word docs, Excel, PowerPoint, audio, and YouTube URLs into clean Markdown for LLM pipelines. One pip install replaces custom parsers for file ingestion.

- [Ashpreet Bedi](https://x.com/ashpreetbedi/status/2041568919085854847) — 2026-04-08: Ashpreet Bedi argues that building agentic software requires systems engineering discipline — you can't optimize AI agent systems by optimizing individual components. Draws parallels to Bell Labs' 1940s discovery that telephone network behavior emerged from component interactions, not individual parts. The current wave of 'harness engineering' is repeating 80-year-old mistakes.

- [Charly Wargnier](https://x.com/datachaz/status/2039963758790156555) — 2026-04-03: Charly Wargnier breaks down Karpathy's new self-improving 'second brain' setup using Obsidian Markdown wikis. Instead of complex RAG, an LLM auto-compiles raw research into indexed .md files, handles its own linting and Q&A routing, and generates outputs (Marp slides, matplotlib plots) filed back into the wiki. The key insight: agents maintaining their own memory layer don't need massive context windows — just clean file organization and the ability to query their own indexes.

- [Dmitriy Kovalenko](https://x.com/neogoose_btw/status/2039508756988620801) — 2026-04-02: Dmitriy Kovalenko demos a blazing-fast, index-free code search tool that works on massive codebases in real time — tested on leaked Claude Code sources, Linux kernel (100k files), and Chromium repo (500k files). Claims it's the most accurate code search approach available.

- [klöss](https://x.com/kloss_xyz/status/2038842907466334550) — 2026-03-31: Critical supply chain attack on axios (100M+ weekly npm downloads). An attacker hijacked a maintainer's credentials and published poisoned versions (1.14.1 and 0.30.4) that inject a fake dependency installing a remote access trojan across macOS, Windows, and Linux. Pin to axios@1.14.0 or 0.30.3 and rotate all secrets on affected machines.

- [Vox](https://x.com/voxyz_ai/status/2038677643000758466) — 2026-03-31: Parallel module development pattern using Codex: break a project into 5 independent modules running in separate windows with a 'foreman' conductor writing to a shared doc. Each module reads the shared state, executes its part, and updates when done. Uses Claude for UI work and Codex for the rest.

- [Tom Dörr](https://x.com/tom_doerr/status/2038456589984690462) — 2026-03-30: Cisco open-sourced DefenseClaw (github.com/cisco-ai-defense/defenseclaw), a tool that scans and blocks dangerous AI agent actions. Designed as a safety layer for autonomous AI workflows.

- [Erick](https://x.com/ericksky/status/2038301058338812119) — 2026-03-30: Tome — an open-source macOS app that transcribes Zoom/Meet/Teams meetings locally with AI (no cloud), detects speakers, and generates Markdown notes directly into your Obsidian vault. No API keys, no subscriptions, 100% private.

- [Tom Dörr](https://x.com/tom_doerr/status/2038137050243711042) — 2026-03-29: Shares a self-improving agent-swarm framework, Hive (github.com/aden-hive/hive) — orchestration for multiple cooperating agents that improve over time.

- [Rohit](https://x.com/rohit4verse/status/2036845273117581676) — 2026-03-26: Rohit argues top AI teams win not on model selection but on 'harness engineering' — how you design the agent's interface, manage context windows, cap search results, run linters at edit time, and maintain persistent state files. A teaser thread for an 8,000-word deep dive covering 8 actionable principles for building more reliable AI agents; key insights include: interface shapes model reasoning, context pollution is costly, and forced query refinement beats flooding with results.

- [Greg Pstrucha](https://x.com/grichadev/status/2036472210152718504) — 2026-03-25: Greg Pstrucha demonstrates how malicious Claude Code skills can hide instructions inside PNGs and abuse Claude Code's 'expand output' feature to fool both humans and agents — a real security threat. He improved `skill-scanner` (also available via Sentry's Warden at warden.sentry.dev) to catch these attack vectors. Only install skills from trusted sources.

- [Denis Yurchak](https://x.com/denisyurchak/status/2036422883350544519) — 2026-03-25: Denis Yurchak shares a Claude prompt (.md file) that fully automates secure Hetzner VPS setup in one shot — configures SSH hardening, fail2ban, UFW firewall, and optionally Tailscale. Buy the server, install Claude, paste the prompt. Open source, PRs welcome. Practical Claude-as-sysadmin pattern.

- [Kshitij Mishra](https://x.com/daievolutionhub/status/2035396799704547453) — 2026-03-22: Kshitij Mishra shares a 'Claude Code Setup Cheatsheet' based on Boris (creator of Claude Code), quoting Shruti Codes' '2026 AI Engineer roadmap' article; 'Save this' engagement framing.

- [Akshay](https://x.com/akshay_pachaar/status/2035341800739877091) — 2026-03-22: Akshay Pachaar's guide 'Anatomy of the .claude/ folder' walks through CLAUDE.md, custom commands, skills, agents, and permissions and how to set them up properly, framing .claude as the control center for how Claude behaves in a project (instructions, commands, permission rules, and cross-session memory).

- [Matt Stockton](https://x.com/mstockton/status/2035179208872202320) — 2026-03-22: Matt Stockton argues building AI-enabled products inverts classical software engineering: the 'right way to build' changes every ~3 months, it is often better to burn the system down and rebuild than to adapt, and modern tools make that cheap — warning against sunk-cost V1 RAG systems that stuff a static context window.

- [Thariq](https://x.com/trq212/status/2033949937936085378) — 2026-03-18: Thariq (Anthropic) shares 'Lessons from Building Claude Code: How We Use Skills' — which skills are worth making, the secret to writing a good one, and when to share them — noting Anthropic runs hundreds of skills internally and that the common 'skills are just markdown files' misconception undersells them.

- [Rohit](https://x.com/rohit4verse/status/2033945654377283643) — 2026-03-18: Rohit's essay 'The Harness Is Everything: What Cursor, Claude Code, and Perplexity Actually Built' argues you're not using AI wrong because of the model — you're using it wrong because you haven't built the right environment; the difference between teams shipping millions of lines and those struggling is the harness, not GPT-5 vs Claude Opus, temperature, or the prompt.

- [Akhilesh Mishra](https://x.com/livingdevops/status/2033845127244825041) — 2026-03-17: Akhilesh Mishra reports NVIDIA open-sourced OpenShell at GTC — an infrastructure-layer sandbox/guardrail for coding agents: filesystem locked at sandbox creation, network blocked by default with whitelisting, API keys injected only at runtime (never on disk), policies in simple YAML, running a full K3s cluster inside a single Docker container. One command sandboxes Claude Code, Codex, or Cursor; Adobe, Atlassian, Cisco, CrowdStrike, and Salesforce are integrating it.

- [Garry Tan](https://x.com/garrytan/status/2032196172430131498) — 2026-03-13: Garry Tan shares a CTO's testimonial that his open-source gstack ('god mode') flagged a subtle cross-site-scripting vulnerability the team wasn't aware of, predicting 90%+ of new repos will adopt it. gstack is MIT-licensed at github.com/garrytan/gstack and installs into local Claude Code and into a repo for teammates with two pastes.

- [Viv](https://x.com/vtrivedy10/status/2031411814232187109) — 2026-03-11: Viv (LangChain applied research) shares a LangChain blog taking a first-principles look at why agent harnesses exist and how they help craft good product experiences and correct model failure modes. It covers filesystems, code execution, sandboxes, context rot, and ralph loops, arguing the best harness for your model probably isn't the one it shipped with.

- [Ming "Tommy" Tang](https://x.com/tangming2005/status/2031358195558658266) — 2026-03-11: Tommy Tang's single biggest CLAUDE.md improvement: when a bug is reported, don't start by fixing it. Start by writing a test that reproduces the bug, then have subagents try to fix it and prove the fix with a passing test.

- [Dominik Tornow](https://x.com/dominiktornow/status/2031233587819983096) — 2026-03-10: Dominik Tornow: the new core skill in software engineering is designing feedback loops. He quotes OpenAI Developers on a small team steering Codex to open and merge 1,500 pull requests for a product used by hundreds of internal users, with zero manual coding.

- [Boris Cherny](https://x.com/bcherny/status/2031089411820228645) — 2026-03-10: Boris Cherny announces Code Review in Claude Code: when a PR opens, a team of agents runs a deep review to hunt for bugs. Built internally first because code output per Anthropic engineer is up 200% this year and review had become the bottleneck; he says it catches many real bugs he'd otherwise miss.

- [0xSero](https://x.com/0xsero/status/2030653670375751942) — 2026-03-08: 0xSero shares advice from Factory's Leo: take screenshots and videos of everything you've built, then review it. Combined with automated QA, this yields a semi-autonomous build/verify system. Links a podcast episode.

- [GitHub Projects Community](https://x.com/githubprojects/status/2030346933009821801) — 2026-03-08: GitHub Projects Community: rather than using AI to generate code directly, let it run a structured build loop — idea -> roadmap -> small tasks -> execute each task in isolation -> commit — for cleaner repos, clearer progress, and far less AI chaos.

- [Numman Ali](https://x.com/nummanali/status/2030012892192309461) — 2026-03-07: Numman Ali strongly recommends a deeply technical article, 'Your LLM Doesn't Write Correct Code. It Writes Plausible Code,' praising its articulation of the plausible-vs-correct distinction in LLM output — illustrated by a 100-row primary-key lookup where SQLite takes 0.09ms but an LLM-generated Rust rewrite takes 1,815.43ms.

- [Alex Prompter](https://x.com/alex_prompter/status/2029961559615607052) — 2026-03-06: Citing a GitHub analysis of 2,500+ repos, argues most agents.md files fail by being too vague. Top performers give each agent ONE narrow job (docs writer, test engineer, lint fixer) with specific examples — specialists beat generalists.

- [Alexey Grigorev](https://x.com/al_grigor/status/2029829363903123636) — 2026-03-06: Argues prompting is only ~5% of AI engineering; the other 95% is making AI testable, observable, versioned and reliable in production. Core skills: evaluation/testing with golden eval sets and regression tests, plus controlled iteration via prompt versioning and experiment tracking (Git/MLflow).

- [Philipp Schmid](https://x.com/_philschmid/status/2029570052530360719) — 2026-03-06: Practical guide to evaluating agent Skills, which are often AI-generated and untested: define success criteria (outcome/style/efficiency), build 10-12 prompts with deterministic checks, add an LLM-as-judge for qualitative checks, and iterate on the skill from eval failures.

- [Sukh Sroay](https://x.com/sukh_saroy/status/2029400474739458379) — 2026-03-05: [Post unavailable — account suspended]

- [yenkel](https://x.com/yenkel/status/2029299384832209259) — 2026-03-05: Crisp engineering-leadership advice for the AI era: fewer handoffs and faster decisions, more exploration, willingness to throw away code/tokens, learning by building, and picking leads who can own design, engineering and product together.

- [Dan Robinson](https://x.com/danlovesproofs/status/2028890694837039202) — 2026-03-05: Argues issue tracking/backlogs are dying: forward-thinking AI-augmented teams skip Linear/tickets entirely because the cost to fix an issue now approaches the cost to understand it. Works for small, flat, high-context teams with strong dev infra; framed as part of the 'death of midwit software engineering.'

- [Nate Kohari](https://x.com/nkohari/status/2028525461689176325) — 2026-03-02: [Post unavailable — page doesn't exist]

- [tetsuo](https://x.com/tetsuoai/status/2028068322106097773) — 2026-03-02: Technical breakdown of recurring agentic failure modes in fast/distilled code models: wrong direct-exec vs shell selection, structured-output (JSON-only) non-compliance, and tool-result grounding failures (reporting success after a tool error). Fix: distill full agent trajectories (request→tool→output→grounded response), add contrastive near-miss examples, and gate on concrete agentic evals.

- [Nyk](https://x.com/nyk_builderz/status/2028022503319203926) — 2026-03-02: Announces open-sourcing Mission Control, a self-hosted AI agent orchestration dashboard: 26 panels, real-time WebSocket+SSE, SQLite (no external services), kanban board, cost tracking, role-based access, quality gates, multi-gateway support. Repo: github.com/builderz-labs/mission-control.

- [Sandhya](https://x.com/agenticgirl/status/2028006725538967614) — 2026-03-02: 'BREAKING'-style but substantive thread on LMCache, an open-source KV-cache layer (6.9K stars, used by Google Cloud, CoreWeave, NVIDIA) that makes the LLM KV cache persistent and shareable across engine instances, tiered GPU→DRAM→disk→S3. Enables instant RAG, disaggregated prefill, and context sharing; integrates with vLLM and SGLang. Apache-2.0, pip install lmcache.

- [vixhaℓ](https://x.com/thevixhal/status/2027763453679841311) — 2026-03-02: Promotes a popular step-by-step article on building a 16-bit CPU from scratch in C (4,000+ bookmarks). A from-scratch systems/architecture learning project rather than AI content.

- [Joseph Thacker](https://x.com/rez0__/status/2027448137133264955) — 2026-03-01: Argues bug bounty / security research changed step-function fast in late 2025: coding agents went from not working to genuinely working. Example: pointed Claude Code at a target's scope (enumerate subdomains, analyze JS bundles, fuzz, test IDORs/GraphQL, write an HTML report); it ran ~30 min, self-recovered from auth/WAF errors, and returned two confirmed vulns. Hunters now build and share custom Claude Code skill libraries (JS static analysis, authenticated fuzzing, IDOR, GraphQL introspection). Quote-tweets Karpathy's parallel observation about programming.

- [Sudo su](https://x.com/sudoingx/status/2027264446989848613) — 2026-02-27: Practical steering tips for local coding agents: tell the model its own architecture/constraints (e.g. Qwen3.5 fires 8 of 256 experts/token), give project structure over single prompts, iterate in layers (scaffold → refine → polish), let it debug its own failures, and use long context (262K) to hold the whole project. Notes Claude Code as a solid harness and that llama.cpp merged native Anthropic endpoints (no proxy/LiteLLM). Argues the skill gap in local inference is now the harness and steering, not the models — all on a single RTX 3090.

- [George from prodmgmt.world](https://x.com/nurijanian/status/2027020091418890613) — 2026-02-27: George argues elite PMs escalate documentation with validation rather than starting with a 10-page PRD: 1-pagers are decision docs (write ~10, ~3 get approved), 3-pagers validate and align, and 5-pagers add execution detail only for ideas that survived two rounds. Documentation should match your confidence level, not your anxiety level.

- [Avi Chawla](https://x.com/_avichawla/status/2026907616337883612) — 2026-02-27: Avi Chawla revives Norm Hardy's 1988 'confused deputy problem' as the defining security issue for autonomous agents that hold real credentials but can't judge intent. He points to Teleport's open-source Agentic Identity Framework, which gives each agent a unique cryptographic identity, evaluates access in real time, auto-discovers shadow agents and unmanaged MCP servers, and keeps full audit trails.

- [Fernando](https://x.com/franc0fernand0/status/2026701684106313791) — 2026-02-27: Fernando summarizes a Microsoft study (Kalliamvakou et al., TSE 2018) on what makes a great manager of software engineers: technical skill is required but not sufficient; what distinguished great managers was availability, granting autonomy, supporting experimentation, and setting clear ways of working.

- [Atlas Forge](https://x.com/atlasforgeai/status/2026380335249002843) — 2026-02-25: Long-form piece on nine 'meta-learning loops' that let an agent improve across sessions, not just within one: failure-to-guardrail pipelines, tiered memory with trust scoring and decay, prediction-outcome calibration, nightly extraction, friction detection, expiring context holds, plus cognitive loops (epistemic tagging, creative-mode directives, recursive self-improvement). Start with a regressions list; the key is closing the loops so learning compounds.

- [Rohit](https://x.com/rohit4verse/status/2026359771427991764) — 2026-02-25: Rohit's 10-step checklist for taking agentic AI from demo to production (40%+ of projects fail on architecture, not models): threat-model boundaries, strict input/output contracts, RBAC + sandboxing, layered/compact context, governed grounding, planning/orchestration as control flow, memory in the architecture, native retry/error handling, full observability, and governance with safety gates and drift detection.

- [Matt Pocock](https://x.com/mattpocockuk/status/2026296080602673316) — 2026-02-25: Matt Pocock observes that AI coding rewards a 'lead dev' mentality: developers who spent their careers leveling up teammates through API design, feedback loops, and architecture find working with AI natural, while those who optimized only their own output find it uncomfortable.

- [Dr Milan Milanović](https://x.com/milan_milanovic/status/2025835518207127968) — 2026-02-23: Milan Milanović makes the case for git worktree (shipped in Git 2.5, July 2015): check out multiple branches into separate directories that share one .git, avoiding stashing and duplicate clones. The standout modern use case is AI agents - give each of 3-5 parallel Claude Code/Cursor/Codex agents its own isolated worktree and branch so they don't overwrite each other.

- [Jeremy Daly](https://x.com/jeremy_daly/status/2025677417398821351) — 2026-02-23: Jeremy Daly wrote a 100+ page guide on building multi-tenant, commercial AI agent systems from ~18 months running them inside a large SaaS platform serving hundreds of enterprise customers. Covers hard requirements around tenant isolation, auditability, retention, and cost control, plus orchestration models, retrieval architectures, and evaluation harnesses.

- [tuna](https://x.com/tunahorse21/status/2024974148259512677) — 2026-02-21: tuna signal-boosts Alex Fazio introducing Plankton, a 'slop guard' for LLM coding agents. It aims to break the loop of copy-pasting pre-commit/linting errors back into the agent by enforcing lint rules the model can't cheat around.

- [Charly Wargnier](https://x.com/datachaz/status/2024803152730423685) — 2026-02-20: Charly Wargnier argues writing crystal-clear instructions for machines is the new 10x dev skill, and the most important file in a repo is now CLAUDE.md rather than the code. Top devs use it as an AI onboarding doc to define agent behavior: force the AI to verify its own work, auto-fix CI bugs, and reject hacky fixes.

- [Adam](https://x.com/adamdotdev/status/2024525246993506346) — 2026-02-20: Adam (working on OpenCode since early 2025) offers an honest, ambivalent reflection on agentic programming: the models are an incredible tool and a real productivity boost, but the shift is confusing and emotionally mixed. He misses the flow of banging out mundane code by hand and notes the growing distance between the developer and the code.

- [Aman](https://x.com/amank1412/status/2023754885473394918) — 2026-02-19: Aman shares Garry Tan's (CEO of Y Combinator) CLAUDE.md prompt for Claude Code, which he uses to ship 4,000+ line features with full tests in about an hour. The prompt makes Claude act like a senior engineer: judge whether a plan is over/under-engineered before coding, do a structured review (architecture -> code quality -> tests -> performance), present tradeoffs with opinionated recommendations, and pause for feedback before implementing.

- [Matt Dancho (Business Science)](https://x.com/mdancho84/status/2023738764841894352) — 2026-02-18: Matt Dancho argues that becoming a '10X engineer' now comes down to a well-crafted SKILLS.md file, teasing a thread/resource on how to build one. High-engagement post (~1.1M views) with a lead-gen hook.

- [Dr Milan Milanovic](https://x.com/milan_milanovic/status/2023381859489767772) — 2026-02-17: Milan Milanovic's thesis: AI won't replace developers so much as the software-development process we're used to. Code is becoming cheap while decisions become expensive; AI reduces typing, not thinking. Developers who only implement tasks will struggle, while those who understand the product, domain, and system architecture will thrive.

- [dax](https://x.com/thdxr/status/2022574719694758147) — 2026-02-14: dax (thdxr) offers a contrarian take on AI coding hype: orgs are rarely bottlenecked by code-production ability. Most workers use AI to do their tasks with less effort rather than to become 10x; the few who genuinely push are getting buried under everyone else's 'slop code' and may quit; teams remain bottlenecked by bureaucracy; and CFOs are noticing each engineer now costs ~$2,000/month more in LLM bills.

- [Aakash Gupta](https://x.com/aakashgupta/status/2021709282224587141) — 2026-02-12: Aakash Gupta highlights Andrej Karpathy's 'microgpt': a complete GPT (training loop, inference, optimizer, attention) in 243 lines of Python whose only imports are os, math, random, and argparse, including a hand-rolled ~40-line scalar autograd engine. Frames it as the fifth step in a six-year compression arc: micrograd (2020), minGPT (2020), nanoGPT (2023), llm.c (2024), microgpt (2026).

- [kitze](https://x.com/thekitze/status/2021494167113990464) — 2026-02-12: kitze boosts Maximiliano Firtman's note that Chrome 146 ships an early flagged preview of WebMCP, which lets AI agents query and execute a web app's services without driving the UI like a human. Services are declared imperatively via a navigator.modelContext API or declaratively through a form; kitze calls exposing them 'the new responsive design.'

- [chiefofautism](https://x.com/chiefofautism/status/2019608146692673886) — 2026-02-07: chiefofautism shares Shannon (github.com/KeygraphHQ/shannon), an autonomous white-box AI pentester for web applications.

- [vogel](https://x.com/ryanvogel/status/2016204202343571474) — 2026-01-28: ryan vogel announces that dynamic agents.md resolution is now live in OpenCode, and suggests pairing it with a /learn command for a powerful workflow; points to @rekram11's explanation of the approach.

- [Theo - t3.gg](https://x.com/theo/status/2013888279355982131) — 2026-01-25: Theo boosts Wayne Sutton's launch of opensync.dev, a tool to track OpenCode and Claude CLI coding sessions in one place: searchable history, markdown export, eval-ready datasets, and views into tool usage, token spend, and session activity across projects. Theo frames it as a model of good devrel in 2026.

- [abhi](https://x.com/abhigyawangoo/status/2013823175855923640) — 2026-01-21: A detailed playbook for building continually-improving AI agents: define the business metric first, think in terms of many per-message/session/long-tail signals (not just thumbs up/down), design UI that makes signal collection easy, build signal-derived few-shot rankers, and A/B test every change against a control group. Includes a long copy-paste prompt for having Claude Code wire feedback loops into an existing agent. Warns about reward hacking when over-optimizing a single signal.

- [Matt Simpson](https://x.com/msmps_/status/2013376201977463038) — 2026-01-20: Matt Simpson shipped 'opentui-skill', a skill that gives coding agents TUI (terminal UI) superpowers via decision trees, progressive disclosure, and documented gotchas. Inspired by Dillon Mulroy's cloudflare-skill. Install instructions in a follow-up reply.

- [am.will](https://x.com/llmjunky/status/2013314055755194468) — 2026-01-20: am.will endorses a post by Dillon Mulroy on writing agent plans, calling it similar to his own approach but more concise. Plans to adopt some of Dillon's phrasing, especially the language around testing.

- [Sumanth](https://x.com/sumanth_077/status/2013232922296561826) — 2026-01-20: Overview of PageIndex, an open-source 'vectorless' RAG framework that drops vector databases and arbitrary chunking. It builds an LLM-optimized hierarchical tree (like a table of contents) and uses reasoning-based tree search to navigate documents the way a human expert would, giving traceable page-level references. Powers Mafin 2.5, which hits 98.7% on FinanceBench. GitHub link in comments.

- [Mischa van den Burg](https://x.com/mischa_vdburg/status/2013178484143571034) — 2026-01-20: Argues AI agent orchestration is the next 'container orchestration war', building on a Steve Yegge framework of two primitives: Workers (making a single agent produce high-quality output) vs Factories (coordinating thousands of work items across many agents). Maps these to familiar infra patterns - Workers = CI runners/pods/Lambdas, Factories = schedulers/control planes/workflow engines. Predicts 'nondeterministic idempotence' as the new eventual consistency, audit trails for AI work, GitOps-style declarative state, and reuse of the microservices observability stack. Kubernetes-fluent engineers have a head start.

- [Rohun](https://x.com/rohunjauhar/status/2012983351288692941) — 2026-01-19: Rohun open-sourced 'claude-build-workflow', a Claude Code workflow for autonomous building: you describe what you want, answer 10-15 min of interview questions, then close your laptop while an autonomous build loop runs in GitHub Codespaces and notifies your phone when done. It generates a PRD with user stories, technical architecture, edge-case analysis, story-quality validation, JSON conversion, then kicks off the build loop. Stitched together from Geoffrey Huntley's Ralph (bash-loop technique), Ryan Carson's snarktank/ralph (PRD skills, progress tracking, auto-commits, quality checks), and the BMAD Method (discovery/interview framework), adapted from Amp to Claude Code with phone notifications and one-command setup. Repo: github.com/rohunj/claude-build-workflow.

- [Ian Nuttall](https://x.com/iannuttall/status/2012833663319195970) — 2026-01-19: Ian Nuttall shares 'dotagents' (github.com/iannuttall/dotagents), a tool he built to stop the pain of switching between different agent harnesses/clients - he now runs everything from ~/.agents or .agents. Posted in reply to Theo asking for a way to sync agent skills/config across repos via symlink. PRs welcome for unsupported clients.

- [Abhishek Singh](https://x.com/0xlelouch_/status/2012816833464922398) — 2026-01-19: A Senior Staff Engineer's method for reasoning about unfamiliar systems: (1) start with the business goal and what 'failure' means, not the code; (2) identify the 2-3 critical paths where latency/correctness/money matter; (3) map ownership boundaries and handoff gray areas; (4) look for invariants that must hold even during partial failures/deploys; (5) read postmortems before docs (real vs intended behavior); (6) ask 'what breaks first at 10x load?' to expose hidden assumptions. The kind of skill that separates senior from staff.

- [Sisyphus Labs](https://x.com/justsisyphus/status/2012441415398109192) — 2026-01-17: Sisyphus Labs recommends Rohit Ghumare's article 'Agents 201: Orchestrating Multiple Agents That Actually Work' as the first useful piece on agent orchestration. The article's premise: after building a single agent, the next challenge isn't making it smarter but making multiple agents cooperate without blowing the token budget or creating coordination chaos.

- [giyu_codes](https://x.com/giyu_codes/status/2012420750855012428) — 2026-01-16: giyu_codes recommends cogsec (@affaan)'s article 'The Shorthand Guide to Everything Claude Code' - a complete setup after 10 months of daily use covering skills, hooks, subagents, MCPs, plugins, and what actually works. High-reach post (~806K views).

- [Gregor Zunic](https://x.com/gregpr07/status/2012052139384979773) — 2026-01-16: Gregor Zunic (Browser Use) argues 'The Bitter Lesson of Agent Frameworks': all the value is in the RL'd model, not thousands of lines of abstractions. An agent is just a for-loop of tool calls that runs until the model stops. Abstractions freeze assumptions and fight what the model already learned; agent frameworks fail because their action spaces are incomplete, not because models are weak. Their fix: start with maximal capability then restrict ('vibe-restrict' via evals). BU Agent gives the model raw Chrome DevTools Protocol + extension APIs for a near-complete action space. Also covers a minimal model-agnostic Chat wrapper (Anthropic/OpenAI/Google), ephemeral messages to keep massive DOM/screenshot state out of context, and the done() tool for explicit completion. Reliability (retries, rate limits, compaction) is ops, not the agent. Open-sourcing as agent-sdk (includes a Claude Code re-implementation).

- [Paul Solt](https://x.com/paulsolt/status/2012010080414081188) — 2026-01-16: Paul Solt's 7 beginner tips for OpenAI Codex: (1) start with GPT-5.2-Codex 'high' reasoning - enough for most work, avoid xhigh unless tricky; (2) when reasoning doesn't help, give agents better up-to-date local docs (he uses DocSetQuery to turn Dash DocSets into local Markdown); (3) read Peter Steinberger's (@steipete) 'shipping at inference speed' post; (4) borrow from Peter's agents.md and agent-scripts (e.g. 'committer' for atomic commits with multiple agents in one folder); (5) just talk to Codex - no complex rules or huge plan files; work one aspect at a time and parallelize projects while waiting; (6) ask agents to copy structure/Makefiles from other projects; (7) you'll likely need YOLO/danger mode to avoid constant approval nagging.

- [vas](https://x.com/vasuman/status/2011983687433212330) — 2026-01-16: vas (@vasuman) shares 'AI Agents 101,' a comprehensive long-form X article on how to build AI agents that actually work, framed as required reading before writing any code and drawing on 3 years as a Meta software engineer. He asks whether a part 2 would be useful.

- [Gergely Orosz](https://x.com/gergelyorosz/status/2011956185650409558) — 2026-01-16: Gergely Orosz amplifies Cindy Sridharan's take that, outside of prototyping, engineers should aim to understand close to 100% of the production code LLMs generate. He adds that the gap between teams who do this and those who don't will be massive, and notes the tension: heavy cutting-edge AI use is easiest on throwaway prototypes where it's fine to let it rip.

- [James Cowling](https://x.com/jamesacowling/status/2011924122922852599) — 2026-01-16: James Cowling points to the Software Crisis of the 1960s-70s (en.wikipedia.org/wiki/Software_crisis) as a warning: productivity ground to a halt until good abstractions for managing software complexity emerged. His thesis is that without good platforms, the same stall will happen again in the AI-coding era.

- [Jarrod Watts](https://x.com/jarrodwatts/status/2009200810870428123) — 2026-01-08: Jarrod Watts open-sourced his 'claude-code-config' repo containing all the agents, commands, hooks, rules, skills, and plugins he's made or collected over the past few months — described as simple but effective enhancements he'll keep updating. A ready-made reference config for a team standardizing Claude Code setups.

- [Denislav Gavrilov](https://x.com/kuberdenis/status/2004934631616086417) — 2025-12-28: Denislav Gavrilov containerizes Claude Code in Kubernetes as 'Clopus-Watcher,' an autonomous monitoring agent that watches a namespace and, on application errors, writes and applies a hotfix and documents it — effectively a 24/7 on-call engineer. Repo, examples, and results at denislavgavrilov.com.

- [AGENTS.md](https://agents.md/) — 2025-12-28: AGENTS.md (agents.md) is a simple, open format for guiding coding agents, now used by over 60k open-source projects. Think of it as a README for agents: a dedicated, predictable place for the build steps, tests, and conventions that coding agents need but that would clutter a human README — kept intentionally separate so agents have one clear location to look.

- [Tech with Mak](https://x.com/technmak/status/2002713140757496299) — 2025-12-22: A structured LangGraph learning path (pitched as filling the gap since LangGraph appears in ~half of AI job descriptions). Progresses from basic agent concepts (Pydantic data validation, agentic chatbots, multi-agent coordination) through production systems (a 2.5-hour LangGraph+MCP crash course, debugging/monitoring, deployment architecture) to RAG pipelines (multimodal RAG, hallucination fixes, end-to-end retrieval, Typesense search).

- [Santiago](https://x.com/svpino/status/2002107789888655655) — 2025-12-19: Santiago shares a video demoing a spec-driven development environment where 100% of the developer's time goes to writing specs and managing agents and 0% to writing code — arguing software development will never be the same.

- [Jason Fried](https://x.com/jasonfried/status/2002084849784676697) — 2025-12-19: Jason Fried shares a talk in which Jeff, an 18-year 37signals veteran, explains the 'recordables pattern' — the single most important architectural pattern behind Basecamp and HEY and a key reason both codebases remain a joy to work on. Fried calls the insights deep, practical, and accessible even to non-technical folks.

- [Justin Mitchel](https://x.com/justinmitchel/status/2001750598329499681) — 2025-12-19: Justin Mitchel flags that pg_textsearch was just open-sourced (github.com/timescale/pg_textsearch), a PostgreSQL extension bringing BM25 relevance-ranked full-text search to your database — meaning teams already on Postgres can skip syncing data to Elasticsearch for keyword search. Post is marked #sponsored.

- [Matt Dancho (Business Science)](https://x.com/mdancho84/status/2000658529753932273) — 2025-12-15: Matt Dancho highlights an open-sourced (free) Python library, 'AI Data Science Team' (github.com/business-science/ai-data-science-team), that automates data-science workflows with AI — data loading, cleaning, exploratory analysis, and feature engineering — tracking each step in a fully reproducible pipeline. Includes a walkthrough video and a free 1-hour agentic AI workshop.

- [Yahiya](https://x.com/yahiyadev/status/1997744726913736979) — 2025-12-08: Answering a request for a book on structuring a monolith so services can be decoupled later, Yahiya recommends 'Event-Driven Architecture in Golang' by Michael Stack — which starts from a modular monolith and gradually transitions to microservices, covering Event Sourcing, CQRS, DDD, choreographed and orchestrated messaging, and sync-to-async refactoring — plus 'Domain-Driven Design with Golang' by Matthew Boyle.

- [AWS Containers](https://github.com/aws-containers/reinvent) — 2025-12-01: The aws-containers/reinvent GitHub repo collects AWS re:Invent 2025 Kubernetes Track assets — slides, the latest EKS launches, and demos from the sessions. A reference for what AWS shipped for Kubernetes/EKS at re:Invent 2025.

- [Dan Shipper](https://x.com/danshipper/status/1986870518046200255) — 2025-11-08: Dan Shipper recommends Kieran Klaassen's Every piece 'Teach Your AI to Think Like a Senior Engineer' (every.to/source-code) as a masterclass on coding with AI.

- [Matt Pocock](https://x.com/mattpocockuk/status/1983255353597870285) — 2025-10-29: Matt Pocock shares his favorite AI coding tip: add 'Be extremely concise. Sacrifice grammar for the sake of concision.' to your global claude.md file for noticeably better output.

- [Pontus Abrahamsson](https://x.com/pontusab/status/1981700333857636550) — 2025-10-24: Pontus Abrahamsson points to midday-ai/ai-sdk-tools (github.com/midday-ai/ai-sdk-tools) — a set of example AI SDK tools/integrations for building agent tooling.

- [Thomas H. Ptacek](https://x.com/tqbf/status/1981439969370558803) — 2025-10-24: Thomas Ptacek, reacting to the AWS outage postmortem and its HN discussion, evangelizes 'How Complex Systems Fail' (howcomplexsystems.fail) as essential reading on how failures emerge in complex socio-technical systems.

- [Raul Junco](https://x.com/rauljuncov/status/1980243241783197925) — 2025-10-21: Raul Junco frames system design as a staircase to climb step by step rather than jumping to distributed systems: foundations (networking, databases, caching, APIs), then mechanics (queues, consistency, observability, failures), then architecture (trade-offs, evolution, resilience).

- [Vivek Galatage](https://x.com/vivekgalatage/status/1974894313948758373) — 2025-10-07: Vivek Galatage recommends Richard Hipp's 2024 'SQLite: How it works' lecture on database internals from the creator himself, in a thread noting SQLite's ubiquity (including in Chromium browser engines).

- [Sumit Mittal](https://x.com/bigdatasumit/status/1972908540692947192) — 2025-10-01: Sumit Mittal walks through S3/Athena query cost optimization: moving from uncompressed row-based CSV to columnar Parquet with Snappy compression, partitioning by city, and column pruning cuts a $25 full-scan query to about $0.01 (~2500x cheaper). Ends with a course promo.

- [Jawad](https://x.com/jawad_shreim/status/1972998935687172213) — 2025-09-30: Jawad shares a humorous, plain-language 'explanation' of AWS services (EC2, ECS, etc.) quote-tweeted from MilkStraw AI.

- [Jamon](https://x.com/jamonholmgren/status/1969883090056249776) — 2025-09-23: Jamon Holmgren strongly recommends Lydia Hallie's article 'Behind The Scenes of Bun Install' as a top-10 must-read for every developer on building performant systems, regardless of whether you use JavaScript or Bun.

- [Dan McAteer](https://x.com/daniel_mac8/status/1970120352664605124) — 2025-09-22: Shares a four-step agentic-coding pattern with an added Verification step (build feedback loops that test the plan was implemented correctly, since models still fail on execution), meant to be copied into an AGENTS.md file. Works with AmpCode or any AGENTS.md-aware coding agent.

- [Raul Junco](https://x.com/rauljuncov/status/1962850589165129870) — 2025-09-03: A practical guide to the Retry pattern for resilience: cap retries (~3), use exponential backoff to avoid the thundering-herd effect, retry only transient errors (408/5xx, not 4xx), and pair with a circuit breaker to prevent cascading failures on a truly-down service.

- [ℏεsam](https://x.com/hesamation/status/1962508535515791739) — 2025-09-02: Recommends a blog (linked in the post) as a strong source of technical playbooks, useful both for engineers and for managers who want a grounding in technical topics.

- [Dan Shipper](https://x.com/danshipper/status/1957469868862677028) — 2025-08-19: Links Dan Shipper's Every essay 'My AI Had Already Fixed the Code Before I Saw It,' on AI coding agents autonomously fixing code before the developer even reviews it.

- [Imrat](https://x.com/imrat/status/1954497164589056090) — 2025-08-11: A recipe for using Claude Code as a DevOps agent with its new background jobs: run Claude in a tmux session, have it spawn a background process to tail server logs and summarize them, then a second process that pings Claude to 'check logs' on an interval.

- [K Srinivas Rao](https://x.com/sriniously/status/1950432839474012456) — 2025-07-31: [Post unavailable — page doesn't exist]

- [Graham Helton](https://x.com/grahamhelton3/status/1936462167751921698) — 2025-06-23: Before leaving Google for Snowflake, Graham Helton braindumped ~34 personal guidelines/principles he follows for work and productivity; the thread lists them.

- [Tom Dörr](https://github.com/tom-doerr/dotfiles/blob/master/instruction.md) — 2025-01-04: Tom Dörr's AI-coding-agent instruction file (an AGENTS.md-style rules doc): single-letter command aliases (c=continue, rc=reduce complexity, acp=add/commit/push, t=add tests), strict engineering rules (no fallbacks, don't swallow exceptions, TDD with many asserts, uv over pip, work on git branches, keep complexity low, don't weaken the linter), and ready-to-paste DSPy optimizer snippets (BootstrapFewShotWithRandomSearch, MIPROv2, SIMBA).

- [Elon Musk](https://x.com/elonmusk/status/1862363270931255356) — 2024-11-29: Elon Musk touts his '5-step algorithm' for making fewer mistakes (make requirements less dumb, delete parts/processes, simplify & optimize, accelerate cycle time, automate), in a quote of a post speculating DOGE might adopt it like SpaceX.

- [Shubham Saboo](https://x.com/saboo_shubham_/status/1849638773136687551) — 2024-10-25: Introduces AutoRAG, an open-source tool that automatically benchmarks multiple RAG strategies to find the optimal RAG pipeline for your data in a few lines of Python.

- [Sarah Cone](https://x.com/sarah_cone/status/1847322215907545129) — 2024-10-19: Points to a superengineer.net blog post as a good summary of Elon Musk's 5-step design/engineering method (DFX).

- [Dominik Tornow](https://x.com/dominiktornow/status/1846507701599433179) — 2024-10-17: Flags a paper as a strong discussion of how hard retries are to get right for reliability under failure—retries are often oversold as a simple fix but are surprisingly complex.

- [Matt Pocock](https://x.com/mattpocockuk/status/1811332713107923156) — 2024-07-10: A take on pre-commit hooks: Matt Pocock prefers 'fewer guard rails, more safety nets'—favoring tooling that catches problems after the fact over friction that blocks commits up front.

- [curvedinf](https://github.com/curvedinf/dir-assistant) — 2024-06-18: dir-assistant is a pip-installable CLI that recursively indexes the text files in your directory so you can chat with them via a local or API LLM, auto-injecting the most contextually relevant files. It uses CGRAG (Contextually Guided RAG) for file selection, supports interactive and single-prompt modes (including auto file edits + git commits), many local acceleration backends and all major LLM APIs via LiteLLM, and optimizes prompt/context caching (50-90% cache hits).

### Skills & MCP (146)

- [JoePro](https://x.com/joepro/status/2076877282312954311) — 2026-07-14: JoePro shares a reworked 'Frontend Design Skill' (an agent/Claude skill spec) engineered to produce distinctive, production-grade UIs that avoid recognizable AI-generated tropes — covering success criteria (signature visual identity, complete states, WCAG AA accessibility, token-driven design systems) and a context-gathering routine before writing code.

- [How To Prompt](https://x.com/howtoprompt__/status/2076689880026096089) — 2026-07-14: How To Prompt highlights an open-source, privacy-first Chromium fork built by an ex-Google engineer with a native AI agent, built-in MCP server, Cowork-style web+local-file agents, scheduled autopilot tasks, 40+ app integrations (Gmail, Slack, Notion, Linear, Figma, Salesforce), and local-model (Ollama) support — drivable from Claude Code or Gemini CLI. Engagement-framed but describes a real agentic-browser tool worth evaluating.

- [Jamon Holmgren](https://x.com/jamonholmgren/status/2076001786700394610) — 2026-07-13: Jamon Holmgren dumps his complete agentic coding setup as a 10+ point checklist: an AGENTS.md that acts as a router to skills/docs/tools; a customized workflow skill (he recommends grabbing Matt Pocock's skills); self-healing, greppable docs with a 7-line summary header; agents that actually run and test the app themselves; e2e tests plus docs on how/what to test; custom precommit linters with --fix that shell out to a cheaper LLM (Composer 2.5 or Sonnet) to actually fix rather than flag; cross-agent review (codex/claude/cursor, never the same model reviewing itself) at research/plan/implementation/wrap-up; handoff worksheets committed with git tags so another agent can finish the job; automatic end-of-session agent feedback docs he periodically ingests to improve workflows; a tools/bin folder of agent-authored scripts (e.g. an agent_review CLI wrapper); and periodic agent sweeps through recent commits. Practical, adoptable patterns for a team running coding agents.

- [How To Prompt](https://x.com/howtoprompt__/status/2074122800961614184) — 2026-07-07: How To Prompt (hype framing: "China has killed the vector database industry") flags Tencent's newly open-sourced TencentDB Agent Memory — local long-term memory for AI agents that runs 100% on plain SQLite with no external vector DB or cloud APIs. Claims 61% fewer tokens and PersonaMem accuracy 48%->76%. Uses a layered 'semantic pyramid' (L0 conversation -> L1 atom -> L2 scenario -> L3 persona) stored as inspectable markdown + Mermaid graphs instead of opaque vector compression, with drill-back to raw logs by node_id. ~5.1k GitHub stars.

- [ericosiu](https://x.com/ericosiu/status/2073943223836270933) — 2026-07-06: Eric Siu shares a 7-step checklist for building a 'Company Brain' (an org-wide AI agent): (1) pick one high-value workflow closest to revenue; (2) map only the critical connectors (Google Drive, Slack, CRM, Gong, Granola); (3) define memory — brand voice, decisions, workflow rules, examples, with recent decisions weighted over old ones; (4) set permissions/approvals/data exposure to avoid 'a security problem with a chat interface'; (5+) route the work. A practical playbook for company-wide AI adoption.

- [Isra](https://x.com/israfill/status/2073789727698743516) — 2026-07-06: Isra flags Alibaba's newly open-sourced Page-Agent (~22K GitHub stars, +949 in a day) — an MIT-licensed JavaScript library that embeds an AI agent directly into any webpage via a single <script> tag. It reads the live DOM as structured text and acts as the real user with no headless browser, Selenium/Playwright, Python server, or computer vision. Works with any LLM (GPT, Claude, Grok, Qwen, local via Ollama), has built-in human confirmation before critical actions, and can pair with the Web Speech API for voice control. Pitched as a lightweight replacement for Selenium/Playwright and vision-based browser agents.

- [Nyk](https://x.com/nyk_builderz/status/2073305434069647735) — 2026-07-05: [Jeremy flagged: urgent for orchestration] Nyk released Council of High Intelligence v1.2.0 as a Claude Code plugin (/plugin marketplace add 0xNyk/council-of-high-intelligence) — an 18-persona deliberation engine (Aristotle, Feynman, Kahneman, Torvalds, Socrates, Taleb, Meadows + more) that runs 3 rounds of anonymized cross-examination to one auditable verdict on your existing subscriptions, no API keys. v1.2.0 adds confidence-weighted verdicts (vote weight scales with stated confidence; a hesitant council escalates to you instead of forcing consensus, per Roundtable Policy + ConfMAD 2025), per-persona reasoning methods (Socratic elenchus, Taleb tail stress-testing, Meadows causal-loop mapping via DMAD), per-project defaults via .council.yaml, and CI parity gates so the Claude/Codex/Gemini coordinators can't silently drift.

- [Elvis](https://x.com/elvissun/status/2073161303997452794) — 2026-07-05: Elvis makes a meta point about eval-driven skill building that extends beyond coding to any knowledge problem where an eval set can be concretely defined. Example: a newsjack.sh skill that judges newsworthiness — he started from labeled examples (stories that made real news vs ones that didn't, e.g. hitting #1 on Product Hunt isn't news even though LLMs say it is), fed them into an eval set, then used /goal to iterate a skill implementation that lets 3 agents (Opus, Sonnet, Haiku) all score stories correctly — proving 'the intelligence lives in the skill, not the model.' Notes Fable's ability to learn across examples and draw a through-line is well beyond Opus.

- [Tom Dörr](https://x.com/tom_doerr/status/2073354493794636248) — 2026-07-04: Tom Dörr shares VoltAgent's awesome-claude-skills (github.com/VoltAgent/awesome-claude-skills) — a curated 'awesome list' of official agent Skills from leading engineering teams.

- [0xSero](https://x.com/0xsero/status/2073274981279260774) — 2026-07-04: 0xSero shares Parcels (github.com/0xSero/parcels) — a tool for 'cloud agents' when you have Tailscale and more than one desktop: it packages your repo plus a live coding-agent session (Claude Code / Codex / pi), transfers it to another machine on your Tailscale network, and runs it in tmux so you can step away from the screen.

- [Archive](https://x.com/archiveexplorer/status/2073136973162872897) — 2026-07-04: Archive (engagement framing, 'met an Anthropic engineer making $1.2M') argues the real lever isn't Opus vs Sonnet but 'what the model wakes up into' — the .claude/ folder: CLAUDE.md (the contract), settings.json (permissions), hooks/ (reflexes), agents/verifier (a shift-notes checker subagent), skills/ (~33 reusable 'muscle memories'), .mcp.json (tools), and MEMORY.md (shift log). 'You write the folder once; the folder runs the model.' Quote-tweets his own article 'Loop and Harness engineering: 7 files, 5 steps.'

- [Dhilip Subramanian](https://x.com/sdhilip/status/2072334422414876957) — 2026-07-02: Dhilip walks through his 7-skill Claude Code setup and what each earns its spot for: data engineering (dbt/Airflow), gstack, grill-me, superpowers (spec/plan/TDD), impeccable (UI audit), last30days, and printing-press (API/site to token-light CLI). Advice: start small, add a skill only when you hit a job your current ones can't do.

- [Akshay](https://x.com/akshay_pachaar/status/2071509401224261823) — 2026-06-29: Walkthrough of Google's Agents CLI as tooling for Karpathy's "agentic engineering" (spec design, eval loops, security). One setup command injects 7 ADK-specific skills into a coding agent; author built and deployed a RAG agent end-to-end with Claude Code, including 20 LLM-as-judge eval scenarios and enterprise registration.

- [Brady Long](https://x.com/thisguyknowsai/status/2070445026233172314) — 2026-06-27: Promo-styled writeup of MemPalace, an open-source local AI memory tool (49K stars). Instead of dumping everything into semantic search, it organizes memory into a structured "palace" (people/projects as wings, topics as rooms, verbatim text in searchable drawers). Claims 96.6% retrieval recall on LongMemEval with zero LLM/API/cloud, 98.4% with a hybrid pipeline; ships 29 MCP tools and auto-save hooks for Claude Code. Python 3.9 + ChromaDB, ~300MB, MIT.

- [Nav Toor](https://x.com/heynavtoor/status/2069773963413340297) — 2026-06-25: Listicle-styled promo for MinerU, an open-source document-extraction tool (68.5K stars) from Shanghai AI Lab's OpenDataLab. Reads PDFs/Office docs/scanned images into clean Markdown with reading-order text, tables → HTML, equations → LaTeX, OCR, 109 languages, batch mode, and 10k-page docs via sliding window. CLI, Python SDK, or web app; plugs into Claude Desktop, Cursor, LangChain, LlamaIndex, etc. Apache-2.0-based license, free.

- [Akshay](https://x.com/akshay_pachaar/status/2069769689560187027) — 2026-06-25: Breakdown of "loop engineering" (opening on a Karpathy quote about removing yourself as the bottleneck): a trigger decides what runs, the loop is the maker, a separate checker grades output (a model grading itself just justifies its work), and state lives on disk not context (suggests Zep's Graphiti temporal knowledge graph). Two failure points: set the exit condition before the loop runs, and add observability on the harness since the checker only catches in-run failures (suggests Comet's Opik). Thesis: the model is a commodity; the loop around it is where the engineering lives.

- [Matthew Berman](https://x.com/matthewberman/status/2069098257444434425) — 2026-06-23: Matthew Berman announces a new Loop Library feature, Lazy Loops (aka Discover), which scans your codebase and chat threads to find potential agentic loops and designs them for you. Links the Forward-Future/loop-library GitHub repo of practical, repeatable AI-agent workflows.

- [冬天](https://x.com/seventhoce56019/status/2068901168940745088) — 2026-06-23: Translated from Chinese: a writeup of reverse-skill (GitHub zhaoxuya520/reverse-skill), an AI skill package that puts reverse-engineering and security tasks behind a routing.md file so the agent self-triages across 20+ sub-skills (APK reversing, IDA static analysis, JS frontend reversing, firmware security, EDR evasion, vulnerability exploitation). Framed as lowering the barrier to security offense/defense.

- [Codez](https://x.com/0xcodez/status/2064374643729773029) — 2026-06-23: A long-form Loop engineering roadmap arguing the leverage point in agentic coding has moved from writing prompts to designing self-running loops. Covers the 4-condition test for when a loop is worth building (task repeats, automated verification, token budget, senior-engineer tooling), the five building blocks (automations like /loop and /goal, git worktrees, skills, MCP connectors, sub-agents), the maker/checker split, the Ralph Wiggum quiet-failure mode, comprehension debt and cognitive surrender, and the security tax of unattended loops. Cites Anthropic engineering docs and Addy Osmani.

- [Hasan Toor](https://x.com/hasantoxr/status/2066247422502957197) — 2026-06-15: Highlights Headroom, a GitHub tool by Netflix engineer Tejas Chopra that compresses everything an AI agent reads before it reaches the LLM (tool outputs, logs, files, RAG chunks, code-search results, conversation history), claiming 60-95% fewer tokens for the same answers. Ships as a Python/TypeScript library, local proxy, and MCP server, with wrappers for Claude Code, Codex, Cursor, Aider, and Copilot.

- [Teknium](https://x.com/teknium/status/2066185784332562605) — 2026-06-15: Demo: the author used the Hermes Agent with a Manim video-generation skill plus its TTS tool to autonomously produce a video explaining the Hermes Agent itself — a self-referential showcase of composing a skill and a tool inside an agent.

- [Avid](https://x.com/av1dlive/status/2065747876005937416) — 2026-06-14: Promotes a 'second brain' pattern attributed to Karpathy: let an LLM maintain a wiki of your notes so knowledge compounds as you dump sources and it reads, links, and files them. Points to a free Claude Code plugin, claude-obsidian by AgriciDaniel (claude plugin marketplace add AgriciDaniel/claude-obsidian; claude plugin install claude-obsidian@agricidaniel-claude-obsidian), then run /wiki inside an Obsidian folder. Quote-tweets the author's own article on building Obsidian from scratch with 13+ Kimi agents.

- [Marie Haynes](https://x.com/marie_haynes/status/2065531158356717721) — 2026-06-13: Flags Google's new Open Knowledge Format (OKF): a standardized way to store information as a directory of interlinked markdown files that acts as a living wiki agents can query and edit, which the author thinks could replace Notion or Obsidian. References Google Cloud's blog post and the spec at github.com/GoogleCloudPlatform/knowledge-catalog (okf/SPEC.md), and notes feeding both links to Antigravity to brainstorm project uses.

- [Suryansh Tiwari](https://x.com/suryanshti777/status/2065473893817848266) — 2026-06-13: Claims Anthropic released an official Claude Code plugin, claude-code-setup, that scans your project and recommends and sets up hooks, skills, MCP servers, subagents, and automations step-by-step (install: /plugin install claude-code-setup@claude-plugins-official), arguing most people run Claude Code vanilla and miss the surrounding ecosystem. Quote-tweets the author's own 'Unveil' build. (Treat the 'official' claim as unverified.)

- [hoeem](https://x.com/hooeem/status/2064099329342640285) — 2026-06-09: hoeem hypes Matt Pocock's new /teach skill — pours 10 years of teaching experience into a Claude skill that teaches you anything (Pocock's demo: it taught him to solve a Rubik's cube). Worth a look as a reusable Claude Code skill pattern.

- [rari](https://x.com/0xwhrrari/status/2063244577482440978) — 2026-06-08: Engagement-farmed but useful link dump of free AI-engineering learning resources (LangChain agent architecture, Anthropic's Claude Code 101 + in-action courses, prompt engineering docs, anthropics/courses interactive prompt tutorial, claude.md docs, skills, MCP). Wrapped in 'Google's former CEO just said...' framing but the underlying link list is the substance.

- [Ole Lehmann](https://x.com/itsolelehmann/status/2061911202830401564) — 2026-06-04: A ~10-minute recipe to turn your X bookmarks into an agent-queryable second brain: export bookmarks (twitter-web-exporter / BookmarkSave), drop the file into your LLM wiki or Obsidian vault, and have your agent convert each into a tagged markdown note with the original link — then query across the whole pile. Directly relevant to this link collection.

- [Thariq](https://x.com/trq212/status/2061907538741006796) — 2026-06-03: Announces dynamic workflows as the biggest Claude Code upgrade since skills and subagents — Claude writing its own task-specific harness on the fly — with excitement about the non-technical tasks it unlocks.

- [Thariq](https://x.com/trq212/status/2061907337154367865) — 2026-06-03: Full Anthropic article on dynamic workflows in Claude Code: Claude writes its own JavaScript harness to spawn/coordinate subagents (own models, own worktrees, resumable), countering agentic laziness, self-preferential bias and goal drift. Covers patterns (fan-out-and-synthesize, adversarial verification, tournament, loop-until-done), many use cases (migrations, deep research, triage, root-cause, evals, model routing), the 'ultracode' trigger, token budgets, and when NOT to use it.

- [Tom Dörr](https://x.com/tom_doerr/status/2061674811122713013) — 2026-06-03: Shares FlowForge, a Skill that generates professional draw.io diagrams from natural language (github.com/wentong2022-arch/flowforge-skill).

- [darkzodchi](https://x.com/zodchiii/status/2061040686330257656) — 2026-05-31: Anthropic-engineer clip: build 5 focused agents (code review, tests, docs, security) in an afternoon, each ~15 minutes as a markdown file with instructions + prompt. Links a beginner subagent-building template.

- [Mr. Buzzoni](https://x.com/polydao/status/2060964743402455212) — 2026-05-31: Engagement-farmed ALL-CAPS thread riffing on Karpathy's 'we're in the 1960s of AI' / software-3.0 framing to push the author's own listicle article '...These Are the Ones That Matter [Full GitHub Links]' cataloguing 32 Claude skills. Clickbait wrapper, but the underlying skills roundup may be worth a skim.

- [恒星](https://x.com/vintcessun/status/2060897802478293013) — 2026-05-31: DeepMind packaged 30+ scientific databases (AlphaGenome, UniProt) into agent skills. The real bottleneck for science agents isn't model quality but knowing how to call databases correctly; skills turn each DB's API into clear instructions + scripts so agents execute step-by-step. One-line npx install (github.com/google-deepmind/science-skills).

- [Charly Wargnier](https://x.com/datachaz/status/2059649544854327466) — 2026-05-29: Recommends Akshay Pachaar's 47-minute 'Hermes Agent Masterclass' on building self-improving, 24/7 local autonomous agents — self-evolving skills, three-tier memory, GEPA optimization, scaling from 1 to 10 agents.

- [Charly Wargnier](https://x.com/datachaz/status/2059909626532155482) — 2026-05-28: Microsoft open-sourced SkillOpt: optimize agent skills the way you train models — a base model runs tasks while an optimizer rewrites the instructions, keeping only edits that raise the benchmark. Claims SOTA over hand-crafted prompts and TextGrad, with no model lock-in since it learns procedural logic.

- [Kyle Jeong](https://x.com/kylejeong/status/2059753008297394245) — 2026-05-28: Browser agents have an 'amnesia problem' — re-discovering each site from scratch every run. Autobrowse uses iterative AutoResearch to let an agent improve its own browser skills (/autobrowse), reportedly up to 90% faster and cheaper.

- [Jerry Liu](https://x.com/jerryjliu0/status/2059710330016817501) — 2026-05-28: LiteParse v2: LlamaIndex's PDF parser rewritten in Rust with native Python/Node (and WASM) packages — claimed fastest and most accurate open-source model-free parser, up to 100x faster, 50+ document types, installable inside an AI agent.

- [刘醒](https://x.com/xingxingli45573/status/2059258034820706541) — 2026-05-27: Taste Skill (~20.3k stars): an install that gives AI-generated front-ends better taste — improved layout, fonts, animations, whitespace — with design directions (premium, minimalist, brutalism), an audit-and-fix skill for old projects, a mockup-first image skill, and three tunable params (layout experimentation, animation richness, info density).

- [Vaishnavi](https://x.com/_vmlops/status/2059207888393138556) — 2026-05-27: Microsoft open-sourced an Agent Governance Toolkit: deterministic interception of every tool call (denied actions structurally impossible), a YAML allow/deny/human-approval policy engine, zero-trust identity (SPIFFE/DID/mTLS), a 4-level execution sandbox, tamper-evident Merkle audit logs, coverage of all OWASP Agentic Top-10 risks, and support across major frameworks and languages — because 'follow the rules' in a prompt is a suggestion, not a guardrail.

- [Shubham Saboo](https://x.com/saboo_shubham_/status/2058269167372153129) — 2026-05-24: Positions codebase-as-queryable-graph as the real 'context engineering' for coding agents — turning any codebase into an interactive graph the agent can query; works with Claude Code, Codex, Antigravity; fully open-source.

- [Kevin Simback](https://x.com/ksimback/status/2058262328496554021) — 2026-05-24: A definitive guide to memory in the Hermes Agent, structured as a 3-layer stack: Layer 1 native (two always-injected markdown files MEMORY.md/USER.md plus a searchable SQLite session DB; the 80% consolidation 'rule' is a prompt instruction, not code), Layer 2 the pluggable MemoryProvider slot (8 official providers — Honcho, Mem0, Hindsight, Holographic, OpenViking, RetainDB, ByteRover, Supermemory — one at a time, each a different architectural bet), and Layer 3 community plug-ins (GBrain, Mnemosyne, etc.). Closes with how to pick and warning signs a memory layer is too heavy.

- [George Nurijanian](https://x.com/nurijanian/status/2058259663238631890) — 2026-05-24: Fixed Claude's 'chart junk' by handing it a book and having it spin up a Tufte-flavored visualization skill — producing leaner, clearer visuals (github.com/gnurio/tufte-vdqi-plugin).

- [Charly Wargnier](https://x.com/datachaz/status/2057787509728522463) — 2026-05-23: Repo shoutout to addyosmani/agent-skills — production-grade engineering skills for AI coding agents, open-sourced by Addy Osmani.

- [swyx](https://x.com/swyx/status/2057559570177007912) — 2026-05-22: swyx is building a skill to turn a vibecoded 'slop' app into a production-ready, e2e-tested, maintainable, parallelizable agent repo — one run went ~16 hours and 103 commits, ending with the same app but a codebase he can build on.

- [BOOTOSHI](https://x.com/kingbootoshi/status/2057528772208034195) — 2026-05-22: Shares an S+-tier skill, directional-prompting (outcome-first + directional language, a two-layer approach), combined with /goal mode — 'agents thrive on positive communication; make the path to success clear.'

- [Alex Veremeyenko](https://x.com/alex_prompter/status/2057476020454949201) — 2026-05-22: Anatomy of the perfect SOUL.md identity file for AI agents — the file an agent reads first. Nine sections: Identity, Values, Communication Style, Expertise, Boundaries, Workflow, Tool Usage, Memory Policy, Example Interactions. 'Be helpful and professional' describes nothing; strong files have real opinions, specific limits, and concrete examples; 200-500 words, shorter = sharper.

- [Akshay](https://x.com/akshay_pachaar/status/2057446083853520948) — 2026-05-22: Argues 'Claude Code isn't a coding tool — it's a programmable dev environment,' with 12 features that make it programmable: CLAUDE.md, Rules, Skills, Hooks, Slash Commands, Plugins, MCP, Plan Mode, Permissions, Subagents, Voice Mode, Rewind (1-5 define the environment, 6-7 extend it, 8-9 control it, 10-12 change how it runs).

- [Greg Ceccarelli](https://x.com/gregce10/status/2056771029867933884) — 2026-05-20: Field notes on a 'goal engineering' workflow: instead of prompts/specs, write two checked-in markdown artifacts per round — a 'goal' capped at 4,000 chars (matching Codex's /goal limit) and an unbounded 'rider' with ~11 phases and named depth tests — authored via a Skill. Aimed at long-running agentic turns.

- [Garry Tan](https://x.com/garrytan/status/2056711154224034125) — 2026-05-20: Garry Tan on dynamic, just-in-time skills for personal AI: 'markdown is code,' and the agent can change its own skills when new cases appear — 'just-in-time personal software is the most powerful idea of 2026.' A reply notes skill bundles carrying their own tests that the agent modifies in-flight create the compounding effect.

- [Suryansh Tiwari](https://x.com/suryanshti777/status/2056022182560665602) — 2026-05-18: Highlights Anthropic's official 'claude-code-setup' plugin that scans a project and recommends hooks, skills, MCP servers, subagents, and automations (/plugin install claude-code-setup@claude-plugins-official). A Community Note corrects the post: the plugin is read-only — it recommends but does NOT install or modify files.

- [AYi](https://x.com/ayi_ainotes/status/2055954675526934642) — 2026-05-18: Enthusiastic (Chinese) take on Garry Tan's GBrain — 'not another RAG toy' but a complete personal-knowledge OS with 8 layers (vs the usual 4): install on OpenClaw/Hermes/Claude Code to remember relationships, decision trajectory, and long-term cognitive evolution, turning per-chat starts into lifelong memory + self-evolution. Garry's production ran 17,888 pages / 4,383 people / 723 companies.

- [Vasilije](https://x.com/tricalt/status/2055876832797581406) — 2026-05-18: 'Memory isn't a plugin. Skills aren't a plugin. They're the same harness' — both are a world model (everything the agent uses to predict its next action). Memory observes the world; skills (SKILL.md procedures) codify it into rules and degrade silently without an Observe→Inspect→Amend→Evaluate loop. Cognee stores skills and memory in one graph so a skill is a traceable, evolving memory node.

- [George from prodmgmt.world](https://x.com/nurijanian/status/2055333397611077881) — 2026-05-15: Favorite ways to 'write requirements' with AI: /grill-me (mattpocock/skills), /shaping (rjs/shaping-skills), and a new skill built from business-analyst literature ('make-requirements-great') — reviving useful BA rigor that got dropped as teams went agile/sloppy.

- [Geek Lite](https://x.com/qingq77/status/2054056472477307084) — 2026-05-14: Oh My Hermes (github.com/Salomondiei08/oh-my-hermes) is a skills+workflow layer for the Hermes Agent that ships 20 skills covering the full app lifecycle (requirements through monitoring/GitHub ops) and 5 role-specialized agents (CTO/PM/Dev/QA/Ops) collaborating on a kanban board. Treats Hermes as primary operator and Claude Code/Codex as optional accelerators — a concrete prior art for our skills + sub-agent architecture.

- [Miles Deutscher](https://x.com/milesdeutscher/status/2054310749884002348) — 2026-05-13: Promotion of skillsmp.com — a marketplace claiming over 1 million ready-to-use agent skills and plug-ins. Marketing-heavy "complete game-changer" framing, low actual detail.

- [George from prodmgmt.world](https://x.com/nurijanian/status/2054216035503587396) — 2026-05-13: George keeps reusing his own AI skill-building pipeline and wishes it were a product. Quote of his March 28 article on building AI skills as a non-expert by finding subject-matter experts in PDFs (he built game-theory and formal-logic skills this way).

- [コムテ (Komte)](https://x.com/commte/status/2054136870016356408) — 2026-05-13: Google open-sourced 13 official Agent Skills (github.com/google/skills) compliant with the Agent Skills standard — interoperable with Claude Code, Antigravity, Gemini CLI, Cursor, GitHub Copilot, and other major agents. Significant cross-vendor signal for the Agent Skills standard.

- [Muhammad Ayan](https://x.com/socialwithaayan/status/2053875867487777175) — 2026-05-12: Engagement-farmed announcement (all-caps 'BREAKING') that Anthropic open-sourced a Claude Code plugin suite for finance workflows — DCF/LBO models, equity research, M&A analysis, KYC, IC memos — with MCP connectors for Bloomberg, FactSet, S&P Global, Morningstar, and PitchBook (github.com/anthropics/financial-services, Apache-2.0, ~19.8K stars). Top replies flag the obvious caveat: the harness is free but the data feeds (Bloomberg Terminal ~$28K/yr, FactSet/S&P/PitchBook six-figure) are not, and the agents draft work for human sign-off rather than autonomously owning workflows.

- [Axel Bitblaze](https://x.com/axel_bitblaze69/status/2052520764545613958) — 2026-05-08: claude-handoff plugin (install: /plugin marketplace add willseltzer/claude-handoff && /plugin install handoff) — three commands (/handoff:create, /handoff:quick, /handoff:resume) that generate a HANDOFF.md with full session state (branch, commits, files touched, dead ends) so a fresh Claude Code session can pick up where the old one ended. Targets the 10-20 message context-degradation point Anthropic recommends restarting at.

- [Avi Chawla](https://x.com/_avichawla/status/2052482874126020882) — 2026-05-08: Avi Chawla on Karpathy's 'remove yourself as the bottleneck' framing and Rowboat — an open-source AI 'second brain' built on the Markdown/Obsidian foundation Karpathy uses, extended to work context (emails, meetings, decisions, commitments). The pitch: most people can't act on Karpathy's advice because their AI has no memory of their work, and Rowboat is one open-source answer to that.

- [Tom Dörr](https://x.com/tom_doerr/status/2052440598452359394) — 2026-05-08: Tom Dörr surfaces 'agentmemory' (github.com/rohitg00/agentmemory) — a knowledge-graph memory layer for Claude Code. Pair with the other agent-memory tools in the corpus (HelixDB, turbovec, mem0).

- [Millie Marconi](https://x.com/milliemarconnni/status/2052363436575826398) — 2026-05-08: Millie Marconi highlights Feynman (github.com/getcompanion-ai/feynman) — an open-source MIT-licensed agent system with four bundled roles (Researcher, Reviewer, Writer, Verifier) that reads papers, audits referenced code, and replicates experiments. Runs in Docker for safe local execution and spins up serverless GPUs on Modal or persistent pods on RunPod. Indexed session search across past research runs, inline citation-URL verification.

- [Rohit Ghumare](https://x.com/ghumare64/status/2052313902214476192) — 2026-05-08: Rohit Ghumare highlights agentmemory — a memory layer for Hermes / Claude Code / Codex that records session observations, compresses them with AI, and injects relevant context back into future sessions. Claims 95% fewer tokens per session and 200x more tool calls before hitting context limits, benchmarked on 240 real coding sessions. MIT-licensed, ~1,000 GitHub stars in its first week. Worth evaluating as a CLAUDE.md alternative for long-running agent work.

- [Om Patel](https://x.com/om_patel5/status/2050441119003971683) — 2026-05-02: Promoted Claude Code skill /graphify that pre-builds a graph of your codebase (functions, deps, docs, PDFs, images, audio, video via Whisper) so Claude doesn't waste tokens exploring. Author claims '71.5x more efficient' (engagement-farming framing).

- [Akshay](https://x.com/akshay_pachaar/status/2050201509821063576) — 2026-05-01: Walkthrough of why Claude skills fail silently and how progressive disclosure works: Tier 1 = YAML frontmatter (~100 tokens, always loaded), Tier 2 = SKILL.md body (loads on trigger from description), Tier 3 = bundled scripts (loaded on demand, only stdout enters context). Description quality determines triggering.

- [Akshay](https://x.com/akshay_pachaar/status/2049476617144287719) — 2026-04-30: Akshay rebuilt 'OpenClaw' core in a single Sim Studio workflow (25 blocks, 29 connections, short+long-term memory, Telegram+Slack channels) without manual coding — pitched as an 'OS for your AI workforce.' Stack is open-source and self-hostable: github.com/simstudioai/sim

- [Yasir Ai](https://x.com/aiwithyasir/status/2047589529650176333) — 2026-04-28: Hyped pitch ('Breaking', 'terrifying how good') for GitNexus — a knowledge-graph engine for codebases using Tree-sitter AST parsing. Maps every function call, import, class inheritance, interface; clusters code by cohesion; runs blast-radius analysis before changes; coordinates rename across files. MCP-compatible with Claude Code, Cursor, Windsurf. Engagement framing but the underlying capability is interesting.

- [Akshay](https://x.com/akshay_pachaar/status/2047220248081015110) — 2026-04-23: Akshay extends Karpathy's wiki idea: a markdown wiki works for static knowledge but breaks for multi-entity questions like 'which authors moved from Google to Anthropic between 2022-2024 and what did they publish after?' A wiki can only answer that if someone already wrote the article; a graph (entities + relations + dates) lets you ask any variation directly. Argues the next step beyond LLM-maintained wikis is LLM-maintained knowledge graphs.

- [Shiv](https://x.com/shivsakhuja/status/2047124337191444844) — 2026-04-23: Shiv on 'Skill Graphs 2.0' — composing skills into a graph (markdown + scripts) where skills depend on other skills (e.g., draft-marketing-email depends on graphic-design). The original skill-graph idea got traction; the v2 wrinkle is that agents stop reliably calling skills past a certain graph depth. Worth tracking alongside Pocock's /teach skill, Akshay's Claude Code 12 features, and the general skills-as-reusable-routines concept.

- [Shrey Pandya](https://x.com/shreypandya/status/2047100550446280792) — 2026-04-23: Shrey Pandya introduces the /autobrowse skill (inspired by Karpathy's autoresearch harness). Pattern: agent explores a web task via the @browserbase CLI, learns from previous attempts' failures, iterates until it converges on a reliable workflow. Once token usage is optimized, the winning approach 'graduates' into a reusable skill. Direct reference for the let-it-cook / routines-as-higher-order-prompts concept.

- [ClaudeDevs](https://x.com/claudedevs/status/2047086372666921217) — 2026-04-23: Anthropic ClaudeDevs blog post: 'Building agents that reach production systems with MCP' (claude.com/blog/building-agents-that-reach-production-systems-with-mcp). Covers when agents should use direct APIs vs CLIs vs MCP, patterns for building MCP servers, context-efficient client design, and pairing MCP with skills. Direct first-party reading for any agent-to-production pipeline work.

- [Vida](https://x.com/vida_agent/status/2047007924279767332) — 2026-04-23: Vida open-sourced OpenChronicle (github.com/Einsia/OpenChronicle) — a local-first memory layer for tool-capable LLMs and agents, framed as a free alternative to OpenAI Chronicle's $100/mo paywall. Fits the agent-memory infrastructure concept thread.

- [Garry Tan](https://x.com/garrytan/status/2046882636069798323) — 2026-04-23: Garry Tan: 'Basically how I'm building all my features these days: Do it once in OpenClaw, then just run /skillify and it does it like that forever.' Quote-tweets his own article on stopping agents making the same mistakes (contrasts with LangChain's $160M/3yr/LangSmith trajectory-evals stack). Fits the skills-as-routines thread.

- [Avi Chawla](https://x.com/_avichawla/status/2046685172666712571) — 2026-04-23: Avi Chawla reports 3x token reduction on Claude Code (10.4M → 3.7M tokens, 10 errors → 0, $9.21 → $2.81) by using Insforge Skills + CLI (github.com/InsForge/InsForge) as a backend context-engineering layer — without changing CLAUDE.md, prompts, or models. Open-source and local. Worth measuring against on a real session.

- [Shubham Saboo](https://x.com/saboo_shubham_/status/2046473615118672325) — 2026-04-21: Shares agentic-stack — 'One brain, many harnesses. Portable .agent/ folder (memory + skills)' — a pattern for sharing a single memory/skill store across multiple agent harnesses. Repo: github.com/codejunkie99/agentic-stack.

- [Sigrid Jin](https://x.com/realsigridjin/status/2046266374948069387) — 2026-04-21: Quote-tweet of Junghwan Na's writeup — Na got his GitHub banned after pushing 500+ commits across 100+ open-source repos in 72 hours using an AI harness. Sigrid pulls out the two highest-leverage principles from Na's method: (1) reproduce the bug locally or drop it, (2) read merge history instead of CONTRIBUTING.md. Jeremy flagged 'worth extracting a skill' — these are skill-worthy contribution-harness patterns.

- [Daniel Miessler](https://x.com/danielmiessler/status/2045148852047827449) — 2026-04-18: Daniel Miessler recommends Interceptor (by Ronald Eddings) as the best browser-control system for AI agents he's used out of 100+, now the highest-value addition to his PAI harness.

- [Alter Ego](https://x.com/alterego_eth/status/2045093809886020058) — 2026-04-17: Alter Ego promotes Nous Research's Hermes Agent, a self-hosted agent that writes its own skills after each task, keeps persistent memory (MEMORY.md/USER.md/SQLite), and runs 24/7 on a VPS with a closed learn-improve loop every ~15 tool calls, using it to build a self-learning Polymarket weather-trading bot. Heavy promotional/profit framing.

- [Garry Tan](https://x.com/garrytan/status/2044479509874020852) — 2026-04-15: X article: "Resolvers: The Routing Table for Intelligence" — argues resolvers (context-routing rules: when task X appears, load document Y first) are the most important but invisible component of agent systems. Follows up on "Thin Harness, Fat Skills" framework. 21K views.

- [Shann³](https://x.com/shannholmberg/status/2044413638388363272) — 2026-04-15: Built a 230-page Obsidian knowledge base (tweets, bookmarks, articles, notes) and connected it to every AI agent project using qmd (Tobi Lütke's tool) with hybrid BM25+vector search and LLM re-ranking. Any agent in any project now searches this global wiki before brainstorming or planning.

- [Akshay](https://x.com/akshay_pachaar/status/2044329897603244093) — 2026-04-15: Akshay argues agent memory is three-dimensional, needing a relational store for provenance, a vector store for semantics, and a graph store for relationships, because flat vector search misses multi-hop connections (the "bridge" fact that links two entities). He points to Cognee, an open-source project that unifies all three behind four async calls (default embedded SQLite+LanceDB+Kuzu, swappable for Postgres/Qdrant/Neo4j).

- [Garry Tan](https://x.com/garrytan/status/2044291663213015491) — 2026-04-15: Garry Tan releases GBrain v0.10.0, packaging his personal OpenClaw "brain" for others: refined RESOLVER.md and SOUL.md, ACLs for multi-user brain access, and 24 distinct "fat" skills shipped with e2e tests, evals, and unit tests.

- [Ihtesham Ali](https://x.com/ihtesham2005/status/2044056849272705246) — 2026-04-15: Aurogen is an open-source (MIT) OpenClaw fork whose differentiator is true multi-agent, multi-instance orchestration inside one deployment: modular agents/channels/providers/skills, a pure web-panel setup with no config files or CLI, ClaWHub skill imports, one-click installers, and it runs on a $50 Linux SBC (github.com/UniRound-Tec/Aurogen).

- [Indie Fox](https://x.com/indie_maker_fox/status/2043857352282255829) — 2026-04-15: Indie Fox praises a Claude skill that generates very high-quality software architecture diagrams (github.com/Cocoon-AI/architecture-diagram-generator), showing an OpenHarness architecture diagram as an example of its clean output.

- [Philipp Schmid](https://x.com/_philschmid/status/2043705197030002904) — 2026-04-14: Links a practical guide '8 Tips for Writing Agent Skills' — covering what kinds of skills exist, how to write them well, and when to retire one. Directly relevant to the skills/plugins workflow.

- [Charly Wargnier](https://x.com/datachaz/status/2043246635996807300) — 2026-04-13: Charly Wargnier covers Addy Osmani's (Google) new Agent Skills package: 19 engineering skills + 7 commands for AI coding agents, based on Google best practices. Covers the full dev lifecycle — define (specs), plan (decompose), build (incremental), verify (TDD), review (security), ship (CI/CD). Aims to prevent agents from skipping quality gates.

- [Garry Tan](https://x.com/garrytan/status/2043198780800197025) — 2026-04-12: 'If your memory dies when your harness dies, you built the harness too thick.' Argues for thin harnesses: memory is markdown, skills are markdown, the 'brain' is a git repo, and the harness is a thin conductor that reads files it doesn't own. Endorses Harrison Chase's 'Your harness, your memory' article on harness/memory coupling and the risk of closed harnesses.

- [Garry Tan](https://x.com/garrytan/status/2042919242283258072) — 2026-04-12: Garry Tan announces GBrain's new guided integration recipes for OpenClaw and Hermes Agent setup. Addresses the struggle new users face getting integrations (mail, calendar, etc.) configured, which is needed to scale to thousands of markdown files in the knowledge base. 36.5K views.

- [Vaishnavi](https://x.com/_vmlops/status/2042486942802321552) — 2026-04-10: Google open-sourced MCP Toolbox (github.com/googleapis/mcp-toolbox) — an MCP server that gives AI agents direct access to 20+ enterprise databases (Postgres, MySQL, MongoDB, BigQuery, Redis, Elasticsearch, Spanner, Snowflake) in plain English. Built-in connection pooling, auth, and OpenTelemetry. Works with LangChain, LlamaIndex, Genkit, and any MCP-compatible client. Less than 10 lines of code to integrate.

- [Avid](https://x.com/av1dlive/status/2042172428127002906) — 2026-04-10: Recommends a 16-minute talk by two Anthropic engineers who built Claude Skills, paired with a comprehensive guide by @eng_khairallah1 on building Claude Skills that actually work. Notes that most of the 80,000+ skills in the community registry are poorly built — this guide covers what separates the good from the bad.

- [Vaishnavi](https://x.com/_vmlops/status/2041869776927261024) — 2026-04-09: Microsoft open-sourced markitdown (github.com/microsoft/markitdown) — a Python tool that converts PDFs, Word docs, Excel, PowerPoint, audio, and YouTube URLs into clean Markdown for LLM pipelines. One pip install replaces custom parsers for file ingestion.

- [0xMarioNawfal](https://x.com/roundtablespace/status/2040500903296352663) — 2026-04-06: Comprehensive open-source Claude Code setup with 27 agents, 64 skills, 33 commands, and built-in AgentShield with 1,282 security tests. Handles planning, code review, fixes, TDD, and token optimization. Works across Cursor, OpenCode, and Codex CLI. github.com/affaan-m/everything-claude-code

- [Arnav Gupta](https://x.com/championswimmer/status/2039109862919905719) — 2026-04-01: Arnav Gupta highlights a set of extensions by @nicopreme (pi-subagents, pi-messenger, pi-mcp-adapter, pi-web-access) that together create a powerful agentic system surpassing tools like Ralph, Gstack, and Conductor.

- [ℏεsam](https://x.com/hesamation/status/2038758029940654507) — 2026-03-31: Ole Lehmann built a Claude skill implementing Karpathy's LLM Council method — 5 AI sub-agents critique your idea from different angles with anonymous peer review. A practical fix for the 'AI yes-man' problem where Claude just tells you what you want to hear.

- [Shann³](https://x.com/shannholmberg/status/2036461256006357409) — 2026-03-29: Karpathy's AutoResearch method applied to Claude skills optimization. Ole Lehmann tested it on landing page copy, improving pass rate from 56% to 92% overnight. The method auto-improves any skill on autopilot by running automated evaluations and iterating.

- [Greg Pstrucha](https://x.com/grichadev/status/2036472210152718504) — 2026-03-25: Greg Pstrucha demonstrates how malicious Claude Code skills can hide instructions inside PNGs and abuse Claude Code's 'expand output' feature to fool both humans and agents — a real security threat. He improved `skill-scanner` (also available via Sentry's Warden at warden.sentry.dev) to catch these attack vectors. Only install skills from trusted sources.

- [Millie Marconi](https://x.com/milliemarconnni/status/2036363493478375797) — 2026-03-25: A Claude Code skill (/last30days) scans Reddit and X from the past 30 days on any topic and generates copy-paste-ready prompts based on what's actually working in the community right now — not months-old advice. Works for any domain (Midjourney, Cursor rules, legal prompts, etc.). Open source, MIT license.

- [hoeem](https://x.com/hooeem/status/2035762966952382646) — 2026-03-22: hoeem re-promotes his 'I want to become a Claude Architect (full course)' article covering Claude Code, the Claude Agent SDK, the Claude API, and MCP; framed for engagement ('Be the 1%', 110k+ bookmarks).

- [Akshay](https://x.com/akshay_pachaar/status/2035341800739877091) — 2026-03-22: Akshay Pachaar's guide 'Anatomy of the .claude/ folder' walks through CLAUDE.md, custom commands, skills, agents, and permissions and how to set them up properly, framing .claude as the control center for how Claude behaves in a project (instructions, commands, permission rules, and cross-session memory).

- [George from prodmgmt](https://x.com/nurijanian/status/2035257434365976671) — 2026-03-22: George (prodmgmt.world) recounts improving his AI skills with Karpathy's Auto Research library (auto-improves prompts via repeated experimentation), using Ole Lehmann's fork turned into a skill that tunes other skills: define test inputs, write judges that score outputs, let the optimization loop run, and wake up to a better skill.

- [Corey Ganim](https://x.com/coreyganim/status/2034717504505823728) — 2026-03-20: Corey Ganim's playbook for running a one-person 'AI company' stacks three free tools: Paperclip (npx paperclipai — assigns work and tracks progress), gstack (15 specialist Claude Code skills from Garry Tan, with /office-hours, /review, /qa, /ship commands), and autoresearch (Karpathy — 100 overnight experiments); the move is running 10-15 gstack commands in parallel. Quotes Nick Spisak's Paperclip follow-up article.

- [Ole Lehmann](https://x.com/itsolelehmann/status/2033982679423848802) — 2026-03-18: Ole Lehmann shares a single skill that auto-improves any other skill using Karpathy's autoresearch method: it runs the skill and scores the output, finds what's failing, makes one small change to the skill prompt, re-runs to check the score, keeps or reverts the change, and repeats until the skill works. Article: 'How to 10x your Claude Skills'.

- [unusual_whales](https://x.com/unusual_whales/status/2033965177918620008) — 2026-03-18: Unusual Whales launched an MCP server that streams live, structured market data to any AI on demand — options flow, dark pools, congressional trades, full financials, technicals, 13Fs, insider activity, and Polymarket data — for building trading bots, dashboards, and screeners (unusualwhales.com/public-api/mcp). 'BREAKING' engagement framing.

- [Thariq](https://x.com/trq212/status/2033949937936085378) — 2026-03-18: Thariq (Anthropic) shares 'Lessons from Building Claude Code: How We Use Skills' — which skills are worth making, the secret to writing a good one, and when to share them — noting Anthropic runs hundreds of skills internally and that the common 'skills are just markdown files' misconception undersells them.

- [Akhilesh Mishra](https://x.com/livingdevops/status/2033845127244825041) — 2026-03-17: Akhilesh Mishra reports NVIDIA open-sourced OpenShell at GTC — an infrastructure-layer sandbox/guardrail for coding agents: filesystem locked at sandbox creation, network blocked by default with whitelisting, API keys injected only at runtime (never on disk), policies in simple YAML, running a full K3s cluster inside a single Docker container. One command sandboxes Claude Code, Codex, or Cursor; Adobe, Atlassian, Cisco, CrowdStrike, and Salesforce are integrating it.

- [Avi Chawla](https://x.com/_avichawla/status/2033797863948632384) — 2026-03-17: Avi Chawla explains the SKILLRL paper: rather than stuffing long, noisy raw trajectories into agent memory, it distills experiences into compact, reusable skills the agent retrieves and applies to future tasks — analogous to how humans turn driving experience into transferable instincts.

- [0xMarioNawfal](https://x.com/roundtablespace/status/2033238044900298844) — 2026-03-16: 0xMarioNawfal amplifies Corey Ganim's article 'Ultimate Claude Cowork Starter Pack: Every Plugin, Skill, and Workflow You Need,' which argues most people install Claude Cowork, poke around for 10 minutes, and revert to ChatGPT because the setup is the hard part.

- [Garry Tan](https://x.com/garrytan/status/2032196172430131498) — 2026-03-13: Garry Tan shares a CTO's testimonial that his open-source gstack ('god mode') flagged a subtle cross-site-scripting vulnerability the team wasn't aware of, predicting 90%+ of new repos will adopt it. gstack is MIT-licensed at github.com/garrytan/gstack and installs into local Claude Code and into a repo for teammates with two pastes.

- [elvis](https://x.com/omarsar0/status/2031727864199208972) — 2026-03-12: elvis highlights EvoSkill, a self-evolving multi-agent framework that automatically discovers and refines agent skills through iterative failure analysis. Three agents (Executor, Proposer, Skill-Builder) drive the loop, with a Pareto frontier retaining only skills that improve held-out validation while the base model stays frozen. Reported gains: Claude Code w/ Opus 4.5 from 60.6%->67.9% on OfficeQA, +12.1% on SealQA, and +5.3% zero-shot transfer to BrowseComp.

- [Alex Prompter](https://x.com/godofprompt/status/2030434641019072867) — 2026-03-08: Alex Prompter (co-founder @godofprompt) shares affaan-m/ECC on GitHub, described as an agent-harness performance-optimization system built around skills and instincts.

- [Philipp Schmid](https://x.com/_philschmid/status/2029570052530360719) — 2026-03-06: Practical guide to evaluating agent Skills, which are often AI-generated and untested: define success criteria (outcome/style/efficiency), build 10-12 prompts with deterministic checks, add an LLM-as-judge for qualitative checks, and iterate on the skill from eval failures.

- [Akshay](https://x.com/akshay_pachaar/status/2029534926828388537) — 2026-03-05: Explains the difference between MCP and Skills for AI agents — commonly conflated. MCP is a shared communication standard that replaces the N-models-by-M-tools custom-connector explosion, whereas Skills are a distinct concept.

- [Meta Alchemist](https://x.com/meta_alchemist/status/2029430826128293906) — 2026-03-05: Roundup of 10 open-source AI memory layers (free, popular on GitHub, some YC-funded) to give coding agents like Claude and Codex better recall than plain memory.md files, with notes on what each is good at and how to combine them. Engagement-styled listicle but substantive.

- [Sukh Sroay](https://x.com/sukh_saroy/status/2029400474739458379) — 2026-03-05: [Post unavailable — account suspended]

- [Daniel San](https://x.com/dani_avila7/status/2029399100240674929) — 2026-03-05: Points to a full Skill in the Anthropic repo as a reference for SKILL.md structure and language support, arguing every company should maintain an internal repository of reusable Skills and components.

- [Dickson Tsai](https://x.com/dickson_tsai/status/2029235808235078095) — 2026-03-05: Dickson Tsai (Anthropic) announced HTTP hooks in Claude Code — a more secure, easier alternative to command hooks: CC POSTs each hook event to a URL you choose and awaits a response, so you can build a web app to view progress, manage permissions, run hook logic server-side, and manage state across agents via a DB. Works everywhere hooks are supported, including plugins, custom agents, and enterprise managed settings. Docs: code.claude.com/docs/en/hooks

- [witcheer ☯︎](https://x.com/witcheer/status/2029013946701381978) — 2026-03-05: [Post unavailable — page doesn’t exist (same status as nummanali)]

- [klöss](https://x.com/kloss_xyz/status/2028237936848994369) — 2026-03-02: Flags Anthropic's free AI academy — 13 courses with official certificates covering MCP, APIs, Claude Code, and AI fluency, at anthropic.skilljar.com. Hype framing ('stop what you're doing') but a genuinely useful free resource.

- [Nyk](https://x.com/nyk_builderz/status/2028022503319203926) — 2026-03-02: Announces open-sourcing Mission Control, a self-hosted AI agent orchestration dashboard: 26 panels, real-time WebSocket+SSE, SQLite (no external services), kanban board, cost tracking, role-based access, quality gates, multi-gateway support. Repo: github.com/builderz-labs/mission-control.

- [Joseph Thacker](https://x.com/rez0__/status/2027448137133264955) — 2026-03-01: Argues bug bounty / security research changed step-function fast in late 2025: coding agents went from not working to genuinely working. Example: pointed Claude Code at a target's scope (enumerate subdomains, analyze JS bundles, fuzz, test IDORs/GraphQL, write an HTML report); it ran ~30 min, self-recovered from auth/WAF errors, and returned two confirmed vulns. Hunters now build and share custom Claude Code skill libraries (JS static analysis, authenticated fuzzing, IDOR, GraphQL introspection). Quote-tweets Karpathy's parallel observation about programming.

- [Thariq](https://x.com/trq212/status/2027463795355095314) — 2026-02-28: Anthropic's Thariq on building Claude Code: designing an agent's action space is an art. Walks through the AskUserQuestion tool's evolution (ExitPlanTool param → output-format parsing → dedicated tool), the shift from TodoWrite to the Task tool as models improved, replacing RAG with a Grep search tool so Claude builds its own context, progressive disclosure via Skills, and the Claude Code Guide subagent. Lesson: revisit tool assumptions as capabilities grow; experiment, read outputs, 'see like an agent.'

- [Avi Chawla](https://x.com/_avichawla/status/2026907616337883612) — 2026-02-27: Avi Chawla revives Norm Hardy's 1988 'confused deputy problem' as the defining security issue for autonomous agents that hold real credentials but can't judge intent. He points to Teleport's open-source Agentic Identity Framework, which gives each agent a unique cryptographic identity, evaluates access in real time, auto-discovers shadow agents and unmanaged MCP servers, and keeps full audit trails.

- [Machina](https://x.com/exm7777/status/2026666140987175221) — 2026-02-27: Engagement-farming post ('the ONLY skill you will ever need for Claude, Codex or Openclaw', 'this skill will change your life') quote-tweeting the author's own X article. Behind the hype the underlying topic is a meta-skill/prompting framework meant to change how AI reasons for you; content quality behind the clickbait is unverified.

- [Aakash Gupta](https://x.com/aakashgupta/status/2026367615602667784) — 2026-02-25: Aakash Gupta, building on a Karpathy quote, argues agents are the new distribution channel for software: they call CLIs and MCP servers and read docs programmatically rather than browsing marketing sites. MCP hit 97M monthly SDK downloads and 10k+ servers in a year and was donated to the Linux Foundation. Winners of the next 24 months build agent-accessible surface area (CLIs, MCP endpoints, machine-readable docs) now.

- [Akshay 🚀](https://x.com/akshay_pachaar/status/2025767534159835443) — 2026-02-21: [Post unavailable - page doesn't exist]

- [tuna](https://x.com/tunahorse21/status/2024974148259512677) — 2026-02-21: tuna signal-boosts Alex Fazio introducing Plankton, a 'slop guard' for LLM coding agents. It aims to break the loop of copy-pasting pre-commit/linting errors back into the agent by enforcing lint rules the model can't cheat around.

- [J.B.](https://x.com/vibemarketer_/status/2019435524532904205) — 2026-02-19: J.B. (VibeMarketer) describes a 'recursive self-improvement loop' skill for Claude: instead of prompting once and shipping, the skill generates output, scores it against explicit criteria, diagnoses weaknesses, rewrites, and re-scores until it clears the bar. Cites @maxwellfinn's image-ad skill that grades concepts on 10 criteria (thumb-stop power, curiosity gap, emotional trigger, persona recognition) and won't stop below 9/10.

- [Matt Dancho (Business Science)](https://x.com/mdancho84/status/2023738764841894352) — 2026-02-18: Matt Dancho argues that becoming a '10X engineer' now comes down to a well-crafted SKILLS.md file, teasing a thread/resource on how to build one. High-engagement post (~1.1M views) with a lead-gen hook.

- [Pavol Lupták](https://x.com/wilderko/status/2025159534159835443) — 2026-02-15: [Post unavailable - page doesn't exist]

- [kitze](https://x.com/thekitze/status/2021494167113990464) — 2026-02-12: kitze boosts Maximiliano Firtman's note that Chrome 146 ships an early flagged preview of WebMCP, which lets AI agents query and execute a web app's services without driving the UI like a human. Services are declared imperatively via a navigator.modelContext API or declaratively through a form; kitze calls exposing them 'the new responsive design.'

- [Matt Simpson](https://x.com/msmps_/status/2013376201977463038) — 2026-01-20: Matt Simpson shipped 'opentui-skill', a skill that gives coding agents TUI (terminal UI) superpowers via decision trees, progressive disclosure, and documented gotchas. Inspired by Dillon Mulroy's cloudflare-skill. Install instructions in a follow-up reply.

- [Ian Nuttall](https://x.com/iannuttall/status/2012833663319195970) — 2026-01-19: Ian Nuttall shares 'dotagents' (github.com/iannuttall/dotagents), a tool he built to stop the pain of switching between different agent harnesses/clients - he now runs everything from ~/.agents or .agents. Posted in reply to Theo asking for a way to sync agent skills/config across repos via symlink. PRs welcome for unsupported clients.

- [giyu_codes](https://x.com/giyu_codes/status/2012420750855012428) — 2026-01-16: giyu_codes recommends cogsec (@affaan)'s article 'The Shorthand Guide to Everything Claude Code' - a complete setup after 10 months of daily use covering skills, hooks, subagents, MCPs, plugins, and what actually works. High-reach post (~806K views).

- [Jarrod Watts](https://x.com/jarrodwatts/status/2009200810870428123) — 2026-01-08: Jarrod Watts open-sourced his 'claude-code-config' repo containing all the agents, commands, hooks, rules, skills, and plugins he's made or collected over the past few months — described as simple but effective enhancements he'll keep updating. A ready-made reference config for a team standardizing Claude Code setups.

- [AGENTS.md](https://agents.md/) — 2025-12-28: AGENTS.md (agents.md) is a simple, open format for guiding coding agents, now used by over 60k open-source projects. Think of it as a README for agents: a dedicated, predictable place for the build steps, tests, and conventions that coding agents need but that would clutter a human README — kept intentionally separate so agents have one clear location to look.

- [Tech with Mak](https://x.com/technmak/status/2002713140757496299) — 2025-12-22: A structured LangGraph learning path (pitched as filling the gap since LangGraph appears in ~half of AI job descriptions). Progresses from basic agent concepts (Pydantic data validation, agentic chatbots, multi-agent coordination) through production systems (a 2.5-hour LangGraph+MCP crash course, debugging/monitoring, deployment architecture) to RAG pipelines (multimodal RAG, hallucination fixes, end-to-end retrieval, Typesense search).

- [Claire Silver](https://x.com/clairesilver12/status/2002443560898208162) — 2025-12-21: Claire Silver highlights Unreal MCP, a free MCP server that lets you prompt Claude to build things in Unreal Engine — e.g. 'make a Victorian manor, here's a reference pic, use the assets in this folder' and it just does it. She promised a demo video and calls it '10/10 magic.'

- [Tom Dörr](https://x.com/tom_doerr/status/1996997820868366397) — 2025-12-08: Tom Dörr shares 'awesome-claude-skills' (github.com/VoltAgent/awesome-claude-skills), a curated collection of official and community-built Claude skills.

- [Ray Fernando](https://x.com/rayfernando1337/status/1992848315541823490) — 2025-11-25: Ray Fernando recommends Lee Han-Chung's 'Claude Skills deep dive' blog post (leehanchung.github.io) as the best breakdown of Claude Skills he's seen.

- [Thariq](https://x.com/trq212/status/1989061939625144388) — 2025-11-15: Thariq gives the setup commands for Anthropic's frontend-design plugin in Claude Code: add the marketplace with '/plugin marketplace add anthropics/claude-code', then '/plugin install frontend-design@claude-code-plugins'. Getting-started reply for the frontend-design plugin.

- [Pontus Abrahamsson](https://x.com/pontusab/status/1981700333857636550) — 2025-10-24: Pontus Abrahamsson points to midday-ai/ai-sdk-tools (github.com/midday-ai/ai-sdk-tools) — a set of example AI SDK tools/integrations for building agent tooling.

- [Ruslan Beskorovainiy](https://x.com/chemobyazan/status/1975326044271079509) — 2025-10-07: Points to the contains-studio/agents GitHub repo, a shared collection of AI agents currently in use.

- [Asterisk (getAsterisk)](https://github.com/getAsterisk/claudia) — 2025-08-18: opcode (formerly Claudia, by Asterisk) is an open-source Tauri 2 desktop GUI and toolkit for Claude Code: visual project/session management, custom CC agents with per-agent file/network permissions and background execution, a usage/cost analytics dashboard, MCP server management (with Claude Desktop import), session timeline/checkpoints with diff and fork, and a built-in CLAUDE.md editor. Note: the repo has been renamed from getAsterisk/claudia to winfunc/opcode.

- [Philip Vollet](https://x.com/philipvollet/status/1955945448860008655) — 2025-08-15: Announces Elysia, an open-source agentic RAG platform (successor to Verba) built on Weaviate and DSPy. Highlights: transparent decision-tree agents with self-healing and custom tools/branches, pre-query data analysis to avoid blind vector/text search, dynamic result displays, feedback-driven few-shot personalization so smaller models perform like larger ones, and query-time chunk-on-demand. Delivered as a FastAPI+NextJS app and a pip package (elysia-ai).

- [Nick Dobos](https://x.com/nickadobos/status/1930878279290060975) — 2025-06-07: Riffs on a repo (Shubham Saboo's) that stores millions of text chunks inside MP4 video files for fast semantic search, pitched as an open-source replacement for expensive vector databases; Nick Dobos speculates video may be an optimal encoding for AI memory, echoing how human memory leans on vision.

- [Mervin Praison](https://x.com/mervinpraison/status/1881788246684013011) — 2025-01-22: Shows a 100% local RAG AI agent with reasoning: DeepSeek via Ollama for the LLM, PraisonAI to build the agent in a few lines, Nomic embeddings, and a Streamlit UI—code included in the thread.

### Prompting (105)

- [JoePro](https://x.com/joepro/status/2076877282312954311) — 2026-07-14: JoePro shares a reworked 'Frontend Design Skill' (an agent/Claude skill spec) engineered to produce distinctive, production-grade UIs that avoid recognizable AI-generated tropes — covering success criteria (signature visual identity, complete states, WCAG AA accessibility, token-driven design systems) and a context-gathering routine before writing code.

- [Alex Prompter](https://x.com/alex_prompter/status/2074198124898181121) — 2026-07-14: Alex Prompter's thread pitches 'cloning' Fable 5's reasoning into Opus 4.8 before Fable 5 shifts to pay-per-use credits — extracting a model's 'operating manual' as a portable prompt and transplanting it onto a cheaper model to keep the way it thinks rather than the model itself. Engagement-framed but a real prompt-portability technique.

- [kaize](https://x.com/0x_kaize/status/2073743517155774641) — 2026-07-06: kaize shares a 'Loop engineering' reading list, arguing 2026 agents are less about smarter prompts and more about longer runs — the real questions are whether an agent can recover from a failed step, control spend, and know when to stop. Curated links: Addy Osmani (addyosmani.com/blog/loop-engineering), Firecrawl (firecrawl.dev/blog/loop-engineering), Oracle 'What is the AI agent loop', OpenAI 'Harness engineering', and Martin Fowler 'Harness engineering for coding agent users'.

- [0xSero](https://x.com/0xsero/status/2073651251594854573) — 2026-07-06: 0xSero (quote-tweeting Rohan Paul on a Meta paper showing quantized reasoning models often fail because compression makes them doubt a correct answer instead of finishing) reports experimenting with penalizing 'self-doubt' words during generation — claiming ~30% fewer output tokens — plus improving tok/s via CPU offloading.

- [Anatoli Kopadze](https://x.com/anatolikopadze/status/2068328135611822149) — 2026-07-06: Anatoli Kopadze's widely-viewed piece 'Loops explained: Claude, GPT, Mira and what actually works' argues most people use AI the slow way (type, wait, fix, repeat by hand) and that the faster approach top AI engineers care about is building loops. Covers what loops are, how they work under the hood, when they're worth it vs a trap, and how to build a basic one in Claude or ChatGPT. Quote-tweets Peter Steinberger: you shouldn't be prompting coding agents, you should be designing loops that prompt your agents. (Includes some self-promotion for his X/Telegram.)

- [Anatoli Kopadze](https://x.com/anatolikopadze/status/2073396351279276397) — 2026-07-05: Anatoli Kopadze (quote-tweeting his own Claude features guide) shares an Anthropic engineer's claim that most people use Sonnet 5 and Fable 5 wrong and can set them up right in one afternoon to stop overpaying — a 31-minute session on testing each model against your real use case, plus a guide to Claude features '99% of users never find.'

- [Avid](https://x.com/av1dlive/status/2073114542851416260) — 2026-07-05: Avid (ALL CAPS engagement framing) makes a practical context-engineering point: give an agent one index file per major folder for a direct line to what it needs. The same task dropped from 2 minutes (7 files opened, wandering, a 3-month-old brief still missing) to 10 seconds with the same model, nothing else changed. 'Build the path or watch it search in the dark.' Quote-tweets Machina's article 'How to build a second brain with Fable 5.'

- [Sprytix](https://x.com/sprytixl/status/2073101741604679714) — 2026-07-05: Sprytix (clickbait 'Anthropic just leaked an internal engineering document' framing) lays out a six-layer self-improving agent loop: Generate -> Evaluate -> Remember -> Schedule -> Optimize -> Recurse. Generation produces its own solutions (no human brief), Evaluation is a second layer that can say no, Memory retains useful discoveries each cycle, Scheduling decides what happens next, Optimization updates behavior based on what worked, and Recursion means removing any single layer drops performance significantly — shifting the human from operator to designer.

- [darkzodchi](https://x.com/zodchiii/status/2072973531768328626) — 2026-07-05: darkzodchi's 'Claude Fable 5 Setup Guide' covers which heavy tasks actually deserve Fable 5, the new safeguards that reroute you to Opus, and how to plan the free window (up to 50% of weekly limit free until July 7). Recaps a reported Fable 5 timeline: launched June 9, pulled June 12 under a US export-control order tied to a jailbreak report, back online July 1. (Includes Telegram self-promo.)

- [Thariq](https://x.com/trq212/status/2073101078145724589) — 2026-07-04: Thariq shares his article 'A Field Guide to Fable: Finding Your Unknowns' — the most important part of working with Claude Fable 5 is discovering your own unknowns so you can prompt it better. Framing: 'the map is not the territory' — your prompts, skills, and context are the map (a representation of the work to be done), and the practice is surfacing what you don't yet know about the actual work.

- [Daniel Miessler](https://x.com/danielmiessler/status/2073076322390384798) — 2026-07-04: Daniel Miessler shares a set of 'prompts to run now that you have Fable back' — a quick collection of prompts to try with Claude Fable 5 following its return.

- [Akshay](https://x.com/akshay_pachaar/status/2072961737008336937) — 2026-07-04: Akshay Pachaar summarizes a Hugging Face blog post on 'evolving the harness' instead of training the model: they took a frozen open model scoring 0% on a hard legal-agent benchmark, left its weights untouched, and let an automated loop rewrite only the surrounding harness code (the runtime wrapper that feeds context, runs tool calls, and decides when a run ends). It ended up essentially matching Sonnet 4.6 on the headline metric at ~7x lower cost per task, zero weights changed. The insight: the 0% wasn't measuring legal reasoning — the model reasoned correctly but saved outputs under the wrong filename/folder or not at all — so it was measuring the harness.

- [Rahul](https://x.com/sairahul1/status/2072749611471835229) — 2026-07-04: Rahul shares a free 'Loop Library' (signals.forwardfuture.com/loop-library/) of reusable agent loops, plus his article '20 Loop Design Patterns Every AI Engineer Should Know.' Framing: most engineers can build an agent (a worker) but few can build a system that gets better after the first attempt — and that gap is 'worth six figures.'

- [zostaff](https://x.com/zostaff/status/2070852153594290195) — 2026-06-27: Long-form "Loop Engineering" article: four autonomous loops that actually pay off because the task repeats, a machine can reject the result, the agent carries it whole, and "done" is objective. Covers the bare while-loop/exit-code/budget mechanics under Claude Code Routines and four worked configs: morning CI test triage (with maker-checker subagent), dependency watchdog, doc synchronizer, and overnight research digest. Theme: the harder the verification, the more you can hand the loop; soft verification keeps a human in the loop.

- [Movez](https://x.com/0xmovez/status/2068763235587694769) — 2026-06-23: Movez highlights an Andrew Ng talk on building self-improving agentic systems from scratch, quoting Ng that AI agents now handle 100% of his tasks and that self-improving loops will replace prompting within 3-6 months. Quote-tweets his own article on a 300-agent swarm running on Kimi K2.6 verified by Opus 4.8. Heavy promotional framing.

- [Codez](https://x.com/0xcodez/status/2064374643729773029) — 2026-06-23: A long-form Loop engineering roadmap arguing the leverage point in agentic coding has moved from writing prompts to designing self-running loops. Covers the 4-condition test for when a loop is worth building (task repeats, automated verification, token budget, senior-engineer tooling), the five building blocks (automations like /loop and /goal, git worktrees, skills, MCP connectors, sub-agents), the maker/checker split, the Ralph Wiggum quiet-failure mode, comprehension debt and cognitive surrender, and the security tax of unattended loops. Cites Anthropic engineering docs and Addy Osmani.

- [Avi Chawla](https://x.com/_avichawla/status/2065727218991735000) — 2026-06-13: Explains 'loop engineering' (framed with a Karpathy quote about removing yourself as the bottleneck and maximizing leverage): move the operator's two manual jobs — deciding what the agent runs next and checking its output — into the system itself. A schedule decides what to run, a maker loop produces the work, a separate checker agent grades the output, and a file on disk holds the shared state both read; the loop runs until done, max iterations, or budget is exhausted.

- [Codez](https://x.com/0xcodez/status/2065097407965127142) — 2026-06-12: Hype-framed thread claiming an Anthropic 'Managed Agents' team demo showing how to build self-improving agent systems with the Fable 5 model from scratch in ~13 minutes, using /loops, dynamic workflows, and 'dreaming.' Quote-tweets the author's own 14-step article on the same. (Strong engagement-farming framing; claims unverified.)

- [hoeem](https://x.com/hooeem/status/2065098599751471454) — 2026-06-11: Quote-tweets his own long-form X article 'Why you should not be looping & what to do instead' — a contrarian breakdown pushing back on the popular agentic self-looping pattern (taking aim at a 'leading voice in AI') and proposing alternatives. The substance is in the linked article; framing is deliberately provocative.

- [Meta Alchemist](https://x.com/meta_alchemist/status/2064431279383433646) — 2026-06-11: Shares a copy-paste 'Repo Audit & Improvement Plan' prompt — a structured, 4-phase principal-engineer audit (Phase 1 discovery/mapping before judging, then a prioritized, actionable improvement plan), with instructions to cite file paths and line numbers and to flag anything unverifiable. Useful prompt template, but wrapped in hype framing around a nonexistent 'Claude Fable 5' model.

- [Paweł Huryn](https://x.com/pawelhuryn/status/2064201950980096078) — 2026-06-09: Lists six patterns for Anthropic-style dynamic agent workflows/loops: classify-and-act (one agent decides type, code routes), fan-out-and-synthesize (per-piece agents merged in code), adversarial verification (separate rubric-checker), generate-and-filter (many candidates → dedupe → survivors), tournament (judges compare different attempts), and loop-until-done (spawn until a stop condition). Each with a concrete example. Links his 'Claude Dynamic Workflows' guide.

- [hoeem](https://x.com/hooeem/status/2064099329342640285) — 2026-06-09: hoeem hypes Matt Pocock's new /teach skill — pours 10 years of teaching experience into a Claude skill that teaches you anything (Pocock's demo: it taught him to solve a Rubik's cube). Worth a look as a reusable Claude Code skill pattern.

- [BOOTOSHI](https://x.com/kingbootoshi/status/2063999432077795579) — 2026-06-09: Long personal write-up: BOOTOSHI claims the agent-orchestrating-subagents pattern (token-maxxing across parallel work) was right for opus-4.5/gpt-5 but is no longer optimal with the newer generation (gpt-5.5, opus-4.8). Argues the extended context window + intelligence means these models are now more capable as a single 'MEGA THREAD' with a single operator. Counter-trend to the multi-agent enthusiasm of early 2026.

- [rody](https://x.com/0x_rody/status/2063722061126651935) — 2026-06-09: Quotes 'Anthropic's main manager': 'Nobody types prompts from scratch. The commands should be live in the project.' Points to a 26-min talk walking through Anthropic's command library every new dev inherits on day one. Links the author's own article 'How to Build a Claude Code Slash Command Library' with a template inside — argues devs spend ~10 hours/month re-typing context that should be a single saved command.

- [darkzodchi](https://x.com/zodchiii/status/2063559498078278109) — 2026-06-08: Quotes 'Anthropic engineer Margot van Laer': 'Every prompt you type more than twice should be a file. The ones we use internally aren't memorized, they're saved.' Points to a 33-min talk on the prompt patterns Anthropic packages and reuses across every Claude Code session — links the same Claude Code slash-command-library template from rody.

- [Viv](https://x.com/vtrivedy10/status/2063429138304668093) — 2026-06-07: A default recipe for optimizing Agent = Model + Harness, 'training' both: (1) build v1 on a sensible base harness with task-specific prompting/tools, (2) harness-engineer against prod-like eval tasks (often enough on its own), (3) SFT on mined traces or synthetic data (good for distilling a cheaper model), (4) RL if you can design environments/rewards to push past SFT copying, (5) light harness engineering again on the trained model. Argues harness engineering will be the dominant optimization lever and most companies are still at steps 1-2; links the 'Anatomy of an Agent Harness' article.

- [Chesny](https://x.com/chesnyfcb/status/2060818732654481693) — 2026-05-31: Polemical pitch (translated) for a 3D 'knowledge galaxy' second brain à la Karpathy: 378 notes auto-generated ~1,854 nodes and ~3,856 connections, surfacing hidden links and missing connections. Pragmatic takeaway: start with an automated Obsidian + Claude vault that extracts content, finds connections, and writes daily reports.

- [MacCallister Higgins](https://x.com/macjshiggins/status/2060045337679532174) — 2026-05-29: Argues classical NASA systems engineering is the ideal model for LLM-assisted coding — being explicit in docs makes it easier than ever to build, test, and verify complex codebases (planning modes only approximate it).

- [Charly Wargnier](https://x.com/datachaz/status/2059909626532155482) — 2026-05-28: Microsoft open-sourced SkillOpt: optimize agent skills the way you train models — a base model runs tasks while an optimizer rewrites the instructions, keeping only edits that raise the benchmark. Claims SOTA over hand-crafted prompts and TextGrad, with no model lock-in since it learns procedural logic.

- [Parag pawar](https://x.com/dharmikpawar13/status/2059571098484675051) — 2026-05-27: Argues CLAUDE.md is a control layer, not a README: use scope hierarchy (global → project → folder, nearest wins) and a WHAT/WHY/HOW framing, favor specificity ('TypeScript strict mode, Zod validation' over 'production-ready code'), start with /init, keep it under ~500 lines, use hooks, and treat it as living infrastructure.

- [George Nurijanian](https://x.com/nurijanian/status/2058259663238631890) — 2026-05-24: Fixed Claude's 'chart junk' by handing it a book and having it spin up a Tufte-flavored visualization skill — producing leaner, clearer visuals (github.com/gnurio/tufte-vdqi-plugin).

- [Viv](https://x.com/vtrivedy10/status/2057673225702937059) — 2026-05-22: An agent-orchestration heuristic Viv finds works in nearly every case: 'bossman supervisor >> external judge >>> self reflection.' A fresh judge (no prior context) beats self-review, but best is a supervisor orchestrating a series of Claudes — the main agent shouldn't think it's doing the work; it should be critically judging and correcting its workers.

- [Ahmad](https://x.com/theahmadosman/status/2057590791241896254) — 2026-05-22: Points to a free 'LLMs 101: A Practical Guide (2026 Edition)' covering model mechanics (tokens, transformers, attention, KV cache, decoding, RAG, agents, fine-tuning, multimodal) and running models locally (quantization, VRAM math, hardware tiers, runtimes, model selection, failure modes).

- [Mnimiy](https://x.com/mnilax/status/2057551699204857930) — 2026-05-22: Reports that Anthropic engineers kept repeating 'let it cook' at Code with Claude London (Boris Cherny, Ravi Trivedi, Katelyn Lesse): stop micromanaging prompts, write the routine, let Claude prompt itself — 'routines are higher-order prompts; the runtime is shipped; the prompts are the bottleneck.' Links 9 tested Claude Cowork prompt-templates.

- [BOOTOSHI](https://x.com/kingbootoshi/status/2057528772208034195) — 2026-05-22: Shares an S+-tier skill, directional-prompting (outcome-first + directional language, a two-layer approach), combined with /goal mode — 'agents thrive on positive communication; make the path to success clear.'

- [Alex Veremeyenko](https://x.com/alex_prompter/status/2057476020454949201) — 2026-05-22: Anatomy of the perfect SOUL.md identity file for AI agents — the file an agent reads first. Nine sections: Identity, Values, Communication Style, Expertise, Boundaries, Workflow, Tool Usage, Memory Policy, Example Interactions. 'Be helpful and professional' describes nothing; strong files have real opinions, specific limits, and concrete examples; 200-500 words, shorter = sharper.

- [Greg Ceccarelli](https://x.com/gregce10/status/2056771029867933884) — 2026-05-20: Field notes on a 'goal engineering' workflow: instead of prompts/specs, write two checked-in markdown artifacts per round — a 'goal' capped at 4,000 chars (matching Codex's /goal limit) and an unbounded 'rider' with ~11 phases and named depth tests — authored via a Skill. Aimed at long-running agentic turns.

- [Aakash Gupta](https://x.com/aakashgupta/status/2056405221908394406) — 2026-05-19: Aakash Gupta on Pawel Huryn's six-item CLAUDE.md 'routing table' (project description, file-structure map, identity context, knowledge routing, workflow pointers, and a 3-line self-improving prompt), with everything else in on-demand files/folders. The paste-ready self-improving prompt: review existing rules/hypotheses, apply confirmed rules, then update them from feedback each session.

- [Dami-Defi](https://x.com/damidefi/status/2056053698674270631) — 2026-05-19: Fed MIT's 12 free graduate-level AI textbooks into Claude and rebuilt his research system around them. Links 'I Fed 12 Free MIT AI Textbooks Into Claude. It Rebuilt My Entire Research System.'

- [Jaynit Makwana](https://x.com/jaynitmakwana/status/2055594459426070640) — 2026-05-18: Turns Barbara Oakley's 'Learning How to Learn' science (rereading and highlighting don't work; intuition about learning misleads) into 10 Claude prompts that build a personalized study system from how the brain actually acquires skill.

- [klöss](https://x.com/kloss_xyz/status/2055477217552142782) — 2026-05-16: Seven production-grade /goal templates (Ideation/Interrogation, Planning & Documentation, Build & Implementation, Refactoring, Consolidation, Hardening, Migrations; use 1-3 in order, 4-7 as needed), building on the argument that /goal is the best command in Codex/Claude Code/Hermes and most use it wrong.

- [George from prodmgmt.world](https://x.com/nurijanian/status/2055333397611077881) — 2026-05-15: Favorite ways to 'write requirements' with AI: /grill-me (mattpocock/skills), /shaping (rjs/shaping-skills), and a new skill built from business-analyst literature ('make-requirements-great') — reviving useful BA rigor that got dropped as teams went agile/sloppy.

- [Ole Lehmann](https://x.com/itsolelehmann/status/2055290989577753034) — 2026-05-15: Listicle of 9 personal-AI-assistant workflows the author would build on Hermes if starting from zero: Daily Brief (calendar+emails+weather+headlines to Telegram at 7am), self-improving Viral Swipe File (auto-extracts hooks/structure/stats from above-threshold posts), Trending Workflows Radar (scans Reddit/X/AI forums daily), and six more. Practical patterns for personal automation.

- [Petra Donka](https://x.com/petradonka/status/2054897826149101588) — 2026-05-15: Argues agents doing judgment-heavy work need feedback loops, not perfect prompts — because no static prompt covers everything as the product/users/team's taste evolves. Walks through Warp's experience building an agent for their Developer Experience team that responds to Warp mentions on Twitter/Reddit and learns from team feedback over time.

- [Anatoli Kopadze](https://x.com/anatolikopadze/status/2054568935274549597) — 2026-05-15: 18-step listicle on getting more out of Claude (2.4M views). Step 1 — use Projects, not bare chats, so context persists across conversations; later steps cover memory, custom instructions, integrations, and workflows. Listicle framing is engagement-farmy but several tips are practical Claude.ai usage patterns worth knowing.

- [George from prodmgmt.world](https://x.com/nurijanian/status/2054244221352325359) — 2026-05-14: PM advocates using an LLM as an adversarial reviewer on your PRD — the flaws that ship to production are the ones you can't see from inside the doc. Short take with a link to his prodmgmt.world article walking through the practice.

- [George from prodmgmt.world](https://x.com/nurijanian/status/2054216035503587396) — 2026-05-13: George keeps reusing his own AI skill-building pipeline and wishes it were a product. Quote of his March 28 article on building AI skills as a non-expert by finding subject-matter experts in PDFs (he built game-theory and formal-logic skills this way).

- [Ronin](https://x.com/deronin_/status/2054255152555545079) — 2026-05-12: Ten token-waste mistakes senior AI engineers stopped making — auto-context loading 50 files for a 30-line fix ($1.20/turn waste), defaulting Opus on lint/format/rename ($0.60 vs Haiku $0.02), tool-call loops resending the full repo on retry, defaulting to Sonnet when Kimi 2.6 matches at 1/6 cost, streaming on stable-prefix workflows killing prompt cache, "just-in-case" file includes blowing 80K-token prompts. Karpathy-quote framing.

- [klöss](https://x.com/kloss_xyz/status/2054096165055217987) — 2026-05-12: Detailed /goal prompt template for Codex / Claude Code / Hermes with structured slots: GOAL (single measurable outcome), CONTEXT, CONSTRAINTS, PRIORITY, PLAN (understand first), DONE WHEN, VERIFY (tests/build/lint/typecheck). Aimed at killing scope creep and ranking uncertainty before acting. Directly usable.

- [Garry Tan](https://x.com/garrytan/status/2053538847795880414) — 2026-05-11: Garry Tan riffs on a Finbarr take — "code as memory": work with an agent non-deterministically the first time to figure out a task (research + write a script), then execute that script on every future repetition. Quote-tweets his own Apr 22 article on stopping agents from making the same mistakes (LangChain context).

- [Garry Tan](https://x.com/garrytan/status/2053127519872614419) — 2026-05-10: Long-form X article "Meta-Meta-Prompting: The Secret to Making AI Agents Work" — Garry Tan argues to stop treating AI as a chat window and start treating it as an OS. Part of his Fat Skills/Fat Code/Thin Harness series. Open source: github.com/garrytan/gbrain and github.com/garrytan/gstack. Concrete "book mirror" example uses sub-agents per chapter that map ideas to your actual life context. 1.2M views.

- [Mnimiy](https://x.com/mnilax/status/2053116311132155938) — 2026-05-10: Long-form post: Karpathy's 4-rule CLAUDE.md template (born Jan 2026 from his thread on Claude failure modes — silent wrong assumptions, over-complication, orthogonal damage) cut mistakes from ~40% to <3% across 30 codebases over 6 weeks. Forrest Chang's repo hit 120K stars. Author argues the template only fixes Jan code-writing problems; he adds 8 more rules targeting May 2026 agent-orchestration issues (agent fights, hook cascades, skill loading conflicts, multi-step workflows). Notes CLAUDE.md is advisory (~80% compliance); past 200 lines compliance drops sharply. 2.5M views.

- [Dave Kline](https://x.com/dklineii/status/2052372231800439054) — 2026-05-08: Dave Kline teases 5 AI prompts for 1:1 prep — claims his 5-minute pre-meeting AI ritual changed the quality of his 1:1s. Listicle framing; substance in the thread.

- [Ole Lehmann](https://x.com/itsolelehmann/status/2050548948419645488) — 2026-05-02: Argues you should run a 'premortem' on your plans with Claude — frame it as 'it's 6 months from now, this plan died, tell me how' — to bypass the model's optimism bias. Cites Kahneman; says Google, Goldman, P&G use it before launches.

- [GPT Maestro](https://x.com/gptmaestro/status/2050060105052561681) — 2026-05-02: Quote-tweet endorsing a clear walkthrough of GEPA — a technique that optimizes prompts before inference rather than cramming more into context. Quoted source: Quarq's 'Exploring GEPA' (also covers Recursive Language Models / RLMs).

- [Akshay](https://x.com/akshay_pachaar/status/2050201509821063576) — 2026-05-01: Walkthrough of why Claude skills fail silently and how progressive disclosure works: Tier 1 = YAML frontmatter (~100 tokens, always loaded), Tier 2 = SKILL.md body (loads on trigger from description), Tier 3 = bundled scripts (loaded on demand, only stdout enters context). Description quality determines triggering.

- [Raymond Weitekamp](https://x.com/raw_works/status/2046240194999755153) — 2026-04-21: Long-form X article 'RLMs are the new reasoning models': Recursive Language Models let a root model treat its own prompt as an environment it inspects/slices/recursively subqueries via a REPL, collapsing reasoning and tool use into one inference abstraction and processing inputs orders of magnitude beyond the context window. Traces the reasoning-vs-tool-use history (CoT, ReAct, Toolformer, o1) and the Oolong/LongMemEval/LongCoT benchmark arc where RLM scaffolds post leading numbers — including small models (Qwen3-8B/27B) jumping well past their base, hinting the frontier stops being GPU-rich-only. Flags cost/time and 'models are bad at acting recursively' as open limits.

- [Ihtesham Ali](https://x.com/ihtesham2005/status/2046197374855582157) — 2026-04-21: Writeup of George Pólya's 1945 book 'How to Solve It' — the four-step problem-solving framework (understand, plan, execute, look back). Central heuristic: if you can't solve the proposed problem, solve a simpler related one first. Jeremy's note 'important for planner?' — relevant for AI agent planning/decomposition patterns.

- [Vox](https://x.com/voxyz_ai/status/2045899539526148193) — 2026-04-21: The #1 GitHub trending repo this week (44,465 stars) is a CLAUDE.md file distilling Andrej Karpathy's LLM coding pitfalls into 4 principles: (1) think before coding — ask when unsure, (2) simplicity first — minimum code, (3) surgical edits — only touch what's required, (4) goal-driven — translate fuzzy instructions into verifiable targets. Directly actionable as a CLAUDE.md system prompt.

- [Alex Ker](https://x.com/thealexker/status/2045203785304232162) — 2026-04-18: Alex Ker's deep-dive guide on optimizing AI coding harnesses: keep config/.md files lean and human-written (frontier LLMs hit a "dumb zone" past a few hundred instructions), use progressive disclosure for CLIs/skills/MCP tools, structure prompts with HumanLayer's Research-Plan-Implement (R.P.I.) framework, and use subagents (parallel fan-out for breadth, pipelines for depth) to keep the main context clean. Core argument: the harness, not the model, is where engineering judgment compounds, so commit to one and iterate.

- [Millie Marconi](https://x.com/milliemarconnni/status/2044358003714097601) — 2026-04-15: Uses Claude as a full inversion engine running Charlie Munger's method — mapping every path to failure to make the path to success obvious by elimination. Shares 5 prompts for applying systematic inversion to any problem.

- [Shaw (spirit/acc)](https://x.com/shawmakesmagic/status/2044269097647779990) — 2026-04-15: Shaw shares a reusable prompt for cleaning up "vibecoded" codebases by spawning 8 parallel subagents, each owning one cleanup task: DRY/dedup, consolidating shared types, removing unused code (knip), untangling circular deps (madge), replacing weak types (any/unknown), stripping needless defensive try/catch, removing legacy/fallback paths, and cutting AI-slop comments. Each subagent researches, writes a critical assessment, then implements high-confidence fixes.

- [Mario Zechner](https://x.com/badlogicgames/status/2043757216885256463) — 2026-04-15: Mario Zechner recommends Alex Volkov's article 'The Z/L Continuum — Do AI engineers even need to read code anymore?' (thursdai.news/zl), which asks how much code AI engineers still need to read in 2026 and beyond.

- [Kevin Simback](https://x.com/ksimback/status/2043745657748361476) — 2026-04-14: 'My Second Brain Setup: A Modified Karpathy Method' — builds on Karpathy's LLM-knowledge-base pattern (LLM incrementally compiles sources into an interlinked markdown wiki; LLM=programmer, wiki=codebase, Obsidian=IDE) and adds a two-author rule: an `author: kevin` vs `author: agent` frontmatter field where human-authored files are untouchable. Runs on Claude Code with five slash commands (/research fanning out 5-8 parallel agents, /ingest, /wiki-query, /wiki-lint, /wiki-output) and a 'graduation' loop that promotes good agent pages into the protected human layer.

- [Alex Finn](https://x.com/alexfinn/status/2043719233213980922) — 2026-04-14: Alex Finn shares a SOUL.md prompt philosophy inspired by Garry Tan's post: demand completeness over 'good enough,' never table things for later when the permanent solve is in reach, always ship with tests and documentation. Includes a copy-paste prompt for OpenClaw/Hermes agents.

- [Tech with Mak](https://x.com/technmak/status/2043683120319520806) — 2026-04-14: Distills three Karpathy critiques of coding agents (wrong assumptions unchecked, overcomplication/bloat, editing code they don't understand) into a drop-in CLAUDE.md with four principles: (1) think before coding / surface ambiguity and push back, (2) simplicity first / no unrequested abstractions, (3) surgical changes / don't touch adjacent code, (4) goal-driven execution / turn tasks into failing tests then loop to green. Practical, copy-paste engineering guardrails.

- [Garry Tan](https://x.com/garrytan/status/2043581361798500602) — 2026-04-13: Garry Tan adds 'Boil the ocean' to his SOUL.md: the marginal cost of completeness is near zero with AI. Do the whole thing with tests, docs, and quality. Never table for later, never present workarounds, never leave dangling threads. 433.1K views.

- [Defileo](https://x.com/defileo/status/2043437202190024912) — 2026-04-13: Defileo promotes a 'prompt vault' going beyond the classic f/prompts.chat role-based prompts (159K GitHub stars). Claims deeper structured prompts with phases, diagnostic questions, and domain-specific workflows for Claude. Engagement-farming style but references the real prompts.chat repo.

- [Justin Brooke](https://x.com/imjustinbrooke/status/2041890745167061245) — 2026-04-09: Introduces 7 markdown files for structuring AI agent systems: SOULS.md, AGENTS.md, USER.md, TOOLS.md, MEMORY.md, HEARTBEAT.md, STYLE.md. Core thesis is "harnesses > models" — the orchestration layer matters more than which foundation model you use.

- [ℏεsam](https://x.com/hesamation/status/2038758029940654507) — 2026-03-31: Ole Lehmann built a Claude skill implementing Karpathy's LLM Council method — 5 AI sub-agents critique your idea from different angles with anonymous peer review. A practical fix for the 'AI yes-man' problem where Claude just tells you what you want to hear.

- [Shann³](https://x.com/shannholmberg/status/2036461256006357409) — 2026-03-29: Karpathy's AutoResearch method applied to Claude skills optimization. Ole Lehmann tested it on landing page copy, improving pass rate from 56% to 92% overnight. The method auto-improves any skill on autopilot by running automated evaluations and iterating.

- [Millie Marconi](https://x.com/milliemarconnni/status/2036363493478375797) — 2026-03-25: A Claude Code skill (/last30days) scans Reddit and X from the past 30 days on any topic and generates copy-paste-ready prompts based on what's actually working in the community right now — not months-old advice. Works for any domain (Midjourney, Cursor rules, legal prompts, etc.). Open source, MIT license.

- [George from prodmgmt](https://x.com/nurijanian/status/2035257434365976671) — 2026-03-22: George (prodmgmt.world) recounts improving his AI skills with Karpathy's Auto Research library (auto-improves prompts via repeated experimentation), using Ole Lehmann's fork turned into a skill that tunes other skills: define test inputs, write judges that score outputs, let the optimization loop run, and wake up to a better skill.

- [Ole Lehmann](https://x.com/itsolelehmann/status/2033982679423848802) — 2026-03-18: Ole Lehmann shares a single skill that auto-improves any other skill using Karpathy's autoresearch method: it runs the skill and scores the output, finds what's failing, makes one small change to the skill prompt, re-runs to check the score, keeps or reverts the change, and repeats until the skill works. Article: 'How to 10x your Claude Skills'.

- [Ming "Tommy" Tang](https://x.com/tangming2005/status/2031358195558658266) — 2026-03-11: Tommy Tang's single biggest CLAUDE.md improvement: when a bug is reported, don't start by fixing it. Start by writing a test that reproduces the bug, then have subagents try to fix it and prove the fix with a passing test.

- [kapilansh](https://x.com/kapilansh_twt/status/2031262184442130863) — 2026-03-11: kapilansh argues most devs learning AI only know how to call an API and write a prompt without understanding what happens inside, and recommends Karpathy's 'Neural Networks: Zero to Hero' playlist (micrograd, makemore, attention from scratch, tokenization, training GPT-2) as the genuine fix for that knowledge gap.

- [Numman Ali](https://x.com/nummanali/status/2030012892192309461) — 2026-03-07: Numman Ali strongly recommends a deeply technical article, 'Your LLM Doesn't Write Correct Code. It Writes Plausible Code,' praising its articulation of the plausible-vs-correct distinction in LLM output — illustrated by a 100-row primary-key lookup where SQLite takes 0.09ms but an LLM-generated Rust rewrite takes 1,815.43ms.

- [Alex Prompter](https://x.com/alex_prompter/status/2029961559615607052) — 2026-03-06: Citing a GitHub analysis of 2,500+ repos, argues most agents.md files fail by being too vague. Top performers give each agent ONE narrow job (docs writer, test engineer, lint fixer) with specific examples — specialists beat generalists.

- [Philipp Schmid](https://x.com/_philschmid/status/2029570052530360719) — 2026-03-06: Practical guide to evaluating agent Skills, which are often AI-generated and untested: define success criteria (outcome/style/efficiency), build 10-12 prompts with deterministic checks, add an LLM-as-judge for qualitative checks, and iterate on the skill from eval failures.

- [tetsuo](https://x.com/tetsuoai/status/2028068322106097773) — 2026-03-02: Technical breakdown of recurring agentic failure modes in fast/distilled code models: wrong direct-exec vs shell selection, structured-output (JSON-only) non-compliance, and tool-result grounding failures (reporting success after a tool error). Fix: distill full agent trajectories (request→tool→output→grounded response), add contrastive near-miss examples, and gate on concrete agentic evals.

- [Thariq](https://x.com/trq212/status/2027463795355095314) — 2026-02-28: Anthropic's Thariq on building Claude Code: designing an agent's action space is an art. Walks through the AskUserQuestion tool's evolution (ExitPlanTool param → output-format parsing → dedicated tool), the shift from TodoWrite to the Task tool as models improved, replacing RAG with a Grep search tool so Claude builds its own context, progressive disclosure via Skills, and the Claude Code Guide subagent. Lesson: revisit tool assumptions as capabilities grow; experiment, read outputs, 'see like an agent.'

- [Sudo su](https://x.com/sudoingx/status/2027264446989848613) — 2026-02-27: Practical steering tips for local coding agents: tell the model its own architecture/constraints (e.g. Qwen3.5 fires 8 of 256 experts/token), give project structure over single prompts, iterate in layers (scaffold → refine → polish), let it debug its own failures, and use long context (262K) to hold the whole project. Notes Claude Code as a solid harness and that llama.cpp merged native Anthropic endpoints (no proxy/LiteLLM). Argues the skill gap in local inference is now the harness and steering, not the models — all on a single RTX 3090.

- [Machina](https://x.com/exm7777/status/2026666140987175221) — 2026-02-27: Engagement-farming post ('the ONLY skill you will ever need for Claude, Codex or Openclaw', 'this skill will change your life') quote-tweeting the author's own X article. Behind the hype the underlying topic is a meta-skill/prompting framework meant to change how AI reasons for you; content quality behind the clickbait is unverified.

- [Atlas Forge](https://x.com/atlasforgeai/status/2026380335249002843) — 2026-02-25: Long-form piece on nine 'meta-learning loops' that let an agent improve across sessions, not just within one: failure-to-guardrail pipelines, tiered memory with trust scoring and decay, prediction-outcome calibration, nightly extraction, friction detection, expiring context holds, plus cognitive loops (epistemic tagging, creative-mode directives, recursive self-improvement). Start with a regressions list; the key is closing the loops so learning compounds.

- [Charly Wargnier](https://x.com/datachaz/status/2024803152730423685) — 2026-02-20: Charly Wargnier argues writing crystal-clear instructions for machines is the new 10x dev skill, and the most important file in a repo is now CLAUDE.md rather than the code. Top devs use it as an AI onboarding doc to define agent behavior: force the AI to verify its own work, auto-fix CI bugs, and reject hacky fixes.

- [Aman](https://x.com/amank1412/status/2023754885473394918) — 2026-02-19: Aman shares Garry Tan's (CEO of Y Combinator) CLAUDE.md prompt for Claude Code, which he uses to ship 4,000+ line features with full tests in about an hour. The prompt makes Claude act like a senior engineer: judge whether a plan is over/under-engineered before coding, do a structured review (architecture -> code quality -> tests -> performance), present tradeoffs with opinionated recommendations, and pause for feedback before implementing.

- [J.B.](https://x.com/vibemarketer_/status/2019435524532904205) — 2026-02-19: J.B. (VibeMarketer) describes a 'recursive self-improvement loop' skill for Claude: instead of prompting once and shipping, the skill generates output, scores it against explicit criteria, diagnoses weaknesses, rewrites, and re-scores until it clears the bar. Cites @maxwellfinn's image-ad skill that grades concepts on 10 criteria (thumb-stop power, curiosity gap, emotional trigger, persona recognition) and won't stop below 9/10.

- [Spencer Baggins](https://x.com/bigaiguy/status/2021532622963585214) — 2026-02-12: Engagement-style thread claiming 'OpenAI and Anthropic engineers leaked' a technique called 'Socratic prompting' that separates beginners from experts. The substantive nugget: instead of telling the AI what to do, ask it questions. Author claims output quality jumped from 6.2 to 9.1 out of 10.

- [Peter Steinberger](https://x.com/steipete/status/2020704611640705485) — 2026-02-09: Peter Steinberger shares a SOUL.md rewrite prompt (via Molty) to give a coding agent a stronger personality: hold strong opinions instead of hedging, delete corporate-handbook rules, never open with filler like 'Great question', enforce brevity, allow natural humor, call out bad ideas (charm over cruelty), and permit well-placed swearing.

- [abhi](https://x.com/abhigyawangoo/status/2013823175855923640) — 2026-01-21: A detailed playbook for building continually-improving AI agents: define the business metric first, think in terms of many per-message/session/long-tail signals (not just thumbs up/down), design UI that makes signal collection easy, build signal-derived few-shot rankers, and A/B test every change against a control group. Includes a long copy-paste prompt for having Claude Code wire feedback loops into an existing agent. Warns about reward hacking when over-optimizing a single signal.

- [am.will](https://x.com/llmjunky/status/2013314055755194468) — 2026-01-20: am.will endorses a post by Dillon Mulroy on writing agent plans, calling it similar to his own approach but more concise. Plans to adopt some of Dillon's phrasing, especially the language around testing.

- [Paul Solt](https://x.com/paulsolt/status/2012010080414081188) — 2026-01-16: Paul Solt's 7 beginner tips for OpenAI Codex: (1) start with GPT-5.2-Codex 'high' reasoning - enough for most work, avoid xhigh unless tricky; (2) when reasoning doesn't help, give agents better up-to-date local docs (he uses DocSetQuery to turn Dash DocSets into local Markdown); (3) read Peter Steinberger's (@steipete) 'shipping at inference speed' post; (4) borrow from Peter's agents.md and agent-scripts (e.g. 'committer' for atomic commits with multiple agents in one folder); (5) just talk to Codex - no complex rules or huge plan files; work one aspect at a time and parallelize projects while waiting; (6) ask agents to copy structure/Makefiles from other projects; (7) you'll likely need YOLO/danger mode to avoid constant approval nagging.

- [Jainam Parmar](https://x.com/aiwithjainam/status/1999815060965994896) — 2025-12-14: An engagement-styled post ('Chain of Thought is dead') claiming that 'Atom of Thought' prompting made models 30-40% more accurate on complex reasoning tasks, pitched as a technique that will change how people use ChatGPT and Claude. Hype framing, but the underlying Atom-of-Thought prompting idea is a real reasoning technique worth a look.

- [Rohan Paul](https://x.com/rohanpaul_ai/status/1998262710040228310) — 2025-12-09: Rohan Paul summarizes a paper proposing an 'agentic file system' for context engineering: treat every memory, tool, external source, and human note as a file in a shared space, with a persistent context repository separating raw history, long-term memory, and short-lived scratchpads so the prompt holds only the slice needed now. Every access is logged with timestamps and provenance, and a constructor/updater/evaluator manage context under the model's limited window.

- [Rohan Paul](https://x.com/rohanpaul_ai/status/1997405403987222642) — 2025-12-07: Rohan Paul summarizes Google's guide on context engineering for multi-agent systems (built around ADK). Instead of giant prompts, it compiles a view over state split into Working Context, Session, Memory, and Artifacts; each call rebuilds Working Context from instructions, selected session events, memory results, and artifact references. ADK controls context growth via compaction, filtering, and caching — summarizing old spans, dropping useless events, and reusing a stable prefix — and pushes large payloads out to Artifacts to keep systems fast, affordable, and less hallucination-prone.

- [George from prodmgmt.world](https://x.com/nurijanian/status/1988335427447869565) — 2025-11-12: George (prodmgmt.world) shares a 'tough, unreasonable product executive' critique prompt he runs product decisions through: it skeptically stress-tests requirements across cross-team collaboration, conflicting requirements, maintainability, strategic implications, clarity, and feasibility, returning structured critiques (section/issue/impact/suggestion). Ends with a paid prompt-library link.

- [Prompter](https://x.com/promptllm/status/1986173095896621150) — 2025-11-06: Prompter claims elite performers all use neuro-linguistic programming (NLP) and offers a prompt that 'teaches you NLP.' Engagement-bait framing with an unsubstantiated claim; the actual prompt is not shown in the post.

- [Charly Wargnier](https://x.com/datachaz/status/1984276199309484409) — 2025-11-01: Charly Wargnier boosts a claim that someone put in 1,000 hours of prompt engineering to distill the 6 prompt patterns that actually matter. Hook post pointing to the six patterns (detailed in the referenced content).

- [Matt Pocock](https://x.com/mattpocockuk/status/1983255353597870285) — 2025-10-29: Matt Pocock shares his favorite AI coding tip: add 'Be extremely concise. Sacrifice grammar for the sake of concision.' to your global claude.md file for noticeably better output.

- [Prompter](https://x.com/promptllm/status/1974518025211818291) — 2025-10-05: Engagement-style post promoting a prompt for learning to think in systems.

- [Prompter](https://x.com/promptllm/status/1974206336511394165) — 2025-10-04: Engagement-style post promoting a prompt that claims to teach 'NLP' (Neuro-Linguistic Programming) techniques used by high performers.

- [Matt Pocock](https://x.com/mattpocockuk/status/1958179930262356032) — 2025-08-21: Praises an Anthropic context-engineering template as a solid reference for structuring context for LLMs.

- [Dante O. Cuales, Jr.](https://x.com/danteocualesjr/status/1957204427909321027) — 2025-08-18: Argues the intimidation factor of AI engineering is mostly artificial: most work is API orchestration, prompt optimization, and data-pipeline plumbing, with model internals abstracted away. The real skill is choosing the right tool and chaining them effectively.

- [Anthropic](https://github.com/anthropics/courses/tree/master/prompt_engineering_interactive_tutorial/Anthropic%201P) — 2025-04-23: Anthropic's official interactive prompt-engineering tutorial (Jupyter notebooks in anthropics/courses): a 9-chapter curriculum on prompt structure, being clear and direct, role prompting, separating data from instructions, output formatting, step-by-step reasoning, few-shot examples, and avoiding hallucinations, plus appendices on prompt chaining, tool use, and search & retrieval.

- [Tom Dörr](https://github.com/tom-doerr/dotfiles/blob/master/instruction.md) — 2025-01-04: Tom Dörr's AI-coding-agent instruction file (an AGENTS.md-style rules doc): single-letter command aliases (c=continue, rc=reduce complexity, acp=add/commit/push, t=add tests), strict engineering rules (no fallbacks, don't swallow exceptions, TDD with many asserts, uv over pip, work on git branches, keep complexity low, don't weaken the linter), and ready-to-paste DSPy optimizer snippets (BootstrapFewShotWithRandomSearch, MIPROv2, SIMBA).

### Research (155)

- [0xSero](https://x.com/0xsero/status/2077488957999173936) — 2026-07-16: 0xSero highlights Thinking Machines' launch of Inkling (thinkingmachines.ai/news/introducing-inkling), a 950B-parameter American open-weight model that reasons across text, image, and audio modalities with full weights released. Available for fine-tuning on Thinking Machines' Tinker platform and via the Inkling Playground.

- [Superman](https://x.com/thesupermanmx/status/2077321341490090486) — 2026-07-16: turbovec (github.com/RyanCodrai/turbovec) is a vector index built on TurboQuant, written in Rust with Python bindings — a performance-oriented approximate nearest-neighbor index relevant to embedding search and RAG pipelines.

- [Alvaro Videla](https://x.com/old_sound/status/2076932819008242037) — 2026-07-14: Alvaro Videla released LeetLLM (github.com/videlalvaro/leet-llm) — a free, problem-based course of 48 lessons for building a small LLM inference engine on Apple Silicon in Swift and Metal, progressing from dot products and GEMV through attention and token generation.

- [witcheer](https://x.com/witcheer/status/2076717324585898343) — 2026-07-14: witcheer crowdsourced and hand-tallied 250+ replies on how people run Hermes (Nous Research's open model), distilling community local-deployment setups into six summary stats.

- [0xSero](https://x.com/0xsero/status/2073651251594854573) — 2026-07-06: 0xSero (quote-tweeting Rohan Paul on a Meta paper showing quantized reasoning models often fail because compression makes them doubt a correct answer instead of finishing) reports experimenting with penalizing 'self-doubt' words during generation — claiming ~30% fewer output tokens — plus improving tok/s via CPU offloading.

- [alex fazio](https://x.com/alxfazio/status/2073091833530392614) — 2026-07-05: alex fazio recommends studying ARC-AGI-winning harnesses to learn harness engineering from first principles — they clearly illustrate what works, what's BS, and why a lot of current harness design is overfitted to benchmark-maxxing.

- [ali](https://x.com/waterloo_intern/status/2073171123542573231) — 2026-07-04: ali (@waterloo_intern) — an apparent parody of distillation hype: claims to have distilled 2.3M Claude Fable 5 reasoning traces into Qwen3-4B with '100% self-consistency @ 512 samples, 0.00 bits output entropy, zero hallucination variance,' that 'the student is not bounded by the teacher,' and that it 'converged on one universal truth,' with open-sourced weights. 3M views; reads as satire rather than a real result.

- [akira](https://x.com/realmcore_/status/2073170941878944022) — 2026-07-04: akira introduces Onyx, a VM/runtime for programmable agent orchestration that 'turns orchestration into software engineering.' The article covers the design constraints and decisions behind the VM and how to write programs and architect agent systems on it. Framing: agents are inherently non-deterministic (that's the point), but breaking execution into structured steps (Plan, Implement, Review, QA) plus scripts/tools/skills to steer, share context, and guardrail agents improves performance. References ReAct and related arxiv papers and karpathy/autoresearch.

- [Akshay](https://x.com/akshay_pachaar/status/2072961737008336937) — 2026-07-04: Akshay Pachaar summarizes a Hugging Face blog post on 'evolving the harness' instead of training the model: they took a frozen open model scoring 0% on a hard legal-agent benchmark, left its weights untouched, and let an automated loop rewrite only the surrounding harness code (the runtime wrapper that feeds context, runs tool calls, and decides when a run ends). It ended up essentially matching Sonnet 4.6 on the headline metric at ~7x lower cost per task, zero weights changed. The insight: the 0% wasn't measuring legal reasoning — the model reasoned correctly but saved outputs under the wrong filename/folder or not at all — so it was measuring the harness.

- [Jason Weston](https://x.com/jaseweston/status/2070117091521204521) — 2026-06-25: Paper announcement ("Autodata", arXiv:2606.25996): agentic data creation as a way to convert increased inference compute into higher-quality model training data. Claims gains on CS, legal, and math problems over classical synthetic-data methods, plus a way to meta-optimize the data-scientist agent so it produces even stronger data. Thread (1/6).

- [Hugging Models](https://x.com/huggingmodels/status/2069750892287721960) — 2026-06-25: Brief hype post: NVIDIA released an FP4 quantized MoE version of Qwen3.6 that fits in 35B parameters but runs with the efficiency of a ~3B model, pitched as a win for efficient inference.

- [Mario Zechner](https://x.com/badlogicgames/status/2069156188902559751) — 2026-06-23: Mario Zechner recommends a video dissecting Voxtral, a family of open-source speech models, and the foundational work behind it (audio tokenization, semantic/acoustic disaggregation). He quote-tweets Julia Turc, who frames it as what you get when you plug LLMs into voice assistants instead of a decade of handwritten rules.

- [0xSero](https://x.com/0xsero/status/2069114653842522463) — 2026-06-23: 0xSero recommends an educational YouTube video explaining LoRA (Low-Rank Adaptation): how tiny trainable matrices let anyone fine-tune large AI models relatively cheaply.

- [冬天](https://x.com/seventhoce56019/status/2068901168940745088) — 2026-06-23: Translated from Chinese: a writeup of reverse-skill (GitHub zhaoxuya520/reverse-skill), an AI skill package that puts reverse-engineering and security tasks behind a routing.md file so the agent self-triages across 20+ sub-skills (APK reversing, IDA static analysis, JS frontend reversing, firmware security, EDR evasion, vulnerability exploitation). Framed as lowering the barrier to security offense/defense.

- [Sakana AI](https://x.com/sakanaailabs/status/2068862070062485867) — 2026-06-23: Sakana AI announces Fugu, an orchestration model that routes across a swappable pool of underlying agents rather than relying on one monolithic model. Their blog argues orchestration is the next frontier and a hedge for AI sovereignty against vendor export controls; Fugu reportedly matches leading models (Fable, Mythos) on engineering, science, and reasoning benchmarks.

- [Avi Chawla](https://x.com/_avichawla/status/2068657496936616314) — 2026-06-23: Avi Chawla explains why BM25, a 30-year-old keyword ranking algorithm with no training or embeddings, still powers Elasticsearch/OpenSearch and excels at exact-match retrieval where embeddings struggle, making hybrid (BM25 + vector) search the default in top RAG systems. He closes on the UX problem of highlighting which span actually drove a semantic match, pointing to his co-founder's article.

- [How To Prompt](https://x.com/howtoprompt__/status/2067176008445513800) — 2026-06-17: Engagement-farmed post claiming an open-source repo compresses 60M text chunks from 201GB to ~6GB (97% smaller) with no accuracy loss, running fully private on a standard laptop with no cloud or GPU — pitched as making vector databases obsolete. No repo link was surfaced in the post or visible replies, so the project would need to be located before the claim can be evaluated.

- [Ahmad](https://x.com/theahmadosman/status/2066825976705646929) — 2026-06-17: Ahmad highlights VibeThinker 3B (built on Qwen 2.5), a 3B-parameter model he claims reaches Opus 4.5-level performance, quoting his own earlier prediction that Claude Code + Opus 4.5-quality models will run locally on a single RTX PRO 6000 before year-end. A signal on how fast small/efficient local models are closing the gap with frontier models.

- [Avid](https://x.com/av1dlive/status/2066127265407336535) — 2026-06-15: Argues you can run capable AI models locally on a Mac for free using Apple's MLX stack — install mlx-lm, launch its server, and point any agent at localhost. Cites a ~23-minute talk from an Apple MLX-team engineer in which a local model builds a working SwiftUI app from a blank Xcode project in two minutes and then fixes a bug, with nothing leaving the machine. Quote-tweets a piece on the ThinkStation PGX local-inference box.

- [Olivia Chowdhury](https://x.com/oliviacoder1/status/2066064093552038070) — 2026-06-15: Hype-framed thread on a Dec 31, 2025 MIT CSAIL paper that claims to 'solve' AI memory not by building bigger context windows but by teaching models how to read/retrieve — positioning the result against the industry's context-window arms race and the 'context rot' problem, where a model's performance on information already in context degrades as more is packed in.

- [Ahmad](https://x.com/theahmadosman/status/2063935919481106560) — 2026-06-09: Self-study curriculum for LLM serving engines and GPU kernel programming: start with vLLM / SGLang / TensorRT-LLM / FlashInfer (PagedAttention, continuous batching, prefix caching), then dive into Triton, CUTLASS/CuTe, FlashAttention papers, PagedAttention paper, MoE docs, Nsight profiling. Followed by a hands-on project sequence (Triton RMSNorm, fused SiLU×gate, etc.). For people actually wanting to learn the inference stack.

- [Rahul](https://x.com/sairahul1/status/2063609922667815064) — 2026-06-07: Rahul follow-up to his Harness Engineering article: points to walkinglabs.github.io/learn-harness-engineering as 'the best site on the internet to learn harness engineering' — free, comprehensive. Most AI engineers haven't heard the term yet. Worth bookmarking alongside his article.

- [Viv](https://x.com/vtrivedy10/status/2063429138304668093) — 2026-06-07: A default recipe for optimizing Agent = Model + Harness, 'training' both: (1) build v1 on a sensible base harness with task-specific prompting/tools, (2) harness-engineer against prod-like eval tasks (often enough on its own), (3) SFT on mined traces or synthetic data (good for distilling a cheaper model), (4) RL if you can design environments/rewards to push past SFT copying, (5) light harness engineering again on the trained model. Argues harness engineering will be the dominant optimization lever and most companies are still at steps 1-2; links the 'Anatomy of an Agent Harness' article.

- [Dan Roy](https://x.com/roydanroy/status/2062917394356429092) — 2026-06-06: Category-theory joke quoting Markus Buehler's claim of a breakthrough in self-evolving AI 'scientists' moving from search to principled discovery — where the search space itself changes and the AI perceives that shift without intervention.

- [さいぺ (cipepser)](https://x.com/cipepser/status/2062397559520502225) — 2026-06-04: Praises mem0's 'State of Memory in Agent Harness' survey — well-organized coverage from field papers/benchmarks through memory implementations in each coding agent (Cursor, Devin, Claude Code, Codex).

- [yv](https://x.com/yvbbrjdr/status/2061914706579984551) — 2026-06-03: Recommends the MAI-Thinking-1 technical paper as containing almost all the details for training a SOTA LLM (microsoft.ai PDF).

- [恒星](https://x.com/vintcessun/status/2060897802478293013) — 2026-05-31: DeepMind packaged 30+ scientific databases (AlphaGenome, UniProt) into agent skills. The real bottleneck for science agents isn't model quality but knowing how to call databases correctly; skills turn each DB's API into clear instructions + scripts so agents execute step-by-step. One-line npx install (github.com/google-deepmind/science-skills).

- [Yohei](https://x.com/yoheinakajima/status/2060068279574843614) — 2026-05-29: Yohei Nakajima's 'log-centric agent architecture' and his first arXiv paper 'The Log is the Agent: Event-Sourced Reactive Graphs for Auditable, Forkable Agentic Systems' — the case for agents that coordinate through persistent, replayable state.

- [AVB](https://x.com/neural_avb/status/2060032255620431877) — 2026-05-29: A 45-minute walkthrough on creating synthetic datasets and training tiny (~100M param) local language models specialized for narrow tasks; code, datasets, models and harnesses linked.

- [Charly Wargnier](https://x.com/datachaz/status/2059909626532155482) — 2026-05-28: Microsoft open-sourced SkillOpt: optimize agent skills the way you train models — a base model runs tasks while an optimizer rewrites the instructions, keeping only edits that raise the benchmark. Claims SOTA over hand-crafted prompts and TextGrad, with no model lock-in since it learns procedural logic.

- [Muratcan Koylan](https://x.com/koylanai/status/2059753045060395240) — 2026-05-28: On the 'Agent Harness Engineering: A Survey' paper (CMU/Yale/JHU/Amazon; 170+ projects reviewed): real-world agent performance = model capability + harness quality, and for long-horizon production tasks the harness is the main bottleneck. Simple harness tweaks (tool formats, sandboxing, verification loops) yield big benchmark gains; the biggest wins come from turning production traces into regression tests + automated harness fixes.

- [Paul Iusztin](https://x.com/pauliusztin_/status/2059613089260003387) — 2026-05-28: Breakdown of Neo4j's graph-native agent memory: three connected layers in one graph — short-term (ordered message chain), long-term (entity/relationship knowledge graph with embeddings, traversed relationally), and reasoning memory (per-run trees of thoughts/tool-calls/decision paths). Typed edges (:MENTIONS/:INITIATED_BY/:TOUCHED) make provenance a one-hop query; 'the ontology is the real product.'

- [Avi Chawla](https://x.com/_avichawla/status/2059556157984006187) — 2026-05-28: Clear explainer of RAG vs Graph RAG vs Agentic RAG as solving different query types: standard RAG for single-hop factual lookups, Graph RAG (LLM-extracted entities/relationships + traversal) for multi-hop connections, Agentic RAG (an agent choosing tools/sources at query time) for dynamic multi-source tasks — plus binary quantization for 32x more memory-efficient vector search.

- [Theo - t3.gg](https://x.com/theo/status/2059352130289651925) — 2026-05-27: Endorses DeepSWE, a new agentic-coding benchmark that reflects the realistic day-to-day developer experience — showing where top models actually diverge rather than clustering as they do on public leaderboards.

- [Binfeng Xu](https://x.com/billxbf/status/2059323616009838703) — 2026-05-27: Release of Polar, Agent-RL rollout infrastructure that takes real-world harnesses (Codex, Claude Code, OpenClaw, Hermes, or your own) directly as training environments with no code change — find a problem, design the harness, train your own agents.

- [Tom Dörr](https://x.com/tom_doerr/status/2059316125049971017) — 2026-05-27: Shares a 500-hour AI infrastructure engineering curriculum (github.com/ai-infra-curriculum/ai-infra-engineer-learning).

- [Garry Tan](https://x.com/garrytan/status/2058378310254793013) — 2026-05-25: Garry Tan: fine-tuned his own Qwen3.5-397B in a couple hours via Thinking Machines, arguing fast usable multimodal will enable mind-blowing personal AI. Cites Thinking Machines' real-time 'interaction models.'

- [Kevin Simback](https://x.com/ksimback/status/2058262328496554021) — 2026-05-24: A definitive guide to memory in the Hermes Agent, structured as a 3-layer stack: Layer 1 native (two always-injected markdown files MEMORY.md/USER.md plus a searchable SQLite session DB; the 80% consolidation 'rule' is a prompt instruction, not code), Layer 2 the pluggable MemoryProvider slot (8 official providers — Honcho, Mem0, Hindsight, Holographic, OpenViking, RetainDB, ByteRover, Supermemory — one at a time, each a different architectural bet), and Layer 3 community plug-ins (GBrain, Mnemosyne, etc.). Closes with how to pick and warning signs a memory layer is too heavy.

- [Ahmad](https://x.com/theahmadosman/status/2057590791241896254) — 2026-05-22: Points to a free 'LLMs 101: A Practical Guide (2026 Edition)' covering model mechanics (tokens, transformers, attention, KV cache, decoding, RAG, agents, fine-tuning, multimodal) and running models locally (quantization, VRAM math, hardware tiers, runtimes, model selection, failure modes).

- [aditya](https://x.com/adxtyahq/status/2057410759236386866) — 2026-05-22: A worked answer to a Google L5 interview question — 'design a RAG pipeline for 10M docs with zero hallucination': ingest/normalize, hybrid retrieval (BM25 + embeddings), ANN + reranking, source-confidence scoring, constrained generation, citation-backed responses, hallucination fallback, continuous evals, caching, and observability. At scale, retrieval quality matters more than the frontier model.

- [Tom Dörr](https://x.com/tom_doerr/status/2057217338844336627) — 2026-05-22: Shares turbovec, a vector store that fits 10 million documents into 4GB of RAM (github.com/RyanCodrai/turbovec).

- [James Cogan](https://x.com/cogan/status/2056702063992607071) — 2026-05-22: A thoughtful essay, 'Machine Time,' arguing AI compresses the unit of meaningful time — shrinking the buffer between noticing a change and having to respond. AI compresses the front end of cognitive work, so the bottleneck moves to human review, judgment, and taste; the danger isn't speed but speed without scaffolding, and institutions increasingly answer with machine-speed coordination rather than restoring the human clock.

- [Viv](https://x.com/vtrivedy10/status/2056993505386622987) — 2026-05-20: Notes on designing LangSmith Engine for customer-scale data: give the agent autonomy AFTER good tooling (around interacting with LangSmith); agents are good at pulling in context selectively, so the job is helping them self-facilitate routing useful info into the window.

- [Yohei](https://x.com/yoheinakajima/status/2056848954848104488) — 2026-05-20: Yohei Nakajima on ActiveGraph, a 'continuity layer for long-running agents' — a novel agent architecture drawing on older designs, promising for self-improving agents via the ability to fork and diff agent runs.

- [elvis](https://x.com/omarsar0/status/2056764334181884158) — 2026-05-20: 'Code as Agent Harness' — a 100+ page survey of methods and applications of code-as-harness, arguing it may be key to a science of harness engineering, and that future systems must be executable, inspectable, stateful, and governed.

- [Lotte](https://x.com/lotte_verheyden/status/2056754091817361670) — 2026-05-20: 'Evals, explained' (Langfuse Academy): offline eval sits between running an experiment and shipping. Three methods — manual review (build intuition + ground-truth labels), code-based (deterministic checks: schema, keywords, length, SQL executes), and LLM-as-a-judge (language-understanding qualities, needs calibration against human labels). Prefer binary pass/fail over 1-5 scales; one evaluator per quality; start manual then automate repeatable checks.

- [Akshay](https://x.com/akshay_pachaar/status/2056714042455343160) — 2026-05-20: RAG vs CAG explained: Cache-Augmented Generation keeps static, high-value knowledge in the model's KV memory instead of hitting the vector DB every query. Combine them — cache 'cold' static data (policies/docs), retrieve 'hot' dynamic data — for faster, cheaper inference. OpenAI and Anthropic already support prompt caching.

- [Sapient Intelligence](https://x.com/sapient_int/status/2056510383935172798) — 2026-05-19: Sapient Intelligence introduces HRM-Text, an ultra-lean 1B-parameter reasoning model trained on just 40B structured tokens (~1/1000 the data of comparable models), with the full model training in ~one day on a $1,000 budget — pitched as making previously-too-expensive research concepts testable again.

- [Amar Singh](https://x.com/amarsvs/status/2056484487891243355) — 2026-05-19: 'Agent Performance: Model-Bound vs Harness-Bound' — counterintuitively, smarter models make harnesses matter MORE ('the smarter the model, the more expensive it is to waste its intelligence'). Model-bound tasks (hard math/proofs) hinge on raw capability; harness-bound tasks (e.g., Terminal-Bench, ~10 pts spread for Opus 4.7 across harnesses) hinge on prompting, tools, context management. As traces balloon and costs rise, the harness becomes the 'scheduler for intelligence'; author's open-source HALO optimizes harnesses from traces.

- [AVB](https://x.com/neural_avb/status/2056462216430535062) — 2026-05-19: Notes that people are now training local recursive language models inside python REPLs with RL — agents divide-and-conquer long problems and pass context around as python variables. Links 'Recursive Agent Optimization using RL, explained clearly.'

- [Paul Iusztin](https://x.com/pauliusztin_/status/2056272402414211175) — 2026-05-19: Calls Neo4j's open-source 'agent-memory' the best repo for a unified graph-based memory layer for AI agents — strong modeling of short/long/reasoning memory, ontology, and extraction algorithms; full write-up on decodingai.com.

- [Dami-Defi](https://x.com/damidefi/status/2056053698674270631) — 2026-05-19: Fed MIT's 12 free graduate-level AI textbooks into Claude and rebuilt his research system around them. Links 'I Fed 12 Free MIT AI Textbooks Into Claude. It Rebuilt My Entire Research System.'

- [Viv](https://x.com/vtrivedy10/status/2056066419360743479) — 2026-05-18: Viv on LangSmith Engine as an always-on self-improvement loop: tracing on for every agent, purpose-built SmithDB for agent-scale data, ambient intelligence over every trace to find errors/insights, and PRs/Evals generated with human gating — the first sparks of company-wide Continual Learning for agents.

- [Vaishnavi](https://x.com/_vmlops/status/2055887618303570151) — 2026-05-18: Recommends walkinglabs.github.io/learn-harness-engineering as the best site to learn harness engineering.

- [Vasilije](https://x.com/tricalt/status/2055876832797581406) — 2026-05-18: 'Memory isn't a plugin. Skills aren't a plugin. They're the same harness' — both are a world model (everything the agent uses to predict its next action). Memory observes the world; skills (SKILL.md procedures) codify it into rules and degrade silently without an Observe→Inspect→Amend→Evaluate loop. Cognee stores skills and memory in one graph so a skill is a traceable, evolving memory node.

- [santi](https://x.com/santtiagom_/status/2055751665345798628) — 2026-05-18: Praises an OpenAI article on Harness Engineering and Codex — how they used agents to build an internal ~1M-line product: preventing agent-generated code from degrading, using tests/CI as more reliable constraints than prompts, keeping code/docs readable for agents, and how engineers' work changes when agents program.

- [Dan McAteer](https://x.com/daniel_mac8/status/2055838212069773456) — 2026-05-16: Flags a continual-learning result: fast-slow training (FST) treats model params as 'slow' weights and optimized context as 'fast' weights, reportedly beating weights-only training on every measured axis across math, code, and general reasoning.

- [Sam Hogan](https://x.com/samhogan/status/2055064462844219603) — 2026-05-15: Sam Hogan introduces HALO (Hierarchical Agent Loop Optimizer) — github.com/context-labs/halo — which uses Reasoning Language Models to let the model itself shape its own agent harness rather than hard-coding it. Inspired by @a1zhang's "Mismanaged Genius Hypothesis" (LLMs are smarter than the harnesses humans design for them). Reports consistent 10%+ benchmark improvements across multiple evals.

- [Berryxia.AI](https://x.com/berryxia/status/2054924976835510337) — 2026-05-15: Translated-from-Chinese thread breaking down Tencent's newly open-sourced AI agent memory system (6 months of work). Highlights three techniques: real-time compression of expired context (cuts token usage 61%), Mermaid-syntax structured task maps that keep 30+ step workflows on track, and a long-term memory tier. Argues most teams over-index on context-length and under-invest in memory architecture.

- [How To AI](https://x.com/howtoai_/status/2054611399792644386) — 2026-05-15: Hype-framed thread about Google's new "Nested Learning: The Illusion of Deep Learning Architectures" paper (calling it "Attention Is All You Need V2"). Argues that today's LLMs suffer catastrophic forgetting because we treat them as one flat function, and Nested Learning instead models a network as thousands of nested optimization problems at different update frequencies — closer to how brains consolidate short- and long-term memory. Substance is real (Google Research paper), framing is clickbait.

- [ar0cket1](https://x.com/ar0cket1/status/2054108160450064571) — 2026-05-15: Research progress report on On-Policy Self Distillation (OPSD) — trying to get RL-like capability gains with the sample efficiency and stability of on-policy distillation. Experiments on Olmo 3 7B (SFT student vs RL'd teacher) on nemotron-math-v2. Frames OPSD as a stepping stone toward continual learning because RL is currently the best engine for new capability gains.

- [divyansh tiwari](https://x.com/divyansht91162/status/2054430633645293687) — 2026-05-14: Highlights a paper called NanoResearch proposing an agent architecture with three co-evolving layers — Skill Bank (turns repeated actions into reusable expertise), Memory Layer (preserves project + user experience across sessions), Policy Learning (turns free-form feedback into permanent behavioral updates). Pitch: an agent that accumulates experience and aligns to the user over time rather than relying on bigger context windows.

- [송준 Jun Song](https://x.com/jun_song/status/2054379887608402199) — 2026-05-14: Claims that within weeks, a Minimax-M3.0-JANGTQ-CRACK release from @dealignai will bring Opus-4.6-tier local inference to 128GB Macs, with open-source quantization efforts targeting 24GB VRAM. Bullish on where local LLMs land in mid-2026.

- [Ihtesham Ali](https://x.com/ihtesham2005/status/2054458335215395223) — 2026-05-13: Google + Meta paper: Claude Code autonomously proposes, tests, and refines algorithms for improving LLM reasoning over 5 rounds with no human in the loop. Discovers a 4-mechanism controller (EMA momentum stopping, coupled width-depth control, alignment-aware depth allocation, conservative branch abandonment) for $39.90 total compute. Paper at arxiv.org/abs/2605.0xxx.

- [IndieDevHailey (开发者Hailey)](https://x.com/indiedevhailey/status/2054386235867812240) — 2026-05-13: GitHub project RuView (50K+ stars) — uses WiFi CSI signals plus AI to detect humans behind walls without cameras. Pose detection (17 keypoints), breathing/heart rate while sleeping, fall alerts. Runs locally on ESP32; no video, no cloud, privacy-preserving. Translated from Chinese.

- [Joseph Viviano](https://x.com/josephdviviano/status/2054253118943363506) — 2026-05-13: Joseph Viviano's "Agentic Research Best Practices" — 15 months of notes on using coding agents in research workflows (with Mila Quebec collaborators). Key argument: research codebases differ from product engineering — no users, active development, speed bound by intelligibility to author/collaborators, not throughput. Many "best practices" from product engineering feel archaic in research.

- [Tom Dörr](https://x.com/tom_doerr/status/2052552468983103608) — 2026-05-08: Tom Dörr highlights agentic-data-scientist (github.com/K-Dense-AI/agentic-data-scientist) — an open-source self-correcting agent for complex data-science tasks. Worth a look as a benchmark for self-correction patterns.

- [ani](https://x.com/anirudhbv_ce/status/2052532004919361958) — 2026-05-08: Provocative paper 'The Geometry of Consolidation' (github.com/niashwin/geometry-of-consolidation): claims only ~3% of dimensions in major embedding models (91/3072 for OpenAI text-embedding-3-large, 80/3072 for Gemini gemini-embedding-001) do real work, the rest is mathematically empty. Argues RAG compression has a hard floor no algorithm can beat, set by a spectral number the embedding model can't escape — and that this is the root cause of RAG hallucinations. Big claim, worth reading the paper before believing.

- [Goodfire](https://x.com/goodfireai/status/2052420446910644616) — 2026-05-08: Goodfire (interpretability research lab) kicks off a series of blog posts on 'neural geometry' — the framing that networks 'speak English but think in shapes,' and that understanding their geometric structure is key to debugging and controlling them. 3.1M views — interpretability research breaking out of the lab into general attention.

- [Millie Marconi](https://x.com/milliemarconnni/status/2052363436575826398) — 2026-05-08: Millie Marconi highlights Feynman (github.com/getcompanion-ai/feynman) — an open-source MIT-licensed agent system with four bundled roles (Researcher, Reviewer, Writer, Verifier) that reads papers, audits referenced code, and replicates experiments. Runs in Docker for safe local execution and spins up serverless GPUs on Modal or persistent pods on RunPod. Indexed session search across past research runs, inline citation-URL verification.

- [Tom Dörr](https://x.com/tom_doerr/status/2052261421744869757) — 2026-05-08: Tom Dörr highlights HelixDB (github.com/HelixDB/helix-db): a database that combines graph and vector storage in one engine for AI apps. Worth evaluating as a building block for RAG and agent-memory pipelines that otherwise span two systems.

- [Kanika](https://x.com/kanikabk/status/2052032420954927357) — 2026-05-08: Kanika points to a 424-page 'Agentic Design Patterns' guide written by a senior Google engineer — every chapter ships working code, all Amazon royalties go to Save the Children, $40 print price. Engagement-bait framing ('bookmark before it's buried') but the reference itself is a real, comprehensive resource.

- [Tom Dörr](https://x.com/tom_doerr/status/2052150733261193390) — 2026-05-07: Tom Dörr points to awesome-foundation-agents (github.com/FoundationAgents/awesome-foundation-agents) — a curated reading list of papers mapping foundation-agent cognition. Reference, not actionable.

- [Vinay](https://x.com/leashless/status/2051437380788158739) — 2026-05-05: Vinay quote-tweets a viral post about Gödel, Escher, Bach (1979) — Douglas Hofstadter's 800-page Pulitzer-winning book on a logician, artist, and composer that became required reading at every major AI lab. Vinay: "Time stopped. We all read it. It took two years to talk through the implications. Nobody ever forgot."

- [Tom Doerr](https://x.com/tom_doerr/status/2050312101504094651) — 2026-05-02: Points to a curated GitHub list on AI agent evolution, memory systems, and self-improvement (github.com/EvoMap/awesome-agent-evolution) — a reference index for the self-improving-agent literature.

- [Xiuyu Li](https://x.com/sheriyuo/status/2050067900820840791) — 2026-05-02: Endorses Will Brown's writeup 'On SFT, RL, and on-policy distillation' — why the SFT→RL pipeline works, where on-policy distillation fits, and how self-distillation goes wrong. Co-authored with Claude Opus 4.7.

- [GPT Maestro](https://x.com/gptmaestro/status/2050060105052561681) — 2026-05-02: Quote-tweet endorsing a clear walkthrough of GEPA — a technique that optimizes prompts before inference rather than cramming more into context. Quoted source: Quarq's 'Exploring GEPA' (also covers Recursive Language Models / RLMs).

- [Xiangyi Li](https://x.com/xdotli/status/2049903693143609627) — 2026-05-02: Short endorsement — 'must read for everyone who wants to reduce the entropy of their agentic systems' — pointing at evals/environments work (benchflow_ai). Framing: disciplined evals as the way to tame nondeterminism in agent systems.

- [Qwen](https://x.com/alibaba_qwen/status/2049861145574690992) — 2026-05-01: Alibaba Qwen team open-sources Qwen-Scope, a suite of sparse autoencoders (SAEs) for the Qwen model family. Surfaces interpretable internal features for steering inference, classifying/synthesizing data, debugging code-switching/repetition at the source, and selecting smarter benchmarks. Blog at qwen.ai/blog?id=qwen-scope, weights on HuggingFace.

- [How To AI](https://x.com/howtoai_/status/2049567036003795269) — 2026-04-30: Tencent's Training-Free GRPO claims to replace expensive RL fine-tuning by extracting the 'semantic advantage' from trial-and-error and injecting it as a 'token prior' / memory rather than updating weights — reportedly trained for $18. Hype-framed ("killed fine-tuning") but the underlying technique is a notable alternative to GRPO/RLHF that avoids overfitting and GPU costs.

- [Edouard Reinach](https://x.com/ereinach/status/2047802558136058258) — 2026-04-28: Edouard Reinach points to Predict-RLM (github.com/Trampoline-AI/predict-rlm) — production-ready implementation of an MIT memory technique. Quote-tweets a hype-framed (questionable) summary of a Dec 31 2025 MIT CSAIL paper claiming they solved AI memory by 'teaching it how to read' rather than building a bigger brain. The repo is the actionable bit; the quoted framing is sales pitch.

- [Ethan Mollick](https://x.com/emollick/status/2047828327856030047) — 2026-04-25: Ethan Mollick: 'Organizational design for agents is hard, benchmarking agents working in concert is hard. Together, this is the next critical frontier for making AI matter in economically valuable tasks, and we really don't know very much about it.' Quote-tweets @krishnanrohit's essay 'Aligned Agents Still Build Misaligned Organisations.'

- [Atal](https://x.com/zabihullahatal/status/2047692175019008019) — 2026-04-25: Engagement-framed ('BREAKING') summary of 'Agent Behavioral Contracts' paper — applies Design-by-Contract (preconditions, invariants, governance rules, recovery mechanisms) as runtime constraints on AI agents instead of prompt-only control. Tested across 1,980 sessions. Real concept (formal verification meets agent runtime) worth tracking under the agents-as-judges concept thread.

- [Tom Dörr](https://x.com/tom_doerr/status/2047258779821949384) — 2026-04-23: Tom Dörr points to CORAL (github.com/Human-Agent-Society/CORAL) — infrastructure for multi-agent self-evolution. Worth a look as a research substrate for agents-that-improve-themselves work.

- [Akshay](https://x.com/akshay_pachaar/status/2047220248081015110) — 2026-04-23: Akshay extends Karpathy's wiki idea: a markdown wiki works for static knowledge but breaks for multi-entity questions like 'which authors moved from Google to Anthropic between 2022-2024 and what did they publish after?' A wiki can only answer that if someone already wrote the article; a graph (entities + relations + dates) lets you ask any variation directly. Argues the next step beyond LLM-maintained wikis is LLM-maintained knowledge graphs.

- [How To AI](https://x.com/howtoai_/status/2047187640781541882) — 2026-04-23: [Post unavailable — page doesn't exist]

- [TRAE](https://x.com/trae_ai/status/2047145274200768969) — 2026-04-23: TRAE's 'Definitive Guide to Harness Engineering' X article — frames harness engineering as the 2026 successor to prompt + context engineering. Term coined by Mitchell Hashimoto (HashiCorp co-founder); gained traction via an OpenAI report. Horse-and-reins metaphor: AI Agent = SOTA Model (wild horse) + Harness (control system) = Elite Performer. Foundational reading for the harness-engineering concept thread alongside Rahul/walkinglabs/Anthropic papers.

- [Alex Volkov](https://x.com/altryne/status/2046977133013311814) — 2026-04-23: OpenAI open-sourced Privacy Filter — a 1.5B-param (50M active) PII detection model on HuggingFace under Apache 2.0. Not a new general LLM; a focused safety-utility model for detecting private info in text. Volkov calls it interesting; useful as a building block in agent pipelines that touch user data.

- [spencer](https://x.com/techspence/status/2046759185593794782) — 2026-04-23: spencer flags OWASP's Autonomous Penetration Testing Standard (github.com/OWASP/APTS) — formal security standard for AI-driven pentesting. Reference for security-team adjacent work; substance pending a real read.

- [Tech with Mak](https://x.com/technmak/status/2046414820241760620) — 2026-04-21: Summary of Meta's REFRAG paper: compresses retrieved RAG chunks into single embeddings (16,384 tokens → 1,024 chunk embeddings), delivering 30.85x faster time-to-first-token, zero perplexity loss, 16x context extension (4K → 64K), and 3.75x better than prior SOTA. Exploits sparse attention patterns in RAG contexts via precomputable embeddings and RL-based compression policy.

- [Aakash Gupta](https://x.com/aakashgupta/status/2046371351016161745) — 2026-04-21: Long analysis of Yann LeCun's post-Meta 'LeWorldModel' JEPA result: first JEPA that trains end-to-end from raw pixels (15M params, single GPU, hours), replacing a pile of collapse-prevention heuristics with one Gaussian-normality regularizer (hyperparam search O(n^6)->O(log n)). Claims 200x fewer tokens/observation than DINO-WM and planning 47s->0.98s/cycle — a potential reset of the humanoid-robotics cost structure, framed as Meta's Xerox-PARC moment.

- [Nav Toor](https://x.com/heynavtoor/status/2046276160930414976) — 2026-04-21: Intro to PoisonedRAG attack: researchers showed 5 malicious documents planted in a 2.6M-document corpus can hijack an LLM's answer 97% of the time. Attacker never touches the model or retriever — just writes documents. Important RAG security consideration.

- [Simplifying AI](https://x.com/simplifyinai/status/2046271932035645599) — 2026-04-21: Summary of Microsoft's MEMENTO paper: instead of growing the KV cache to fit long reasoning chains, train the model to break reasoning into blocks and emit dense compressed 'memento' summaries between them, then drop the raw tokens. Framed as 'the secret isn't remembering everything — it's knowing what to forget.' Engagement-farming tone but real underlying paper.

- [Raymond Weitekamp](https://x.com/raw_works/status/2046240194999755153) — 2026-04-21: Long-form X article 'RLMs are the new reasoning models': Recursive Language Models let a root model treat its own prompt as an environment it inspects/slices/recursively subqueries via a REPL, collapsing reasoning and tool use into one inference abstraction and processing inputs orders of magnitude beyond the context window. Traces the reasoning-vs-tool-use history (CoT, ReAct, Toolformer, o1) and the Oolong/LongMemEval/LongCoT benchmark arc where RLM scaffolds post leading numbers — including small models (Qwen3-8B/27B) jumping well past their base, hinting the frontier stops being GPU-rich-only. Flags cost/time and 'models are bad at acting recursively' as open limits.

- [Akshay](https://x.com/akshay_pachaar/status/2046151867177308181) — 2026-04-20: Akshay summarizes Google DeepMind's 'AI Agent Traps' paper — the first systematic framework for adversarial content engineered to hijack AI agents browsing the web. Maps six attack surfaces: Content Injection (perception: invisible CSS, hidden HTML, steganographic payloads in images — HTML injections hijack web agents in up to 86% of scenarios), Semantic Manipulation (reasoning: biased framing weaponizing cognitive biases), Cognitive State Traps (memory: RAG poisoning, long-term memory corruption), plus three more not visible in the truncated scrape. High-priority reading for anyone building agents that browse arbitrary web content.

- [AYi](https://x.com/ayi_ainotes/status/2045874192155824616) — 2026-04-20: AYi (translated from Chinese) recaps OpenMythos, an open-source first-principles reconstruction of Anthropic's "Claude Mythos" as a looped/recurrent transformer with MoE routing: the same weights run ~16x per forward pass so reasoning happens silently in latent space. Argues a 770B recurrent model can match a 1.3T standard model and that future scaling competes on loop-count rather than parameter count.

- [Akshay](https://x.com/akshay_pachaar/status/2045404494641733962) — 2026-04-18: Akshay summarizes a UCL paper (arXiv:2604.14228) dissecting Claude Code's architecture: only 1.6% of the codebase is AI decision logic while 98.4% is operational harness (permission gates with 7 modes, tool routing, a 5-layer context compaction pipeline, subagents that return only summaries). Core thesis: as frontier models converge on raw coding ability, harness quality, not the model, becomes the differentiator.

- [Eric Hartford](https://x.com/quixiai/status/2044952124568527298) — 2026-04-18: Eric Hartford releases Clearwing, an MIT-licensed open-source vulnerability-discovery engine that reproduces Anthropic's "Project Glasswing" results with any LLM. His argument: the real innovation isn't the gated Claude Mythos model but the model-agnostic pipeline, rank files by attack surface, fan out hundreds of file-scoped agents, use crash oracles (AddressSanitizer/UBSan) as ground truth, and run a verification agent to filter noise. Reproduced findings with OpenAI Codex 5.4 and a Qwen3.5 finetune.

- [Hamudi](https://x.com/hamudinaanaa/status/2044872907072164304) — 2026-04-17: Hamudi ties into Sequoia's "$1T thesis" that AI sells outcomes (work) rather than software tools, introducing "Outcome Primitives" as a way to measure economic outcomes, citing a published paper tracking 1,300 agents over 21 days that created $32M in value (jobs secured, $200k grants won, e-commerce shops shipped). Framing: copilots compete on software margins and lose to big labs; outcome engines compete on services margins.

- [Yoonho Lee](https://x.com/yoonholeee/status/2044442372864700510) — 2026-04-15: Released code for Meta-Harness — a method to autonomously improve LLM evaluation harnesses on problems humans are actively working on, solving long-horizon credit assignment over code, traces, and scores. Repo at github.com/stanford-iris-lab/meta-harness with ONBOARDING.md for agent-guided setup.

- [Akshay](https://x.com/akshay_pachaar/status/2044329897603244093) — 2026-04-15: Akshay argues agent memory is three-dimensional, needing a relational store for provenance, a vector store for semantics, and a graph store for relationships, because flat vector search misses multi-hop connections (the "bridge" fact that links two entities). He points to Cognee, an open-source project that unifies all three behind four async calls (default embedded SQLite+LanceDB+Kuzu, swappable for Postgres/Qdrant/Neo4j).

- [0xSero](https://x.com/0xsero/status/2044165332928213243) — 2026-04-15: Guide to running large LLMs on limited hardware: use REAPs (50% savings), quantization (AWQ/GPTQ/W4A16/FP8 for fast inference; GGUF/EXL3 for compatibility; MLX for Apple silicon), and 8-bit KV cache (50-75% savings). Practical tips for local AI deployment.

- [kwindla](https://x.com/kwindla/status/2044106314612408437) — 2026-04-15: kwindla introduces Gradient Bang, claimed to be the first massively-multiplayer, fully LLM-driven game: a retro space-trading game (Factorio-like) where you cajole a ship AI into tasking other AIs. Built to explore sub-agent orchestration, partial context sharing across inference loops, long contexts and episodic memory, LLM-generated dynamic UIs, and voice input. Built on pipecat_ai plus Supabase and Vercel, fully open source.

- [How To Prompt](https://x.com/howtoai_/status/2043753502850351525) — 2026-04-14: Hype-framed math claim ('God Particle for calculus'): a paper reportedly shows every elementary function can be generated by one binary operator eml(x,y)=exp(x)-ln(y) plus the constant 1, found by exhaustive search, analogous to the NAND gate. Pitches an AI angle — one uniform trainable circuit instead of juggling math primitives. Interesting if true, but clickbait presentation warrants skepticism.

- [Garry Tan](https://x.com/garrytan/status/2043339811088699446) — 2026-04-12: Garry Tan on open-source agent self-improvement: applied research now happens in the open, and 'just-in-time software' is a new paradigm. Quotes an analysis of the Hermes agent architecture taking a more explicit self-improvement route than typical offline trajectory-mining systems.

- [Nav Toor](https://x.com/heynavtoor/status/2042879339256254689) — 2026-04-11: Covers Kronos, an open-source foundation model for financial markets trained on 12 billion candlestick records from 45 exchanges (Binance, NYSE, NASDAQ, LSE, and more). Claims 93% more accurate than leading time series models, zero-shot across any asset/timeframe. Built at Tsinghua University, accepted at AAAI 2026. Ships in 4 sizes from 4M to 499M params; live BTC demo running. Available on HuggingFace.

- [Veeral Patel](https://x.com/vral/status/2042674854764130549) — 2026-04-10: Quote-tweets Ramp Labs article on "Latent Briefing" — a KV cache compaction technique for efficient memory sharing across multi-agent systems. Patel quips that passing .md files between agents will soon seem as archaic as mailing floppy disks. Paper tackles token inefficiency in hierarchical multi-agent architectures.

- [Santiago](https://x.com/svpino/status/2042275938390639069) — 2026-04-10: Engramme (engramme.com) — a startup building "Large Memory Models," a new architecture designed specifically for how human memory works. Instead of RAG or vector search, it's a different paradigm for memory retrieval. Founded by researchers with 160+ publications in Nature and ICLR who closed their Harvard lab to build this.

- [Sowmay Jain](https://x.com/sowmay_jain/status/2041982135305957425) — 2026-04-08: Describes using an AI agent (@laukiantonson) to fully analyze a 67GB raw genome file for $5 in compute: rented a 32-core/64GB machine, aligned 21M long reads (99.83% mapped), called 5.8M variants, phased maternal/paternal inheritance, annotated against ClinVar/PharmGKB/gnomAD, produced a health risk map across 39 conditions and drug compatibility guide for 41 medications. Striking real-world demonstration of autonomous agentic capability on complex bioinformatics tasks. Went massively viral (909K views).

- [Alex Prompter](https://x.com/alex_prompter/status/2040731938751914065) — 2026-04-06: Google DeepMind published the largest empirical study of AI agent manipulation — 502 participants across 8 countries, 23 attack types tested against GPT-4o, Claude, and Gemini. Found that websites can already detect AI agents and serve them different content, with hidden instructions in HTML, malicious commands in image pixels, and jailbreaks in PDFs. Current defenses fail in predictable, invisible ways.

- [Tom Dörr](https://x.com/tom_doerr/status/2039115357839929610) — 2026-04-01: Shares an open-source AI research agent, Feynman (github.com/getcompanion-ai/feynman) — an autonomous research-assistant agent.

- [sarah guo](https://x.com/saranormous/status/2035080458304987603) — 2026-03-22: Sarah Guo's No Priors podcast episode with Andrej Karpathy covers the phase shift in engineering, AI psychosis, AutoResearch, model speciation, jobs-market data, open vs closed models, autonomous robotics, and agentic education.

- [Avi Chawla](https://x.com/_avichawla/status/2033797863948632384) — 2026-03-17: Avi Chawla explains the SKILLRL paper: rather than stuffing long, noisy raw trajectories into agent memory, it distills experiences into compact, reusable skills the agent retrieves and applies to future tasks — analogous to how humans turn driving experience into transferable instincts.

- [Josh Kale](https://x.com/joshkale/status/2033183463759626261) — 2026-03-16: Karpathy scored every job in America on AI replacement risk, then deleted it. Josh cloned the repo before it went down — 342 occupations scored 0-10 on AI exposure. Average across US economy: 5.3/10. Community note: Karpathy called it a casual 2-hour 'vibe code experiment' and deleted because it was 'wildly misinterpreted.'

- [Huaxiu Yao](https://x.com/huaxiuyaoml/status/2033038170653405308) — 2026-03-15: Huaxiu Yao announces AutoResearchClaw, which automates the full research loop beyond Karpathy's autoresearch experiment loop: one message in, a full conference paper out with real experiments, verified citations, and code. It mines arXiv and Semantic Scholar (50+ papers), has three agents fight over the best hypothesis, writes and self-debugs experiment code, and pivots when results are weak — no human in the loop.

- [kpaxs](https://x.com/kpaxs/status/2032345995095179680) — 2026-03-13: [Login wall — content not extracted. Custom subject suggests a mental model or heuristic worth revisiting.]

- [elvis](https://x.com/omarsar0/status/2031727864199208972) — 2026-03-12: elvis highlights EvoSkill, a self-evolving multi-agent framework that automatically discovers and refines agent skills through iterative failure analysis. Three agents (Executor, Proposer, Skill-Builder) drive the loop, with a Pareto frontier retaining only skills that improve held-out validation while the base model stays frozen. Reported gains: Claude Code w/ Opus 4.5 from 60.6%->67.9% on OfficeQA, +12.1% on SealQA, and +5.3% zero-shot transfer to BrowseComp.

- [kapilansh](https://x.com/kapilansh_twt/status/2031262184442130863) — 2026-03-11: kapilansh argues most devs learning AI only know how to call an API and write a prompt without understanding what happens inside, and recommends Karpathy's 'Neural Networks: Zero to Hero' playlist (micrograd, makemore, attention from scratch, tokenization, training GPT-2) as the genuine fix for that knowledge gap.

- [Daniel Miessler](https://x.com/danielmiessler/status/2030436867745923347) — 2026-03-08: Daniel Miessler flags Karpathy's new self-contained 'autoresearch' repo (nanochat training core stripped to a single-GPU, ~630-line file the human iterates on) as under-appreciated, tying it to the long-discussed goal of automating ML research and predicting it will accelerate progress again.

- [Numman Ali](https://x.com/nummanali/status/2030012892192309461) — 2026-03-07: Numman Ali strongly recommends a deeply technical article, 'Your LLM Doesn't Write Correct Code. It Writes Plausible Code,' praising its articulation of the plausible-vs-correct distinction in LLM output — illustrated by a 100-row primary-key lookup where SQLite takes 0.09ms but an LLM-generated Rust rewrite takes 1,815.43ms.

- [swarit](https://x.com/swaritjoshipura/status/2029219363749020051) — 2026-03-05: Curated links on agent context and evaluation: Foundation Capital on "context graphs" as AIs trillion-dollar opportunity (foundationcapital.com/context-graphs-ais-trillion-dollar-opportunity/), Anthropics guide to demystifying evals for AI agents (anthropic.com/engineering/demystifying-evals-for-ai-agents), a YouTube talk, and resolve.ai.

- [hoeem](https://x.com/hooeem/status/2029167629076676955) — 2026-03-05: A free, beginner-to-expert ranked list of AI learning resources: Anthropic Academy (Claude 101 & AI Fluency), Google AI Essentials, AWS Generative AI Essentials, Elements of AI (University of Helsinki), DeepLearning.AI short courses, and Harvard CS50s Intro to AI with Python.

- [Aarno](https://x.com/theglobalminima/status/2028432457784340950) — 2026-03-03: Suggests software engineers working on agentic AI should study reinforcement learning. As coding agents make custom harnesses/tools easy, the real challenges are behavior control, consistency, memory, and correction — areas where traditional RL on 'agents' intersects fruitfully with LLM agents.

- [tetsuo](https://x.com/tetsuoai/status/2028068322106097773) — 2026-03-02: Technical breakdown of recurring agentic failure modes in fast/distilled code models: wrong direct-exec vs shell selection, structured-output (JSON-only) non-compliance, and tool-result grounding failures (reporting success after a tool error). Fix: distill full agent trajectories (request→tool→output→grounded response), add contrastive near-miss examples, and gate on concrete agentic evals.

- [Sandhya](https://x.com/agenticgirl/status/2028006725538967614) — 2026-03-02: 'BREAKING'-style but substantive thread on LMCache, an open-source KV-cache layer (6.9K stars, used by Google Cloud, CoreWeave, NVIDIA) that makes the LLM KV cache persistent and shareable across engine instances, tiered GPU→DRAM→disk→S3. Enables instant RAG, disaggregated prefill, and context sharing; integrates with vLLM and SGLang. Apache-2.0, pip install lmcache.

- [AVB](https://x.com/neural_avb/status/2027957534159835443) — 2026-03-01: [Post unavailable — page doesn't exist]

- [Sudo su](https://x.com/sudoingx/status/2027264446989848613) — 2026-02-27: Practical steering tips for local coding agents: tell the model its own architecture/constraints (e.g. Qwen3.5 fires 8 of 256 experts/token), give project structure over single prompts, iterate in layers (scaffold → refine → polish), let it debug its own failures, and use long context (262K) to hold the whole project. Notes Claude Code as a solid harness and that llama.cpp merged native Anthropic endpoints (no proxy/LiteLLM). Argues the skill gap in local inference is now the harness and steering, not the models — all on a single RTX 3090.

- [Brian Roemmele](https://x.com/BrianRoemmele/status/2027169646485729698) — 2026-02-27: [Post unavailable — page doesn't exist]

- [Fernando](https://x.com/franc0fernand0/status/2026701684106313791) — 2026-02-27: Fernando summarizes a Microsoft study (Kalliamvakou et al., TSE 2018) on what makes a great manager of software engineers: technical skill is required but not sufficient; what distinguished great managers was availability, granting autonomy, supporting experimentation, and setting clear ways of working.

- [Sukh Sroay](https://x.com/sukh_saroy/status/2026624254800965848) — 2026-02-27: [Post unavailable — account suspended]

- [Ejaaz](https://x.com/cryptopunk7213/status/2025761121328582814) — 2026-02-23: Ejaaz's weekly AI recap: Google shipped Gemini 3.1 (underwhelming to critics) but followed with Lyria 3 song generation and Pomelli one-shot product photoshoots; Microsoft demoed data storage on glass (~10,000-year retention, cheaper than silica); and Taalus fused an AI model directly into silicon at ~17,000 tokens/sec (~17x faster than typical inference).

- [Aakash Gupta](https://x.com/aakashgupta/status/2021709282224587141) — 2026-02-12: Aakash Gupta highlights Andrej Karpathy's 'microgpt': a complete GPT (training loop, inference, optimizer, attention) in 243 lines of Python whose only imports are os, math, random, and argparse, including a hand-rolled ~40-line scalar autograd engine. Frames it as the fifth step in a six-year compression arc: micrograd (2020), minGPT (2020), nanoGPT (2023), llm.c (2024), microgpt (2026).

- [chiefofautism](https://x.com/chiefofautism/status/2019608146692673886) — 2026-02-07: chiefofautism shares Shannon (github.com/KeygraphHQ/shannon), an autonomous white-box AI pentester for web applications.

- [Sumanth](https://x.com/sumanth_077/status/2013232922296561826) — 2026-01-20: Overview of PageIndex, an open-source 'vectorless' RAG framework that drops vector databases and arbitrary chunking. It builds an LLM-optimized hierarchical tree (like a table of contents) and uses reasoning-based tree search to navigate documents the way a human expert would, giving traceable page-level references. Powers Mafin 2.5, which hits 98.7% on FinanceBench. GitHub link in comments.

- [DAIR.AI](https://x.com/dair_ai/status/2012903315890225220) — 2026-01-19: DAIR.AI's Top AI Papers of the Week (Jan 12-18, 2026), heavy on agent memory and self-improvement: (1) Learning Latent Action World Models from in-the-wild video without action labels; (2) DroPE - extending context by dropping positional embeddings with cheap recalibration; (3) Dr. Zero - self-evolving search agents with no training data via proposer/solver loop (HRPO); (4) AgeMem - unified long/short-term memory as tool actions; (5) Focus - bio-inspired active context compression (22.7% token cut on SWE-bench Lite with Claude Haiku 4.5); (6) Agent-as-a-Judge survey; (7) SimpleMem - lifelong memory via semantic compression (30x token reduction); (8) Mistral's Ministral 3 (3B/8B/14B, Apache 2.0); (9) UniversalRAG - modality-aware multimodal RAG routing; (10) MemRL - runtime RL on episodic memory.

- [Justin Mitchel](https://x.com/justinmitchel/status/2001750598329499681) — 2025-12-19: Justin Mitchel flags that pg_textsearch was just open-sourced (github.com/timescale/pg_textsearch), a PostgreSQL extension bringing BM25 relevance-ranked full-text search to your database — meaning teams already on Postgres can skip syncing data to Elasticsearch for keyword search. Post is marked #sponsored.

- [Matt Dancho (Business Science)](https://x.com/mdancho84/status/2000658529753932273) — 2025-12-15: Matt Dancho highlights an open-sourced (free) Python library, 'AI Data Science Team' (github.com/business-science/ai-data-science-team), that automates data-science workflows with AI — data loading, cleaning, exploratory analysis, and feature engineering — tracking each step in a fully reproducible pipeline. Includes a walkthrough video and a free 1-hour agentic AI workshop.

- [Tech with Mak](https://x.com/technmak/status/1998264904563007889) — 2025-12-09: Tech with Mak distills Google's quiet December release of five AI-agent papers published one per day over five consecutive days — more than 250 pages covering how agents should be built, evaluated, secured, and deployed.

- [Rohan Paul](https://x.com/rohanpaul_ai/status/1998262710040228310) — 2025-12-09: Rohan Paul summarizes a paper proposing an 'agentic file system' for context engineering: treat every memory, tool, external source, and human note as a file in a shared space, with a persistent context repository separating raw history, long-term memory, and short-lived scratchpads so the prompt holds only the slice needed now. Every access is logged with timestamps and provenance, and a constructor/updater/evaluator manage context under the model's limited window.

- [Rohan Paul](https://x.com/rohanpaul_ai/status/1997405403987222642) — 2025-12-07: Rohan Paul summarizes Google's guide on context engineering for multi-agent systems (built around ADK). Instead of giant prompts, it compiles a view over state split into Working Context, Session, Memory, and Artifacts; each call rebuilds Working Context from instructions, selected session events, memory results, and artifact references. ADK controls context growth via compaction, filtering, and caching — summarizing old spans, dropping useless events, and reusing a stable prefix — and pushes large payloads out to Artifacts to keep systems fast, affordable, and less hallucination-prone.

- [Ray Fernando](https://x.com/rayfernando1337/status/1980180030971150690) — 2025-10-21: Ray Fernando shares DeepSeek-OCR (github.com/deepseek-ai/DeepSeek-OCR) — DeepSeek's 'Contexts Optical Compression' approach that encodes long text contexts as visual tokens for efficient OCR and document understanding.

- [Vivek Galatage](https://x.com/vivekgalatage/status/1974894313948758373) — 2025-10-07: Vivek Galatage recommends Richard Hipp's 2024 'SQLite: How it works' lecture on database internals from the creator himself, in a thread noting SQLite's ubiquity (including in Chromium browser engines).

- [Sumit Mittal](https://x.com/bigdatasumit/status/1972908540692947192) — 2025-10-01: Sumit Mittal walks through S3/Athena query cost optimization: moving from uncompressed row-based CSV to columnar Parquet with Snappy compression, partitioning by city, and column pruning cuts a $25 full-scan query to about $0.01 (~2500x cheaper). Ends with a course promo.

- [Jamon](https://x.com/jamonholmgren/status/1969883090056249776) — 2025-09-23: Jamon Holmgren strongly recommends Lydia Hallie's article 'Behind The Scenes of Bun Install' as a top-10 must-read for every developer on building performant systems, regardless of whether you use JavaScript or Bun.

- [Philip Vollet](https://x.com/philipvollet/status/1955945448860008655) — 2025-08-15: Announces Elysia, an open-source agentic RAG platform (successor to Verba) built on Weaviate and DSPy. Highlights: transparent decision-tree agents with self-healing and custom tools/branches, pre-query data analysis to avoid blind vector/text search, dynamic result displays, feedback-driven few-shot personalization so smaller models perform like larger ones, and query-time chunk-on-demand. Delivered as a FastAPI+NextJS app and a pip package (elysia-ai).

- [Nick Dobos](https://x.com/nickadobos/status/1930878279290060975) — 2025-06-07: Riffs on a repo (Shubham Saboo's) that stores millions of text chunks inside MP4 video files for fast semantic search, pitched as an open-source replacement for expensive vector databases; Nick Dobos speculates video may be an optimal encoding for AI memory, echoing how human memory leans on vision.

- [Anthropic](https://github.com/anthropics/courses/tree/master/prompt_engineering_interactive_tutorial/Anthropic%201P) — 2025-04-23: Anthropic's official interactive prompt-engineering tutorial (Jupyter notebooks in anthropics/courses): a 9-chapter curriculum on prompt structure, being clear and direct, role prompting, separating data from instructions, output formatting, step-by-step reasoning, few-shot examples, and avoiding hallucinations, plus appendices on prompt chaining, tool use, and search & retrieval.

- [Mervin Praison](https://x.com/mervinpraison/status/1881788246684013011) — 2025-01-22: Shows a 100% local RAG AI agent with reasoning: DeepSeek via Ollama for the LLM, PraisonAI to build the agent in a few lines, Nomic embeddings, and a Streamlit UI—code included in the thread.

- [Santiago](https://x.com/svpino/status/1881336934418755862) — 2025-01-21: Walks through GroundX, an open-source, self-hostable/air-gapped enterprise RAG system. Two services: Ingest (a pretrained vision model that 'understands' documents instead of feeding raw docs to the LLM) and Search (text+vector search with a fine-tuned re-ranker). Santiago's thesis: most teams need better ingestion, not better retrieval; includes a video demo and the free X-Ray inspection tool.

- [Shubham Saboo](https://x.com/saboo_shubham_/status/1849638773136687551) — 2024-10-25: Introduces AutoRAG, an open-source tool that automatically benchmarks multiple RAG strategies to find the optimal RAG pipeline for your data in a few lines of Python.

- [Dominik Tornow](https://x.com/dominiktornow/status/1846507701599433179) — 2024-10-17: Flags a paper as a strong discussion of how hard retries are to get right for reliability under failure—retries are often oversold as a simple fix but are surprisingly complex.

- [Shubham Saboo](https://x.com/saboo_shubham_/status/1818111127286579448) — 2024-07-30: Tutorial for building a no-code RAG chatbot to chat with any GitHub repo, powered by open-source Llama 3.1 405B.

- [Akshay](https://x.com/akshay_pachaar/status/1816088785152848028) — 2024-07-24: A tutorial thread on building a 100% local RAG app using Meta's Llama 3.1.

- [curvedinf](https://github.com/curvedinf/dir-assistant) — 2024-06-18: dir-assistant is a pip-installable CLI that recursively indexes the text files in your directory so you can chat with them via a local or API LLM, auto-injecting the most contextually relevant files. It uses CGRAG (Contextually Guided RAG) for file selection, supports interactive and single-prompt modes (including auto file edits + git commits), many local acceleration backends and all major LLM APIs via LiteLLM, and optimizes prompt/context caching (50-90% cache hits).

- [Santiago](https://x.com/svpino/status/1800151091461652740) — 2024-06-11: A 15-part thread giving an intuitive explanation of matrix multiplication as the crucial idea underlying modern machine learning.

### Industry (95)

- [Aaron Levie](https://x.com/levie/status/2077526010753581156) — 2026-07-16: Aaron Levie's notes from a dinner with enterprise IT leaders on agent adoption: change management is the biggest blocker (processes and data pipelines must be modernized to work with agents), embedding engineers directly into business functions as internal forward-deployed engineers dramatically accelerates successful agent rollouts, and the technical function is becoming more strategically important than ever.

- [0xSero](https://x.com/0xsero/status/2077488957999173936) — 2026-07-16: 0xSero highlights Thinking Machines' launch of Inkling (thinkingmachines.ai/news/introducing-inkling), a 950B-parameter American open-weight model that reasons across text, image, and audio modalities with full weights released. Available for fine-tuning on Thinking Machines' Tinker platform and via the Inkling Playground.

- [How To Prompt](https://x.com/howtoprompt__/status/2076689880026096089) — 2026-07-14: How To Prompt highlights an open-source, privacy-first Chromium fork built by an ex-Google engineer with a native AI agent, built-in MCP server, Cowork-style web+local-file agents, scheduled autopilot tasks, 40+ app integrations (Gmail, Slack, Notion, Linear, Figma, Salesforce), and local-model (Ollama) support — drivable from Claude Code or Gemini CLI. Engagement-framed but describes a real agentic-browser tool worth evaluating.

- [Aaron Levie](https://x.com/levie/status/2073138135014502777) — 2026-07-05: Aaron Levie (Box CEO) argues the battle in AI is shaping up to be a battle for context: agent effectiveness comes down to having the right domain expertise, access to the right context and tools, and being embedded in workflows users can easily review and incorporate. The platforms that capture and leverage the best context within their agents — and pick the right model per task — will be where agents do their best work (coding, legal, support agents at scale). This is why the applied-AI layer is worth far more than being an 'LLM wrapper': the value is in organizing the critical knowledge.

- [ℏεsam](https://x.com/hesamation/status/2073104617706008840) — 2026-07-04: [Jeremy flagged: read for work] hesam recommends Phil Chen's article 'Career advice in the age of AI' (Chen: a researcher from OpenAI, DeepMind, and Stanford). TL;DR: AI makes execution cheaper, so the durable edge is choosing the right problems, building strong connections, and investing real time — the argument being that AI models improve at anything you can write a loss function for, and school is mostly loss functions (well-defined problems graded against known answers), so the valuable work shifts elsewhere.

- [Boris Cherny](https://x.com/bcherny/status/2071379474277613732) — 2026-06-29: As engineering/product/design/DS roles blur, Cherny proposes five team archetypes (not tied to job function): Prototyper, Builder, Sweeper, Grower, Maintainer. Healthy teams need different mixes by product maturity — pre-PMF wants 1+2+3, growing wants 2+3+4+some 5, strong-PMF wants 3+4+5+some 2.

- [Brian Armstrong](https://x.com/brian_armstrong/status/2070670644577280109) — 2026-06-27: Coinbase's playbook for keeping AI spend flat while token usage grows: better defaults (experimenting with cheaper open-weight models like GLM 5.2 / Kimi 2.7 via an LLM gateway, since 91% never hit caps), better routing (frontier for planning, cheaper for execution), better caching (LibreChat cache-hit rate 5% → 60%), lean context, and usage visibility. Cut AI spend nearly in half while token usage kept growing.

- [Hugging Models](https://x.com/huggingmodels/status/2069750892287721960) — 2026-06-25: Brief hype post: NVIDIA released an FP4 quantized MoE version of Qwen3.6 that fits in 35B parameters but runs with the efficiency of a ~3B model, pitched as a win for efficient inference.

- [Mario Zechner](https://x.com/badlogicgames/status/2069156188902559751) — 2026-06-23: Mario Zechner recommends a video dissecting Voxtral, a family of open-source speech models, and the foundational work behind it (audio tokenization, semantic/acoustic disaggregation). He quote-tweets Julia Turc, who frames it as what you get when you plug LLMs into voice assistants instead of a decade of handwritten rules.

- [Dhilip Subramanian](https://x.com/sdhilip/status/2069140867466797200) — 2026-06-23: Dhilip Subramanian, a heavy dictation user (44,414 words via Wispr Flow), recommends FluidVoice: a free, open-source, locally-run macOS voice-to-text tool that needs no API key and handles slang well. He cancelled his paid plan after switching.

- [Sakana AI](https://x.com/sakanaailabs/status/2068862070062485867) — 2026-06-23: Sakana AI announces Fugu, an orchestration model that routes across a swappable pool of underlying agents rather than relying on one monolithic model. Their blog argues orchestration is the next frontier and a hedge for AI sovereignty against vendor export controls; Fugu reportedly matches leading models (Fable, Mythos) on engineering, science, and reasoning benchmarks.

- [Ahmad](https://x.com/theahmadosman/status/2066825976705646929) — 2026-06-17: Ahmad highlights VibeThinker 3B (built on Qwen 2.5), a 3B-parameter model he claims reaches Opus 4.5-level performance, quoting his own earlier prediction that Claude Code + Opus 4.5-quality models will run locally on a single RTX PRO 6000 before year-end. A signal on how fast small/efficient local models are closing the gap with frontier models.

- [Marie Haynes](https://x.com/marie_haynes/status/2065531158356717721) — 2026-06-13: Flags Google's new Open Knowledge Format (OKF): a standardized way to store information as a directory of interlinked markdown files that acts as a living wiki agents can query and edit, which the author thinks could replace Notion or Obsidian. References Google Cloud's blog post and the spec at github.com/GoogleCloudPlatform/knowledge-catalog (okf/SPEC.md), and notes feeding both links to Antigravity to brainstorm project uses.

- [Rahul](https://x.com/sairahul1/status/2063544956158185927) — 2026-06-08: Long-form X article framing 'Harness Engineering' as the most important AI discipline of 2026 — OpenAI shipped 1M lines of production code in Feb 2026 using agents wrapped in a reliable system (the 'harness'); Anthropic published 3 papers on it; ThoughtWorks formalized a framework; Philipp Schmid called it the most important discipline of 2026. Article walks through what a harness is and the mental models needed to actually use it. 1.1M views — the term is breaking out of AI-infra circles fast.

- [Garry Tan](https://x.com/garrytan/status/2061878212213572083) — 2026-06-03: Garry Tan on model routing as strategy: frontier labs will want their harness to be the moat, but the consumer-best outcome is model capabilities flattening and commoditizing — 'a preview of the AI Harness Wars of 2027.' Cites Factory's auto model-router (claimed 25% cost cut at frontier performance).

- [Atenov int.](https://x.com/atenov_d/status/2058868770257416239) — 2026-05-25: Highlights MoneyPrinterTurbo (13k+ stars): give a topic/keyword and it generates a script (via any LLM), pulls copyright-free footage, and adds subtitles/music/voiceover to output a finished short video; runs locally with Web UI/API/Docker/Colab. (Author's other posts are off-topic trading/politics.)

- [Garry Tan](https://x.com/garrytan/status/2058378310254793013) — 2026-05-25: Garry Tan: fine-tuned his own Qwen3.5-397B in a couple hours via Thinking Machines, arguing fast usable multimodal will enable mind-blowing personal AI. Cites Thinking Machines' real-time 'interaction models.'

- [shdu](https://x.com/shdu11546816/status/2057642195524419748) — 2026-05-22: Macro speculation that AI triggers a 'Deflationary Doom Loop' via the Paradox of Thrift: agent-driven layoffs push white-collar workers into physical-labor markets, wages crash, and discretionary spending collapses because intelligence isn't the bottleneck for land, energy, and calories. A pessimistic counter to 'everything becomes cheap and abundant.'

- [Dan Shipper](https://x.com/danshipper/status/2057514494960513272) — 2026-05-22: Dan Shipper: Every automated everything it could with AI agents, yet has more human work than ever, growing 4→30 employees since GPT-3. His report 'After Automation' argues AI makes expert competence cheap, which raises demand for experts, and the dynamic intensifies toward AGI.

- [Aaron Levie](https://x.com/levie/status/2057315272156135501) — 2026-05-22: Aaron Levie on why Forward Deployed Engineers (FDEs) will persist: unlike cloud (concentrated users, little workflow change, slow enough for best practices to spread), agents are highly technical to deploy AND directly change users' workflows, and the fast model-change cadence keeps resetting best practices — so vendors/partners who've done it hundreds of times do the work. A great early-career path.

- [James Cogan](https://x.com/cogan/status/2056702063992607071) — 2026-05-22: A thoughtful essay, 'Machine Time,' arguing AI compresses the unit of meaningful time — shrinking the buffer between noticing a change and having to respond. AI compresses the front end of cognitive work, so the bottleneck moves to human review, judgment, and taste; the danger isn't speed but speed without scaffolding, and institutions increasingly answer with machine-speed coordination rather than restoring the human clock.

- [Tom Blomfield](https://x.com/t_blom/status/2056909934156280088) — 2026-05-20: Tom Blomfield breaks down what YC is seeing in recursively self-improving companies — creating recursive self-improving AI loops so founders 'run companies that improve while they sleep.'

- [Linas Beliūnas](https://x.com/linasbeliunas/status/2056679329484927356) — 2026-05-20: Summarizes Anthropic's free AI-native founder playbook: build AROUND Claude across Idea → MVP → Launch → Scale (pressure-test the idea, Claude Code builds the product, Claude Cowork handles ops, Claude turns knowledge into compounding context). 'AI compresses execution but not judgment' — the edge becomes knowing what NOT to build; best AI-native startups have the best AI operating systems, not the biggest teams.

- [Sapient Intelligence](https://x.com/sapient_int/status/2056510383935172798) — 2026-05-19: Sapient Intelligence introduces HRM-Text, an ultra-lean 1B-parameter reasoning model trained on just 40B structured tokens (~1/1000 the data of comparable models), with the full model training in ~one day on a $1,000 budget — pitched as making previously-too-expensive research concepts testable again.

- [Erik Townsend](https://x.com/erikstownsend/status/2055444404337582106) — 2026-05-16: Erik Townsend flags ex-Goldman commodities chief Jeff Currie's thread calling AI's physical inputs (energy/commodities) 'the most asymmetric trade in modern financial history' — capital chased the AI software trade while ignoring the physical assets AI needs to run.

- [Khairallah AL-Awady](https://x.com/eng_khairallah1/status/2055215784092401966) — 2026-05-15: Thread about Anthropic's May 6, 2026 multi-agent orchestration announcement (Code with Claude event): Claude Managed Agents can now run up to 20 specialized agents in parallel on a single task. Cites Netflix (parallel build-log analysis), Harvey (multi-document legal coordination), and Shopify (pushing toward 90% autonomous coding by Q3 2026) as production users. Good signal that parallel sub-agent orchestration is going mainstream.

- [CyrilXBT](https://x.com/cyrilxbt/status/2055183411619549265) — 2026-05-15: ALL-CAPS engagement-farming thread announcing GitHub's new official certification GH-600 "Agentic AI Developer" — framed as the first formal credential for engineers who operate, supervise, and integrate AI agent teams across the SDLC. Worth knowing the cert exists; treat the framing as hype.

- [Guri Singh](https://x.com/heygurisingh/status/2054405672176091449) — 2026-05-14: Listicle of 10 side-hustle / digital-product sites (Carrd, Gumroad, Systeme.io, Payhip, Ko-fi, Sellfy, …) framed as 'print money while you sleep'. Off-topic for the AI collection and engagement-farmed; flagging as questionable.

- [송준 Jun Song](https://x.com/jun_song/status/2054379887608402199) — 2026-05-14: Claims that within weeks, a Minimax-M3.0-JANGTQ-CRACK release from @dealignai will bring Opus-4.6-tier local inference to 128GB Macs, with open-source quantization efforts targeting 24GB VRAM. Bullish on where local LLMs land in mid-2026.

- [Jamie Signorile](https://x.com/sigsnyc/status/2054238175758111156) — 2026-05-14: Frames AI as widening the gap between strong and average employees in enterprise GTM roles rather than uplifting everyone. Author uses a two-axis hiring framework (technical capability x business savvy) drawn from a decade at Addepar and KizenTech and argues AI inverts how operators get evaluated.

- [ericosiu](https://x.com/ericosiu/status/2054413343776223393) — 2026-05-13: ericosiu hiring forward-deployed engineers globally. Quotes Aaron Levie noting FDEs (or equivalent) are about to become one of the most in-demand jobs in tech for AI rollouts. References a "beat AI" challenge in his profile as their filter. Subject flagged "worth an extra look".

- [IndieDevHailey (开发者Hailey)](https://x.com/indiedevhailey/status/2054386235867812240) — 2026-05-13: GitHub project RuView (50K+ stars) — uses WiFi CSI signals plus AI to detect humans behind walls without cameras. Pose detection (17 keypoints), breathing/heart rate while sleeping, fall alerts. Runs locally on ESP32; no video, no cloud, privacy-preserving. Translated from Chinese.

- [Founder Thoughts & Strategies](https://x.com/mogulinfluence/status/2054274159706853837) — 2026-05-13: Quote of Tom Verrilli (Whatnot) article on building product teams in the AI era — 31,832 people applied to be a PM at Whatnot in two years, only one hired. Framing: best product teams will ship 10x faster post-AI. Subject flagged "have a look".

- [GREG ISENBERG](https://x.com/gregisenberg/status/2054261832718889216) — 2026-05-13: Free 47-minute course on building a managed AI-agent business solo. Pitch: sell "unlimited agents/infrastructure" as digital employees, don't niche too early, every executive has the same problems (emails, meetings, follow-ups). Stack: Hermes Agent (harness), Codex or Claude Code (build), Orgo (cloud computer sandboxes per agent), Composio (one-click auth), Obsidian (docs).

- [コムテ (Komte)](https://x.com/commte/status/2054136870016356408) — 2026-05-13: Google open-sourced 13 official Agent Skills (github.com/google/skills) compliant with the Agent Skills standard — interoperable with Claude Code, Antigravity, Gemini CLI, Cursor, GitHub Copilot, and other major agents. Significant cross-vendor signal for the Agent Skills standard.

- [Rahul](https://x.com/sairahul1/status/2054171777119801764) — 2026-05-12: Hypes a 22-minute Anthropic talk on production AI agents covering tool orchestration, memory systems, observability, long-running agents, and production infrastructure. Pitches a personal "How to Become an AI Agent Engineer in 2026" roadmap pushing back on CrewAI-by-default and framework chasing.

- [Muhammad Ayan](https://x.com/socialwithaayan/status/2053875867487777175) — 2026-05-12: Engagement-farmed announcement (all-caps 'BREAKING') that Anthropic open-sourced a Claude Code plugin suite for finance workflows — DCF/LBO models, equity research, M&A analysis, KYC, IC memos — with MCP connectors for Bloomberg, FactSet, S&P Global, Morningstar, and PitchBook (github.com/anthropics/financial-services, Apache-2.0, ~19.8K stars). Top replies flag the obvious caveat: the harness is free but the data feeds (Bloomberg Terminal ~$28K/yr, FactSet/S&P/PitchBook six-figure) are not, and the agents draft work for human sign-off rather than autonomously owning workflows.

- [Himanshu Kumar](https://x.com/codewithimanshu/status/2052573291131589101) — 2026-05-08: Engagement-heavy framing around a free MIT lecture from Jim Simons on quant trading math. Claims Renaissance Technologies-style pattern recognition is now buildable in a weekend with Claude Code (no team of 50 PhDs needed). Hype style; the lecture link itself is the real reference.

- [divyansh tiwari](https://x.com/divyansht91162/status/2052474052841984110) — 2026-05-08: TinyFish drops web search to $0 for AI agents. divyansh switched OpenClaw and Hermes agents to it and reports they can now browse, research, and retrieve live info at scale for free — a real shift in agent-cost economics if it holds up.

- [Mgoes](https://x.com/m_goes_distance/status/2052433497575293307) — 2026-05-08: Biotech-progress digest for 2026 — Japan endorsing iPS cell therapies for heart failure / Parkinson's, Altos Labs' Atlas of Rejuvenation, rapalink-1 as longevity drug, Retro Biosciences dosing brain-cleanup pill, peptides moving from banned to federal policy, psychedelics executive order, GLP-1s at 12.4% adult adoption. Off-topic for the AI links collection but Jeremy emailed it, so capturing it honestly.

- [Allen Braden](https://x.com/allen_explains/status/2052340555942924368) — 2026-05-08: Allen Braden points to a free 1-hour UC Berkeley lecture on systematic-trading fundamentals (the math Jane Street quants use). Engagement-style framing without the actual lecture link — finding it requires follow-through outside the post.

- [Uncle Bob Martin](https://x.com/unclebobmartin/status/2052370749701214226) — 2026-05-07: Uncle Bob Martin: 'It's not wrong. It just shows that driving an AI is a form of engineering that is not for the faint of heart.' The post he was reacting to is now from a suspended account, so the original content is lost — Uncle Bob's framing is all that remains. 130.6K views suggests it resonated.

- [Adam Ghowiba](https://x.com/adamghowiba/status/2050886233921061281) — 2026-05-05: JP Morgan's investment research team broke down their "Ask David" multi-agent architecture: a supervisor agent orchestrates specialized subagents (retrieval, structured data, analytics), with an LLM-as-judge reflection node before the answer ships and human-in-the-loop for the last accuracy gap. Same supervisor + specialist + reflection pattern showing up everywhere.

- [Keith Rabois](https://x.com/rabois/status/2050250243552239956) — 2026-05-02: Rabois (one-word 'Useful.') endorsing Ann Miura-Ko's piece arguing most scaled companies (e.g. Ramp, 1500-person org) are still Level 1 on AI adoption despite the 'AI-pilled' narrative — based on her recent office visits.

- [Allen Braden](https://x.com/allen_explains/status/2050163013165224332) — 2026-05-01: Engagement-farming claim that a 'junior at Jane Street' landed $220K-600K by using AI on trillions of data points. Community Note corrects: it's actually a 2024 Horace He talk on ML systems infra at Jane Street — he was a guest speaker, not an employee, and it has nothing to do with AI for trading.

- [Qwen](https://x.com/alibaba_qwen/status/2049861145574690992) — 2026-05-01: Alibaba Qwen team open-sources Qwen-Scope, a suite of sparse autoencoders (SAEs) for the Qwen model family. Surfaces interpretable internal features for steering inference, classifying/synthesizing data, debugging code-switching/repetition at the source, and selecting smarter benchmarks. Blog at qwen.ai/blog?id=qwen-scope, weights on HuggingFace.

- [StacyOnChain](https://x.com/stacyonchain/status/2047278412922831260) — 2026-04-23: Off-topic for AI links — promotional content for centpro.bot (Polymarket trading framework supposedly extracted from 327 real tests). ALL-CAPS engagement framing, crypto-twitter signal. Capturing for completeness but not useful as AI/agents reference.

- [Alex Volkov](https://x.com/altryne/status/2046977133013311814) — 2026-04-23: OpenAI open-sourced Privacy Filter — a 1.5B-param (50M active) PII detection model on HuggingFace under Apache 2.0. Not a new general LLM; a focused safety-utility model for detecting private info in text. Volkov calls it interesting; useful as a building block in agent pipelines that touch user data.

- [Aakash Gupta](https://x.com/aakashgupta/status/2046371351016161745) — 2026-04-21: Long analysis of Yann LeCun's post-Meta 'LeWorldModel' JEPA result: first JEPA that trains end-to-end from raw pixels (15M params, single GPU, hours), replacing a pile of collapse-prevention heuristics with one Gaussian-normality regularizer (hyperparam search O(n^6)->O(log n)). Claims 200x fewer tokens/observation than DINO-WM and planning 47s->0.98s/cycle — a potential reset of the humanoid-robotics cost structure, framed as Meta's Xerox-PARC moment.

- [Kevin Simback](https://x.com/ksimback/status/2045120939680038923) — 2026-04-18: Kevin Simback shares his article "The AI Agent Moat Is Real, but Narrower Than You Think," arguing that the durable moat in the agent space isn't the harness itself but lies elsewhere, after going deep on where to invest and build in the agent space.

- [PolyArb](https://x.com/usepolyarb/status/2045109166599963026) — 2026-04-18: [Post unavailable — page doesn't exist]

- [Eric Hartford](https://x.com/quixiai/status/2044952124568527298) — 2026-04-18: Eric Hartford releases Clearwing, an MIT-licensed open-source vulnerability-discovery engine that reproduces Anthropic's "Project Glasswing" results with any LLM. His argument: the real innovation isn't the gated Claude Mythos model but the model-agnostic pipeline, rank files by attack surface, fan out hundreds of file-scoped agents, use crash oracles (AddressSanitizer/UBSan) as ground truth, and run a verification agent to filter noise. Reproduced findings with OpenAI Codex 5.4 and a Qwen3.5 finetune.

- [Hamudi](https://x.com/hamudinaanaa/status/2044872907072164304) — 2026-04-17: Hamudi ties into Sequoia's "$1T thesis" that AI sells outcomes (work) rather than software tools, introducing "Outcome Primitives" as a way to measure economic outcomes, citing a published paper tracking 1,300 agents over 21 days that created $32M in value (jobs secured, $200k grants won, e-commerce shops shipped). Framing: copilots compete on software margins and lose to big labs; outcome engines compete on services margins.

- [Garry Tan](https://x.com/garrytan/status/2044059516497711522) — 2026-04-15: Garry Tan amplifies Alfred Lin's article 'Heat Seeking Missile for Pain': the realest founders actively hunt the hairiest, gnarliest problems and surgically destroy them, citing an interview with Keller of Zipline.

- [Alex Vacca](https://x.com/itsalexvacca/status/2043834187095150673) — 2026-04-14: Growth/marketing content (mostly off the AI/dev core): endorses Michel Lieben's article on running a 4-layer funnel instead of a bare 'book a call', citing a $7M-ARR bootstrapped funnel (330k visitors, 1,500+ meetings, $4M new ARR). Relevant only as go-to-market reading.

- [am.will](https://x.com/llmjunky/status/2043817254152814785) — 2026-04-14: How to get free NVIDIA API credits for open-source models via the OpenAI-compatible endpoint integrate.api.nvidia.com/v1 (Minimax 2.7, Qwen 3.5, GLM 5, Gemma, Nemotron). Won't match Opus-tier, but the author rates Minimax M2.7's 'personality' highly; includes a paste-ready client config block. Useful for cheap/free local-agent experimentation.

- [North@CreaoAI](https://x.com/anorth_chen/status/2043694726764003817) — 2026-04-14: Endorses (translated from Chinese) an 'AI-First' engineering essay by the author's CTO: after going AI-first, the team merges/deploys 20+ PRs daily with ~99% of production code written by AI, shipping and A/B-killing features within a day. Argument: teams stuck in 'AI-assisted' rather than 'AI-first' mode risk fading from the market within a year. Provocative management/strategy read.

- [Garry Tan](https://x.com/garrytan/status/2043339811088699446) — 2026-04-12: Garry Tan on open-source agent self-improvement: applied research now happens in the open, and 'just-in-time software' is a new paradigm. Quotes an analysis of the Hermes agent architecture taking a more explicit self-improvement route than typical offline trajectory-mining systems.

- [Nav Toor](https://x.com/heynavtoor/status/2042879339256254689) — 2026-04-11: Covers Kronos, an open-source foundation model for financial markets trained on 12 billion candlestick records from 45 exchanges (Binance, NYSE, NASDAQ, LSE, and more). Claims 93% more accurate than leading time series models, zero-shot across any asset/timeframe. Built at Tsinghua University, accepted at AAAI 2026. Ships in 4 sizes from 4M to 499M params; live BTC demo running. Available on HuggingFace.

- [Santiago](https://x.com/svpino/status/2042275938390639069) — 2026-04-10: Engramme (engramme.com) — a startup building "Large Memory Models," a new architecture designed specifically for how human memory works. Instead of RAG or vector search, it's a different paradigm for memory retrieval. Founded by researchers with 160+ publications in Nature and ICLR who closed their Harvard lab to build this.

- [carsonfarmer](https://x.com/carsonfarmer/status/2042038527639068763) — 2026-04-09: Points out that Anthropic's new managed agents API closely mirrors the Letta/MemGPT API that's been open-source for a year — including read-only memory blocks and memory block sharing. Quoting Sarah Wooders (Letta co-creator) who calls it closed-source with provider lock-in.

- [Ksenia Se](https://x.com/theturingpost/status/2041455210342871094) — 2026-04-08: Ksenia from TuringPost on the enterprise AI adoption gap: despite SF hype, most companies are still at ChatGPT-for-writing stage. AI adoption isn't a straight line but a stack of dependencies — you can't jump to agents if workflows aren't legible, can't act on data you don't trust. Most AI pilots fail because organizational readiness, not the technology, is the bottleneck.

- [Factory](https://x.com/factoryai/status/2036184745059688923) — 2026-03-24: Factory launches "Missions" — long-running agentic workflows now available to all users, built to automate large software tasks like app development from scratch, codebases migrations, and AI research. Strong signal that autonomous multi-step coding agents are going mainstream.

- [sarah guo](https://x.com/saranormous/status/2035080458304987603) — 2026-03-22: Sarah Guo's No Priors podcast episode with Andrej Karpathy covers the phase shift in engineering, AI psychosis, AutoResearch, model speciation, jobs-market data, open vs closed models, autonomous robotics, and agentic education.

- [felpix](https://x.com/felpix_/status/2033249213614538804) — 2026-03-21: felpix reports filing taxes end-to-end with Claude + FreeTaxUSA: dropped a W-2, several 1099-NECs and 1099-Bs plus expense/budget spreadsheets in a folder, asked Claude to itemize and optimize expenses, and let it use Chrome to submit — the return was accepted. (Directly relevant: FreeTaxUSA is TaxHawk's own product.)

- [unusual_whales](https://x.com/unusual_whales/status/2033965177918620008) — 2026-03-18: Unusual Whales launched an MCP server that streams live, structured market data to any AI on demand — options flow, dark pools, congressional trades, full financials, technicals, 13Fs, insider activity, and Polymarket data — for building trading bots, dashboards, and screeners (unusualwhales.com/public-api/mcp). 'BREAKING' engagement framing.

- [zostaff](https://x.com/zostaff/status/2033930728044372275) — 2026-03-18: zostaff's clickbait-titled ('How to Quit Your Job in One Day') walkthrough of an autonomous Polymarket trading system built from three agents: Claude (strategist — probability/recommendation/confidence), Codex (engineer — writes and debugs bot code), and OpenClaw (orchestrator — persistent memory, cron, modular skills, Telegram interface that executes trades and logs everything).

- [Akhilesh Mishra](https://x.com/livingdevops/status/2033845127244825041) — 2026-03-17: Akhilesh Mishra reports NVIDIA open-sourced OpenShell at GTC — an infrastructure-layer sandbox/guardrail for coding agents: filesystem locked at sandbox creation, network blocked by default with whitelisting, API keys injected only at runtime (never on disk), policies in simple YAML, running a full K3s cluster inside a single Docker container. One command sandboxes Claude Code, Codex, or Cursor; Adobe, Atlassian, Cisco, CrowdStrike, and Salesforce are integrating it.

- [Josh Kale](https://x.com/joshkale/status/2033183463759626261) — 2026-03-16: Karpathy scored every job in America on AI replacement risk, then deleted it. Josh cloned the repo before it went down — 342 occupations scored 0-10 on AI exposure. Average across US economy: 5.3/10. Community note: Karpathy called it a casual 2-hour 'vibe code experiment' and deleted because it was 'wildly misinterpreted.'

- [Suhail Gupta](https://x.com/audiinidesign/status/2031213732941230240) — 2026-03-10: Suhail Gupta endorses Harrison Chase's article 'How Coding Agents Are Reshaping Engineering, Product and Design,' agreeing the EPD blur toward functional software over separate roles will only become more visible and obvious in the coming months.

- [Anish Moonka](https://x.com/anisha_moonka/status/2030015356383691121) — 2026-03-07: Anish Moonka's 12-point notes from Boris Cherny (Head of Claude Code) on Lenny's Podcast: coding is largely solved (Boris ships 10-30 PRs/day, no hand-written code since Nov 2025); the next frontier is AI deciding what to build; productivity per Anthropic engineer is up 200%; underfund teams on purpose; give engineers unlimited tokens; the Bitter Lesson favors general models over rigid orchestration; build for the model six months out; latent demand is the best product signal; 'software engineer' is becoming 'builder'; mechanistic interpretability enables layered safety; and 70% of engineers/PMs enjoy their jobs more now.

- [Jamie Quint](https://x.com/jamiequint/status/2029951631534739951) — 2026-03-07: Jamie Quint (built Notion's early data stack in 2020) shares his article 'How to Build a Data Agent in 2026,' claiming the approach can cut a company's projected data-team headcount by ~80% this year.

- [John Rush](https://x.com/johnrushx/status/2029406051716743354) — 2026-03-05: Opinion piece: AI does not make work easier — it strips away the easy 99% of jobs so everyone now competes on the hard 1%, raising cognitive load and stress sharply. A take on how AI reshapes knowledge work.

- [0xSero](https://x.com/0xsero/status/2029305128084218265) — 2026-03-05: Argues real-time, very fast inference (e.g. models served by Cerebras, used via "Spark") is a major shift that requires changing your working strategy, pointing to companion articles for details.

- [Tech Layoff Tracker](https://x.com/techlayofflover/status/2029261882834501665) — 2026-03-05: Shares a venting DM from a senior Big Tech SWE (~$350k TC): leadership now touts an "AI leverage ratio" of 4.2x — each engineer shipping the output of a former four-person team — fueling job anxiety. Engagement-styled but a real signal on AI-driven productivity expectations and layoffs.

- [Peter Yang](https://x.com/petergyang/status/2029220235375714766) — 2026-03-05: Deep dive arguing your new job is to onboard and manage AI agents, with examples from Linear (AI team members you assign tasks to), Ramp (Claude Code as baseline for all roles), and Factory (codifying PM, frontend, and data-analysis work into reusable skills).

- [swarit](https://x.com/swaritjoshipura/status/2029219363749020051) — 2026-03-05: Curated links on agent context and evaluation: Foundation Capital on "context graphs" as AIs trillion-dollar opportunity (foundationcapital.com/context-graphs-ais-trillion-dollar-opportunity/), Anthropics guide to demystifying evals for AI agents (anthropic.com/engineering/demystifying-evals-for-ai-agents), a YouTube talk, and resolve.ai.

- [Dan Robinson](https://x.com/danlovesproofs/status/2028890694837039202) — 2026-03-05: Argues issue tracking/backlogs are dying: forward-thinking AI-augmented teams skip Linear/tickets entirely because the cost to fix an issue now approaches the cost to understand it. Works for small, flat, high-context teams with strong dev infra; framed as part of the 'death of midwit software engineering.'

- [David Byttow](https://x.com/davidbyttow/status/2028233578329600449) — 2026-03-02: Essay arguing AI agents are collapsing the coordination layer of organizations. As execution and coordination costs approach zero, the remaining scarce skill is goal clarity, taste, and ownership. Warns bad judgment now scales faster — strategic mistakes show up as fast delivery of the wrong thing.

- [Sandhya](https://x.com/agenticgirl/status/2028006725538967614) — 2026-03-02: 'BREAKING'-style but substantive thread on LMCache, an open-source KV-cache layer (6.9K stars, used by Google Cloud, CoreWeave, NVIDIA) that makes the LLM KV cache persistent and shareable across engine instances, tiered GPU→DRAM→disk→S3. Enables instant RAG, disaggregated prefill, and context sharing; integrates with vLLM and SGLang. Apache-2.0, pip install lmcache.

- [SightBringer](https://x.com/_the_prophet__/status/2027235489930191056) — 2026-02-27: Critique of AI auto-memory (quote-tweeting Anthropic's Claude auto-memory announcement) as a "power grab disguised as convenience": capturing your patterns, defaults, and definitions of 'good' shifts the model from serving you to shaping you, and dependency is the business model. Counter-playbook: treat memory as a controlled instrument — scope it like permissions, separate persona from operations, keep a purge cycle, audit what the model believes about you, and never let it silently rewrite your intent. Frames the AI era as shifting from intelligence to custody of context/continuity.

- [Brian Roemmele](https://x.com/BrianRoemmele/status/2027169646485729698) — 2026-02-27: [Post unavailable — page doesn't exist]

- [Aakash Gupta](https://x.com/aakashgupta/status/2026367615602667784) — 2026-02-25: Aakash Gupta, building on a Karpathy quote, argues agents are the new distribution channel for software: they call CLIs and MCP servers and read docs programmatically rather than browsing marketing sites. MCP hit 97M monthly SDK downloads and 10k+ servers in a year and was donated to the Linux Foundation. Winners of the next 24 months build agent-accessible surface area (CLIs, MCP endpoints, machine-readable docs) now.

- [Ejaaz](https://x.com/cryptopunk7213/status/2025761121328582814) — 2026-02-23: Ejaaz's weekly AI recap: Google shipped Gemini 3.1 (underwhelming to critics) but followed with Lyria 3 song generation and Pomelli one-shot product photoshoots; Microsoft demoed data storage on glass (~10,000-year retention, cheaper than silica); and Taalus fused an AI model directly into silicon at ~17,000 tokens/sec (~17x faster than typical inference).

- [Dr Milan Milanovic](https://x.com/milan_milanovic/status/2023381859489767772) — 2026-02-17: Milan Milanovic's thesis: AI won't replace developers so much as the software-development process we're used to. Code is becoming cheap while decisions become expensive; AI reduces typing, not thinking. Developers who only implement tasks will struggle, while those who understand the product, domain, and system architecture will thrive.

- [dax](https://x.com/thdxr/status/2022574719694758147) — 2026-02-14: dax (thdxr) offers a contrarian take on AI coding hype: orgs are rarely bottlenecked by code-production ability. Most workers use AI to do their tasks with less effort rather than to become 10x; the few who genuinely push are getting buried under everyone else's 'slop code' and may quit; teams remain bottlenecked by bureaucracy; and CFOs are noticing each engineer now costs ~$2,000/month more in LLM bills.

- [Machina](https://x.com/exm7777/status/2019787951530725396) — 2026-02-07: Machina's thread on how to stop feeling behind in AI: the relentless cadence of releases (GPT-5.3 Codex, Opus 4.6, Kling 3.0, all 'redefining everything') creates a low-grade, never-ending pressure. His reframe is that the problem isn't too much happening, it's the lack of a personal filter for what actually matters to your work.

- [James Cowling](https://x.com/jamesacowling/status/2011924122922852599) — 2026-01-16: James Cowling points to the Software Crisis of the 1960s-70s (en.wikipedia.org/wiki/Software_crisis) as a warning: productivity ground to a halt until good abstractions for managing software complexity emerged. His thesis is that without good platforms, the same stall will happen again in the AI-coding era.

- [SightBringer](https://x.com/_the_prophet__/status/2004796159299084424) — 2025-12-27: An essay arguing software engineering is undergoing a 'phase transition' in human leverage: for decades leverage came from writing more correct instructions faster, but the unit of leverage has shifted from writing code to orchestrating intelligence. The programmer becomes a systems integrator of probabilistic entities whose reasoning can't be fully inspected or controlled — which the author says explains why even Karpathy feels 'behind.'

- [Kermit](https://x.com/fixer9999/status/2000332286055850464) — 2025-12-14: A bare link post sharing Perplexity's 'Perplexity at Work' PDF report (r2cdn.perplexity.ai/pdf/pplx-at-work.pdf) — Perplexity's enterprise/workplace positioning material. Low engagement; minimal commentary.

- [AWS Containers](https://github.com/aws-containers/reinvent) — 2025-12-01: The aws-containers/reinvent GitHub repo collects AWS re:Invent 2025 Kubernetes Track assets — slides, the latest EKS launches, and demos from the sessions. A reference for what AWS shipped for Kubernetes/EKS at re:Invent 2025.

- [Aadit Sheth](https://x.com/aaditsh/status/1983103310791159863) — 2025-10-31: Aadit Sheth shares a chart breaking down what being 'good with AI' looks like role by role, framed as a way to gauge whether a team is truly AI-fluent and pitched as useful for hiring and leading in 2025. The breakdown itself is in an attached chart image.

- [Ray Fernando](https://x.com/rayfernando1337/status/1980180030971150690) — 2025-10-21: Ray Fernando shares DeepSeek-OCR (github.com/deepseek-ai/DeepSeek-OCR) — DeepSeek's 'Contexts Optical Compression' approach that encodes long text contexts as visual tokens for efficient OCR and document understanding.

- [Arthur MacWaters](https://x.com/arthurmacwaters/status/1957580001433514167) — 2025-08-19: Endorses a referenced approach as 'unironically the right way to build a startup.' The substantive content is in the quoted/referenced post rather than the one-line commentary.

- [Santiago](https://x.com/svpino/status/1881336934418755862) — 2025-01-21: Walks through GroundX, an open-source, self-hostable/air-gapped enterprise RAG system. Two services: Ingest (a pretrained vision model that 'understands' documents instead of feeding raw docs to the LLM) and Search (text+vector search with a fine-tuned re-ranker). Santiago's thesis: most teams need better ingestion, not better retrieval; includes a video demo and the free X-Ray inspection tool.

### Management (106)

- [Aaron Levie](https://x.com/levie/status/2077526010753581156) — 2026-07-16: Aaron Levie's notes from a dinner with enterprise IT leaders on agent adoption: change management is the biggest blocker (processes and data pipelines must be modernized to work with agents), embedding engineers directly into business functions as internal forward-deployed engineers dramatically accelerates successful agent rollouts, and the technical function is becoming more strategically important than ever.

- [Ryan Carson](https://x.com/ryancarson/status/2074093250399330418) — 2026-07-07: Ryan Carson (@HelloUntangle) details orchestrating the largest/riskiest engineering program in the company's history with a single Fable parent orchestrator session: 834 files, prod data mutation, DB schema update, 31 PRs, started Friday->completed Monday, zero prod incidents. One parent Devin/Fable session planned the work, spawned ~40 child sessions to execute, enforced regression gates and backup checks between phases, and escalated only owner-level decisions (scope rulings, go/no-go on irreversible steps). Distills reusable program-management patterns for large migrations. In a follow-up he asks Cognition to let child Devin sessions pick their own model/mode independent of the parent.

- [leopardracer](https://x.com/leopardracer/status/2074071476181876944) — 2026-07-06: Engagement-farmed take (ALL CAPS) claiming an Anthropic engineer said memory/retrieval architecture is the only skill worth learning in 2026 — arguing prompt writers cap ~$90k, engineers building memory/retrieval systems clear $250-400k, and those architecting 'the whole loop' pull seven figures ('architecture is the moat, memory is the new distribution'). Quote-tweets CyrilXBT's article 'How To Become An AI Engineer in 2026 (Without a CS Degree).' Mostly hype, thin substance.

- [ericosiu](https://x.com/ericosiu/status/2073943223836270933) — 2026-07-06: Eric Siu shares a 7-step checklist for building a 'Company Brain' (an org-wide AI agent): (1) pick one high-value workflow closest to revenue; (2) map only the critical connectors (Google Drive, Slack, CRM, Gong, Granola); (3) define memory — brand voice, decisions, workflow rules, examples, with recent decisions weighted over old ones; (4) set permissions/approvals/data exposure to avoid 'a security problem with a chat interface'; (5+) route the work. A practical playbook for company-wide AI adoption.

- [Akshay](https://x.com/akshay_pachaar/status/2073783428735250595) — 2026-07-06: Akshay Pachaar explains building a '1-person AI company' that runs locally, is 100% open-source, has no human employees (all agents), and collaborates in real time via email. His framing: multi-agent orchestration isn't new, but instead of hand-wiring a graph of nodes/edges you should model coordination on the org-chart structure companies have used for a century — lay out an org chart, each agent fills one role with reporting lines, and work flows up/down without manually relaying each message.

- [Aaron Levie](https://x.com/levie/status/2073138135014502777) — 2026-07-05: Aaron Levie (Box CEO) argues the battle in AI is shaping up to be a battle for context: agent effectiveness comes down to having the right domain expertise, access to the right context and tools, and being embedded in workflows users can easily review and incorporate. The platforms that capture and leverage the best context within their agents — and pick the right model per task — will be where agents do their best work (coding, legal, support agents at scale). This is why the applied-AI layer is worth far more than being an 'LLM wrapper': the value is in organizing the critical knowledge.

- [ℏεsam](https://x.com/hesamation/status/2073104617706008840) — 2026-07-04: [Jeremy flagged: read for work] hesam recommends Phil Chen's article 'Career advice in the age of AI' (Chen: a researcher from OpenAI, DeepMind, and Stanford). TL;DR: AI makes execution cheaper, so the durable edge is choosing the right problems, building strong connections, and investing real time — the argument being that AI models improve at anything you can write a loss function for, and school is mostly loss functions (well-defined problems graded against known answers), so the valuable work shifts elsewhere.

- [Andrew Ng](https://x.com/andrewyng/status/2071988145667928442) — 2026-07-02: Andrew Ng's 'loop engineering' letter lays out three nested loops for building 0-to-1 products: the fast agentic coding loop (agent writes/tests/iterates every few minutes), the developer feedback loop (human steers over tens of minutes to hours), and the slow external feedback loop (alpha testers, A/B tests over days). Humans retain a context advantage, so engineers increasingly play a partial product-management role.

- [Boris Cherny](https://x.com/bcherny/status/2071379474277613732) — 2026-06-29: As engineering/product/design/DS roles blur, Cherny proposes five team archetypes (not tied to job function): Prototyper, Builder, Sweeper, Grower, Maintainer. Healthy teams need different mixes by product maturity — pre-PMF wants 1+2+3, growing wants 2+3+4+some 5, strong-PMF wants 3+4+5+some 2.

- [Brian Armstrong](https://x.com/brian_armstrong/status/2070670644577280109) — 2026-06-27: Coinbase's playbook for keeping AI spend flat while token usage grows: better defaults (experimenting with cheaper open-weight models like GLM 5.2 / Kimi 2.7 via an LLM gateway, since 91% never hit caps), better routing (frontier for planning, cheaper for execution), better caching (LibreChat cache-hit rate 5% → 60%), lean context, and usage visibility. Cut AI spend nearly in half while token usage kept growing.

- [Alex Lieberman](https://x.com/businessbarista/status/2070194343034360004) — 2026-06-25: A "5 levels of work" framework for teaching high agency (credited to @stephsmithio): L1 name a problem; L2 add causes; L3 add possible solutions; L4 add a recommended pick; L5 already fixed it, just keeping you in the loop. Lieberman tells new hires to operate at Level 4 from day one and rise to Level 5 as trust builds.

- [Jaynit](https://x.com/jaynitx/status/2066506535250092378) — 2026-06-16: Thread relaying Elon Musk's 5-step engineering 'algorithm': (1) make the requirements less dumb / question them, (2) try to delete the part or process step entirely (if you aren't forced to add ~10% back, you didn't delete enough), (3) simplify and optimize, (4) accelerate cycle time, (5) automate — with the warning that the most common mistake of smart engineers is optimizing something that shouldn't exist.

- [Peter Yang](https://x.com/petergyang/status/2063988122720055772) — 2026-06-09: Five takeaways from a conversation with @kunchenguid (ex-Meta L8 engineer) on agentic engineering: (1) plan and validate, don't code yourself — you're the always-on team's manager; (2) plan quality determines how long agents run autonomously — a detailed spec can run for hours vs minutes for a one-liner; (3) use visual plans, not walls of markdown — Lavish (github.com/kunchenguid/lavish) generates visual HTML plans; (4 and 5 truncated in scrape — likely about validation rubrics and feedback loops).

- [Elon Musk](https://x.com/elonmusk/status/2063401522327666828) — 2026-06-07: Elon Musk endorses first-principles 'physics thinking in the limit' — the 'Magic Wand Number' and 'Idiot Index' as universal cost-engineering mental models. Not AI/dev, but a useful thinking frame.

- [Garry Tan](https://x.com/garrytan/status/2061878212213572083) — 2026-06-03: Garry Tan on model routing as strategy: frontier labs will want their harness to be the moat, but the consumer-best outcome is model capabilities flattening and commoditizing — 'a preview of the AI Harness Wars of 2027.' Cites Factory's auto model-router (claimed 25% cost cut at frontier performance).

- [Dave Kline](https://x.com/dklineii/status/2059634666030637286) — 2026-05-28: Management thread: 'the biggest mistake I made as a manager was not managing up' — assuming impact is obvious and the boss is plugged in — plus how to fix it.

- [Dave Kline](https://x.com/dklineii/status/2058538089224519806) — 2026-05-24: Management thread: you can't create lasting motivation (it's intrinsic), but you can demotivate — the 5 most common leadership missteps.

- [Garry Tan](https://x.com/garrytan/status/2057946119725080878) — 2026-05-24: Garry Tan's 'simple secret to agentic coding,' linking a Forbes profile ('The YC Chief Who Codes 10,000 Lines A Day Has A Simple Secret').

- [Dan Shipper](https://x.com/danshipper/status/2057514494960513272) — 2026-05-22: Dan Shipper: Every automated everything it could with AI agents, yet has more human work than ever, growing 4→30 employees since GPT-3. His report 'After Automation' argues AI makes expert competence cheap, which raises demand for experts, and the dynamic intensifies toward AGI.

- [Dave Kline](https://x.com/dklineii/status/2057451633303322715) — 2026-05-22: Management thread from a trainer of 1,500+ managers: delegation's hard part isn't assigning work but ensuring it's done well without micromanaging — with a simple 5-step system.

- [Aaron Levie](https://x.com/levie/status/2057315272156135501) — 2026-05-22: Aaron Levie on why Forward Deployed Engineers (FDEs) will persist: unlike cloud (concentrated users, little workflow change, slow enough for best practices to spread), agents are highly technical to deploy AND directly change users' workflows, and the fast model-change cadence keeps resetting best practices — so vendors/partners who've done it hundreds of times do the work. A great early-career path.

- [James Cogan](https://x.com/cogan/status/2056702063992607071) — 2026-05-22: A thoughtful essay, 'Machine Time,' arguing AI compresses the unit of meaningful time — shrinking the buffer between noticing a change and having to respond. AI compresses the front end of cognitive work, so the bottleneck moves to human review, judgment, and taste; the danger isn't speed but speed without scaffolding, and institutions increasingly answer with machine-speed coordination rather than restoring the human clock.

- [Tom Blomfield](https://x.com/t_blom/status/2056909934156280088) — 2026-05-20: Tom Blomfield breaks down what YC is seeing in recursively self-improving companies — creating recursive self-improving AI loops so founders 'run companies that improve while they sleep.'

- [Ronan Berder](https://x.com/hunvreus/status/2056742771386638454) — 2026-05-20: Pushback on Spec-Driven Development: agents are faster at writing code and (some) humans are better at system thinking, but humans suck at planning. Argument: you can't sit down, write all the specs upfront, and then write code — experienced engineers know that doesn't work. Quote-tweets a now-unavailable @iamsahaj_xyz post.

- [Linas Beliūnas](https://x.com/linasbeliunas/status/2056679329484927356) — 2026-05-20: Summarizes Anthropic's free AI-native founder playbook: build AROUND Claude across Idea → MVP → Launch → Scale (pressure-test the idea, Claude Code builds the product, Claude Cowork handles ops, Claude turns knowledge into compounding context). 'AI compresses execution but not judgment' — the edge becomes knowing what NOT to build; best AI-native startups have the best AI operating systems, not the biggest teams.

- [Dave Kline](https://x.com/dklineii/status/2056363703230980364) — 2026-05-19: Management thread: while most leaders worry about AI, a few become their company's AI expert and make themselves irreplaceable — a 5-step plan to become that leader.

- [darkzodchi](https://x.com/zodchiii/status/2056336049589092866) — 2026-05-19: Shopify Head of Engineering Farhan Thawar: 'if you don't figure out how to harness agents in 2026, you'll be behind.' A practical enterprise-AI-coding breakdown / Shopify AI playbook, linking a 'Claude Code setup behind Shopify's 23,000 engineers' article (racing to automate 96% of coding by Q3, many parallel Claude Code agents).

- [George from prodmgmt.world](https://x.com/nurijanian/status/2054244221352325359) — 2026-05-14: PM advocates using an LLM as an adversarial reviewer on your PRD — the flaws that ship to production are the ones you can't see from inside the doc. Short take with a link to his prodmgmt.world article walking through the practice.

- [Jamie Signorile](https://x.com/sigsnyc/status/2054238175758111156) — 2026-05-14: Frames AI as widening the gap between strong and average employees in enterprise GTM roles rather than uplifting everyone. Author uses a two-axis hiring framework (technical capability x business savvy) drawn from a decade at Addepar and KizenTech and argues AI inverts how operators get evaluated.

- [Jaynit](https://x.com/jaynitx/status/2054200520575967698) — 2026-05-14: Personal essay on developing implicit pattern recognition — author tracked his own pre-post predictions on engagement and hit 70-80% accuracy without being able to articulate why. Reflection on tacit-knowledge skill-building, not AI-specific.

- [Alfred Lin](https://x.com/alfred_lin/status/2054556828118245710) — 2026-05-13: Alfred Lin (Sequoia) on using simplicity humbly — frameworks have a domain of validity. Four complements: face the limits, zoom in and out, check convergence across frameworks, probabilistic thinking. Not about AI specifically, broader management/judgment essay.

- [Michael Eisenberg](https://x.com/mikeeisenberg/status/2054431554240201008) — 2026-05-13: Michael Eisenberg endorses a Zohar Atkins essay applying Jevons Paradox to Torah learning — when knowledge becomes cheap (AI), insight is what matters. Reference to Jevons' 1865 Coal Question. Off-topic for the AI stack but thoughtful framing on the value of insight in an AI-abundant world.

- [ericosiu](https://x.com/ericosiu/status/2054413343776223393) — 2026-05-13: ericosiu hiring forward-deployed engineers globally. Quotes Aaron Levie noting FDEs (or equivalent) are about to become one of the most in-demand jobs in tech for AI rollouts. References a "beat AI" challenge in his profile as their filter. Subject flagged "worth an extra look".

- [Founder Thoughts & Strategies](https://x.com/mogulinfluence/status/2054274159706853837) — 2026-05-13: Quote of Tom Verrilli (Whatnot) article on building product teams in the AI era — 31,832 people applied to be a PM at Whatnot in two years, only one hired. Framing: best product teams will ship 10x faster post-AI. Subject flagged "have a look".

- [Dave Kline](https://x.com/dklineii/status/2052372231800439054) — 2026-05-08: Dave Kline teases 5 AI prompts for 1:1 prep — claims his 5-minute pre-meeting AI ritual changed the quality of his 1:1s. Listicle framing; substance in the thread.

- [Dave Kline](https://x.com/dklineii/status/2050563237490344194) — 2026-05-02: A 15-minute manager/employee playbook for resetting expectations when someone is stuck — Kline argues 95% of work problems trace back to unclear expectations. Practical management tactic, no AI angle.

- [Ole Lehmann](https://x.com/itsolelehmann/status/2050548948419645488) — 2026-05-02: Argues you should run a 'premortem' on your plans with Claude — frame it as 'it's 6 months from now, this plan died, tell me how' — to bypass the model's optimism bias. Cites Kahneman; says Google, Goldman, P&G use it before launches.

- [Kpaxs](https://x.com/kpaxs/status/2050470605804216695) — 2026-05-02: Kpaxs reframes high-agency behavior: 'I'm doing this unless someone stops me' vs 'Can I do this?' — most permissions get granted retroactively, so it's easier to ask forgiveness than permission. Useful framing for engineering culture and AI adoption.

- [Keith Rabois](https://x.com/rabois/status/2050250243552239956) — 2026-05-02: Rabois (one-word 'Useful.') endorsing Ann Miura-Ko's piece arguing most scaled companies (e.g. Ramp, 1500-person org) are still Level 1 on AI adoption despite the 'AI-pilled' narrative — based on her recent office visits.

- [Dan Shipper](https://x.com/danshipper/status/2050235671466606665) — 2026-05-02: Dan Shipper recommends Marcus's 'definitive guide' on how a PM can ship product with coding agents at Every: every.to/guides/ai-product-management-guide. Pitched as required reading for non-engineer builders.

- [regent0x](https://x.com/regent0x_/status/2050143341656838449) — 2026-05-02: Story (likely embellished) about a solo Chinese dev billing $320k/yr by orchestrating 5 specialized Claude agents in parallel: architect, coder, reviewer, tester, ops. Each agent has its own context, no shared state. Engagement-y framing but the parallel-specialist pattern is real.

- [Ethan Mollick](https://x.com/emollick/status/2047828327856030047) — 2026-04-25: Ethan Mollick: 'Organizational design for agents is hard, benchmarking agents working in concert is hard. Together, this is the next critical frontier for making AI matter in economically valuable tasks, and we really don't know very much about it.' Quote-tweets @krishnanrohit's essay 'Aligned Agents Still Build Misaligned Organisations.'

- [Ihtesham Ali](https://x.com/ihtesham2005/status/2046197374855582157) — 2026-04-21: Writeup of George Pólya's 1945 book 'How to Solve It' — the four-step problem-solving framework (understand, plan, execute, look back). Central heuristic: if you can't solve the proposed problem, solve a simpler related one first. Jeremy's note 'important for planner?' — relevant for AI agent planning/decomposition patterns.

- [0xSero](https://x.com/0xsero/status/2044879665001595263) — 2026-04-17: 0xSero (quote-tweeting Sarah Chieng's article 'Single-agent AI coding is a nightmare for engineers') says he's gone 180 on multi-agents/subagents after analyzing hundreds of AI coding agent sessions — they actually help a lot. Practitioner's change-of-mind about orchestration.

- [Hamudi](https://x.com/hamudinaanaa/status/2044872907072164304) — 2026-04-17: Hamudi ties into Sequoia's "$1T thesis" that AI sells outcomes (work) rather than software tools, introducing "Outcome Primitives" as a way to measure economic outcomes, citing a published paper tracking 1,300 agents over 21 days that created $32M in value (jobs secured, $200k grants won, e-commerce shops shipped). Framing: copilots compete on software margins and lose to big labs; outcome engines compete on services margins.

- [Garry Tan](https://x.com/garrytan/status/2044059516497711522) — 2026-04-15: Garry Tan amplifies Alfred Lin's article 'Heat Seeking Missile for Pain': the realest founders actively hunt the hairiest, gnarliest problems and surgically destroy them, citing an interview with Keller of Zipline.

- [Amir Salihefendić](https://x.com/amix3k/status/2044046057315742146) — 2026-04-15: Amir Salihefendić (Doist) treats Jack Dorsey's recent framing as an org-design question for companies blending human and machine intelligence: remote-first, transparent, functional teams with clear DRIs, where AI increasingly supplies the 'connective tissue' that moves context across teams, tools, and decisions.

- [Alex Vacca](https://x.com/itsalexvacca/status/2043834187095150673) — 2026-04-14: Growth/marketing content (mostly off the AI/dev core): endorses Michel Lieben's article on running a 4-layer funnel instead of a bare 'book a call', citing a $7M-ARR bootstrapped funnel (330k visitors, 1,500+ meetings, $4M new ARR). Relevant only as go-to-market reading.

- [North@CreaoAI](https://x.com/anorth_chen/status/2043694726764003817) — 2026-04-14: Endorses (translated from Chinese) an 'AI-First' engineering essay by the author's CTO: after going AI-first, the team merges/deploys 20+ PRs daily with ~99% of production code written by AI, shipping and A/B-killing features within a day. Argument: teams stuck in 'AI-assisted' rather than 'AI-first' mode risk fading from the market within a year. Provocative management/strategy read.

- [Garry Tan](https://x.com/garrytan/status/2043581361798500602) — 2026-04-13: Garry Tan adds 'Boil the ocean' to his SOUL.md: the marginal cost of completeness is near zero with AI. Do the whole thing with tests, docs, and quality. Never table for later, never present workarounds, never leave dangling threads. 433.1K views.

- [Garry Tan](https://x.com/garrytan/status/2043198780800197025) — 2026-04-12: 'If your memory dies when your harness dies, you built the harness too thick.' Argues for thin harnesses: memory is markdown, skills are markdown, the 'brain' is a git repo, and the harness is a thin conductor that reads files it doesn't own. Endorses Harrison Chase's 'Your harness, your memory' article on harness/memory coupling and the risk of closed harnesses.

- [Seb Goddijn](https://x.com/sebgoddijn/status/2042286523001737545) — 2026-04-10: Ramp hit 99% AI adoption company-wide but found most employees stuck in chat windows while power users ran laps. They built "Glass" — an internal AI productivity suite on Anthropic's Claude Agent SDK — reaching 700 DAUs in one month. Philosophy: raise the floor for all employees rather than lowering the ceiling for power users.

- [Aakash Gupta](https://x.com/aakashgupta/status/2041984945380585785) — 2026-04-09: Makes the case for "Team OS" — a shared GitHub repo that serves as a team's collective brain for Claude. Companies spending $200K/yr on AI seats see zero productivity gains because each person starts from scratch every conversation with no shared context. Structured context (customer calls, specs, constraints, strategy docs) compounds across the team.

- [Ksenia Se](https://x.com/theturingpost/status/2041455210342871094) — 2026-04-08: Ksenia from TuringPost on the enterprise AI adoption gap: despite SF hype, most companies are still at ChatGPT-for-writing stage. AI adoption isn't a straight line but a stack of dependencies — you can't jump to agents if workflows aren't legible, can't act on data you don't trust. Most AI pilots fail because organizational readiness, not the technology, is the bottleneck.

- [Allie K. Miller](https://x.com/alliekmiller/status/2041577000804991485) — 2026-04-07: Allie K. Miller shares a 5-level 'Proactive AI-First Team Member' framework for hiring and onboarding. Levels range from 1 (not using AI) to 5 (full ownership with AI-augmented critical thinking). Key insight: most candidates interview at level 3 (solution-oriented but not action-oriented) — she wants new hires starting at level 4 (action-oriented with technical/business tradeoff awareness). Originally from @businessbarista and @stephsmithio, with AI additions by Miller.

- [Eric Siu](https://x.com/ericosiu/status/2040785346120859946) — 2026-04-06: Practical guide to deploying Jack Dorsey's 'world intelligence' concept — a company-wide AI knowledge layer that powers 50+ daily workflows, coordinates decisions across teams, and surfaces issues automatically. Includes a linked article with implementation details from 4 months of running this at his company.

- [Dave Kline](https://x.com/dklineii/status/2040776601223246334) — 2026-04-06: Management advice on fixing broken 1:1 meetings — 4 tests to determine if your 1:1s are actually working. Covers common anti-patterns like cancelling on top performers, using 1:1s as status reports, and doing most of the talking instead of listening.

- [Daniel Miessler](https://x.com/danielmiessler/status/2038284628130492870) — 2026-03-30: 'Bitter Lesson Engineering' (danielmiessler.com): don't over-engineer your AI harness — lean on scaling/general methods rather than hand-crafted scaffolding, applying Sutton's bitter lesson to agent-harness design.

- [Matt Stockton](https://x.com/mstockton/status/2035179208872202320) — 2026-03-22: Matt Stockton argues building AI-enabled products inverts classical software engineering: the 'right way to build' changes every ~3 months, it is often better to burn the system down and rebuild than to adapt, and modern tools make that cheap — warning against sunk-cost V1 RAG systems that stuff a static context window.

- [Beacon](https://x.com/0xxbeacon/status/2033224402070810940) — 2026-03-16: Beacon links Anthropic's Skilljar course catalog (anthropic.skilljar.com) and the access-request page for the Claude Certified Architect: Foundations certification.

- [Suhail Gupta](https://x.com/audiinidesign/status/2031213732941230240) — 2026-03-10: Suhail Gupta endorses Harrison Chase's article 'How Coding Agents Are Reshaping Engineering, Product and Design,' agreeing the EPD blur toward functional software over separate roles will only become more visible and obvious in the coming months.

- [Anish Moonka](https://x.com/anisha_moonka/status/2030015356383691121) — 2026-03-07: Anish Moonka's 12-point notes from Boris Cherny (Head of Claude Code) on Lenny's Podcast: coding is largely solved (Boris ships 10-30 PRs/day, no hand-written code since Nov 2025); the next frontier is AI deciding what to build; productivity per Anthropic engineer is up 200%; underfund teams on purpose; give engineers unlimited tokens; the Bitter Lesson favors general models over rigid orchestration; build for the model six months out; latent demand is the best product signal; 'software engineer' is becoming 'builder'; mechanistic interpretability enables layered safety; and 70% of engineers/PMs enjoy their jobs more now.

- [staysaasy](https://x.com/staysaasy/status/2029965845548462281) — 2026-03-07: staysaasy long-form article 'Avoiding a Culture of Emergencies': the best managers have far fewer preventable emergencies because they know how hard things actually are, know what's important and can say no, hold a strong mental model of their team and company to forecast needs, and genuinely care. Emergencies are largely a management choice, and avoiding them is one of the best talent-retention mechanisms.

- [Jamie Quint](https://x.com/jamiequint/status/2029951631534739951) — 2026-03-07: Jamie Quint (built Notion's early data stack in 2020) shares his article 'How to Build a Data Agent in 2026,' claiming the approach can cut a company's projected data-team headcount by ~80% this year.

- [Alexey Grigorev](https://x.com/al_grigor/status/2029829363903123636) — 2026-03-06: Argues prompting is only ~5% of AI engineering; the other 95% is making AI testable, observable, versioned and reliable in production. Core skills: evaluation/testing with golden eval sets and regression tests, plus controlled iteration via prompt versioning and experiment tracking (Git/MLflow).

- [John Rush](https://x.com/johnrushx/status/2029406051716743354) — 2026-03-05: Opinion piece: AI does not make work easier — it strips away the easy 99% of jobs so everyone now competes on the hard 1%, raising cognitive load and stress sharply. A take on how AI reshapes knowledge work.

- [yenkel](https://x.com/yenkel/status/2029299384832209259) — 2026-03-05: Crisp engineering-leadership advice for the AI era: fewer handoffs and faster decisions, more exploration, willingness to throw away code/tokens, learning by building, and picking leads who can own design, engineering and product together.

- [Tech Layoff Tracker](https://x.com/techlayofflover/status/2029261882834501665) — 2026-03-05: Shares a venting DM from a senior Big Tech SWE (~$350k TC): leadership now touts an "AI leverage ratio" of 4.2x — each engineer shipping the output of a former four-person team — fueling job anxiety. Engagement-styled but a real signal on AI-driven productivity expectations and layoffs.

- [Peter Yang](https://x.com/petergyang/status/2029220235375714766) — 2026-03-05: Deep dive arguing your new job is to onboard and manage AI agents, with examples from Linear (AI team members you assign tasks to), Ramp (Claude Code as baseline for all roles), and Factory (codifying PM, frontend, and data-analysis work into reusable skills).

- [Bojan Tunguz](https://x.com/tunguz/status/2029164042028236942) — 2026-03-05: Reflects on "mid season" knowledge — many roles require grappling with a problem mid-stream without enough runway to catch up on missing context, something even smart people underestimate.

- [Dan Robinson](https://x.com/danlovesproofs/status/2028890694837039202) — 2026-03-05: Argues issue tracking/backlogs are dying: forward-thinking AI-augmented teams skip Linear/tickets entirely because the cost to fix an issue now approaches the cost to understand it. Works for small, flat, high-context teams with strong dev infra; framed as part of the 'death of midwit software engineering.'

- [Avid](https://x.com/av1dlive/status/2027429188471558475) — 2026-03-05: Engagement-style 'AI will take your job' listicle, but with a usable career playbook: audit which tasks AI can replicate, learn local agent tooling and stackable 'skills', layer AI-native competence (prompting, orchestration, RAG, automation), shift from executor to system designer, double down on human edge, and build a product/brand.

- [David Byttow](https://x.com/davidbyttow/status/2028233578329600449) — 2026-03-02: Essay arguing AI agents are collapsing the coordination layer of organizations. As execution and coordination costs approach zero, the remaining scarce skill is goal clarity, taste, and ownership. Warns bad judgment now scales faster — strategic mistakes show up as fast delivery of the wrong thing.

- [SightBringer](https://x.com/_the_prophet__/status/2027235489930191056) — 2026-02-27: Critique of AI auto-memory (quote-tweeting Anthropic's Claude auto-memory announcement) as a "power grab disguised as convenience": capturing your patterns, defaults, and definitions of 'good' shifts the model from serving you to shaping you, and dependency is the business model. Counter-playbook: treat memory as a controlled instrument — scope it like permissions, separate persona from operations, keep a purge cycle, audit what the model believes about you, and never let it silently rewrite your intent. Frames the AI era as shifting from intelligence to custody of context/continuity.

- [George from prodmgmt.world](https://x.com/nurijanian/status/2027020091418890613) — 2026-02-27: George argues elite PMs escalate documentation with validation rather than starting with a 10-page PRD: 1-pagers are decision docs (write ~10, ~3 get approved), 3-pagers validate and align, and 5-pagers add execution detail only for ideas that survived two rounds. Documentation should match your confidence level, not your anxiety level.

- [Fernando](https://x.com/franc0fernand0/status/2026701684106313791) — 2026-02-27: Fernando summarizes a Microsoft study (Kalliamvakou et al., TSE 2018) on what makes a great manager of software engineers: technical skill is required but not sufficient; what distinguished great managers was availability, granting autonomy, supporting experimentation, and setting clear ways of working.

- [Matt Pocock](https://x.com/mattpocockuk/status/2026296080602673316) — 2026-02-25: Matt Pocock observes that AI coding rewards a 'lead dev' mentality: developers who spent their careers leveling up teammates through API design, feedback loops, and architecture find working with AI natural, while those who optimized only their own output find it uncomfortable.

- [Dr Milan Milanovic](https://x.com/milan_milanovic/status/2023381859489767772) — 2026-02-17: Milan Milanovic's thesis: AI won't replace developers so much as the software-development process we're used to. Code is becoming cheap while decisions become expensive; AI reduces typing, not thinking. Developers who only implement tasks will struggle, while those who understand the product, domain, and system architecture will thrive.

- [dax](https://x.com/thdxr/status/2022574719694758147) — 2026-02-14: dax (thdxr) offers a contrarian take on AI coding hype: orgs are rarely bottlenecked by code-production ability. Most workers use AI to do their tasks with less effort rather than to become 10x; the few who genuinely push are getting buried under everyone else's 'slop code' and may quit; teams remain bottlenecked by bureaucracy; and CFOs are noticing each engineer now costs ~$2,000/month more in LLM bills.

- [Machina](https://x.com/exm7777/status/2019787951530725396) — 2026-02-07: Machina's thread on how to stop feeling behind in AI: the relentless cadence of releases (GPT-5.3 Codex, Opus 4.6, Kling 3.0, all 'redefining everything') creates a low-grade, never-ending pressure. His reframe is that the problem isn't too much happening, it's the lack of a personal filter for what actually matters to your work.

- [Dave Kline](https://x.com/dklineii/status/2018690947215663592) — 2026-02-05: Dave Kline's thread on how the management job changes by level: most managers fail because they're thrown in with no training, little support, and unrealistic expectations, and the required abilities, priorities, and skills differ sharply from first-line management up through senior levels.

- [Dave Kline](https://x.com/dklineii/status/2015406993612079328) — 2026-01-25: Dave Kline shares a 5-step delegation system, noting that across 1,400+ managers he's trained, delegation is the universal struggle: the hard part isn't assigning work but ensuring it gets done well without micromanaging.

- [Mischa van den Burg](https://x.com/mischa_vdburg/status/2013178484143571034) — 2026-01-20: Argues AI agent orchestration is the next 'container orchestration war', building on a Steve Yegge framework of two primitives: Workers (making a single agent produce high-quality output) vs Factories (coordinating thousands of work items across many agents). Maps these to familiar infra patterns - Workers = CI runners/pods/Lambdas, Factories = schedulers/control planes/workflow engines. Predicts 'nondeterministic idempotence' as the new eventual consistency, audit trails for AI work, GitOps-style declarative state, and reuse of the microservices observability stack. Kubernetes-fluent engineers have a head start.

- [Abhishek Singh](https://x.com/0xlelouch_/status/2012816833464922398) — 2026-01-19: A Senior Staff Engineer's method for reasoning about unfamiliar systems: (1) start with the business goal and what 'failure' means, not the code; (2) identify the 2-3 critical paths where latency/correctness/money matter; (3) map ownership boundaries and handoff gray areas; (4) look for invariants that must hold even during partial failures/deploys; (5) read postmortems before docs (real vs intended behavior); (6) ask 'what breaks first at 10x load?' to expose hidden assumptions. The kind of skill that separates senior from staff.

- [Gergely Orosz](https://x.com/gergelyorosz/status/2011956185650409558) — 2026-01-16: Gergely Orosz amplifies Cindy Sridharan's take that, outside of prototyping, engineers should aim to understand close to 100% of the production code LLMs generate. He adds that the gap between teams who do this and those who don't will be massive, and notes the tension: heavy cutting-edge AI use is easiest on throwaway prototypes where it's fine to let it rip.

- [SightBringer](https://x.com/_the_prophet__/status/2004796159299084424) — 2025-12-27: An essay arguing software engineering is undergoing a 'phase transition' in human leverage: for decades leverage came from writing more correct instructions faster, but the unit of leverage has shifted from writing code to orchestrating intelligence. The programmer becomes a systems integrator of probabilistic entities whose reasoning can't be fully inspected or controlled — which the author says explains why even Karpathy feels 'behind.'

- [Abhishek Singh](https://x.com/0xlelouch_/status/2002673253912113644) — 2025-12-22: A reflective essay on career fulfillment in software engineering: you don't magically know whether backend, frontend, infra, ML, startups, big tech, or management will fulfill you — you only find out through reps. Early on people confuse novelty (new frameworks, jobs, titles) with fulfillment; real self-knowledge is earned by shipping boring features, debugging 3am outages, owning systems, and sticking with things long enough to feel the responsibility.

- [Dave Kline](https://x.com/dklineii/status/1994761636742050226) — 2025-11-29: Dave Kline's thread on 'The 7 Deadly Sins of New Managers,' framed around the claim that ~60% of people fail in their first leadership role. This post is the hook for a list of common first-time-manager mistakes (detailed items continue in the thread/graphic).

- [George from prodmgmt.world](https://x.com/nurijanian/status/1988335427447869565) — 2025-11-12: George (prodmgmt.world) shares a 'tough, unreasonable product executive' critique prompt he runs product decisions through: it skeptically stress-tests requirements across cross-team collaboration, conflicting requirements, maintainability, strategic implications, clarity, and feasibility, returning structured critiques (section/issue/impact/suggestion). Ends with a paid prompt-library link.

- [Aadit Sheth](https://x.com/aaditsh/status/1983103310791159863) — 2025-10-31: Aadit Sheth shares a chart breaking down what being 'good with AI' looks like role by role, framed as a way to gauge whether a team is truly AI-fluent and pitched as useful for hiring and leading in 2025. The breakdown itself is in an attached chart image.

- [William Meijer](https://x.com/williameijer/status/1982843287095717935) — 2025-10-28: William Meijer argues that a willingness to voice 'unkind truths' — blunt, uncomfortable candor — is a key element of Elon Musk's entrepreneurial success.

- [Aakash Gupta](https://x.com/aakashg0/status/1979517333015334953) — 2025-10-19: Aakash Gupta highlights Jeff Bezos's framework distinguishing reversible ('two-way door') from irreversible ('one-way door') decisions as a guide to how much deliberation a call deserves.

- [Always Keep Learning](https://x.com/alwayskeepl/status/1979452892059967974) — 2025-10-19: Infographic-style post outlining servant leadership as an alternative model for leading teams differently.

- [Alex Lieberman](https://x.com/businessbarista/status/1978988763620741503) — 2025-10-17: Alex Lieberman shares a '5 levels of work' framework for teaching high agency, from L1 'there is a problem' to L5 'I found it, fixed it, just keeping you in the loop.' He tells new hires to operate at Level 4 from day one and grow into Level 5. Credits Steph Smith.

- [Kevin Box](https://x.com/fuel_yourgrowth/status/1977008526867546245) — 2025-10-11: Infographic contrasting a toxic boss with a great leader, arguing a manager's impact on employee mental health can exceed a therapist's.

- [Kevin Box](https://x.com/fuel_yourgrowth/status/1976274742702440662) — 2025-10-09: Short motivational post arguing that being easy to work with is an underrated professional skill.

- [keshav](https://x.com/kshvbgde/status/1974835291358969895) — 2025-10-07: Post (likely video/thread) on Steve Jobs's principles for designing insanely great products.

- [ℏεsam](https://x.com/hesamation/status/1962508535515791739) — 2025-09-02: Recommends a blog (linked in the post) as a strong source of technical playbooks, useful both for engineers and for managers who want a grounding in technical topics.

- [Arthur MacWaters](https://x.com/arthurmacwaters/status/1957580001433514167) — 2025-08-19: Endorses a referenced approach as 'unironically the right way to build a startup.' The substantive content is in the quoted/referenced post rather than the one-line commentary.

- [Dante O. Cuales, Jr.](https://x.com/danteocualesjr/status/1957204427909321027) — 2025-08-18: Argues the intimidation factor of AI engineering is mostly artificial: most work is API orchestration, prompt optimization, and data-pipeline plumbing, with model internals abstracted away. The real skill is choosing the right tool and chaining them effectively.

- [Book Therapy](https://x.com/book_therapy223/status/1943651617976283236) — 2025-07-11: Shares content on the distinction 'A Plan is Not a Strategy' (the Roger Martin / HBR theme): strategy is an integrated set of choices about where to play and how to win, not merely a list of planned activities. Post text is just the headline; the substance is in the attached media.

- [Graham Helton](https://x.com/grahamhelton3/status/1936462167751921698) — 2025-06-23: Before leaving Google for Snowflake, Graham Helton braindumped ~34 personal guidelines/principles he follows for work and productivity; the thread lists them.

- [DHH](https://x.com/dhh/status/1934978649872371944) — 2025-06-18: DHH argues the jump from Programmer to Senior Programmer is the biggest career-progression chasm in software; those who cross it tend to keep advancing, but many never do.

- [Dave Kline](https://x.com/dklineii/status/1928797718907908342) — 2025-06-01: Opens a management thread promising one skill to become a better manager overnight; the specific skill and guidance are developed in the replies.

- [Elon Musk](https://x.com/elonmusk/status/1862363270931255356) — 2024-11-29: Elon Musk touts his '5-step algorithm' for making fewer mistakes (make requirements less dumb, delete parts/processes, simplify & optimize, accelerate cycle time, automate), in a quote of a post speculating DOGE might adopt it like SpaceX.

- [Sarah Cone](https://x.com/sarah_cone/status/1847322215907545129) — 2024-10-19: Points to a superengineer.net blog post as a good summary of Elon Musk's 5-step design/engineering method (DFX).

### Questionable (114)

- [How To Prompt](https://x.com/howtoprompt__/status/2076689880026096089) — 2026-07-14: How To Prompt highlights an open-source, privacy-first Chromium fork built by an ex-Google engineer with a native AI agent, built-in MCP server, Cowork-style web+local-file agents, scheduled autopilot tasks, 40+ app integrations (Gmail, Slack, Notion, Linear, Figma, Salesforce), and local-model (Ollama) support — drivable from Claude Code or Gemini CLI. Engagement-framed but describes a real agentic-browser tool worth evaluating.

- [Alex Prompter](https://x.com/alex_prompter/status/2074198124898181121) — 2026-07-14: Alex Prompter's thread pitches 'cloning' Fable 5's reasoning into Opus 4.8 before Fable 5 shifts to pay-per-use credits — extracting a model's 'operating manual' as a portable prompt and transplanting it onto a cheaper model to keep the way it thinks rather than the model itself. Engagement-framed but a real prompt-portability technique.

- [How To Prompt](https://x.com/howtoprompt__/status/2074122800961614184) — 2026-07-07: How To Prompt (hype framing: "China has killed the vector database industry") flags Tencent's newly open-sourced TencentDB Agent Memory — local long-term memory for AI agents that runs 100% on plain SQLite with no external vector DB or cloud APIs. Claims 61% fewer tokens and PersonaMem accuracy 48%->76%. Uses a layered 'semantic pyramid' (L0 conversation -> L1 atom -> L2 scenario -> L3 persona) stored as inspectable markdown + Mermaid graphs instead of opaque vector compression, with drill-back to raw logs by node_id. ~5.1k GitHub stars.

- [leopardracer](https://x.com/leopardracer/status/2074071476181876944) — 2026-07-06: Engagement-farmed take (ALL CAPS) claiming an Anthropic engineer said memory/retrieval architecture is the only skill worth learning in 2026 — arguing prompt writers cap ~$90k, engineers building memory/retrieval systems clear $250-400k, and those architecting 'the whole loop' pull seven figures ('architecture is the moat, memory is the new distribution'). Quote-tweets CyrilXBT's article 'How To Become An AI Engineer in 2026 (Without a CS Degree).' Mostly hype, thin substance.

- [Isra](https://x.com/israfill/status/2073789727698743516) — 2026-07-06: Isra flags Alibaba's newly open-sourced Page-Agent (~22K GitHub stars, +949 in a day) — an MIT-licensed JavaScript library that embeds an AI agent directly into any webpage via a single <script> tag. It reads the live DOM as structured text and acts as the real user with no headless browser, Selenium/Playwright, Python server, or computer vision. Works with any LLM (GPT, Claude, Grok, Qwen, local via Ollama), has built-in human confirmation before critical actions, and can pair with the Web Speech API for voice control. Pitched as a lightweight replacement for Selenium/Playwright and vision-based browser agents.

- [Dami-Defi](https://x.com/damidefi/status/2073397918447423966) — 2026-07-05: Dami-Defi promotes an Obsidian community plugin (19,184 downloads) that fixes Obsidian's long-open YouTube-embed bug, plus a workflow to turn a messy YouTube-note vault into a visual, AI-powered knowledge system using AI-friendly metadata and automatic thumbnails — arguing structured knowledge bases outperform scattered notes in AI-native workflows. Credits Paul's Obsidian Systems (YouTube).

- [Anatoli Kopadze](https://x.com/anatolikopadze/status/2073396351279276397) — 2026-07-05: Anatoli Kopadze (quote-tweeting his own Claude features guide) shares an Anthropic engineer's claim that most people use Sonnet 5 and Fable 5 wrong and can set them up right in one afternoon to stop overpaying — a 31-minute session on testing each model against your real use case, plus a guide to Claude features '99% of users never find.'

- [Avid](https://x.com/av1dlive/status/2073114542851416260) — 2026-07-05: Avid (ALL CAPS engagement framing) makes a practical context-engineering point: give an agent one index file per major folder for a direct line to what it needs. The same task dropped from 2 minutes (7 files opened, wandering, a 3-month-old brief still missing) to 10 seconds with the same model, nothing else changed. 'Build the path or watch it search in the dark.' Quote-tweets Machina's article 'How to build a second brain with Fable 5.'

- [Sprytix](https://x.com/sprytixl/status/2073101741604679714) — 2026-07-05: Sprytix (clickbait 'Anthropic just leaked an internal engineering document' framing) lays out a six-layer self-improving agent loop: Generate -> Evaluate -> Remember -> Schedule -> Optimize -> Recurse. Generation produces its own solutions (no human brief), Evaluation is a second layer that can say no, Memory retains useful discoveries each cycle, Scheduling decides what happens next, Optimization updates behavior based on what worked, and Recursion means removing any single layer drops performance significantly — shifting the human from operator to designer.

- [darkzodchi](https://x.com/zodchiii/status/2072973531768328626) — 2026-07-05: darkzodchi's 'Claude Fable 5 Setup Guide' covers which heavy tasks actually deserve Fable 5, the new safeguards that reroute you to Opus, and how to plan the free window (up to 50% of weekly limit free until July 7). Recaps a reported Fable 5 timeline: launched June 9, pulled June 12 under a US export-control order tied to a jailbreak report, back online July 1. (Includes Telegram self-promo.)

- [me](https://x.com/twetsfyp/status/2072939523160285688) — 2026-07-05: Engagement-farmed clickbait promoting a 16-minute tutorial on building '$50,000 cinematic websites' step by step with Claude Fable 5 ('Mito Claude is back in an insane way'). Little substance in the post itself. 1.9M views.

- [ali](https://x.com/waterloo_intern/status/2073171123542573231) — 2026-07-04: ali (@waterloo_intern) — an apparent parody of distillation hype: claims to have distilled 2.3M Claude Fable 5 reasoning traces into Qwen3-4B with '100% self-consistency @ 512 samples, 0.00 bits output entropy, zero hallucination variance,' that 'the student is not bounded by the teacher,' and that it 'converged on one universal truth,' with open-sourced weights. 3M views; reads as satire rather than a real result.

- [Archive](https://x.com/archiveexplorer/status/2073136973162872897) — 2026-07-04: Archive (engagement framing, 'met an Anthropic engineer making $1.2M') argues the real lever isn't Opus vs Sonnet but 'what the model wakes up into' — the .claude/ folder: CLAUDE.md (the contract), settings.json (permissions), hooks/ (reflexes), agents/verifier (a shift-notes checker subagent), skills/ (~33 reusable 'muscle memories'), .mcp.json (tools), and MEMORY.md (shift log). 'You write the folder once; the folder runs the model.' Quote-tweets his own article 'Loop and Harness engineering: 7 files, 5 steps.'

- [Prajwal Tomar](https://x.com/prajwaltomar_/status/2070545372880245179) — 2026-06-27: Pro tip framed around the author's promotional "Hermes Agent" article: rather than just reading an article, paste it into an agent session and tell it to update itself, read the playbook, and set up whichever features help your workflow. Thesis: articles are becoming playbooks your agent runs for you. Heavy self-promotion / engagement framing.

- [Brady Long](https://x.com/thisguyknowsai/status/2070445026233172314) — 2026-06-27: Promo-styled writeup of MemPalace, an open-source local AI memory tool (49K stars). Instead of dumping everything into semantic search, it organizes memory into a structured "palace" (people/projects as wings, topics as rooms, verbatim text in searchable drawers). Claims 96.6% retrieval recall on LongMemEval with zero LLM/API/cloud, 98.4% with a hybrid pipeline; ships 29 MCP tools and auto-save hooks for Claude Code. Python 3.9 + ChromaDB, ~300MB, MIT.

- [hoeem](https://x.com/hooeem/status/2070072775201444118) — 2026-06-25: Engagement-bait post hyping a quote-tweeted "how to escape the rat race and become financially free" article. No substantive AI content; clickbait framing ("most important article you'll read").

- [Nav Toor](https://x.com/heynavtoor/status/2069773963413340297) — 2026-06-25: Listicle-styled promo for MinerU, an open-source document-extraction tool (68.5K stars) from Shanghai AI Lab's OpenDataLab. Reads PDFs/Office docs/scanned images into clean Markdown with reading-order text, tables → HTML, equations → LaTeX, OCR, 109 languages, batch mode, and 10k-page docs via sliding window. CLI, Python SDK, or web app; plugs into Claude Desktop, Cursor, LangChain, LlamaIndex, etc. Apache-2.0-based license, free.

- [Hugging Models](https://x.com/huggingmodels/status/2069750892287721960) — 2026-06-25: Brief hype post: NVIDIA released an FP4 quantized MoE version of Qwen3.6 that fits in 35B parameters but runs with the efficiency of a ~3B model, pitched as a win for efficient inference.

- [Movez](https://x.com/0xmovez/status/2068763235587694769) — 2026-06-23: Movez highlights an Andrew Ng talk on building self-improving agentic systems from scratch, quoting Ng that AI agents now handle 100% of his tasks and that self-improving loops will replace prompting within 3-6 months. Quote-tweets his own article on a 300-agent swarm running on Kimi K2.6 verified by Opus 4.8. Heavy promotional framing.

- [How To Prompt](https://x.com/howtoprompt__/status/2067176008445513800) — 2026-06-17: Engagement-farmed post claiming an open-source repo compresses 60M text chunks from 201GB to ~6GB (97% smaller) with no accuracy loss, running fully private on a standard laptop with no cloud or GPU — pitched as making vector databases obsolete. No repo link was surfaced in the post or visible replies, so the project would need to be located before the claim can be evaluated.

- [Jaynit](https://x.com/jaynitx/status/2066506535250092378) — 2026-06-16: Thread relaying Elon Musk's 5-step engineering 'algorithm': (1) make the requirements less dumb / question them, (2) try to delete the part or process step entirely (if you aren't forced to add ~10% back, you didn't delete enough), (3) simplify and optimize, (4) accelerate cycle time, (5) automate — with the warning that the most common mistake of smart engineers is optimizing something that shouldn't exist.

- [Avid](https://x.com/av1dlive/status/2066127265407336535) — 2026-06-15: Argues you can run capable AI models locally on a Mac for free using Apple's MLX stack — install mlx-lm, launch its server, and point any agent at localhost. Cites a ~23-minute talk from an Apple MLX-team engineer in which a local model builds a working SwiftUI app from a blank Xcode project in two minutes and then fixes a bug, with nothing leaving the machine. Quote-tweets a piece on the ThinkStation PGX local-inference box.

- [Olivia Chowdhury](https://x.com/oliviacoder1/status/2066064093552038070) — 2026-06-15: Hype-framed thread on a Dec 31, 2025 MIT CSAIL paper that claims to 'solve' AI memory not by building bigger context windows but by teaching models how to read/retrieve — positioning the result against the industry's context-window arms race and the 'context rot' problem, where a model's performance on information already in context degrades as more is packed in.

- [Lorwen Harris Nagle, PhD](https://x.com/lorwen108/status/2065852553208992218) — 2026-06-14: Off-topic motivational thread on Elon Musk, Nietzsche, and overcoming teenage depression/anxiety through imagination rather than analysis — pop-psychology engagement content with no AI or technical substance.

- [Avid](https://x.com/av1dlive/status/2065747876005937416) — 2026-06-14: Promotes a 'second brain' pattern attributed to Karpathy: let an LLM maintain a wiki of your notes so knowledge compounds as you dump sources and it reads, links, and files them. Points to a free Claude Code plugin, claude-obsidian by AgriciDaniel (claude plugin marketplace add AgriciDaniel/claude-obsidian; claude plugin install claude-obsidian@agricidaniel-claude-obsidian), then run /wiki inside an Obsidian folder. Quote-tweets the author's own article on building Obsidian from scratch with 13+ Kimi agents.

- [Nav Toor](https://x.com/heynavtoor/status/2065427656112505017) — 2026-06-14: Spotlights Clone-Wars, an open-source GitHub collection (~34,555 stars) by developer Gourav Goyal that catalogues 100+ open-source clones of major apps (Netflix, Spotify, Instagram, Airbnb, WhatsApp, TikTok, Amazon) with source code, demos, and tech stacks listed — e.g., a Netflix clone in React + TMDB API. Started December 2020 and hit GitHub Trending and Hacker News #1.

- [Suryansh Tiwari](https://x.com/suryanshti777/status/2065473893817848266) — 2026-06-13: Claims Anthropic released an official Claude Code plugin, claude-code-setup, that scans your project and recommends and sets up hooks, skills, MCP servers, subagents, and automations step-by-step (install: /plugin install claude-code-setup@claude-plugins-official), arguing most people run Claude Code vanilla and miss the surrounding ecosystem. Quote-tweets the author's own 'Unveil' build. (Treat the 'official' claim as unverified.)

- [Codez](https://x.com/0xcodez/status/2065097407965127142) — 2026-06-12: Hype-framed thread claiming an Anthropic 'Managed Agents' team demo showing how to build self-improving agent systems with the Fable 5 model from scratch in ~13 minutes, using /loops, dynamic workflows, and 'dreaming.' Quote-tweets the author's own 14-step article on the same. (Strong engagement-farming framing; claims unverified.)

- [Nainsi Dwivedi](https://x.com/nainsidwiv50980/status/2064947761779208476) — 2026-06-11: Alibaba open-sourced 'open-code-review' (Apache-2.0), the internal AI code reviewer that's run on their codebase for ~2 years — 20,000+ engineers, 1M+ reviews. Design: deterministic engineering handles what must never fail (file selection, bundling, rule matching, comment positioning) while the LLM only does context reading, codebase search, and reasoning. Claims ~1/5 the token cost of a generic agent + skills and precise line-level comments that don't drift on large changesets. Repo name: open-code-review.

- [Meta Alchemist](https://x.com/meta_alchemist/status/2064431279383433646) — 2026-06-11: Shares a copy-paste 'Repo Audit & Improvement Plan' prompt — a structured, 4-phase principal-engineer audit (Phase 1 discovery/mapping before judging, then a prioritized, actionable improvement plan), with instructions to cite file paths and line numbers and to flag anything unverifiable. Useful prompt template, but wrapped in hype framing around a nonexistent 'Claude Fable 5' model.

- [Jeff Tang](https://x.com/jefftangx/status/2064052420888363090) — 2026-06-09: Off-topic for the AI links collection — points to a 57-page Reddit-sourced Google Doc summarizing peptide human trials (BPC-157 et al). Health/biohacking, not AI/agents. Engagement-style 'Bookmark this' framing. Probably an accidental email-to-self.

- [rari](https://x.com/0xwhrrari/status/2063244577482440978) — 2026-06-08: Engagement-farmed but useful link dump of free AI-engineering learning resources (LangChain agent architecture, Anthropic's Claude Code 101 + in-action courses, prompt engineering docs, anthropics/courses interactive prompt tutorial, claude.md docs, skills, MCP). Wrapped in 'Google's former CEO just said...' framing but the underlying link list is the substance.

- [Sprytix](https://x.com/sprytixl/status/2063234969510588640) — 2026-06-07: Engagement-farmed hype ('170 AI agents make every company decision') pushing a listicle on running 170–300 parallel agents with Kimi K2.6. Clickbait framing, but the underlying topic — massed parallel agents for research/ops — is real.

- [Livsun](https://x.com/l1vsun/status/2061876167687201243) — 2026-06-03: Off-topic trading engagement-farm: a neural net trained on years of tick data supposedly calling setups hours before the open (71% win rate, built for <$500), promoting a 'win every trade' listicle. Not AI/dev material.

- [Mr. Buzzoni](https://x.com/polydao/status/2060964743402455212) — 2026-05-31: Engagement-farmed ALL-CAPS thread riffing on Karpathy's 'we're in the 1960s of AI' / software-3.0 framing to push the author's own listicle article '...These Are the Ones That Matter [Full GitHub Links]' cataloguing 32 Claude skills. Clickbait wrapper, but the underlying skills roundup may be worth a skim.

- [Livsun](https://x.com/l1vsun/status/2059707097583906917) — 2026-05-28: Off-topic trading content dressed as a discovery: pitches Markov-chain state machines (trending/ranging/reversing transition matrix + Kelly sizing) with a Renaissance Technologies '66% annual returns' framing, promoting a quant listicle. Engagement-farmed, not AI/dev material.

- [Rahul](https://x.com/sairahul1/status/2059632149716942923) — 2026-05-28: Hype-framed ('Anthropic just released the blueprint for a company run by Claude Code; work is dying') push for a listicle on building a SaaS MVP in an afternoon with 7 AI agents. Clickbait wrapper over a real multi-agent build walkthrough.

- [Atenov int.](https://x.com/atenov_d/status/2058868770257416239) — 2026-05-25: Highlights MoneyPrinterTurbo (13k+ stars): give a topic/keyword and it generates a script (via any LLM), pulls copyright-free footage, and adds subtitles/music/voiceover to output a finished short video; runs locally with Web UI/API/Docker/Colab. (Author's other posts are off-topic trading/politics.)

- [Khairallah AL-Awady](https://x.com/eng_khairallah1/status/2057433528363811098) — 2026-05-22: Engagement-framed roundup of a Boris Cherny podcast on why most people don't get results from Claude — they never set it up (CLAUDE.md, features that change how Claude thinks, unopened settings) — claiming ~30-38 untouched features. Links a '40 Features Most Users Have Never Touched' article.

- [CyrilXBT](https://x.com/cyrilxbt/status/2056933229924372546) — 2026-05-20: ALL-CAPS hype ('ANTHROPIC JUST KILLED THE DEMO AGENT ERA') about Anthropic's Agents team showing a production-grade four-layer framework for multi-agent systems in a 30-minute video. (The quoted article is mismatched — about turning Obsidian into a personal OS.)

- [Suryansh Tiwari](https://x.com/suryanshti777/status/2056022182560665602) — 2026-05-18: Highlights Anthropic's official 'claude-code-setup' plugin that scans a project and recommends hooks, skills, MCP servers, subagents, and automations (/plugin install claude-code-setup@claude-plugins-official). A Community Note corrects the post: the plugin is read-only — it recommends but does NOT install or modify files.

- [Mr. Buzzoni](https://x.com/polydao/status/2055197994635424038) — 2026-05-15: Engagement-farmed post about a fired Atlassian infra engineer who allegedly posted a 38-minute breakdown of every system he built: Envoy proxy instead of enterprise load balancers, sidecar architecture for auth/logging/rate limits, DynamoDB + SQS for async provisioning, Packer + SaltStack for VM deployments at scale. 16.3M views, heavy 'save this' framing — substance is generic enterprise-infra patterns, not AI-specific.

- [CyrilXBT](https://x.com/cyrilxbt/status/2055183411619549265) — 2026-05-15: ALL-CAPS engagement-farming thread announcing GitHub's new official certification GH-600 "Agentic AI Developer" — framed as the first formal credential for engineers who operate, supervise, and integrate AI agent teams across the SDLC. Worth knowing the cert exists; treat the framing as hype.

- [Meenakshi Yadav](https://x.com/meenakshiyacs/status/2055104295641710718) — 2026-05-15: Generic agentic-AI architecture "cheat sheet" listing the standard layer stack: goal definition, orchestration, agents, tools, memory, monitoring, reliability (retries/HITL), and governance. No new ideas — useful as a one-slide overview to hand a junior or non-engineer.

- [How To AI](https://x.com/howtoai_/status/2054611399792644386) — 2026-05-15: Hype-framed thread about Google's new "Nested Learning: The Illusion of Deep Learning Architectures" paper (calling it "Attention Is All You Need V2"). Argues that today's LLMs suffer catastrophic forgetting because we treat them as one flat function, and Nested Learning instead models a network as thousands of nested optimization problems at different update frequencies — closer to how brains consolidate short- and long-term memory. Substance is real (Google Research paper), framing is clickbait.

- [Anatoli Kopadze](https://x.com/anatolikopadze/status/2054568935274549597) — 2026-05-15: 18-step listicle on getting more out of Claude (2.4M views). Step 1 — use Projects, not bare chats, so context persists across conversations; later steps cover memory, custom instructions, integrations, and workflows. Listicle framing is engagement-farmy but several tips are practical Claude.ai usage patterns worth knowing.

- [Guri Singh](https://x.com/heygurisingh/status/2054405672176091449) — 2026-05-14: Listicle of 10 side-hustle / digital-product sites (Carrd, Gumroad, Systeme.io, Payhip, Ko-fi, Sellfy, …) framed as 'print money while you sleep'. Off-topic for the AI collection and engagement-farmed; flagging as questionable.

- [Khairallah AL-Awady](https://x.com/eng_khairallah1/status/2054211760631185485) — 2026-05-14: Hype-styled promo pointing to a free 30-min Boris Cherny (creator of Claude Code) walkthrough plus the author's own 'turn Claude into a full-time AI employee in 7 days' course. The Cherny session is the real link worth chasing; the framing is engagement-farmed.

- [Miles Deutscher](https://x.com/milesdeutscher/status/2054310749884002348) — 2026-05-13: Promotion of skillsmp.com — a marketplace claiming over 1 million ready-to-use agent skills and plug-ins. Marketing-heavy "complete game-changer" framing, low actual detail.

- [Charly Wargnier](https://x.com/datachaz/status/2054225085100151163) — 2026-05-13: Charly Wargnier hyping a Rohit article "What to Learn, Build, and Skip in AI Agents (2026)" — invokes Karpathy line that 90% of AI advice dies in 6 months. Signal-vs-noise framing for agent tooling, but very engagement-bait copy.

- [Ronin](https://x.com/deronin_/status/2054255152555545079) — 2026-05-12: Ten token-waste mistakes senior AI engineers stopped making — auto-context loading 50 files for a 30-line fix ($1.20/turn waste), defaulting Opus on lint/format/rename ($0.60 vs Haiku $0.02), tool-call loops resending the full repo on retry, defaulting to Sonnet when Kimi 2.6 matches at 1/6 cost, streaming on stable-prefix workflows killing prompt cache, "just-in-case" file includes blowing 80K-token prompts. Karpathy-quote framing.

- [Roan](https://x.com/rohonchain/status/2054245904258142593) — 2026-05-12: Stanford MDP lecture pitched as a Markov-Chains-for-trading framework — quote of his own article on hedge-fund Markov chain trading. Not AI/agent content; trading/quant finance with engagement-bait framing. Tag as questionable.

- [Muhammad Ayan](https://x.com/socialwithaayan/status/2053875867487777175) — 2026-05-12: Engagement-farmed announcement (all-caps 'BREAKING') that Anthropic open-sourced a Claude Code plugin suite for finance workflows — DCF/LBO models, equity research, M&A analysis, KYC, IC memos — with MCP connectors for Bloomberg, FactSet, S&P Global, Morningstar, and PitchBook (github.com/anthropics/financial-services, Apache-2.0, ~19.8K stars). Top replies flag the obvious caveat: the harness is free but the data feeds (Bloomberg Terminal ~$28K/yr, FactSet/S&P/PitchBook six-figure) are not, and the agents draft work for human sign-off rather than autonomously owning workflows.

- [Himanshu Kumar](https://x.com/codewithimanshu/status/2052573291131589101) — 2026-05-08: Engagement-heavy framing around a free MIT lecture from Jim Simons on quant trading math. Claims Renaissance Technologies-style pattern recognition is now buildable in a weekend with Claude Code (no team of 50 PhDs needed). Hype style; the lecture link itself is the real reference.

- [darkzodchi](https://x.com/zodchiii/status/2052400272840720565) — 2026-05-08: Hype-style pointer to a 22-minute Anthropic Claude team talk on their 2026 agent roadmap — tools, memory, observability, builder-state-of-the-art. Last 3 minutes called out as especially worth watching. Quote-tweets the author's own article on agent reliability (AI agent breaking at 2am, sending 47 broken emails over the weekend, burning $340 in API calls).

- [Allen Braden](https://x.com/allen_explains/status/2052340555942924368) — 2026-05-08: Allen Braden points to a free 1-hour UC Berkeley lecture on systematic-trading fundamentals (the math Jane Street quants use). Engagement-style framing without the actual lecture link — finding it requires follow-through outside the post.

- [Kanika](https://x.com/kanikabk/status/2052032420954927357) — 2026-05-08: Kanika points to a 424-page 'Agentic Design Patterns' guide written by a senior Google engineer — every chapter ships working code, all Amazon royalties go to Save the Children, $40 print price. Engagement-bait framing ('bookmark before it's buried') but the reference itself is a real, comprehensive resource.

- [darkzodchi](https://x.com/zodchiii/status/2050537397377532341) — 2026-05-02: Promotes a security article + .gitignore template after citing that Anthropic allegedly leaked 512K lines of source code from a missing .gitignore entry. Boris Cherny (Claude Code creator) cited as the cautionary tale. Engagement framing, but the .gitignore best-practices angle is legitimately useful.

- [Om Patel](https://x.com/om_patel5/status/2050441119003971683) — 2026-05-02: Promoted Claude Code skill /graphify that pre-builds a graph of your codebase (functions, deps, docs, PDFs, images, audio, video via Whisper) so Claude doesn't waste tokens exploring. Author claims '71.5x more efficient' (engagement-farming framing).

- [regent0x](https://x.com/regent0x_/status/2050143341656838449) — 2026-05-02: Story (likely embellished) about a solo Chinese dev billing $320k/yr by orchestrating 5 specialized Claude agents in parallel: architect, coder, reviewer, tester, ops. Each agent has its own context, no shared state. Engagement-y framing but the parallel-specialist pattern is real.

- [Allen Braden](https://x.com/allen_explains/status/2050163013165224332) — 2026-05-01: Engagement-farming claim that a 'junior at Jane Street' landed $220K-600K by using AI on trillions of data points. Community Note corrects: it's actually a 2024 Horace He talk on ML systems infra at Jane Street — he was a guest speaker, not an employee, and it has nothing to do with AI for trading.

- [摆烂程序媛](https://x.com/wanerfu/status/2050158295911137370) — 2026-05-01: Translated-from-Chinese promotion of Scrapling (github.com/D4Vinci/Scrapling) — open-source web scraper claiming Cloudflare bypass with no selector maintenance and '774x faster than BeautifulSoup'. Useful for AI scrape pipelines if benchmark holds up.

- [How To AI](https://x.com/howtoai_/status/2049567036003795269) — 2026-04-30: Tencent's Training-Free GRPO claims to replace expensive RL fine-tuning by extracting the 'semantic advantage' from trial-and-error and injecting it as a 'token prior' / memory rather than updating weights — reportedly trained for $18. Hype-framed ("killed fine-tuning") but the underlying technique is a notable alternative to GRPO/RLHF that avoids overfitting and GPU costs.

- [Darshak Rana](https://x.com/thedarshakrana/status/2049151671692136778) — 2026-04-30: Long-form personal development X article ('Your Next 5 Years Will Be an Exact Copy of Your Last 5') riffing on the marshmallow test and the idea that personality is a set of learned thought patterns rather than fixed identity. 1.1M views — engagement-farming framing; not AI-related but Jeremy flagged it.

- [Edouard Reinach](https://x.com/ereinach/status/2047802558136058258) — 2026-04-28: Edouard Reinach points to Predict-RLM (github.com/Trampoline-AI/predict-rlm) — production-ready implementation of an MIT memory technique. Quote-tweets a hype-framed (questionable) summary of a Dec 31 2025 MIT CSAIL paper claiming they solved AI memory by 'teaching it how to read' rather than building a bigger brain. The repo is the actionable bit; the quoted framing is sales pitch.

- [Yasir Ai](https://x.com/aiwithyasir/status/2047589529650176333) — 2026-04-28: Hyped pitch ('Breaking', 'terrifying how good') for GitNexus — a knowledge-graph engine for codebases using Tree-sitter AST parsing. Maps every function call, import, class inheritance, interface; clusters code by cohesion; runs blast-radius analysis before changes; coordinates rename across files. MCP-compatible with Claude Code, Cursor, Windsurf. Engagement framing but the underlying capability is interesting.

- [Atal](https://x.com/zabihullahatal/status/2047692175019008019) — 2026-04-25: Engagement-framed ('BREAKING') summary of 'Agent Behavioral Contracts' paper — applies Design-by-Contract (preconditions, invariants, governance rules, recovery mechanisms) as runtime constraints on AI agents instead of prompt-only control. Tested across 1,980 sessions. Real concept (formal verification meets agent runtime) worth tracking under the agents-as-judges concept thread.

- [StacyOnChain](https://x.com/stacyonchain/status/2047278412922831260) — 2026-04-23: Off-topic for AI links — promotional content for centpro.bot (Polymarket trading framework supposedly extracted from 327 real tests). ALL-CAPS engagement framing, crypto-twitter signal. Capturing for completeness but not useful as AI/agents reference.

- [Tech with Mak](https://x.com/technmak/status/2046414820241760620) — 2026-04-21: Summary of Meta's REFRAG paper: compresses retrieved RAG chunks into single embeddings (16,384 tokens → 1,024 chunk embeddings), delivering 30.85x faster time-to-first-token, zero perplexity loss, 16x context extension (4K → 64K), and 3.75x better than prior SOTA. Exploits sparse attention patterns in RAG contexts via precomputable embeddings and RL-based compression policy.

- [Simplifying AI](https://x.com/simplifyinai/status/2046271932035645599) — 2026-04-21: Summary of Microsoft's MEMENTO paper: instead of growing the KV cache to fit long reasoning chains, train the model to break reasoning into blocks and emit dense compressed 'memento' summaries between them, then drop the raw tokens. Framed as 'the secret isn't remembering everything — it's knowing what to forget.' Engagement-farming tone but real underlying paper.

- [Alter Ego](https://x.com/alterego_eth/status/2045093809886020058) — 2026-04-17: Alter Ego promotes Nous Research's Hermes Agent, a self-hosted agent that writes its own skills after each task, keeps persistent memory (MEMORY.md/USER.md/SQLite), and runs 24/7 on a VPS with a closed learn-improve loop every ~15 tool calls, using it to build a self-learning Polymarket weather-trading bot. Heavy promotional/profit framing.

- [Punisher](https://x.com/0x_punisher/status/2044100729133019416) — 2026-04-15: [Promotional / paid partnership] A guide to a Polymarket sweeper bot that profits not by prediction but by FIFO-queueing bids near $0.999 on already-decided markets to absorb mispriced liquidity, covering resolution detection, latency, and capital allocation. Ends with wallet/PnL claims and a Telegram funnel. Off-topic crypto money-making content rather than AI tooling.

- [StacyOnChain](https://x.com/stacyonchain/status/2044069002192847200) — 2026-04-15: [Engagement-farming / crypto promo] StacyOnChain hypes an institutional-grade Polymarket bot architecture (fractional Kelly sizing, latency optimizations), urging readers to bookmark and download before it is pulled, and quote-tweets their own how-we-built-a-Polymarket-bot article. Off-topic relative to the AI tooling collection.

- [How To Prompt](https://x.com/howtoai_/status/2043753502850351525) — 2026-04-14: Hype-framed math claim ('God Particle for calculus'): a paper reportedly shows every elementary function can be generated by one binary operator eml(x,y)=exp(x)-ln(y) plus the constant 1, found by exhaustive search, analogous to the NAND gate. Pitches an AI angle — one uniform trainable circuit instead of juggling math primitives. Interesting if true, but clickbait presentation warrants skepticism.

- [Vaishnavi](https://x.com/_vmlops/status/2043624154646409708) — 2026-04-14: Vaishnavi covers Google's open-sourced Magika — an AI-powered file content type detection tool. Trained on 100M files, 200+ content types, 99% accuracy at 5ms/file. Sees through renamed malware and disguised scripts. Install via pip install magika. github.com/google/magika

- [Noisy](https://x.com/noisyb0y1/status/2043609541477044439) — 2026-04-14: Noisy describes a Google engineer who automated 80% of his work with Claude Code using a CLAUDE.md file based on Karpathy's principles and a .NET orchestration app. Covers the Karpathy-inspired CLAUDE.md, a dotnet service that spawns Claude Code instances with git worktrees, and a review pipeline. Claims $28K passive income working 2-3 hours/day.

- [Defileo](https://x.com/defileo/status/2043437202190024912) — 2026-04-13: Defileo promotes a 'prompt vault' going beyond the classic f/prompts.chat role-based prompts (159K GitHub stars). Claims deeper structured prompts with phases, diagnostic questions, and domain-specific workflows for Claude. Engagement-farming style but references the real prompts.chat repo.

- [Nav Toor](https://x.com/heynavtoor/status/2042879339256254689) — 2026-04-11: Covers Kronos, an open-source foundation model for financial markets trained on 12 billion candlestick records from 45 exchanges (Binance, NYSE, NASDAQ, LSE, and more). Claims 93% more accurate than leading time series models, zero-shot across any asset/timeframe. Built at Tsinghua University, accepted at AAAI 2026. Ships in 4 sizes from 4M to 499M params; live BTC demo running. Available on HuggingFace.

- [Vaishnavi](https://x.com/_vmlops/status/2041869776927261024) — 2026-04-09: Microsoft open-sourced markitdown (github.com/microsoft/markitdown) — a Python tool that converts PDFs, Word docs, Excel, PowerPoint, audio, and YouTube URLs into clean Markdown for LLM pipelines. One pip install replaces custom parsers for file ingestion.

- [cvxv666](https://x.com/antpalkin/status/2041517093670052193) — 2026-04-08: Engagement-farming thread about building a Polymarket prediction market trading bot with Claude. Claims $300→$2.38M strategy. Quote-tweets @adiix_official's viral guide on debugging Claude-built arbitrage bots. Typical crypto/trading bot hype pattern — treat with skepticism.

- [Poonam Soni](https://x.com/codebypoonam/status/2036517669684519362) — 2026-03-25: Teaser thread claiming Anthropic demonstrated a 3-agent system that builds production-quality apps from a single prompt in under 6 hours without human intervention. Architecture details promised in thread. Engagement-farming format ('Breaking') but the underlying multi-agent app-building claim is worth verifying.

- [Millie Marconi](https://x.com/milliemarconnni/status/2036363493478375797) — 2026-03-25: A Claude Code skill (/last30days) scans Reddit and X from the past 30 days on any topic and generates copy-paste-ready prompts based on what's actually working in the community right now — not months-old advice. Works for any domain (Midjourney, Cursor rules, legal prompts, etc.). Open source, MIT license.

- [hoeem](https://x.com/hooeem/status/2035762966952382646) — 2026-03-22: hoeem re-promotes his 'I want to become a Claude Architect (full course)' article covering Claude Code, the Claude Agent SDK, the Claude API, and MCP; framed for engagement ('Be the 1%', 110k+ bookmarks).

- [Kshitij Mishra](https://x.com/daievolutionhub/status/2035396799704547453) — 2026-03-22: Kshitij Mishra shares a 'Claude Code Setup Cheatsheet' based on Boris (creator of Claude Code), quoting Shruti Codes' '2026 AI Engineer roadmap' article; 'Save this' engagement framing.

- [Corey Ganim](https://x.com/coreyganim/status/2034717504505823728) — 2026-03-20: Corey Ganim's playbook for running a one-person 'AI company' stacks three free tools: Paperclip (npx paperclipai — assigns work and tracks progress), gstack (15 specialist Claude Code skills from Garry Tan, with /office-hours, /review, /qa, /ship commands), and autoresearch (Karpathy — 100 overnight experiments); the move is running 10-15 gstack commands in parallel. Quotes Nick Spisak's Paperclip follow-up article.

- [unusual_whales](https://x.com/unusual_whales/status/2033965177918620008) — 2026-03-18: Unusual Whales launched an MCP server that streams live, structured market data to any AI on demand — options flow, dark pools, congressional trades, full financials, technicals, 13Fs, insider activity, and Polymarket data — for building trading bots, dashboards, and screeners (unusualwhales.com/public-api/mcp). 'BREAKING' engagement framing.

- [zostaff](https://x.com/zostaff/status/2033930728044372275) — 2026-03-18: zostaff's clickbait-titled ('How to Quit Your Job in One Day') walkthrough of an autonomous Polymarket trading system built from three agents: Claude (strategist — probability/recommendation/confidence), Codex (engineer — writes and debugs bot code), and OpenClaw (orchestrator — persistent memory, cron, modular skills, Telegram interface that executes trades and logs everything).

- [0xMarioNawfal](https://x.com/roundtablespace/status/2033238044900298844) — 2026-03-16: 0xMarioNawfal amplifies Corey Ganim's article 'Ultimate Claude Cowork Starter Pack: Every Plugin, Skill, and Workflow You Need,' which argues most people install Claude Cowork, poke around for 10 minutes, and revert to ChatGPT because the setup is the hard part.

- [hoeem](https://x.com/hooeem/status/2033146416428708168) — 2026-03-16: A low-substance reaction post ('hoeem style takeover kek') quoting another post that now comes from a suspended account; little usable content beyond the meta-commentary.

- [Meta Alchemist](https://x.com/meta_alchemist/status/2029430826128293906) — 2026-03-05: Roundup of 10 open-source AI memory layers (free, popular on GitHub, some YC-funded) to give coding agents like Claude and Codex better recall than plain memory.md files, with notes on what each is good at and how to combine them. Engagement-styled listicle but substantive.

- [Sukh Sroay](https://x.com/sukh_saroy/status/2029400474739458379) — 2026-03-05: [Post unavailable — account suspended]

- [Tech Layoff Tracker](https://x.com/techlayofflover/status/2029261882834501665) — 2026-03-05: Shares a venting DM from a senior Big Tech SWE (~$350k TC): leadership now touts an "AI leverage ratio" of 4.2x — each engineer shipping the output of a former four-person team — fueling job anxiety. Engagement-styled but a real signal on AI-driven productivity expectations and layoffs.

- [Avid](https://x.com/av1dlive/status/2027429188471558475) — 2026-03-05: Engagement-style 'AI will take your job' listicle, but with a usable career playbook: audit which tasks AI can replicate, learn local agent tooling and stackable 'skills', layer AI-native competence (prompting, orchestration, RAG, automation), shift from executor to system designer, double down on human edge, and build a product/brand.

- [Atharva](https://x.com/atharvaxdevs/status/2028903519802232991) — 2026-03-04: A teaser post aimed at engineers chasing the top 0.01% of "agentic engineering" skill (thread/resource hook).

- [klöss](https://x.com/kloss_xyz/status/2028237936848994369) — 2026-03-02: Flags Anthropic's free AI academy — 13 courses with official certificates covering MCP, APIs, Claude Code, and AI fluency, at anthropic.skilljar.com. Hype framing ('stop what you're doing') but a genuinely useful free resource.

- [Sandhya](https://x.com/agenticgirl/status/2028006725538967614) — 2026-03-02: 'BREAKING'-style but substantive thread on LMCache, an open-source KV-cache layer (6.9K stars, used by Google Cloud, CoreWeave, NVIDIA) that makes the LLM KV cache persistent and shareable across engine instances, tiered GPU→DRAM→disk→S3. Enables instant RAG, disaggregated prefill, and context sharing; integrates with vLLM and SGLang. Apache-2.0, pip install lmcache.

- [Machina](https://x.com/exm7777/status/2026666140987175221) — 2026-02-27: Engagement-farming post ('the ONLY skill you will ever need for Claude, Codex or Openclaw', 'this skill will change your life') quote-tweeting the author's own X article. Behind the hype the underlying topic is a meta-skill/prompting framework meant to change how AI reasons for you; content quality behind the clickbait is unverified.

- [Sukh Sroay](https://x.com/sukh_saroy/status/2026624254800965848) — 2026-02-27: [Post unavailable — account suspended]

- [Ejaaz](https://x.com/cryptopunk7213/status/2025761121328582814) — 2026-02-23: Ejaaz's weekly AI recap: Google shipped Gemini 3.1 (underwhelming to critics) but followed with Lyria 3 song generation and Pomelli one-shot product photoshoots; Microsoft demoed data storage on glass (~10,000-year retention, cheaper than silica); and Taalus fused an AI model directly into silicon at ~17,000 tokens/sec (~17x faster than typical inference).

- [J.B.](https://x.com/vibemarketer_/status/2019435524532904205) — 2026-02-19: J.B. (VibeMarketer) describes a 'recursive self-improvement loop' skill for Claude: instead of prompting once and shipping, the skill generates output, scores it against explicit criteria, diagnoses weaknesses, rewrites, and re-scores until it clears the bar. Cites @maxwellfinn's image-ad skill that grades concepts on 10 criteria (thumb-stop power, curiosity gap, emotional trigger, persona recognition) and won't stop below 9/10.

- [Tech with Mak](https://x.com/technmak/status/2023990222027915746) — 2026-02-18: Tech with Mak boosts Matthew Berman's 'OpenClaw masterclass' video, in which Berman claims to have spent 2.54 billion tokens perfecting the OpenClaw coding agent and walks through 21 daily use cases (markdown files, memory system, CRM, and more). Quoted post had ~1.3M views.

- [Matt Dancho (Business Science)](https://x.com/mdancho84/status/2023738764841894352) — 2026-02-18: Matt Dancho argues that becoming a '10X engineer' now comes down to a well-crafted SKILLS.md file, teasing a thread/resource on how to build one. High-engagement post (~1.1M views) with a lead-gen hook.

- [Spencer Baggins](https://x.com/bigaiguy/status/2021532622963585214) — 2026-02-12: Engagement-style thread claiming 'OpenAI and Anthropic engineers leaked' a technique called 'Socratic prompting' that separates beginners from experts. The substantive nugget: instead of telling the AI what to do, ask it questions. Author claims output quality jumped from 6.2 to 9.1 out of 10.

- [Miles Deutscher](https://x.com/milesdeutscher/status/2012237674409796036) — 2026-01-17: Miles Deutscher promotes a curated 'Claude Code Starter Pack (Part 2)' article by AI Edge - a filtered list of Claude Code tools, tutorials, and resources claimed to be the 1% worth your time. Framing leans on hype ('mega viral', 'extract alpha', 'life-changing systems'), so tagged questionable, but the underlying resource is a legitimate Claude Code tool/resource roundup.

- [fintechjunkie](https://x.com/fintechjunkie/status/2010910565279961423) — 2026-01-13: fintechjunkie gives a glowing, no-edits endorsement of a Dan Koe (@thedankoe) long-form article titled 'How to fix your entire life in 1 day' — a self-improvement/productivity piece rather than an AI or engineering topic. Off-theme for the collection; kept for completeness.

- [Tech with Mak](https://x.com/technmak/status/2002713140757496299) — 2025-12-22: A structured LangGraph learning path (pitched as filling the gap since LangGraph appears in ~half of AI job descriptions). Progresses from basic agent concepts (Pydantic data validation, agentic chatbots, multi-agent coordination) through production systems (a 2.5-hour LangGraph+MCP crash course, debugging/monitoring, deployment architecture) to RAG pipelines (multimodal RAG, hallucination fixes, end-to-end retrieval, Typesense search).

- [Jainam Parmar](https://x.com/aiwithjainam/status/1999815060965994896) — 2025-12-14: An engagement-styled post ('Chain of Thought is dead') claiming that 'Atom of Thought' prompting made models 30-40% more accurate on complex reasoning tasks, pitched as a technique that will change how people use ChatGPT and Claude. Hype framing, but the underlying Atom-of-Thought prompting idea is a real reasoning technique worth a look.

- [Prompter](https://x.com/promptllm/status/1986173095896621150) — 2025-11-06: Prompter claims elite performers all use neuro-linguistic programming (NLP) and offers a prompt that 'teaches you NLP.' Engagement-bait framing with an unsubstantiated claim; the actual prompt is not shown in the post.

- [Charly Wargnier](https://x.com/datachaz/status/1984276199309484409) — 2025-11-01: Charly Wargnier boosts a claim that someone put in 1,000 hours of prompt engineering to distill the 6 prompt patterns that actually matter. Hook post pointing to the six patterns (detailed in the referenced content).

- [Raul Junco](https://x.com/rauljuncov/status/1980243241783197925) — 2025-10-21: Raul Junco frames system design as a staircase to climb step by step rather than jumping to distributed systems: foundations (networking, databases, caching, APIs), then mechanics (queues, consistency, observability, failures), then architecture (trade-offs, evolution, resilience).

- [Prompter](https://x.com/promptllm/status/1974518025211818291) — 2025-10-05: Engagement-style post promoting a prompt for learning to think in systems.

- [Prompter](https://x.com/promptllm/status/1974206336511394165) — 2025-10-04: Engagement-style post promoting a prompt that claims to teach 'NLP' (Neuro-Linguistic Programming) techniques used by high performers.

- [Jawad](https://x.com/jawad_shreim/status/1972998935687172213) — 2025-09-30: Jawad shares a humorous, plain-language 'explanation' of AWS services (EC2, ECS, etc.) quote-tweeted from MilkStraw AI.

- [Aakash Gupta](https://x.com/aakashg0/status/1967135994228166848) — 2025-09-15: Boosts another user's step-by-step roadmap for building your first AI agent, calling it 'gold.' Engagement-style framing; the substantive content lives in the referenced roadmap rather than the post itself.

### General (100)

- [witcheer](https://x.com/witcheer/status/2076717324585898343) — 2026-07-14: witcheer crowdsourced and hand-tallied 250+ replies on how people run Hermes (Nous Research's open model), distilling community local-deployment setups into six summary stats.

- [Dami-Defi](https://x.com/damidefi/status/2073397918447423966) — 2026-07-05: Dami-Defi promotes an Obsidian community plugin (19,184 downloads) that fixes Obsidian's long-open YouTube-embed bug, plus a workflow to turn a messy YouTube-note vault into a visual, AI-powered knowledge system using AI-friendly metadata and automatic thumbnails — arguing structured knowledge bases outperform scattered notes in AI-native workflows. Credits Paul's Obsidian Systems (YouTube).

- [Alex Lieberman](https://x.com/businessbarista/status/2070194343034360004) — 2026-06-25: A "5 levels of work" framework for teaching high agency (credited to @stephsmithio): L1 name a problem; L2 add causes; L3 add possible solutions; L4 add a recommended pick; L5 already fixed it, just keeping you in the loop. Lieberman tells new hires to operate at Level 4 from day one and rise to Level 5 as trust builds.

- [hoeem](https://x.com/hooeem/status/2070072775201444118) — 2026-06-25: Engagement-bait post hyping a quote-tweeted "how to escape the rat race and become financially free" article. No substantive AI content; clickbait framing ("most important article you'll read").

- [Ethan](https://x.com/lambethethan/status/2068958764276051987) — 2026-06-23: Ethan describes a personal wiki of ~1,000 supplements built from 150k papers and 200k health-influencer mentions, and floats handing the entire dataset to an AI agent next.

- [Shenyang Deng](https://x.com/dengshenyang24/status/2065853130567279073) — 2026-06-15: [Post unavailable - page doesn't exist]

- [Lorwen Harris Nagle, PhD](https://x.com/lorwen108/status/2065852553208992218) — 2026-06-14: Off-topic motivational thread on Elon Musk, Nietzsche, and overcoming teenage depression/anxiety through imagination rather than analysis — pop-psychology engagement content with no AI or technical substance.

- [Nav Toor](https://x.com/heynavtoor/status/2065427656112505017) — 2026-06-14: Spotlights Clone-Wars, an open-source GitHub collection (~34,555 stars) by developer Gourav Goyal that catalogues 100+ open-source clones of major apps (Netflix, Spotify, Instagram, Airbnb, WhatsApp, TikTok, Amazon) with source code, demos, and tech stacks listed — e.g., a Netflix clone in React + TMDB API. Started December 2020 and hit GitHub Trending and Hacker News #1.

- [Jeff Tang](https://x.com/jefftangx/status/2064052420888363090) — 2026-06-09: Off-topic for the AI links collection — points to a 57-page Reddit-sourced Google Doc summarizing peptide human trials (BPC-157 et al). Health/biohacking, not AI/agents. Engagement-style 'Bookmark this' framing. Probably an accidental email-to-self.

- [Elon Musk](https://x.com/elonmusk/status/2063401522327666828) — 2026-06-07: Elon Musk endorses first-principles 'physics thinking in the limit' — the 'Magic Wand Number' and 'Idiot Index' as universal cost-engineering mental models. Not AI/dev, but a useful thinking frame.

- [Ihtesham Ali](https://x.com/ihtesham2005/status/2063297401344147719) — 2026-06-07: A well-written essay on The Art of Problem Solving (AoPS): problem-solving is a transferable skill, not memorized formulas; teach the difference between a formula (what to compute) and a method (how to see), and treat confusion as where learning starts. Education/thinking, not AI/dev.

- [shdu](https://x.com/shdu11546816/status/2057642195524419748) — 2026-05-22: Macro speculation that AI triggers a 'Deflationary Doom Loop' via the Paradox of Thrift: agent-driven layoffs push white-collar workers into physical-labor markets, wages crash, and discretionary spending collapses because intelligence isn't the bottleneck for land, energy, and calories. A pessimistic counter to 'everything becomes cheap and abundant.'

- [Jaynit Makwana](https://x.com/jaynitmakwana/status/2055594459426070640) — 2026-05-18: Turns Barbara Oakley's 'Learning How to Learn' science (rereading and highlighting don't work; intuition about learning misleads) into 10 Claude prompts that build a personalized study system from how the brain actually acquires skill.

- [Erik Townsend](https://x.com/erikstownsend/status/2055444404337582106) — 2026-05-16: Erik Townsend flags ex-Goldman commodities chief Jeff Currie's thread calling AI's physical inputs (energy/commodities) 'the most asymmetric trade in modern financial history' — capital chased the AI software trade while ignoring the physical assets AI needs to run.

- [Meenakshi Yadav](https://x.com/meenakshiyacs/status/2055104295641710718) — 2026-05-15: Generic agentic-AI architecture "cheat sheet" listing the standard layer stack: goal definition, orchestration, agents, tools, memory, monitoring, reliability (retries/HITL), and governance. No new ideas — useful as a one-slide overview to hand a junior or non-engineer.

- [Joe Hudson](https://x.com/fu_joehudson/status/2054264609683689941) — 2026-05-14: Coaching post (not AI-specific) — Joe Hudson summarizes his 'dirty fuel to clean fuel' framework for personal energy/motivation on a single page. Off-topic for the collection but in Jeremy's inbox; keeping for completeness.

- [Jaynit](https://x.com/jaynitx/status/2054200520575967698) — 2026-05-14: Personal essay on developing implicit pattern recognition — author tracked his own pre-post predictions on engagement and hit 70-80% accuracy without being able to articulate why. Reflection on tacit-knowledge skill-building, not AI-specific.

- [Michael Eisenberg](https://x.com/mikeeisenberg/status/2054431554240201008) — 2026-05-13: Michael Eisenberg endorses a Zohar Atkins essay applying Jevons Paradox to Torah learning — when knowledge becomes cheap (AI), insight is what matters. Reference to Jevons' 1865 Coal Question. Off-topic for the AI stack but thoughtful framing on the value of insight in an AI-abundant world.

- [Roan](https://x.com/rohonchain/status/2054245904258142593) — 2026-05-12: Stanford MDP lecture pitched as a Markov-Chains-for-trading framework — quote of his own article on hedge-fund Markov chain trading. Not AI/agent content; trading/quant finance with engagement-bait framing. Tag as questionable.

- [Vinay](https://x.com/leashless/status/2051437380788158739) — 2026-05-05: Vinay quote-tweets a viral post about Gödel, Escher, Bach (1979) — Douglas Hofstadter's 800-page Pulitzer-winning book on a logician, artist, and composer that became required reading at every major AI lab. Vinay: "Time stopped. We all read it. It took two years to talk through the implications. Nobody ever forgot."

- [BasedBiohacker](https://x.com/basedbiohacker/status/2049235599874200049) — 2026-05-02: [Off-topic — not AI/tech] Biohacking/nootropics vendor and dosage list at basedbiohacker.any.org, including 'research-only' compounds. Likely sent to the AI inbox by accident.

- [Garry Tan](https://x.com/garrytan/status/2049720409965392052) — 2026-04-30: Garry Tan (YC President & CEO) shipping 10 PRs to GBrain — his personal AI/markdown 'second brain' tool — focused on quality-of-life improvements to make it scale across a corpus of 74k markdown files.

- [Darshak Rana](https://x.com/thedarshakrana/status/2049151671692136778) — 2026-04-30: Long-form personal development X article ('Your Next 5 Years Will Be an Exact Copy of Your Last 5') riffing on the marshmallow test and the idea that personality is a set of learned thought patterns rather than fixed identity. 1.1M views — engagement-farming framing; not AI-related but Jeremy flagged it.

- [PolyArb](https://x.com/usepolyarb/status/2045109166599963026) — 2026-04-18: [Post unavailable — page doesn't exist]

- [Erick](https://x.com/ericksky/status/2044225008419922270) — 2026-04-15: [Post unavailable — login wall or deleted]

- [Paul Bakaus](https://x.com/pbakaus/status/2044118871326765541) — 2026-04-15: Paul Bakaus praises Matt Sims (English PhD plus ML/startup background) for building in the open at the intersection of creativity, storytelling, and AI. Quote-tweets Sims on teaching Claude Code to think systematically, getting consistent answers to recurring review-for-security / sufficient-tests / update-instruction-files prompts.

- [Punisher](https://x.com/0x_punisher/status/2044100729133019416) — 2026-04-15: [Promotional / paid partnership] A guide to a Polymarket sweeper bot that profits not by prediction but by FIFO-queueing bids near $0.999 on already-decided markets to absorb mispriced liquidity, covering resolution detection, latency, and capital allocation. Ends with wallet/PnL claims and a Telegram funnel. Off-topic crypto money-making content rather than AI tooling.

- [StacyOnChain](https://x.com/stacyonchain/status/2044069002192847200) — 2026-04-15: [Engagement-farming / crypto promo] StacyOnChain hypes an institutional-grade Polymarket bot architecture (fractional Kelly sizing, latency optimizations), urging readers to bookmark and download before it is pulled, and quote-tweets their own how-we-built-a-Polymarket-bot article. Off-topic relative to the AI tooling collection.

- [Recogard](https://x.com/recogard/status/2042356576032358505) — 2026-04-10: 36 GB dataset of 72 million Polymarket trades available free on GitHub for prediction market analysis. Includes tools to build trading strategies from historical market data — analyze price behavior before resolution, compare category volatility, and find repeating patterns.

- [cvxv666](https://x.com/antpalkin/status/2041517093670052193) — 2026-04-08: Engagement-farming thread about building a Polymarket prediction market trading bot with Claude. Claims $300→$2.38M strategy. Quote-tweets @adiix_official's viral guide on debugging Claude-built arbitrage bots. Typical crypto/trading bot hype pattern — treat with skepticism.

- [The Curious Tales](https://x.com/thecurioustales/status/2039360822200442914) — 2026-04-02: Self-help/life advice post recommending an article about being '3 decisions away from a completely different life.' Not AI or tech related — personal development content.

- [Erick](https://x.com/ericksky/status/2038301058338812119) — 2026-03-30: Tome — an open-source macOS app that transcribes Zoom/Meet/Teams meetings locally with AI (no cloud), detects speakers, and generates Markdown notes directly into your Obsidian vault. No API keys, no subscriptions, 100% private.

- [BuBBliK](https://x.com/k1rallik/status/2037936518862446694) — 2026-03-29: TurboQuant — Google's algorithm for 3-bit KV cache compression that enables 100K token conversations on a 16GB M2 MacBook with quality identical to cloud APIs. Claims 6x memory compression and 8x speedup with zero accuracy loss. Free paper/algorithm.

- [Suryansh Tiwari](https://x.com/suryanshti777/status/2037892411666645363) — 2026-03-29: Cheat sheet mapping 21 real agent design patterns — prompt chaining, routing, parallelization, reflection, tool use, planning, multi-agent, memory management, MCP, RAG, guardrails, evaluation, and more. Solid reference doc for anyone building agentic systems.

- [Cheng Lou](https://x.com/_chenglou/status/2037713766205608234) — 2026-03-29: Cheng Lou (React/ReasonML creator) released a foundational piece of UI engineering: a fast, accurate, comprehensive userland text measurement algorithm in pure TypeScript that can lay out entire web pages without CSS, bypassing DOM measurements and reflow. 21M+ views, huge community response.

- [hoeem](https://x.com/hooeem/status/2033146416428708168) — 2026-03-16: A low-substance reaction post ('hoeem style takeover kek') quoting another post that now comes from a suspended account; little usable content beyond the meta-commentary.

- [hoeem](https://x.com/hooeem/status/2029167629076676955) — 2026-03-05: A free, beginner-to-expert ranked list of AI learning resources: Anthropic Academy (Claude 101 & AI Fluency), Google AI Essentials, AWS Generative AI Essentials, Elements of AI (University of Helsinki), DeepLearning.AI short courses, and Harvard CS50s Intro to AI with Python.

- [Bojan Tunguz](https://x.com/tunguz/status/2029164042028236942) — 2026-03-05: Reflects on "mid season" knowledge — many roles require grappling with a problem mid-stream without enough runway to catch up on missing context, something even smart people underestimate.

- [Dickson Tsai]([not found]) — 2026-03-05: [Superseded — re-keyed to canonical post 2029235808235078095]

- [vixhaℓ](https://x.com/thevixhal/status/2027763453679841311) — 2026-03-02: Promotes a popular step-by-step article on building a 16-bit CPU from scratch in C (4,000+ bookmarks). A from-scratch systems/architecture learning project rather than AI content.

- [Machina](https://x.com/exm7777/status/2019787951530725396) — 2026-02-07: Machina's thread on how to stop feeling behind in AI: the relentless cadence of releases (GPT-5.3 Codex, Opus 4.6, Kling 3.0, all 'redefining everything') creates a low-grade, never-ending pressure. His reframe is that the problem isn't too much happening, it's the lack of a personal filter for what actually matters to your work.

- [Yishan](https://x.com/yishan/status/2012067968331710639) — 2026-01-16: [Post deleted/unavailable]

- [Bojan Tunguz](https://x.com/tunguz/status/2011949233658925298) — 2026-01-16: [Post deleted/unavailable]

- [Meta Alchemist](https://x.com/meta_alchemist/status/2010882913784070231) — 2026-01-16: [Post deleted/unavailable]

- [Simplifying AI](https://x.com/simplifyinAI/status/2010878423325364233) — 2026-01-16: [Post deleted/unavailable — in Jan 3-16 dead zone]

- [Sahil Bloom](https://x.com/SahilBloom/status/2010703181900464151) — 2026-01-16: [Post deleted/unavailable — in Jan 3-16 dead zone]

- [geoff](https://x.com/GeoffreyHuntley/status/2010567043629113814) — 2026-01-15: [Post deleted/unavailable — in Jan 3-16 dead zone]

- [will brown](https://x.com/willccbb/status/2010547008387408150) — 2026-01-15: [Post deleted/unavailable — in Jan 3-16 dead zone]

- [James Shields](https://x.com/scaling_shields/status/2010413738506264649) — 2026-01-15: [Post deleted/unavailable — in Jan 3-16 dead zone]

- [siddhi surana](https://x.com/siddhisurana/status/2010361699087921253) — 2026-01-15: [Post deleted/unavailable — in Jan 3-16 dead zone]

- [Jaime Jorge](https://x.com/jaimefjorge/status/2010254648389550243) — 2026-01-15: [Post deleted/unavailable — in Jan 3-16 dead zone]

- [BOOTOSHI](https://x.com/KingBootoshi/status/2010002905316757751) — 2026-01-14: [Post deleted/unavailable — in Jan 3-16 dead zone]

- [Matt Pocock](https://x.com/mpocock/status/2009888462821732368) — 2026-01-14: [Post deleted/unavailable — in Jan 3-16 dead zone]

- [fintechjunkie](https://x.com/fintechjunkie/status/2010910565279961423) — 2026-01-13: fintechjunkie gives a glowing, no-edits endorsement of a Dan Koe (@thedankoe) long-form article titled 'How to fix your entire life in 1 day' — a self-improvement/productivity piece rather than an AI or engineering topic. Off-theme for the collection; kept for completeness.

- [bluecow](https://x.com/bluecow/status/2009065743606194185) — 2026-01-12: [Post deleted/unavailable]

- [Nozz](https://x.com/nozz/status/2008835341649346666) — 2026-01-12: [Post deleted/unavailable — in Jan 3-16 dead zone]

- [Nick Dobos](https://x.com/dobosn/status/2008036181346656365) — 2026-01-10: [Post deleted/unavailable]

- [Param](https://x.com/param_bharadwaj/status/2007915284024619160) — 2026-01-10: [Post deleted/unavailable — in Jan 3-16 dead zone]

- [Felipe Coury](https://x.com/felipecoury/status/2007882656892014636) — 2026-01-10: [Post deleted/unavailable]

- [kitze](https://x.com/kitze/status/2007809540919521316) — 2026-01-10: [Post deleted/unavailable — in Jan 3-16 dead zone]

- [Rohit](https://x.com/rohitxo/status/2007748502661742686) — 2026-01-10: [Post deleted/unavailable — in Jan 3-16 dead zone]

- [Aakash Gupta](https://x.com/AakashGuptaGH/status/2007704814065365016) — 2026-01-10: [Post deleted/unavailable — in Jan 3-16 dead zone]

- [elvis](https://x.com/elvisnguyen/status/2007665597046087848) — 2026-01-10: [Post deleted/unavailable — in Jan 3-16 dead zone]

- [nader dabit](https://x.com/dabit3/status/2007623542340276413) — 2026-01-10: [Post deleted/unavailable — in Jan 3-16 dead zone]

- [dei](https://x.com/delilahime/status/2007599629893906627) — 2026-01-10: [Post deleted/unavailable — in Jan 3-16 dead zone]

- [Brandon Gell](https://x.com/brandongell/status/2007537024606646369) — 2026-01-10: [Post deleted/unavailable — in Jan 3-16 dead zone]

- [Alex Hillman](https://x.com/alexhillman/status/2007195403503431942) — 2026-01-09: [Post deleted/unavailable — in Jan 3-16 dead zone]

- [dei](https://x.com/delilahime/status/2007112398968512604) — 2026-01-09: [Post deleted/unavailable — in Jan 3-16 dead zone]

- [Lior Alexander](https://x.com/lioralexander/status/2006763456879984843) — 2026-01-08: [Post deleted/unavailable — in Jan 3-16 dead zone]

- [Josh Pigford](https://x.com/joshpigford/status/2006722184752509040) — 2026-01-08: [Post deleted/unavailable — in Jan 3-16 dead zone]

- [Tom Dörr](https://x.com/tom_dorr/status/2006640889625956454) — 2026-01-08: [Post deleted/unavailable — in Jan 3-16 dead zone]

- [Ryan Carson](https://x.com/ryancarson/status/2006579357155549261) — 2026-01-08: [Post deleted/unavailable — in Jan 3-16 dead zone]

- [Jeffrey Emanuel](https://x.com/jfemanuel13/status/2006283589341868394) — 2026-01-07: [Post deleted/unavailable]

- [Tech with Mak](https://x.com/TechWithMak/status/2006215651880165597) — 2026-01-07: [Post deleted/unavailable — in Jan 3-16 dead zone]

- [Obie Fernandez](https://x.com/obiefernandez/status/2006152066925707274) — 2026-01-07: [Post deleted/unavailable — in Jan 3-16 dead zone]

- [Melvin Vivas](https://x.com/melvinator/status/2006020697936482443) — 2026-01-07: [Post deleted/unavailable — in Jan 3-16 dead zone]

- [Sumanth](https://x.com/Sumanth_077/status/2005956018357575750) — 2026-01-07: [Post deleted/unavailable — in Jan 3-16 dead zone]

- [Md Ismail](https://x.com/mdismail/status/2005671283621953665) — 2026-01-06: [Post deleted/unavailable — in Jan 3-16 dead zone]

- [Simplifying AI](https://x.com/simplifyinAI/status/2005513621646409748) — 2026-01-06: [Post deleted/unavailable — in Jan 3-16 dead zone]

- [Josh Schultz](https://x.com/jschultzme/status/2005421815916028959) — 2026-01-06: [Post deleted/unavailable — in Jan 3-16 dead zone]

- [Trending GitHub](https://x.com/TrendingGitHubl/status/2005310239286649010) — 2026-01-06: [Post deleted/unavailable — in Jan 3-16 dead zone]

- [The Boring Marketer](https://x.com/BoringMarketer/status/2005239063816110289) — 2026-01-06: [Post deleted/unavailable — in Jan 3-16 dead zone]

- [Tom Dörr](https://x.com/tom_dorr/status/2005167892304969882) — 2026-01-06: [Post deleted/unavailable — in Jan 3-16 dead zone]

- [Santiago](https://x.com/santiagoemeli/status/2005035706842611040) — 2026-01-06: [Post deleted/unavailable — in Jan 3-16 dead zone]

- [hoeem](https://x.com/hoeemlim/status/2004948633556197506) — 2026-01-06: [Post deleted/unavailable — in Jan 3-16 dead zone]

- [Matt Pocock](https://x.com/mpocock/status/2004505491297665063) — 2026-01-05: [Post deleted/unavailable]

- [Daniel San](https://x.com/dcsan/status/2003544127356903508) — 2026-01-03: [Post deleted/unavailable]

- [sankalp](https://x.com/sankalpdev/status/2003384719234969898) — 2026-01-03: [Post deleted/unavailable — in Jan 3-16 dead zone]

- [CloudAI-X](https://x.com/CloudAI_X/status/2003298874369306643) — 2026-01-03: [Post deleted/unavailable — in Jan 3-16 dead zone]

- [Grok](https://x.com/XAI/status/2003101023145590851) — 2026-01-03: [Post deleted/unavailable]

- [Yu Lin](https://x.com/yulintwt/status/2004537183978590695) — 2025-12-27: [Account suspended]

- [Abhishek Singh](https://x.com/0xlelouch_/status/2002673253912113644) — 2025-12-22: A reflective essay on career fulfillment in software engineering: you don't magically know whether backend, frontend, infra, ML, startups, big tech, or management will fulfill you — you only find out through reps. Early on people confuse novelty (new frameworks, jobs, titles) with fulfillment; real self-knowledge is earned by shipping boring features, debugging 3am outages, owning systems, and sticking with things long enough to feel the responsibility.

- [Hayes](https://x.com/hayesdev_/status/1996897853642592428) — 2025-12-07: [Account suspended]

- [Hayes](https://x.com/neatprompts/status/1981241949173825687) — 2025-10-24: [Account suspended]

- [keshav](https://x.com/kshvbgde/status/1974835291358969895) — 2025-10-07: Post (likely video/thread) on Steve Jobs's principles for designing insanely great products.

- [Jawad](https://x.com/jawad_shreim/status/1972998935687172213) — 2025-09-30: Jawad shares a humorous, plain-language 'explanation' of AWS services (EC2, ECS, etc.) quote-tweeted from MilkStraw AI.

- [maxleedev](https://x.com/maxleedev/status/1962938769914658984) — 2025-09-03: Announces a canvas-style interface for LLMs, built in response to a viral post arguing chat UIs need git-like branching/forking of conversations to explore alternate threads without derailing the main one.

- [Aadit Sheth](https://x.com/aaditsh/status/1953462911961374889) — 2025-08-09: [Post deleted/unavailable]

- [Pau Labarta Bajo](https://x.com/paulabartabajo_/status/1815990574580699209) — 2024-07-25: [Post deleted/unavailable]

- [Santiago](https://x.com/svpino/status/1800151091461652740) — 2024-06-11: A 15-part thread giving an intuitive explanation of matrix multiplication as the crucial idea underlying modern machine learning.

---
## Full Chronological List

### Jul 2026

- **2026-07-16** | [Aaron Levie](https://x.com/levie/status/2077526010753581156) | management, agent-design, industry
  Aaron Levie's notes from a dinner with enterprise IT leaders on agent adoption: change management is the biggest blocker (processes and data pipelines must be modernized to work with agents), embedding engineers directly into business functions as internal forward-deployed engineers dramatically accelerates successful agent rollouts, and the technical function is becoming more strategically important than ever.

- **2026-07-16** | [0xSero](https://x.com/0xsero/status/2077488957999173936) | research, industry
  0xSero highlights Thinking Machines' launch of Inkling (thinkingmachines.ai/news/introducing-inkling), a 950B-parameter American open-weight model that reasons across text, image, and audio modalities with full weights released. Available for fine-tuning on Thinking Machines' Tinker platform and via the Inkling Playground.

- **2026-07-16** | [Superman](https://x.com/thesupermanmx/status/2077321341490090486) | research, dev-practices
  turbovec (github.com/RyanCodrai/turbovec) is a vector index built on TurboQuant, written in Rust with Python bindings — a performance-oriented approximate nearest-neighbor index relevant to embedding search and RAG pipelines.

- **2026-07-15** | [Ashpreet Bedi](https://x.com/ashpreetbedi/status/2077169299777531942) | agent-design, dev-practices
  Ashpreet Bedi (Agno) shares a new post, Self-Driving Agent Infrastructure (ashpreetbedi.com/self-driving-agent-infrastructure), arguing AI/software engineering is the first domain to gain autonomous 'self-driving' capabilities, and walking through how he built his self-driving agent platform.

- **2026-07-14** | [Alvaro Videla](https://x.com/old_sound/status/2076932819008242037) | research, dev-practices
  Alvaro Videla released LeetLLM (github.com/videlalvaro/leet-llm) — a free, problem-based course of 48 lessons for building a small LLM inference engine on Apple Silicon in Swift and Metal, progressing from dot products and GEMV through attention and token generation.

- **2026-07-14** | [JoePro](https://x.com/joepro/status/2076877282312954311) | skills-mcp, prompting, dev-practices
  JoePro shares a reworked 'Frontend Design Skill' (an agent/Claude skill spec) engineered to produce distinctive, production-grade UIs that avoid recognizable AI-generated tropes — covering success criteria (signature visual identity, complete states, WCAG AA accessibility, token-driven design systems) and a context-gathering routine before writing code.

- **2026-07-14** | [witcheer](https://x.com/witcheer/status/2076717324585898343) | research, general
  witcheer crowdsourced and hand-tallied 250+ replies on how people run Hermes (Nous Research's open model), distilling community local-deployment setups into six summary stats.

- **2026-07-14** | [How To Prompt](https://x.com/howtoprompt__/status/2076689880026096089) | agent-design, skills-mcp, industry, questionable
  How To Prompt highlights an open-source, privacy-first Chromium fork built by an ex-Google engineer with a native AI agent, built-in MCP server, Cowork-style web+local-file agents, scheduled autopilot tasks, 40+ app integrations (Gmail, Slack, Notion, Linear, Figma, Salesforce), and local-model (Ollama) support — drivable from Claude Code or Gemini CLI. Engagement-framed but describes a real agentic-browser tool worth evaluating.

- **2026-07-14** | [Alex Prompter](https://x.com/alex_prompter/status/2074198124898181121) | prompting, claude-code, questionable
  Alex Prompter's thread pitches 'cloning' Fable 5's reasoning into Opus 4.8 before Fable 5 shifts to pay-per-use credits — extracting a model's 'operating manual' as a portable prompt and transplanting it onto a cheaper model to keep the way it thinks rather than the model itself. Engagement-framed but a real prompt-portability technique.

- **2026-07-13** | [Jamon Holmgren](https://x.com/jamonholmgren/status/2076001786700394610) | agent-design, dev-practices, skills-mcp
  Jamon Holmgren dumps his complete agentic coding setup as a 10+ point checklist: an AGENTS.md that acts as a router to skills/docs/tools; a customized workflow skill (he recommends grabbing Matt Pocock's skills); self-healing, greppable docs with a 7-line summary header; agents that actually run and test the app themselves; e2e tests plus docs on how/what to test; custom precommit linters with --fix that shell out to a cheaper LLM (Composer 2.5 or Sonnet) to actually fix rather than flag; cross-agent review (codex/claude/cursor, never the same model reviewing itself) at research/plan/implementation/wrap-up; handoff worksheets committed with git tags so another agent can finish the job; automatic end-of-session agent feedback docs he periodically ingests to improve workflows; a tools/bin folder of agent-authored scripts (e.g. an agent_review CLI wrapper); and periodic agent sweeps through recent commits. Practical, adoptable patterns for a team running coding agents.

- **2026-07-09** | [Kodus](https://kodus.io/self-hosted-ai-code-review/) | dev-practices, agent-design
  Kodus (github.com/kodustech/kodus-ai) — open-source AGPLv3 self-hosted AI code review. The full PR-review pipeline (Kody agent) runs on your own infrastructure with bring-your-own-LLM: it posts line-anchored inline comments covering logic/security/performance (or 'deep mode' with parallel bug/security/performance specialists), keeps source code, LLM calls, and audit trails inside your VPC, and supports GitHub Enterprise Server / GitLab Self-Managed / Bitbucket DC and air-gapped deploys. Jeremy flagged it to evaluate for work code reviews.

- **2026-07-07** | [How To Prompt](https://x.com/howtoprompt__/status/2074122800961614184) | agent-design, skills-mcp, questionable
  How To Prompt (hype framing: "China has killed the vector database industry") flags Tencent's newly open-sourced TencentDB Agent Memory — local long-term memory for AI agents that runs 100% on plain SQLite with no external vector DB or cloud APIs. Claims 61% fewer tokens and PersonaMem accuracy 48%->76%. Uses a layered 'semantic pyramid' (L0 conversation -> L1 atom -> L2 scenario -> L3 persona) stored as inspectable markdown + Mermaid graphs instead of opaque vector compression, with drill-back to raw logs by node_id. ~5.1k GitHub stars.

- **2026-07-07** | [Ryan Carson](https://x.com/ryancarson/status/2074093250399330418) | agent-design, dev-practices, management
  Ryan Carson (@HelloUntangle) details orchestrating the largest/riskiest engineering program in the company's history with a single Fable parent orchestrator session: 834 files, prod data mutation, DB schema update, 31 PRs, started Friday->completed Monday, zero prod incidents. One parent Devin/Fable session planned the work, spawned ~40 child sessions to execute, enforced regression gates and backup checks between phases, and escalated only owner-level decisions (scope rulings, go/no-go on irreversible steps). Distills reusable program-management patterns for large migrations. In a follow-up he asks Cognition to let child Devin sessions pick their own model/mode independent of the parent.

- **2026-07-06** | [Satyam Pariyar](https://x.com/spariyar07/status/2074142974095835518) | agent-design, dev-practices
  Satyam Pariyar shares Kybernetes (github.com/pariyar07/kybernetes), a small OSS experiment: a 'loop governor' / runtime-adaptive control plane for agentic coding work, aimed at governing coding-agent execution loops at runtime.

- **2026-07-06** | [leopardracer](https://x.com/leopardracer/status/2074071476181876944) | questionable, management, agent-design
  Engagement-farmed take (ALL CAPS) claiming an Anthropic engineer said memory/retrieval architecture is the only skill worth learning in 2026 — arguing prompt writers cap ~$90k, engineers building memory/retrieval systems clear $250-400k, and those architecting 'the whole loop' pull seven figures ('architecture is the moat, memory is the new distribution'). Quote-tweets CyrilXBT's article 'How To Become An AI Engineer in 2026 (Without a CS Degree).' Mostly hype, thin substance.

- **2026-07-06** | [ericosiu](https://x.com/ericosiu/status/2073943223836270933) | agent-design, management, skills-mcp
  Eric Siu shares a 7-step checklist for building a 'Company Brain' (an org-wide AI agent): (1) pick one high-value workflow closest to revenue; (2) map only the critical connectors (Google Drive, Slack, CRM, Gong, Granola); (3) define memory — brand voice, decisions, workflow rules, examples, with recent decisions weighted over old ones; (4) set permissions/approvals/data exposure to avoid 'a security problem with a chat interface'; (5+) route the work. A practical playbook for company-wide AI adoption.

- **2026-07-06** | [Isra](https://x.com/israfill/status/2073789727698743516) | agent-design, skills-mcp, questionable
  Isra flags Alibaba's newly open-sourced Page-Agent (~22K GitHub stars, +949 in a day) — an MIT-licensed JavaScript library that embeds an AI agent directly into any webpage via a single <script> tag. It reads the live DOM as structured text and acts as the real user with no headless browser, Selenium/Playwright, Python server, or computer vision. Works with any LLM (GPT, Claude, Grok, Qwen, local via Ollama), has built-in human confirmation before critical actions, and can pair with the Web Speech API for voice control. Pitched as a lightweight replacement for Selenium/Playwright and vision-based browser agents.

- **2026-07-06** | [Akshay](https://x.com/akshay_pachaar/status/2073783428735250595) | agent-design, management
  Akshay Pachaar explains building a '1-person AI company' that runs locally, is 100% open-source, has no human employees (all agents), and collaborates in real time via email. His framing: multi-agent orchestration isn't new, but instead of hand-wiring a graph of nodes/edges you should model coordination on the org-chart structure companies have used for a century — lay out an org chart, each agent fills one role with reporting lines, and work flows up/down without manually relaying each message.

- **2026-07-06** | [kaize](https://x.com/0x_kaize/status/2073743517155774641) | agent-design, dev-practices, prompting
  kaize shares a 'Loop engineering' reading list, arguing 2026 agents are less about smarter prompts and more about longer runs — the real questions are whether an agent can recover from a failed step, control spend, and know when to stop. Curated links: Addy Osmani (addyosmani.com/blog/loop-engineering), Firecrawl (firecrawl.dev/blog/loop-engineering), Oracle 'What is the AI agent loop', OpenAI 'Harness engineering', and Martin Fowler 'Harness engineering for coding agent users'.

- **2026-07-06** | [0xSero](https://x.com/0xsero/status/2073651251594854573) | research, prompting, agent-design
  0xSero (quote-tweeting Rohan Paul on a Meta paper showing quantized reasoning models often fail because compression makes them doubt a correct answer instead of finishing) reports experimenting with penalizing 'self-doubt' words during generation — claiming ~30% fewer output tokens — plus improving tok/s via CPU offloading.

- **2026-07-06** | [Anatoli Kopadze](https://x.com/anatolikopadze/status/2068328135611822149) | agent-design, prompting, claude-code
  Anatoli Kopadze's widely-viewed piece 'Loops explained: Claude, GPT, Mira and what actually works' argues most people use AI the slow way (type, wait, fix, repeat by hand) and that the faster approach top AI engineers care about is building loops. Covers what loops are, how they work under the hood, when they're worth it vs a trap, and how to build a basic one in Claude or ChatGPT. Quote-tweets Peter Steinberger: you shouldn't be prompting coding agents, you should be designing loops that prompt your agents. (Includes some self-promotion for his X/Telegram.)

- **2026-07-05** | [Dami-Defi](https://x.com/damidefi/status/2073397918447423966) | general, questionable
  Dami-Defi promotes an Obsidian community plugin (19,184 downloads) that fixes Obsidian's long-open YouTube-embed bug, plus a workflow to turn a messy YouTube-note vault into a visual, AI-powered knowledge system using AI-friendly metadata and automatic thumbnails — arguing structured knowledge bases outperform scattered notes in AI-native workflows. Credits Paul's Obsidian Systems (YouTube).

- **2026-07-05** | [Anatoli Kopadze](https://x.com/anatolikopadze/status/2073396351279276397) | claude-code, prompting, questionable
  Anatoli Kopadze (quote-tweeting his own Claude features guide) shares an Anthropic engineer's claim that most people use Sonnet 5 and Fable 5 wrong and can set them up right in one afternoon to stop overpaying — a 31-minute session on testing each model against your real use case, plus a guide to Claude features '99% of users never find.'

- **2026-07-05** | [Nyk](https://x.com/nyk_builderz/status/2073305434069647735) | agent-design, claude-code, skills-mcp
  [Jeremy flagged: urgent for orchestration] Nyk released Council of High Intelligence v1.2.0 as a Claude Code plugin (/plugin marketplace add 0xNyk/council-of-high-intelligence) — an 18-persona deliberation engine (Aristotle, Feynman, Kahneman, Torvalds, Socrates, Taleb, Meadows + more) that runs 3 rounds of anonymized cross-examination to one auditable verdict on your existing subscriptions, no API keys. v1.2.0 adds confidence-weighted verdicts (vote weight scales with stated confidence; a hesitant council escalates to you instead of forcing consensus, per Roundtable Policy + ConfMAD 2025), per-persona reasoning methods (Socratic elenchus, Taleb tail stress-testing, Meadows causal-loop mapping via DMAD), per-project defaults via .council.yaml, and CI parity gates so the Claude/Codex/Gemini coordinators can't silently drift.

- **2026-07-05** | [Elvis](https://x.com/elvissun/status/2073161303997452794) | skills-mcp, agent-design, dev-practices, claude-code
  Elvis makes a meta point about eval-driven skill building that extends beyond coding to any knowledge problem where an eval set can be concretely defined. Example: a newsjack.sh skill that judges newsworthiness — he started from labeled examples (stories that made real news vs ones that didn't, e.g. hitting #1 on Product Hunt isn't news even though LLMs say it is), fed them into an eval set, then used /goal to iterate a skill implementation that lets 3 agents (Opus, Sonnet, Haiku) all score stories correctly — proving 'the intelligence lives in the skill, not the model.' Notes Fable's ability to learn across examples and draw a through-line is well beyond Opus.

- **2026-07-05** | [Aaron Levie](https://x.com/levie/status/2073138135014502777) | industry, agent-design, management
  Aaron Levie (Box CEO) argues the battle in AI is shaping up to be a battle for context: agent effectiveness comes down to having the right domain expertise, access to the right context and tools, and being embedded in workflows users can easily review and incorporate. The platforms that capture and leverage the best context within their agents — and pick the right model per task — will be where agents do their best work (coding, legal, support agents at scale). This is why the applied-AI layer is worth far more than being an 'LLM wrapper': the value is in organizing the critical knowledge.

- **2026-07-05** | [Avid](https://x.com/av1dlive/status/2073114542851416260) | agent-design, claude-code, prompting, questionable
  Avid (ALL CAPS engagement framing) makes a practical context-engineering point: give an agent one index file per major folder for a direct line to what it needs. The same task dropped from 2 minutes (7 files opened, wandering, a 3-month-old brief still missing) to 10 seconds with the same model, nothing else changed. 'Build the path or watch it search in the dark.' Quote-tweets Machina's article 'How to build a second brain with Fable 5.'

- **2026-07-05** | [Sprytix](https://x.com/sprytixl/status/2073101741604679714) | agent-design, prompting, questionable
  Sprytix (clickbait 'Anthropic just leaked an internal engineering document' framing) lays out a six-layer self-improving agent loop: Generate -> Evaluate -> Remember -> Schedule -> Optimize -> Recurse. Generation produces its own solutions (no human brief), Evaluation is a second layer that can say no, Memory retains useful discoveries each cycle, Scheduling decides what happens next, Optimization updates behavior based on what worked, and Recursion means removing any single layer drops performance significantly — shifting the human from operator to designer.

- **2026-07-05** | [alex fazio](https://x.com/alxfazio/status/2073091833530392614) | agent-design, research, dev-practices
  alex fazio recommends studying ARC-AGI-winning harnesses to learn harness engineering from first principles — they clearly illustrate what works, what's BS, and why a lot of current harness design is overfitted to benchmark-maxxing.

- **2026-07-05** | [darkzodchi](https://x.com/zodchiii/status/2072973531768328626) | claude-code, prompting, questionable
  darkzodchi's 'Claude Fable 5 Setup Guide' covers which heavy tasks actually deserve Fable 5, the new safeguards that reroute you to Opus, and how to plan the free window (up to 50% of weekly limit free until July 7). Recaps a reported Fable 5 timeline: launched June 9, pulled June 12 under a US export-control order tied to a jailbreak report, back online July 1. (Includes Telegram self-promo.)

- **2026-07-05** | [me](https://x.com/twetsfyp/status/2072939523160285688) | questionable, claude-code
  Engagement-farmed clickbait promoting a 16-minute tutorial on building '$50,000 cinematic websites' step by step with Claude Fable 5 ('Mito Claude is back in an insane way'). Little substance in the post itself. 1.9M views.

- **2026-07-04** | [Tom Dörr](https://x.com/tom_doerr/status/2073354493794636248) | skills-mcp, claude-code, agent-design
  Tom Dörr shares VoltAgent's awesome-claude-skills (github.com/VoltAgent/awesome-claude-skills) — a curated 'awesome list' of official agent Skills from leading engineering teams.

- **2026-07-04** | [0xSero](https://x.com/0xsero/status/2073274981279260774) | claude-code, agent-design, dev-practices, skills-mcp
  0xSero shares Parcels (github.com/0xSero/parcels) — a tool for 'cloud agents' when you have Tailscale and more than one desktop: it packages your repo plus a live coding-agent session (Claude Code / Codex / pi), transfers it to another machine on your Tailscale network, and runs it in tmux so you can step away from the screen.

- **2026-07-04** | [ali](https://x.com/waterloo_intern/status/2073171123542573231) | questionable, research
  ali (@waterloo_intern) — an apparent parody of distillation hype: claims to have distilled 2.3M Claude Fable 5 reasoning traces into Qwen3-4B with '100% self-consistency @ 512 samples, 0.00 bits output entropy, zero hallucination variance,' that 'the student is not bounded by the teacher,' and that it 'converged on one universal truth,' with open-sourced weights. 3M views; reads as satire rather than a real result.

- **2026-07-04** | [akira](https://x.com/realmcore_/status/2073170941878944022) | agent-design, dev-practices, research
  akira introduces Onyx, a VM/runtime for programmable agent orchestration that 'turns orchestration into software engineering.' The article covers the design constraints and decisions behind the VM and how to write programs and architect agent systems on it. Framing: agents are inherently non-deterministic (that's the point), but breaking execution into structured steps (Plan, Implement, Review, QA) plus scripts/tools/skills to steer, share context, and guardrail agents improves performance. References ReAct and related arxiv papers and karpathy/autoresearch.

- **2026-07-04** | [Archive](https://x.com/archiveexplorer/status/2073136973162872897) | claude-code, agent-design, skills-mcp, dev-practices, questionable
  Archive (engagement framing, 'met an Anthropic engineer making $1.2M') argues the real lever isn't Opus vs Sonnet but 'what the model wakes up into' — the .claude/ folder: CLAUDE.md (the contract), settings.json (permissions), hooks/ (reflexes), agents/verifier (a shift-notes checker subagent), skills/ (~33 reusable 'muscle memories'), .mcp.json (tools), and MEMORY.md (shift log). 'You write the folder once; the folder runs the model.' Quote-tweets his own article 'Loop and Harness engineering: 7 files, 5 steps.'

- **2026-07-04** | [ℏεsam](https://x.com/hesamation/status/2073104617706008840) | management, industry
  [Jeremy flagged: read for work] hesam recommends Phil Chen's article 'Career advice in the age of AI' (Chen: a researcher from OpenAI, DeepMind, and Stanford). TL;DR: AI makes execution cheaper, so the durable edge is choosing the right problems, building strong connections, and investing real time — the argument being that AI models improve at anything you can write a loss function for, and school is mostly loss functions (well-defined problems graded against known answers), so the valuable work shifts elsewhere.

- **2026-07-04** | [Thariq](https://x.com/trq212/status/2073101078145724589) | prompting, claude-code, agent-design
  Thariq shares his article 'A Field Guide to Fable: Finding Your Unknowns' — the most important part of working with Claude Fable 5 is discovering your own unknowns so you can prompt it better. Framing: 'the map is not the territory' — your prompts, skills, and context are the map (a representation of the work to be done), and the practice is surfacing what you don't yet know about the actual work.

- **2026-07-04** | [Daniel Miessler](https://x.com/danielmiessler/status/2073076322390384798) | prompting, claude-code
  Daniel Miessler shares a set of 'prompts to run now that you have Fable back' — a quick collection of prompts to try with Claude Fable 5 following its return.

- **2026-07-04** | [Akshay](https://x.com/akshay_pachaar/status/2072961737008336937) | agent-design, dev-practices, research, prompting
  Akshay Pachaar summarizes a Hugging Face blog post on 'evolving the harness' instead of training the model: they took a frozen open model scoring 0% on a hard legal-agent benchmark, left its weights untouched, and let an automated loop rewrite only the surrounding harness code (the runtime wrapper that feeds context, runs tool calls, and decides when a run ends). It ended up essentially matching Sonnet 4.6 on the headline metric at ~7x lower cost per task, zero weights changed. The insight: the 0% wasn't measuring legal reasoning — the model reasoned correctly but saved outputs under the wrong filename/folder or not at all — so it was measuring the harness.

- **2026-07-04** | [Rahul](https://x.com/sairahul1/status/2072749611471835229) | agent-design, dev-practices, prompting
  Rahul shares a free 'Loop Library' (signals.forwardfuture.com/loop-library/) of reusable agent loops, plus his article '20 Loop Design Patterns Every AI Engineer Should Know.' Framing: most engineers can build an agent (a worker) but few can build a system that gets better after the first attempt — and that gap is 'worth six figures.'

- **2026-07-02** | [Dhilip Subramanian](https://x.com/sdhilip/status/2072334422414876957) | claude-code, skills-mcp, dev-practices
  Dhilip walks through his 7-skill Claude Code setup and what each earns its spot for: data engineering (dbt/Airflow), gstack, grill-me, superpowers (spec/plan/TDD), impeccable (UI audit), last30days, and printing-press (API/site to token-light CLI). Advice: start small, add a skill only when you hit a job your current ones can't do.

- **2026-07-02** | [Andrew Ng](https://x.com/andrewyng/status/2071988145667928442) | agent-design, dev-practices, claude-code, management
  Andrew Ng's 'loop engineering' letter lays out three nested loops for building 0-to-1 products: the fast agentic coding loop (agent writes/tests/iterates every few minutes), the developer feedback loop (human steers over tens of minutes to hours), and the slow external feedback loop (alpha testers, A/B tests over days). Humans retain a context advantage, so engineers increasingly play a partial product-management role.

### Jun 2026

- **2026-06-29** | [Akshay](https://x.com/akshay_pachaar/status/2071509401224261823) | agent-design, dev-practices, claude-code, skills-mcp
  Walkthrough of Google's Agents CLI as tooling for Karpathy's "agentic engineering" (spec design, eval loops, security). One setup command injects 7 ADK-specific skills into a coding agent; author built and deployed a RAG agent end-to-end with Claude Code, including 20 LLM-as-judge eval scenarios and enterprise registration.

- **2026-06-29** | [Boris Cherny](https://x.com/bcherny/status/2071379474277613732) | management, claude-code, industry
  As engineering/product/design/DS roles blur, Cherny proposes five team archetypes (not tied to job function): Prototyper, Builder, Sweeper, Grower, Maintainer. Healthy teams need different mixes by product maturity — pre-PMF wants 1+2+3, growing wants 2+3+4+some 5, strong-PMF wants 3+4+5+some 2.

- **2026-06-27** | [zostaff](https://x.com/zostaff/status/2070852153594290195) | agent-design, claude-code, dev-practices, prompting
  Long-form "Loop Engineering" article: four autonomous loops that actually pay off because the task repeats, a machine can reject the result, the agent carries it whole, and "done" is objective. Covers the bare while-loop/exit-code/budget mechanics under Claude Code Routines and four worked configs: morning CI test triage (with maker-checker subagent), dependency watchdog, doc synchronizer, and overnight research digest. Theme: the harder the verification, the more you can hand the loop; soft verification keeps a human in the loop.

- **2026-06-27** | [Brian Armstrong](https://x.com/brian_armstrong/status/2070670644577280109) | management, industry, dev-practices, agent-design
  Coinbase's playbook for keeping AI spend flat while token usage grows: better defaults (experimenting with cheaper open-weight models like GLM 5.2 / Kimi 2.7 via an LLM gateway, since 91% never hit caps), better routing (frontier for planning, cheaper for execution), better caching (LibreChat cache-hit rate 5% → 60%), lean context, and usage visibility. Cut AI spend nearly in half while token usage kept growing.

- **2026-06-27** | [Prajwal Tomar](https://x.com/prajwaltomar_/status/2070545372880245179) | agent-design, questionable
  Pro tip framed around the author's promotional "Hermes Agent" article: rather than just reading an article, paste it into an agent session and tell it to update itself, read the playbook, and set up whichever features help your workflow. Thesis: articles are becoming playbooks your agent runs for you. Heavy self-promotion / engagement framing.

- **2026-06-27** | [Brady Long](https://x.com/thisguyknowsai/status/2070445026233172314) | skills-mcp, agent-design, claude-code, questionable
  Promo-styled writeup of MemPalace, an open-source local AI memory tool (49K stars). Instead of dumping everything into semantic search, it organizes memory into a structured "palace" (people/projects as wings, topics as rooms, verbatim text in searchable drawers). Claims 96.6% retrieval recall on LongMemEval with zero LLM/API/cloud, 98.4% with a hybrid pipeline; ships 29 MCP tools and auto-save hooks for Claude Code. Python 3.9 + ChromaDB, ~300MB, MIT.

- **2026-06-25** | [Alex Lieberman](https://x.com/businessbarista/status/2070194343034360004) | management, general
  A "5 levels of work" framework for teaching high agency (credited to @stephsmithio): L1 name a problem; L2 add causes; L3 add possible solutions; L4 add a recommended pick; L5 already fixed it, just keeping you in the loop. Lieberman tells new hires to operate at Level 4 from day one and rise to Level 5 as trust builds.

- **2026-06-25** | [Jason Weston](https://x.com/jaseweston/status/2070117091521204521) | research, agent-design
  Paper announcement ("Autodata", arXiv:2606.25996): agentic data creation as a way to convert increased inference compute into higher-quality model training data. Claims gains on CS, legal, and math problems over classical synthetic-data methods, plus a way to meta-optimize the data-scientist agent so it produces even stronger data. Thread (1/6).

- **2026-06-25** | [hoeem](https://x.com/hooeem/status/2070072775201444118) | questionable, general
  Engagement-bait post hyping a quote-tweeted "how to escape the rat race and become financially free" article. No substantive AI content; clickbait framing ("most important article you'll read").

- **2026-06-25** | [Nav Toor](https://x.com/heynavtoor/status/2069773963413340297) | skills-mcp, dev-practices, agent-design, questionable
  Listicle-styled promo for MinerU, an open-source document-extraction tool (68.5K stars) from Shanghai AI Lab's OpenDataLab. Reads PDFs/Office docs/scanned images into clean Markdown with reading-order text, tables → HTML, equations → LaTeX, OCR, 109 languages, batch mode, and 10k-page docs via sliding window. CLI, Python SDK, or web app; plugs into Claude Desktop, Cursor, LangChain, LlamaIndex, etc. Apache-2.0-based license, free.

- **2026-06-25** | [Akshay](https://x.com/akshay_pachaar/status/2069769689560187027) | agent-design, dev-practices, claude-code, skills-mcp
  Breakdown of "loop engineering" (opening on a Karpathy quote about removing yourself as the bottleneck): a trigger decides what runs, the loop is the maker, a separate checker grades output (a model grading itself just justifies its work), and state lives on disk not context (suggests Zep's Graphiti temporal knowledge graph). Two failure points: set the exit condition before the loop runs, and add observability on the harness since the checker only catches in-run failures (suggests Comet's Opik). Thesis: the model is a commodity; the loop around it is where the engineering lives.

- **2026-06-25** | [Hugging Models](https://x.com/huggingmodels/status/2069750892287721960) | research, industry, questionable
  Brief hype post: NVIDIA released an FP4 quantized MoE version of Qwen3.6 that fits in 35B parameters but runs with the efficiency of a ~3B model, pitched as a win for efficient inference.

- **2026-06-23** | [Mario Zechner](https://x.com/badlogicgames/status/2069156188902559751) | research, industry
  Mario Zechner recommends a video dissecting Voxtral, a family of open-source speech models, and the foundational work behind it (audio tokenization, semantic/acoustic disaggregation). He quote-tweets Julia Turc, who frames it as what you get when you plug LLMs into voice assistants instead of a decade of handwritten rules.

- **2026-06-23** | [Dhilip Subramanian](https://x.com/sdhilip/status/2069140867466797200) | industry, dev-practices
  Dhilip Subramanian, a heavy dictation user (44,414 words via Wispr Flow), recommends FluidVoice: a free, open-source, locally-run macOS voice-to-text tool that needs no API key and handles slang well. He cancelled his paid plan after switching.

- **2026-06-23** | [0xSero](https://x.com/0xsero/status/2069114653842522463) | research
  0xSero recommends an educational YouTube video explaining LoRA (Low-Rank Adaptation): how tiny trainable matrices let anyone fine-tune large AI models relatively cheaply.

- **2026-06-23** | [Matthew Berman](https://x.com/matthewberman/status/2069098257444434425) | agent-design, skills-mcp, dev-practices
  Matthew Berman announces a new Loop Library feature, Lazy Loops (aka Discover), which scans your codebase and chat threads to find potential agentic loops and designs them for you. Links the Forward-Future/loop-library GitHub repo of practical, repeatable AI-agent workflows.

- **2026-06-23** | [Ethan](https://x.com/lambethethan/status/2068958764276051987) | agent-design, general
  Ethan describes a personal wiki of ~1,000 supplements built from 150k papers and 200k health-influencer mentions, and floats handing the entire dataset to an AI agent next.

- **2026-06-23** | [冬天](https://x.com/seventhoce56019/status/2068901168940745088) | skills-mcp, agent-design, research
  Translated from Chinese: a writeup of reverse-skill (GitHub zhaoxuya520/reverse-skill), an AI skill package that puts reverse-engineering and security tasks behind a routing.md file so the agent self-triages across 20+ sub-skills (APK reversing, IDA static analysis, JS frontend reversing, firmware security, EDR evasion, vulnerability exploitation). Framed as lowering the barrier to security offense/defense.

- **2026-06-23** | [Sakana AI](https://x.com/sakanaailabs/status/2068862070062485867) | agent-design, industry, research
  Sakana AI announces Fugu, an orchestration model that routes across a swappable pool of underlying agents rather than relying on one monolithic model. Their blog argues orchestration is the next frontier and a hedge for AI sovereignty against vendor export controls; Fugu reportedly matches leading models (Fable, Mythos) on engineering, science, and reasoning benchmarks.

- **2026-06-23** | [Movez](https://x.com/0xmovez/status/2068763235587694769) | agent-design, prompting, questionable
  Movez highlights an Andrew Ng talk on building self-improving agentic systems from scratch, quoting Ng that AI agents now handle 100% of his tasks and that self-improving loops will replace prompting within 3-6 months. Quote-tweets his own article on a 300-agent swarm running on Kimi K2.6 verified by Opus 4.8. Heavy promotional framing.

- **2026-06-23** | [Avi Chawla](https://x.com/_avichawla/status/2068657496936616314) | research, agent-design, dev-practices
  Avi Chawla explains why BM25, a 30-year-old keyword ranking algorithm with no training or embeddings, still powers Elasticsearch/OpenSearch and excels at exact-match retrieval where embeddings struggle, making hybrid (BM25 + vector) search the default in top RAG systems. He closes on the UX problem of highlighting which span actually drove a semantic match, pointing to his co-founder's article.

- **2026-06-23** | [Codez](https://x.com/0xcodez/status/2064374643729773029) | agent-design, dev-practices, claude-code, skills-mcp, prompting
  A long-form Loop engineering roadmap arguing the leverage point in agentic coding has moved from writing prompts to designing self-running loops. Covers the 4-condition test for when a loop is worth building (task repeats, automated verification, token budget, senior-engineer tooling), the five building blocks (automations like /loop and /goal, git worktrees, skills, MCP connectors, sub-agents), the maker/checker split, the Ralph Wiggum quiet-failure mode, comprehension debt and cognitive surrender, and the security tax of unattended loops. Cites Anthropic engineering docs and Addy Osmani.

- **2026-06-17** | [How To Prompt](https://x.com/howtoprompt__/status/2067176008445513800) | research, questionable
  Engagement-farmed post claiming an open-source repo compresses 60M text chunks from 201GB to ~6GB (97% smaller) with no accuracy loss, running fully private on a standard laptop with no cloud or GPU — pitched as making vector databases obsolete. No repo link was surfaced in the post or visible replies, so the project would need to be located before the claim can be evaluated.

- **2026-06-17** | [Viv](https://x.com/vtrivedy10/status/2066954487466459163) | agent-design, dev-practices
  Viv amplifies Sydney Runkle's X article 'The Art of Loop Engineering,' which argues reliable agents need more than a good model — they need a carefully engineered hierarchy of loops. Viv's key takeaway: verification is a critical primitive; it's worth spending days to weeks making the distribution of desired agent outcomes verifiable in practice by your system, especially for non-slop, semi-long-horizon work.

- **2026-06-17** | [Ahmad](https://x.com/theahmadosman/status/2066825976705646929) | research, industry
  Ahmad highlights VibeThinker 3B (built on Qwen 2.5), a 3B-parameter model he claims reaches Opus 4.5-level performance, quoting his own earlier prediction that Claude Code + Opus 4.5-quality models will run locally on a single RTX PRO 6000 before year-end. A signal on how fast small/efficient local models are closing the gap with frontier models.

- **2026-06-16** | [Jaynit](https://x.com/jaynitx/status/2066506535250092378) | management, dev-practices, questionable
  Thread relaying Elon Musk's 5-step engineering 'algorithm': (1) make the requirements less dumb / question them, (2) try to delete the part or process step entirely (if you aren't forced to add ~10% back, you didn't delete enough), (3) simplify and optimize, (4) accelerate cycle time, (5) automate — with the warning that the most common mistake of smart engineers is optimizing something that shouldn't exist.

- **2026-06-15** | [Hasan Toor](https://x.com/hasantoxr/status/2066247422502957197) | agent-design, skills-mcp, dev-practices
  Highlights Headroom, a GitHub tool by Netflix engineer Tejas Chopra that compresses everything an AI agent reads before it reaches the LLM (tool outputs, logs, files, RAG chunks, code-search results, conversation history), claiming 60-95% fewer tokens for the same answers. Ships as a Python/TypeScript library, local proxy, and MCP server, with wrappers for Claude Code, Codex, Cursor, Aider, and Copilot.

- **2026-06-15** | [Teknium](https://x.com/teknium/status/2066185784332562605) | agent-design, skills-mcp
  Demo: the author used the Hermes Agent with a Manim video-generation skill plus its TTS tool to autonomously produce a video explaining the Hermes Agent itself — a self-referential showcase of composing a skill and a tool inside an agent.

- **2026-06-15** | [Avid](https://x.com/av1dlive/status/2066127265407336535) | dev-practices, research, questionable
  Argues you can run capable AI models locally on a Mac for free using Apple's MLX stack — install mlx-lm, launch its server, and point any agent at localhost. Cites a ~23-minute talk from an Apple MLX-team engineer in which a local model builds a working SwiftUI app from a blank Xcode project in two minutes and then fixes a bug, with nothing leaving the machine. Quote-tweets a piece on the ThinkStation PGX local-inference box.

- **2026-06-15** | [Olivia Chowdhury](https://x.com/oliviacoder1/status/2066064093552038070) | research, agent-design, questionable
  Hype-framed thread on a Dec 31, 2025 MIT CSAIL paper that claims to 'solve' AI memory not by building bigger context windows but by teaching models how to read/retrieve — positioning the result against the industry's context-window arms race and the 'context rot' problem, where a model's performance on information already in context degrades as more is packed in.

- **2026-06-15** | [Shenyang Deng](https://x.com/dengshenyang24/status/2065853130567279073) | general
  [Post unavailable - page doesn't exist]

- **2026-06-14** | [Lorwen Harris Nagle, PhD](https://x.com/lorwen108/status/2065852553208992218) | questionable, general
  Off-topic motivational thread on Elon Musk, Nietzsche, and overcoming teenage depression/anxiety through imagination rather than analysis — pop-psychology engagement content with no AI or technical substance.

- **2026-06-14** | [Harry Tandy](https://x.com/harrytandy/status/2065818850633932996) | agent-design, dev-practices, claude-code
  Opens with a Sam Altman quote that the cost to use a given level of AI falls ~10x every 12 months, then lays out a 10-step agentic-coding sprint: pick the heaviest backlog item, write a FABLE_RUN.md spec (goal/scope/commands/review rules/done criteria), map the repo first, break the job into checkpoints that each end with diff + test output + next decision, split builder and checker agents, use git worktrees for parallel attempts, and keep a RUN_LOG.md of every failed command and accepted fix.

- **2026-06-14** | [Avid](https://x.com/av1dlive/status/2065747876005937416) | claude-code, skills-mcp, agent-design, dev-practices, questionable
  Promotes a 'second brain' pattern attributed to Karpathy: let an LLM maintain a wiki of your notes so knowledge compounds as you dump sources and it reads, links, and files them. Points to a free Claude Code plugin, claude-obsidian by AgriciDaniel (claude plugin marketplace add AgriciDaniel/claude-obsidian; claude plugin install claude-obsidian@agricidaniel-claude-obsidian), then run /wiki inside an Obsidian folder. Quote-tweets the author's own article on building Obsidian from scratch with 13+ Kimi agents.

- **2026-06-14** | [Nav Toor](https://x.com/heynavtoor/status/2065427656112505017) | dev-practices, general, questionable
  Spotlights Clone-Wars, an open-source GitHub collection (~34,555 stars) by developer Gourav Goyal that catalogues 100+ open-source clones of major apps (Netflix, Spotify, Instagram, Airbnb, WhatsApp, TikTok, Amazon) with source code, demos, and tech stacks listed — e.g., a Netflix clone in React + TMDB API. Started December 2020 and hit GitHub Trending and Hacker News #1.

- **2026-06-13** | [Avi Chawla](https://x.com/_avichawla/status/2065727218991735000) | agent-design, dev-practices, prompting
  Explains 'loop engineering' (framed with a Karpathy quote about removing yourself as the bottleneck and maximizing leverage): move the operator's two manual jobs — deciding what the agent runs next and checking its output — into the system itself. A schedule decides what to run, a maker loop produces the work, a separate checker agent grades the output, and a file on disk holds the shared state both read; the loop runs until done, max iterations, or budget is exhausted.

- **2026-06-13** | [Marie Haynes](https://x.com/marie_haynes/status/2065531158356717721) | agent-design, skills-mcp, dev-practices, industry
  Flags Google's new Open Knowledge Format (OKF): a standardized way to store information as a directory of interlinked markdown files that acts as a living wiki agents can query and edit, which the author thinks could replace Notion or Obsidian. References Google Cloud's blog post and the spec at github.com/GoogleCloudPlatform/knowledge-catalog (okf/SPEC.md), and notes feeding both links to Antigravity to brainstorm project uses.

- **2026-06-13** | [Suryansh Tiwari](https://x.com/suryanshti777/status/2065473893817848266) | claude-code, skills-mcp, agent-design, questionable
  Claims Anthropic released an official Claude Code plugin, claude-code-setup, that scans your project and recommends and sets up hooks, skills, MCP servers, subagents, and automations step-by-step (install: /plugin install claude-code-setup@claude-plugins-official), arguing most people run Claude Code vanilla and miss the surrounding ecosystem. Quote-tweets the author's own 'Unveil' build. (Treat the 'official' claim as unverified.)

- **2026-06-12** | [Codez](https://x.com/0xcodez/status/2065097407965127142) | agent-design, claude-code, prompting, questionable
  Hype-framed thread claiming an Anthropic 'Managed Agents' team demo showing how to build self-improving agent systems with the Fable 5 model from scratch in ~13 minutes, using /loops, dynamic workflows, and 'dreaming.' Quote-tweets the author's own 14-step article on the same. (Strong engagement-farming framing; claims unverified.)

- **2026-06-11** | [hoeem](https://x.com/hooeem/status/2065098599751471454) | agent-design, prompting
  Quote-tweets his own long-form X article 'Why you should not be looping & what to do instead' — a contrarian breakdown pushing back on the popular agentic self-looping pattern (taking aim at a 'leading voice in AI') and proposing alternatives. The substance is in the linked article; framing is deliberately provocative.

- **2026-06-11** | [Nainsi Dwivedi](https://x.com/nainsidwiv50980/status/2064947761779208476) | dev-practices, agent-design, questionable
  Alibaba open-sourced 'open-code-review' (Apache-2.0), the internal AI code reviewer that's run on their codebase for ~2 years — 20,000+ engineers, 1M+ reviews. Design: deterministic engineering handles what must never fail (file selection, bundling, rule matching, comment positioning) while the LLM only does context reading, codebase search, and reasoning. Claims ~1/5 the token cost of a generic agent + skills and precise line-level comments that don't drift on large changesets. Repo name: open-code-review.

- **2026-06-11** | [Meta Alchemist](https://x.com/meta_alchemist/status/2064431279383433646) | prompting, dev-practices, claude-code, questionable
  Shares a copy-paste 'Repo Audit & Improvement Plan' prompt — a structured, 4-phase principal-engineer audit (Phase 1 discovery/mapping before judging, then a prioritized, actionable improvement plan), with instructions to cite file paths and line numbers and to flag anything unverifiable. Useful prompt template, but wrapped in hype framing around a nonexistent 'Claude Fable 5' model.

- **2026-06-11** | [Boris Cherny](https://x.com/bcherny/status/2064426115255730578) | claude-code, agent-design, dev-practices
  Boris Cherny (Anthropic / Claude Code) on why self-verification loops matter: letting a model check its own work lets it run autonomously for much longer and land closer to your intent, so you check in less. Points to a breakdown by @delba_oliveira (via @ClaudeDevs) on encoding your manual checks so Claude Code closes its own feedback loop.

- **2026-06-09** | [Paweł Huryn](https://x.com/pawelhuryn/status/2064201950980096078) | agent-design, prompting
  Lists six patterns for Anthropic-style dynamic agent workflows/loops: classify-and-act (one agent decides type, code routes), fan-out-and-synthesize (per-piece agents merged in code), adversarial verification (separate rubric-checker), generate-and-filter (many candidates → dedupe → survivors), tournament (judges compare different attempts), and loop-until-done (spawn until a stop condition). Each with a concrete example. Links his 'Claude Dynamic Workflows' guide.

- **2026-06-09** | [hoeem](https://x.com/hooeem/status/2064099329342640285) | skills-mcp, prompting
  hoeem hypes Matt Pocock's new /teach skill — pours 10 years of teaching experience into a Claude skill that teaches you anything (Pocock's demo: it taught him to solve a Rubik's cube). Worth a look as a reusable Claude Code skill pattern.

- **2026-06-09** | [Jeff Tang](https://x.com/jefftangx/status/2064052420888363090) | general, questionable
  Off-topic for the AI links collection — points to a 57-page Reddit-sourced Google Doc summarizing peptide human trials (BPC-157 et al). Health/biohacking, not AI/agents. Engagement-style 'Bookmark this' framing. Probably an accidental email-to-self.

- **2026-06-09** | [BOOTOSHI](https://x.com/kingbootoshi/status/2063999432077795579) | claude-code, agent-design, prompting
  Long personal write-up: BOOTOSHI claims the agent-orchestrating-subagents pattern (token-maxxing across parallel work) was right for opus-4.5/gpt-5 but is no longer optimal with the newer generation (gpt-5.5, opus-4.8). Argues the extended context window + intelligence means these models are now more capable as a single 'MEGA THREAD' with a single operator. Counter-trend to the multi-agent enthusiasm of early 2026.

- **2026-06-09** | [Peter Yang](https://x.com/petergyang/status/2063988122720055772) | agent-design, claude-code, management
  Five takeaways from a conversation with @kunchenguid (ex-Meta L8 engineer) on agentic engineering: (1) plan and validate, don't code yourself — you're the always-on team's manager; (2) plan quality determines how long agents run autonomously — a detailed spec can run for hours vs minutes for a one-liner; (3) use visual plans, not walls of markdown — Lavish (github.com/kunchenguid/lavish) generates visual HTML plans; (4 and 5 truncated in scrape — likely about validation rubrics and feedback loops).

- **2026-06-09** | [Ahmad](https://x.com/theahmadosman/status/2063935919481106560) | research, dev-practices
  Self-study curriculum for LLM serving engines and GPU kernel programming: start with vLLM / SGLang / TensorRT-LLM / FlashInfer (PagedAttention, continuous batching, prefix caching), then dive into Triton, CUTLASS/CuTe, FlashAttention papers, PagedAttention paper, MoE docs, Nsight profiling. Followed by a hands-on project sequence (Triton RMSNorm, fused SiLU×gate, etc.). For people actually wanting to learn the inference stack.

- **2026-06-09** | [rody](https://x.com/0x_rody/status/2063722061126651935) | claude-code, prompting
  Quotes 'Anthropic's main manager': 'Nobody types prompts from scratch. The commands should be live in the project.' Points to a 26-min talk walking through Anthropic's command library every new dev inherits on day one. Links the author's own article 'How to Build a Claude Code Slash Command Library' with a template inside — argues devs spend ~10 hours/month re-typing context that should be a single saved command.

- **2026-06-08** | [darkzodchi](https://x.com/zodchiii/status/2063559498078278109) | claude-code, prompting
  Quotes 'Anthropic engineer Margot van Laer': 'Every prompt you type more than twice should be a file. The ones we use internally aren't memorized, they're saved.' Points to a 33-min talk on the prompt patterns Anthropic packages and reuses across every Claude Code session — links the same Claude Code slash-command-library template from rody.

- **2026-06-08** | [Rahul](https://x.com/sairahul1/status/2063544956158185927) | agent-design, dev-practices, industry
  Long-form X article framing 'Harness Engineering' as the most important AI discipline of 2026 — OpenAI shipped 1M lines of production code in Feb 2026 using agents wrapped in a reliable system (the 'harness'); Anthropic published 3 papers on it; ThoughtWorks formalized a framework; Philipp Schmid called it the most important discipline of 2026. Article walks through what a harness is and the mental models needed to actually use it. 1.1M views — the term is breaking out of AI-infra circles fast.

- **2026-06-08** | [rari](https://x.com/0xwhrrari/status/2063244577482440978) | claude-code, skills-mcp, questionable
  Engagement-farmed but useful link dump of free AI-engineering learning resources (LangChain agent architecture, Anthropic's Claude Code 101 + in-action courses, prompt engineering docs, anthropics/courses interactive prompt tutorial, claude.md docs, skills, MCP). Wrapped in 'Google's former CEO just said...' framing but the underlying link list is the substance.

- **2026-06-07** | [Rahul](https://x.com/sairahul1/status/2063609922667815064) | agent-design, dev-practices, research
  Rahul follow-up to his Harness Engineering article: points to walkinglabs.github.io/learn-harness-engineering as 'the best site on the internet to learn harness engineering' — free, comprehensive. Most AI engineers haven't heard the term yet. Worth bookmarking alongside his article.

- **2026-06-07** | [Viv](https://x.com/vtrivedy10/status/2063429138304668093) | agent-design, prompting, research
  A default recipe for optimizing Agent = Model + Harness, 'training' both: (1) build v1 on a sensible base harness with task-specific prompting/tools, (2) harness-engineer against prod-like eval tasks (often enough on its own), (3) SFT on mined traces or synthetic data (good for distilling a cheaper model), (4) RL if you can design environments/rewards to push past SFT copying, (5) light harness engineering again on the trained model. Argues harness engineering will be the dominant optimization lever and most companies are still at steps 1-2; links the 'Anatomy of an Agent Harness' article.

- **2026-06-07** | [Elon Musk](https://x.com/elonmusk/status/2063401522327666828) | management, general
  Elon Musk endorses first-principles 'physics thinking in the limit' — the 'Magic Wand Number' and 'Idiot Index' as universal cost-engineering mental models. Not AI/dev, but a useful thinking frame.

- **2026-06-07** | [Hanako](https://x.com/hanakoxbt/status/2063305395687522702) | agent-design, claude-code
  Describes an Anthropic 'dreaming agents' memory pattern: a second set of agents that, after you log off, reopen every session, fact-check the first agents, merge duplicates and burn stale memory — up to 100 at once, ~95% cached so a full rewrite costs almost nothing. Points to a multi-agent code/review/deploy team guide.

- **2026-06-07** | [Ihtesham Ali](https://x.com/ihtesham2005/status/2063297401344147719) | general
  A well-written essay on The Art of Problem Solving (AoPS): problem-solving is a transferable skill, not memorized formulas; teach the difference between a formula (what to compute) and a method (how to see), and treat confusion as where learning starts. Education/thinking, not AI/dev.

- **2026-06-07** | [Sprytix](https://x.com/sprytixl/status/2063234969510588640) | questionable, agent-design
  Engagement-farmed hype ('170 AI agents make every company decision') pushing a listicle on running 170–300 parallel agents with Kimi K2.6. Clickbait framing, but the underlying topic — massed parallel agents for research/ops — is real.

- **2026-06-06** | [Dan Roy](https://x.com/roydanroy/status/2062917394356429092) | research
  Category-theory joke quoting Markus Buehler's claim of a breakthrough in self-evolving AI 'scientists' moving from search to principled discovery — where the search space itself changes and the AI perceives that shift without intervention.

- **2026-06-06** | [海拉鲁编程客 (hylarucoder)](https://x.com/hylarucoder/status/2062881239900766292) | agent-design, dev-practices
  Recommends Peter Pang's 'Building cloud agent infrastructure' — most agent frameworks assume a desktop (one user, one machine, local filesystem, keys in env vars); cloud agent infra changes those assumptions.

- **2026-06-06** | [Cat Wu (Anthropic)](https://x.com/_catwu/status/2062408623565984209) | claude-code, agent-design, dev-practices
  Anthropic's data team automated ~95% of business-analytics queries with Claude; the linked blog covers their approach to skills, data foundations, evals, ablations, and online validation for data-analysis agents.

- **2026-06-04** | [hoeem](https://x.com/hooeem/status/2062443798647517197) | agent-design, dev-practices
  Points to a guide on making agentic workflows ~100x cheaper by fixing token waste in the orchestration loop.

- **2026-06-04** | [さいぺ (cipepser)](https://x.com/cipepser/status/2062397559520502225) | agent-design, research
  Praises mem0's 'State of Memory in Agent Harness' survey — well-organized coverage from field papers/benchmarks through memory implementations in each coding agent (Cursor, Devin, Claude Code, Codex).

- **2026-06-04** | [Ole Lehmann](https://x.com/itsolelehmann/status/2061911202830401564) | agent-design, dev-practices, skills-mcp
  A ~10-minute recipe to turn your X bookmarks into an agent-queryable second brain: export bookmarks (twitter-web-exporter / BookmarkSave), drop the file into your LLM wiki or Obsidian vault, and have your agent convert each into a tagged markdown note with the original link — then query across the whole pile. Directly relevant to this link collection.

- **2026-06-03** | [yv](https://x.com/yvbbrjdr/status/2061914706579984551) | research
  Recommends the MAI-Thinking-1 technical paper as containing almost all the details for training a SOTA LLM (microsoft.ai PDF).

- **2026-06-03** | [Thariq](https://x.com/trq212/status/2061907538741006796) | claude-code, agent-design, skills-mcp
  Announces dynamic workflows as the biggest Claude Code upgrade since skills and subagents — Claude writing its own task-specific harness on the fly — with excitement about the non-technical tasks it unlocks.

- **2026-06-03** | [Thariq](https://x.com/trq212/status/2061907337154367865) | claude-code, agent-design, skills-mcp
  Full Anthropic article on dynamic workflows in Claude Code: Claude writes its own JavaScript harness to spawn/coordinate subagents (own models, own worktrees, resumable), countering agentic laziness, self-preferential bias and goal drift. Covers patterns (fan-out-and-synthesize, adversarial verification, tournament, loop-until-done), many use cases (migrations, deep research, triage, root-cause, evals, model routing), the 'ultracode' trigger, token budgets, and when NOT to use it.

- **2026-06-03** | [Garry Tan](https://x.com/garrytan/status/2061878212213572083) | industry, agent-design, management
  Garry Tan on model routing as strategy: frontier labs will want their harness to be the moat, but the consumer-best outcome is model capabilities flattening and commoditizing — 'a preview of the AI Harness Wars of 2027.' Cites Factory's auto model-router (claimed 25% cost cut at frontier performance).

- **2026-06-03** | [Livsun](https://x.com/l1vsun/status/2061876167687201243) | questionable
  Off-topic trading engagement-farm: a neural net trained on years of tick data supposedly calling setups hours before the open (71% win rate, built for <$500), promoting a 'win every trade' listicle. Not AI/dev material.

- **2026-06-03** | [Tom Dörr](https://x.com/tom_doerr/status/2061674811122713013) | skills-mcp, dev-practices, agent-design
  Shares FlowForge, a Skill that generates professional draw.io diagrams from natural language (github.com/wentong2022-arch/flowforge-skill).

### May 2026

- **2026-05-31** | [darkzodchi](https://x.com/zodchiii/status/2061040686330257656) | claude-code, agent-design, skills-mcp
  Anthropic-engineer clip: build 5 focused agents (code review, tests, docs, security) in an afternoon, each ~15 minutes as a markdown file with instructions + prompt. Links a beginner subagent-building template.

- **2026-05-31** | [Mr. Buzzoni](https://x.com/polydao/status/2060964743402455212) | claude-code, questionable, skills-mcp
  Engagement-farmed ALL-CAPS thread riffing on Karpathy's 'we're in the 1960s of AI' / software-3.0 framing to push the author's own listicle article '...These Are the Ones That Matter [Full GitHub Links]' cataloguing 32 Claude skills. Clickbait wrapper, but the underlying skills roundup may be worth a skim.

- **2026-05-31** | [恒星](https://x.com/vintcessun/status/2060897802478293013) | skills-mcp, research, agent-design
  DeepMind packaged 30+ scientific databases (AlphaGenome, UniProt) into agent skills. The real bottleneck for science agents isn't model quality but knowing how to call databases correctly; skills turn each DB's API into clear instructions + scripts so agents execute step-by-step. One-line npx install (github.com/google-deepmind/science-skills).

- **2026-05-31** | [Chesny](https://x.com/chesnyfcb/status/2060818732654481693) | agent-design, prompting
  Polemical pitch (translated) for a 3D 'knowledge galaxy' second brain à la Karpathy: 378 notes auto-generated ~1,854 nodes and ~3,856 connections, surfacing hidden links and missing connections. Pragmatic takeaway: start with an automated Obsidian + Claude vault that extracts content, finds connections, and writes daily reports.

- **2026-05-29** | [0xSero](https://x.com/0xsero/status/2060128492247740640) | agent-design, dev-practices
  Recommends Peter Steinberger's 'Just Talk To It — the no-bs Way of Agentic Engineering' (steipete.me): after trying every elaborate workflow, the author keeps returning to a conversational, no-ceremony way of working with coding agents rather than heavy prompting scaffolds.

- **2026-05-29** | [Rohit Ghumare](https://x.com/ghumare64/status/2060072412868235587) | agent-design, dev-practices
  Summarizes Mike Piccolo's argument that a harness isn't one thing but ~15 separate concerns (turn state machines, provider routing, credential vaults, policy engines, approval gates, budget trackers, context compaction, session trees, tracing) bundled by frameworks out of necessity. When each layer is a worker on a shared bus with a typed contract, 'build your own harness' means swapping a worker, not forking a framework.

- **2026-05-29** | [Yohei](https://x.com/yoheinakajima/status/2060068279574843614) | agent-design, research
  Yohei Nakajima's 'log-centric agent architecture' and his first arXiv paper 'The Log is the Agent: Event-Sourced Reactive Graphs for Auditable, Forkable Agentic Systems' — the case for agents that coordinate through persistent, replayable state.

- **2026-05-29** | [MacCallister Higgins](https://x.com/macjshiggins/status/2060045337679532174) | dev-practices, prompting
  Argues classical NASA systems engineering is the ideal model for LLM-assisted coding — being explicit in docs makes it easier than ever to build, test, and verify complex codebases (planning modes only approximate it).

- **2026-05-29** | [AVB](https://x.com/neural_avb/status/2060032255620431877) | research, dev-practices
  A 45-minute walkthrough on creating synthetic datasets and training tiny (~100M param) local language models specialized for narrow tasks; code, datasets, models and harnesses linked.

- **2026-05-29** | [Charly Wargnier](https://x.com/datachaz/status/2059649544854327466) | agent-design, skills-mcp
  Recommends Akshay Pachaar's 47-minute 'Hermes Agent Masterclass' on building self-improving, 24/7 local autonomous agents — self-evolving skills, three-tier memory, GEPA optimization, scaling from 1 to 10 agents.

- **2026-05-28** | [Charly Wargnier](https://x.com/datachaz/status/2059909626532155482) | skills-mcp, research, prompting
  Microsoft open-sourced SkillOpt: optimize agent skills the way you train models — a base model runs tasks while an optimizer rewrites the instructions, keeping only edits that raise the benchmark. Claims SOTA over hand-crafted prompts and TextGrad, with no model lock-in since it learns procedural logic.

- **2026-05-28** | [Muratcan Koylan](https://x.com/koylanai/status/2059753045060395240) | research, agent-design
  On the 'Agent Harness Engineering: A Survey' paper (CMU/Yale/JHU/Amazon; 170+ projects reviewed): real-world agent performance = model capability + harness quality, and for long-horizon production tasks the harness is the main bottleneck. Simple harness tweaks (tool formats, sandboxing, verification loops) yield big benchmark gains; the biggest wins come from turning production traces into regression tests + automated harness fixes.

- **2026-05-28** | [Kyle Jeong](https://x.com/kylejeong/status/2059753008297394245) | agent-design, skills-mcp, dev-practices
  Browser agents have an 'amnesia problem' — re-discovering each site from scratch every run. Autobrowse uses iterative AutoResearch to let an agent improve its own browser skills (/autobrowse), reportedly up to 90% faster and cheaper.

- **2026-05-28** | [Jerry Liu](https://x.com/jerryjliu0/status/2059710330016817501) | dev-practices, skills-mcp
  LiteParse v2: LlamaIndex's PDF parser rewritten in Rust with native Python/Node (and WASM) packages — claimed fastest and most accurate open-source model-free parser, up to 100x faster, 50+ document types, installable inside an AI agent.

- **2026-05-28** | [Livsun](https://x.com/l1vsun/status/2059707097583906917) | questionable
  Off-topic trading content dressed as a discovery: pitches Markov-chain state machines (trending/ranging/reversing transition matrix + Kelly sizing) with a Renaissance Technologies '66% annual returns' framing, promoting a quant listicle. Engagement-farmed, not AI/dev material.

- **2026-05-28** | [John Yeo](https://x.com/johnyeo_/status/2059688796728267261) | agent-design, dev-practices
  Describes an in-house agent that automatically queries logs and investigates support tickets — with billing state/history making each case stateful. Links a build writeup.

- **2026-05-28** | [Dave Kline](https://x.com/dklineii/status/2059634666030637286) | management
  Management thread: 'the biggest mistake I made as a manager was not managing up' — assuming impact is obvious and the boss is plugged in — plus how to fix it.

- **2026-05-28** | [Rahul](https://x.com/sairahul1/status/2059632149716942923) | claude-code, agent-design, questionable
  Hype-framed ('Anthropic just released the blueprint for a company run by Claude Code; work is dying') push for a listicle on building a SaaS MVP in an afternoon with 7 AI agents. Clickbait wrapper over a real multi-agent build walkthrough.

- **2026-05-28** | [Paul Iusztin](https://x.com/pauliusztin_/status/2059613089260003387) | agent-design, research
  Breakdown of Neo4j's graph-native agent memory: three connected layers in one graph — short-term (ordered message chain), long-term (entity/relationship knowledge graph with embeddings, traversed relationally), and reasoning memory (per-run trees of thoughts/tool-calls/decision paths). Typed edges (:MENTIONS/:INITIATED_BY/:TOUCHED) make provenance a one-hop query; 'the ontology is the real product.'

- **2026-05-28** | [Avi Chawla](https://x.com/_avichawla/status/2059556157984006187) | research, agent-design, dev-practices
  Clear explainer of RAG vs Graph RAG vs Agentic RAG as solving different query types: standard RAG for single-hop factual lookups, Graph RAG (LLM-extracted entities/relationships + traversal) for multi-hop connections, Agentic RAG (an agent choosing tools/sources at query time) for dynamic multi-source tasks — plus binary quantization for 32x more memory-efficient vector search.

- **2026-05-27** | [darkzodchi](https://x.com/zodchiii/status/2059603103070945391) | claude-code, dev-practices, agent-design
  Boris Cherny (Claude Code): 'we stopped fixing Claude's mistakes; we made Claude fix them itself.' Links a copyable setup for having Claude Code catch, fix, and learn from its own errors instead of the write-code/tests-fail/explain loop.

- **2026-05-27** | [Parag pawar](https://x.com/dharmikpawar13/status/2059571098484675051) | claude-code, prompting, dev-practices
  Argues CLAUDE.md is a control layer, not a README: use scope hierarchy (global → project → folder, nearest wins) and a WHAT/WHY/HOW framing, favor specificity ('TypeScript strict mode, Zod validation' over 'production-ready code'), start with /init, keep it under ~500 lines, use hooks, and treat it as living infrastructure.

- **2026-05-27** | [Rohit](https://x.com/rohit4verse/status/2059366212501696609) | agent-design, dev-practices
  A Databricks tech lead's talk on the unglamorous core of multi-agent: agents fail not because the model is dumb but because nothing coordinates them — one agent is a feature, fifty is a distributed-systems problem, and getting hundreds of agents to share one coherent brain is the whole game.

- **2026-05-27** | [Theo - t3.gg](https://x.com/theo/status/2059352130289651925) | research, dev-practices, claude-code
  Endorses DeepSWE, a new agentic-coding benchmark that reflects the realistic day-to-day developer experience — showing where top models actually diverge rather than clustering as they do on public leaderboards.

- **2026-05-27** | [Movez](https://x.com/0xmovez/status/2059346354984612126) | claude-code, agent-design
  An Anthropic engineer's 37-minute masterclass on shipping production agent teams: three building blocks (brain=persona, hands=environment, sessions), a server-side loop so nothing breaks on refresh, and why agents 'die before production.' Links a 10-step multi-agent build guide.

- **2026-05-27** | [Binfeng Xu](https://x.com/billxbf/status/2059323616009838703) | research, agent-design, dev-practices
  Release of Polar, Agent-RL rollout infrastructure that takes real-world harnesses (Codex, Claude Code, OpenClaw, Hermes, or your own) directly as training environments with no code change — find a problem, design the harness, train your own agents.

- **2026-05-27** | [Tom Dörr](https://x.com/tom_doerr/status/2059316125049971017) | dev-practices, research
  Shares a 500-hour AI infrastructure engineering curriculum (github.com/ai-infra-curriculum/ai-infra-engineer-learning).

- **2026-05-27** | [刘醒](https://x.com/xingxingli45573/status/2059258034820706541) | skills-mcp, dev-practices
  Taste Skill (~20.3k stars): an install that gives AI-generated front-ends better taste — improved layout, fonts, animations, whitespace — with design directions (premium, minimalist, brutalism), an audit-and-fix skill for old projects, a mockup-first image skill, and three tunable params (layout experimentation, animation richness, info density).

- **2026-05-27** | [Vaishnavi](https://x.com/_vmlops/status/2059207888393138556) | agent-design, dev-practices, skills-mcp
  Microsoft open-sourced an Agent Governance Toolkit: deterministic interception of every tool call (denied actions structurally impossible), a YAML allow/deny/human-approval policy engine, zero-trust identity (SPIFFE/DID/mTLS), a 4-level execution sandbox, tamper-evident Merkle audit logs, coverage of all OWASP Agentic Top-10 risks, and support across major frameworks and languages — because 'follow the rules' in a prompt is a suggestion, not a guardrail.

- **2026-05-25** | [darkzodchi](https://x.com/zodchiii/status/2058928613987160287) | claude-code, agent-design
  Boris Cherny (Claude Code): 'every night I have a few thousand agents running,' monitored from his phone. Links a piece arguing the next wave is a team of agents in a real chat app where they @mention each other, delegate, and remember — versus one sandboxed, memoryless ChatGPT tab.

- **2026-05-25** | [Atenov int.](https://x.com/atenov_d/status/2058868770257416239) | industry, dev-practices, questionable
  Highlights MoneyPrinterTurbo (13k+ stars): give a topic/keyword and it generates a script (via any LLM), pulls copyright-free footage, and adds subtitles/music/voiceover to output a finished short video; runs locally with Web UI/API/Docker/Colab. (Author's other posts are off-topic trading/politics.)

- **2026-05-25** | [Hasan Toor](https://x.com/hasantoxr/status/2058863173462352313) | agent-design, dev-practices
  Engagement-framed tool share: an open-source engine claiming to replace agent harness, queues, sandboxing and APIs with three primitives (TypeScript/Python/Rust, Docker-ready, 15k+ stars).

- **2026-05-25** | [Garry Tan](https://x.com/garrytan/status/2058378310254793013) | industry, research
  Garry Tan: fine-tuned his own Qwen3.5-397B in a couple hours via Thinking Machines, arguing fast usable multimodal will enable mind-blowing personal AI. Cites Thinking Machines' real-time 'interaction models.'

- **2026-05-24** | [Dave Kline](https://x.com/dklineii/status/2058538089224519806) | management
  Management thread: you can't create lasting motivation (it's intrinsic), but you can demotivate — the 5 most common leadership missteps.

- **2026-05-24** | [Shubham Saboo](https://x.com/saboo_shubham_/status/2058269167372153129) | agent-design, dev-practices, skills-mcp
  Positions codebase-as-queryable-graph as the real 'context engineering' for coding agents — turning any codebase into an interactive graph the agent can query; works with Claude Code, Codex, Antigravity; fully open-source.

- **2026-05-24** | [Kevin Simback](https://x.com/ksimback/status/2058262328496554021) | agent-design, research, skills-mcp
  A definitive guide to memory in the Hermes Agent, structured as a 3-layer stack: Layer 1 native (two always-injected markdown files MEMORY.md/USER.md plus a searchable SQLite session DB; the 80% consolidation 'rule' is a prompt instruction, not code), Layer 2 the pluggable MemoryProvider slot (8 official providers — Honcho, Mem0, Hindsight, Holographic, OpenViking, RetainDB, ByteRover, Supermemory — one at a time, each a different architectural bet), and Layer 3 community plug-ins (GBrain, Mnemosyne, etc.). Closes with how to pick and warning signs a memory layer is too heavy.

- **2026-05-24** | [George Nurijanian](https://x.com/nurijanian/status/2058259663238631890) | skills-mcp, dev-practices, prompting
  Fixed Claude's 'chart junk' by handing it a book and having it spin up a Tufte-flavored visualization skill — producing leaner, clearer visuals (github.com/gnurio/tufte-vdqi-plugin).

- **2026-05-24** | [Garry Tan](https://x.com/garrytan/status/2057946119725080878) | claude-code, management, dev-practices
  Garry Tan's 'simple secret to agentic coding,' linking a Forbes profile ('The YC Chief Who Codes 10,000 Lines A Day Has A Simple Secret').

- **2026-05-23** | [Charly Wargnier](https://x.com/datachaz/status/2057787509728522463) | skills-mcp, dev-practices
  Repo shoutout to addyosmani/agent-skills — production-grade engineering skills for AI coding agents, open-sourced by Addy Osmani.

- **2026-05-22** | [Viv](https://x.com/vtrivedy10/status/2057673225702937059) | agent-design, prompting
  An agent-orchestration heuristic Viv finds works in nearly every case: 'bossman supervisor >> external judge >>> self reflection.' A fresh judge (no prior context) beats self-review, but best is a supervisor orchestrating a series of Claudes — the main agent shouldn't think it's doing the work; it should be critically judging and correcting its workers.

- **2026-05-22** | [shdu](https://x.com/shdu11546816/status/2057642195524419748) | industry, general
  Macro speculation that AI triggers a 'Deflationary Doom Loop' via the Paradox of Thrift: agent-driven layoffs push white-collar workers into physical-labor markets, wages crash, and discretionary spending collapses because intelligence isn't the bottleneck for land, energy, and calories. A pessimistic counter to 'everything becomes cheap and abundant.'

- **2026-05-22** | [Ahmad](https://x.com/theahmadosman/status/2057590791241896254) | research, dev-practices, prompting
  Points to a free 'LLMs 101: A Practical Guide (2026 Edition)' covering model mechanics (tokens, transformers, attention, KV cache, decoding, RAG, agents, fine-tuning, multimodal) and running models locally (quantization, VRAM math, hardware tiers, runtimes, model selection, failure modes).

- **2026-05-22** | [swyx](https://x.com/swyx/status/2057559570177007912) | dev-practices, agent-design, skills-mcp
  swyx is building a skill to turn a vibecoded 'slop' app into a production-ready, e2e-tested, maintainable, parallelizable agent repo — one run went ~16 hours and 103 commits, ending with the same app but a codebase he can build on.

- **2026-05-22** | [Mnimiy](https://x.com/mnilax/status/2057551699204857930) | claude-code, prompting, agent-design
  Reports that Anthropic engineers kept repeating 'let it cook' at Code with Claude London (Boris Cherny, Ravi Trivedi, Katelyn Lesse): stop micromanaging prompts, write the routine, let Claude prompt itself — 'routines are higher-order prompts; the runtime is shipped; the prompts are the bottleneck.' Links 9 tested Claude Cowork prompt-templates.

- **2026-05-22** | [BOOTOSHI](https://x.com/kingbootoshi/status/2057528772208034195) | prompting, skills-mcp, agent-design
  Shares an S+-tier skill, directional-prompting (outcome-first + directional language, a two-layer approach), combined with /goal mode — 'agents thrive on positive communication; make the path to success clear.'

- **2026-05-22** | [Dan Shipper](https://x.com/danshipper/status/2057514494960513272) | management, industry
  Dan Shipper: Every automated everything it could with AI agents, yet has more human work than ever, growing 4→30 employees since GPT-3. His report 'After Automation' argues AI makes expert competence cheap, which raises demand for experts, and the dynamic intensifies toward AGI.

- **2026-05-22** | [Alex Veremeyenko](https://x.com/alex_prompter/status/2057476020454949201) | prompting, agent-design, skills-mcp
  Anatomy of the perfect SOUL.md identity file for AI agents — the file an agent reads first. Nine sections: Identity, Values, Communication Style, Expertise, Boundaries, Workflow, Tool Usage, Memory Policy, Example Interactions. 'Be helpful and professional' describes nothing; strong files have real opinions, specific limits, and concrete examples; 200-500 words, shorter = sharper.

- **2026-05-22** | [Dave Kline](https://x.com/dklineii/status/2057451633303322715) | management
  Management thread from a trainer of 1,500+ managers: delegation's hard part isn't assigning work but ensuring it's done well without micromanaging — with a simple 5-step system.

- **2026-05-22** | [Akshay](https://x.com/akshay_pachaar/status/2057446083853520948) | claude-code, skills-mcp, dev-practices
  Argues 'Claude Code isn't a coding tool — it's a programmable dev environment,' with 12 features that make it programmable: CLAUDE.md, Rules, Skills, Hooks, Slash Commands, Plugins, MCP, Plan Mode, Permissions, Subagents, Voice Mode, Rewind (1-5 define the environment, 6-7 extend it, 8-9 control it, 10-12 change how it runs).

- **2026-05-22** | [Khairallah AL-Awady](https://x.com/eng_khairallah1/status/2057433528363811098) | claude-code, questionable
  Engagement-framed roundup of a Boris Cherny podcast on why most people don't get results from Claude — they never set it up (CLAUDE.md, features that change how Claude thinks, unopened settings) — claiming ~30-38 untouched features. Links a '40 Features Most Users Have Never Touched' article.

- **2026-05-22** | [aditya](https://x.com/adxtyahq/status/2057410759236386866) | research, dev-practices, agent-design
  A worked answer to a Google L5 interview question — 'design a RAG pipeline for 10M docs with zero hallucination': ingest/normalize, hybrid retrieval (BM25 + embeddings), ANN + reranking, source-confidence scoring, constrained generation, citation-backed responses, hallucination fallback, continuous evals, caching, and observability. At scale, retrieval quality matters more than the frontier model.

- **2026-05-22** | [Aaron Levie](https://x.com/levie/status/2057315272156135501) | management, industry
  Aaron Levie on why Forward Deployed Engineers (FDEs) will persist: unlike cloud (concentrated users, little workflow change, slow enough for best practices to spread), agents are highly technical to deploy AND directly change users' workflows, and the fast model-change cadence keeps resetting best practices — so vendors/partners who've done it hundreds of times do the work. A great early-career path.

- **2026-05-22** | [Tom Dörr](https://x.com/tom_doerr/status/2057217338844336627) | dev-practices, research
  Shares turbovec, a vector store that fits 10 million documents into 4GB of RAM (github.com/RyanCodrai/turbovec).

- **2026-05-22** | [James Cogan](https://x.com/cogan/status/2056702063992607071) | management, industry, research
  A thoughtful essay, 'Machine Time,' arguing AI compresses the unit of meaningful time — shrinking the buffer between noticing a change and having to respond. AI compresses the front end of cognitive work, so the bottleneck moves to human review, judgment, and taste; the danger isn't speed but speed without scaffolding, and institutions increasingly answer with machine-speed coordination rather than restoring the human clock.

- **2026-05-20** | [Viv](https://x.com/vtrivedy10/status/2056993505386622987) | agent-design, dev-practices, research
  Notes on designing LangSmith Engine for customer-scale data: give the agent autonomy AFTER good tooling (around interacting with LangSmith); agents are good at pulling in context selectively, so the job is helping them self-facilitate routing useful info into the window.

- **2026-05-20** | [Arpit Bhayani](https://x.com/arpit_bhayani/status/2056946273165656375) | dev-practices, agent-design
  Argues long-running agentic systems need reliability/fault-tolerance, and that teams accidentally rebuild distributed workflows (cron + queue + state + retries → state machines, idempotency, compensating actions). An essay on Temporal, an open-source durable-execution engine (Workflows, Activities, event histories, replay, Signals, retries, determinism) as the plumbing for agents that need state and execution that survives failures.

- **2026-05-20** | [CyrilXBT](https://x.com/cyrilxbt/status/2056933229924372546) | agent-design, claude-code, questionable
  ALL-CAPS hype ('ANTHROPIC JUST KILLED THE DEMO AGENT ERA') about Anthropic's Agents team showing a production-grade four-layer framework for multi-agent systems in a 30-minute video. (The quoted article is mismatched — about turning Obsidian into a personal OS.)

- **2026-05-20** | [Tom Blomfield](https://x.com/t_blom/status/2056909934156280088) | management, agent-design, industry
  Tom Blomfield breaks down what YC is seeing in recursively self-improving companies — creating recursive self-improving AI loops so founders 'run companies that improve while they sleep.'

- **2026-05-20** | [Alex Hillman](https://x.com/alexhillman/status/2056904462162133233) | dev-practices, agent-design
  Reframes tmux as an agent superpower: it lets agents manipulate your terminal sessions — read logs from any pane/window, answer prompts in interactive CLIs, send keys into TUIs and capture the screen, and run subagents in separate windows to inspect their output.

- **2026-05-20** | [Yohei](https://x.com/yoheinakajima/status/2056848954848104488) | agent-design, research
  Yohei Nakajima on ActiveGraph, a 'continuity layer for long-running agents' — a novel agent architecture drawing on older designs, promising for self-improving agents via the ability to fork and diff agent runs.

- **2026-05-20** | [Greg Ceccarelli](https://x.com/gregce10/status/2056771029867933884) | prompting, agent-design, skills-mcp
  Field notes on a 'goal engineering' workflow: instead of prompts/specs, write two checked-in markdown artifacts per round — a 'goal' capped at 4,000 chars (matching Codex's /goal limit) and an unbounded 'rider' with ~11 phases and named depth tests — authored via a Skill. Aimed at long-running agentic turns.

- **2026-05-20** | [elvis](https://x.com/omarsar0/status/2056764334181884158) | research, agent-design, dev-practices
  'Code as Agent Harness' — a 100+ page survey of methods and applications of code-as-harness, arguing it may be key to a science of harness engineering, and that future systems must be executable, inspectable, stateful, and governed.

- **2026-05-20** | [Lotte](https://x.com/lotte_verheyden/status/2056754091817361670) | dev-practices, research, agent-design
  'Evals, explained' (Langfuse Academy): offline eval sits between running an experiment and shipping. Three methods — manual review (build intuition + ground-truth labels), code-based (deterministic checks: schema, keywords, length, SQL executes), and LLM-as-a-judge (language-understanding qualities, needs calibration against human labels). Prefer binary pass/fail over 1-5 scales; one evaluator per quality; start manual then automate repeatable checks.

- **2026-05-20** | [Ronan Berder](https://x.com/hunvreus/status/2056742771386638454) | dev-practices, agent-design, management
  Pushback on Spec-Driven Development: agents are faster at writing code and (some) humans are better at system thinking, but humans suck at planning. Argument: you can't sit down, write all the specs upfront, and then write code — experienced engineers know that doesn't work. Quote-tweets a now-unavailable @iamsahaj_xyz post.

- **2026-05-20** | [Akshay](https://x.com/akshay_pachaar/status/2056714042455343160) | research, dev-practices, claude-code
  RAG vs CAG explained: Cache-Augmented Generation keeps static, high-value knowledge in the model's KV memory instead of hitting the vector DB every query. Combine them — cache 'cold' static data (policies/docs), retrieve 'hot' dynamic data — for faster, cheaper inference. OpenAI and Anthropic already support prompt caching.

- **2026-05-20** | [Garry Tan](https://x.com/garrytan/status/2056711154224034125) | skills-mcp, agent-design, claude-code
  Garry Tan on dynamic, just-in-time skills for personal AI: 'markdown is code,' and the agent can change its own skills when new cases appear — 'just-in-time personal software is the most powerful idea of 2026.' A reply notes skill bundles carrying their own tests that the agent modifies in-flight create the compounding effect.

- **2026-05-20** | [Linas Beliūnas](https://x.com/linasbeliunas/status/2056679329484927356) | management, claude-code, industry
  Summarizes Anthropic's free AI-native founder playbook: build AROUND Claude across Idea → MVP → Launch → Scale (pressure-test the idea, Claude Code builds the product, Claude Cowork handles ops, Claude turns knowledge into compounding context). 'AI compresses execution but not judgment' — the edge becomes knowing what NOT to build; best AI-native startups have the best AI operating systems, not the biggest teams.

- **2026-05-19** | [Sapient Intelligence](https://x.com/sapient_int/status/2056510383935172798) | research, industry
  Sapient Intelligence introduces HRM-Text, an ultra-lean 1B-parameter reasoning model trained on just 40B structured tokens (~1/1000 the data of comparable models), with the full model training in ~one day on a $1,000 budget — pitched as making previously-too-expensive research concepts testable again.

- **2026-05-19** | [Amar Singh](https://x.com/amarsvs/status/2056484487891243355) | agent-design, research, dev-practices
  'Agent Performance: Model-Bound vs Harness-Bound' — counterintuitively, smarter models make harnesses matter MORE ('the smarter the model, the more expensive it is to waste its intelligence'). Model-bound tasks (hard math/proofs) hinge on raw capability; harness-bound tasks (e.g., Terminal-Bench, ~10 pts spread for Opus 4.7 across harnesses) hinge on prompting, tools, context management. As traces balloon and costs rise, the harness becomes the 'scheduler for intelligence'; author's open-source HALO optimizes harnesses from traces.

- **2026-05-19** | [AVB](https://x.com/neural_avb/status/2056462216430535062) | research, agent-design
  Notes that people are now training local recursive language models inside python REPLs with RL — agents divide-and-conquer long problems and pass context around as python variables. Links 'Recursive Agent Optimization using RL, explained clearly.'

- **2026-05-19** | [Aakash Gupta](https://x.com/aakashgupta/status/2056405221908394406) | claude-code, prompting, agent-design
  Aakash Gupta on Pawel Huryn's six-item CLAUDE.md 'routing table' (project description, file-structure map, identity context, knowledge routing, workflow pointers, and a 3-line self-improving prompt), with everything else in on-demand files/folders. The paste-ready self-improving prompt: review existing rules/hypotheses, apply confirmed rules, then update them from feedback each session.

- **2026-05-19** | [ClaudeDevs](https://x.com/claudedevs/status/2056403446056784288) | claude-code, dev-practices
  Anthropic blog on running Claude Code at scale — best practices from teams working across multi-million-line monorepos, decades-old legacy systems, and distributed microservices.

- **2026-05-19** | [Dave Kline](https://x.com/dklineii/status/2056363703230980364) | management
  Management thread: while most leaders worry about AI, a few become their company's AI expert and make themselves irreplaceable — a 5-step plan to become that leader.

- **2026-05-19** | [darkzodchi](https://x.com/zodchiii/status/2056336049589092866) | claude-code, management, dev-practices
  Shopify Head of Engineering Farhan Thawar: 'if you don't figure out how to harness agents in 2026, you'll be behind.' A practical enterprise-AI-coding breakdown / Shopify AI playbook, linking a 'Claude Code setup behind Shopify's 23,000 engineers' article (racing to automate 96% of coding by Q3, many parallel Claude Code agents).

- **2026-05-19** | [Paul Iusztin](https://x.com/pauliusztin_/status/2056272402414211175) | agent-design, research
  Calls Neo4j's open-source 'agent-memory' the best repo for a unified graph-based memory layer for AI agents — strong modeling of short/long/reasoning memory, ontology, and extraction algorithms; full write-up on decodingai.com.

- **2026-05-19** | [Dami-Defi](https://x.com/damidefi/status/2056053698674270631) | research, claude-code, prompting
  Fed MIT's 12 free graduate-level AI textbooks into Claude and rebuilt his research system around them. Links 'I Fed 12 Free MIT AI Textbooks Into Claude. It Rebuilt My Entire Research System.'

- **2026-05-18** | [Viv](https://x.com/vtrivedy10/status/2056066419360743479) | agent-design, dev-practices, research
  Viv on LangSmith Engine as an always-on self-improvement loop: tracing on for every agent, purpose-built SmithDB for agent-scale data, ambient intelligence over every trace to find errors/insights, and PRs/Evals generated with human gating — the first sparks of company-wide Continual Learning for agents.

- **2026-05-18** | [Suryansh Tiwari](https://x.com/suryanshti777/status/2056022182560665602) | claude-code, skills-mcp, questionable
  Highlights Anthropic's official 'claude-code-setup' plugin that scans a project and recommends hooks, skills, MCP servers, subagents, and automations (/plugin install claude-code-setup@claude-plugins-official). A Community Note corrects the post: the plugin is read-only — it recommends but does NOT install or modify files.

- **2026-05-18** | [AYi](https://x.com/ayi_ainotes/status/2055954675526934642) | agent-design, skills-mcp
  Enthusiastic (Chinese) take on Garry Tan's GBrain — 'not another RAG toy' but a complete personal-knowledge OS with 8 layers (vs the usual 4): install on OpenClaw/Hermes/Claude Code to remember relationships, decision trajectory, and long-term cognitive evolution, turning per-chat starts into lifelong memory + self-evolution. Garry's production ran 17,888 pages / 4,383 people / 723 companies.

- **2026-05-18** | [Vaishnavi](https://x.com/_vmlops/status/2055887618303570151) | agent-design, dev-practices, research
  Recommends walkinglabs.github.io/learn-harness-engineering as the best site to learn harness engineering.

- **2026-05-18** | [Vasilije](https://x.com/tricalt/status/2055876832797581406) | agent-design, skills-mcp, research
  'Memory isn't a plugin. Skills aren't a plugin. They're the same harness' — both are a world model (everything the agent uses to predict its next action). Memory observes the world; skills (SKILL.md procedures) codify it into rules and degrade silently without an Observe→Inspect→Amend→Evaluate loop. Cognee stores skills and memory in one graph so a skill is a traceable, evolving memory node.

- **2026-05-18** | [santi](https://x.com/santtiagom_/status/2055751665345798628) | dev-practices, agent-design, research
  Praises an OpenAI article on Harness Engineering and Codex — how they used agents to build an internal ~1M-line product: preventing agent-generated code from degrading, using tests/CI as more reliable constraints than prompts, keeping code/docs readable for agents, and how engineers' work changes when agents program.

- **2026-05-18** | [Jaynit Makwana](https://x.com/jaynitmakwana/status/2055594459426070640) | prompting, general, claude-code
  Turns Barbara Oakley's 'Learning How to Learn' science (rereading and highlighting don't work; intuition about learning misleads) into 10 Claude prompts that build a personalized study system from how the brain actually acquires skill.

- **2026-05-16** | [Dan McAteer](https://x.com/daniel_mac8/status/2055838212069773456) | research
  Flags a continual-learning result: fast-slow training (FST) treats model params as 'slow' weights and optimized context as 'fast' weights, reportedly beating weights-only training on every measured axis across math, code, and general reasoning.

- **2026-05-16** | [klöss](https://x.com/kloss_xyz/status/2055477217552142782) | prompting, claude-code, dev-practices
  Seven production-grade /goal templates (Ideation/Interrogation, Planning & Documentation, Build & Implementation, Refactoring, Consolidation, Hardening, Migrations; use 1-3 in order, 4-7 as needed), building on the argument that /goal is the best command in Codex/Claude Code/Hermes and most use it wrong.

- **2026-05-16** | [Erik Townsend](https://x.com/erikstownsend/status/2055444404337582106) | industry, general
  Erik Townsend flags ex-Goldman commodities chief Jeff Currie's thread calling AI's physical inputs (energy/commodities) 'the most asymmetric trade in modern financial history' — capital chased the AI software trade while ignoring the physical assets AI needs to run.

- **2026-05-15** | [George from prodmgmt.world](https://x.com/nurijanian/status/2055333397611077881) | skills-mcp, dev-practices, prompting
  Favorite ways to 'write requirements' with AI: /grill-me (mattpocock/skills), /shaping (rjs/shaping-skills), and a new skill built from business-analyst literature ('make-requirements-great') — reviving useful BA rigor that got dropped as teams went agile/sloppy.

- **2026-05-15** | [nader dabit](https://x.com/dabit3/status/2055319214202777894) | dev-practices, agent-design, claude-code
  'Agent Hooks: Deterministic Control for Agent Workflows' — hooks attach handlers to lifecycle points (SessionStart, UserPromptSubmit, PreToolUse, PostToolUse, Stop, SessionEnd) so scripts/tests/policy run every time instead of relying on the model to remember. Operating model: event → matcher → handler → outcome. Rule of thumb: 'always/never/block/record/run/verify' belongs in a hook. Includes a demo and per-runtime notes (Claude Code, Codex, Cursor, Devin); layer prompts (guidance) with hooks (controls), CI, and human review.

- **2026-05-15** | [Ole Lehmann](https://x.com/itsolelehmann/status/2055290989577753034) | agent-design, prompting
  Listicle of 9 personal-AI-assistant workflows the author would build on Hermes if starting from zero: Daily Brief (calendar+emails+weather+headlines to Telegram at 7am), self-improving Viral Swipe File (auto-extracts hooks/structure/stats from above-threshold posts), Trending Workflows Radar (scans Reddit/X/AI forums daily), and six more. Practical patterns for personal automation.

- **2026-05-15** | [0xMarioNawfal](https://x.com/roundtablespace/status/2055268207221682640) | claude-code, dev-practices
  SocratiCode — local zero-config tool giving AI agents semantic understanding of an entire codebase (dependency graphs, symbol-level impact analysis, cross-project search). Claimed numbers: 61% less context, 84% fewer tool calls, 37x faster than grep-based exploration, tested on 40M LoC. Fully local, free.

- **2026-05-15** | [Arpit Bhayani](https://x.com/arpit_bhayani/status/2055265636390207784) | agent-design, dev-practices
  Deep dive on what production-grade RAG actually requires beyond demos: how retrieval actually works, why chunking is where most systems fail, embedding-model lock-in, reindexing, document registries and chunk identity, index updates/deployments, retrieval tracing and observability. Argues production RAG failures are operational, not LLM, failures.

- **2026-05-15** | [Khairallah AL-Awady](https://x.com/eng_khairallah1/status/2055215784092401966) | agent-design, claude-code, industry
  Thread about Anthropic's May 6, 2026 multi-agent orchestration announcement (Code with Claude event): Claude Managed Agents can now run up to 20 specialized agents in parallel on a single task. Cites Netflix (parallel build-log analysis), Harvey (multi-document legal coordination), and Shopify (pushing toward 90% autonomous coding by Q3 2026) as production users. Good signal that parallel sub-agent orchestration is going mainstream.

- **2026-05-15** | [Mr. Buzzoni](https://x.com/polydao/status/2055197994635424038) | questionable, dev-practices
  Engagement-farmed post about a fired Atlassian infra engineer who allegedly posted a 38-minute breakdown of every system he built: Envoy proxy instead of enterprise load balancers, sidecar architecture for auth/logging/rate limits, DynamoDB + SQS for async provisioning, Packer + SaltStack for VM deployments at scale. 16.3M views, heavy 'save this' framing — substance is generic enterprise-infra patterns, not AI-specific.

- **2026-05-15** | [CyrilXBT](https://x.com/cyrilxbt/status/2055183411619549265) | industry, agent-design, questionable
  ALL-CAPS engagement-farming thread announcing GitHub's new official certification GH-600 "Agentic AI Developer" — framed as the first formal credential for engineers who operate, supervise, and integrate AI agent teams across the SDLC. Worth knowing the cert exists; treat the framing as hype.

- **2026-05-15** | [charmaine](https://x.com/charmaine_klee/status/2055106811225931883) | claude-code, dev-practices
  Anthropic engineer sharing the team's learnings on how Claude Code works in LARGE codebases — best practices and where to start. Links to the official Anthropic blog post: claude.com/blog/how-claude-code-works-in-large-codebases-best-practices-and-where-to-start. Direct, no hype.

- **2026-05-15** | [Meenakshi Yadav](https://x.com/meenakshiyacs/status/2055104295641710718) | agent-design, general, questionable
  Generic agentic-AI architecture "cheat sheet" listing the standard layer stack: goal definition, orchestration, agents, tools, memory, monitoring, reliability (retries/HITL), and governance. No new ideas — useful as a one-slide overview to hand a junior or non-engineer.

- **2026-05-15** | [Sam Hogan](https://x.com/samhogan/status/2055064462844219603) | agent-design, research
  Sam Hogan introduces HALO (Hierarchical Agent Loop Optimizer) — github.com/context-labs/halo — which uses Reasoning Language Models to let the model itself shape its own agent harness rather than hard-coding it. Inspired by @a1zhang's "Mismanaged Genius Hypothesis" (LLMs are smarter than the harnesses humans design for them). Reports consistent 10%+ benchmark improvements across multiple evals.

- **2026-05-15** | [Avid](https://x.com/av1dlive/status/2054948286403150017) | agent-design, dev-practices
  Promo for a live 15-minute lecture by two Airbnb Senior Staff Engineers on agentic coding in 2026 — Airbnb already shipped one of the most ambitious LLM-agent migrations in production. Quote-tweets Avid's May 12 article "How to Build AI Agents in 2026 (Full Course)" (527.6K views). Worth watching for real production agentic-coding patterns from a company that has actually done the migration.

- **2026-05-15** | [Berryxia.AI](https://x.com/berryxia/status/2054924976835510337) | agent-design, research
  Translated-from-Chinese thread breaking down Tencent's newly open-sourced AI agent memory system (6 months of work). Highlights three techniques: real-time compression of expired context (cuts token usage 61%), Mermaid-syntax structured task maps that keep 30+ step workflows on track, and a long-term memory tier. Argues most teams over-index on context-length and under-invest in memory architecture.

- **2026-05-15** | [Petra Donka](https://x.com/petradonka/status/2054897826149101588) | agent-design, prompting
  Argues agents doing judgment-heavy work need feedback loops, not perfect prompts — because no static prompt covers everything as the product/users/team's taste evolves. Walks through Warp's experience building an agent for their Developer Experience team that responds to Warp mentions on Twitter/Reddit and learns from team feedback over time.

- **2026-05-15** | [How To AI](https://x.com/howtoai_/status/2054611399792644386) | research, questionable
  Hype-framed thread about Google's new "Nested Learning: The Illusion of Deep Learning Architectures" paper (calling it "Attention Is All You Need V2"). Argues that today's LLMs suffer catastrophic forgetting because we treat them as one flat function, and Nested Learning instead models a network as thousands of nested optimization problems at different update frequencies — closer to how brains consolidate short- and long-term memory. Substance is real (Google Research paper), framing is clickbait.

- **2026-05-15** | [Anatoli Kopadze](https://x.com/anatolikopadze/status/2054568935274549597) | claude-code, prompting, questionable
  18-step listicle on getting more out of Claude (2.4M views). Step 1 — use Projects, not bare chats, so context persists across conversations; later steps cover memory, custom instructions, integrations, and workflows. Listicle framing is engagement-farmy but several tips are practical Claude.ai usage patterns worth knowing.

- **2026-05-15** | [ar0cket1](https://x.com/ar0cket1/status/2054108160450064571) | research
  Research progress report on On-Policy Self Distillation (OPSD) — trying to get RL-like capability gains with the sample efficiency and stability of on-policy distillation. Experiments on Olmo 3 7B (SFT student vs RL'd teacher) on nemotron-math-v2. Frames OPSD as a stepping stone toward continual learning because RL is currently the best engine for new capability gains.

- **2026-05-14** | [Rohit Ghumare](https://x.com/ghumare64/status/2054625511897489423) | agent-design, dev-practices
  Argues agent codebases that survive past month six do so because the architecture makes the wrong shape harder to write than the right one — not because the team is disciplined. Cites a 'Mike' post listing four canonical month-six failures: shared mutable defaults across agents, tool fns that swallow any string and return None, session memory poisoned by LLM-extracted strings, and multi-agent setups passing the parent's full context. Aligns with the Anthropic/Glean harness-is-the-backend debate.

- **2026-05-14** | [divyansh tiwari](https://x.com/divyansht91162/status/2054430633645293687) | agent-design, research
  Highlights a paper called NanoResearch proposing an agent architecture with three co-evolving layers — Skill Bank (turns repeated actions into reusable expertise), Memory Layer (preserves project + user experience across sessions), Policy Learning (turns free-form feedback into permanent behavioral updates). Pitch: an agent that accumulates experience and aligns to the user over time rather than relying on bigger context windows.

- **2026-05-14** | [Guri Singh](https://x.com/heygurisingh/status/2054405672176091449) | questionable, industry
  Listicle of 10 side-hustle / digital-product sites (Carrd, Gumroad, Systeme.io, Payhip, Ko-fi, Sellfy, …) framed as 'print money while you sleep'. Off-topic for the AI collection and engagement-farmed; flagging as questionable.

- **2026-05-14** | [송준 Jun Song](https://x.com/jun_song/status/2054379887608402199) | research, industry
  Claims that within weeks, a Minimax-M3.0-JANGTQ-CRACK release from @dealignai will bring Opus-4.6-tier local inference to 128GB Macs, with open-source quantization efforts targeting 24GB VRAM. Bullish on where local LLMs land in mid-2026.

- **2026-05-14** | [Joe Hudson](https://x.com/fu_joehudson/status/2054264609683689941) | general
  Coaching post (not AI-specific) — Joe Hudson summarizes his 'dirty fuel to clean fuel' framework for personal energy/motivation on a single page. Off-topic for the collection but in Jeremy's inbox; keeping for completeness.

- **2026-05-14** | [George from prodmgmt.world](https://x.com/nurijanian/status/2054244221352325359) | management, prompting
  PM advocates using an LLM as an adversarial reviewer on your PRD — the flaws that ship to production are the ones you can't see from inside the doc. Short take with a link to his prodmgmt.world article walking through the practice.

- **2026-05-14** | [Jamie Signorile](https://x.com/sigsnyc/status/2054238175758111156) | management, industry
  Frames AI as widening the gap between strong and average employees in enterprise GTM roles rather than uplifting everyone. Author uses a two-axis hiring framework (technical capability x business savvy) drawn from a decade at Addepar and KizenTech and argues AI inverts how operators get evaluated.

- **2026-05-14** | [Khairallah AL-Awady](https://x.com/eng_khairallah1/status/2054211760631185485) | claude-code, questionable
  Hype-styled promo pointing to a free 30-min Boris Cherny (creator of Claude Code) walkthrough plus the author's own 'turn Claude into a full-time AI employee in 7 days' course. The Cherny session is the real link worth chasing; the framing is engagement-farmed.

- **2026-05-14** | [Jaynit](https://x.com/jaynitx/status/2054200520575967698) | management, general
  Personal essay on developing implicit pattern recognition — author tracked his own pre-post predictions on engagement and hit 70-80% accuracy without being able to articulate why. Reflection on tacit-knowledge skill-building, not AI-specific.

- **2026-05-14** | [Geek Lite](https://x.com/qingq77/status/2054056472477307084) | agent-design, skills-mcp
  Oh My Hermes (github.com/Salomondiei08/oh-my-hermes) is a skills+workflow layer for the Hermes Agent that ships 20 skills covering the full app lifecycle (requirements through monitoring/GitHub ops) and 5 role-specialized agents (CTO/PM/Dev/QA/Ops) collaborating on a kanban board. Treats Hermes as primary operator and Claude Code/Codex as optional accelerators — a concrete prior art for our skills + sub-agent architecture.

- **2026-05-13** | [Alfred Lin](https://x.com/alfred_lin/status/2054556828118245710) | management
  Alfred Lin (Sequoia) on using simplicity humbly — frameworks have a domain of validity. Four complements: face the limits, zoom in and out, check convergence across frameworks, probabilistic thinking. Not about AI specifically, broader management/judgment essay.

- **2026-05-13** | [darkzodchi](https://x.com/zodchiii/status/2054526937561796939) | claude-code, dev-practices
  Pointer to an Anthropic-engineer video on the 7 Claude Code mistakes that waste tokens — model switching, context management, settings that halve token usage. Key data point: Claude Code resends the full conversation history every turn, so a 30-message session can burn 232K tokens. Every MCP server, skill, and read file rides along.

- **2026-05-13** | [Avi Chawla](https://x.com/_avichawla/status/2054493154045567400) | claude-code
  Direct comparison of Anthropic's three Claude surfaces: Chat (for thinking — conversational, no local file access), Code (for building — CLI, dev-focused), Cowork (for doing — desktop, agentic file/task automation). Useful framing for choosing the right surface per task.

- **2026-05-13** | [Ihtesham Ali](https://x.com/ihtesham2005/status/2054458335215395223) | research, agent-design, claude-code
  Google + Meta paper: Claude Code autonomously proposes, tests, and refines algorithms for improving LLM reasoning over 5 rounds with no human in the loop. Discovers a 4-mechanism controller (EMA momentum stopping, coupled width-depth control, alignment-aware depth allocation, conservative branch abandonment) for $39.90 total compute. Paper at arxiv.org/abs/2605.0xxx.

- **2026-05-13** | [Michael Eisenberg](https://x.com/mikeeisenberg/status/2054431554240201008) | management, general
  Michael Eisenberg endorses a Zohar Atkins essay applying Jevons Paradox to Torah learning — when knowledge becomes cheap (AI), insight is what matters. Reference to Jevons' 1865 Coal Question. Off-topic for the AI stack but thoughtful framing on the value of insight in an AI-abundant world.

- **2026-05-13** | [ericosiu](https://x.com/ericosiu/status/2054413343776223393) | industry, management, agent-design
  ericosiu hiring forward-deployed engineers globally. Quotes Aaron Levie noting FDEs (or equivalent) are about to become one of the most in-demand jobs in tech for AI rollouts. References a "beat AI" challenge in his profile as their filter. Subject flagged "worth an extra look".

- **2026-05-13** | [IndieDevHailey (开发者Hailey)](https://x.com/indiedevhailey/status/2054386235867812240) | research, industry
  GitHub project RuView (50K+ stars) — uses WiFi CSI signals plus AI to detect humans behind walls without cameras. Pose detection (17 keypoints), breathing/heart rate while sleeping, fall alerts. Runs locally on ESP32; no video, no cloud, privacy-preserving. Translated from Chinese.

- **2026-05-13** | [Miles Deutscher](https://x.com/milesdeutscher/status/2054310749884002348) | skills-mcp, questionable
  Promotion of skillsmp.com — a marketplace claiming over 1 million ready-to-use agent skills and plug-ins. Marketing-heavy "complete game-changer" framing, low actual detail.

- **2026-05-13** | [Founder Thoughts & Strategies](https://x.com/mogulinfluence/status/2054274159706853837) | management, industry
  Quote of Tom Verrilli (Whatnot) article on building product teams in the AI era — 31,832 people applied to be a PM at Whatnot in two years, only one hired. Framing: best product teams will ship 10x faster post-AI. Subject flagged "have a look".

- **2026-05-13** | [GREG ISENBERG](https://x.com/gregisenberg/status/2054261832718889216) | agent-design, industry, claude-code
  Free 47-minute course on building a managed AI-agent business solo. Pitch: sell "unlimited agents/infrastructure" as digital employees, don't niche too early, every executive has the same problems (emails, meetings, follow-ups). Stack: Hermes Agent (harness), Codex or Claude Code (build), Orgo (cloud computer sandboxes per agent), Composio (one-click auth), Obsidian (docs).

- **2026-05-13** | [Joseph Viviano](https://x.com/josephdviviano/status/2054253118943363506) | agent-design, dev-practices, research
  Joseph Viviano's "Agentic Research Best Practices" — 15 months of notes on using coding agents in research workflows (with Mila Quebec collaborators). Key argument: research codebases differ from product engineering — no users, active development, speed bound by intelligibility to author/collaborators, not throughput. Many "best practices" from product engineering feel archaic in research.

- **2026-05-13** | [Charly Wargnier](https://x.com/datachaz/status/2054225085100151163) | agent-design, questionable
  Charly Wargnier hyping a Rohit article "What to Learn, Build, and Skip in AI Agents (2026)" — invokes Karpathy line that 90% of AI advice dies in 6 months. Signal-vs-noise framing for agent tooling, but very engagement-bait copy.

- **2026-05-13** | [George from prodmgmt.world](https://x.com/nurijanian/status/2054216035503587396) | skills-mcp, prompting
  George keeps reusing his own AI skill-building pipeline and wishes it were a product. Quote of his March 28 article on building AI skills as a non-expert by finding subject-matter experts in PDFs (he built game-theory and formal-logic skills this way).

- **2026-05-13** | [コムテ (Komte)](https://x.com/commte/status/2054136870016356408) | skills-mcp, claude-code, industry
  Google open-sourced 13 official Agent Skills (github.com/google/skills) compliant with the Agent Skills standard — interoperable with Claude Code, Antigravity, Gemini CLI, Cursor, GitHub Copilot, and other major agents. Significant cross-vendor signal for the Agent Skills standard.

- **2026-05-12** | [Ronin](https://x.com/deronin_/status/2054255152555545079) | claude-code, dev-practices, prompting, questionable
  Ten token-waste mistakes senior AI engineers stopped making — auto-context loading 50 files for a 30-line fix ($1.20/turn waste), defaulting Opus on lint/format/rename ($0.60 vs Haiku $0.02), tool-call loops resending the full repo on retry, defaulting to Sonnet when Kimi 2.6 matches at 1/6 cost, streaming on stable-prefix workflows killing prompt cache, "just-in-case" file includes blowing 80K-token prompts. Karpathy-quote framing.

- **2026-05-12** | [Roan](https://x.com/rohonchain/status/2054245904258142593) | questionable, general
  Stanford MDP lecture pitched as a Markov-Chains-for-trading framework — quote of his own article on hedge-fund Markov chain trading. Not AI/agent content; trading/quant finance with engagement-bait framing. Tag as questionable.

- **2026-05-12** | [Rahul](https://x.com/sairahul1/status/2054171777119801764) | agent-design, industry
  Hypes a 22-minute Anthropic talk on production AI agents covering tool orchestration, memory systems, observability, long-running agents, and production infrastructure. Pitches a personal "How to Become an AI Agent Engineer in 2026" roadmap pushing back on CrewAI-by-default and framework chasing.

- **2026-05-12** | [klöss](https://x.com/kloss_xyz/status/2054096165055217987) | prompting, claude-code, dev-practices
  Detailed /goal prompt template for Codex / Claude Code / Hermes with structured slots: GOAL (single measurable outcome), CONTEXT, CONSTRAINTS, PRIORITY, PLAN (understand first), DONE WHEN, VERIFY (tests/build/lint/typecheck). Aimed at killing scope creep and ranking uncertainty before acting. Directly usable.

- **2026-05-12** | [Muhammad Ayan](https://x.com/socialwithaayan/status/2053875867487777175) | claude-code, skills-mcp, industry, questionable
  Engagement-farmed announcement (all-caps 'BREAKING') that Anthropic open-sourced a Claude Code plugin suite for finance workflows — DCF/LBO models, equity research, M&A analysis, KYC, IC memos — with MCP connectors for Bloomberg, FactSet, S&P Global, Morningstar, and PitchBook (github.com/anthropics/financial-services, Apache-2.0, ~19.8K stars). Top replies flag the obvious caveat: the harness is free but the data feeds (Bloomberg Terminal ~$28K/yr, FactSet/S&P/PitchBook six-figure) are not, and the agents draft work for human sign-off rather than autonomously owning workflows.

- **2026-05-11** | [Garry Tan](https://x.com/garrytan/status/2053538847795880414) | agent-design, prompting
  Garry Tan riffs on a Finbarr take — "code as memory": work with an agent non-deterministically the first time to figure out a task (research + write a script), then execute that script on every future repetition. Quote-tweets his own Apr 22 article on stopping agents from making the same mistakes (LangChain context).

- **2026-05-10** | [Garry Tan](https://x.com/garrytan/status/2053127519872614419) | agent-design, prompting, claude-code
  Long-form X article "Meta-Meta-Prompting: The Secret to Making AI Agents Work" — Garry Tan argues to stop treating AI as a chat window and start treating it as an OS. Part of his Fat Skills/Fat Code/Thin Harness series. Open source: github.com/garrytan/gbrain and github.com/garrytan/gstack. Concrete "book mirror" example uses sub-agents per chapter that map ideas to your actual life context. 1.2M views.

- **2026-05-10** | [Mnimiy](https://x.com/mnilax/status/2053116311132155938) | claude-code, prompting, dev-practices
  Long-form post: Karpathy's 4-rule CLAUDE.md template (born Jan 2026 from his thread on Claude failure modes — silent wrong assumptions, over-complication, orthogonal damage) cut mistakes from ~40% to <3% across 30 codebases over 6 weeks. Forrest Chang's repo hit 120K stars. Author argues the template only fixes Jan code-writing problems; he adds 8 more rules targeting May 2026 agent-orchestration issues (agent fights, hook cascades, skill loading conflicts, multi-step workflows). Notes CLAUDE.md is advisory (~80% compliance); past 200 lines compliance drops sharply. 2.5M views.

- **2026-05-08** | [Himanshu Kumar](https://x.com/codewithimanshu/status/2052573291131589101) | industry, questionable
  Engagement-heavy framing around a free MIT lecture from Jim Simons on quant trading math. Claims Renaissance Technologies-style pattern recognition is now buildable in a weekend with Claude Code (no team of 50 PhDs needed). Hype style; the lecture link itself is the real reference.

- **2026-05-08** | [Tom Dörr](https://x.com/tom_doerr/status/2052552468983103608) | agent-design, research
  Tom Dörr highlights agentic-data-scientist (github.com/K-Dense-AI/agentic-data-scientist) — an open-source self-correcting agent for complex data-science tasks. Worth a look as a benchmark for self-correction patterns.

- **2026-05-08** | [ani](https://x.com/anirudhbv_ce/status/2052532004919361958) | research, agent-design
  Provocative paper 'The Geometry of Consolidation' (github.com/niashwin/geometry-of-consolidation): claims only ~3% of dimensions in major embedding models (91/3072 for OpenAI text-embedding-3-large, 80/3072 for Gemini gemini-embedding-001) do real work, the rest is mathematically empty. Argues RAG compression has a hard floor no algorithm can beat, set by a spectral number the embedding model can't escape — and that this is the root cause of RAG hallucinations. Big claim, worth reading the paper before believing.

- **2026-05-08** | [Axel Bitblaze](https://x.com/axel_bitblaze69/status/2052520764545613958) | claude-code, skills-mcp
  claude-handoff plugin (install: /plugin marketplace add willseltzer/claude-handoff && /plugin install handoff) — three commands (/handoff:create, /handoff:quick, /handoff:resume) that generate a HANDOFF.md with full session state (branch, commits, files touched, dead ends) so a fresh Claude Code session can pick up where the old one ended. Targets the 10-20 message context-degradation point Anthropic recommends restarting at.

- **2026-05-08** | [Avi Chawla](https://x.com/_avichawla/status/2052482874126020882) | claude-code, skills-mcp, agent-design
  Avi Chawla on Karpathy's 'remove yourself as the bottleneck' framing and Rowboat — an open-source AI 'second brain' built on the Markdown/Obsidian foundation Karpathy uses, extended to work context (emails, meetings, decisions, commitments). The pitch: most people can't act on Karpathy's advice because their AI has no memory of their work, and Rowboat is one open-source answer to that.

- **2026-05-08** | [divyansh tiwari](https://x.com/divyansht91162/status/2052474052841984110) | agent-design, industry
  TinyFish drops web search to $0 for AI agents. divyansh switched OpenClaw and Hermes agents to it and reports they can now browse, research, and retrieve live info at scale for free — a real shift in agent-cost economics if it holds up.

- **2026-05-08** | [Tom Dörr](https://x.com/tom_doerr/status/2052440598452359394) | claude-code, agent-design, skills-mcp
  Tom Dörr surfaces 'agentmemory' (github.com/rohitg00/agentmemory) — a knowledge-graph memory layer for Claude Code. Pair with the other agent-memory tools in the corpus (HelixDB, turbovec, mem0).

- **2026-05-08** | [Mgoes](https://x.com/m_goes_distance/status/2052433497575293307) | industry
  Biotech-progress digest for 2026 — Japan endorsing iPS cell therapies for heart failure / Parkinson's, Altos Labs' Atlas of Rejuvenation, rapalink-1 as longevity drug, Retro Biosciences dosing brain-cleanup pill, peptides moving from banned to federal policy, psychedelics executive order, GLP-1s at 12.4% adult adoption. Off-topic for the AI links collection but Jeremy emailed it, so capturing it honestly.

- **2026-05-08** | [Goodfire](https://x.com/goodfireai/status/2052420446910644616) | research
  Goodfire (interpretability research lab) kicks off a series of blog posts on 'neural geometry' — the framing that networks 'speak English but think in shapes,' and that understanding their geometric structure is key to debugging and controlling them. 3.1M views — interpretability research breaking out of the lab into general attention.

- **2026-05-08** | [darkzodchi](https://x.com/zodchiii/status/2052400272840720565) | claude-code, agent-design, questionable
  Hype-style pointer to a 22-minute Anthropic Claude team talk on their 2026 agent roadmap — tools, memory, observability, builder-state-of-the-art. Last 3 minutes called out as especially worth watching. Quote-tweets the author's own article on agent reliability (AI agent breaking at 2am, sending 47 broken emails over the weekend, burning $340 in API calls).

- **2026-05-08** | [Dave Kline](https://x.com/dklineii/status/2052372231800439054) | management, prompting
  Dave Kline teases 5 AI prompts for 1:1 prep — claims his 5-minute pre-meeting AI ritual changed the quality of his 1:1s. Listicle framing; substance in the thread.

- **2026-05-08** | [Millie Marconi](https://x.com/milliemarconnni/status/2052363436575826398) | agent-design, research, skills-mcp
  Millie Marconi highlights Feynman (github.com/getcompanion-ai/feynman) — an open-source MIT-licensed agent system with four bundled roles (Researcher, Reviewer, Writer, Verifier) that reads papers, audits referenced code, and replicates experiments. Runs in Docker for safe local execution and spins up serverless GPUs on Modal or persistent pods on RunPod. Indexed session search across past research runs, inline citation-URL verification.

- **2026-05-08** | [Allen Braden](https://x.com/allen_explains/status/2052340555942924368) | industry, questionable
  Allen Braden points to a free 1-hour UC Berkeley lecture on systematic-trading fundamentals (the math Jane Street quants use). Engagement-style framing without the actual lecture link — finding it requires follow-through outside the post.

- **2026-05-08** | [Rohit Ghumare](https://x.com/ghumare64/status/2052313902214476192) | claude-code, skills-mcp, agent-design
  Rohit Ghumare highlights agentmemory — a memory layer for Hermes / Claude Code / Codex that records session observations, compresses them with AI, and injects relevant context back into future sessions. Claims 95% fewer tokens per session and 200x more tool calls before hitting context limits, benchmarked on 240 real coding sessions. MIT-licensed, ~1,000 GitHub stars in its first week. Worth evaluating as a CLAUDE.md alternative for long-running agent work.

- **2026-05-08** | [Tom Dörr](https://x.com/tom_doerr/status/2052261421744869757) | dev-practices, research
  Tom Dörr highlights HelixDB (github.com/HelixDB/helix-db): a database that combines graph and vector storage in one engine for AI apps. Worth evaluating as a building block for RAG and agent-memory pipelines that otherwise span two systems.

- **2026-05-08** | [Kanika](https://x.com/kanikabk/status/2052032420954927357) | agent-design, research, questionable
  Kanika points to a 424-page 'Agentic Design Patterns' guide written by a senior Google engineer — every chapter ships working code, all Amazon royalties go to Save the Children, $40 print price. Engagement-bait framing ('bookmark before it's buried') but the reference itself is a real, comprehensive resource.

- **2026-05-07** | [Uncle Bob Martin](https://x.com/unclebobmartin/status/2052370749701214226) | dev-practices, industry
  Uncle Bob Martin: 'It's not wrong. It just shows that driving an AI is a form of engineering that is not for the faint of heart.' The post he was reacting to is now from a suspended account, so the original content is lost — Uncle Bob's framing is all that remains. 130.6K views suggests it resonated.

- **2026-05-07** | [Tom Dörr](https://x.com/tom_doerr/status/2052150733261193390) | research, agent-design
  Tom Dörr points to awesome-foundation-agents (github.com/FoundationAgents/awesome-foundation-agents) — a curated reading list of papers mapping foundation-agent cognition. Reference, not actionable.

- **2026-05-05** | [Vinay](https://x.com/leashless/status/2051437380788158739) | research, general
  Vinay quote-tweets a viral post about Gödel, Escher, Bach (1979) — Douglas Hofstadter's 800-page Pulitzer-winning book on a logician, artist, and composer that became required reading at every major AI lab. Vinay: "Time stopped. We all read it. It took two years to talk through the implications. Nobody ever forgot."

- **2026-05-05** | [Adam Ghowiba](https://x.com/adamghowiba/status/2050886233921061281) | agent-design, industry
  JP Morgan's investment research team broke down their "Ask David" multi-agent architecture: a supervisor agent orchestrates specialized subagents (retrieval, structured data, analytics), with an LLM-as-judge reflection node before the answer ships and human-in-the-loop for the last accuracy gap. Same supervisor + specialist + reflection pattern showing up everywhere.

- **2026-05-02** | [Dave Kline](https://x.com/dklineii/status/2050563237490344194) | management
  A 15-minute manager/employee playbook for resetting expectations when someone is stuck — Kline argues 95% of work problems trace back to unclear expectations. Practical management tactic, no AI angle.

- **2026-05-02** | [Ole Lehmann](https://x.com/itsolelehmann/status/2050548948419645488) | prompting, management
  Argues you should run a 'premortem' on your plans with Claude — frame it as 'it's 6 months from now, this plan died, tell me how' — to bypass the model's optimism bias. Cites Kahneman; says Google, Goldman, P&G use it before launches.

- **2026-05-02** | [0xSero](https://x.com/0xsero/status/2050544304360165585) | claude-code, dev-practices
  Reminder that Claude Code session history is auto-deleted monthly unless you change settings.json — that's all valuable training/context data. 0xSero shares a backup repo (github.com/0xSero/ai-data-extraction) to help you preserve it.

- **2026-05-02** | [darkzodchi](https://x.com/zodchiii/status/2050537397377532341) | dev-practices, claude-code, questionable
  Promotes a security article + .gitignore template after citing that Anthropic allegedly leaked 512K lines of source code from a missing .gitignore entry. Boris Cherny (Claude Code creator) cited as the cautionary tale. Engagement framing, but the .gitignore best-practices angle is legitimately useful.

- **2026-05-02** | [Blaze](https://x.com/browomo/status/2050509770604331510) | agent-design, claude-code
  French teenager built a 3D map of 217 mental models (1284 connections) controlled by hand gestures + voice, running Three.js + MediaPipe Hands + local Whisper + Claude API + Google Antigravity. Whole stack assembled in one weekend; 80ms gesture-to-graph latency, runs from a 47MB Obsidian vault on a regular laptop.

- **2026-05-02** | [Muhammad Ayan](https://x.com/socialwithaayan/status/2050484688968724820) | agent-design, dev-practices
  Pointer to github.com/warpdotdev/warp — Warp terminal's source has been published as 'an agentic development environment, born out of the terminal.' Worth a look as a coding-agent shell.

- **2026-05-02** | [Kpaxs](https://x.com/kpaxs/status/2050470605804216695) | management
  Kpaxs reframes high-agency behavior: 'I'm doing this unless someone stops me' vs 'Can I do this?' — most permissions get granted retroactively, so it's easier to ask forgiveness than permission. Useful framing for engineering culture and AI adoption.

- **2026-05-02** | [Om Patel](https://x.com/om_patel5/status/2050441119003971683) | claude-code, skills-mcp, agent-design, questionable
  Promoted Claude Code skill /graphify that pre-builds a graph of your codebase (functions, deps, docs, PDFs, images, audio, video via Whisper) so Claude doesn't waste tokens exploring. Author claims '71.5x more efficient' (engagement-farming framing).

- **2026-05-02** | [Tom Doerr](https://x.com/tom_doerr/status/2050312101504094651) | agent-design, research
  Points to a curated GitHub list on AI agent evolution, memory systems, and self-improvement (github.com/EvoMap/awesome-agent-evolution) — a reference index for the self-improving-agent literature.

- **2026-05-02** | [Keith Rabois](https://x.com/rabois/status/2050250243552239956) | management, industry
  Rabois (one-word 'Useful.') endorsing Ann Miura-Ko's piece arguing most scaled companies (e.g. Ramp, 1500-person org) are still Level 1 on AI adoption despite the 'AI-pilled' narrative — based on her recent office visits.

- **2026-05-02** | [Dan Shipper](https://x.com/danshipper/status/2050235671466606665) | agent-design, management, dev-practices
  Dan Shipper recommends Marcus's 'definitive guide' on how a PM can ship product with coding agents at Every: every.to/guides/ai-product-management-guide. Pitched as required reading for non-engineer builders.

- **2026-05-02** | [regent0x](https://x.com/regent0x_/status/2050143341656838449) | agent-design, management, questionable
  Story (likely embellished) about a solo Chinese dev billing $320k/yr by orchestrating 5 specialized Claude agents in parallel: architect, coder, reviewer, tester, ops. Each agent has its own context, no shared state. Engagement-y framing but the parallel-specialist pattern is real.

- **2026-05-02** | [Xiuyu Li](https://x.com/sheriyuo/status/2050067900820840791) | research
  Endorses Will Brown's writeup 'On SFT, RL, and on-policy distillation' — why the SFT→RL pipeline works, where on-policy distillation fits, and how self-distillation goes wrong. Co-authored with Claude Opus 4.7.

- **2026-05-02** | [GPT Maestro](https://x.com/gptmaestro/status/2050060105052561681) | prompting, research
  Quote-tweet endorsing a clear walkthrough of GEPA — a technique that optimizes prompts before inference rather than cramming more into context. Quoted source: Quarq's 'Exploring GEPA' (also covers Recursive Language Models / RLMs).

- **2026-05-02** | [Mike Bespalov](https://x.com/bbssppllvv/status/2049924037111841027) | agent-design, dev-practices
  Refero.design publishes 2000 DESIGN.md files (colors, type, spacing, layouts) extracted from the world's best products, structured for an LLM to read so coding agents stop producing ugly UIs. Free at styles.refero.design.

- **2026-05-02** | [Xiangyi Li](https://x.com/xdotli/status/2049903693143609627) | agent-design, research
  Short endorsement — 'must read for everyone who wants to reduce the entropy of their agentic systems' — pointing at evals/environments work (benchflow_ai). Framing: disciplined evals as the way to tame nondeterminism in agent systems.

- **2026-05-02** | [BasedBiohacker](https://x.com/basedbiohacker/status/2049235599874200049) | general
  [Off-topic — not AI/tech] Biohacking/nootropics vendor and dosage list at basedbiohacker.any.org, including 'research-only' compounds. Likely sent to the AI inbox by accident.

- **2026-05-01** | [Akshay](https://x.com/akshay_pachaar/status/2050201509821063576) | claude-code, skills-mcp, prompting
  Walkthrough of why Claude skills fail silently and how progressive disclosure works: Tier 1 = YAML frontmatter (~100 tokens, always loaded), Tier 2 = SKILL.md body (loads on trigger from description), Tier 3 = bundled scripts (loaded on demand, only stdout enters context). Description quality determines triggering.

- **2026-05-01** | [Allen Braden](https://x.com/allen_explains/status/2050163013165224332) | questionable, industry
  Engagement-farming claim that a 'junior at Jane Street' landed $220K-600K by using AI on trillions of data points. Community Note corrects: it's actually a 2024 Horace He talk on ML systems infra at Jane Street — he was a guest speaker, not an employee, and it has nothing to do with AI for trading.

- **2026-05-01** | [摆烂程序媛](https://x.com/wanerfu/status/2050158295911137370) | dev-practices, questionable
  Translated-from-Chinese promotion of Scrapling (github.com/D4Vinci/Scrapling) — open-source web scraper claiming Cloudflare bypass with no selector maintenance and '774x faster than BeautifulSoup'. Useful for AI scrape pipelines if benchmark holds up.

- **2026-05-01** | [Teknium](https://x.com/teknium/status/2050098631907434871) | agent-design, dev-practices
  Teknium ships a /goal command in NousResearch hermes-agent (PR github.com/NousResearch/hermes-agent/pull/18262) — supervisor-loop pattern inspired by ralph loops + Codex's upcoming /goal: keeps re-prompting the agent until the supervisor judges the task complete.

- **2026-05-01** | [Qwen](https://x.com/alibaba_qwen/status/2049861145574690992) | research, industry
  Alibaba Qwen team open-sources Qwen-Scope, a suite of sparse autoencoders (SAEs) for the Qwen model family. Surfaces interpretable internal features for steering inference, classifying/synthesizing data, debugging code-switching/repetition at the source, and selecting smarter benchmarks. Blog at qwen.ai/blog?id=qwen-scope, weights on HuggingFace.

### Apr 2026

- **2026-04-30** | [Garry Tan](https://x.com/garrytan/status/2049720409965392052) | dev-practices, general
  Garry Tan (YC President & CEO) shipping 10 PRs to GBrain — his personal AI/markdown 'second brain' tool — focused on quality-of-life improvements to make it scale across a corpus of 74k markdown files.

- **2026-04-30** | [How To AI](https://x.com/howtoai_/status/2049567036003795269) | research, agent-design, questionable
  Tencent's Training-Free GRPO claims to replace expensive RL fine-tuning by extracting the 'semantic advantage' from trial-and-error and injecting it as a 'token prior' / memory rather than updating weights — reportedly trained for $18. Hype-framed ("killed fine-tuning") but the underlying technique is a notable alternative to GRPO/RLHF that avoids overfitting and GPU costs.

- **2026-04-30** | [Akshay](https://x.com/akshay_pachaar/status/2049476617144287719) | agent-design, skills-mcp
  Akshay rebuilt 'OpenClaw' core in a single Sim Studio workflow (25 blocks, 29 connections, short+long-term memory, Telegram+Slack channels) without manual coding — pitched as an 'OS for your AI workforce.' Stack is open-source and self-hostable: github.com/simstudioai/sim

- **2026-04-30** | [Darshak Rana](https://x.com/thedarshakrana/status/2049151671692136778) | questionable, general
  Long-form personal development X article ('Your Next 5 Years Will Be an Exact Copy of Your Last 5') riffing on the marshmallow test and the idea that personality is a set of learned thought patterns rather than fixed identity. 1.1M views — engagement-farming framing; not AI-related but Jeremy flagged it.

- **2026-04-28** | [Aparna Dhinakaran](https://x.com/aparnadhinak/status/2047849364547420382) | agent-design, dev-practices
  Aparna Dhinakaran (Arize) on harnesses converging on similar context-passing problems — letting the agent decide context dynamically. Quote-tweets Aran Komatsuzaki on Anthropic's forked subagents (introduced Apr 23, 2026): forked subagents can inherit the same context as the main agent, useful when richer context matters more than minimal context. Direct relevant to the bossman-supervisor concept.

- **2026-04-28** | [Edouard Reinach](https://x.com/ereinach/status/2047802558136058258) | agent-design, research, questionable
  Edouard Reinach points to Predict-RLM (github.com/Trampoline-AI/predict-rlm) — production-ready implementation of an MIT memory technique. Quote-tweets a hype-framed (questionable) summary of a Dec 31 2025 MIT CSAIL paper claiming they solved AI memory by 'teaching it how to read' rather than building a bigger brain. The repo is the actionable bit; the quoted framing is sales pitch.

- **2026-04-28** | [Hasan Toor](https://x.com/hasantoxr/status/2047637109343928827) | agent-design, dev-practices
  Hasan Toor points to future-agi (github.com/future-agi/future-agi + app.futureagi.com) — open-source end-to-end platform for evaluating, observing, and improving production AI agents. Nightly release; stable coming. Worth evaluating alongside other agent-observability tools.

- **2026-04-28** | [Yasir Ai](https://x.com/aiwithyasir/status/2047589529650176333) | dev-practices, agent-design, skills-mcp, questionable
  Hyped pitch ('Breaking', 'terrifying how good') for GitNexus — a knowledge-graph engine for codebases using Tree-sitter AST parsing. Maps every function call, import, class inheritance, interface; clusters code by cohesion; runs blast-radius analysis before changes; coordinates rename across files. MCP-compatible with Claude Code, Cursor, Windsurf. Engagement framing but the underlying capability is interesting.

- **2026-04-25** | [Eric Clemmons](https://x.com/ericclemmons/status/2047838932369387914) | agent-design
  Eric Clemmons: 'Brilliant.' Quote-tweets Teddy Riker's 'Designing for Agents' article — anti-engagement-noise reflective piece (opens with 'If you spend time in the same corner of X as I do, scrolling past the How I built a second brain with Obsidian and Anthropic just KILLED [insert industry] FOREVER posts...').

- **2026-04-25** | [Ethan Mollick](https://x.com/emollick/status/2047828327856030047) | agent-design, management, research
  Ethan Mollick: 'Organizational design for agents is hard, benchmarking agents working in concert is hard. Together, this is the next critical frontier for making AI matter in economically valuable tasks, and we really don't know very much about it.' Quote-tweets @krishnanrohit's essay 'Aligned Agents Still Build Misaligned Organisations.'

- **2026-04-25** | [Atal](https://x.com/zabihullahatal/status/2047692175019008019) | research, agent-design, questionable
  Engagement-framed ('BREAKING') summary of 'Agent Behavioral Contracts' paper — applies Design-by-Contract (preconditions, invariants, governance rules, recovery mechanisms) as runtime constraints on AI agents instead of prompt-only control. Tested across 1,980 sessions. Real concept (formal verification meets agent runtime) worth tracking under the agents-as-judges concept thread.

- **2026-04-23** | [StacyOnChain](https://x.com/stacyonchain/status/2047278412922831260) | industry, questionable
  Off-topic for AI links — promotional content for centpro.bot (Polymarket trading framework supposedly extracted from 327 real tests). ALL-CAPS engagement framing, crypto-twitter signal. Capturing for completeness but not useful as AI/agents reference.

- **2026-04-23** | [Tom Dörr](https://x.com/tom_doerr/status/2047258779821949384) | research, agent-design
  Tom Dörr points to CORAL (github.com/Human-Agent-Society/CORAL) — infrastructure for multi-agent self-evolution. Worth a look as a research substrate for agents-that-improve-themselves work.

- **2026-04-23** | [Akshay](https://x.com/akshay_pachaar/status/2047220248081015110) | agent-design, skills-mcp, research
  Akshay extends Karpathy's wiki idea: a markdown wiki works for static knowledge but breaks for multi-entity questions like 'which authors moved from Google to Anthropic between 2022-2024 and what did they publish after?' A wiki can only answer that if someone already wrote the article; a graph (entities + relations + dates) lets you ask any variation directly. Argues the next step beyond LLM-maintained wikis is LLM-maintained knowledge graphs.

- **2026-04-23** | [How To AI](https://x.com/howtoai_/status/2047187640781541882) | research, agent-design
  [Post unavailable — page doesn't exist]

- **2026-04-23** | [TRAE](https://x.com/trae_ai/status/2047145274200768969) | agent-design, dev-practices, research
  TRAE's 'Definitive Guide to Harness Engineering' X article — frames harness engineering as the 2026 successor to prompt + context engineering. Term coined by Mitchell Hashimoto (HashiCorp co-founder); gained traction via an OpenAI report. Horse-and-reins metaphor: AI Agent = SOTA Model (wild horse) + Harness (control system) = Elite Performer. Foundational reading for the harness-engineering concept thread alongside Rahul/walkinglabs/Anthropic papers.

- **2026-04-23** | [Shiv](https://x.com/shivsakhuja/status/2047124337191444844) | skills-mcp, agent-design
  Shiv on 'Skill Graphs 2.0' — composing skills into a graph (markdown + scripts) where skills depend on other skills (e.g., draft-marketing-email depends on graphic-design). The original skill-graph idea got traction; the v2 wrinkle is that agents stop reliably calling skills past a certain graph depth. Worth tracking alongside Pocock's /teach skill, Akshay's Claude Code 12 features, and the general skills-as-reusable-routines concept.

- **2026-04-23** | [Shrey Pandya](https://x.com/shreypandya/status/2047100550446280792) | skills-mcp, agent-design
  Shrey Pandya introduces the /autobrowse skill (inspired by Karpathy's autoresearch harness). Pattern: agent explores a web task via the @browserbase CLI, learns from previous attempts' failures, iterates until it converges on a reliable workflow. Once token usage is optimized, the winning approach 'graduates' into a reusable skill. Direct reference for the let-it-cook / routines-as-higher-order-prompts concept.

- **2026-04-23** | [ClaudeDevs](https://x.com/claudedevs/status/2047086372666921217) | claude-code, skills-mcp, agent-design
  Anthropic ClaudeDevs blog post: 'Building agents that reach production systems with MCP' (claude.com/blog/building-agents-that-reach-production-systems-with-mcp). Covers when agents should use direct APIs vs CLIs vs MCP, patterns for building MCP servers, context-efficient client design, and pairing MCP with skills. Direct first-party reading for any agent-to-production pipeline work.

- **2026-04-23** | [Matt Van Horn](https://x.com/mvanhorn/status/2047073560267817469) | agent-design, dev-practices
  Matt Van Horn endorses Compound Engineering v3 (Trevin Chow's project, ~15k stars) — names brainstorm and plan artifacts that give requirements a paper trail from idea to commit, harness alignment across the build. Worth a real evaluation as a methodology framework alongside harness engineering.

- **2026-04-23** | [Mario Zechner](https://x.com/badlogicgames/status/2047055760236916759) | agent-design
  Mario Zechner: 'recommended reading.' Quote-tweets @walden_yan's 'Multi-Agents: What's Actually Working' — a 10-months-later follow-up to his earlier 'Don't Build Multi-Agents' essay. The two-essay arc is worth reading together: an evolving view from a thoughtful critic of multi-agent overreach.

- **2026-04-23** | [Vida](https://x.com/vida_agent/status/2047007924279767332) | agent-design, skills-mcp
  Vida open-sourced OpenChronicle (github.com/Einsia/OpenChronicle) — a local-first memory layer for tool-capable LLMs and agents, framed as a free alternative to OpenAI Chronicle's $100/mo paywall. Fits the agent-memory infrastructure concept thread.

- **2026-04-23** | [Alex Volkov](https://x.com/altryne/status/2046977133013311814) | research, industry
  OpenAI open-sourced Privacy Filter — a 1.5B-param (50M active) PII detection model on HuggingFace under Apache 2.0. Not a new general LLM; a focused safety-utility model for detecting private info in text. Volkov calls it interesting; useful as a building block in agent pipelines that touch user data.

- **2026-04-23** | [Garry Tan](https://x.com/garrytan/status/2046882636069798323) | agent-design, skills-mcp, claude-code
  Garry Tan: 'Basically how I'm building all my features these days: Do it once in OpenClaw, then just run /skillify and it does it like that forever.' Quote-tweets his own article on stopping agents making the same mistakes (contrasts with LangChain's $160M/3yr/LangSmith trajectory-evals stack). Fits the skills-as-routines thread.

- **2026-04-23** | [spencer](https://x.com/techspence/status/2046759185593794782) | research, dev-practices
  spencer flags OWASP's Autonomous Penetration Testing Standard (github.com/OWASP/APTS) — formal security standard for AI-driven pentesting. Reference for security-team adjacent work; substance pending a real read.

- **2026-04-23** | [Avi Chawla](https://x.com/_avichawla/status/2046685172666712571) | claude-code, skills-mcp, dev-practices
  Avi Chawla reports 3x token reduction on Claude Code (10.4M → 3.7M tokens, 10 errors → 0, $9.21 → $2.81) by using Insforge Skills + CLI (github.com/InsForge/InsForge) as a backend context-engineering layer — without changing CLAUDE.md, prompts, or models. Open-source and local. Worth measuring against on a real session.

- **2026-04-21** | [Shubham Saboo](https://x.com/saboo_shubham_/status/2046473615118672325) | agent-design, skills-mcp
  Shares agentic-stack — 'One brain, many harnesses. Portable .agent/ folder (memory + skills)' — a pattern for sharing a single memory/skill store across multiple agent harnesses. Repo: github.com/codejunkie99/agentic-stack.

- **2026-04-21** | [Tech with Mak](https://x.com/technmak/status/2046414820241760620) | research, agent-design, questionable
  Summary of Meta's REFRAG paper: compresses retrieved RAG chunks into single embeddings (16,384 tokens → 1,024 chunk embeddings), delivering 30.85x faster time-to-first-token, zero perplexity loss, 16x context extension (4K → 64K), and 3.75x better than prior SOTA. Exploits sparse attention patterns in RAG contexts via precomputable embeddings and RL-based compression policy.

- **2026-04-21** | [Aakash Gupta](https://x.com/aakashgupta/status/2046371351016161745) | industry, research
  Long analysis of Yann LeCun's post-Meta 'LeWorldModel' JEPA result: first JEPA that trains end-to-end from raw pixels (15M params, single GPU, hours), replacing a pile of collapse-prevention heuristics with one Gaussian-normality regularizer (hyperparam search O(n^6)->O(log n)). Claims 200x fewer tokens/observation than DINO-WM and planning 47s->0.98s/cycle — a potential reset of the humanoid-robotics cost structure, framed as Meta's Xerox-PARC moment.

- **2026-04-21** | [Tom Dörr](https://x.com/tom_doerr/status/2046369616411185635) | agent-design
  Shares a recursive self-improving agent harness (github.com/greyhaven-ai/autocontext) — an agent scaffold designed to iterate on and improve its own context/behavior.

- **2026-04-21** | [Sydney Runkle](https://x.com/sydneyrunkle/status/2046277232537256002) | agent-design, dev-practices
  LangChain team piece on 'The runtime behind production deep agents' — distinguishing the harness (prompts, tools, skills, model loop) from the runtime (durable execution, memory, multi-tenancy, observability). Walks through production requirements for agents and how LangSmith Deployment + Agent Server package those capabilities. Reference architecture for shipping agents in production.

- **2026-04-21** | [Nav Toor](https://x.com/heynavtoor/status/2046276160930414976) | research, dev-practices
  Intro to PoisonedRAG attack: researchers showed 5 malicious documents planted in a 2.6M-document corpus can hijack an LLM's answer 97% of the time. Attacker never touches the model or retriever — just writes documents. Important RAG security consideration.

- **2026-04-21** | [Simplifying AI](https://x.com/simplifyinai/status/2046271932035645599) | research, questionable
  Summary of Microsoft's MEMENTO paper: instead of growing the KV cache to fit long reasoning chains, train the model to break reasoning into blocks and emit dense compressed 'memento' summaries between them, then drop the raw tokens. Framed as 'the secret isn't remembering everything — it's knowing what to forget.' Engagement-farming tone but real underlying paper.

- **2026-04-21** | [Sigrid Jin](https://x.com/realsigridjin/status/2046266374948069387) | agent-design, skills-mcp, dev-practices
  Quote-tweet of Junghwan Na's writeup — Na got his GitHub banned after pushing 500+ commits across 100+ open-source repos in 72 hours using an AI harness. Sigrid pulls out the two highest-leverage principles from Na's method: (1) reproduce the bug locally or drop it, (2) read merge history instead of CONTRIBUTING.md. Jeremy flagged 'worth extracting a skill' — these are skill-worthy contribution-harness patterns.

- **2026-04-21** | [Raymond Weitekamp](https://x.com/raw_works/status/2046240194999755153) | agent-design, prompting, research
  Long-form X article 'RLMs are the new reasoning models': Recursive Language Models let a root model treat its own prompt as an environment it inspects/slices/recursively subqueries via a REPL, collapsing reasoning and tool use into one inference abstraction and processing inputs orders of magnitude beyond the context window. Traces the reasoning-vs-tool-use history (CoT, ReAct, Toolformer, o1) and the Oolong/LongMemEval/LongCoT benchmark arc where RLM scaffolds post leading numbers — including small models (Qwen3-8B/27B) jumping well past their base, hinting the frontier stops being GPU-rich-only. Flags cost/time and 'models are bad at acting recursively' as open limits.

- **2026-04-21** | [Ihtesham Ali](https://x.com/ihtesham2005/status/2046197374855582157) | prompting, agent-design, management
  Writeup of George Pólya's 1945 book 'How to Solve It' — the four-step problem-solving framework (understand, plan, execute, look back). Central heuristic: if you can't solve the proposed problem, solve a simpler related one first. Jeremy's note 'important for planner?' — relevant for AI agent planning/decomposition patterns.

- **2026-04-21** | [Vox](https://x.com/voxyz_ai/status/2045899539526148193) | claude-code, prompting, dev-practices
  The #1 GitHub trending repo this week (44,465 stars) is a CLAUDE.md file distilling Andrej Karpathy's LLM coding pitfalls into 4 principles: (1) think before coding — ask when unsure, (2) simplicity first — minimum code, (3) surgical edits — only touch what's required, (4) goal-driven — translate fuzzy instructions into verifiable targets. Directly actionable as a CLAUDE.md system prompt.

- **2026-04-20** | [Akshay](https://x.com/akshay_pachaar/status/2046151867177308181) | research, agent-design, dev-practices
  Akshay summarizes Google DeepMind's 'AI Agent Traps' paper — the first systematic framework for adversarial content engineered to hijack AI agents browsing the web. Maps six attack surfaces: Content Injection (perception: invisible CSS, hidden HTML, steganographic payloads in images — HTML injections hijack web agents in up to 86% of scenarios), Semantic Manipulation (reasoning: biased framing weaponizing cognitive biases), Cognitive State Traps (memory: RAG poisoning, long-term memory corruption), plus three more not visible in the truncated scrape. High-priority reading for anyone building agents that browse arbitrary web content.

- **2026-04-20** | [Kenneth Auchenberg](https://x.com/auchenberg/status/2045940742678368570) | agent-design
  Kenneth Auchenberg highlights an article arguing that in the "harness era" of AI agents the harness is the application and the sandbox is the server, framing swarms as harnesses managing harnesses.

- **2026-04-20** | [AYi](https://x.com/ayi_ainotes/status/2045874192155824616) | research, claude-code
  AYi (translated from Chinese) recaps OpenMythos, an open-source first-principles reconstruction of Anthropic's "Claude Mythos" as a looped/recurrent transformer with MoE routing: the same weights run ~16x per forward pass so reasoning happens silently in latent space. Argues a 770B recurrent model can match a 1.3T standard model and that future scaling competes on loop-count rather than parameter count.

- **2026-04-19** | [Garry Tan](https://x.com/garrytan/status/2045427057656729985) | agent-design, dev-practices
  Garry Tan launches GBrain v0.11 with "Minions," a BullMQ-style queue/jobs system built on Postgres/PGLite to make OpenClaw/GBrain subagents faster and more reliable instead of timing out.

- **2026-04-18** | [Akshay](https://x.com/akshay_pachaar/status/2045404494641733962) | agent-design, claude-code, research
  Akshay summarizes a UCL paper (arXiv:2604.14228) dissecting Claude Code's architecture: only 1.6% of the codebase is AI decision logic while 98.4% is operational harness (permission gates with 7 modes, tool routing, a 5-layer context compaction pipeline, subagents that return only summaries). Core thesis: as frontier models converge on raw coding ability, harness quality, not the model, becomes the differentiator.

- **2026-04-18** | [Alex Ker](https://x.com/thealexker/status/2045203785304232162) | agent-design, prompting, dev-practices, claude-code
  Alex Ker's deep-dive guide on optimizing AI coding harnesses: keep config/.md files lean and human-written (frontier LLMs hit a "dumb zone" past a few hundred instructions), use progressive disclosure for CLIs/skills/MCP tools, structure prompts with HumanLayer's Research-Plan-Implement (R.P.I.) framework, and use subagents (parallel fan-out for breadth, pipelines for depth) to keep the main context clean. Core argument: the harness, not the model, is where engineering judgment compounds, so commit to one and iterate.

- **2026-04-18** | [Daniel Miessler](https://x.com/danielmiessler/status/2045148852047827449) | agent-design, skills-mcp
  Daniel Miessler recommends Interceptor (by Ronald Eddings) as the best browser-control system for AI agents he's used out of 100+, now the highest-value addition to his PAI harness.

- **2026-04-18** | [Kevin Simback](https://x.com/ksimback/status/2045120939680038923) | industry, agent-design
  Kevin Simback shares his article "The AI Agent Moat Is Real, but Narrower Than You Think," arguing that the durable moat in the agent space isn't the harness itself but lies elsewhere, after going deep on where to invest and build in the agent space.

- **2026-04-18** | [PolyArb](https://x.com/usepolyarb/status/2045109166599963026) | industry, general
  [Post unavailable — page doesn't exist]

- **2026-04-18** | [Eric Hartford](https://x.com/quixiai/status/2044952124568527298) | research, agent-design, dev-practices, industry
  Eric Hartford releases Clearwing, an MIT-licensed open-source vulnerability-discovery engine that reproduces Anthropic's "Project Glasswing" results with any LLM. His argument: the real innovation isn't the gated Claude Mythos model but the model-agnostic pipeline, rank files by attack surface, fan out hundreds of file-scoped agents, use crash oracles (AddressSanitizer/UBSan) as ground truth, and run a verification agent to filter noise. Reproduced findings with OpenAI Codex 5.4 and a Qwen3.5 finetune.

- **2026-04-17** | [Alter Ego](https://x.com/alterego_eth/status/2045093809886020058) | agent-design, skills-mcp, questionable
  Alter Ego promotes Nous Research's Hermes Agent, a self-hosted agent that writes its own skills after each task, keeps persistent memory (MEMORY.md/USER.md/SQLite), and runs 24/7 on a VPS with a closed learn-improve loop every ~15 tool calls, using it to build a self-learning Polymarket weather-trading bot. Heavy promotional/profit framing.

- **2026-04-17** | [0xSero](https://x.com/0xsero/status/2044879665001595263) | agent-design, claude-code, management
  0xSero (quote-tweeting Sarah Chieng's article 'Single-agent AI coding is a nightmare for engineers') says he's gone 180 on multi-agents/subagents after analyzing hundreds of AI coding agent sessions — they actually help a lot. Practitioner's change-of-mind about orchestration.

- **2026-04-17** | [Hamudi](https://x.com/hamudinaanaa/status/2044872907072164304) | industry, agent-design, management, research
  Hamudi ties into Sequoia's "$1T thesis" that AI sells outcomes (work) rather than software tools, introducing "Outcome Primitives" as a way to measure economic outcomes, citing a published paper tracking 1,300 agents over 21 days that created $32M in value (jobs secured, $200k grants won, e-commerce shops shipped). Framing: copilots compete on software margins and lose to big labs; outcome engines compete on services margins.

- **2026-04-15** | [Garry Tan](https://x.com/garrytan/status/2044479509874020852) | agent-design, skills-mcp
  X article: "Resolvers: The Routing Table for Intelligence" — argues resolvers (context-routing rules: when task X appears, load document Y first) are the most important but invisible component of agent systems. Follows up on "Thin Harness, Fat Skills" framework. 21K views.

- **2026-04-15** | [GitHub Projects Community](https://x.com/githubprojects/status/2044453433743458686) | agent-design, dev-practices
  Tool share: Graphify (osp.fyi/graphify) turns any folder of code into a queryable knowledge graph instantly — code-as-graph for agent/dev navigation and retrieval.

- **2026-04-15** | [Yoonho Lee](https://x.com/yoonholeee/status/2044442372864700510) | research, agent-design
  Released code for Meta-Harness — a method to autonomously improve LLM evaluation harnesses on problems humans are actively working on, solving long-horizon credit assignment over code, traces, and scores. Repo at github.com/stanford-iris-lab/meta-harness with ONBOARDING.md for agent-guided setup.

- **2026-04-15** | [Viv](https://x.com/vtrivedy10/status/2044430694458310870) | dev-practices
  Points to Hunter Leath's article "Bash is the SQL for file systems" — a deep dive on storage, filesystems, and egress fees from cloud providers. Framed as must-read alpha for anyone working at the storage/filesystem layer.

- **2026-04-15** | [Shann³](https://x.com/shannholmberg/status/2044413638388363272) | agent-design, skills-mcp
  Built a 230-page Obsidian knowledge base (tweets, bookmarks, articles, notes) and connected it to every AI agent project using qmd (Tobi Lütke's tool) with hybrid BM25+vector search and LLM re-ranking. Any agent in any project now searches this global wiki before brainstorming or planning.

- **2026-04-15** | [Millie Marconi](https://x.com/milliemarconnni/status/2044358003714097601) | prompting, claude-code
  Uses Claude as a full inversion engine running Charlie Munger's method — mapping every path to failure to make the path to success obvious by elimination. Shares 5 prompts for applying systematic inversion to any problem.

- **2026-04-15** | [Akshay](https://x.com/akshay_pachaar/status/2044329897603244093) | agent-design, research, skills-mcp, dev-practices
  Akshay argues agent memory is three-dimensional, needing a relational store for provenance, a vector store for semantics, and a graph store for relationships, because flat vector search misses multi-hop connections (the "bridge" fact that links two entities). He points to Cognee, an open-source project that unifies all three behind four async calls (default embedded SQLite+LanceDB+Kuzu, swappable for Postgres/Qdrant/Neo4j).

- **2026-04-15** | [Europurr](https://x.com/vrloom/status/2044314974101877175) | agent-design
  Europurr reports switching from OpenClaw to Nous Research's Hermes agent and setting up its "Hindsight" memory, calling it light-years ahead of OpenClaw.

- **2026-04-15** | [Garry Tan](https://x.com/garrytan/status/2044291663213015491) | agent-design, skills-mcp, dev-practices
  Garry Tan releases GBrain v0.10.0, packaging his personal OpenClaw "brain" for others: refined RESOLVER.md and SOUL.md, ACLs for multi-user brain access, and 24 distinct "fat" skills shipped with e2e tests, evals, and unit tests.

- **2026-04-15** | [Shaw (spirit/acc)](https://x.com/shawmakesmagic/status/2044269097647779990) | prompting, dev-practices, agent-design
  Shaw shares a reusable prompt for cleaning up "vibecoded" codebases by spawning 8 parallel subagents, each owning one cleanup task: DRY/dedup, consolidating shared types, removing unused code (knip), untangling circular deps (madge), replacing weak types (any/unknown), stripping needless defensive try/catch, removing legacy/fallback paths, and cutting AI-slop comments. Each subagent researches, writes a critical assessment, then implements high-confidence fixes.

- **2026-04-15** | [Erick](https://x.com/ericksky/status/2044225008419922270) | general
  [Post unavailable — login wall or deleted]

- **2026-04-15** | [mr-r0b0t](https://x.com/mr_r0b0t/status/2044199154004472009) | agent-design, dev-practices
  Amplifies a tip on a 3-tool agent web stack: SearXNG for candidate source discovery, Firecrawl for known-URL scraping, Camofox for JS/interaction browser fallback. Described as essential for any agent doing web search or scraping.

- **2026-04-15** | [klöss](https://x.com/kloss_xyz/status/2044169678961234282) | agent-design, claude-code, dev-practices
  klss argues agents fail across repos because of unstructured markdown, and proposes a four-folder convention to remove ambiguity: /audits (proof), /docs (description), /plans (intent), /specs (law). Separating intent from proof from law stops Claude Code, Codex, and Cursor agents from hallucinating context.

- **2026-04-15** | [0xSero](https://x.com/0xsero/status/2044165332928213243) | research, dev-practices
  Guide to running large LLMs on limited hardware: use REAPs (50% savings), quantization (AWQ/GPTQ/W4A16/FP8 for fast inference; GGUF/EXL3 for compatibility; MLX for Apple silicon), and 8-bit KV cache (50-75% savings). Practical tips for local AI deployment.

- **2026-04-15** | [Paul Bakaus](https://x.com/pbakaus/status/2044118871326765541) | claude-code, agent-design, general
  Paul Bakaus praises Matt Sims (English PhD plus ML/startup background) for building in the open at the intersection of creativity, storytelling, and AI. Quote-tweets Sims on teaching Claude Code to think systematically, getting consistent answers to recurring review-for-security / sufficient-tests / update-instruction-files prompts.

- **2026-04-15** | [kwindla](https://x.com/kwindla/status/2044106314612408437) | agent-design, research, dev-practices
  kwindla introduces Gradient Bang, claimed to be the first massively-multiplayer, fully LLM-driven game: a retro space-trading game (Factorio-like) where you cajole a ship AI into tasking other AIs. Built to explore sub-agent orchestration, partial context sharing across inference loops, long contexts and episodic memory, LLM-generated dynamic UIs, and voice input. Built on pipecat_ai plus Supabase and Vercel, fully open source.

- **2026-04-15** | [Punisher](https://x.com/0x_punisher/status/2044100729133019416) | questionable, general
  [Promotional / paid partnership] A guide to a Polymarket sweeper bot that profits not by prediction but by FIFO-queueing bids near $0.999 on already-decided markets to absorb mispriced liquidity, covering resolution detection, latency, and capital allocation. Ends with wallet/PnL claims and a Telegram funnel. Off-topic crypto money-making content rather than AI tooling.

- **2026-04-15** | [StacyOnChain](https://x.com/stacyonchain/status/2044069002192847200) | questionable, general
  [Engagement-farming / crypto promo] StacyOnChain hypes an institutional-grade Polymarket bot architecture (fractional Kelly sizing, latency optimizations), urging readers to bookmark and download before it is pulled, and quote-tweets their own how-we-built-a-Polymarket-bot article. Off-topic relative to the AI tooling collection.

- **2026-04-15** | [Garry Tan](https://x.com/garrytan/status/2044059516497711522) | management, industry
  Garry Tan amplifies Alfred Lin's article 'Heat Seeking Missile for Pain': the realest founders actively hunt the hairiest, gnarliest problems and surgically destroy them, citing an interview with Keller of Zipline.

- **2026-04-15** | [Ihtesham Ali](https://x.com/ihtesham2005/status/2044056849272705246) | agent-design, skills-mcp
  Aurogen is an open-source (MIT) OpenClaw fork whose differentiator is true multi-agent, multi-instance orchestration inside one deployment: modular agents/channels/providers/skills, a pure web-panel setup with no config files or CLI, ClaWHub skill imports, one-click installers, and it runs on a $50 Linux SBC (github.com/UniRound-Tec/Aurogen).

- **2026-04-15** | [Amir Salihefendić](https://x.com/amix3k/status/2044046057315742146) | management, agent-design
  Amir Salihefendić (Doist) treats Jack Dorsey's recent framing as an org-design question for companies blending human and machine intelligence: remote-first, transparent, functional teams with clear DRIs, where AI increasingly supplies the 'connective tissue' that moves context across teams, tools, and decisions.

- **2026-04-15** | [Indie Fox](https://x.com/indie_maker_fox/status/2043857352282255829) | skills-mcp, claude-code, agent-design
  Indie Fox praises a Claude skill that generates very high-quality software architecture diagrams (github.com/Cocoon-AI/architecture-diagram-generator), showing an OpenHarness architecture diagram as an example of its clean output.

- **2026-04-15** | [Mario Zechner](https://x.com/badlogicgames/status/2043757216885256463) | dev-practices, agent-design, prompting
  Mario Zechner recommends Alex Volkov's article 'The Z/L Continuum — Do AI engineers even need to read code anymore?' (thursdai.news/zl), which asks how much code AI engineers still need to read in 2026 and beyond.

- **2026-04-14** | [Alex Vacca](https://x.com/itsalexvacca/status/2043834187095150673) | industry, management
  Growth/marketing content (mostly off the AI/dev core): endorses Michel Lieben's article on running a 4-layer funnel instead of a bare 'book a call', citing a $7M-ARR bootstrapped funnel (330k visitors, 1,500+ meetings, $4M new ARR). Relevant only as go-to-market reading.

- **2026-04-14** | [am.will](https://x.com/llmjunky/status/2043817254152814785) | dev-practices, industry
  How to get free NVIDIA API credits for open-source models via the OpenAI-compatible endpoint integrate.api.nvidia.com/v1 (Minimax 2.7, Qwen 3.5, GLM 5, Gemma, Nemotron). Won't match Opus-tier, but the author rates Minimax M2.7's 'personality' highly; includes a paste-ready client config block. Useful for cheap/free local-agent experimentation.

- **2026-04-14** | [Phil Chen](https://x.com/philhchen/status/2043759400121458922) | agent-design, claude-code, dev-practices
  'How I built Filbert' — a background coding agent that is a lightweight wrapper around an existing harness running on the team's own infra with full dev-env access and recursive self-improvement. Per the linked article it wrote 95% of the team's PRs in a week and runs 14 scheduled jobs daily (bug triage, security audits, dead-code sweeps, CI optimization). Strong template for self-hosted background agents.

- **2026-04-14** | [How To Prompt](https://x.com/howtoai_/status/2043753502850351525) | research, questionable
  Hype-framed math claim ('God Particle for calculus'): a paper reportedly shows every elementary function can be generated by one binary operator eml(x,y)=exp(x)-ln(y) plus the constant 1, found by exhaustive search, analogous to the NAND gate. Pitches an AI angle — one uniform trainable circuit instead of juggling math primitives. Interesting if true, but clickbait presentation warrants skepticism.

- **2026-04-14** | [Kevin Simback](https://x.com/ksimback/status/2043745657748361476) | agent-design, prompting, claude-code
  'My Second Brain Setup: A Modified Karpathy Method' — builds on Karpathy's LLM-knowledge-base pattern (LLM incrementally compiles sources into an interlinked markdown wiki; LLM=programmer, wiki=codebase, Obsidian=IDE) and adds a two-author rule: an `author: kevin` vs `author: agent` frontmatter field where human-authored files are untouchable. Runs on Claude Code with five slash commands (/research fanning out 5-8 parallel agents, /ingest, /wiki-query, /wiki-lint, /wiki-output) and a 'graduation' loop that promotes good agent pages into the protected human layer.

- **2026-04-14** | [Akshay](https://x.com/akshay_pachaar/status/2043745099792953508) | agent-design
  Akshay provides a first-principles walkthrough of agent memory: from Python lists to markdown files to vector search to graph-vector hybrids. Covers 7 failure modes of stateless agents (context amnesia, zero personalization, repeated mistakes, etc.) and builds up to a clean open-source solution for persistent agent memory.

- **2026-04-14** | [Alex Finn](https://x.com/alexfinn/status/2043719233213980922) | prompting, claude-code
  Alex Finn shares a SOUL.md prompt philosophy inspired by Garry Tan's post: demand completeness over 'good enough,' never table things for later when the permanent solve is in reach, always ship with tests and documentation. Includes a copy-paste prompt for OpenClaw/Hermes agents.

- **2026-04-14** | [Philipp Schmid](https://x.com/_philschmid/status/2043705197030002904) | agent-design, skills-mcp
  Links a practical guide '8 Tips for Writing Agent Skills' — covering what kinds of skills exist, how to write them well, and when to retire one. Directly relevant to the skills/plugins workflow.

- **2026-04-14** | [North@CreaoAI](https://x.com/anorth_chen/status/2043694726764003817) | agent-design, management, industry
  Endorses (translated from Chinese) an 'AI-First' engineering essay by the author's CTO: after going AI-first, the team merges/deploys 20+ PRs daily with ~99% of production code written by AI, shipping and A/B-killing features within a day. Argument: teams stuck in 'AI-assisted' rather than 'AI-first' mode risk fading from the market within a year. Provocative management/strategy read.

- **2026-04-14** | [Tech with Mak](https://x.com/technmak/status/2043683120319520806) | claude-code, dev-practices, prompting
  Distills three Karpathy critiques of coding agents (wrong assumptions unchecked, overcomplication/bloat, editing code they don't understand) into a drop-in CLAUDE.md with four principles: (1) think before coding / surface ambiguity and push back, (2) simplicity first / no unrequested abstractions, (3) surgical changes / don't touch adjacent code, (4) goal-driven execution / turn tasks into failing tests then loop to green. Practical, copy-paste engineering guardrails.

- **2026-04-14** | [Lorenzo Rondan](https://x.com/lorenrd/status/2043677918262395235) | agent-design
  Highlights Viv (@Vtrivedy10)'s diagram/mental-model of an agent harness — memory, context fragments, and the search 'bitter lesson' — calling it one of the best harness diagrams around. Pointer into the harness-design discourse.

- **2026-04-14** | [Vaishnavi](https://x.com/_vmlops/status/2043624154646409708) | dev-practices, agent-design, questionable
  Vaishnavi covers Google's open-sourced Magika — an AI-powered file content type detection tool. Trained on 100M files, 200+ content types, 99% accuracy at 5ms/file. Sees through renamed malware and disguised scripts. Install via pip install magika. github.com/google/magika

- **2026-04-14** | [Noisy](https://x.com/noisyb0y1/status/2043609541477044439) | claude-code, agent-design, dev-practices, questionable
  Noisy describes a Google engineer who automated 80% of his work with Claude Code using a CLAUDE.md file based on Karpathy's principles and a .NET orchestration app. Covers the Karpathy-inspired CLAUDE.md, a dotnet service that spawns Claude Code instances with git worktrees, and a review pipeline. Claims $28K passive income working 2-3 hours/day.

- **2026-04-13** | [Garry Tan](https://x.com/garrytan/status/2043581361798500602) | prompting, management, claude-code
  Garry Tan adds 'Boil the ocean' to his SOUL.md: the marginal cost of completeness is near zero with AI. Do the whole thing with tests, docs, and quality. Never table for later, never present workarounds, never leave dangling threads. 433.1K views.

- **2026-04-13** | [Defileo](https://x.com/defileo/status/2043437202190024912) | prompting, questionable
  Defileo promotes a 'prompt vault' going beyond the classic f/prompts.chat role-based prompts (159K GitHub stars). Claims deeper structured prompts with phases, diagnostic questions, and domain-specific workflows for Claude. Engagement-farming style but references the real prompts.chat repo.

- **2026-04-13** | [Charly Wargnier](https://x.com/datachaz/status/2043246635996807300) | skills-mcp, dev-practices, agent-design
  Charly Wargnier covers Addy Osmani's (Google) new Agent Skills package: 19 engineering skills + 7 commands for AI coding agents, based on Google best practices. Covers the full dev lifecycle — define (specs), plan (decompose), build (incremental), verify (TDD), review (security), ship (CI/CD). Aims to prevent agents from skipping quality gates.

- **2026-04-12** | [Ahmad](https://x.com/theahmadosman/status/2043366810494337354) | agent-design, dev-practices
  A concise recipe for running parallel agents: either have one agent fan out or drive deterministic script runs — spin up workers, isolate each in a git worktree, gate merges with diffs, add backups/rules/logs for deterministic runs, and merge only what passes. Author is packaging it as a Skill.

- **2026-04-12** | [Garry Tan](https://x.com/garrytan/status/2043339811088699446) | agent-design, research, industry
  Garry Tan on open-source agent self-improvement: applied research now happens in the open, and 'just-in-time software' is a new paradigm. Quotes an analysis of the Hermes agent architecture taking a more explicit self-improvement route than typical offline trajectory-mining systems.

- **2026-04-12** | [Nav Toor](https://x.com/heynavtoor/status/2043321909971202403) | agent-design
  Nav Toor covers LLM Wiki v2 — an extension of Karpathy's original LLM Wiki pattern (5K stars in 48h). Adds confidence scoring (source count, recency, contradictions), memory tiers (working/episodic/semantic/procedural), knowledge graphs with typed entities, automated hooks, and forgetting curves for knowledge decay.

- **2026-04-12** | [Garry Tan](https://x.com/garrytan/status/2043198780800197025) | agent-design, management, skills-mcp
  'If your memory dies when your harness dies, you built the harness too thick.' Argues for thin harnesses: memory is markdown, skills are markdown, the 'brain' is a git repo, and the harness is a thin conductor that reads files it doesn't own. Endorses Harrison Chase's 'Your harness, your memory' article on harness/memory coupling and the risk of closed harnesses.

- **2026-04-12** | [Nick Spisak](https://x.com/nickspisak_/status/2043060265823146202) | claude-code
  Nick Spisak explains Claude Code's new /ultraplan feature: 4 Opus agents plan in parallel (3 explorers + 1 critic) on Anthropic's cloud. Covers when the review workflow matters more than speed, 5 scenarios preventing hours of rework, and when to skip it for local plan mode instead. 250.3K views.

- **2026-04-12** | [Garry Tan](https://x.com/garrytan/status/2042919242283258072) | agent-design, skills-mcp
  Garry Tan announces GBrain's new guided integration recipes for OpenClaw and Hermes Agent setup. Addresses the struggle new users face getting integrations (mail, calendar, etc.) configured, which is needed to scale to thousands of markdown files in the knowledge base. 36.5K views.

- **2026-04-11** | [Nav Toor](https://x.com/heynavtoor/status/2042879339256254689) | research, industry, questionable
  Covers Kronos, an open-source foundation model for financial markets trained on 12 billion candlestick records from 45 exchanges (Binance, NYSE, NASDAQ, LSE, and more). Claims 93% more accurate than leading time series models, zero-shot across any asset/timeframe. Built at Tsinghua University, accepted at AAAI 2026. Ships in 4 sizes from 4M to 499M params; live BTC demo running. Available on HuggingFace.

- **2026-04-10** | [Veeral Patel](https://x.com/vral/status/2042674854764130549) | agent-design, research
  Quote-tweets Ramp Labs article on "Latent Briefing" — a KV cache compaction technique for efficient memory sharing across multi-agent systems. Patel quips that passing .md files between agents will soon seem as archaic as mailing floppy disks. Paper tackles token inefficiency in hierarchical multi-agent architectures.

- **2026-04-10** | [Alpha Batcher](https://x.com/alphabatcher/status/2042606770816704643) | agent-design, claude-code, dev-practices
  Distills architectural principles for production AI agents by quoting Rohit's article reverse-engineering Claude Code's architecture (github.com/rohit4verse). Key patterns: async generators for streaming, parallel read-only tools vs serial write tools, tools executing during generation (not after), system prompt designed for cache efficiency, hierarchical context compaction cheapest-first, isolated worktree per sub-agent. Calls it the most detailed public breakdown of a production agent architecture available.

- **2026-04-10** | [Akshay](https://x.com/akshay_pachaar/status/2042586319390674994) | agent-design
  Comparison of how Anthropic, OpenAI, CrewAI, and LangChain approach the agent harness differently. The one agreement: the model is not the product, the infrastructure around it is. Anthropic bets on a deliberately thin "dumb loop" harness where the model makes all decisions. OpenAI takes a similar but slightly thicker approach. CrewAI and LangChain bet on heavier orchestration infrastructure. The core architectural question: as models get smarter, do you need less infrastructure or more?

- **2026-04-10** | [Vaishnavi](https://x.com/_vmlops/status/2042486942802321552) | skills-mcp, agent-design
  Google open-sourced MCP Toolbox (github.com/googleapis/mcp-toolbox) — an MCP server that gives AI agents direct access to 20+ enterprise databases (Postgres, MySQL, MongoDB, BigQuery, Redis, Elasticsearch, Spanner, Snowflake) in plain English. Built-in connection pooling, auth, and OpenTelemetry. Works with LangChain, LlamaIndex, Genkit, and any MCP-compatible client. Less than 10 lines of code to integrate.

- **2026-04-10** | [Sigrid Jin](https://x.com/realsigridjin/status/2042440330503733343) | agent-design, dev-practices
  Summary of "Better Harness" paper on using evals as a flywheel for agent improvement. Key insight: evals are the new training data — instead of updating weights, you update the agent harness. Warns that agents reward-hack evals, so you need strict train/test splits. Quality over quantity in eval design. The flywheel: mine prod traces for failures, turn into evals, auto-tweak prompts/tools, validate, repeat.

- **2026-04-10** | [Teknium](https://x.com/teknium/status/2042396576245825543) | agent-design, claude-code
  Teknium claims Anthropic copied their "notify when done" feature from Hermes Agent (github.com/NousResearch/hermes-agent/pull/5779) — lets background processes notify the agent when finished instead of polling, so the agent can work on other tasks in the same session. Points to Claude Code's new Monitor tool as the equivalent. Makes the case that open source moves faster than closed companies.

- **2026-04-10** | [ProxySoul](https://x.com/bniwael/status/2042364421373121018) | agent-design, dev-practices
  SoulForge — an open-source AI coding agent that builds a live graph of the codebase before the agent reads any code. Uses real LSP via embedded Neovim for go-to-definition, references, and call hierarchy instead of regex hacks. Features multi-tab with cross-tab coordination where agents share context through a real-time bus, and supports mixing models (Opus, Gemini, Haiku, Ollama). Claims 1.8x faster and 2.1x cheaper than standard approaches.

- **2026-04-10** | [Recogard](https://x.com/recogard/status/2042356576032358505) | general
  36 GB dataset of 72 million Polymarket trades available free on GitHub for prediction market analysis. Includes tools to build trading strategies from historical market data — analyze price behavior before resolution, compare category volatility, and find repeating patterns.

- **2026-04-10** | [Aakash Gupta](https://x.com/aakashgupta/status/2042334495664455848) | agent-design, claude-code
  The "advisor pattern" for AI agent cost optimization: run Sonnet for routine execution ($3/$15 per MTok) and fire a tool call to Opus only for genuine decision points. Both models share full context, eliminating the fragmentation problem in multi-model architectures. Claude Code has been doing this internally. Practical architecture for any company hitting the cost wall with frontier models in production agent loops.

- **2026-04-10** | [Seb Goddijn](https://x.com/sebgoddijn/status/2042286523001737545) | management, claude-code, agent-design
  Ramp hit 99% AI adoption company-wide but found most employees stuck in chat windows while power users ran laps. They built "Glass" — an internal AI productivity suite on Anthropic's Claude Agent SDK — reaching 700 DAUs in one month. Philosophy: raise the floor for all employees rather than lowering the ceiling for power users.

- **2026-04-10** | [Santiago](https://x.com/svpino/status/2042275938390639069) | research, industry
  Engramme (engramme.com) — a startup building "Large Memory Models," a new architecture designed specifically for how human memory works. Instead of RAG or vector search, it's a different paradigm for memory retrieval. Founded by researchers with 160+ publications in Nature and ICLR who closed their Harvard lab to build this.

- **2026-04-10** | [Avid](https://x.com/av1dlive/status/2042172428127002906) | skills-mcp, claude-code
  Recommends a 16-minute talk by two Anthropic engineers who built Claude Skills, paired with a comprehensive guide by @eng_khairallah1 on building Claude Skills that actually work. Notes that most of the 80,000+ skills in the community registry are poorly built — this guide covers what separates the good from the bad.

- **2026-04-09** | [carsonfarmer](https://x.com/carsonfarmer/status/2042038527639068763) | agent-design, claude-code, industry
  Points out that Anthropic's new managed agents API closely mirrors the Letta/MemGPT API that's been open-source for a year — including read-only memory blocks and memory block sharing. Quoting Sarah Wooders (Letta co-creator) who calls it closed-source with provider lock-in.

- **2026-04-09** | [Aakash Gupta](https://x.com/aakashgupta/status/2041984945380585785) | management, agent-design
  Makes the case for "Team OS" — a shared GitHub repo that serves as a team's collective brain for Claude. Companies spending $200K/yr on AI seats see zero productivity gains because each person starts from scratch every conversation with no shared context. Structured context (customer calls, specs, constraints, strategy docs) compounds across the team.

- **2026-04-09** | [Ashpreet Bedi](https://x.com/ashpreetbedi/status/2041966288541507861) | agent-design, dev-practices
  Ashpreet highlights @Vtrivedy10's LangChain article on auto-improving agent harnesses using evals as a hill-climbing signal. The approach formalizes iterative system improvement — build a harness, eval it, improve it automatically. Directly applicable to anyone building agentic workflows who wants systematic quality gains.

- **2026-04-09** | [mr-r0b0t](https://x.com/mr_r0b0t/status/2041930298238087464) | agent-design, dev-practices
  Endorses the same LangChain article by @Vtrivedy10 on harness hill-climbing with evals. Argues that harness evolution combined with specialist local models will be the path forward for agent development.

- **2026-04-09** | [Justin Brooke](https://x.com/imjustinbrooke/status/2041890745167061245) | agent-design, prompting
  Introduces 7 markdown files for structuring AI agent systems: SOULS.md, AGENTS.md, USER.md, TOOLS.md, MEMORY.md, HEARTBEAT.md, STYLE.md. Core thesis is "harnesses > models" — the orchestration layer matters more than which foundation model you use.

- **2026-04-09** | [Vaishnavi](https://x.com/_vmlops/status/2041869776927261024) | dev-practices, skills-mcp, questionable
  Microsoft open-sourced markitdown (github.com/microsoft/markitdown) — a Python tool that converts PDFs, Word docs, Excel, PowerPoint, audio, and YouTube URLs into clean Markdown for LLM pipelines. One pip install replaces custom parsers for file ingestion.

- **2026-04-08** | [Sowmay Jain](https://x.com/sowmay_jain/status/2041982135305957425) | agent-design, research
  Describes using an AI agent (@laukiantonson) to fully analyze a 67GB raw genome file for $5 in compute: rented a 32-core/64GB machine, aligned 21M long reads (99.83% mapped), called 5.8M variants, phased maternal/paternal inheritance, annotated against ClinVar/PharmGKB/gnomAD, produced a health risk map across 39 conditions and drug compatibility guide for 41 medications. Striking real-world demonstration of autonomous agentic capability on complex bioinformatics tasks. Went massively viral (909K views).

- **2026-04-08** | [Ashpreet Bedi](https://x.com/ashpreetbedi/status/2041568919085854847) | agent-design, dev-practices
  Ashpreet Bedi argues that building agentic software requires systems engineering discipline — you can't optimize AI agent systems by optimizing individual components. Draws parallels to Bell Labs' 1940s discovery that telephone network behavior emerged from component interactions, not individual parts. The current wave of 'harness engineering' is repeating 80-year-old mistakes.

- **2026-04-08** | [cvxv666](https://x.com/antpalkin/status/2041517093670052193) | questionable, general
  Engagement-farming thread about building a Polymarket prediction market trading bot with Claude. Claims $300→$2.38M strategy. Quote-tweets @adiix_official's viral guide on debugging Claude-built arbitrage bots. Typical crypto/trading bot hype pattern — treat with skepticism.

- **2026-04-08** | [Ksenia Se](https://x.com/theturingpost/status/2041455210342871094) | management, industry
  Ksenia from TuringPost on the enterprise AI adoption gap: despite SF hype, most companies are still at ChatGPT-for-writing stage. AI adoption isn't a straight line but a stack of dependencies — you can't jump to agents if workflows aren't legible, can't act on data you don't trust. Most AI pilots fail because organizational readiness, not the technology, is the bottleneck.

- **2026-04-07** | [Allie K. Miller](https://x.com/alliekmiller/status/2041577000804991485) | management, agent-design
  Allie K. Miller shares a 5-level 'Proactive AI-First Team Member' framework for hiring and onboarding. Levels range from 1 (not using AI) to 5 (full ownership with AI-augmented critical thinking). Key insight: most candidates interview at level 3 (solution-oriented but not action-oriented) — she wants new hires starting at level 4 (action-oriented with technical/business tradeoff awareness). Originally from @businessbarista and @stephsmithio, with AI additions by Miller.

- **2026-04-06** | [Eric Siu](https://x.com/ericosiu/status/2040785346120859946) | management, agent-design
  Practical guide to deploying Jack Dorsey's 'world intelligence' concept — a company-wide AI knowledge layer that powers 50+ daily workflows, coordinates decisions across teams, and surfaces issues automatically. Includes a linked article with implementation details from 4 months of running this at his company.

- **2026-04-06** | [Dave Kline](https://x.com/dklineii/status/2040776601223246334) | management
  Management advice on fixing broken 1:1 meetings — 4 tests to determine if your 1:1s are actually working. Covers common anti-patterns like cancelling on top performers, using 1:1s as status reports, and doing most of the talking instead of listening.

- **2026-04-06** | [Alex Prompter](https://x.com/alex_prompter/status/2040731938751914065) | research, agent-design
  Google DeepMind published the largest empirical study of AI agent manipulation — 502 participants across 8 countries, 23 attack types tested against GPT-4o, Claude, and Gemini. Found that websites can already detect AI agents and serve them different content, with hidden instructions in HTML, malicious commands in image pixels, and jailbreaks in PDFs. Current defenses fail in predictable, invisible ways.

- **2026-04-06** | [0xMarioNawfal](https://x.com/roundtablespace/status/2040500903296352663) | claude-code, agent-design, skills-mcp
  Comprehensive open-source Claude Code setup with 27 agents, 64 skills, 33 commands, and built-in AgentShield with 1,282 security tests. Handles planning, code review, fixes, TDD, and token optimization. Works across Cursor, OpenCode, and Codex CLI. github.com/affaan-m/everything-claude-code

- **2026-04-05** | [Ejaaz](https://x.com/cryptopunk7213/status/2040434869399138368) | agent-design, claude-code
  Open-sourced self-improving AI agent framework: a meta-agent that autonomously tweaks an agent's harness (tools, system prompts), runs tests, and iterates until it tops benchmarks. Demonstrated on TerminalBench (code) and spreadsheets (financial modeling), reaching #1 in both domains in under 24 hours using Claude evaluating Claude for better failure analysis.

- **2026-04-03** | [Charly Wargnier](https://x.com/datachaz/status/2039963758790156555) | agent-design, dev-practices
  Charly Wargnier breaks down Karpathy's new self-improving 'second brain' setup using Obsidian Markdown wikis. Instead of complex RAG, an LLM auto-compiles raw research into indexed .md files, handles its own linting and Q&A routing, and generates outputs (Marp slides, matplotlib plots) filed back into the wiki. The key insight: agents maintaining their own memory layer don't need massive context windows — just clean file organization and the ability to query their own indexes.

- **2026-04-02** | [Dmitriy Kovalenko](https://x.com/neogoose_btw/status/2039508756988620801) | dev-practices
  Dmitriy Kovalenko demos a blazing-fast, index-free code search tool that works on massive codebases in real time — tested on leaked Claude Code sources, Linux kernel (100k files), and Chromium repo (500k files). Claims it's the most accurate code search approach available.

- **2026-04-02** | [The Curious Tales](https://x.com/thecurioustales/status/2039360822200442914) | general
  Self-help/life advice post recommending an article about being '3 decisions away from a completely different life.' Not AI or tech related — personal development content.

- **2026-04-02** | [Adam](https://x.com/_overment/status/2039061635776618554) | agent-design
  Adam shares his personal AI system architecture based on a dynamic dependency graph with a heartbeat loop involving LLM, code, and events. Describes it as the best architecture he's found for building personal AI systems.

- **2026-04-01** | [Tom Dörr](https://x.com/tom_doerr/status/2039115357839929610) | agent-design, research
  Shares an open-source AI research agent, Feynman (github.com/getcompanion-ai/feynman) — an autonomous research-assistant agent.

- **2026-04-01** | [Arnav Gupta](https://x.com/championswimmer/status/2039109862919905719) | agent-design, skills-mcp
  Arnav Gupta highlights a set of extensions by @nicopreme (pi-subagents, pi-messenger, pi-mcp-adapter, pi-web-access) that together create a powerful agentic system surpassing tools like Ralph, Gstack, and Conductor.

### Mar 2026

- **2026-03-31** | [klöss](https://x.com/kloss_xyz/status/2038842907466334550) | dev-practices
  Critical supply chain attack on axios (100M+ weekly npm downloads). An attacker hijacked a maintainer's credentials and published poisoned versions (1.14.1 and 0.30.4) that inject a fake dependency installing a remote access trojan across macOS, Windows, and Linux. Pin to axios@1.14.0 or 0.30.3 and rotate all secrets on affected machines.

- **2026-03-31** | [ℏεsam](https://x.com/hesamation/status/2038758029940654507) | skills-mcp, prompting
  Ole Lehmann built a Claude skill implementing Karpathy's LLM Council method — 5 AI sub-agents critique your idea from different angles with anonymous peer review. A practical fix for the 'AI yes-man' problem where Claude just tells you what you want to hear.

- **2026-03-31** | [Vox](https://x.com/voxyz_ai/status/2038677643000758466) | agent-design, dev-practices
  Parallel module development pattern using Codex: break a project into 5 independent modules running in separate windows with a 'foreman' conductor writing to a shared doc. Each module reads the shared state, executes its part, and updates when done. Uses Claude for UI work and Codex for the rest.

- **2026-03-30** | [Tom Dörr](https://x.com/tom_doerr/status/2038456589984690462) | agent-design, dev-practices
  Cisco open-sourced DefenseClaw (github.com/cisco-ai-defense/defenseclaw), a tool that scans and blocks dangerous AI agent actions. Designed as a safety layer for autonomous AI workflows.

- **2026-03-30** | [Viv](https://x.com/vtrivedy10/status/2038346865775874285) | agent-design
  Commentary on a writeup by @systematicls about solving problems in long-running autonomous agentic engineering workflows. Key insight: all harness design is about overcoming agent laziness (cutting corners) and confusion. Solutions involve task decomposition, looping, and human-in-the-loop for underspecified tasks.

- **2026-03-30** | [Erick](https://x.com/ericksky/status/2038301058338812119) | dev-practices, general
  Tome — an open-source macOS app that transcribes Zoom/Meet/Teams meetings locally with AI (no cloud), detects speakers, and generates Markdown notes directly into your Obsidian vault. No API keys, no subscriptions, 100% private.

- **2026-03-30** | [Daniel Miessler](https://x.com/danielmiessler/status/2038284628130492870) | agent-design, management
  'Bitter Lesson Engineering' (danielmiessler.com): don't over-engineer your AI harness — lean on scaling/general methods rather than hand-crafted scaffolding, applying Sutton's bitter lesson to agent-harness design.

- **2026-03-29** | [Meta Alchemist](https://x.com/meta_alchemist/status/2038222105654022325) | claude-code, agent-design
  Detailed guide on turning Claude Code into a self-evolving system. The approach captures corrections across sessions so the CLI learns and improves over time, building persistent memory of what works and what doesn't for each project.

- **2026-03-29** | [Tom Dörr](https://x.com/tom_doerr/status/2038137050243711042) | agent-design, dev-practices
  Shares a self-improving agent-swarm framework, Hive (github.com/aden-hive/hive) — orchestration for multiple cooperating agents that improve over time.

- **2026-03-29** | [BuBBliK](https://x.com/k1rallik/status/2037936518862446694) | general
  TurboQuant — Google's algorithm for 3-bit KV cache compression that enables 100K token conversations on a 16GB M2 MacBook with quality identical to cloud APIs. Claims 6x memory compression and 8x speedup with zero accuracy loss. Free paper/algorithm.

- **2026-03-29** | [Suryansh Tiwari](https://x.com/suryanshti777/status/2037892411666645363) | general
  Cheat sheet mapping 21 real agent design patterns — prompt chaining, routing, parallelization, reflection, tool use, planning, multi-agent, memory management, MCP, RAG, guardrails, evaluation, and more. Solid reference doc for anyone building agentic systems.

- **2026-03-29** | [Cheng Lou](https://x.com/_chenglou/status/2037713766205608234) | general
  Cheng Lou (React/ReasonML creator) released a foundational piece of UI engineering: a fast, accurate, comprehensive userland text measurement algorithm in pure TypeScript that can lay out entire web pages without CSS, bypassing DOM measurements and reflow. 21M+ views, huge community response.

- **2026-03-29** | [Shann³](https://x.com/shannholmberg/status/2036461256006357409) | skills-mcp, prompting
  Karpathy's AutoResearch method applied to Claude skills optimization. Ole Lehmann tested it on landing page copy, improving pass rate from 56% to 92% overnight. The method auto-improves any skill on autopilot by running automated evaluations and iterating.

- **2026-03-26** | [Rohit](https://x.com/rohit4verse/status/2036845273117581676) | agent-design, dev-practices
  Rohit argues top AI teams win not on model selection but on 'harness engineering' — how you design the agent's interface, manage context windows, cap search results, run linters at edit time, and maintain persistent state files. A teaser thread for an 8,000-word deep dive covering 8 actionable principles for building more reliable AI agents; key insights include: interface shapes model reasoning, context pollution is costly, and forced query refinement beats flooding with results.

- **2026-03-25** | [Poonam Soni](https://x.com/codebypoonam/status/2036517669684519362) | agent-design, claude-code, questionable
  Teaser thread claiming Anthropic demonstrated a 3-agent system that builds production-quality apps from a single prompt in under 6 hours without human intervention. Architecture details promised in thread. Engagement-farming format ('Breaking') but the underlying multi-agent app-building claim is worth verifying.

- **2026-03-25** | [Greg Pstrucha](https://x.com/grichadev/status/2036472210152718504) | skills-mcp, claude-code, dev-practices
  Greg Pstrucha demonstrates how malicious Claude Code skills can hide instructions inside PNGs and abuse Claude Code's 'expand output' feature to fool both humans and agents — a real security threat. He improved `skill-scanner` (also available via Sentry's Warden at warden.sentry.dev) to catch these attack vectors. Only install skills from trusted sources.

- **2026-03-25** | [Denis Yurchak](https://x.com/denisyurchak/status/2036422883350544519) | dev-practices, claude-code
  Denis Yurchak shares a Claude prompt (.md file) that fully automates secure Hetzner VPS setup in one shot — configures SSH hardening, fail2ban, UFW firewall, and optionally Tailscale. Buy the server, install Claude, paste the prompt. Open source, PRs welcome. Practical Claude-as-sysadmin pattern.

- **2026-03-25** | [Millie Marconi](https://x.com/milliemarconnni/status/2036363493478375797) | claude-code, skills-mcp, prompting, questionable
  A Claude Code skill (/last30days) scans Reddit and X from the past 30 days on any topic and generates copy-paste-ready prompts based on what's actually working in the community right now — not months-old advice. Works for any domain (Midjourney, Cursor rules, legal prompts, etc.). Open source, MIT license.

- **2026-03-24** | [Factory](https://x.com/factoryai/status/2036184745059688923) | agent-design, industry
  Factory launches "Missions" — long-running agentic workflows now available to all users, built to automate large software tasks like app development from scratch, codebases migrations, and AI research. Strong signal that autonomous multi-step coding agents are going mainstream.

- **2026-03-22** | [hoeem](https://x.com/hooeem/status/2035762966952382646) | claude-code, skills-mcp, questionable
  hoeem re-promotes his 'I want to become a Claude Architect (full course)' article covering Claude Code, the Claude Agent SDK, the Claude API, and MCP; framed for engagement ('Be the 1%', 110k+ bookmarks).

- **2026-03-22** | [Kshitij Mishra](https://x.com/daievolutionhub/status/2035396799704547453) | claude-code, dev-practices, questionable
  Kshitij Mishra shares a 'Claude Code Setup Cheatsheet' based on Boris (creator of Claude Code), quoting Shruti Codes' '2026 AI Engineer roadmap' article; 'Save this' engagement framing.

- **2026-03-22** | [Akshay](https://x.com/akshay_pachaar/status/2035341800739877091) | claude-code, skills-mcp, dev-practices
  Akshay Pachaar's guide 'Anatomy of the .claude/ folder' walks through CLAUDE.md, custom commands, skills, agents, and permissions and how to set them up properly, framing .claude as the control center for how Claude behaves in a project (instructions, commands, permission rules, and cross-session memory).

- **2026-03-22** | [George from prodmgmt](https://x.com/nurijanian/status/2035257434365976671) | skills-mcp, prompting, agent-design
  George (prodmgmt.world) recounts improving his AI skills with Karpathy's Auto Research library (auto-improves prompts via repeated experimentation), using Ole Lehmann's fork turned into a skill that tunes other skills: define test inputs, write judges that score outputs, let the optimization loop run, and wake up to a better skill.

- **2026-03-22** | [Matt Stockton](https://x.com/mstockton/status/2035179208872202320) | agent-design, dev-practices, management
  Matt Stockton argues building AI-enabled products inverts classical software engineering: the 'right way to build' changes every ~3 months, it is often better to burn the system down and rebuild than to adapt, and modern tools make that cheap — warning against sunk-cost V1 RAG systems that stuff a static context window.

- **2026-03-22** | [sarah guo](https://x.com/saranormous/status/2035080458304987603) | industry, research, agent-design
  Sarah Guo's No Priors podcast episode with Andrej Karpathy covers the phase shift in engineering, AI psychosis, AutoResearch, model speciation, jobs-market data, open vs closed models, autonomous robotics, and agentic education.

- **2026-03-21** | [felpix](https://x.com/felpix_/status/2033249213614538804) | agent-design, claude-code, industry
  felpix reports filing taxes end-to-end with Claude + FreeTaxUSA: dropped a W-2, several 1099-NECs and 1099-Bs plus expense/budget spreadsheets in a folder, asked Claude to itemize and optimize expenses, and let it use Chrome to submit — the return was accepted. (Directly relevant: FreeTaxUSA is TaxHawk's own product.)

- **2026-03-20** | [Corey Ganim](https://x.com/coreyganim/status/2034717504505823728) | agent-design, skills-mcp, claude-code, questionable
  Corey Ganim's playbook for running a one-person 'AI company' stacks three free tools: Paperclip (npx paperclipai — assigns work and tracks progress), gstack (15 specialist Claude Code skills from Garry Tan, with /office-hours, /review, /qa, /ship commands), and autoresearch (Karpathy — 100 overnight experiments); the move is running 10-15 gstack commands in parallel. Quotes Nick Spisak's Paperclip follow-up article.

- **2026-03-18** | [Ole Lehmann](https://x.com/itsolelehmann/status/2033982679423848802) | skills-mcp, prompting, claude-code
  Ole Lehmann shares a single skill that auto-improves any other skill using Karpathy's autoresearch method: it runs the skill and scores the output, finds what's failing, makes one small change to the skill prompt, re-runs to check the score, keeps or reverts the change, and repeats until the skill works. Article: 'How to 10x your Claude Skills'.

- **2026-03-18** | [unusual_whales](https://x.com/unusual_whales/status/2033965177918620008) | skills-mcp, industry, questionable
  Unusual Whales launched an MCP server that streams live, structured market data to any AI on demand — options flow, dark pools, congressional trades, full financials, technicals, 13Fs, insider activity, and Polymarket data — for building trading bots, dashboards, and screeners (unusualwhales.com/public-api/mcp). 'BREAKING' engagement framing.

- **2026-03-18** | [Thariq](https://x.com/trq212/status/2033949937936085378) | skills-mcp, claude-code, dev-practices
  Thariq (Anthropic) shares 'Lessons from Building Claude Code: How We Use Skills' — which skills are worth making, the secret to writing a good one, and when to share them — noting Anthropic runs hundreds of skills internally and that the common 'skills are just markdown files' misconception undersells them.

- **2026-03-18** | [Rohit](https://x.com/rohit4verse/status/2033945654377283643) | agent-design, dev-practices, claude-code
  Rohit's essay 'The Harness Is Everything: What Cursor, Claude Code, and Perplexity Actually Built' argues you're not using AI wrong because of the model — you're using it wrong because you haven't built the right environment; the difference between teams shipping millions of lines and those struggling is the harness, not GPT-5 vs Claude Opus, temperature, or the prompt.

- **2026-03-18** | [zostaff](https://x.com/zostaff/status/2033930728044372275) | agent-design, industry, questionable
  zostaff's clickbait-titled ('How to Quit Your Job in One Day') walkthrough of an autonomous Polymarket trading system built from three agents: Claude (strategist — probability/recommendation/confidence), Codex (engineer — writes and debugs bot code), and OpenClaw (orchestrator — persistent memory, cron, modular skills, Telegram interface that executes trades and logs everything).

- **2026-03-17** | [Akhilesh Mishra](https://x.com/livingdevops/status/2033845127244825041) | dev-practices, agent-design, skills-mcp, industry
  Akhilesh Mishra reports NVIDIA open-sourced OpenShell at GTC — an infrastructure-layer sandbox/guardrail for coding agents: filesystem locked at sandbox creation, network blocked by default with whitelisting, API keys injected only at runtime (never on disk), policies in simple YAML, running a full K3s cluster inside a single Docker container. One command sandboxes Claude Code, Codex, or Cursor; Adobe, Atlassian, Cisco, CrowdStrike, and Salesforce are integrating it.

- **2026-03-17** | [Avi Chawla](https://x.com/_avichawla/status/2033797863948632384) | research, agent-design, skills-mcp
  Avi Chawla explains the SKILLRL paper: rather than stuffing long, noisy raw trajectories into agent memory, it distills experiences into compact, reusable skills the agent retrieves and applies to future tasks — analogous to how humans turn driving experience into transferable instincts.

- **2026-03-16** | [0xMarioNawfal](https://x.com/roundtablespace/status/2033238044900298844) | claude-code, skills-mcp, questionable
  0xMarioNawfal amplifies Corey Ganim's article 'Ultimate Claude Cowork Starter Pack: Every Plugin, Skill, and Workflow You Need,' which argues most people install Claude Cowork, poke around for 10 minutes, and revert to ChatGPT because the setup is the hard part.

- **2026-03-16** | [Beacon](https://x.com/0xxbeacon/status/2033224402070810940) | claude-code, management
  Beacon links Anthropic's Skilljar course catalog (anthropic.skilljar.com) and the access-request page for the Claude Certified Architect: Foundations certification.

- **2026-03-16** | [Josh Kale](https://x.com/joshkale/status/2033183463759626261) | industry, research
  Karpathy scored every job in America on AI replacement risk, then deleted it. Josh cloned the repo before it went down — 342 occupations scored 0-10 on AI exposure. Average across US economy: 5.3/10. Community note: Karpathy called it a casual 2-hour 'vibe code experiment' and deleted because it was 'wildly misinterpreted.'

- **2026-03-16** | [hoeem](https://x.com/hooeem/status/2033146416428708168) | questionable, general
  A low-substance reaction post ('hoeem style takeover kek') quoting another post that now comes from a suspended account; little usable content beyond the meta-commentary.

- **2026-03-15** | [Huaxiu Yao](https://x.com/huaxiuyaoml/status/2033038170653405308) | research, agent-design
  Huaxiu Yao announces AutoResearchClaw, which automates the full research loop beyond Karpathy's autoresearch experiment loop: one message in, a full conference paper out with real experiments, verified citations, and code. It mines arXiv and Semantic Scholar (50+ papers), has three agents fight over the best hypothesis, writes and self-debugs experiment code, and pivots when results are weak — no human in the loop.

- **2026-03-13** | [kpaxs](https://x.com/kpaxs/status/2032345995095179680) | research
  [Login wall — content not extracted. Custom subject suggests a mental model or heuristic worth revisiting.]

- **2026-03-13** | [Garry Tan](https://x.com/garrytan/status/2032196172430131498) | claude-code, skills-mcp, dev-practices, agent-design
  Garry Tan shares a CTO's testimonial that his open-source gstack ('god mode') flagged a subtle cross-site-scripting vulnerability the team wasn't aware of, predicting 90%+ of new repos will adopt it. gstack is MIT-licensed at github.com/garrytan/gstack and installs into local Claude Code and into a repo for teammates with two pastes.

- **2026-03-12** | [elvis](https://x.com/omarsar0/status/2031727864199208972) | agent-design, skills-mcp, research
  elvis highlights EvoSkill, a self-evolving multi-agent framework that automatically discovers and refines agent skills through iterative failure analysis. Three agents (Executor, Proposer, Skill-Builder) drive the loop, with a Pareto frontier retaining only skills that improve held-out validation while the base model stays frozen. Reported gains: Claude Code w/ Opus 4.5 from 60.6%->67.9% on OfficeQA, +12.1% on SealQA, and +5.3% zero-shot transfer to BrowseComp.

- **2026-03-11** | [Viv](https://x.com/vtrivedy10/status/2031411814232187109) | agent-design, dev-practices
  Viv (LangChain applied research) shares a LangChain blog taking a first-principles look at why agent harnesses exist and how they help craft good product experiences and correct model failure modes. It covers filesystems, code execution, sandboxes, context rot, and ralph loops, arguing the best harness for your model probably isn't the one it shipped with.

- **2026-03-11** | [Ming "Tommy" Tang](https://x.com/tangming2005/status/2031358195558658266) | claude-code, dev-practices, prompting
  Tommy Tang's single biggest CLAUDE.md improvement: when a bug is reported, don't start by fixing it. Start by writing a test that reproduces the bug, then have subagents try to fix it and prove the fix with a passing test.

- **2026-03-11** | [kapilansh](https://x.com/kapilansh_twt/status/2031262184442130863) | research, prompting
  kapilansh argues most devs learning AI only know how to call an API and write a prompt without understanding what happens inside, and recommends Karpathy's 'Neural Networks: Zero to Hero' playlist (micrograd, makemore, attention from scratch, tokenization, training GPT-2) as the genuine fix for that knowledge gap.

- **2026-03-10** | [Dominik Tornow](https://x.com/dominiktornow/status/2031233587819983096) | agent-design, dev-practices
  Dominik Tornow: the new core skill in software engineering is designing feedback loops. He quotes OpenAI Developers on a small team steering Codex to open and merge 1,500 pull requests for a product used by hundreds of internal users, with zero manual coding.

- **2026-03-10** | [Suhail Gupta](https://x.com/audiinidesign/status/2031213732941230240) | industry, management, agent-design
  Suhail Gupta endorses Harrison Chase's article 'How Coding Agents Are Reshaping Engineering, Product and Design,' agreeing the EPD blur toward functional software over separate roles will only become more visible and obvious in the coming months.

- **2026-03-10** | [Boris Cherny](https://x.com/bcherny/status/2031089411820228645) | claude-code, dev-practices, agent-design
  Boris Cherny announces Code Review in Claude Code: when a PR opens, a team of agents runs a deep review to hunt for bugs. Built internally first because code output per Anthropic engineer is up 200% this year and review had become the bottleneck; he says it catches many real bugs he'd otherwise miss.

- **2026-03-08** | [0xSero](https://x.com/0xsero/status/2030653670375751942) | agent-design, dev-practices
  0xSero shares advice from Factory's Leo: take screenshots and videos of everything you've built, then review it. Combined with automated QA, this yields a semi-autonomous build/verify system. Links a podcast episode.

- **2026-03-08** | [Daniel Miessler](https://x.com/danielmiessler/status/2030436867745923347) | research, agent-design
  Daniel Miessler flags Karpathy's new self-contained 'autoresearch' repo (nanochat training core stripped to a single-GPU, ~630-line file the human iterates on) as under-appreciated, tying it to the long-discussed goal of automating ML research and predicting it will accelerate progress again.

- **2026-03-08** | [Alex Prompter](https://x.com/godofprompt/status/2030434641019072867) | agent-design, skills-mcp
  Alex Prompter (co-founder @godofprompt) shares affaan-m/ECC on GitHub, described as an agent-harness performance-optimization system built around skills and instincts.

- **2026-03-08** | [GitHub Projects Community](https://x.com/githubprojects/status/2030346933009821801) | agent-design, dev-practices
  GitHub Projects Community: rather than using AI to generate code directly, let it run a structured build loop — idea -> roadmap -> small tasks -> execute each task in isolation -> commit — for cleaner repos, clearer progress, and far less AI chaos.

- **2026-03-07** | [Anish Moonka](https://x.com/anisha_moonka/status/2030015356383691121) | management, claude-code, industry
  Anish Moonka's 12-point notes from Boris Cherny (Head of Claude Code) on Lenny's Podcast: coding is largely solved (Boris ships 10-30 PRs/day, no hand-written code since Nov 2025); the next frontier is AI deciding what to build; productivity per Anthropic engineer is up 200%; underfund teams on purpose; give engineers unlimited tokens; the Bitter Lesson favors general models over rigid orchestration; build for the model six months out; latent demand is the best product signal; 'software engineer' is becoming 'builder'; mechanistic interpretability enables layered safety; and 70% of engineers/PMs enjoy their jobs more now.

- **2026-03-07** | [Numman Ali](https://x.com/nummanali/status/2030012892192309461) | dev-practices, research, prompting
  Numman Ali strongly recommends a deeply technical article, 'Your LLM Doesn't Write Correct Code. It Writes Plausible Code,' praising its articulation of the plausible-vs-correct distinction in LLM output — illustrated by a 100-row primary-key lookup where SQLite takes 0.09ms but an LLM-generated Rust rewrite takes 1,815.43ms.

- **2026-03-07** | [staysaasy](https://x.com/staysaasy/status/2029965845548462281) | management
  staysaasy long-form article 'Avoiding a Culture of Emergencies': the best managers have far fewer preventable emergencies because they know how hard things actually are, know what's important and can say no, hold a strong mental model of their team and company to forecast needs, and genuinely care. Emergencies are largely a management choice, and avoiding them is one of the best talent-retention mechanisms.

- **2026-03-07** | [Jamie Quint](https://x.com/jamiequint/status/2029951631534739951) | agent-design, management, industry
  Jamie Quint (built Notion's early data stack in 2020) shares his article 'How to Build a Data Agent in 2026,' claiming the approach can cut a company's projected data-team headcount by ~80% this year.

- **2026-03-07** | [Nate.Google](https://x.com/nate_google_/status/2029941042133262721) | claude-code
  Nate.Google highlights a walkthrough he calls the best guide to Claude Cowork, wishing such hands-on guides existed when he started with AI.

- **2026-03-06** | [Alex Prompter](https://x.com/alex_prompter/status/2029961559615607052) | agent-design, prompting, dev-practices
  Citing a GitHub analysis of 2,500+ repos, argues most agents.md files fail by being too vague. Top performers give each agent ONE narrow job (docs writer, test engineer, lint fixer) with specific examples — specialists beat generalists.

- **2026-03-06** | [Jayden](https://x.com/thejayden/status/2029899328400109732) | agent-design, claude-code
  Jayden recommends an article on building a "Chief of Staff" with Claude Code, calling it one of the best real-world examples of agentic systems he has seen.

- **2026-03-06** | [Alexey Grigorev](https://x.com/al_grigor/status/2029829363903123636) | dev-practices, agent-design, management
  Argues prompting is only ~5% of AI engineering; the other 95% is making AI testable, observable, versioned and reliable in production. Core skills: evaluation/testing with golden eval sets and regression tests, plus controlled iteration via prompt versioning and experiment tracking (Git/MLflow).

- **2026-03-06** | [Philipp Schmid](https://x.com/_philschmid/status/2029570052530360719) | skills-mcp, dev-practices, prompting
  Practical guide to evaluating agent Skills, which are often AI-generated and untested: define success criteria (outcome/style/efficiency), build 10-12 prompts with deterministic checks, add an LLM-as-judge for qualitative checks, and iterate on the skill from eval failures.

- **2026-03-05** | [Akshay](https://x.com/akshay_pachaar/status/2029534926828388537) | skills-mcp, agent-design
  Explains the difference between MCP and Skills for AI agents — commonly conflated. MCP is a shared communication standard that replaces the N-models-by-M-tools custom-connector explosion, whereas Skills are a distinct concept.

- **2026-03-05** | [Meta Alchemist](https://x.com/meta_alchemist/status/2029430826128293906) | agent-design, skills-mcp, questionable
  Roundup of 10 open-source AI memory layers (free, popular on GitHub, some YC-funded) to give coding agents like Claude and Codex better recall than plain memory.md files, with notes on what each is good at and how to combine them. Engagement-styled listicle but substantive.

- **2026-03-05** | [John Rush](https://x.com/johnrushx/status/2029406051716743354) | industry, management
  Opinion piece: AI does not make work easier — it strips away the easy 99% of jobs so everyone now competes on the hard 1%, raising cognitive load and stress sharply. A take on how AI reshapes knowledge work.

- **2026-03-05** | [Sukh Sroay](https://x.com/sukh_saroy/status/2029400474739458379) | questionable, skills-mcp, agent-design, dev-practices
  [Post unavailable — account suspended]

- **2026-03-05** | [Daniel San](https://x.com/dani_avila7/status/2029399100240674929) | skills-mcp, claude-code
  Points to a full Skill in the Anthropic repo as a reference for SKILL.md structure and language support, arguing every company should maintain an internal repository of reusable Skills and components.

- **2026-03-05** | [0xSero](https://x.com/0xsero/status/2029305128084218265) | industry, agent-design
  Argues real-time, very fast inference (e.g. models served by Cerebras, used via "Spark") is a major shift that requires changing your working strategy, pointing to companion articles for details.

- **2026-03-05** | [yenkel](https://x.com/yenkel/status/2029299384832209259) | management, dev-practices
  Crisp engineering-leadership advice for the AI era: fewer handoffs and faster decisions, more exploration, willingness to throw away code/tokens, learning by building, and picking leads who can own design, engineering and product together.

- **2026-03-05** | [Tech Layoff Tracker](https://x.com/techlayofflover/status/2029261882834501665) | industry, management, questionable
  Shares a venting DM from a senior Big Tech SWE (~$350k TC): leadership now touts an "AI leverage ratio" of 4.2x — each engineer shipping the output of a former four-person team — fueling job anxiety. Engagement-styled but a real signal on AI-driven productivity expectations and layoffs.

- **2026-03-05** | [Dickson Tsai](https://x.com/dickson_tsai/status/2029235808235078095) | claude-code, skills-mcp
  Dickson Tsai (Anthropic) announced HTTP hooks in Claude Code — a more secure, easier alternative to command hooks: CC POSTs each hook event to a URL you choose and awaits a response, so you can build a web app to view progress, manage permissions, run hook logic server-side, and manage state across agents via a DB. Works everywhere hooks are supported, including plugins, custom agents, and enterprise managed settings. Docs: code.claude.com/docs/en/hooks

- **2026-03-05** | [Peter Yang](https://x.com/petergyang/status/2029220235375714766) | management, agent-design, industry
  Deep dive arguing your new job is to onboard and manage AI agents, with examples from Linear (AI team members you assign tasks to), Ramp (Claude Code as baseline for all roles), and Factory (codifying PM, frontend, and data-analysis work into reusable skills).

- **2026-03-05** | [swarit](https://x.com/swaritjoshipura/status/2029219363749020051) | agent-design, research, industry
  Curated links on agent context and evaluation: Foundation Capital on "context graphs" as AIs trillion-dollar opportunity (foundationcapital.com/context-graphs-ais-trillion-dollar-opportunity/), Anthropics guide to demystifying evals for AI agents (anthropic.com/engineering/demystifying-evals-for-ai-agents), a YouTube talk, and resolve.ai.

- **2026-03-05** | [hoeem](https://x.com/hooeem/status/2029167629076676955) | general, research
  A free, beginner-to-expert ranked list of AI learning resources: Anthropic Academy (Claude 101 & AI Fluency), Google AI Essentials, AWS Generative AI Essentials, Elements of AI (University of Helsinki), DeepLearning.AI short courses, and Harvard CS50s Intro to AI with Python.

- **2026-03-05** | [Bojan Tunguz](https://x.com/tunguz/status/2029164042028236942) | management, general
  Reflects on "mid season" knowledge — many roles require grappling with a problem mid-stream without enough runway to catch up on missing context, something even smart people underestimate.

- **2026-03-05** | [witcheer ☯︎](https://x.com/witcheer/status/2029013946701381978) | agent-design, skills-mcp
  [Post unavailable — page doesn’t exist (same status as nummanali)]

- **2026-03-05** | [Numman Ali](https://x.com/nummanali/status/2029013946701381978) | agent-design
  [Post unavailable — page doesn’t exist]

- **2026-03-05** | [Dan Robinson](https://x.com/danlovesproofs/status/2028890694837039202) | management, dev-practices, agent-design, industry
  Argues issue tracking/backlogs are dying: forward-thinking AI-augmented teams skip Linear/tickets entirely because the cost to fix an issue now approaches the cost to understand it. Works for small, flat, high-context teams with strong dev infra; framed as part of the 'death of midwit software engineering.'

- **2026-03-05** | [Avid](https://x.com/av1dlive/status/2027429188471558475) | questionable, management, agent-design
  Engagement-style 'AI will take your job' listicle, but with a usable career playbook: audit which tasks AI can replicate, learn local agent tooling and stackable 'skills', layer AI-native competence (prompting, orchestration, RAG, automation), shift from executor to system designer, double down on human edge, and build a product/brand.

- **2026-03-05** | [Dickson Tsai]([not found]) | general
  [Superseded — re-keyed to canonical post 2029235808235078095]

- **2026-03-05** | [Muratcan Koylan](https://x.com/koylanai/status/2032671843) | agent-design
  [Post unavailable — corrupt status id resolves to unrelated @BizBlogger account]

- **2026-03-04** | [Atharva](https://x.com/atharvaxdevs/status/2028903519802232991) | agent-design, questionable
  A teaser post aimed at engineers chasing the top 0.01% of "agentic engineering" skill (thread/resource hook).

- **2026-03-04** | [Nate.Google](https://x.com/nate_google_/status/2028836031932355067) | claude-code
  Nate.Google recommends what he calls the most valuable channel for learning everything about Claude.

- **2026-03-03** | [Aarno](https://x.com/theglobalminima/status/2028432457784340950) | research, agent-design
  Suggests software engineers working on agentic AI should study reinforcement learning. As coding agents make custom harnesses/tools easy, the real challenges are behavior control, consistency, memory, and correction — areas where traditional RL on 'agents' intersects fruitfully with LLM agents.

- **2026-03-02** | [Nate Kohari](https://x.com/nkohari/status/2028525461689176325) | dev-practices
  [Post unavailable — page doesn't exist]

- **2026-03-02** | [klöss](https://x.com/kloss_xyz/status/2028237936848994369) | claude-code, skills-mcp, questionable
  Flags Anthropic's free AI academy — 13 courses with official certificates covering MCP, APIs, Claude Code, and AI fluency, at anthropic.skilljar.com. Hype framing ('stop what you're doing') but a genuinely useful free resource.

- **2026-03-02** | [David Byttow](https://x.com/davidbyttow/status/2028233578329600449) | management, agent-design, industry
  Essay arguing AI agents are collapsing the coordination layer of organizations. As execution and coordination costs approach zero, the remaining scarce skill is goal clarity, taste, and ownership. Warns bad judgment now scales faster — strategic mistakes show up as fast delivery of the wrong thing.

- **2026-03-02** | [tetsuo](https://x.com/tetsuoai/status/2028068322106097773) | research, agent-design, dev-practices, prompting
  Technical breakdown of recurring agentic failure modes in fast/distilled code models: wrong direct-exec vs shell selection, structured-output (JSON-only) non-compliance, and tool-result grounding failures (reporting success after a tool error). Fix: distill full agent trajectories (request→tool→output→grounded response), add contrastive near-miss examples, and gate on concrete agentic evals.

- **2026-03-02** | [Nyk](https://x.com/nyk_builderz/status/2028022503319203926) | agent-design, dev-practices, skills-mcp
  Announces open-sourcing Mission Control, a self-hosted AI agent orchestration dashboard: 26 panels, real-time WebSocket+SSE, SQLite (no external services), kanban board, cost tracking, role-based access, quality gates, multi-gateway support. Repo: github.com/builderz-labs/mission-control.

- **2026-03-02** | [Sandhya](https://x.com/agenticgirl/status/2028006725538967614) | research, dev-practices, questionable, industry
  'BREAKING'-style but substantive thread on LMCache, an open-source KV-cache layer (6.9K stars, used by Google Cloud, CoreWeave, NVIDIA) that makes the LLM KV cache persistent and shareable across engine instances, tiered GPU→DRAM→disk→S3. Enables instant RAG, disaggregated prefill, and context sharing; integrates with vLLM and SGLang. Apache-2.0, pip install lmcache.

- **2026-03-02** | [vixhaℓ](https://x.com/thevixhal/status/2027763453679841311) | dev-practices, general
  Promotes a popular step-by-step article on building a 16-bit CPU from scratch in C (4,000+ bookmarks). A from-scratch systems/architecture learning project rather than AI content.

- **2026-03-01** | [AVB](https://x.com/neural_avb/status/2027957534159835443) | agent-design, research
  [Post unavailable — page doesn't exist]

- **2026-03-01** | [Joseph Thacker](https://x.com/rez0__/status/2027448137133264955) | agent-design, claude-code, dev-practices, skills-mcp
  Argues bug bounty / security research changed step-function fast in late 2025: coding agents went from not working to genuinely working. Example: pointed Claude Code at a target's scope (enumerate subdomains, analyze JS bundles, fuzz, test IDORs/GraphQL, write an HTML report); it ran ~30 min, self-recovered from auth/WAF errors, and returned two confirmed vulns. Hunters now build and share custom Claude Code skill libraries (JS static analysis, authenticated fuzzing, IDOR, GraphQL introspection). Quote-tweets Karpathy's parallel observation about programming.

### Feb 2026

- **2026-02-28** | [Thariq](https://x.com/trq212/status/2027463795355095314) | claude-code, agent-design, skills-mcp, prompting
  Anthropic's Thariq on building Claude Code: designing an agent's action space is an art. Walks through the AskUserQuestion tool's evolution (ExitPlanTool param → output-format parsing → dedicated tool), the shift from TodoWrite to the Task tool as models improved, replacing RAG with a Grep search tool so Claude builds its own context, progressive disclosure via Skills, and the Claude Code Guide subagent. Lesson: revisit tool assumptions as capabilities grow; experiment, read outputs, 'see like an agent.'

- **2026-02-27** | [Sudo su](https://x.com/sudoingx/status/2027264446989848613) | prompting, agent-design, claude-code, dev-practices, research
  Practical steering tips for local coding agents: tell the model its own architecture/constraints (e.g. Qwen3.5 fires 8 of 256 experts/token), give project structure over single prompts, iterate in layers (scaffold → refine → polish), let it debug its own failures, and use long context (262K) to hold the whole project. Notes Claude Code as a solid harness and that llama.cpp merged native Anthropic endpoints (no proxy/LiteLLM). Argues the skill gap in local inference is now the harness and steering, not the models — all on a single RTX 3090.

- **2026-02-27** | [SightBringer](https://x.com/_the_prophet__/status/2027235489930191056) | claude-code, industry, management, agent-design
  Critique of AI auto-memory (quote-tweeting Anthropic's Claude auto-memory announcement) as a "power grab disguised as convenience": capturing your patterns, defaults, and definitions of 'good' shifts the model from serving you to shaping you, and dependency is the business model. Counter-playbook: treat memory as a controlled instrument — scope it like permissions, separate persona from operations, keep a purge cycle, audit what the model believes about you, and never let it silently rewrite your intent. Frames the AI era as shifting from intelligence to custody of context/continuity.

- **2026-02-27** | [Brian Roemmele](https://x.com/BrianRoemmele/status/2027169646485729698) | research, industry
  [Post unavailable — page doesn't exist]

- **2026-02-27** | [Kirk Borne](https://x.com/KirkDBorne/status/2027031353849852309) | agent-design
  [Post unavailable — page doesn't exist]

- **2026-02-27** | [George from prodmgmt.world](https://x.com/nurijanian/status/2027020091418890613) | management, dev-practices
  George argues elite PMs escalate documentation with validation rather than starting with a 10-page PRD: 1-pagers are decision docs (write ~10, ~3 get approved), 3-pagers validate and align, and 5-pagers add execution detail only for ideas that survived two rounds. Documentation should match your confidence level, not your anxiety level.

- **2026-02-27** | [Avi Chawla](https://x.com/_avichawla/status/2026907616337883612) | agent-design, dev-practices, skills-mcp
  Avi Chawla revives Norm Hardy's 1988 'confused deputy problem' as the defining security issue for autonomous agents that hold real credentials but can't judge intent. He points to Teleport's open-source Agentic Identity Framework, which gives each agent a unique cryptographic identity, evaluates access in real time, auto-discovers shadow agents and unmanaged MCP servers, and keeps full audit trails.

- **2026-02-27** | [Fernando](https://x.com/franc0fernand0/status/2026701684106313791) | management, research, dev-practices
  Fernando summarizes a Microsoft study (Kalliamvakou et al., TSE 2018) on what makes a great manager of software engineers: technical skill is required but not sufficient; what distinguished great managers was availability, granting autonomy, supporting experimentation, and setting clear ways of working.

- **2026-02-27** | [Machina](https://x.com/exm7777/status/2026666140987175221) | questionable, skills-mcp, claude-code, prompting
  Engagement-farming post ('the ONLY skill you will ever need for Claude, Codex or Openclaw', 'this skill will change your life') quote-tweeting the author's own X article. Behind the hype the underlying topic is a meta-skill/prompting framework meant to change how AI reasons for you; content quality behind the clickbait is unverified.

- **2026-02-27** | [Sukh Sroay](https://x.com/sukh_saroy/status/2026624254800965848) | questionable, research, agent-design
  [Post unavailable — account suspended]

- **2026-02-25** | [Atlas Forge](https://x.com/atlasforgeai/status/2026380335249002843) | agent-design, prompting, dev-practices
  Long-form piece on nine 'meta-learning loops' that let an agent improve across sessions, not just within one: failure-to-guardrail pipelines, tiered memory with trust scoring and decay, prediction-outcome calibration, nightly extraction, friction detection, expiring context holds, plus cognitive loops (epistemic tagging, creative-mode directives, recursive self-improvement). Start with a regressions list; the key is closing the loops so learning compounds.

- **2026-02-25** | [Aakash Gupta](https://x.com/aakashgupta/status/2026367615602667784) | agent-design, skills-mcp, industry, claude-code
  Aakash Gupta, building on a Karpathy quote, argues agents are the new distribution channel for software: they call CLIs and MCP servers and read docs programmatically rather than browsing marketing sites. MCP hit 97M monthly SDK downloads and 10k+ servers in a year and was donated to the Linux Foundation. Winners of the next 24 months build agent-accessible surface area (CLIs, MCP endpoints, machine-readable docs) now.

- **2026-02-25** | [Rohit](https://x.com/rohit4verse/status/2026359771427991764) | agent-design, dev-practices
  Rohit's 10-step checklist for taking agentic AI from demo to production (40%+ of projects fail on architecture, not models): threat-model boundaries, strict input/output contracts, RBAC + sandboxing, layered/compact context, governed grounding, planning/orchestration as control flow, memory in the architecture, native retry/error handling, full observability, and governance with safety gates and drift detection.

- **2026-02-25** | [Matt Pocock](https://x.com/mattpocockuk/status/2026296080602673316) | management, dev-practices, claude-code
  Matt Pocock observes that AI coding rewards a 'lead dev' mentality: developers who spent their careers leveling up teammates through API design, feedback loops, and architecture find working with AI natural, while those who optimized only their own output find it uncomfortable.

- **2026-02-23** | [Dr Milan Milanović](https://x.com/milan_milanovic/status/2025835518207127968) | dev-practices, agent-design, claude-code
  Milan Milanović makes the case for git worktree (shipped in Git 2.5, July 2015): check out multiple branches into separate directories that share one .git, avoiding stashing and duplicate clones. The standout modern use case is AI agents - give each of 3-5 parallel Claude Code/Cursor/Codex agents its own isolated worktree and branch so they don't overwrite each other.

- **2026-02-23** | [Ejaaz](https://x.com/cryptopunk7213/status/2025761121328582814) | industry, research, questionable
  Ejaaz's weekly AI recap: Google shipped Gemini 3.1 (underwhelming to critics) but followed with Lyria 3 song generation and Pomelli one-shot product photoshoots; Microsoft demoed data storage on glass (~10,000-year retention, cheaper than silica); and Taalus fused an AI model directly into silicon at ~17,000 tokens/sec (~17x faster than typical inference).

- **2026-02-23** | [Jeremy Daly](https://x.com/jeremy_daly/status/2025677417398821351) | agent-design, dev-practices
  Jeremy Daly wrote a 100+ page guide on building multi-tenant, commercial AI agent systems from ~18 months running them inside a large SaaS platform serving hundreds of enterprise customers. Covers hard requirements around tenant isolation, auditability, retention, and cost control, plus orchestration models, retrieval architectures, and evaluation harnesses.

- **2026-02-21** | [Akshay 🚀](https://x.com/akshay_pachaar/status/2025767534159835443) | agent-design, skills-mcp
  [Post unavailable - page doesn't exist]

- **2026-02-21** | [tuna](https://x.com/tunahorse21/status/2024974148259512677) | dev-practices, agent-design, skills-mcp
  tuna signal-boosts Alex Fazio introducing Plankton, a 'slop guard' for LLM coding agents. It aims to break the loop of copy-pasting pre-commit/linting errors back into the agent by enforcing lint rules the model can't cheat around.

- **2026-02-20** | [Charly Wargnier](https://x.com/datachaz/status/2024803152730423685) | claude-code, prompting, agent-design, dev-practices
  Charly Wargnier argues writing crystal-clear instructions for machines is the new 10x dev skill, and the most important file in a repo is now CLAUDE.md rather than the code. Top devs use it as an AI onboarding doc to define agent behavior: force the AI to verify its own work, auto-fix CI bugs, and reject hacky fixes.

- **2026-02-20** | [Adam](https://x.com/adamdotdev/status/2024525246993506346) | agent-design, dev-practices
  Adam (working on OpenCode since early 2025) offers an honest, ambivalent reflection on agentic programming: the models are an incredible tool and a real productivity boost, but the shift is confusing and emotionally mixed. He misses the flow of banging out mundane code by hand and notes the growing distance between the developer and the code.

- **2026-02-19** | [Aman](https://x.com/amank1412/status/2023754885473394918) | claude-code, prompting, dev-practices
  Aman shares Garry Tan's (CEO of Y Combinator) CLAUDE.md prompt for Claude Code, which he uses to ship 4,000+ line features with full tests in about an hour. The prompt makes Claude act like a senior engineer: judge whether a plan is over/under-engineered before coding, do a structured review (architecture -> code quality -> tests -> performance), present tradeoffs with opinionated recommendations, and pause for feedback before implementing.

- **2026-02-19** | [J.B.](https://x.com/vibemarketer_/status/2019435524532904205) | prompting, skills-mcp, claude-code, questionable
  J.B. (VibeMarketer) describes a 'recursive self-improvement loop' skill for Claude: instead of prompting once and shipping, the skill generates output, scores it against explicit criteria, diagnoses weaknesses, rewrites, and re-scores until it clears the bar. Cites @maxwellfinn's image-ad skill that grades concepts on 10 criteria (thumb-stop power, curiosity gap, emotional trigger, persona recognition) and won't stop below 9/10.

- **2026-02-18** | [Viv](https://x.com/Vtrivedy10/status/2029576534159835443) | agent-design
  [Post unavailable - page doesn't exist]

- **2026-02-18** | [Tech with Mak](https://x.com/technmak/status/2023990222027915746) | agent-design, claude-code, questionable
  Tech with Mak boosts Matthew Berman's 'OpenClaw masterclass' video, in which Berman claims to have spent 2.54 billion tokens perfecting the OpenClaw coding agent and walks through 21 daily use cases (markdown files, memory system, CRM, and more). Quoted post had ~1.3M views.

- **2026-02-18** | [Matt Dancho (Business Science)](https://x.com/mdancho84/status/2023738764841894352) | skills-mcp, claude-code, dev-practices, questionable
  Matt Dancho argues that becoming a '10X engineer' now comes down to a well-crafted SKILLS.md file, teasing a thread/resource on how to build one. High-engagement post (~1.1M views) with a lead-gen hook.

- **2026-02-17** | [Dr Milan Milanovic](https://x.com/milan_milanovic/status/2023381859489767772) | management, dev-practices, industry
  Milan Milanovic's thesis: AI won't replace developers so much as the software-development process we're used to. Code is becoming cheap while decisions become expensive; AI reduces typing, not thinking. Developers who only implement tasks will struggle, while those who understand the product, domain, and system architecture will thrive.

- **2026-02-15** | [Pavol Lupták](https://x.com/wilderko/status/2025159534159835443) | claude-code, skills-mcp
  [Post unavailable - page doesn't exist]

- **2026-02-14** | [dax](https://x.com/thdxr/status/2022574719694758147) | management, dev-practices, industry
  dax (thdxr) offers a contrarian take on AI coding hype: orgs are rarely bottlenecked by code-production ability. Most workers use AI to do their tasks with less effort rather than to become 10x; the few who genuinely push are getting buried under everyone else's 'slop code' and may quit; teams remain bottlenecked by bureaucracy; and CFOs are noticing each engineer now costs ~$2,000/month more in LLM bills.

- **2026-02-12** | [Aakash Gupta](https://x.com/aakashgupta/status/2021709282224587141) | research, dev-practices
  Aakash Gupta highlights Andrej Karpathy's 'microgpt': a complete GPT (training loop, inference, optimizer, attention) in 243 lines of Python whose only imports are os, math, random, and argparse, including a hand-rolled ~40-line scalar autograd engine. Frames it as the fifth step in a six-year compression arc: micrograd (2020), minGPT (2020), nanoGPT (2023), llm.c (2024), microgpt (2026).

- **2026-02-12** | [Spencer Baggins](https://x.com/bigaiguy/status/2021532622963585214) | prompting, questionable
  Engagement-style thread claiming 'OpenAI and Anthropic engineers leaked' a technique called 'Socratic prompting' that separates beginners from experts. The substantive nugget: instead of telling the AI what to do, ask it questions. Author claims output quality jumped from 6.2 to 9.1 out of 10.

- **2026-02-12** | [kitze](https://x.com/thekitze/status/2021494167113990464) | skills-mcp, agent-design, dev-practices
  kitze boosts Maximiliano Firtman's note that Chrome 146 ships an early flagged preview of WebMCP, which lets AI agents query and execute a web app's services without driving the UI like a human. Services are declared imperatively via a navigator.modelContext API or declaratively through a form; kitze calls exposing them 'the new responsive design.'

- **2026-02-09** | [Peter Steinberger](https://x.com/steipete/status/2020704611640705485) | prompting, agent-design, claude-code
  Peter Steinberger shares a SOUL.md rewrite prompt (via Molty) to give a coding agent a stronger personality: hold strong opinions instead of hedging, delete corporate-handbook rules, never open with filler like 'Great question', enforce brevity, allow natural humor, call out bad ideas (charm over cruelty), and permit well-placed swearing.

- **2026-02-07** | [Machina](https://x.com/exm7777/status/2019787951530725396) | management, general, industry
  Machina's thread on how to stop feeling behind in AI: the relentless cadence of releases (GPT-5.3 Codex, Opus 4.6, Kling 3.0, all 'redefining everything') creates a low-grade, never-ending pressure. His reframe is that the problem isn't too much happening, it's the lack of a personal filter for what actually matters to your work.

- **2026-02-07** | [chiefofautism](https://x.com/chiefofautism/status/2019608146692673886) | agent-design, dev-practices, research
  chiefofautism shares Shannon (github.com/KeygraphHQ/shannon), an autonomous white-box AI pentester for web applications.

- **2026-02-05** | [Dave Kline](https://x.com/dklineii/status/2018690947215663592) | management
  Dave Kline's thread on how the management job changes by level: most managers fail because they're thrown in with no training, little support, and unrealistic expectations, and the required abilities, priorities, and skills differ sharply from first-line management up through senior levels.

### Jan 2026

- **2026-01-28** | [vogel](https://x.com/ryanvogel/status/2016204202343571474) | agent-design, dev-practices, claude-code
  ryan vogel announces that dynamic agents.md resolution is now live in OpenCode, and suggests pairing it with a /learn command for a powerful workflow; points to @rekram11's explanation of the approach.

- **2026-01-25** | [Dave Kline](https://x.com/dklineii/status/2015406993612079328) | management
  Dave Kline shares a 5-step delegation system, noting that across 1,400+ managers he's trained, delegation is the universal struggle: the hard part isn't assigning work but ensuring it gets done well without micromanaging.

- **2026-01-25** | [Theo - t3.gg](https://x.com/theo/status/2013888279355982131) | claude-code, dev-practices, agent-design
  Theo boosts Wayne Sutton's launch of opensync.dev, a tool to track OpenCode and Claude CLI coding sessions in one place: searchable history, markdown export, eval-ready datasets, and views into tool usage, token spend, and session activity across projects. Theo frames it as a model of good devrel in 2026.

- **2026-01-21** | [abhi](https://x.com/abhigyawangoo/status/2013823175855923640) | agent-design, dev-practices, prompting
  A detailed playbook for building continually-improving AI agents: define the business metric first, think in terms of many per-message/session/long-tail signals (not just thumbs up/down), design UI that makes signal collection easy, build signal-derived few-shot rankers, and A/B test every change against a control group. Includes a long copy-paste prompt for having Claude Code wire feedback loops into an existing agent. Warns about reward hacking when over-optimizing a single signal.

- **2026-01-20** | [Matt Simpson](https://x.com/msmps_/status/2013376201977463038) | skills-mcp, agent-design, dev-practices
  Matt Simpson shipped 'opentui-skill', a skill that gives coding agents TUI (terminal UI) superpowers via decision trees, progressive disclosure, and documented gotchas. Inspired by Dillon Mulroy's cloudflare-skill. Install instructions in a follow-up reply.

- **2026-01-20** | [am.will](https://x.com/llmjunky/status/2013314055755194468) | dev-practices, prompting, agent-design
  am.will endorses a post by Dillon Mulroy on writing agent plans, calling it similar to his own approach but more concise. Plans to adopt some of Dillon's phrasing, especially the language around testing.

- **2026-01-20** | [Sumanth](https://x.com/sumanth_077/status/2013232922296561826) | research, agent-design, dev-practices
  Overview of PageIndex, an open-source 'vectorless' RAG framework that drops vector databases and arbitrary chunking. It builds an LLM-optimized hierarchical tree (like a table of contents) and uses reasoning-based tree search to navigate documents the way a human expert would, giving traceable page-level references. Powers Mafin 2.5, which hits 98.7% on FinanceBench. GitHub link in comments.

- **2026-01-20** | [Mischa van den Burg](https://x.com/mischa_vdburg/status/2013178484143571034) | agent-design, dev-practices, management
  Argues AI agent orchestration is the next 'container orchestration war', building on a Steve Yegge framework of two primitives: Workers (making a single agent produce high-quality output) vs Factories (coordinating thousands of work items across many agents). Maps these to familiar infra patterns - Workers = CI runners/pods/Lambdas, Factories = schedulers/control planes/workflow engines. Predicts 'nondeterministic idempotence' as the new eventual consistency, audit trails for AI work, GitOps-style declarative state, and reuse of the microservices observability stack. Kubernetes-fluent engineers have a head start.

- **2026-01-19** | [Rohun](https://x.com/rohunjauhar/status/2012983351288692941) | claude-code, agent-design, dev-practices
  Rohun open-sourced 'claude-build-workflow', a Claude Code workflow for autonomous building: you describe what you want, answer 10-15 min of interview questions, then close your laptop while an autonomous build loop runs in GitHub Codespaces and notifies your phone when done. It generates a PRD with user stories, technical architecture, edge-case analysis, story-quality validation, JSON conversion, then kicks off the build loop. Stitched together from Geoffrey Huntley's Ralph (bash-loop technique), Ryan Carson's snarktank/ralph (PRD skills, progress tracking, auto-commits, quality checks), and the BMAD Method (discovery/interview framework), adapted from Amp to Claude Code with phone notifications and one-command setup. Repo: github.com/rohunj/claude-build-workflow.

- **2026-01-19** | [DAIR.AI](https://x.com/dair_ai/status/2012903315890225220) | research, agent-design
  DAIR.AI's Top AI Papers of the Week (Jan 12-18, 2026), heavy on agent memory and self-improvement: (1) Learning Latent Action World Models from in-the-wild video without action labels; (2) DroPE - extending context by dropping positional embeddings with cheap recalibration; (3) Dr. Zero - self-evolving search agents with no training data via proposer/solver loop (HRPO); (4) AgeMem - unified long/short-term memory as tool actions; (5) Focus - bio-inspired active context compression (22.7% token cut on SWE-bench Lite with Claude Haiku 4.5); (6) Agent-as-a-Judge survey; (7) SimpleMem - lifelong memory via semantic compression (30x token reduction); (8) Mistral's Ministral 3 (3B/8B/14B, Apache 2.0); (9) UniversalRAG - modality-aware multimodal RAG routing; (10) MemRL - runtime RL on episodic memory.

- **2026-01-19** | [Ian Nuttall](https://x.com/iannuttall/status/2012833663319195970) | skills-mcp, dev-practices, claude-code
  Ian Nuttall shares 'dotagents' (github.com/iannuttall/dotagents), a tool he built to stop the pain of switching between different agent harnesses/clients - he now runs everything from ~/.agents or .agents. Posted in reply to Theo asking for a way to sync agent skills/config across repos via symlink. PRs welcome for unsupported clients.

- **2026-01-19** | [Abhishek Singh](https://x.com/0xlelouch_/status/2012816833464922398) | dev-practices, management
  A Senior Staff Engineer's method for reasoning about unfamiliar systems: (1) start with the business goal and what 'failure' means, not the code; (2) identify the 2-3 critical paths where latency/correctness/money matter; (3) map ownership boundaries and handoff gray areas; (4) look for invariants that must hold even during partial failures/deploys; (5) read postmortems before docs (real vs intended behavior); (6) ask 'what breaks first at 10x load?' to expose hidden assumptions. The kind of skill that separates senior from staff.

- **2026-01-17** | [Sisyphus Labs](https://x.com/justsisyphus/status/2012441415398109192) | agent-design, dev-practices
  Sisyphus Labs recommends Rohit Ghumare's article 'Agents 201: Orchestrating Multiple Agents That Actually Work' as the first useful piece on agent orchestration. The article's premise: after building a single agent, the next challenge isn't making it smarter but making multiple agents cooperate without blowing the token budget or creating coordination chaos.

- **2026-01-17** | [Miles Deutscher](https://x.com/milesdeutscher/status/2012237674409796036) | claude-code, questionable
  Miles Deutscher promotes a curated 'Claude Code Starter Pack (Part 2)' article by AI Edge - a filtered list of Claude Code tools, tutorials, and resources claimed to be the 1% worth your time. Framing leans on hype ('mega viral', 'extract alpha', 'life-changing systems'), so tagged questionable, but the underlying resource is a legitimate Claude Code tool/resource roundup.

- **2026-01-16** | [giyu_codes](https://x.com/giyu_codes/status/2012420750855012428) | claude-code, skills-mcp, dev-practices
  giyu_codes recommends cogsec (@affaan)'s article 'The Shorthand Guide to Everything Claude Code' - a complete setup after 10 months of daily use covering skills, hooks, subagents, MCPs, plugins, and what actually works. High-reach post (~806K views).

- **2026-01-16** | [Yishan](https://x.com/yishan/status/2012067968331710639) | general
  [Post deleted/unavailable]

- **2026-01-16** | [Gregor Zunic](https://x.com/gregpr07/status/2012052139384979773) | agent-design, dev-practices, claude-code
  Gregor Zunic (Browser Use) argues 'The Bitter Lesson of Agent Frameworks': all the value is in the RL'd model, not thousands of lines of abstractions. An agent is just a for-loop of tool calls that runs until the model stops. Abstractions freeze assumptions and fight what the model already learned; agent frameworks fail because their action spaces are incomplete, not because models are weak. Their fix: start with maximal capability then restrict ('vibe-restrict' via evals). BU Agent gives the model raw Chrome DevTools Protocol + extension APIs for a near-complete action space. Also covers a minimal model-agnostic Chat wrapper (Anthropic/OpenAI/Google), ephemeral messages to keep massive DOM/screenshot state out of context, and the done() tool for explicit completion. Reliability (retries, rate limits, compaction) is ops, not the agent. Open-sourcing as agent-sdk (includes a Claude Code re-implementation).

- **2026-01-16** | [Paul Solt](https://x.com/paulsolt/status/2012010080414081188) | dev-practices, agent-design, prompting
  Paul Solt's 7 beginner tips for OpenAI Codex: (1) start with GPT-5.2-Codex 'high' reasoning - enough for most work, avoid xhigh unless tricky; (2) when reasoning doesn't help, give agents better up-to-date local docs (he uses DocSetQuery to turn Dash DocSets into local Markdown); (3) read Peter Steinberger's (@steipete) 'shipping at inference speed' post; (4) borrow from Peter's agents.md and agent-scripts (e.g. 'committer' for atomic commits with multiple agents in one folder); (5) just talk to Codex - no complex rules or huge plan files; work one aspect at a time and parallelize projects while waiting; (6) ask agents to copy structure/Makefiles from other projects; (7) you'll likely need YOLO/danger mode to avoid constant approval nagging.

- **2026-01-16** | [vas](https://x.com/vasuman/status/2011983687433212330) | agent-design, dev-practices
  vas (@vasuman) shares 'AI Agents 101,' a comprehensive long-form X article on how to build AI agents that actually work, framed as required reading before writing any code and drawing on 3 years as a Meta software engineer. He asks whether a part 2 would be useful.

- **2026-01-16** | [Gergely Orosz](https://x.com/gergelyorosz/status/2011956185650409558) | dev-practices, management
  Gergely Orosz amplifies Cindy Sridharan's take that, outside of prototyping, engineers should aim to understand close to 100% of the production code LLMs generate. He adds that the gap between teams who do this and those who don't will be massive, and notes the tension: heavy cutting-edge AI use is easiest on throwaway prototypes where it's fine to let it rip.

- **2026-01-16** | [Bojan Tunguz](https://x.com/tunguz/status/2011949233658925298) | general
  [Post deleted/unavailable]

- **2026-01-16** | [James Cowling](https://x.com/jamesacowling/status/2011924122922852599) | dev-practices, industry, agent-design
  James Cowling points to the Software Crisis of the 1960s-70s (en.wikipedia.org/wiki/Software_crisis) as a warning: productivity ground to a halt until good abstractions for managing software complexity emerged. His thesis is that without good platforms, the same stall will happen again in the AI-coding era.

- **2026-01-16** | [Meta Alchemist](https://x.com/meta_alchemist/status/2010882913784070231) | general
  [Post deleted/unavailable]

- **2026-01-16** | [Simplifying AI](https://x.com/simplifyinAI/status/2010878423325364233) | general
  [Post deleted/unavailable — in Jan 3-16 dead zone]

- **2026-01-16** | [Sahil Bloom](https://x.com/SahilBloom/status/2010703181900464151) | general
  [Post deleted/unavailable — in Jan 3-16 dead zone]

- **2026-01-15** | [geoff](https://x.com/GeoffreyHuntley/status/2010567043629113814) | general
  [Post deleted/unavailable — in Jan 3-16 dead zone]

- **2026-01-15** | [will brown](https://x.com/willccbb/status/2010547008387408150) | general
  [Post deleted/unavailable — in Jan 3-16 dead zone]

- **2026-01-15** | [James Shields](https://x.com/scaling_shields/status/2010413738506264649) | general
  [Post deleted/unavailable — in Jan 3-16 dead zone]

- **2026-01-15** | [siddhi surana](https://x.com/siddhisurana/status/2010361699087921253) | general
  [Post deleted/unavailable — in Jan 3-16 dead zone]

- **2026-01-15** | [Jaime Jorge](https://x.com/jaimefjorge/status/2010254648389550243) | general
  [Post deleted/unavailable — in Jan 3-16 dead zone]

- **2026-01-14** | [BOOTOSHI](https://x.com/KingBootoshi/status/2010002905316757751) | general
  [Post deleted/unavailable — in Jan 3-16 dead zone]

- **2026-01-14** | [Matt Pocock](https://x.com/mpocock/status/2009888462821732368) | general
  [Post deleted/unavailable — in Jan 3-16 dead zone]

- **2026-01-13** | [fintechjunkie](https://x.com/fintechjunkie/status/2010910565279961423) | general, questionable
  fintechjunkie gives a glowing, no-edits endorsement of a Dan Koe (@thedankoe) long-form article titled 'How to fix your entire life in 1 day' — a self-improvement/productivity piece rather than an AI or engineering topic. Off-theme for the collection; kept for completeness.

- **2026-01-12** | [bluecow](https://x.com/bluecow/status/2009065743606194185) | general
  [Post deleted/unavailable]

- **2026-01-12** | [Nozz](https://x.com/nozz/status/2008835341649346666) | general
  [Post deleted/unavailable — in Jan 3-16 dead zone]

- **2026-01-10** | [Nick Dobos](https://x.com/dobosn/status/2008036181346656365) | general
  [Post deleted/unavailable]

- **2026-01-10** | [Param](https://x.com/param_bharadwaj/status/2007915284024619160) | general
  [Post deleted/unavailable — in Jan 3-16 dead zone]

- **2026-01-10** | [Felipe Coury](https://x.com/felipecoury/status/2007882656892014636) | general
  [Post deleted/unavailable]

- **2026-01-10** | [kitze](https://x.com/kitze/status/2007809540919521316) | general
  [Post deleted/unavailable — in Jan 3-16 dead zone]

- **2026-01-10** | [Rohit](https://x.com/rohitxo/status/2007748502661742686) | general
  [Post deleted/unavailable — in Jan 3-16 dead zone]

- **2026-01-10** | [Aakash Gupta](https://x.com/AakashGuptaGH/status/2007704814065365016) | general
  [Post deleted/unavailable — in Jan 3-16 dead zone]

- **2026-01-10** | [elvis](https://x.com/elvisnguyen/status/2007665597046087848) | general
  [Post deleted/unavailable — in Jan 3-16 dead zone]

- **2026-01-10** | [nader dabit](https://x.com/dabit3/status/2007623542340276413) | general
  [Post deleted/unavailable — in Jan 3-16 dead zone]

- **2026-01-10** | [dei](https://x.com/delilahime/status/2007599629893906627) | general
  [Post deleted/unavailable — in Jan 3-16 dead zone]

- **2026-01-10** | [Brandon Gell](https://x.com/brandongell/status/2007537024606646369) | general
  [Post deleted/unavailable — in Jan 3-16 dead zone]

- **2026-01-09** | [Alex Hillman](https://x.com/alexhillman/status/2007195403503431942) | general
  [Post deleted/unavailable — in Jan 3-16 dead zone]

- **2026-01-09** | [dei](https://x.com/delilahime/status/2007112398968512604) | general
  [Post deleted/unavailable — in Jan 3-16 dead zone]

- **2026-01-08** | [Jarrod Watts](https://x.com/jarrodwatts/status/2009200810870428123) | claude-code, skills-mcp, dev-practices
  Jarrod Watts open-sourced his 'claude-code-config' repo containing all the agents, commands, hooks, rules, skills, and plugins he's made or collected over the past few months — described as simple but effective enhancements he'll keep updating. A ready-made reference config for a team standardizing Claude Code setups.

- **2026-01-08** | [Lior Alexander](https://x.com/lioralexander/status/2006763456879984843) | general
  [Post deleted/unavailable — in Jan 3-16 dead zone]

- **2026-01-08** | [Josh Pigford](https://x.com/joshpigford/status/2006722184752509040) | general
  [Post deleted/unavailable — in Jan 3-16 dead zone]

- **2026-01-08** | [Tom Dörr](https://x.com/tom_dorr/status/2006640889625956454) | general
  [Post deleted/unavailable — in Jan 3-16 dead zone]

- **2026-01-08** | [Ryan Carson](https://x.com/ryancarson/status/2006579357155549261) | general
  [Post deleted/unavailable — in Jan 3-16 dead zone]

- **2026-01-07** | [Jeffrey Emanuel](https://x.com/jfemanuel13/status/2006283589341868394) | general
  [Post deleted/unavailable]

- **2026-01-07** | [Tech with Mak](https://x.com/TechWithMak/status/2006215651880165597) | general
  [Post deleted/unavailable — in Jan 3-16 dead zone]

- **2026-01-07** | [Obie Fernandez](https://x.com/obiefernandez/status/2006152066925707274) | general
  [Post deleted/unavailable — in Jan 3-16 dead zone]

- **2026-01-07** | [Melvin Vivas](https://x.com/melvinator/status/2006020697936482443) | general
  [Post deleted/unavailable — in Jan 3-16 dead zone]

- **2026-01-07** | [Sumanth](https://x.com/Sumanth_077/status/2005956018357575750) | general
  [Post deleted/unavailable — in Jan 3-16 dead zone]

- **2026-01-06** | [Md Ismail](https://x.com/mdismail/status/2005671283621953665) | general
  [Post deleted/unavailable — in Jan 3-16 dead zone]

- **2026-01-06** | [Simplifying AI](https://x.com/simplifyinAI/status/2005513621646409748) | general
  [Post deleted/unavailable — in Jan 3-16 dead zone]

- **2026-01-06** | [Josh Schultz](https://x.com/jschultzme/status/2005421815916028959) | general
  [Post deleted/unavailable — in Jan 3-16 dead zone]

- **2026-01-06** | [Trending GitHub](https://x.com/TrendingGitHubl/status/2005310239286649010) | general
  [Post deleted/unavailable — in Jan 3-16 dead zone]

- **2026-01-06** | [The Boring Marketer](https://x.com/BoringMarketer/status/2005239063816110289) | general
  [Post deleted/unavailable — in Jan 3-16 dead zone]

- **2026-01-06** | [Tom Dörr](https://x.com/tom_dorr/status/2005167892304969882) | general
  [Post deleted/unavailable — in Jan 3-16 dead zone]

- **2026-01-06** | [Santiago](https://x.com/santiagoemeli/status/2005035706842611040) | general
  [Post deleted/unavailable — in Jan 3-16 dead zone]

- **2026-01-06** | [hoeem](https://x.com/hoeemlim/status/2004948633556197506) | general
  [Post deleted/unavailable — in Jan 3-16 dead zone]

- **2026-01-05** | [Matt Pocock](https://x.com/mpocock/status/2004505491297665063) | general
  [Post deleted/unavailable]

- **2026-01-03** | [Daniel San](https://x.com/dcsan/status/2003544127356903508) | general
  [Post deleted/unavailable]

- **2026-01-03** | [sankalp](https://x.com/sankalpdev/status/2003384719234969898) | general
  [Post deleted/unavailable — in Jan 3-16 dead zone]

- **2026-01-03** | [CloudAI-X](https://x.com/CloudAI_X/status/2003298874369306643) | general
  [Post deleted/unavailable — in Jan 3-16 dead zone]

- **2026-01-03** | [Grok](https://x.com/XAI/status/2003101023145590851) | general
  [Post deleted/unavailable]

### Dec 2025

- **2025-12-28** | [Denislav Gavrilov](https://x.com/kuberdenis/status/2004934631616086417) | claude-code, agent-design, dev-practices
  Denislav Gavrilov containerizes Claude Code in Kubernetes as 'Clopus-Watcher,' an autonomous monitoring agent that watches a namespace and, on application errors, writes and applies a hotfix and documents it — effectively a 24/7 on-call engineer. Repo, examples, and results at denislavgavrilov.com.

- **2025-12-28** | [AGENTS.md](https://agents.md/) | agent-design, dev-practices, skills-mcp
  AGENTS.md (agents.md) is a simple, open format for guiding coding agents, now used by over 60k open-source projects. Think of it as a README for agents: a dedicated, predictable place for the build steps, tests, and conventions that coding agents need but that would clutter a human README — kept intentionally separate so agents have one clear location to look.

- **2025-12-27** | [SightBringer](https://x.com/_the_prophet__/status/2004796159299084424) | industry, management, agent-design
  An essay arguing software engineering is undergoing a 'phase transition' in human leverage: for decades leverage came from writing more correct instructions faster, but the unit of leverage has shifted from writing code to orchestrating intelligence. The programmer becomes a systems integrator of probabilistic entities whose reasoning can't be fully inspected or controlled — which the author says explains why even Karpathy feels 'behind.'

- **2025-12-27** | [Yu Lin](https://x.com/yulintwt/status/2004537183978590695) | general
  [Account suspended]

- **2025-12-22** | [Tech with Mak](https://x.com/technmak/status/2002713140757496299) | agent-design, skills-mcp, dev-practices, questionable
  A structured LangGraph learning path (pitched as filling the gap since LangGraph appears in ~half of AI job descriptions). Progresses from basic agent concepts (Pydantic data validation, agentic chatbots, multi-agent coordination) through production systems (a 2.5-hour LangGraph+MCP crash course, debugging/monitoring, deployment architecture) to RAG pipelines (multimodal RAG, hallucination fixes, end-to-end retrieval, Typesense search).

- **2025-12-22** | [Abhishek Singh](https://x.com/0xlelouch_/status/2002673253912113644) | management, general
  A reflective essay on career fulfillment in software engineering: you don't magically know whether backend, frontend, infra, ML, startups, big tech, or management will fulfill you — you only find out through reps. Early on people confuse novelty (new frameworks, jobs, titles) with fulfillment; real self-knowledge is earned by shipping boring features, debugging 3am outages, owning systems, and sticking with things long enough to feel the responsibility.

- **2025-12-21** | [Claire Silver](https://x.com/clairesilver12/status/2002443560898208162) | skills-mcp, claude-code, agent-design
  Claire Silver highlights Unreal MCP, a free MCP server that lets you prompt Claude to build things in Unreal Engine — e.g. 'make a Victorian manor, here's a reference pic, use the assets in this folder' and it just does it. She promised a demo video and calls it '10/10 magic.'

- **2025-12-19** | [Santiago](https://x.com/svpino/status/2002107789888655655) | agent-design, dev-practices
  Santiago shares a video demoing a spec-driven development environment where 100% of the developer's time goes to writing specs and managing agents and 0% to writing code — arguing software development will never be the same.

- **2025-12-19** | [Jason Fried](https://x.com/jasonfried/status/2002084849784676697) | dev-practices
  Jason Fried shares a talk in which Jeff, an 18-year 37signals veteran, explains the 'recordables pattern' — the single most important architectural pattern behind Basecamp and HEY and a key reason both codebases remain a joy to work on. Fried calls the insights deep, practical, and accessible even to non-technical folks.

- **2025-12-19** | [Justin Mitchel](https://x.com/justinmitchel/status/2001750598329499681) | dev-practices, research
  Justin Mitchel flags that pg_textsearch was just open-sourced (github.com/timescale/pg_textsearch), a PostgreSQL extension bringing BM25 relevance-ranked full-text search to your database — meaning teams already on Postgres can skip syncing data to Elasticsearch for keyword search. Post is marked #sponsored.

- **2025-12-16** | [Femke Plantinga](https://x.com/femke_plantinga/status/2000883645888827806) | agent-design
  Femke Plantinga argues multi-agent AI systems are displacing single-agent architectures and breaks down what a well-structured one looks like: a supervisor/orchestration layer that plans, routes queries to specialists and refines them (the 'air traffic controller'), plus specialized task-specific agents (query rewriters, etc.). She notes the real trade-off — more complex workflows but serious coordination challenges.

- **2025-12-15** | [Matt Dancho (Business Science)](https://x.com/mdancho84/status/2000658529753932273) | agent-design, dev-practices, research
  Matt Dancho highlights an open-sourced (free) Python library, 'AI Data Science Team' (github.com/business-science/ai-data-science-team), that automates data-science workflows with AI — data loading, cleaning, exploratory analysis, and feature engineering — tracking each step in a fully reproducible pipeline. Includes a walkthrough video and a free 1-hour agentic AI workshop.

- **2025-12-14** | [Kermit](https://x.com/fixer9999/status/2000332286055850464) | industry
  A bare link post sharing Perplexity's 'Perplexity at Work' PDF report (r2cdn.perplexity.ai/pdf/pplx-at-work.pdf) — Perplexity's enterprise/workplace positioning material. Low engagement; minimal commentary.

- **2025-12-14** | [Jainam Parmar](https://x.com/aiwithjainam/status/1999815060965994896) | prompting, questionable
  An engagement-styled post ('Chain of Thought is dead') claiming that 'Atom of Thought' prompting made models 30-40% more accurate on complex reasoning tasks, pitched as a technique that will change how people use ChatGPT and Claude. Hype framing, but the underlying Atom-of-Thought prompting idea is a real reasoning technique worth a look.

- **2025-12-09** | [Tech with Mak](https://x.com/technmak/status/1998264904563007889) | research, agent-design
  Tech with Mak distills Google's quiet December release of five AI-agent papers published one per day over five consecutive days — more than 250 pages covering how agents should be built, evaluated, secured, and deployed.

- **2025-12-09** | [Rohan Paul](https://x.com/rohanpaul_ai/status/1998262710040228310) | research, agent-design, prompting
  Rohan Paul summarizes a paper proposing an 'agentic file system' for context engineering: treat every memory, tool, external source, and human note as a file in a shared space, with a persistent context repository separating raw history, long-term memory, and short-lived scratchpads so the prompt holds only the slice needed now. Every access is logged with timestamps and provenance, and a constructor/updater/evaluator manage context under the model's limited window.

- **2025-12-08** | [Yahiya](https://x.com/yahiyadev/status/1997744726913736979) | dev-practices
  Answering a request for a book on structuring a monolith so services can be decoupled later, Yahiya recommends 'Event-Driven Architecture in Golang' by Michael Stack — which starts from a modular monolith and gradually transitions to microservices, covering Event Sourcing, CQRS, DDD, choreographed and orchestrated messaging, and sync-to-async refactoring — plus 'Domain-Driven Design with Golang' by Matthew Boyle.

- **2025-12-08** | [Tom Dörr](https://x.com/tom_doerr/status/1996997820868366397) | skills-mcp, claude-code
  Tom Dörr shares 'awesome-claude-skills' (github.com/VoltAgent/awesome-claude-skills), a curated collection of official and community-built Claude skills.

- **2025-12-07** | [Rohan Paul](https://x.com/rohanpaul_ai/status/1997405403987222642) | research, agent-design, prompting
  Rohan Paul summarizes Google's guide on context engineering for multi-agent systems (built around ADK). Instead of giant prompts, it compiles a view over state split into Working Context, Session, Memory, and Artifacts; each call rebuilds Working Context from instructions, selected session events, memory results, and artifact references. ADK controls context growth via compaction, filtering, and caching — summarizing old spans, dropping useless events, and reusing a stable prefix — and pushes large payloads out to Artifacts to keep systems fast, affordable, and less hallucination-prone.

- **2025-12-07** | [Hayes](https://x.com/hayesdev_/status/1996897853642592428) | general
  [Account suspended]

- **2025-12-01** | [AWS Containers](https://github.com/aws-containers/reinvent) | dev-practices, industry
  The aws-containers/reinvent GitHub repo collects AWS re:Invent 2025 Kubernetes Track assets — slides, the latest EKS launches, and demos from the sessions. A reference for what AWS shipped for Kubernetes/EKS at re:Invent 2025.

### Nov 2025

- **2025-11-29** | [Dave Kline](https://x.com/dklineii/status/1994761636742050226) | management
  Dave Kline's thread on 'The 7 Deadly Sins of New Managers,' framed around the claim that ~60% of people fail in their first leadership role. This post is the hook for a list of common first-time-manager mistakes (detailed items continue in the thread/graphic).

- **2025-11-25** | [Ray Fernando](https://x.com/rayfernando1337/status/1992848315541823490) | skills-mcp, claude-code
  Ray Fernando recommends Lee Han-Chung's 'Claude Skills deep dive' blog post (leehanchung.github.io) as the best breakdown of Claude Skills he's seen.

- **2025-11-15** | [Thariq](https://x.com/trq212/status/1989061939625144388) | claude-code, skills-mcp
  Thariq gives the setup commands for Anthropic's frontend-design plugin in Claude Code: add the marketplace with '/plugin marketplace add anthropics/claude-code', then '/plugin install frontend-design@claude-code-plugins'. Getting-started reply for the frontend-design plugin.

- **2025-11-12** | [George from prodmgmt.world](https://x.com/nurijanian/status/1988335427447869565) | prompting, management
  George (prodmgmt.world) shares a 'tough, unreasonable product executive' critique prompt he runs product decisions through: it skeptically stress-tests requirements across cross-team collaboration, conflicting requirements, maintainability, strategic implications, clarity, and feasibility, returning structured critiques (section/issue/impact/suggestion). Ends with a paid prompt-library link.

- **2025-11-08** | [Dan Shipper](https://x.com/danshipper/status/1986870518046200255) | dev-practices, claude-code, agent-design
  Dan Shipper recommends Kieran Klaassen's Every piece 'Teach Your AI to Think Like a Senior Engineer' (every.to/source-code) as a masterclass on coding with AI.

- **2025-11-06** | [Prompter](https://x.com/promptllm/status/1986173095896621150) | questionable, prompting
  Prompter claims elite performers all use neuro-linguistic programming (NLP) and offers a prompt that 'teaches you NLP.' Engagement-bait framing with an unsubstantiated claim; the actual prompt is not shown in the post.

- **2025-11-01** | [Charly Wargnier](https://x.com/datachaz/status/1984276199309484409) | prompting, questionable
  Charly Wargnier boosts a claim that someone put in 1,000 hours of prompt engineering to distill the 6 prompt patterns that actually matter. Hook post pointing to the six patterns (detailed in the referenced content).

### Oct 2025

- **2025-10-31** | [Aadit Sheth](https://x.com/aaditsh/status/1983103310791159863) | management, industry
  Aadit Sheth shares a chart breaking down what being 'good with AI' looks like role by role, framed as a way to gauge whether a team is truly AI-fluent and pitched as useful for hiring and leading in 2025. The breakdown itself is in an attached chart image.

- **2025-10-29** | [Matt Pocock](https://x.com/mattpocockuk/status/1983255353597870285) | claude-code, prompting, dev-practices
  Matt Pocock shares his favorite AI coding tip: add 'Be extremely concise. Sacrifice grammar for the sake of concision.' to your global claude.md file for noticeably better output.

- **2025-10-28** | [William Meijer](https://x.com/williameijer/status/1982843287095717935) | management
  William Meijer argues that a willingness to voice 'unkind truths' — blunt, uncomfortable candor — is a key element of Elon Musk's entrepreneurial success.

- **2025-10-24** | [Pontus Abrahamsson](https://x.com/pontusab/status/1981700333857636550) | agent-design, skills-mcp, dev-practices
  Pontus Abrahamsson points to midday-ai/ai-sdk-tools (github.com/midday-ai/ai-sdk-tools) — a set of example AI SDK tools/integrations for building agent tooling.

- **2025-10-24** | [Thomas H. Ptacek](https://x.com/tqbf/status/1981439969370558803) | dev-practices
  Thomas Ptacek, reacting to the AWS outage postmortem and its HN discussion, evangelizes 'How Complex Systems Fail' (howcomplexsystems.fail) as essential reading on how failures emerge in complex socio-technical systems.

- **2025-10-24** | [Hayes](https://x.com/neatprompts/status/1981241949173825687) | general
  [Account suspended]

- **2025-10-21** | [Raul Junco](https://x.com/rauljuncov/status/1980243241783197925) | dev-practices, questionable
  Raul Junco frames system design as a staircase to climb step by step rather than jumping to distributed systems: foundations (networking, databases, caching, APIs), then mechanics (queues, consistency, observability, failures), then architecture (trade-offs, evolution, resilience).

- **2025-10-21** | [Ray Fernando](https://x.com/rayfernando1337/status/1980180030971150690) | research, industry
  Ray Fernando shares DeepSeek-OCR (github.com/deepseek-ai/DeepSeek-OCR) — DeepSeek's 'Contexts Optical Compression' approach that encodes long text contexts as visual tokens for efficient OCR and document understanding.

- **2025-10-19** | [Aakash Gupta](https://x.com/aakashg0/status/1979517333015334953) | management
  Aakash Gupta highlights Jeff Bezos's framework distinguishing reversible ('two-way door') from irreversible ('one-way door') decisions as a guide to how much deliberation a call deserves.

- **2025-10-19** | [Always Keep Learning](https://x.com/alwayskeepl/status/1979452892059967974) | management
  Infographic-style post outlining servant leadership as an alternative model for leading teams differently.

- **2025-10-17** | [Alex Lieberman](https://x.com/businessbarista/status/1978988763620741503) | management
  Alex Lieberman shares a '5 levels of work' framework for teaching high agency, from L1 'there is a problem' to L5 'I found it, fixed it, just keeping you in the loop.' He tells new hires to operate at Level 4 from day one and grow into Level 5. Credits Steph Smith.

- **2025-10-11** | [Kevin Box](https://x.com/fuel_yourgrowth/status/1977008526867546245) | management
  Infographic contrasting a toxic boss with a great leader, arguing a manager's impact on employee mental health can exceed a therapist's.

- **2025-10-09** | [Kevin Box](https://x.com/fuel_yourgrowth/status/1976274742702440662) | management
  Short motivational post arguing that being easy to work with is an underrated professional skill.

- **2025-10-07** | [Ruslan Beskorovainiy](https://x.com/chemobyazan/status/1975326044271079509) | agent-design, skills-mcp
  Points to the contains-studio/agents GitHub repo, a shared collection of AI agents currently in use.

- **2025-10-07** | [Vivek Galatage](https://x.com/vivekgalatage/status/1974894313948758373) | dev-practices, research
  Vivek Galatage recommends Richard Hipp's 2024 'SQLite: How it works' lecture on database internals from the creator himself, in a thread noting SQLite's ubiquity (including in Chromium browser engines).

- **2025-10-07** | [keshav](https://x.com/kshvbgde/status/1974835291358969895) | management, general
  Post (likely video/thread) on Steve Jobs's principles for designing insanely great products.

- **2025-10-05** | [Prompter](https://x.com/promptllm/status/1974518025211818291) | prompting, questionable
  Engagement-style post promoting a prompt for learning to think in systems.

- **2025-10-05** | [Agentic Design Patterns](https://github.com/sarwarbeing-ai/Agentic_Design_Patterns/blob/main/Agentic_Design_Patterns.pdf) | agent-design
  [Post unavailable — Agentic Design Patterns GitHub repo removed via DMCA takedown]

- **2025-10-04** | [Prompter](https://x.com/promptllm/status/1974206336511394165) | prompting, questionable
  Engagement-style post promoting a prompt that claims to teach 'NLP' (Neuro-Linguistic Programming) techniques used by high performers.

- **2025-10-01** | [Sumit Mittal](https://x.com/bigdatasumit/status/1972908540692947192) | dev-practices, research
  Sumit Mittal walks through S3/Athena query cost optimization: moving from uncompressed row-based CSV to columnar Parquet with Snappy compression, partitioning by city, and column pruning cuts a $25 full-scan query to about $0.01 (~2500x cheaper). Ends with a course promo.

### Sep 2025

- **2025-09-30** | [Jawad](https://x.com/jawad_shreim/status/1972998935687172213) | dev-practices, general, questionable
  Jawad shares a humorous, plain-language 'explanation' of AWS services (EC2, ECS, etc.) quote-tweeted from MilkStraw AI.

- **2025-09-23** | [Jamon](https://x.com/jamonholmgren/status/1969883090056249776) | dev-practices, research
  Jamon Holmgren strongly recommends Lydia Hallie's article 'Behind The Scenes of Bun Install' as a top-10 must-read for every developer on building performant systems, regardless of whether you use JavaScript or Bun.

- **2025-09-22** | [Dan McAteer](https://x.com/daniel_mac8/status/1970120352664605124) | agent-design, dev-practices
  Shares a four-step agentic-coding pattern with an added Verification step (build feedback loops that test the plan was implemented correctly, since models still fail on execution), meant to be copied into an AGENTS.md file. Works with AmpCode or any AGENTS.md-aware coding agent.

- **2025-09-15** | [Aakash Gupta](https://x.com/aakashg0/status/1967135994228166848) | agent-design, questionable
  Boosts another user's step-by-step roadmap for building your first AI agent, calling it 'gold.' Engagement-style framing; the substantive content lives in the referenced roadmap rather than the post itself.

- **2025-09-03** | [maxleedev](https://x.com/maxleedev/status/1962938769914658984) | agent-design, general
  Announces a canvas-style interface for LLMs, built in response to a viral post arguing chat UIs need git-like branching/forking of conversations to explore alternate threads without derailing the main one.

- **2025-09-03** | [Raul Junco](https://x.com/rauljuncov/status/1962850589165129870) | dev-practices
  A practical guide to the Retry pattern for resilience: cap retries (~3), use exponential backoff to avoid the thundering-herd effect, retry only transient errors (408/5xx, not 4xx), and pair with a circuit breaker to prevent cascading failures on a truly-down service.

- **2025-09-02** | [ℏεsam](https://x.com/hesamation/status/1962508535515791739) | dev-practices, management
  Recommends a blog (linked in the post) as a strong source of technical playbooks, useful both for engineers and for managers who want a grounding in technical topics.

### Aug 2025

- **2025-08-21** | [Matt Pocock](https://x.com/mattpocockuk/status/1958179930262356032) | prompting, claude-code
  Praises an Anthropic context-engineering template as a solid reference for structuring context for LLMs.

- **2025-08-19** | [Arthur MacWaters](https://x.com/arthurmacwaters/status/1957580001433514167) | industry, management
  Endorses a referenced approach as 'unironically the right way to build a startup.' The substantive content is in the quoted/referenced post rather than the one-line commentary.

- **2025-08-19** | [Dan Shipper](https://x.com/danshipper/status/1957469868862677028) | agent-design, dev-practices, claude-code
  Links Dan Shipper's Every essay 'My AI Had Already Fixed the Code Before I Saw It,' on AI coding agents autonomously fixing code before the developer even reviews it.

- **2025-08-18** | [Dante O. Cuales, Jr.](https://x.com/danteocualesjr/status/1957204427909321027) | agent-design, management, prompting
  Argues the intimidation factor of AI engineering is mostly artificial: most work is API orchestration, prompt optimization, and data-pipeline plumbing, with model internals abstracted away. The real skill is choosing the right tool and chaining them effectively.

- **2025-08-18** | [Asterisk (getAsterisk)](https://github.com/getAsterisk/claudia) | claude-code, agent-design, skills-mcp
  opcode (formerly Claudia, by Asterisk) is an open-source Tauri 2 desktop GUI and toolkit for Claude Code: visual project/session management, custom CC agents with per-agent file/network permissions and background execution, a usage/cost analytics dashboard, MCP server management (with Claude Desktop import), session timeline/checkpoints with diff and fork, and a built-in CLAUDE.md editor. Note: the repo has been renamed from getAsterisk/claudia to winfunc/opcode.

- **2025-08-15** | [Philip Vollet](https://x.com/philipvollet/status/1955945448860008655) | agent-design, research, skills-mcp
  Announces Elysia, an open-source agentic RAG platform (successor to Verba) built on Weaviate and DSPy. Highlights: transparent decision-tree agents with self-healing and custom tools/branches, pre-query data analysis to avoid blind vector/text search, dynamic result displays, feedback-driven few-shot personalization so smaller models perform like larger ones, and query-time chunk-on-demand. Delivered as a FastAPI+NextJS app and a pip package (elysia-ai).

- **2025-08-11** | [Imrat](https://x.com/imrat/status/1954497164589056090) | claude-code, agent-design, dev-practices
  A recipe for using Claude Code as a DevOps agent with its new background jobs: run Claude in a tmux session, have it spawn a background process to tail server logs and summarize them, then a second process that pings Claude to 'check logs' on an interval.

- **2025-08-09** | [Aadit Sheth](https://x.com/aaditsh/status/1953462911961374889) | general
  [Post deleted/unavailable]

### Jul 2025

- **2025-07-31** | [K Srinivas Rao](https://x.com/sriniously/status/1950432839474012456) | dev-practices
  [Post unavailable — page doesn't exist]

- **2025-07-11** | [Book Therapy](https://x.com/book_therapy223/status/1943651617976283236) | management
  Shares content on the distinction 'A Plan is Not a Strategy' (the Roger Martin / HBR theme): strategy is an integrated set of choices about where to play and how to win, not merely a list of planned activities. Post text is just the headline; the substance is in the attached media.

### Jun 2025

- **2025-06-23** | [Graham Helton](https://x.com/grahamhelton3/status/1936462167751921698) | management, dev-practices
  Before leaving Google for Snowflake, Graham Helton braindumped ~34 personal guidelines/principles he follows for work and productivity; the thread lists them.

- **2025-06-18** | [DHH](https://x.com/dhh/status/1934978649872371944) | management
  DHH argues the jump from Programmer to Senior Programmer is the biggest career-progression chasm in software; those who cross it tend to keep advancing, but many never do.

- **2025-06-07** | [Nick Dobos](https://x.com/nickadobos/status/1930878279290060975) | research, agent-design, skills-mcp
  Riffs on a repo (Shubham Saboo's) that stores millions of text chunks inside MP4 video files for fast semantic search, pitched as an open-source replacement for expensive vector databases; Nick Dobos speculates video may be an optimal encoding for AI memory, echoing how human memory leans on vision.

- **2025-06-01** | [Dave Kline](https://x.com/dklineii/status/1928797718907908342) | management
  Opens a management thread promising one skill to become a better manager overnight; the specific skill and guidance are developed in the replies.

### Apr 2025

- **2025-04-23** | [Anthropic](https://github.com/anthropics/courses/tree/master/prompt_engineering_interactive_tutorial/Anthropic%201P) | prompting, claude-code, research
  Anthropic's official interactive prompt-engineering tutorial (Jupyter notebooks in anthropics/courses): a 9-chapter curriculum on prompt structure, being clear and direct, role prompting, separating data from instructions, output formatting, step-by-step reasoning, few-shot examples, and avoiding hallucinations, plus appendices on prompt chaining, tool use, and search & retrieval.

### Jan 2025

- **2025-01-22** | [Mervin Praison](https://x.com/mervinpraison/status/1881788246684013011) | agent-design, research, skills-mcp
  Shows a 100% local RAG AI agent with reasoning: DeepSeek via Ollama for the LLM, PraisonAI to build the agent in a few lines, Nomic embeddings, and a Streamlit UI—code included in the thread.

- **2025-01-21** | [Santiago](https://x.com/svpino/status/1881336934418755862) | research, agent-design, industry
  Walks through GroundX, an open-source, self-hostable/air-gapped enterprise RAG system. Two services: Ingest (a pretrained vision model that 'understands' documents instead of feeding raw docs to the LLM) and Search (text+vector search with a fine-tuned re-ranker). Santiago's thesis: most teams need better ingestion, not better retrieval; includes a video demo and the free X-Ray inspection tool.

- **2025-01-04** | [Tom Dörr](https://github.com/tom-doerr/dotfiles/blob/master/instruction.md) | claude-code, prompting, dev-practices, agent-design
  Tom Dörr's AI-coding-agent instruction file (an AGENTS.md-style rules doc): single-letter command aliases (c=continue, rc=reduce complexity, acp=add/commit/push, t=add tests), strict engineering rules (no fallbacks, don't swallow exceptions, TDD with many asserts, uv over pip, work on git branches, keep complexity low, don't weaken the linter), and ready-to-paste DSPy optimizer snippets (BootstrapFewShotWithRandomSearch, MIPROv2, SIMBA).

### Nov 2024

- **2024-11-29** | [Elon Musk](https://x.com/elonmusk/status/1862363270931255356) | management, dev-practices
  Elon Musk touts his '5-step algorithm' for making fewer mistakes (make requirements less dumb, delete parts/processes, simplify & optimize, accelerate cycle time, automate), in a quote of a post speculating DOGE might adopt it like SpaceX.

### Oct 2024

- **2024-10-25** | [Shubham Saboo](https://x.com/saboo_shubham_/status/1849638773136687551) | research, agent-design, dev-practices
  Introduces AutoRAG, an open-source tool that automatically benchmarks multiple RAG strategies to find the optimal RAG pipeline for your data in a few lines of Python.

- **2024-10-19** | [Sarah Cone](https://x.com/sarah_cone/status/1847322215907545129) | management, dev-practices
  Points to a superengineer.net blog post as a good summary of Elon Musk's 5-step design/engineering method (DFX).

- **2024-10-17** | [Dominik Tornow](https://x.com/dominiktornow/status/1846507701599433179) | dev-practices, research
  Flags a paper as a strong discussion of how hard retries are to get right for reliability under failure—retries are often oversold as a simple fix but are surprisingly complex.

### Jul 2024

- **2024-07-30** | [Shubham Saboo](https://x.com/saboo_shubham_/status/1818111127286579448) | agent-design, research
  Tutorial for building a no-code RAG chatbot to chat with any GitHub repo, powered by open-source Llama 3.1 405B.

- **2024-07-25** | [Pau Labarta Bajo](https://x.com/paulabartabajo_/status/1815990574580699209) | general
  [Post deleted/unavailable]

- **2024-07-24** | [Akshay](https://x.com/akshay_pachaar/status/1816088785152848028) | agent-design, research
  A tutorial thread on building a 100% local RAG app using Meta's Llama 3.1.

- **2024-07-10** | [Matt Pocock](https://x.com/mattpocockuk/status/1811332713107923156) | dev-practices
  A take on pre-commit hooks: Matt Pocock prefers 'fewer guard rails, more safety nets'—favoring tooling that catches problems after the fact over friction that blocks commits up front.

### Jun 2024

- **2024-06-18** | [curvedinf](https://github.com/curvedinf/dir-assistant) | agent-design, dev-practices, research, claude-code
  dir-assistant is a pip-installable CLI that recursively indexes the text files in your directory so you can chat with them via a local or API LLM, auto-injecting the most contextually relevant files. It uses CGRAG (Contextually Guided RAG) for file selection, supports interactive and single-prompt modes (including auto file edits + git commits), many local acceleration backends and all major LLM APIs via LiteLLM, and optimizes prompt/context caching (50-90% cache hits).

- **2024-06-11** | [Santiago](https://x.com/svpino/status/1800151091461652740) | research, general
  A 15-part thread giving an intuitive explanation of matrix multiplication as the crucial idea underlying modern machine learning.
