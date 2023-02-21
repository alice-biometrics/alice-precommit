# alice-precommit

Repo to upload custom hooks to use with pre-commit

### jwt-checker

Hook to find jwt keys on files

To use, add following code on your `.pre-commit-config.yaml`

```yaml
repos:
  - repo: https://github.com/alice-biometrics/alice-precommit
    rev: v1
    hooks:
      - id: jwt-checker
        language: system
        types: [ python ]
        require_serial: true
        fail_fast: true
```
