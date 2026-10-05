# Learn GitHub Actions step by step

You'll learn GitHub Actions by automating a real (tiny) project: `tempconv`, a
Python temperature converter with tests. Each lesson adds one workflow file in
`.github/workflows/`. Every file is heavily commented, so read the YAML alongside
this guide.

| Lesson | File | You learn |
|---|---|---|
| 0 | `src/`, `tests/` | The project we're automating |
| 1 | `01-hello.yml` | Workflows, triggers, jobs, steps, contexts, `actions/checkout` |
| 2 | `02-test.yml` | Real CI: set up Python, install, run tests on push and pull request |
| 3 | `03-ci-pipeline.yml` | Multiple jobs, `needs`, matrix builds, caching, filters, concurrency |
| 4 | `04-build-artifact.yml` | Manual runs with inputs, env vars, outputs, summaries, artifacts |

---

## Key vocabulary

```
Workflow  (a .yml file in .github/workflows/)
 └── triggered by an Event   (push, pull_request, workflow_dispatch, schedule…)
 └── contains Jobs           (run in parallel by default, each on a fresh Runner VM)
      └── contain Steps      (run in order)
           ├── run:  shell commands
           └── uses: a reusable Action (e.g. actions/checkout@v7)
```

- **Runner**: the virtual machine that runs a job (`ubuntu-latest`, `windows-latest`, `macos-latest`). It starts empty every time.
- **Action**: a reusable building block, written `owner/repo@version`. Find more at <https://github.com/marketplace?type=actions>.
- **Expression**: `${{ ... }}`, which reads values like `github.sha`, `matrix.os` and `inputs.temperature`.

---

## Lesson 0: the project

Read `src/tempconv/convert.py` and `tests/test_convert.py`, then run locally:

```bash
pip install -e ".[dev]"
pytest
```

**Rule of thumb:** before automating anything, make sure you can run it by hand.
CI just runs your manual commands on a clean machine.

## Lesson 1: Hello Actions (`01-hello.yml`)

1. Open the file and read the comments.
2. Push any commit (or go to **Actions → 01 - Hello Actions → Run workflow**).
3. On GitHub, open the **Actions** tab, click the run, then the `say-hello` job, and expand each step.

**Notice:** the first `ls -la` shows an empty folder. Your code only appears
after `actions/checkout`. This is the #1 beginner mistake.

✏️ **Try it:** add a step that runs `python --version` and `date`.

## Lesson 2: Run tests on every push (`02-test.yml`)

The steps are the same ones you run locally: checkout, install Python, install deps, `pytest`.

✏️ **Try it: break the build on purpose.**
1. In `convert.py`, change `+ 32` to `+ 31` and push.
2. Watch the run go ❌ red, and read the failing test in the log.
3. Revert, push, and watch it go ✅ green.

This is the whole value of CI: you learn about breakage within minutes, on every commit.

✏️ **Try it:** open a pull request. The check results appear right on the PR.

## Lesson 3: A real CI pipeline (`03-ci-pipeline.yml`)

New ideas:
- **Two jobs** (`lint`, `test`). `needs: lint` makes `test` wait, so you get fast feedback on style before running the slower tests.
- **Matrix:** one definition becomes 6 jobs (3 Python versions × 2 OSes). On the run page you'll see a graph of all of them.
- **`cache: pip`** reuses downloaded packages, so later runs are faster.
- **Filters:** `branches:` and `paths-ignore:` control *when* it runs. Editing only `.md` files won't trigger it.
- **`concurrency`** cancels an older run when you push again quickly.

✏️ **Try it:**
1. Add a badly formatted line (e.g. `x=1`) to `cli.py` and push. `lint` fails and `test` is **skipped**.
2. Fix it locally with `ruff format .`
3. Add `macos-latest` to the matrix. How many jobs run now?

## Lesson 4: Inputs, outputs and artifacts (`04-build-artifact.yml`)

This one only runs **manually**. The file must be on the default branch (`main`)
for the button to appear. Go to **Actions → 04 - Build & convert → Run workflow**,
enter `37`, choose `f`, and run it.

Then look at:
- **Summary page:** the conversion result, written via `$GITHUB_STEP_SUMMARY`.
- **Job outputs:** the `build` job prints the value that the `convert` job produced (`needs.convert.outputs.result`).
- **Artifacts:** at the bottom of the summary, download `tempconv-dist` (the built `.whl` and `.tar.gz`).

🔐 **Security note:** inputs are passed via `env:` and used as `"$VAR"`, never
pasted straight into `run:` with `${{ inputs.x }}`. Pasting them in directly would let someone
inject shell commands.

---

## Debugging tips

- Click a failed step: the log shows the exact command and error.
- **Re-run jobs → Enable debug logging** gives you much more detail.
- YAML is indentation-sensitive. Use spaces, never tabs.
- A workflow file must be on the branch you push to, in `.github/workflows/`, with a `.yml` or `.yaml` extension.
- Check workflow syntax locally with [actionlint](https://github.com/rhysd/actionlint).
- **"My workflow didn't run!"** Check its filters. Lesson 3 ignores pushes that
  only change `**.md` files, so pushing just this guide won't trigger it. That's intended.
- **No "Run workflow" button?** `workflow_dispatch` (manual runs, used by
  lessons 1 and 4) only shows up once the workflow file exists on the repo's
  **default branch** (`main`). Merge your branch into `main` first.

## Where to go next

- **Scheduled runs:** `on: schedule: - cron: "0 6 * * 1"` (every Monday 06:00 UTC).
- **Secrets:** go to Settings → Secrets and variables → Actions, then use `${{ secrets.MY_TOKEN }}`.
- **Publish a release** when you push a tag `v*` (e.g. to PyPI with trusted publishing).
- **Branch protection:** require the CI checks to pass before merging into `main`.
- **Reusable workflows** (`workflow_call`) and **composite actions** to share steps between repos.
- Official docs: <https://docs.github.com/actions>
