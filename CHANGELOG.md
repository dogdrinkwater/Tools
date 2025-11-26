# Changelog

All notable changes to the "GitLab Pipeline Monitor" plugin will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.2] - 2025-11-26

### Added
- 🎉 **Merge Request Integration** - Complete MR management with list view, detail panel, and drag-resizable split panes
- 🔔 **Desktop Notifications** - Automatic balloon notifications when user-created pipelines complete (success/failed/canceled) with one-click navigation to view results
- ⬅️➡️ **Job Log Navigation** - Previous/Next buttons in job log viewer for easy sequential browsing through all pipeline jobs (sorted by creation time)
- 📊 **Enhanced MR Details** - Comprehensive merge request information display including:
  - Assignee with avatar (or "Unassigned" indicator)
  - Author information
  - Merge status (merged/open with merge actor details)
  - Source and target branches
  - Created and updated timestamps
  - MR description
  - Direct "Open in GitLab" browser integration
- 🔄 **Unified Tab Interface** - Seamless tab-based navigation between Pipelines and Merge Requests with:
  - Independent refresh mechanisms
  - Separate selection states maintained across tab switches
  - Visual loading indicators for both tabs
- ↔️ **Resizable Panels** - Drag-to-resize JSplitPane dividers for both pipeline and MR views to customize workspace layout
- 🎯 **Pipeline Tracking Service** - Background monitoring service that:
  - Automatically tracks pipelines created by the user
  - Polls pipeline status every 10 seconds
  - Shows desktop notification on completion
  - Provides one-click navigation to completed pipeline
  - Properly cleans up resources via Disposable interface
- 🛠️ **Renamed Tool Window** - Changed from "GitLab Pipelines" to "GitLab Toolkit" to reflect expanded functionality

### Changed
- Improved auto-refresh behavior with visual loading states for better user feedback
- Enhanced pipeline detail refresh to only update status/jobs without rebuilding entire UI
- Optimized MR list loading with proper retry logic and error handling

### Fixed
- Pipeline detail auto-refresh now correctly stops when pipeline reaches terminal state
- Job log viewer properly stops refresh timer when dialog is closed
- Proper resource cleanup for notification monitoring service via Disposable implementation

### Technical
- Added `PipelineNotificationService` as project-level service implementing Disposable
- Added `UnifiedGitLabPanel` with JTabbedPane for Pipelines and Merge Requests tabs
- Added `MergeRequestListPanel` for MR display and management
- Implemented notification group "GitLabPipelineNotifications" for desktop alerts
- Enhanced logging with console println statements for better debugging visibility

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
- **Supported IDE Versions**: IntelliJ IDEA 2024.2 - 2025.2.*
- **Minimum Requirements**: Java 17, GitLab API v4

---

[1.1.2]: https://github.com/dogdrinkwater/gitlab-pipeline-plugin/releases/tag/v1.1.2
[1.0.1]: https://github.com/dogdrinkwater/gitlab-pipeline-plugin/releases/tag/v1.0.1
[1.0.0]: https://github.com/dogdrinkwater/gitlab-pipeline-plugin/releases/tag/v1.0.0

