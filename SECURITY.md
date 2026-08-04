# Security Policy

## Supported Versions

| Version | Supported |
|---------|-----------|
| v12.x   | ✅ Active support |
| v11.x   | ⚠️ Critical fixes only |
| < v11   | ❌ No longer supported |

---

## Reporting a Vulnerability

**Please do NOT report security vulnerabilities via public GitHub Issues.**

If you discover a security vulnerability in AEGIS-Core, please report it responsibly:

### Option 1: GitHub Private Advisory (Preferred)
1. Go to [Security Advisories](https://github.com/wahyunuriman999/AEGIS-Core/security/advisories)
2. Click **"Report a vulnerability"**
3. Fill in the details

### Option 2: Email
Send a detailed report to: **wahyunuriman999@gmail.com**

Subject format: `[SECURITY] AEGIS-Core — <brief description>`

---

## What to Include in Your Report

- **Description**: Clear explanation of the vulnerability
- **Impact**: What an attacker could achieve
- **Steps to Reproduce**: Minimal reproduction steps
- **Affected Version**: Which version(s) are affected
- **Suggested Fix**: If you have one (optional but appreciated)

---

## Response Timeline

| Step | Target Time |
|------|-------------|
| Acknowledgement | Within 48 hours |
| Initial assessment | Within 5 business days |
| Fix or mitigation | Within 30 days (critical: 7 days) |
| Public disclosure | After fix is released |

---

## Scope

**In scope:**
- Arbitrary code execution via AEGIS pipeline
- Path traversal in Knowledge Compiler or Runtime
- Secrets leakage via `FAILURE_DB.json`, `runtime_trace.json`, or logs
- Dependency vulnerabilities in `requirements.txt`

**Out of scope:**
- Social engineering
- Denial of service via resource exhaustion in development/local mode
- Issues in dependencies themselves (report to upstream)

---

Thank you for helping keep AEGIS-Core safe. 🙏
