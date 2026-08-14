# ste — security vetting record

**Verdict: CLEAN.** No prompt injection, no exfiltration, no tool or permission escalation. Safe to install.

- **Vetted:** 2026-08-14
- **Received:** email attachment `ste.zip` from Ruben Hassid, obtained by signing up with an email address to get a skill he promoted on X
- **Related post:** `2087856703773508025` — "Post by Ruben Hassid on X (add to review)"
- **Treated as:** untrusted third-party input. Static inspection only; nothing in the archive was executed.

## Provenance of the artifact

| File | SHA-256 |
|---|---|
| `ste.zip` (as received) | `414ea5203634db1f2a02c5eabc8736d435e34ac71164603f075e5f1be4bfd5b9` |
| `SKILL.md` | `258ef722268d786b5adaa471aa61db848a3bd6554a52ed32b87f29d18c318580` |
| `references/examples.md` | `0e05e0916da918631d9b6a907b8f1552eedd234321039b998fc3601984d2a81b` |
| `references/word-substitutions.md` | `b1d030266b05d6093bded85ac5f0f26448ac6d1ac6d00d1eb546068a85aad18d` |

The original archive is kept verbatim as `ste.zip.original` so these hashes stay checkable. The unpacked copies here are byte-identical to what came out of it.

## What was checked

**Archive structure.** Ten entries, of which three are real files and the rest are macOS `__MACOSX` resource forks. All paths stay under `ste/` — no path traversal (`../`), no absolute paths, no symlinks. No executables, no scripts, no binaries: three UTF-8 markdown files totalling ~12 KB. Archive integrity test passed.

**Hidden content.** Zero invisible or format characters (checked the zero-width set, bidi overrides, BOM, soft hyphen, and every Unicode `Cf` category character). The only non-ASCII characters in the whole payload are `—` and `→`. No base64-shaped blobs of 40+ characters, no HTML comments, no `<script>`/`<iframe>`, no `data:` URIs, no event handlers.

**Injection and escalation.** Grepped for instruction-override patterns ("ignore previous", "disregard", "system prompt", "you are now", jailbreak), credential language (API key, token, password, secret, `.env`), and anything tool-shaped (`curl`, `wget`, `fetch(`, `subprocess`, `os.system`, `eval(`, `exec(`, `chmod`, `sudo`, send/upload/exfil). One hit, and it is a false positive: an example sentence in `examples.md` demonstrating a rewrite — "Perform a compression of the log files prior to upload." That is style content, not an instruction.

**Network surface.** Exactly one external domain appears anywhere in the payload: `asd-ste100.org`, the official home of the standard, cited in an honest compliance note. The skill never instructs the model to fetch it or anything else.

**Scope of effect.** The skill only shapes prose style. It requests no tools, reads no files outside its own `references/` directory, touches no settings, and asks for no data about the user. Its blast radius is the wording of text in a chat where it was deliberately invoked.

## Notes in the skill's favour

The `description` frontmatter is unusually well-scoped: it insists on explicit invocation (`/ste` or naming the skill) and *specifically* tells the model not to trigger on paraphrased intent like "simplify this" or "make it clearer". Malicious or attention-grabbing skills want the opposite — the broadest possible trigger surface. Narrow self-scoping is a good-faith signal.

The copyright note is honest and legally careful. ASD owns the copyright on ASD-STE100; the skill says so, states plainly that it encodes paraphrased rules and a publicly sourced word list rather than the official ~900-word dictionary, points to the free official specification, and instructs the model to never claim certified compliance. That is what a careful author writes and what a sloppy or bad-faith one omits.

## One thing to be aware of

`SKILL.md` tells the model: "Do not announce that you use STE, do not name the standard, and do not explain the style unless the user asks." Read cold, an instruction not to disclose its own operation deserves a second look. In context it is benign — it is suppressing chatty meta-commentary in the output, the same as any house-style guide, and it applies only in a chat where the skill was deliberately invoked. It does not conceal anything from the person who turned it on. Worth knowing rather than worth worrying about.

## Claim verification

The standard is real and the skill's description of it is accurate. ASD-STE100 Simplified Technical English is maintained by the AeroSpace and Defence Industries Association of Europe; Issue 9 was released 15 January 2025 and comprises 53 writing rules plus a controlled dictionary of roughly 900 approved words. The official specification is downloadable free from asd-ste100.org. The specific rules the skill encodes — 20-word procedural and 25-word descriptive sentence caps, one word/one meaning/one part of speech, restricted verb forms with no `-ing` verbs, command-before-risk warning structure, three-word noun-cluster limit — match the real standard.

Ruben's operational claims were not independently tested: that Skills require Capabilities → file creation to be enabled before the menu appears, and that the same zip works in ChatGPT.

**The concept is not unique to this zip.** At least two independent open-source ASD-STE100 skills exist on GitHub (`nuelcyoung/asd-ste100`, `danyuchn/asd-ste100-skill`), plus listings on skill marketplaces. Their file layouts differ from this one — `nuelcyoung` ships `dictionary.md`/`checklist.md`/`background.md` against this zip's `examples.md`/`word-substitutions.md` — so this appears to be Ruben's own build rather than a repackage. If provenance ever matters more than convenience, a public repo with visible commit history is a stronger supply chain than an emailed attachment behind an email-capture form.

## Caveats on use

Ruben's own warning is sound and worth repeating: this is built on a standard for aerospace maintenance manuals. It is good for instructions, documentation, and explanation, and bad for anything that needs warmth or voice — poems, jokes, social posts. It will make those read like a fridge manual.

Do not use it for certified aerospace or defence deliverables. The word list here is a public approximation, not the official ASD dictionary, and real compliance needs the official specification plus human sign-off. The skill says this itself.

## Re-vetting

If a newer version of this skill arrives, diff it against the hashes above before trusting it. A clean audit of one version says nothing about the next.
