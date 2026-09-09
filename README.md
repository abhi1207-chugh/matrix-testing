# Matrix Builds for Multi-Environment Testing

## 📌 Project Overview

This project demonstrates **automated multi-environment software testing using GitHub Actions Matrix Strategy**.

The main objective is to verify that the same Python application and unit test suite work correctly across:

- Multiple Operating Systems
- Multiple Python runtime versions

Instead of manually running tests on every environment, GitHub Actions automatically creates and executes multiple testing jobs using a **matrix configuration**.

---

## 🎯 Objectives

The main objectives of this project are:

1. Understand GitHub Actions and Continuous Integration (CI).
2. Implement automated unit testing using `pytest`.
3. Use GitHub Actions Matrix Strategy for multi-environment testing.
4. Test the application on multiple operating systems.
5. Test compatibility across multiple Python versions.
6. Run the same unit test suite automatically across all environments.
7. Demonstrate parallel execution of matrix jobs.

---

## 🏗️ Project Architecture

```text
                         GitHub Repository
                                │
                                ▼
                     GitHub Actions Workflow
                                │
                                ▼
                         Matrix Strategy
                                │
                 ┌──────────────┴──────────────┐
                 │                             │
              Ubuntu                        Windows
                 │                             │
        ┌────────┼────────┐           ┌────────┼────────┐
        │        │        │           │        │        │
      Python   Python   Python       Python   Python   Python
       3.10     3.11     3.12        3.10     3.11     3.12
        │        │        │           │        │        │
        └────────┴────────┴───────────┴────────┴────────┘
                                │
                                ▼
                         Same Unit Tests
                                │
                                ▼
                           Test Results
```
