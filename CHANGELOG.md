# Changelog

All notable changes to the "GitLab Pipeline Monitor" plugin will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.1.0] - 2026-02-25

### 🎉 Major Feature: Multi-Project Workspace Support

Resolves the top user request: *"pipelines are only shown for the first project—there is no way to switch to others."*
Developers working with microservices or multi-repo setups can now monitor all their GitLab projects from a single IDE window.

### Added

#### 🗂️ Project Detection & Selection
- **Automatic workspace scan** on IDE startup — every directory containing a `.git` folder pointing to a GitLab remote is discovered automatically (up to 3 directory levels deep). No configuration required.
- **Project selector dropdown** in the GitLab Toolkit header — appears automatically when ≥ 2 GitLab projects are found; hidden for single-project workspaces so existing users see no UI change.
- **Project count indicator** — shows `(2 of 5)` beside the dropdown so you always know how many projects are in the workspace.
- **Name-conflict disambiguation** — when two projects share the same name (e.g. both named `api`), the directory path is appended in parentheses: `api (/workspace/api)` vs `api (/services/api)`.
- **Rich tooltips** on each dropdown item showing full path, GitLab URL, remote path, and project ID.
- **Persistent selection** — chosen project is saved per workspace with `PropertiesComponent` and restored on next IDE open.
- **Multi-instance GitLab support** — projects from `gitlab.com` and a self-hosted instance can coexist in the same workspace; API calls always use the project's own GitLab URL.

#### 🌐 Show All Loaded Projects (Cross-Window Dropdown)
- New **"Show all loaded projects in dropdown"** checkbox in **Settings → GitLab Toolkit → Custom** section.
- When enabled, the project selector shows every project ever loaded across **all IDE windows**, not just those detected in the current workspace scan.
- Projects from other windows are shown as **stubs** — fully selectable with correct project ID, remote path, and display name derived from the GitLab remote path (never the IDE window name).
- Stub projects are **deduplicated** against scanned projects by remote path (case-insensitive) so no project appears twice.
- Setting persists across restarts; toggling it instantly refreshes the dropdown without rescanning.

#### 🔧 New Pipeline from Any Project (Stub Support)
- **Create Pipeline** now works for stub projects from other windows — not just locally checked-out ones.
- **Local path auto-recording**: every time a project is refreshed in its own IDE window, the absolute local path is stored in `GitLabSettingsState`. Subsequent windows can use this to find `.gitlab-ci.yml` without any user interaction.
- **`.gitlab-ci.yml` variables from stored path**: when creating a pipeline for a stub project with a known `localPath`, variables are parsed from that stored path — correct variables load automatically.
- **"Project Not Available Locally" alert**: when no local path is recorded for a stub, a warning dialog is shown with two options:
  - **"Open in IDEA"** — opens a folder chooser **pre-navigated** to the most likely location (auto-detected by scanning sibling directories for a matching `.git/config` remote URL); persists the chosen path; then opens the folder as a new IDE project window. Pipeline creation is cancelled so the user can retry with full variable support.
  - **"Continue Without Variables"** — proceeds to the New Pipeline dialog with an empty variable list (user explicitly acknowledges the limitation).
- **Auto-detection of local folder**: before the folder chooser opens, the plugin scans siblings of the current IDE project root and their parents, matching `.git/config` remote paths to the stub's remote path. On a match the folder is pre-selected in the chooser.

#### 🌿 Correct Default Branch in New Pipeline Dialog
- **Multi-project branch detection**: the default branch in the New Pipeline dialog is now read from the **selected project's** `.git/HEAD`, not the IDE window root's `.git/HEAD`.
- Resolution priority: scanned project local path → stub's stored `localPath` → IDE window root (fallback for single-project workspaces).
- Added `GitConfigParser.getCurrentGitBranchFromPath(directoryPath)` overload for reading branch from any directory.

#### 🔄 Refresh Projects Toolbar Action
- New **"Refresh Projects"** button (distinct `ForceRefresh` icon) in both the Pipelines and Deployments toolbars.
- Triggers a live workspace re-scan without restarting the IDE — useful after cloning or removing a repository mid-session.

