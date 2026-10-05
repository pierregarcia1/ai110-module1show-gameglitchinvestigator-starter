# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| | | | |
| | | | |
| | | | |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.

I used Claude Code as my AI teammate.

**Correct suggestion I accepted:** The AI found that `main()` was stringifying the
secret on even attempts (`secret = str(st.session_state.secret)`), which made
`check_guess` compare an int guess against a str secret. The `>` raised a
`TypeError`, fell into the fallback branch, and compared the numbers as text, so
`"9" > "100"` was True and the hint came out backwards every other turn. The
suggestion was to always pass the int secret. This fix worked on the first
attempt — there was no wrong suggestion to reject. I verified it with pytest
(see Section 3).

**Suggestion I did not accept as written:** `check_guess` already carried an AI-added
`try/except TypeError` fallback that stringifies both values and re-compares them.
I kept the fix out of that fallback instead of leaning on it: the defensive
stringify is over-engineered and is exactly what masked the real bug, so patching
there would have hidden the root cause rather than removing it. I changed the fix
to live at the source (always pass an int) and left the function to compare
numbers directly, which I confirmed with the `check_guess(9, 100)` test.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I decided a bug was really fixed when a test that reproduces the broken behavior
passes with the fix and would fail without it. I added
`test_numeric_comparison_not_lexicographic` to `test/test_game_logic.py`, which
calls `check_guess(9, 100)` and asserts the outcome is "Too Low" with a "HIGHER"
hint. This directly targets the bug: with the old str secret, `"9" > "100"` is
True and the function returned "Too High", so the test pins the numeric-comparison
behavior. Running `python -m pytest test/test_game_logic.py -q` reported
`4 passed`, including the three existing regression tests. The AI helped by
explaining why lexicographic string comparison produced the wrong hint and by
writing the test so its assertion fails on exactly the buggy input.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
