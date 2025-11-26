# GitLab Pipeline Monitor

[![Version](https://img.shields.io/badge/version-1.1.0-blue.svg)](https://github.com/dogdrinkwater/gitlab-pipeline-plugin)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A powerful IntelliJ IDEA plugin for real-time GitLab CI/CD pipeline and merge request monitoring, designed to streamline your DevOps workflow without leaving your IDE.

## ✨ Key Features

### Pipeline Management
- **Real-Time Pipeline Monitoring** - Live status updates with configurable auto-refresh (5s to 1hr intervals)
- **Desktop Notifications** - Automatic alerts when your pipelines complete with one-click navigation
- **Smart Selection Persistence** - Maintains your selected pipeline across refreshes for seamless monitoring
- **Create Pipelines with Variables** - Trigger new pipelines directly from IDE with automatic .gitlab-ci.yml variable parsing
- **Cancel or Retry Pipelines** - Stop running/pending pipelines or retry them with preserved variables
- **Advanced Job Log Viewer** - Full ANSI color support, auto-scroll, raw log mode, real-time updates, and Previous/Next job navigation
- **Infinite Scroll** - Seamlessly load thousands of pipelines with smart pagination

### Merge Request Integration
- **MR List View** - Browse all merge requests for your project with status indicators
- **Detailed MR Information** - View assignee, author, merge status, source/target branches, and metadata
- **MR Notifications** - Stay updated on merge request status changes
- **Browser Integration** - Quick jump to GitLab UI for any merge request

### Smart Features
- **Auto-Star Projects** - Intelligent project detection with one-click starring workflow
- **Unified Tab Interface** - Seamless switching between Pipelines and Merge Requests
- **Resizable Panels** - Drag-to-resize split panes for customized workspace
- **Multi-Environment Support** - Visual distinction for dev, qa, ppe, prod environments
- **Comprehensive Details View** - View all variables, jobs timeline, status, duration, and metadata

## 🚀 What Makes This Plugin Special

### Industry-First Features:
- **Unified GitLab Toolkit** - Only plugin combining pipelines AND merge requests in one seamless interface
- **Smart Notifications** - Desktop alerts with one-click navigation when your pipelines complete
- **ANSI Log Rendering** - Full color-coded log display (colors, bold, italic, underline)
- **Job Log Navigation** - Unique Previous/Next buttons for sequential job log browsing
- **Smart Variable Parser** - Automatically extracts variables from .gitlab-ci.yml with options support
- **Live Job Logs** - Real-time log streaming with 5-second auto-refresh for running jobs
- **MR Detail View** - Comprehensive merge request information including assignees and merge status
- **Selection Persistence** - Unique feature maintaining context across refreshes
- **Auto-Star Workflow** - Streamlined project onboarding with automatic starring

## 📋 Requirements

- IntelliJ IDEA 2024.2 or later (Community or Ultimate Edition)
- GitLab instance (self-hosted or GitLab.com)
- GitLab Personal Access Token with `api` scope
- Starred projects in GitLab (or use auto-star feature)

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
3. Pipelines and merge requests for your current project will load automatically

## 📖 Usage Guide

### Viewing Pipelines
- Pipelines are displayed in chronological order with status indicators
- Click any pipeline to view detailed information
- Your selection persists across refreshes
- Switch between **Pipelines** and **Merge Requests** tabs

### Viewing Merge Requests
- Browse all merge requests in the **Merge Requests** tab
- Click any MR to view detailed information including assignee, merge status, and branches
- Click **Open in GitLab** to view the MR in your browser
- Drag the divider to resize the MR list and details panels

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

### Version 1.1.0 (2025-11-26)
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
- **Issues**: [GitHub Issues](https://github.com/dogdrinkwater/gitlab-pipeline-plugin/issues)

## 🙏 Acknowledgments

- Built with [IntelliJ Platform SDK](https://plugins.jetbrains.com/docs/intellij/)
- Uses [OkHttp](https://square.github.io/okhttp/) for HTTP requests
- Uses [Gson](https://github.com/google/gson) for JSON parsing
- Uses [SnakeYAML](https://bitbucket.org/snakeyaml/snakeyaml) for YAML parsing

---

**Made with ❤️ by developers, for developers**



