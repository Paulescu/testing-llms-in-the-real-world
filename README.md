<div align="center">
    <a href='https://www.realworldml.xyz/'><img src='./media/rwml_logo.png' width='350'></a>    
</div>

<div align="center">
    <h1>How to test LLM apps in the real-world</h1>
    <h2>with Giskard and MLOps best-practices</h2>
    <img src="./media/diskard_ci_cd.gif" width='550' />
</div>

#### Table of contents
* [The problem](#the-problem)
* [Solution](#solution)
* [Run the whole thing in 5 minutes](#run-the-whole-thing-in-5-minutes)
* [Wanna learn more real-time ML?](#wanna-learn-more-real-time-ml)


## The problem

Large Language Models, like any other ML model are bound to make mistakes, not matter how good they are.

Typical mistakes include:

* hallucinations
* misinformation
* harmfulness, or
* disclosures of sensitive information

And the thing is, these mistakes are no big deal when you are building a demo. 

However, these same mistakes are a deal breaker when you build a production-ready LLM app, that real customers will interact with ❗

Moreover, it is not enough to test for all these things once. Real-world LLM apps, as opposed to demos, are iteratively improved over time. So you need to automatically launch all these tests every time you push a new version of your model source code to your repo.

So the question is:

> Is there an automatic way to test an LLM app, including hallucinations misinformation or harmfulness, before releasing it to the public?

And the answer is … YES!


## Solution

[Giskard](https://github.com/Giskard-AI/giskard) is an open-source testing library for LLMs and traditional ML models.

Giskard provides a scan functionality that is designed to automatically detect a variety of risks associated with your LLMs.

Let me show you how to combine.

* the LLM-testing capabilities of Giskard, with
* CI/CD best-practices

to build an automatic testing workflow for your LLM app.


## Run the whole thing in 5 minutes

1. Install all project dependencies inside an isolated virtual env, using Python Poetry
    ```
    $ make init
    ```

2. Create an `.env` file and fill in the necessary credentials. You will need an OpenAI API Key, and optionally a few Giskard Hub and HF credentials if you plan to use the Giskard Hub.
    ```
    $ cp .env.example .env
    ```

3. Make a change in the `hyper-parameters.yaml` file, for example update the `PROMPT_TEMPLATE`, commit your changes, push them to your remote GitHub repo and open a Pull request.

4. Check the Actions pannel in your GitHub repo, and see the testing happening!

5. Once the action completed, check the PR discussion to see the testing results, and decide if you want to merge with master, or not.

## Video lecture

🔜 Coming soon!

## Wanna learn more real-time LLMOps?

Join more than 10k subscribers to the Real-World ML Newsletter. Every Saturday morning.

[👉🏽 Click to subscribe](https://www.realworldml.xyz/subscribe)