# Python-Devops

A structured, project-based Python learning journey focused on building real-world skills in DevOps, Cloud Engineering, and AI/LLM development.

Each chapter introduces core Python concepts through hands-on projects rooted in IT and infrastructure contexts — reflecting a background in network and systems support and a goal of transitioning into DevOps and AI engineering roles at scale.

---

## About

Currently working as an IT Network Support Specialist, I am systematically building Python proficiency with a focus on automation, cloud tooling, and AI integration. This repository documents that journey — one chapter, one project at a time.

**Target roles:** DevOps Engineer · Cloud Engineer · AI/ML Engineer · IAM & Security Engineer

---

## Roadmap

| Chapter | Topic | Project | Status |
|---------|-------|---------|--------|
| 01 | Python Foundations | Server Config Manager | ✅ Complete |
| 02 | Data Structures | Network Device Inventory | 🔄 In Progress |
| 03 | Files, Errors & Modules | Log Analyzer | 🔒 Locked |
| 04 | OOP Basics | IT Ticket System | 🔒 Locked |
| 05 | APIs & HTTP | IP Lookup & Alert Tool | 🔒 Locked |
| 06 | Automation & Scripting | System Health Monitor | 🔒 Locked |
| 07 | Python for AI & LLMs | IT Support Chatbot | 🔒 Locked |
| 08 | Cloud & DevOps Integration | Cloud Infra Auditor | 🔒 Locked |

---

## Projects

### Chapter 01 — Server Config Manager
**Concepts:** Variables, data types, user input, conditionals, loops, functions

A command-line tool that stores and manages server configuration settings. Users can view the current config, update individual settings, and check what service runs on a given port number — all through an interactive menu loop.

**Skills demonstrated:** Function design, dictionary manipulation, input handling, while loop control flow

---

### Chapter 02 — Network Device Inventory *(in progress)*
**Concepts:** Lists, dictionaries, tuples, sets, list comprehensions, nested data structures

A CLI-based inventory system for managing network devices — routers, switches, firewalls — with the ability to add, search, filter, and display devices by type or status.

**Skills demonstrated:** Nested dictionaries, list comprehensions, data filtering, structured output

---

### Chapter 03 — Log Analyzer *(upcoming)*
**Concepts:** File I/O, error handling, os module, json, regex basics

Parses real server log files, counts occurrences of error types, and exports a structured summary report.

---

### Chapter 04 — IT Ticket System *(upcoming)*
**Concepts:** Classes, objects, `__init__`, inheritance, encapsulation

An OOP-based support ticket system where tickets can be created, assigned, escalated, and resolved through defined class structures.

---

### Chapter 05 — IP Lookup & Alert Tool *(upcoming)*
**Concepts:** `requests` library, REST APIs, JSON parsing, `.env` secrets

Queries public threat intelligence APIs to look up IP reputation, flags suspicious addresses, and sends alerts.

---

### Chapter 06 — System Health Monitor *(upcoming)*
**Concepts:** `subprocess`, `argparse`, `schedule`, CLI design

Automatically checks CPU, memory, and disk usage on a schedule and triggers email alerts when thresholds are exceeded.

---

### Chapter 07 — IT Support Chatbot *(upcoming)*
**Concepts:** Anthropic/OpenAI SDK, prompt engineering, streaming, conversation memory

An AI-powered chatbot that answers network and IT support questions using an LLM API, with persistent conversation context.

---

### Chapter 08 — Cloud Infra Auditor *(upcoming)*
**Concepts:** `boto3` (AWS SDK), Azure SDK, Docker via Python, `pytest`

Scans AWS and Azure resources for misconfigurations, flags security gaps, and generates a structured audit report.

---

## Tech Stack

- **Language:** Python 3.x
- **Tools:** VS Code, Git, GitHub
- **Libraries (progressive):** `requests`, `os`, `json`, `subprocess`, `boto3`, Azure SDK, OpenAI/Anthropic SDK
- **Platforms:** AWS, Azure, Docker

---

## Structure

```
Python-Devops/
├── ch_01_foundations/
│   └── server_config_manager.py
├── chapter-02-data-structures/
│   └── network_device_inventory.py
├── chapter-03-files-errors/
├── chapter-04-oop/
├── chapter-05-apis/
├── chapter-06-automation/
├── chapter-07-llm/
├── chapter-08-cloud/
└── README.md
```

---

*Updated progressively as each chapter is completed.*