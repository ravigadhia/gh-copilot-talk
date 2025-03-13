---
theme: seriph
background: >-
  https://github.com/LadyKerr/mealmetrics-copilot/assets/47188731/fbeeed3f-7a00-4b01-90a5-a4ea495a0f1c
title: Code Smarter not Harder with GitHub Copilot
favicon: ''
font: Playfair Display
layout: cover
lineNumbers: true
transition: fade
record: dev
download: true
exportFilename: gh-copilot-101-bootcamp
export:
  format: pdf
  timeout: 30000
  dark: false
  withClicks: false
---



<!--
Hello good afternoon! Thank you all for being here with me today to learn how to GitHub Copilot to build. I'm Kedasha and I'm so excited that you're here with me today.
-->

---
layout: image-right
image: https://github.com/LadyKerr/mealmetrics-copilot/assets/47188731/7d0e2430-c5c9-483a-b8eb-afcda71e80f8
transition: fade-out
---

# Hi! I'm Kedasha!

- Jamaican gyal! 🇯🇲
- Developer Advocate at GitHub
- Software Engineer for 5 years
- Technical Content Creator ✨
- Bootcamp Grad 🎓
- Completely obsessed with Apple juice 🍎🥤

<br>

I love, love, love creating technical content on Instagram, Tiktok and sometimes Twitter. 

**Find me online @itsthatladydev**