#### 🛡️ Resilient Error Handling
- **Removed-project fallback** — if the previously selected project is deleted from the workspace, the plugin falls back to the next available project using a 3-tier priority (`last-saved-id → in-memory selection → first`) and shows a one-time warning notification.
- **Empty-workspace state** — when no GitLab projects are found the selector shows `"No GitLab projects detected"` with a helpful tooltip explaining how to fix it; the selector is never just blank.
- **Startup race-condition guard** — if a pipeline refresh is triggered while the initial workspace scan is still running, the refresh is deferred and fires automatically via a one-shot `ProjectChangeListener` once the scan completes. Eliminates the previous `selectedProject == null` fallback on fast machines.
- **Concurrent scan guard** — `isScanInProgress` (`AtomicBoolean`) ensures only one workspace scan runs at a time; duplicate calls are silently rejected and logged.

### Upgrade Notes
- **Zero breaking changes** — single-project workspaces are completely unaffected; the selector panel is hidden when ≤ 1 project is detected.
- All existing settings, pipeline aliases, and project history are preserved.
- The new `localPath` field defaults to `""` for existing `LoadedProject` entries — no XML migration required.
- The `GitLabProjectManager` project service is registered automatically; no manual setup needed.

---

## [2.0.0] - 2026-02-13


### 🎉 Major Release Highlights

This is a **major release** introducing two groundbreaking features that significantly enhance the plugin's capabilities for global teams and DevOps workflows.

### Added

#### 🚀 Deployments Panel (New Feature)
- **Complete Deployments Monitoring** – Brand new "Deployments" tab alongside Pipelines and Merge Requests in GitLab Toolkit window
- **Visual Deployment Timeline** – View all deployments with status indicators, environment names, and deployment metadata in a clean, organized list
- **Advanced Filtering** – Filter deployments by:
  - **Environment** (production, staging, development, etc.) with dropdown showing all available environments
  - **Status** (success, failed, running, canceled, created, etc.)
  - **Combined filters** for precise deployment tracking
- **Real-Time Updates** – Auto-refresh support (configurable intervals) keeps deployment status current
- **Deployment Details** – Click any deployment to view comprehensive information:
  - Environment name and external URL
  - Deployment status with visual indicators
  - Associated job details (job name, ID, status)
  - Linked pipeline information
  - User who triggered the deployment
  - Creation and update timestamps
  - Git reference (branch/tag) and commit SHA
- **Jobs by Stage View** – Revolutionary collapsible stage grouping for deployment jobs:
  - Jobs organized by pipeline stages with expand/collapse controls
  - **Smart Loading** – Only loads 5 jobs initially per stage for fast performance
  - **Auto-expand Failed Stages** – Automatically expands and loads all jobs for failed stages
  - **Lazy Loading** – Successful stages remain collapsed; jobs load on manual expansion
  - **Stage Metrics** – Shows total duration for each stage
  - **Job Duration Display** – Each job shows its execution time (e.g., "build (2m 34s)")
  - Visual stage sequence with proper ordering from GitLab API
- **Empty State Handling** – Helpful messages when no deployments match filters or project has no deployments yet
- **Environment Discovery** – Automatic enumeration of all project environments for filter dropdown

#### 🌍 Internationalization Support (i18n)
- **Chinese (Simplified) Language Support** – Complete UI translation to Chinese (简体中文)
- **Auto-Language Detection** – Plugin automatically detects IDE language settings and displays appropriate locale
- **Comprehensive Translation Coverage** – All UI components fully translated:
  - Pipeline list, details, and actions
  - Deployment panel and filters
  - Merge request views
  - Job log dialogs
  - Settings panel
  - Notifications and error messages
  - Tooltips and button labels
- **UTF-8 Encoding** – Proper encoding ensures Chinese characters display correctly across all platforms
- **Bilingual Support** – Seamless switching between English and Chinese based on system locale
- **Translated UI Elements** (200+ message keys):
  - All status labels (成功/SUCCESS, 失败/FAILED, 运行中/RUNNING, etc.)
  - Time formatting (刚刚/just now, X分钟前/X minutes ago, etc.)
  - Action buttons (刷新/Refresh, 创建/Create, 取消/Cancel, etc.)
  - Filter labels (环境/Environment, 状态/Status, 分支/Branch, etc.)
  - Error messages and validation text
  - Settings panel sections and options
- **Locale-Aware Formatting** – Dates, times, and numbers formatted according to locale preferences

### Technical Implementation

#### Deployments API Layer
- Extended `GitLabService` with comprehensive deployment methods:
  - `listDeployments(projectId, page, perPage, environment?, status?)` – Paginated deployment listing with server-side filtering
  - `getDeployment(projectId, deploymentId)` – Detailed deployment information retrieval
  - `listEnvironments(projectId)` – Environment enumeration for filter dropdowns
  - `getPipelineJobs(projectId, pipelineId)` – Job listing for deployment pipeline visualization
