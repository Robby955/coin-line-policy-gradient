# Correction times for linear policy gradient

Rob Sneiderman

[Paper](paper/coin-line-rates.pdf) · [LaTeX source](paper/coin-line-rates.tex) ·
[Version 0.1.0](https://github.com/Robby955/coin-line-policy-gradient/releases/tag/v0.1.0)

This companion studies the coin-line model from MAIS-A8. It contains the
exact finite-horizon return and gradient, a manuscript on correction-time
asymptotics, numerical receipts, and independent finite checks.

The paper concerns **zero initialization, exact Euclidean gradient flow,
fixed integer L >= 4, and the first correction of the test-state logit**.
It claims a two-sided order bound

    T_epsilon = Theta_L(epsilon^(-alpha_L)),
    alpha_L = M / (M - n(L+1) - 2r),
    n = ceil((L+1)/2), r = L+1-n, M = n^2(1+L^2)+r^2.

Read [the manuscript](paper/coin-line-rates.pdf) for the proof and scope.
[STATUS.md](STATUS.md) records the review status and links the reports.
The original qualitative O87 submission is
[MAIS issue #35](https://github.com/lionellevine/MAIS/issues/35).
This manuscript is a preprint; no upstream acceptance is claimed.

## Install and test

The recorded environment is Python 3.13; exact package versions are in
`requirements.txt` and platform details in `environment.json`.

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
python -m unittest discover -v
```

Tests compare the gradient against independent rational path enumeration,
including saturated policies. They also check failed-path score inequalities,
path multiplicities, the ratio-barrier identity, the region estimates, and
correct handling of a crossing from an initially zero probe. Finite checks
and ODE diagnostics are not formal verification of the theorems.

## Reproduce the rate experiments

Commands below write new results under `runs/`, leaving retained receipts
untouched. Drivers refuse to overwrite an existing output file.

```sh
OPENBLAS_NUM_THREADS=1 python correction_time.py --output runs/pilot.jsonl
OPENBLAS_NUM_THREADS=1 python correction_time.py --powers 24 32 48 64 96 --output runs/small-diversity.jsonl
OPENBLAS_NUM_THREADS=1 python correction_time.py --powers 32 96 --rtol 2e-11 --method RK45 --output runs/solver-comparison.jsonl
python summarize_correction_time.py
```

The first two commands reproduce thirty runs at L=4,5,6. The third repeats
six runs with a second solver and tighter tolerance. The summary script reads
the dated retained results and regenerates the table and figures in
`output/figures/`. The physical clock is t=exp(s)-1: the solver integrates
in s, rather than taking an enormous number of physical-time steps.

## Other checks

```sh
OPENBLAS_NUM_THREADS=1 python verify_zero_diversity_ray.py --output runs/zero-ray.json
OPENBLAS_NUM_THREADS=1 python verify_tracking.py --output runs/tracking.json
OPENBLAS_NUM_THREADS=1 python transition_model.py --output runs/transition.json
python verify_precision.py --output runs/precision.json
python verify_uniform_bound.py --output runs/uniform-bound.json
python validate_saturation.py
```

The zero-ray check independently counts paths and compares the exact leading
loss coefficient against a high-precision recurrence. The tracking check
compares two flows and checks a Hessian bound. Its normalized-error report
excludes scales below 1e-7, where floating-point subtraction can dominate.
The transition model is an exploratory approximation; its finite-time escape
is not used as a substitute for the full-flow upper-bound proof.

## Build the paper

From `paper/`, with a working TeX installation:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error coin-line-rates.tex
```

## Evidence map

| Claim/check | Source | Retained evidence |
|---|---|---|
| Return and gradient | `model.py` | rational tests in `test_model.py` |
| First correction times | `correction_time.py` | `results/correction-time-pilot-20260919.jsonl`, `results/correction-time-small-eps-20260919.jsonl` |
| Solver comparison | same driver, RK45 | `results/correction-time-validation-20260919.jsonl` |
| 180-digit endpoint gradient checks | `verify_precision.py` | `results/correction-time-precision-20260919.json` |
| Zero-diversity ray diagnostics | `verify_zero_diversity_ray.py` | `results/zero-diversity-ray-20260919.json` |
| Perturbation diagnostics | `verify_tracking.py` | `results/tracking-diagnostics-filtered-20260919.json` |
| Uniform approximation across b=0 | `verify_uniform_bound.py` | `results/uniform-bound-diagnostics-20260919.json` |
| Ratio barrier and region algebra | `test_transition_bound.py` | exact finite arithmetic tests |
| Exploratory transition model | `transition_model.py` | `results/transition-model-two-phase-20260919.json` |

`MANIFEST.json` records SHA256 hashes of the paper, implementation, and
retained evidence. `sources/receipt.json` identifies the pinned model source.
The upstream source and its license are retained under `sources/`.

## Limits

The tests cover specified finite ranges; the paper supplies the general
argument. Numerical integration is not interval-certified. No sharp limiting
prefactor, random-initialization law, discrete-update theorem, or bound on
permanent correction is claimed. The review record distinguishes mathematical
arguments, model reviews, and upstream acceptance.

## Citation and license

Cite Rob Sneiderman, *Correction times for linear policy gradient on a coin
line* (2026). CITATION.cff provides machine-readable metadata.

Code is MIT licensed. The paper, figures and original result data are CC BY
4.0. See [LICENSING.md](LICENSING.md) for scope and upstream attribution.