<style>
h1 {
  background-color: #E81CFF;
  background-image: linear-gradient(45deg, #40C9FF 10%, #E81CFF 20%);
  background-size: 100%;
  -webkit-background-clip: text;
  -moz-background-clip: text;
  -webkit-text-fill-color: transparent;
  -moz-text-fill-color: transparent;
}
</style>

<!--

I'm Kedasha Kerr and Im a Developer Advocate at GitHub. 

This time 5 years ago I was in the process of transitioning into tech from a career as a social worker. I've been a software engineer for 5 years and much like many of you, Im a bootcamp grad. I'm also a technical content creator and I love creating content on Instagram, Tiktok and Linkedin.

I know that AI has been the most used buzz word in the tech industry for the oast few years and sometimes we may have the expectation that the AI tool we're implenting will do all the work for us. But just as we need to learn how to use a new framework or library, we also need to learn how to make AI tools work for us to get the results that we need. 

Today, I'll be sharing some pragmatic ways to get the most out of GitHub Copilot during your day to day development.
-->

---
layout: intro
transition: fade-out
---

# What we'll cover:

- What is GitHub Copilot?
- Features of GitHub Copilot
- How does it work?
- Access & Installation
- Demos
- Q&A

<style>
h1 {
  background-color: #E81CFF;
  background-image: linear-gradient(45deg, #40C9FF 10%, #E81CFF 20%);
  background-size: 100%;
  -webkit-background-clip: text;
  -moz-background-clip: text;
  -webkit-text-fill-color: transparent;
  -moz-text-fill-color: transparent;
}
</style>

<!--
Today we'll walk through:
What GitHub Copilot is
Its key features
How it works behind the scenes
How to get access and install it
Live demos
And plenty of time for Q&A

Here's what fascinates me about Copilot: while it's made headlines as an AI coding assistant, what many don't realize is that it's revolutionizing how we work with all kinds of content. Whether you're writing documentation, building your next startup, or managing projects, Copilot has surprising capabilities that can make your work more efficient and creative. Today, I'll show you how Copilot can be your ally, regardless of your role or technical background. My goal is for you to leave with practical tips you can start using immediately.
-->

---
transition: fade-out
---

# What is GitHub Copilot?

### GitHub Copilot is an AI pair programmer that helps you write code faster.

<br> 

<img src="https://github.com/LadyKerr/mealmetrics-copilot/assets/47188731/b3b0193f-913f-49b3-860e-9659db72a348" alt="GitHub Copilot" width="100%"/>

<style>
h1 {
  background-color: #40C9FF;
  background-image: linear-gradient(45deg, #40C9FF 10%, #E81CFF 20%);
  background-size: 100%;
  -webkit-background-clip: text;
  -moz-background-clip: text;
  -webkit-text-fill-color: transparent;
  -moz-text-fill-color: transparent;
}
</style>

<!--

But first, what is GitHub Copilot? :thinking:

Just in case you didn't know, GitHub Copilot is an AI pair programmer that helps you write code faster. It is designed to help with programming tasks and serves as your assistant while you're working in your IDE.

GitHub Copilot is comprised of a suite of products that goes beyond code completion.

Some of the tools that accompany GitHub Copilot includes a chat interface that you can use in your IDE, a command line tool via a GitHub CLI extension, GitHub Copilot for PRs, Copilot Edits that allows you to make Multi file changes, Copilot integrated into dotcom and many more. Today, we'll be looking at a few of the features that I've found to be most useful during my everyday development.

-->


---
transition: fade-out
---

# Installation and Availability

### You can use GitHub Copilot in your IDE. 
### It is available in VSCode, Neovim, Jetbrain IDE and Visual Studio.

<br>

![various-ide-copilot](https://github.com/LadyKerr/mealmetrics-copilot/assets/47188731/e39af215-9314-4524-8c23-eb3e0b280308)

![lprogramming-langauges](https://github.com/LadyKerr/mealmetrics-copilot/assets/47188731/94e3f958-bb51-4b47-b698-f6da3a992483)


<style>
h1 {
  background-color: #40C9FF;
  background-image: linear-gradient(45deg, #40C9FF 10%, #E81CFF 20%);
  background-size: 100%;
  -webkit-background-clip: text;
  -moz-background-clip: text;
  -webkit-text-fill-color: transparent;
  -moz-text-fill-color: transparent;
}
</style>

<!--
To install it you'll go to your respective marketplaces for your IDE and install the extension. Once it's installed you'll need to authenticate with your GitHub account. and if you have accesss, you'll be able to use GitHub Copilot in your IDE.

You can use it in VSCode, Neovim, Jetbrain IDE and Visual Studio and more. Most of the features we'll be looking at today is available in VSCode.

And it works with many languages - especially open source languages like javascript, typescript, python, java, python, go, ruby, and more.
-->

---
transition: fade-out
---

# Beyond the Editor

### You can use GitHub Copilot on GitHub dotcom! 
### Talk to your repos, create docs, draft PRs, get code reviews, inquire about issues and more.

<br>

![copilot-chat-dotcom](https://github.com/user-attachments/assets/8761ef7f-4329-4036-b263-621633e4204a)


<style>
h1 {
  background-color: #40C9FF;
  background-image: linear-gradient(45deg, #40C9FF 10%, #E81CFF 20%);
  background-size: 100%;
  -webkit-background-clip: text;
  -moz-background-clip: text;
  -webkit-text-fill-color: transparent;
  -moz-text-fill-color: transparent;
}
</style>

<!--
Beyond IDEs, Copilot is integrated right into GitHub.com. You can use it to talk to your repositories, create documentation, draft pull requests, and get insights about issues
-->


---
transition: fade-out
---

# Features of GitHub Copilot

- Code Complete (inline suggestions)
- Copilot Chat (inline and chat box)
- Copilot Chat on Mobile!
- Copilot in the CLI
- Copilot PR Summaries (ent)
- Copilot Knowledge bases (ent)
- Copilot Autofix for CodeQL
- Copilot Edits (multi file changes)
- Copilot Agent mode (preview)

![subscribe-rss-feed-copilot](https://github.com/user-attachments/assets/d8a59971-e365-435e-824d-bfbfe21afd9f)

<!--
GitHub Copilot is comprised of a suite of products that goes beyond code completion.

Some of the tools that accompany GitHub Copilot includes a chat interface that you can use in your IDE, a command line tool via a GitHub CLI extension, GitHub Copilot for PRs, Copilot integrated into dotcom and many more. Today, we'll be looking at a few of the features that I've found to be most useful during my everyday development.


-->

<style>
h1 {
  background-color: #E81CFF;
  background-image: linear-gradient(45deg, #40C9FF 10%, #E81CFF 20%);
  background-size: 100%;
  -webkit-background-clip: text;
  -moz-background-clip: text;
  -webkit-text-fill-color: transparent;
  -moz-text-fill-color: transparent;
}
</style>

<!--
Copilot comes with a powerful suite of features:

Code completion with inline suggestions
Copilot Chat for conversations about your code
Mobile access, if you havent download the mobile app
GitHub CLI integration
multi model chat interface
Copilot in your terminals
PR summaries for enterprise users
Knowledge bases
Extensions in public beta
And automated fixes for CodeQL
Copilot Edits for multi file changes
Copilot Agent mode to build even faster (currently in preview)
-->


---
transition: fade-out
---

# What is GitHub Copilot good for?

- 🛠️ Boilerplate code and frameworks
- 🤷🏽‍♀️ Uncommon or confusing syntax
- 🔗 Pattern matching
- 👨🏽‍💻 Writing code faster
- ⛓️ Building entire features
- 👀 Helping you remember things you forgot
- 💻 Extending and refactoring existing code
- 🔖 Explaining unfamiliar code
- 📝 Documentation (which we all love to write!)
- 🚨 Understandiing error messages (and fixing it!)
- 🧪 Writing unit tests

. . . and much more! 🚀

<style>
h1 {
  background-color: #40C9FF;
  background-image: linear-gradient(45deg, #40C9FF 10%, #E81CFF 20%);
  background-size: 100%;
  -webkit-background-clip: text;
  -moz-background-clip: text;
  -webkit-text-fill-color: transparent;
  -moz-text-fill-color: transparent;
}
</style>

<!--
Now what is GitHub Copilot good for?

Many things! Some of what it's best at is . . .
-->


---
transition: fade-out
layout: center
---

![life-of-a-completion](https://github.com/user-attachments/assets/b4184921-7699-45ca-bed9-9f7244f98aaa)

<style>
h1 {
  background-color: #40C9FF;
  background-image: linear-gradient(45deg, #40C9FF 10%, #E81CFF 20%);
  background-size: 100%;
  -webkit-background-clip: text;
  -moz-background-clip: text;
  -webkit-text-fill-color: transparent;
  -moz-text-fill-color: transparent;
}
</style>

<!--
behind the scenes.
Copilot returns suggestions to your editor where you choose what to accept or ignore.

KEY THING TO REMEMBER it will no act agentically for you.
GitHub Copilot shares data in an ephemeral way. It’s shared just long enough for GitHub Copilot to provide a suggestion. We do not take that code and put it back into the data model.

The Technical Flow:

Context Collection:
Analyzes your current file, open tabs, and file structure
Captures code before and after your cursor position
Maps relevant dependencies and patterns


Prompt Formation:
Uses a "Fill-in-the-Middle" approach with prefix and suffix text
Prioritizes local context using the Prompt Library
Structures data into an AI-optimized format

AI Processing:
Runs your context through a filter model for appropriateness and quality
Feeds filtered prompt to a GPT model trained on code
Generates multiple code completions in parallel

Suggestion Delivery:
Returns the highest-quality completions to your editor
Processes code temporarily - doesn't store your code in training data
Presents suggestions as you type, with no action required

Key Technical Point:
Copilot doesn't just match patterns - it understands code semantics and can generate novel solutions based on your specific context.
-->

---
transition: fade-out
---

# Some Limitations of GitHub Copilot 

- GitHub copilot != Compiler
- It cannot read your mind - you need to provide as much context as possible 
- It is not a replacement for good coding practices 

<style>
h1 {
  background-color: #40C9FF;
  background-image: linear-gradient(45deg, #40C9FF 10%, #E81CFF 20%);
  background-size: 100%;
  -webkit-background-clip: text;
  -moz-background-clip: text;
  -webkit-text-fill-color: transparent;
  -moz-text-fill-color: transparent;
}
</style>

<!--
It cannot read minds, although it sometimes feels like it can. It’s not a compiler, and it’s not a replacement for good coding practices. Actually if you have bad coding practices this will be more apparent when you use the AI because it uses the patterns in your code to give you suggestions.

This means, if you have bad coding practices, you’ll get bad suggestions. So it’s important to keep that in mind when you’re using it.

Also, one of the most important points I want to drive home today is that - GitHub Copilot is a tool that can help you write code faster, and it’s up to you to decide how to use it. 

It is not here to do your work for you or to write everything for you. It will guide you and nudge you in the right direction just as a coworker would if you asked them questions or for guidance on a particular issue.

-->

---
transition: fade-out
---

# Best Practices for Using GitHub Copilot

- 👀 Review all generated code carefully
- 🧩 Break down complex tasks into smaller chunks
- 📝 Write clear comments and provide good context
- 💬 Use Copilot Chat when you need explanations
- 🔨 Combine Copilot with your expertise
- 🚀 Start simple and gradually explore advanced features

<style>
h1 {
  background-color: #E81CFF;
  background-image: linear-gradient(45deg, #40C9FF 10%, #E81CFF 20%);
  background-size: 100%;
  -webkit-background-clip: text;
  -moz-background-clip: text;
  -webkit-text-fill-color: transparent;
  -moz-text-fill-color: transparent;
}
</style>

<!--

Think of GitHub Copilot like a skilled apprentice working alongside you - eager to help but needing proper guidance to be most effective.

* 👀 **Quality Control Matters**: Always review generated code carefully. Like any collaborative work, verification is key to maintaining quality and security.

* 🧩 **Divide and Conquer**: Complex problems become manageable when broken down. Feed Copilot smaller, well-defined tasks rather than massive, ambiguous ones.

* 📝 **Clear Communication**: The better your comments and context, the more relevant Copilot's suggestions. Good input leads to good output.

* 💬 **Leverage the Dialog**: Use Copilot Chat when you need deeper understanding. It's like having a senior developer available for quick consultations.

* 🔨 **Combine Forces**: Let Copilot enhance your expertise, not replace it. Your knowledge and judgment remain essential.

* 🚀 **Progressive Learning**: Start with basic features and gradually explore more advanced capabilities as you become comfortable.

Remember: Copilot adapts to your coding patterns - both good and bad. If you write unclear or inefficient code, Copilot will learn and suggest similar patterns. Think of it as a mirror reflecting your own coding practices.

Copilot is designed to augment your development process, not take it over. It's a sophisticated tool that works best when guided by your expertise and judgment. Like any good assistant, it helps you work more efficiently while leaving the important decisions in your hands.

The key is understanding that Copilot is part of your development toolkit - a powerful one, but still just a tool. You're the developer, the decision-maker, and the one responsible for the final code. Use Copilot to enhance your capabilities, not replace your critical thinking.  # Best Practices for Effective Use of GitHub Copilot

-->

---
layout: center
transition: fade-out
---
# Let's do some demos!

> 🔗 Repo Link: [gh.io/task-manager](https://gh.io/task-manager)

<style>
h1 {
  background-color: #E81CFF;
  background-image: linear-gradient(45deg, #40C9FF 10%, #E81CFF 20%);
  background-size: 100%;
  -webkit-background-clip: text;
  -moz-background-clip: text;
  -webkit-text-fill-color: transparent;
  -moz-text-fill-color: transparent;
}
</style>

<!---
Demo repo: https://gh.io/task-manager

-->

---
transition: fade-out
layout: center
---

# Questions?

<style>
h1 {
  background-color: #40C9FF;
  background-image: linear-gradient(45deg, #40C9FF 10%, #E81CFF 20%);
  background-size: 100%;
  -webkit-background-clip: text;
  -moz-background-clip: text;
  -webkit-text-fill-color: transparent;
  -moz-text-fill-color: transparent;
}
</style>
---
transition: fade-out
---

# Resources

- [Getting Started with GitHub copilot - video](https://www.youtube.com/watch?v=n0NlxUyA7FI)
- [Getting Started with GitHub Copilot - blog](https://github.blog/ai-and-ml/github-copilot/github-for-beginners-how-to-get-started-with-github-copilot/)
- [Coding with an AI Pair Programmer - video](https://youtu.be/dhfTaSGYQ4o?si=wdhu3C7uwG5cqX0K)
- [Using GitHub Copilot in your IDE - best practices](https://github.blog/developer-skills/github/how-to-use-github-copilot-in-your-ide-tips-tricks-and-best-practices/)
- [How to use GitHub Copilot: Prompts, tips, and use cases](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/)
- [Prompting GitHub Copilot Chat to become your personal AI assistant for accessibility](https://github.blog/2023-10-09-prompting-github-copilot-chat-to-become-your-personal-ai-assistant-for-accessibility/)

<br>
<br>

Kedasha Kerr | @itsthatladydev
<br>
Find me on all socials!

<style>
h1 {
  background-color: #40C9FF;
  background-image: linear-gradient(45deg, #40C9FF 10%, #E81CFF 20%);
  background-size: 100%;
  -webkit-background-clip: text;
  -moz-background-clip: text;
  -webkit-text-fill-color: transparent;
  -moz-text-fill-color: transparent;
}
</style>