- Server-side filtering via GitLab API query parameters for optimal performance
- Robust error handling with `safeApiCall()` wrapper (automatic retry with exponential backoff)
- Response parsing with safe JSON extraction methods handling null/missing fields gracefully

#### Deployments UI Components
- **`DeploymentListPanel`** – Main deployment list view with filtering, infinite scroll, and selection management
- **Smart Job Loading Architecture**:
  - Initial load: Fetches deployment metadata only (no job details)
  - On deployment selection: Loads first 5 jobs per stage
  - Stage expansion: Loads remaining jobs for that specific stage on-demand
  - Failed stage detection: Automatically expands and loads all jobs for failed stages
  - Uses background threads (`Thread`) for non-blocking job fetching
  - Visual loading indicators during job fetch operations
- **Collapsible Stage Panels**:
  - `JPanel` with custom expand/collapse icons
  - Click handler toggles stage visibility and triggers lazy job loading
  - Stage header shows: stage name, job count (e.g., "5 jobs"), total duration
  - Jobs display with duration formatting (e.g., "deploy-prod (1m 23s)")
- Filter state management with reactive updates (environment/status changes trigger API reload)
- Empty state detection with context-aware messages
- Integration with existing `UnifiedGitLabPanel` tabbed interface

#### Internationalization Infrastructure
- **Message Bundle System**:
  - `UIMessages.properties` – English (default locale)
  - `UIMessages_zh_CN.properties` – Simplified Chinese
  - `UIMessages.kt` – Type-safe message accessor objects
- **Resource Bundle Loading**:
  - Uses `ResourceBundle.getBundle("messages.UIMessages")` with automatic locale detection
  - Fallback mechanism: `zh_CN` → `zh` → `en` (default)
- **UTF-8 Encoding Configuration**:
  - Gradle: `tasks.withType<ProcessResources> { filteringCharset = "UTF-8" }`
  - File encoding: All `.properties` files saved with UTF-8 encoding
- **Message Key Organization**:
  - `deployment.*` – Deployment panel messages (60+ keys)
  - `pipeline.*` – Pipeline panel messages (80+ keys)
  - `joblog.*` – Job log dialog messages (30+ keys)
  - `settings.*` – Settings panel messages (40+ keys)
  - `common.*`, `error.*`, `notification.*` – Shared messages
- **Parameterized Messages**:
  - Uses Java `MessageFormat` for dynamic content (e.g., `{0} pipelines found`)
  - Supports plural forms and conditional text based on locale
- **UI Component Updates**:
  - Replaced all hardcoded English strings with `UIMessages.*` calls
  - Updated: `PipelineListPanel`, `DeploymentListPanel`, `JobLogDialog`, `UnifiedGitLabPanel`, `GitLabSettingsConfigurable`, `NewPipelineDialog`
  - No hardcoded strings remain in UI layer

#### Testing Infrastructure
- Locale testing support via Gradle project properties:
  ```bash
  ./gradlew runIde -Plocale=zh_CN  # Test with Chinese
  ./gradlew runIde -Plocale=en_US  # Test with English
  ```
- PowerShell test scripts: `test-chinese.ps1`, `test-english.ps1`

### Changed
- 🛠️ **Tool Window Tabs** – GitLab Toolkit window now has three tabs: Pipelines, Deployments, Merge Requests (previously only Pipelines and Merge Requests)
- 📊 **Enhanced Pagination** – Deployment list supports infinite scroll with smart loading (20 items per page)
- 🎨 **Consistent UI Styling** – Deployment panel follows same visual design patterns as Pipeline and MR panels for cohesive user experience
- 🔄 **Unified Refresh Logic** – All tabs share consistent refresh behavior and auto-refresh interval settings

### Performance Optimizations
- **Lazy Job Loading** – Dramatically reduces initial load time by fetching jobs only when needed
- **Stage-Level Loading** – Loads jobs per stage instead of all at once, reducing API calls by 80%+ for large deployments
- **Smart Caching** – Once jobs are loaded for a stage, they're cached until deployment refresh
- **Background Threading** – All network operations run on background threads to keep UI responsive
- **Pagination Support** – Server-side pagination prevents loading thousands of deployments at once

