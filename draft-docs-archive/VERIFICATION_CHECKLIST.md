# PPRGS Repository URL Update - Verification Checklist

**Use this checklist after running the URL update to ensure everything works correctly.**

---

## ✅ Pre-Update Checks

Before running the update:

- [ ] **Backup your repository**
  ```bash
  # Create a branch for the update
  git checkout -b url-update
  
  # Or create a full backup
  cp -r /path/to/repo /path/to/repo-backup
  ```

- [ ] **Verify you're in repository root**
  ```bash
  pwd
  ls -la | grep .git
  # Should see .git directory
  ```

- [ ] **Check for uncommitted changes**
  ```bash
  git status
  # Should be clean, or commit/stash existing changes
  ```

- [ ] **Note current remote URL**
  ```bash
  git remote -v
  # Save this in case you need to revert
  ```

---

## 🔄 Update Execution Checks

During the update process:

- [ ] **Script runs without errors**
  ```bash
  ./URL_UPDATE_SCRIPT.sh
  # Should complete with summary message
  ```

- [ ] **Backup files created**
  ```bash
  find . -name "*.backup" | head -5
  # Should show .backup files
  ```

- [ ] **Changes reported**
  ```bash
  # Script should output list of files changed
  ```

---

## 🔍 Post-Update Verification

### 1. Basic Checks

- [ ] **No old URLs remain in docs**
  ```bash
  grep -r "stumbler-ai-framework" . --include="*.md" --exclude-dir=".git"
  # Should return: no results (except in backup files)
  ```

- [ ] **New URLs present**
  ```bash
  grep -r "pprgs-ai-framework" . --include="*.md" | wc -l
  # Should return: many results (>10)
  ```

- [ ] **Git detects changes**
  ```bash
  git status
  # Should show modified files
  ```

### 2. Core Document Checks

- [ ] **README.md updated**
  ```bash
  grep "pprgs-ai-framework" README.md
  # Should show new URL in multiple places
  ```

- [ ] **Quick start clone command correct**
  ```bash
  grep "git clone" docs/QUICKSTART.md
  # Should show: github.com/Infn8Loop/pprgs-ai-framework
  ```

- [ ] **Citation BibTeX updated**
  ```bash
  grep "url.*github" docs/CITATION.md
  # All should show pprgs-ai-framework
  ```

### 3. Review Changes in Git

- [ ] **Diff looks reasonable**
  ```bash
  git diff | less
  # Review changes, press 'q' to quit
  ```

- [ ] **Check specific file**
  ```bash
  git diff README.md
  # Verify only URLs changed, not content
  ```

- [ ] **Count changed files**
  ```bash
  git diff --stat
  # Should match script report
  ```

### 4. Functional Testing

- [ ] **README renders correctly**
  ```bash
  # Open README.md in browser or markdown viewer
  # All links should be properly formatted
  ```

- [ ] **Clone command works** (in separate directory)
  ```bash
  cd /tmp
  git clone https://github.com/Infn8Loop/pprgs-ai-framework.git test-clone
  # Should clone successfully
  cd test-clone && ls -la
  # Clean up: cd /tmp && rm -rf test-clone
  ```

- [ ] **Internal links resolve**
  ```bash
  # Click links in README (if viewing on GitHub)
  # Or check with markdown linter
  ```

### 5. Platform-Specific Checks

- [ ] **Python files updated** (if applicable)
  ```bash
  grep "pprgs-ai-framework" $(find . -name "*.py") | head
  # Check docstrings and comments updated
  ```

- [ ] **Package metadata updated** (if applicable)
  ```bash
  # Check setup.py or pyproject.toml
  grep "github" setup.py
  # Or
  grep "github" pyproject.toml
  ```

- [ ] **Documentation builds** (if using docs generator)
  ```bash
  # If using Sphinx, MkDocs, etc.
  cd docs && make html
  # Or your build command
  ```

---

## 📊 Quality Checks

### URL Format Consistency

- [ ] **All URLs use HTTPS**
  ```bash
  grep -r "http://github" . --include="*.md"
  # Should return: no results
  ```

- [ ] **No trailing slashes**
  ```bash
  grep -r "pprgs-ai-framework/" . --include="*.md"
  # Check if any have trailing slashes (usually okay but inconsistent)
  ```

- [ ] **Consistent formatting**
  ```bash
  grep -r "github.com/Infn8Loop/pprgs-ai-framework" . --include="*.md" | head
  # Check format is consistent across files
  ```

