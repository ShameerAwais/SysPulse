# Contributing to SysPulse

We love your input! We want to make contributing to SysPulse as easy and transparent as possible, whether it's:

- Reporting a bug
- Discussing the current state of the code
- Submitting a fix
- Proposing new features
- Becoming a maintainer

## We Develop with GitHub
We use GitHub to host code, to track issues and feature requests, as well as accept pull requests.

## We Use [Github Flow](https://guides.github.com/introduction/flow/index.html)
Pull requests are the best way to propose changes to the codebase. We actively welcome your pull requests:

1. Fork the repo and create your branch from `main`.
2. If you've added code that should be tested, add tests.
3. If you've changed APIs, update the documentation.
4. Ensure the test suite passes.
5. Make sure your code lints.
6. Issue that pull request!

## Any contributions you make will be under the MIT Software License
In short, when you submit code changes, your submissions are understood to be under the same [MIT License](http://choosealicense.com/licenses/mit/) that covers the project. Feel free to contact the maintainers if that's a concern.

## Report bugs using GitHub's [issue tracker](https://github.com/yourusername/SysPulse/issues)
We use GitHub issues to track public bugs. Report a bug by [opening a new issue](https://github.com/yourusername/SysPulse/issues/new); it's that easy!

## Write bug reports with detail, background, and sample code

**Great Bug Reports** tend to have:

- A quick summary and/or background
- Steps to reproduce
  - Be specific!
  - Give sample code if you can.
- What you expected would happen
- What actually happens
- Notes (possibly including why you think this might be happening, or stuff you tried that didn't work)

## Use a Consistent Coding Style

* Use 4 spaces for indentation rather than tabs
* Keep line length under 120 characters
* Run `flake8` for style enforcement

## License
By contributing, you agree that your contributions will be licensed under its MIT License.

## Branching Strategy

- `main`: Stable production-ready code
- `dev`: Integration branch
- `feature/*`: One feature per branch (e.g., `feature/metrics-endpoint`)

## Workflow

1. Create feature branch from `dev`
2. Push code and open a Pull Request (PR) into `dev`
3. PR must pass CI and be reviewed before merge

## Code Style

- Python: Follow PEP8 (use flake8)
- Bash: Use shellcheck for scripts