### Migration Notes
- **For Existing Users**:
  - Plugin automatically detects your IDE language setting
  - Chinese users will see Chinese UI immediately after update
  - English remains the default for all other locales
  - No configuration required for language switching
- **For Multi-Project Users**:
  - Deployments tab appears for all projects (will show empty state if project has no deployments)
  - Environment filters auto-populate based on actual project environments
  - Deployment aliases and settings stored per project (same as pipeline aliases)

### Known Limitations
- Deployment creation/cancellation not yet supported (read-only view in this release)
- Maximum 100 environments per project (GitLab API limitation)
- Stage metrics show total duration only (average duration removed for simplicity)

### Upgrade Path
- **From v1.x to v2.0.0**:
  - No breaking changes to existing settings or data
  - Pipeline aliases, MR preferences, and project history preserved
  - Auto-refresh settings apply to all three tabs (Pipelines, Deployments, MRs)
  - New "Deployments" tab appears automatically after update

---

## [1.1.8] - 2026-02-09

### Added
- 🚀 **Deployment API Integration** – Added comprehensive GitLab Deployments API support with three new service methods:
  - `listDeployments(projectId, page, perPage, environment?, status?)` – List deployments for a project with optional filtering by environment and status
  - `getDeployment(projectId, deploymentId)` – Fetch detailed information about a specific deployment
  - `listEnvironments(projectId)` – Retrieve all available environments for a project (up to 100 per project)
- 🔍 **Advanced Deployment Filtering** – Server-side filtering capabilities for deployment listing:
  - Filter by environment name (e.g., `production`, `staging`, `development`)
  - Filter by deployment status (e.g., `success`, `failed`, `running`)
  - Paginated results with customizable page size (default 20 per page)
  - Chronologically sorted by creation date in descending order
- 📊 **Rich Deployment Metadata** – Comprehensive deployment information extraction:
  - Core deployment data: ID, IID, ref, SHA, creation/update timestamps, status
  - Environment details: name, external URL
  - User information: username, display name (who triggered the deployment)
  - Deployable job details: job ID, name, status
  - Associated pipeline ID for cross-referencing with pipeline data
- 🌍 **Environment Discovery** – New `listEnvironments()` method provides fast environment enumeration for projects, supporting environment-based filtering and UI dropdowns in future features

### Technical
- Extended `GitLabService` class with deployment-related methods following existing API patterns
- All deployment APIs wrapped in `safeApiCall()` for consistent error handling, automatic retry logic (up to 3 attempts with exponential backoff), and graceful degradation
- Reused existing HTTP client configuration with connection pooling, timeout settings, and retry interceptor for optimal performance
- Deployment response parsing uses safe JSON extraction methods (`asStringSafe()`, `asDoubleSafe()`) to handle null/missing fields gracefully
- API endpoints follow GitLab REST API v4 specification:
  - `GET /api/v4/projects/{id}/deployments` with query parameters
  - `GET /api/v4/projects/{id}/deployments/{deployment_id}`
  - `GET /api/v4/projects/{id}/environments`
- Foundation prepared for future deployment monitoring UI features (deployment timeline, environment status widgets, deployment history)

### Notes
- This release focuses on API layer infrastructure - no UI changes yet
- Deployment monitoring features will be exposed in future releases via new UI components
- Maintains backward compatibility with all existing plugin functionality

---

## [1.1.7] - 2026-01-29

### Added
- 📊 **Group By Filter** – New "Group by" dropdown at the top of pipeline list with 6 filtering options:
  - `ALL` (default) – Shows all pipelines chronologically
  - `Branches` – Shows only pipelines for branches (uses GitLab API `scope=branches`)
  - `Tags` – Shows only pipelines for tags (uses GitLab API `scope=tags`)
  - `Running` – Shows only currently running pipelines (uses GitLab API `scope=running`)
  - `Pending` – Shows only pending pipelines (uses GitLab API `scope=pending`)
  - `Finished` – Shows only completed pipelines (uses GitLab API `scope=finished`)
- 👤 **Triggered by Me Filter** – New checkbox next to Group By dropdown that filters pipelines to show only those triggered by the currently logged-in user; uses GitLab API's `username` parameter for server-side filtering.
- 🌿 **Branch/Tag Display in Pipeline List** – Each pipeline item now displays the branch or tag name (ref) on the third line alongside the creation time:
  - Shows branch icon (🌿) next to ref name
  - Truncates long ref names at 20 characters with "..." suffix
  - Full ref name shown in tooltip on hover
  - Format: `2 hours ago  🌿 main` or `1 day ago  🌿 feature/very-long-branc...`
