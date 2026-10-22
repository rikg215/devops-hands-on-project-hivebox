[![Hivebox-CI](https://github.com/rikg215/devops-hands-on-project-hivebox/actions/workflows/Hivebox-CI.yaml/badge.svg)](https://github.com/rikg215/devops-hands-on-project-hivebox/actions/workflows/Hivebox-CI.yaml)

[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/rikg215/devops-hands-on-project-hivebox/badge)](https://scorecard.dev/viewer/?uri=github.com/rikg215/devops-hands-on-project-hivebox)

[![Dynamic DevOps Roadmap](https://img.shields.io/badge/Dynamic_DevOps_Roadmap-559e11?style=for-the-badge&logo=Vercel&logoColor=white)](https://devopsroadmap.io/getting-started/)
[![Community](https://img.shields.io/badge/Join_Community-%23FF6719?style=for-the-badge&logo=substack&logoColor=white)](https://newsletter.devopsroadmap.io/subscribe)
[![Telegram Group](https://img.shields.io/badge/Telegram_Group-%232ca5e0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/DevOpsHive/985)
[![Fork on GitHub](https://img.shields.io/badge/Fork_On_GitHub-%2336465D?style=for-the-badge&logo=github&logoColor=white)](https://github.com/DevOpsHiveHQ/devops-hands-on-project-hivebox/fork)

# HiveBox - DevOps End-to-End Hands-On Project

<p align="center">
  <a href="https://devopsroadmap.io/projects/hivebox" style="display: block; padding: .5em 0; text-align: center;">
    <img alt="HiveBox - DevOps End-to-End Hands-On Project" border="0" width="90%" src="https://devopsroadmap.io/img/projects/hivebox-devops-end-to-end-project.png" />
  </a>
</p>

This repository is the starting point for [HiveBox](https://devopsroadmap.io/projects/hivebox/), the end-to-end hands-on project.

You can fork this repository and start implementing the [HiveBox](https://devopsroadmap.io/projects/hivebox/) project. HiveBox project follows the same Dynamic MVP-style mindset used in the [roadmap](https://devopsroadmap.io/).

The project aims to cover the whole Software Development Life Cycle (SDLC). That means each phase will cover all aspects of DevOps, such as planning, coding, containers, testing, continuous integration, continuous delivery, infrastructure, etc.

Happy DevOpsing ♾️

---

## Implementation

### Phase 1: Planning

**Methodology:** Kanban, tracked with [HiveBox project board](https://github.com/users/rikg215/projects/4)

**senseBox IDs:**

| senseBoxID | Link |
|---|---|
| `5eba5fbad46fb8001b799786` | [openSenseMap](https://opensensemap.org/explore/5eba5fbad46fb8001b799786)
| `5c21ff8f919bf8001adf2488` | [openSenseMap](https://opensensemap.org/explore/5c21ff8f919bf8001adf2488)
| `5ade1acf223bd80019a1011c` | [openSenseMap](https://opensensemap.org/explore/5ade1acf223bd80019a1011c)


### Phase 2: Basics

#### Testing

```bash
docker build -t "app-test:v0.0.1" .
docker run --name "app-test" app-test:v0.0.1
```
**EXPECTED OUTPUT**

`v0.0.1`

### Phase 3: Laying the Base

#### Testing

```bash
uv sync
uv run pytest
```

