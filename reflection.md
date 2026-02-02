# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

The hint messages were unreliable; when I guessed higher than the secret number, the game sometimes gave misleading guidance instead of clearly telling me to go lower or higher. I also had to manually refresh the browser every time I wanted to start a new game, which made the game feel broken. In addition, the UI always said “Guess a number between 1 and 100” even when I selected Easy or Hard difficulty, so the difficulty setting was not reflected correctly.

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  --- I used COPILOT and GPT 5-mini
- Give one example of an AI suggestion you accepted and why.
- Give one example of an AI suggestion you changed or rejected and why.

I used GitHub Copilot and ChatGPT (GPT-5-mini) as AI tools during this project. One AI suggestion I accepted was using (st.session_state) together with (st.rerun()) to fix issues where the UI did not update immediately after a guess or when starting a new game. This suggestion worked because it matched how Streamlit reruns scripts and helped keep the interface in sync with updated state. One AI suggestion I changed was related to scoring logic; the original AI logic produced off-by-one errors, so I adjusted the math myself to ensure a first-try win correctly awarded 100 points.

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.

I decided a bug was fixed when both the game behavior matched expectations and the automated tests passed. I manually tested the game by playing multiple rounds, changing difficulty levels, and observing whether attempts, hints, and scores updated correctly without refreshing the page. Running one of the unit tests showed my scoring logic was off. It also showed the hint messages were wrong.

- Did AI help you design or understand any tests? How?

Yes, AI helped create tests for updating the score. It designed the test using various cases and I was able to run them and make sure I got the expected test result.

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

The secret number kept changing in the original app because Streamlit reruns the entire script on every interaction, and the secret was being regenerated without proper state protection. The key change that fixed this issue was storing the secret in st.session_state and only resetting it intentionally when starting a new game or changing difficulty.

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

One strategy from this projectn I want to reuse is working on one problem at a time and commiting and pushing my changes as I go. It keeps an organized structure and helps keep track of the order you're making changes. Something I would do differently is maybe exploring different options the AI agent could give and weighing pros and cons of both. Overall, this project made me realize that human eyes are necessary to look through AI generated code because little bugs and logic errors can screw the whole proejct if not checked.