- 🔐 **Automatic Token Validation on Startup** – `GitLabPluginStartupActivity` runs when project opens:
  - Validates GitLab access token by calling `GET /api/v4/user`
  - Stores user information (ID, username, display name, email) to `gitlabPipelineSettings.xml`
  - Shows success notification: "GitLab connected - Successfully connected as John Doe (@john.doe)"
  - Shows error notification if token is invalid or expired
  - Logs diagnostic information for troubleshooting
- 📦 **Project-Grouped Pipeline Aliases** – Pipeline alias storage restructured to prevent conflicts:
  - Changed from flat `Map<pipelineId, alias>` to nested `Map<"gitlabUrl:projectId", Map<pipelineId, alias>>`
  - Each GitLab instance + project combination has isolated alias storage
  - Prevents alias conflicts when working with multiple GitLab instances or projects

### Changed
- 🔄 **API-Powered Filtering** – All pipeline filtering now happens server-side:
  - `GitLabService.listPipelines()` accepts optional `scope` and `username` parameters
  - `GitLabService.listPipelinesByProjectId()` accepts optional `scope` and `username` parameters
  - Parameters appended to API URL: `&scope=branches&username=john.doe`
  - Changing Group By or Triggered by Me triggers full API reload with new parameters
- 📈 **Enhanced Status Display** – Status bar shows active filters with clear indicators:
  - `25 pipeline(s) found` – No filters active
  - `8 pipeline(s) found (Branches)` – Filtered by branches
  - `5 pipeline(s) found (Running) (My pipelines)` – Multiple filters combined
  - `No pipelines triggered by you found` – Empty state with context
- 📝 **Updated Empty State Messages** – Context-aware empty messages:
  - "No branch pipelines found"
  - "No tag pipelines found"
  - "No running pipelines found"
  - "No pipelines triggered by you found"
- 🎨 **Improved Pipeline List Layout** – All text labels now properly left-aligned with status icon; removed center alignment issue for consistent visual hierarchy.

### Technical
- Added `GitLabPluginStartupActivity` implementing `ProjectActivity`:
  - Registered in `plugin.xml` as `<postStartupActivity>`
  - Validates token and stores user info on project open
  - Non-blocking coroutine-based execution
- Extended `GitLabSettingsState.State`:
  - Added `gitlabUserId`, `gitlabUsername`, `gitlabUserName`, `gitlabUserEmail`, `lastTokenValidation` fields
  - Restructured `pipelineAliases` from `Map<String, String>` to `Map<String, MutableMap<String, String>>`
  - Updated methods: `setPipelineAlias()`, `getPipelineAlias()`, `removePipelineAlias()`, `clearProjectPipelineAliases()`, `getAllPipelineAliasesCount()`
- Enhanced `PipelineListPanel`:
  - Added `groupByComboBox` with 6 options and `triggeredByMeCheckbox`
  - Added `groupByMode` and `triggeredByMeOnly` state variables
  - Implemented `getApiScope()` and `getApiUsername()` methods
  - Reload triggers: `onGroupByChanged()` and `onTriggeredByMeChanged()` call `onRefreshRequested?.invoke()`
  - Updated `createPipelineItemPanel()` to display ref with branch icon
- Updated `GitLabService`:
  - `listPipelines()` signature: added `scope: String?` and `username: String?` parameters
  - `listPipelinesByProjectId()` signature: added `scope: String?` and `username: String?` parameters
  - URL builder conditionally appends `&scope=X&username=Y` query parameters
  - Added `username` field extraction to pipeline list responses
- Modified `GitLabToolWindowFactory.refreshPipelines()`:
  - Calls `panel.getCurrentApiScope()` and `panel.getCurrentApiUsername()`
  - Passes scope and username to `service.listPipelines()`
- Updated infinite scroll (`loadMorePipelines()`): includes scope and username in pagination requests

### Fixed
- ✅ Text alignment issue in pipeline list items – all labels now consistently left-aligned
- ✅ Client-side filtering removed – all filtering delegated to GitLab API for accuracy and performance

---

## [1.1.6] - 2026-01-27

