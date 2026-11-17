# Source code for static analysis (SAST)

Use Semgrep rule:

```
rules:
  - id: hardcoded-conditional
    patterns:
      - pattern-either:
          - pattern: if (true) { ... }
          - pattern: if (false) { ... }
          - pattern: if ($VAR = true) { ... }
          - pattern: if ($VAR = false) { ... }
          - pattern: if ($EXPR && false) { ... }
          - pattern: if (false && $EXPR) { ... }
          - pattern: if ($EXPR || true) { ... }
          - pattern: if (true || $EXPR) { ... }
    message: This if statement will always have the same behavior and is therefore
      unnecessary.
    languages:
      - java
    severity: ERROR
    metadata:
      category: correctness
      technology:
        - java
      license: Semgrep Rules License v1.0. For more details, visit
        semgrep.dev/legal/rules-license
```