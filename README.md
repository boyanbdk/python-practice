# python-practice

Daily Python practice while studying Computer Science at Sofia University (FMI).
Plain Python 3, no dependencies — each file is one self-contained solution.

## Layout

```
coding/          Codewars katas, grouped by rank (8 kyu = easiest → 5 kyu)
  kyu 8/         12 solutions
  kyu 7/         20 solutions
  kyu 6/         18 solutions
  kyu 5/          2 solutions
python hels/     exercises from the University of Helsinki "Python Programming MOOC"
```

Each kata file is named after the problem (`build_tower.py`, `duplicate_encode.py`, …)
and contains the function the kata asks for, e.g.

```python
def tower_builder(n):
    return [(n - i - 1) * " " + (2 * i + 1) * "*" + (n - i - 1) * " " for i in range(n)]
```

## Running

```bash
python3 "coding/kyu 6/build_tower.py"
```

Files with a `__main__` block print sample output; the rest define the function
only — import it or paste it into the Codewars editor.

## Why this exists

Practice log for the fundamentals — strings, lists, dicts, comprehensions, basic
algorithms — as the base for data-engineering and automation work.