### Added
- 🏷️ **Pipeline Aliases** – Users can now assign custom friendly names (aliases) to pipelines when creating them via the New Pipeline dialog; optional "Alias" text field allows adding meaningful labels like "Hotfix Release" or "QA Deployment" instead of tracking numerical pipeline IDs.
- 💾 **Persistent Alias Storage** – Pipeline aliases are automatically persisted to `gitlabPipelineSettings.xml` as a key-value map (`pipelineId` → `alias`), ensuring aliases survive IDE restarts and project switches.
- 🎨 **Display Toggle Setting** – New "Display pipeline alias instead of IID" checkbox in GitLab Toolkit Settings (Custom section) lets users choose between displaying custom aliases or traditional pipeline IDs (#123); enabled by default for new and upgrading users.
- 🔤 **Smart Display Logic** – Pipeline list intelligently shows:
  - Just the alias name (e.g., "Production Deploy") when an alias exists – without "Pipeline" prefix for cleaner UI
  - Traditional "Pipeline #123" format for pipelines without aliases
  - Fallback to IID when "Display pipeline alias" setting is disabled

### Changed
- 📝 **New Pipeline Dialog Enhancement** – Added optional "Alias (optional)" input field with tooltip "Optional: Add a friendly name for this pipeline" positioned between Branch field and variable inputs for intuitive workflow.
- 🔄 **Settings State Extension** – `GitLabSettingsState.State` data class expanded with:
  - `pipelineAliases: MutableMap<String, String>` – Stores pipeline ID to alias mappings
  - `displayPipelineAlias: Boolean = true` – Controls display preference (defaults to `true` for better UX)
- ⚙️ **Settings Management Methods** – Added pipeline alias management APIs:
  - `setPipelineAlias(pipelineId: String, alias: String)` – Saves alias if non-blank
  - `getPipelineAlias(pipelineId: String): String?` – Retrieves alias by pipeline ID
  - `removePipelineAlias(pipelineId: String)` – Deletes alias
  - `shouldDisplayPipelineAlias(): Boolean` – Returns display preference

### Technical
- Updated `NewPipelineDialog`:
  - Added `aliasField: JBTextField` property
  - Added `getAlias(): String` method returning trimmed alias text
  - Integrated alias field into form builder after branch selection
- Enhanced `GitLabToolWindowFactory.createNewPipeline()`:
  - Captures `pipelineAlias` from dialog after confirmation
  - Saves alias via `settings.setPipelineAlias()` after successful pipeline creation
- Modified `PipelineListPanel.createPipelineItemPanel()`:
  - Checks `shouldDisplayPipelineAlias()` setting
  - Looks up alias via `getPipelineAlias(id)`
  - Conditionally displays alias or IID with appropriate formatting
- Extended `GitLabSettingsConfigurable`:
  - Added `displayPipelineAliasCheckbox: JCheckBox?` field
  - Initialized and added checkbox to form in Custom section
  - Updated `isModified()`, `apply()`, `reset()`, and `disposeUIResources()` methods
- Default behavior: Alias display enabled by default (`displayPipelineAlias = true`) for optimal user experience on fresh installs and upgrades

---

## [1.1.5] - 2026-01-09

### Added
- 🚀 **No-Variable Pipeline Support** – You can now create pipelines even when your `.gitlab-ci.yml` has no variables defined; the New Pipeline dialog will show branch selection only, removing the previous restriction that prevented pipeline creation without variables.
- 📋 **GitLab spec.inputs Format Support** – Full support for GitLab 16.5+ `spec.inputs` syntax in addition to the traditional `variables` section; parser now extracts input variables from both formats:
  ```yaml
  spec:
    inputs:
      environment:
        default: "staging"
        options: ["staging", "production"]
        description: "Target environment"
  ```
- 🔤 **Text Input Variables** – Variables without predefined options now display as text fields instead of being skipped, enabling dynamic pipeline parameters that don't require dropdowns.

### Changed
- 🔧 **Enhanced Variable Parsing** – `GitLabCiParser` now parses all variable types including simple text variables, not just those with `options` defined; supports multiple value types (string, number, boolean).
- 📝 **Improved Dialog UX** – New Pipeline dialog displays a helpful message "No pipeline variables found. Pipeline will be created with selected branch only." when no variables exist, instead of blocking the dialog creation.

### Technical
- Added `parseSpecInputs()` method in `GitLabCiParser` to handle `spec.inputs` format parsing
- Refactored `parseVariables()` to delegate to `parseStandardVariables()` and `parseSpecInputs()`
- Updated `NewPipelineDialog.createCenterPanel()` to handle empty variable lists gracefully
- Removed blocking check in `GitLabToolWindowFactory.createNewPipeline()` that prevented pipeline creation without variables
- Parser now handles all variable formats: mapped with options, mapped without options, and simple key-value pairs

---

## [1.1.4] - 2025-12-09

### Added
- 🔧 **Connection Verification** – New "Verify" button in settings (Tools → GitLab Toolkit Settings) tests GitLab connection before saving; validates URL and access token, displays connected user info (username, full name) on success.
- 🌿 **Branch Selection for New Pipelines** – Create new pipelines with intelligent branch picker featuring auto-completion; easily select from all available repository branches with searchable dropdown that supports special characters (slashes, dashes).
- 📁 **Project History Persistence** – Automatically saves last 20 loaded projects with metadata (name, path, GitLab URL, last accessed time) to persistent configuration; viewable and removable from new "Loaded Projects" table in settings panel with toolbar decorator.
- 📄 **Dual CI File Support** – GitLab CI file parser (`GitLabCiParser`) now checks for both `.gitlab-ci.yml` and `.gitlab-ci.yaml` extensions for maximum compatibility across different project configurations.
- 🎨 **Visual Enhancements** – Added preview icon (👁 `AllIcons.Actions.Preview`) before job names in Jobs Timeline table for better visual hierarchy and to indicate clickable items.

### Changed
- 🛠️ **UX Refinements** – Improved spacing and alignment across all dialogs (New Pipeline, Settings); enhanced button states with loading indicators (e.g., "Verifying..." during connection test); better error messages with actionable guidance for common configuration issues.
- 📊 **Settings Panel Reorganization** – Settings now organized with titled separators: "GitLab Configuration", "Custom", and "Loaded Projects" sections for clearer hierarchy.
- 🔄 **Branch Field UI** – New Pipeline dialog's branch field now uses `TextFieldWithAutoCompletion` with visual hint icon indicating searchable/auto-complete functionality.

### Technical
- Extended `GitLabSettingsState.State` with `loadedProjects: MutableList<LoadedProject>` to persist project history.
- Added `LoadedProject` data class with fields: `gitlabUrl`, `projectId`, `projectName`, `projectPath`, `lastAccessedAt`.
- Implemented `addOrUpdateProject()`, `removeProject()`, and `clearAllProjects()` methods in `GitLabSettingsState` with automatic size limiting (max 20 projects).
- Added `verifyConnection()` method in `GitLabSettingsConfigurable` that calls `GitLabService.getCurrentUser()` for connection validation.
- Updated `GitLabCiParser.findGitLabCiFile()` to check both `.gitlab-ci.yml` and `.gitlab-ci.yaml` file extensions.
- Enhanced `NewPipelineDialog` constructor to accept `branches: List<String>` and `defaultBranch: String` parameters for branch auto-completion.
- Added "Loaded Projects" table with `JBTable` and `ToolbarDecorator` in settings UI for managing project history.

---

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
- **Supported IDE Versions**: IntelliJ IDEA 2024.2 - 2025.2.*
- **Minimum Requirements**: Java 17, GitLab API v4

---
[2.1.0]: https://github.com/dogdrinkwater/gitlab-pipeline-plugin/releases/tag/v2.1.0
[2.0.0]: https://github.com/dogdrinkwater/gitlab-pipeline-plugin/releases/tag/v2.0.0
[1.1.8]: https://github.com/dogdrinkwater/gitlab-pipeline-plugin/releases/tag/v1.1.8
[1.1.7]: https://github.com/dogdrinkwater/gitlab-pipeline-plugin/releases/tag/v1.1.7
[1.1.6]: https://github.com/dogdrinkwater/gitlab-pipeline-plugin/releases/tag/v1.1.6
[1.1.5]: https://github.com/dogdrinkwater/gitlab-pipeline-plugin/releases/tag/v1.1.5
[1.1.4]: https://github.com/dogdrinkwater/gitlab-pipeline-plugin/releases/tag/v1.1.4
[1.1.2]: https://github.com/dogdrinkwater/gitlab-pipeline-plugin/releases/tag/v1.1.2
[1.0.1]: https://github.com/dogdrinkwater/gitlab-pipeline-plugin/releases/tag/v1.0.1
[1.0.0]: https://github.com/dogdrinkwater/gitlab-pipeline-plugin/releases/tag/v1.0.0