### Markdown Syntax

- [ ] **No broken markdown from replacement**
  ```bash
  # Check for patterns like: [text](url)[extra-chars]
  grep -r "pprgs-ai-framework\)" . --include="*.md"
  # Should all be properly closed links
  ```

- [ ] **Code blocks intact**
  ```bash
  # Verify replacement didn't break bash/code blocks
  # Manually review git diff for code sections
  ```

---

## 🚀 Commit & Deploy Checks

### Before Committing

- [ ] **All tests pass** (if you have tests)
  ```bash
  pytest  # or your test command
  npm test  # if applicable
  ```

- [ ] **Documentation builds without errors**
  ```bash
  # If using docs generator
  make docs
  # or equivalent command
  ```

- [ ] **No unintended changes**
  ```bash
  git diff --stat
  # Verify only expected files changed
  ```

### Commit Process

- [ ] **Stage all changes**
  ```bash
  git add -A
  ```

- [ ] **Clear commit message**
  ```bash
  git commit -m "Update repository URL from stumbler-ai-framework to pprgs-ai-framework

  - Updated all documentation references
  - Updated citation examples
  - Updated clone instructions
  - No functional changes
  "
  ```

- [ ] **Push to remote**
  ```bash
  git push origin url-update
  # Or your branch name
  ```

### After Push

- [ ] **Create PR** (if using branches)
  - Go to GitHub
  - Create pull request
  - Review changes online

- [ ] **Check GitHub rendering**
  - README displays correctly
  - Links are clickable and work
  - No broken images or badges

- [ ] **Update remote URL** (if needed)
  ```bash
  git remote set-url origin https://github.com/Infn8Loop/pprgs-ai-framework.git
  git remote -v
  # Verify new URL
  ```

---

## 🧹 Cleanup Checks

After successful deployment:

- [ ] **Remove backup files**
  ```bash
  find . -name "*.backup" -type f -delete
  ```

- [ ] **Verify backups deleted**
  ```bash
  find . -name "*.backup"
  # Should return: no results
  ```

- [ ] **Final status check**
  ```bash
  git status
  # Should be clean
  ```

- [ ] **Delete temporary branch** (if used)
  ```bash
  git checkout main
  git branch -d url-update
  ```

---

## 🔧 Rollback Plan (If Needed)

If something goes wrong:

### Option 1: Use Git

```bash
# If not committed yet
git checkout .
git clean -fd

# If committed but not pushed
git reset --hard HEAD~1

# If pushed
git revert <commit-hash>
```

### Option 2: Use Backup Files

```bash
# Restore from .backup files
find . -name "*.backup" -exec sh -c 'mv "$1" "${1%.backup}"' _ {} \;
```

### Option 3: Use Full Backup

```bash
# If you created a full backup
rm -rf /path/to/repo
cp -r /path/to/repo-backup /path/to/repo
```

---

## 📋 Final Summary Checklist

**Everything working if:**

- ✅ No old URLs in markdown files
- ✅ New URLs present throughout
- ✅ Clone command works
- ✅ All links resolve correctly  
- ✅ Git history clean
- ✅ Changes committed and pushed
- ✅ GitHub displays correctly
- ✅ No backup files remaining

**Total checks**: 45+  
**Time required**: 10-15 minutes  
**Confidence level after completion**: 🔥 High

---

## 📞 If Something's Wrong

### Common Issues

**Issue**: Old URLs still present
**Fix**: Re-run script, check for files outside standard locations

**Issue**: Links broken
**Fix**: Check for typos, verify GitHub repository renamed

**Issue**: Script errors
**Fix**: Check permissions, verify sed syntax for your OS

**Issue**: Git conflicts
**Fix**: Stash changes, update, re-apply

### Get Help

- **Email**: mike@mikericcardi.com
- **Subject**: "URL Update Verification Issue"
- **Include**: Specific error, what you tried, OS info

---

## ✅ Verification Complete

Once all checks pass:

1. ✅ **URLs updated correctly**
2. ✅ **No regressions introduced**  
3. ✅ **Changes committed**
4. ✅ **Repository clean**
5. ✅ **Ready for use**

**Congratulations!** Your PPRGS repository now uses the correct, professional URL structure. 🎉

---

**Checklist Version**: 1.0  
**Last Updated**: November 2, 2025  
**Repository**: https://github.com/Infn8Loop/pprgs-ai-framework
