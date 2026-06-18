# GitLab Pipeline Monitor

A powerful IntelliJ IDEA plugin for real-time GitLab CI/CD pipeline monitoring, deployment tracking, and merge request management — designed to streamline your DevOps workflow without leaving your IDE. Now with **multi-project workspace support** and **full Chinese language support**!


## ✨ Key Features

### 🗂️ Multi-Project Workspace Support (New in v2.1!)
- **Automatic Detection** - Plugin scans your workspace on startup and discovers every directory with a GitLab remote. No configuration needed.
- **Project Selector Dropdown** - A clean dropdown at the top of the GitLab Toolkit panel lets you switch between projects in one click. Automatically hidden for single-project workspaces — zero UI change for existing users.
- **Persistent Selection** - Your last chosen project is remembered and restored on next IDE open.
- **Name-Conflict Disambiguation** - Two repos named `api`? The dropdown shows their paths: `api (/services/api)`.
- **Refresh Projects Button** - New toolbar button re-scans the workspace without restarting the IDE — great for mid-session repo cloning.
- **Multi-Instance GitLab** - Mix projects from `gitlab.com` and your company's self-hosted server in the same workspace.
- **Resilient Edge Cases** - Removed a repo? The plugin falls back gracefully and shows a notification. No GitLab repos found? A helpful empty-state label guides you.

### 🌐 Show All Loaded Projects (New in v2.1!)
- **Cross-Window Project Dropdown** - Enable *"Show all loaded projects in dropdown"* in **Settings → Custom** to see every project you've ever opened across all IDE windows — ideal for microservice teams working with many repos.
- **Smart Deduplication** - Projects open in the current window and other windows never appear twice.
- **Correct Names Always** - Project names are derived from the GitLab remote path (e.g. `transcript-services`), never from the IDE window name.
- **Create Pipelines Anywhere** - Trigger pipelines for projects from other windows. Variables are loaded from the stored local path automatically. If the path isn't known yet, the plugin guides you to open the folder and remembers it for next time.

### 🚀 Deployment Monitoring (New in v2.0!)
- **Complete Deployment Tracking** - Monitor all deployments across environments in a dedicated Deployments tab
- **Smart Stage Grouping** - Jobs organized by pipeline stages with collapsible panels
- **Lazy Loading** - Loads only 5 jobs initially per stage for lightning-fast performance
- **Auto-Expand Failed Stages** - Automatically expands failed stages to show all job details
- **Environment Filtering** - Filter by production, staging, development, or custom environments
- **Status Filtering** - Track deployments by success, failed, running, canceled, and more
- **Deployment Details** - View environment URLs, job info, pipeline links, and commit SHAs
- **Real-Time Updates** - Auto-refresh keeps deployment status current

### Pipeline Management
- **Real-Time Pipeline Monitoring** - Live status updates with configurable auto-refresh (5s to 1hr intervals)
- **Desktop Notifications** - Automatic alerts when your pipelines complete with one-click navigation
- **Smart Selection Persistence** - Maintains your selected pipeline across refreshes for seamless monitoring
- **Create Pipelines with Variables** - Trigger new pipelines directly from IDE with automatic .gitlab-ci.yml variable parsing
- **Cancel or Retry Pipelines** - Stop running/pending pipelines or retry them with preserved variables
- **Advanced Job Log Viewer** - Full ANSI color support, auto-scroll, raw log mode, real-time updates, and Previous/Next job navigation
- **Infinite Scroll** - Seamlessly load thousands of pipelines with smart pagination

### Smart Features
- **Auto-Star Projects** - Intelligent project detection with one-click starring workflow
- **Resizable Panels** - Drag-to-resize split panes for customized workspace
- **Multi-Environment Support** - Visual distinction for dev, qa, ppe, prod environments
- **Comprehensive Details View** - View all variables, jobs timeline, status, duration, and metadata

### 🌍 Internationalization (New in v2.0!)
- **Chinese Language Support** - Complete UI translation to Simplified Chinese (简体中文)
- **Auto-Language Detection** - Automatically displays in your IDE's configured language
- **Bilingual Interface** - Seamlessly switch between English and Chinese
- **200+ Translated Elements** - All UI components, dialogs, tooltips, and messages fully localized
- **UTF-8 Encoding** - Perfect rendering of Chinese characters across all platforms

## 🚀 What Makes This Plugin Special

