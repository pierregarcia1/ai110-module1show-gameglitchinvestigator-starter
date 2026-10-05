# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] **Describe the game's purpose.** A Streamlit number-guessing game: the app
  picks a secret number in a range set by difficulty (Easy 1–20, Normal 1–100,
  Hard 1–50), and the player guesses until they hit it or run out of attempts.
  Each guess returns a "Too High" / "Too Low" hint and updates a running score.
- [x] **Detail which bugs you found.** The main logic bug: on every even-numbered
  attempt, `main()` passed the secret to `check_guess` as a string instead of an
  int. Comparing an int guess to a str secret raised `TypeError`, dropped into a
  fallback branch, and compared the values as text — so `"9" > "100"` was True and
  the "Higher/Lower" hint came out backwards every other turn.
- [x] **Explain what fixes you applied.** Removed the stringify step so the secret
  is always an int, letting `check_guess` compare numerically. Added a regression
  test (`check_guess(9, 100)` -> "Too Low") that fails on the old behavior and
  passes now.

## 📸 Demo Walkthrough

A sample game, step by step, so a reader can follow along without watching a video:

1. Launch the app with `python -m streamlit run app.py` and leave the difficulty on
   **Normal** (range 1-100, 8 attempts).
2. Expand **Developer Debug Info** to peek at the secret - say it's **42** - so the
   walkthrough is easy to follow.
3. Type `50` and click **Submit Guess**. The hint reads **"Go LOWER!"** because
   50 is above 42. (Before the fix, this second-attempt guess would have lied.)
4. Type `30` and submit. The hint reads **"Go HIGHER!"** - 30 is below 42.
5. Type `42` and submit. The game shows **"Correct!"**, balloons appear, and the
   win banner reports the secret and final score.
6. Click **New Game** to reset the attempt count and draw a fresh secret, then
   repeat from step 2.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
$ python -m pytest test/
platform win32 -- Python 3.12.9, pytest-8.3.3, pluggy-1.5.0
rootdir: C:\Users\pierr\AI110\Module_1\Week2
plugins: anyio-4.15.1
collected 4 items

test\test_game_logic.py ....                                             [100%]

============================== 4 passed in 0.04s ==============================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
