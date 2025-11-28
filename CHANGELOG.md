# Changelog

All notable changes to the "GitLab Pipeline Monitor" plugin will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.2] - 2025-11-28

### Added
- 🎉 **Merge Request Workspace** – brand-new MR tab (list + details) with drag-resizable layout, assignee/author metadata, browser deeplinks, and a GitLab Toolkit setting that lets teams hide the tab when they only care about pipelines.
- 🔔 **Pipeline Completion Notifications** – project-level `PipelineNotificationService` watches every pipeline you trigger, polls GitLab, and surfaces balloon notifications with one-click navigation when runs finish (success, failed, canceled).
- ⬅️➡️ **Job Log Navigation** – Previous/Next controls inside the job log dialog so you can review an entire pipeline without reopening the viewer; ordering follows job creation time for clarity.
- ⚙️ **Configurable MR Visibility** – Settings → Tools → GitLab Toolkit now includes a *Merge Requests list display* checkbox so workspaces can opt out of MR tooling entirely.

### Changed
- 🛠️ **GitLab Toolkit window** replaces the former pipelines-only tool window and keeps Pipelines/Merge Requests in sync with independent refresh + selection states.
- 🔄 Pipeline detail refresh now updates status, variables, and jobs incrementally (no more full repaint) and shows visual loading states during manual refreshes.
- ↔️ Both pipeline and MR panes use consistent JSplitPane resizing so you can dedicate more space to whichever panel you are actively using.

### Fixed
- Auto-refresh timers correctly stop once a pipeline reaches a terminal status, preventing unnecessary polling or UI churn.
- Job log dialog now tears down its internal refresh timer when you close it, eliminating the lingering background work seen in 1.0.1.
- Merge Requests tab initialization logic ensures only a single tab is ever created, even after toggling the new visibility preference.

### Technical
- Introduced `UnifiedGitLabPanel` (tabbed pipeline + MR UI) and `MergeRequestListPanel` UI components.
- Added `PipelineNotificationService` as a project-level service implementing `Disposable` for clean shutdown.
- Extended `GitLabSettingsState`/`GitLabSettingsConfigurable` with the merge-request visibility flag to persist the new preference.

---

## [1.0.1] - 2025-11-24

### Added
- ✅ GitHub Actions workflow that builds the plugin on every push to `main`, automatically tags releases, and publishes GitHub releases whenever the plugin version changes.
- 🛡️ `GitLabVariable` now tracks whether user input is required, allowing the new pipeline dialog to enforce validation only when `.gitlab-ci.yml` does not define a default value.
- ⛔ Cancel Pipeline button that lets you stop running/pending pipelines directly from the IDE before retrying.

### Fixed
- Ensured pipeline variable validation matches the default value semantics from `.gitlab-ci.yml`, preventing unnecessary errors when defaults exist.

---

## [1.0.0] - 2025-11-21

### Added
- 🎉 **Initial Release** - First public version of GitLab Pipeline Monitor

#### Pipeline Management
- Real-time pipeline monitoring with auto-refresh support (configurable: 5s to 1hr or disabled)
- Create new pipelines directly from IDE with branch detection
- One-click pipeline retry with original variables preserved
- Infinite scroll for seamless loading of large pipeline histories
- Smart selection persistence - maintains selected pipeline across refreshes

#### Variable Management
- Automatic `.gitlab-ci.yml` variable parsing with options support
- Smart variable parser extracts all configurable variables
- Dropdown UI for easy variable selection during pipeline creation
- Variable preservation on pipeline retry

#### Job Log Viewer
- Advanced job log viewer with full ANSI color rendering (colors, bold, italic, underline)
- Real-time log streaming with 5-second auto-refresh for running jobs
- Auto-scroll feature to follow live log output
- Raw log toggle to view ANSI escape codes
- Job status detection (running, success, failed, etc.)
- Automatic refresh stop when job completes

#### Project Management
- Auto-star workflow for unstarred projects
- Intelligent project detection with one-click starring dialog
- Support for both starred and newly-discovered projects

#### User Interface
- Comprehensive pipeline details view (variables, jobs timeline, status, duration)
- Job timeline sorted by creation time for logical flow
- Visual status indicators with icons and colors
- Browser integration - quick jump to GitLab UI
- Split-pane layout for pipeline list and details
- Configurable settings panel (GitLab URL, token, refresh interval)

#### Technical Features
- Support for IntelliJ IDEA 2024.2+ (build 242 to 252.*)
- Performance optimized with lazy loading and pagination
- Thread-safe operations with background processing
- Comprehensive error handling and user feedback
- Compatible with self-hosted GitLab and GitLab.com

### Technical Details
- Minimum IDE version: 2024.2 (build 242)
- Maximum IDE version: 2025.2.* (build 252.*)
- Java/Kotlin compatibility: JVM 17
- Dependencies: OkHttp 4.12.0, Gson 2.10.1, SnakeYAML 2.2

---

## Future Roadmap

### Planned for v1.2.0
- Multi-project monitoring dashboard
- Custom filters for pipelines and MRs (by branch, author, status)
- Pipeline comparison view
- MR approval workflow integration
- Inline commenting on merge requests

### Under Consideration
- GitLab Runner status monitoring
- Pipeline metrics and statistics dashboard
- Export pipeline history
- Custom ANSI color schemes
- Keyboard shortcuts customization
- Commit message integration
- Issue tracking integration

---

## Version Support Policy

- **Current Version**: 1.1.2
- **Supported IDE Versions**: IntelliJ IDEA 2022.3 - 2025.2.*
- **Minimum Requirements**: Java 17, GitLab API v4

---

## ☕ Support the Project

<p align="center">
  <img src="alipay.jpg" alt="Donate via Alipay" width="260px" height="400px" style="max-width:100%;margin:0 12px;" />
  <img src="wechatpay.png" alt="Donate via WeChat Pay" width="260px" height="400px" style="max-width:100%;margin:0 12px;" />
</p>

---

[1.1.2]: https://github.com/dogdrinkwater/gitlab-pipeline-plugin/releases/tag/v1.1.2
[1.0.1]: https://github.com/dogdrinkwater/gitlab-pipeline-plugin/releases/tag/v1.0.1
[1.0.0]: https://github.com/dogdrinkwater/gitlab-pipeline-plugin/releases/tag/v1.0.0