### Industry-First Features:
- **Deployment Monitoring** - Dedicated deployment tracking with stage grouping and lazy loading
- **Smart Notifications** - Desktop alerts with one-click navigation when your pipelines complete
- **ANSI Log Rendering** - Full color-coded log display (colors, bold, italic, underline)
- **Job Log Navigation** - Unique Previous/Next buttons for sequential job log browsing
- **Smart Variable Parser** - Automatically extracts variables from .gitlab-ci.yml with options support
- **Live Job Logs** - Real-time log streaming with 5-second auto-refresh for running jobs
- **Selection Persistence** - Unique feature maintaining context across refreshes
- **Auto-Star Workflow** - Streamlined project onboarding with automatic starring
- **Full Internationalization** - Native Chinese language support with auto-detection

## 📋 Requirements

- IntelliJ IDEA 2024.2 or later (Community or Ultimate Edition)
- GitLab instance (self-hosted or GitLab.com)
- GitLab Personal Access Token with `api` scope
- A workspace folder containing at least one directory with a `.git` remote pointing to GitLab (or starred projects for the fallback discovery path)

## 🔧 Installation

### From JetBrains Marketplace (Recommended)
1. Open IntelliJ IDEA
2. Go to **Settings** → **Plugins**
3. Search for "**GitLab Pipeline Monitor**"
4. Click **Install**
5. Restart IDE

### Manual Installation
1. Download the latest release from [Releases](https://github.com/dogdrinkwater/gitlab-pipeline-plugin/releases)
2. Go to **Settings** → **Plugins** → ⚙️ → **Install Plugin from Disk**
3. Select the downloaded `.zip` file
4. Restart IDE

## ⚙️ Configuration

### Step 1: Get GitLab Personal Access Token
1. Log in to your GitLab instance
2. Go to **Settings** → **Access Tokens**
3. Create a token with `api` scope
4. Copy the token (you won't see it again!)

### Step 2: Configure Plugin
1. Open IntelliJ IDEA
2. Go to **Settings** → **Tools** → **GitLab Settings**
3. Enter your **GitLab URL** (e.g., `https://gitlab.com`)
4. Paste your **Access Token**
5. (Optional) Set **Auto-refresh interval**
6. Click **Apply** → **OK**

### Step 3: Open GitLab Toolkit Tool Window
1. Click **View** → **Tool Windows** → **GitLab Toolkit**
2. Or use the tool window icon on the right sidebar
3. Pipelines for your current project will load automatically

## 📖 Usage Guide

### Multi-Project Workspaces (v2.1+)

If your workspace contains two or more directories with GitLab remotes, a **project selector dropdown** automatically appears at the top of the GitLab Toolkit panel.

```
┌────────────────────────────────────────────────────────────┐
│  Project: [frontend ▼]  (1 of 5)  [↺] [⟳] [⚙]           │
├────────────────────────────────────────────────────────────┤
│  Pipelines  │  Deployments                                 │
└────────────────────────────────────────────────────────────┘
```

**Switching projects:**
1. Click the dropdown and select any project — pipelines and deployments reload immediately.
2. Your selection persists across IDE restarts.

**After cloning a new repo:**
1. Click the **"Refresh Projects"** button (⟳, distinct from the pipeline Refresh button).
2. The new repository appears in the dropdown within seconds.

**No GitLab projects found?**
- Make sure the workspace folder contains a `.git` directory whose `origin` remote points to a GitLab instance.
- Check that the GitLab URL in Settings → Tools → GitLab Toolkit Settings matches your instance.

### Viewing Pipelines
- Pipelines are displayed in chronological order with status indicators
- Click any pipeline to view detailed information
- Your selection persists across refreshes

### Pipeline Notifications
- When you create a pipeline, the plugin automatically tracks it
- You'll receive a desktop notification when the pipeline completes
- Click **View pipeline** in the notification to navigate directly to the completed pipeline
- Notifications show status (✅ success, ❌ failed, 🚫 canceled) and branch information

### Creating New Pipelines
1. Click the **+** (New Pipeline) button
2. Plugin automatically parses `.gitlab-ci.yml` variables and marks only those without defaults as required
3. Select values from dropdown options
4. Click **Create** to trigger the pipeline

### Cancelling & Retrying Pipelines
- Click the **⏸** (Cancel) button to stop a running/pending pipeline right from the IDE
- Click the **↻** (Retry) button next to any pipeline to re-run it
- Original variables are automatically preserved so the new pipeline mirrors the previous one

### Viewing Job Logs
1. Click on any job name in the Jobs Timeline
2. Logs display with full ANSI color support
3. Enable **Auto-scroll** to follow real-time output
4. Toggle **Show Raw Log** to see escape codes
5. Use **Previous** and **Next** buttons to navigate between job logs sequentially

### Auto-Star Projects
- If your project isn't starred, plugin will offer to star it automatically
- Click **Star Project** in the dialog
- Pipelines load immediately after starring

## 💡 Pro Tips

- **Monitor Running Jobs**: Enable auto-refresh (10-30s) to track pipeline progress
- **Color-Coded Logs**: Use ANSI rendering to quickly identify errors (red) and success (green)
- **Selection Persistence**: Select a pipeline and let auto-refresh update details automatically
- **Keyboard Navigation**: Use arrow keys to navigate pipeline list
- **Branch Context**: Plugin detects your current Git branch for pipeline creation

## 🐛 Troubleshooting

### "No pipelines found"
- Ensure your project is starred in GitLab
- Or click **Star Project** when prompted by the plugin
- Verify your Access Token has `api` scope

### "Access token not configured"
- Go to **Settings** → **Tools** → **GitLab Settings**
- Enter your GitLab URL and Access Token
- Click **Apply**

### "Project not found"
- Check that project name matches GitLab project name
- Ensure you have access to the project in GitLab
- Try starring the project manually in GitLab

### ANSI colors not showing
- Ensure you're viewing the formatted log (not raw mode)
- Check that your GitLab jobs use ANSI escape codes
- Some jobs may not output colored text


## 📝 Changelog

### Version 2.1.0 (2026-02-25)
- 🗂️ **Multi-Project Workspace Support** - Automatic detection of all GitLab repositories in the workspace with a project selector dropdown
- 🔄 **Refresh Projects** - New toolbar button to re-scan the workspace without restarting the IDE
- 🛡️ **Resilient Edge Cases** - Graceful handling of removed projects, empty workspaces, and startup race conditions
- 🌍 **9 New i18n Keys** - Full English and Chinese translations for all multi-project UI strings
- 🐛 **53 New Unit Tests** - Comprehensive coverage of detection logic, API integration, edge cases, and i18n

### Version 2.0.0 (2026-02-13)
- 🚀 **Deployment Monitoring** - Brand new Deployments tab with environment and status filtering
- 🎯 **Smart Stage Grouping** - Collapsible stages with lazy loading (5 jobs initially)
- 🔄 **Auto-Expand Failed Stages** - Automatically shows all jobs in failed stages
- 🌍 **Chinese Language Support** - Complete UI translation to Simplified Chinese (简体中文)
- 🔤 **Auto-Language Detection** - Automatically displays in your IDE's configured language
- 📝 **200+ Translated Elements** - All UI components fully localized for English and Chinese
- 🎨 **UTF-8 Encoding** - Perfect rendering of Chinese characters
- ⚡ **Performance Optimizations** - Stage-level job loading reduces API calls by 80%+
- 🔧 **Unified Refresh Logic** - All tabs share consistent auto-refresh settings

### Version 1.1.8 (2026-02-09)
- 🎉 **Merge Request Integration** - Brand new MR tab with full list view and detailed information
- 🔔 **Desktop Notifications** - Automatic alerts when your pipelines complete with one-click navigation
- ⬅️➡️ **Job Log Navigation** - New Previous/Next buttons for sequential job log browsing
- 📊 **Enhanced MR Details** - View assignee, author, merge status, and branches
- 🔄 **Unified Tab Interface** - Seamless switching between Pipelines and Merge Requests
- ↔️ **Resizable Panels** - Drag-to-resize split panes for customized workspace
- 🎯 **Pipeline Tracking** - Automatically monitor user-created pipelines for completion
- 🛠️ **Renamed Tool Window** - Now "GitLab Toolkit" reflecting expanded functionality

### Version 1.0.1 (2025-11-24)
- ✅ GitHub Actions workflow now builds the plugin, tags releases, and publishes release artifacts automatically
- 🛡️ New pipeline dialog enforces required inputs only when `.gitlab-ci.yml` lacks defaults
- ⛔ Cancel button in the pipeline list lets you stop running/pending pipelines directly from the IDE

### Version 1.0.0 (2025-11-21)
- 🎉 Initial release
- ✅ Real-time pipeline monitoring with auto-refresh
- ✅ ANSI log rendering with full color support
- ✅ Smart selection persistence across refreshes
- ✅ Create pipelines with variable parsing
- ✅ One-click pipeline retry
- ✅ Auto-star project workflow
- ✅ Infinite scroll with pagination
- ✅ Live job log streaming
- ✅ Comprehensive pipeline details view

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📧 Support

- **Email**: 7motor28@gmail.com


## 🙏 Acknowledgments

- Built with [IntelliJ Platform SDK](https://plugins.jetbrains.com/docs/intellij/)
- Uses [OkHttp](https://square.github.io/okhttp/) for HTTP requests
- Uses [Gson](https://github.com/google/gson) for JSON parsing
- Uses [SnakeYAML](https://bitbucket.org/snakeyaml/snakeyaml) for YAML parsing

---

**Made with ❤️ by developers, for developers**
